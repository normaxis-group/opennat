# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 7 de l'édition complète : schéma XSD, dictionnaire des données et exemple validé du RSNat."""
import os

from lxml import etree

from commun import EDITION, RACINE, ecrire, tableau
from rsnat_spec import ENUMS, RACINE as RSNAT, E

XS = 'http://www.w3.org/2001/XMLSchema'
BASE = {'texte': 'xs:string', 'decimal': 'xs:decimal', 'entier': 'xs:integer', 'booleen': 'xs:boolean',
        'date': 'xs:date'}
NOMS_TYPES = {'texte': 'texte', 'decimal': 'nombre décimal', 'entier': 'entier', 'booleen': 'booléen',
              'date': 'date'}


def xs(tag, **att):
    el = etree.Element(f'{{{XS}}}{tag}')
    for k, v in att.items():
        el.set(k, str(v))
    return el


def construire_xsd():
    racine = etree.Element(f'{{{XS}}}schema', nsmap={'xs': XS})
    racine.set('elementFormDefault', 'qualified')
    doc = xs('annotation')
    d = etree.SubElement(doc, f'{{{XS}}}documentation')
    d.text = ('Récapitulatif standardisé RSNat (nom provisoire) de la méthode OpenNAT, version 1. '
              'NORMATYS, CC BY 4.0. Généré par outils/edition/partie7_rsnat.py.')
    racine.append(doc)
    for nom, valeurs in ENUMS.items():
        st = xs('simpleType', name=nom)
        r = etree.SubElement(st, f'{{{XS}}}restriction', base='xs:string')
        for v in valeurs:
            etree.SubElement(r, f'{{{XS}}}enumeration', value=v)
        racine.append(st)

    def element(noeud):
        att = {'name': noeud.nom}
        if noeud.min != 1:
            att['minOccurs'] = noeud.min
        if noeud.max != 1:
            att['maxOccurs'] = noeud.max
        if isinstance(noeud, E):
            el = xs('element', **att)
            ann = etree.SubElement(el, f'{{{XS}}}annotation')
            etree.SubElement(ann, f'{{{XS}}}documentation').text = noeud.description
            ct = etree.SubElement(el, f'{{{XS}}}complexType')
            seq = etree.SubElement(ct, f'{{{XS}}}sequence')
            for enf in noeud.enfants:
                seq.append(element(enf))
            return el
        att['type'] = BASE.get(noeud.type, noeud.type)
        el = xs('element', **att)
        ann = etree.SubElement(el, f'{{{XS}}}annotation')
        etree.SubElement(ann, f'{{{XS}}}documentation').text = (
            noeud.description + (f' ({noeud.unite})' if noeud.unite else ''))
        return el

    racine.append(element(RSNAT))
    return etree.ElementTree(racine)


def dictionnaire():
    out = []
    compteur = [0]

    def parcourir(noeud, chemin):
        if not isinstance(noeud, E):
            return
        compteur[0] += 1
        p = f'{chemin}/{noeud.nom}' if chemin else noeud.nom
        lignes = []
        for enf in noeud.enfants:
            card = f'{enf.min}..{"n" if enf.max == "unbounded" else enf.max}'
            if isinstance(enf, E):
                lignes.append([enf.nom, 'élément composé', '', card, enf.description, ''])
            else:
                typ = NOMS_TYPES.get(enf.type, 'énumération : ' + ', '.join(ENUMS.get(enf.type, [])))
                lignes.append([enf.nom, typ, enf.unite, card, enf.description, enf.origine])
        out.extend([f'#### 7.3.{compteur[0]} `{p}`', '', noeud.description + '.', '',
                    tableau(['Élément', 'Type', 'Unité', 'Card.', 'Description', 'Origine'], lignes), ''])
        for enf in noeud.enfants:
            parcourir(enf, p)

    parcourir(RSNAT, '')
    return out


def exemple():
    """RSNat de l'exemple de l'annexe C de la partie 1, réduit aux éléments obligatoires et aux résultats."""
    def sub(parent, nom, texte=None):
        el = etree.SubElement(parent, nom)
        if texte is not None:
            el.text = str(texte)
        return el

    r = etree.Element('RSNat')
    for k, v in (('version_methode', 'OpenNAT 1'), ('version_donnees', 'exemple'), ('graine', 20261018),
                 ('date_calcul', '2026-10-18')):
        sub(r, k, v)
    ent = sub(r, 'Entree_Projet')
    p = sub(ent, 'Projet')
    for k, v in (('identifiant', 'EX-ANNEXE-C'), ('nom', 'Résidence sur friche urbaine'),
                 ('zone_biogeographique', 'continentale'), ('departement', '78'), ('zone_climatique', 'H1a'),
                 ('texture_sol', 'limon'), ('profondeur_sol', 1.0), ('annee_debut_chantier', 2027),
                 ('mois_debut_chantier', 9), ('mois_destruction', 9), ('plan_gestion_annees', 10),
                 ('typologie', 'logement'), ('date_etude', '2026-10-18')):
        sub(p, k, v)
    par = sub(ent, 'Parcelle')
    sub(par, 'surface', 2000)
    bc = sub(ent, 'Batiment_Collection')
    b = sub(bc, 'Batiment')
    for k, v in (('index', 1), ('sref', 1400), ('emprise_au_sol', 700), ('duree_chantier', 18)):
        sub(b, k, v)
    gc = sub(b, 'Ges_Collection')
    for ph, v in (('A1-A3', 350), ('A4-A5', 120), ('B', 400), ('C', 55), ('D', -40)):
        g = sub(gc, 'Ges')
        sub(g, 'phase', ph)
        sub(g, 'valeur', v)
    tc = sub(ent, 'Tache_Collection')
    for t in ('P1', 'P2', 'P3'):
        tt = sub(tc, 'Tache')
        sub(tt, 'identifiant', t)
        sub(tt, 'connexion', 'faible')
        sub(tt, 'cloture', 'aucune')
    ei = sub(ent, 'Etat_Initial')
    uc = sub(ei, 'Unite_Collection')

    def unite(parent, ident, code, pos, surf, tache=None, statut=None, criteres=(), **autres):
        u = sub(parent, 'Unite')
        sub(u, 'identifiant', ident)
        sub(u, 'code_habitat', code)
        sub(u, 'position', pos)
        sub(u, 'surface', surf)
        for k in ('epaisseur_substrat', 'classe_diametre', 'stade'):
            if k in autres:
                sub(u, k, autres[k])
        if tache:
            sub(u, 'tache', tache)
        if 'eclairage' in autres:
            sub(u, 'eclairage', autres['eclairage'])
        if statut:
            sub(u, 'statut', statut)
        if 'protection_chantier' in autres:
            sub(u, 'protection_chantier', autres['protection_chantier'])
        if criteres:
            cc = sub(u, 'Critere_Collection')
            for code_c, rep in criteres:
                c = sub(cc, 'Critere')
                sub(c, 'code', code_c)
                sub(c, 'reponse', rep)
        return u

    unite(uc, 'U0-1', 'VB.8', 'sol_pleine_terre', 1200, 'P1', criteres=[
        ('A', 'oui'), ('B', 'oui'), ('C', 'non'), ('D', 'oui'), ('E1', 'sans_objet'), ('E2', 'sans_objet'),
        ('F', 'sans_objet'), ('G', 'sans_objet')])
    unite(uc, 'U0-2', 'VB.2', 'sol_pleine_terre', 600)
    unite(uc, 'U0-3', 'VB.9', 'sol_pleine_terre', 200, 'P1', criteres=[
        ('A', 'oui'), ('B', 'non'), ('C', 'oui'), ('D', 'non'), ('E', 'non')])
    unite(uc, 'U0-4', 'VB.18a', 'arbre', 100, 'P1', stade='M', classe_diametre='moyen', criteres=[
        ('A', 'oui'), ('B', 'oui'), ('C', 'non'), ('D', 'oui'), ('E', 'oui'), ('F', 'oui')])
    vc = sub(ent, 'Variante_Collection')
    v = sub(vc, 'Variante')
    sub(v, 'index', 1)
    sub(v, 'nom', 'Projet de référence')
    sub(v, 'reference', 'true')
    uc = sub(v, 'Unite_Collection')
    unite(uc, 'U1-1', 'VB.1', 'sol_pleine_terre', 700, statut='creee')
    unite(uc, 'U1-2', 'VB.2', 'sol_pleine_terre', 300, statut='creee')
    unite(uc, 'U1-3', 'VB.3', 'sol_pleine_terre', 150, statut='creee')
    unite(uc, 'U1-4', 'VB.26', 'sol_pleine_terre', 450, 'P2', 'creee', eclairage='L1')
    unite(uc, 'U1-5', 'VB.7', 'sol_pleine_terre', 320, 'P2', 'creee')
    unite(uc, 'U1-6', 'FA.3', 'lineaire', 80, 'P2', 'creee', stade='M')
    unite(uc, 'U1-7', 'VB.18a', 'arbre', 100, 'P2', 'conservee', stade='M', protection_chantier='true')
    unite(uc, 'U1-8', 'VB.12', 'hors_sol_toiture', 500, 'P3', 'creee', epaisseur_substrat=15)
    bo = sub(v, 'Bois_Collection')
    bb = sub(bo, 'Bois')
    sub(bb, 'regime', 'coupe_rase')
    sub(bb, 'volume', 30)
    gr = sub(v, 'Granulats')
    sub(gr, 'masse', 1800)

    so = sub(r, 'Sortie_Projet')
    vr = sub(so, 'Variante_Resultat')
    sub(vr, 'index', 1)
    c = sub(vr, 'Contexte')
    for k, val in (('part_emprise', 0.35), ('bnat_min', 45), ('pleine_terre_min', 0.15),
                   ('multiplicateur_delai', 1)):
        sub(c, k, val)
    fc = sub(vr, 'Fermeture_Collection')
    for etat in ('initial', 'projet'):
        f = sub(fc, 'Fermeture')
        for k, val in (('etat', etat), ('somme', 2000), ('ecart', 0), ('conforme', 'true')):
            sub(f, k, val)
    sub(vr, 'Unite_Resultat_Collection')
    import sys as _s
    _s.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import carnet_reference as CR
    from cas_validation import ANNEXE_C
    rc = CR.calculer(ANNEXE_C)
    r1 = lambda x: round(x, 1)
    s = sub(vr, 'Site')
    for k, val in (('valeur_initiale', r1(rc['v0'])), ('i0', r1(rc['i0'])), ('i1', r1(rc['i1'])),
                   ('i0_30', r1(rc['i0_30'])), ('i1_30', r1(rc['i1_30'])), ('dette_maturite', r1(rc['dm'])),
                   ('supplement_destruction', r1(rc['faune'])), ('arrosage_annuel', r1(rc['arrosage_m3_an'])),
                   ('rang_plantation', 17), ('annees_periode', f"{rc['annees'][0]} {rc['annees'][-1]}"),
                   ('trajectoire_reference', ' '.join(f'{x:.1f}' for x in rc['ref'])),
                   ('trajectoire_site', ' '.join(f'{x:.1f}' for x in rc['site'])),
                   ('pleine_terre', round(rc['pt'], 3)), ('pleine_terre_initiale', round(rc['pt0'], 3)),
                   ('impermeable_initial', r1(rc['aimp0'])), ('impermeable_projet', r1(rc['aimp1'])),
                   ('impermeabilisation_nette', r1(rc['aimp1'] - rc['aimp0']))):
        sub(s, k, val)
    m = sub(vr, 'Materiaux')
    for k, val in (('facteur_climat', rc['mat']['CF']), ('inat_climat', r1(rc['mat']['inat_clim'])),
                   ('inat_bois', r1(rc['mat']['inat_bois'])), ('inat_carrieres', r1(rc['mat']['inat_carr']))):
        sub(m, k, val)
    ind = sub(vr, 'Indicateurs')
    for k, val in (('cnat', r1(rc['cnat'])), ('cnat_moyen', r1(rc['cnat'] / 50)),
                   ('cnat_relatif', round(rc['cnat_rel'], 3)), ('cnat_30', r1(rc['cnat_30'])),
                   ('inat', r1(rc['inat'])), ('snat', r1(rc['snat'])), ('bnat', r1(rc['bnat'])),
                   ('cbs', round(rc['bnat'] / 100, 3)), ('cnat_par_m2_parcelle', round(rc['cnat'] / 2000, 3)),
                   ('inat_par_m2_sref', r1(rc['inat'] / 1400))):
        sub(ind, k, val)
    co = sub(vr, 'Conformite')
    for k, val in (('bnat_conforme', 'true'), ('pleine_terre_conforme', 'true'), ('niveau_cnat', 0)):
        sub(co, k, val)
    ap = sub(r, 'Attestation_Permis')
    for k, val in (('variante', 1), ('bnat', 59.0), ('bnat_min', 45), ('pleine_terre', 0.425),
                   ('pleine_terre_min', 0.15), ('conforme', 'true')):
        sub(ap, k, val)
    em = sub(r, 'Empreinte')
    sub(em, 'entrees', 'exemple')
    sub(em, 'sorties', 'exemple')
    return etree.ElementTree(r)


def exemple_moteur():
    """RSNat de l'exemple de l'annexe C produit par le moteur (calcul aux valeurs centrales)."""
    import datetime as dt
    import sys
    sys.path.insert(0, RACINE)
    from opennat import chaine, projet, recapitulatif
    from opennat.donnees import Parametres, Tables
    T = Tables()
    P = Parametres(T)
    e, _ = projet.normaliser(P, projet.lire(os.path.join(RACINE, 'banc', 'cas', 'exemple_de_l_annexe_c.json')))
    e['projet']['date_etude'] = '2026-10-18'
    res = [chaine.calculer(P, e, v, []) for v in e['variantes']]
    return recapitulatif.construire(e, res, {}, T.empreinte, '2026-10-18')


def dictionnaire_projet():
    """Dictionnaire du fichier projet, lu dans schemas/projet.schema.json."""
    import json
    with open(os.path.join(RACINE, 'schemas', 'projet.schema.json'), encoding='utf-8') as f:
        sch = json.load(f)
    lignes = []

    def typ(x):
        if '$ref' in x:
            return 'voir ' + x['$ref'].split('/')[-1]
        if 'enum' in x:
            return 'un de : ' + ', '.join(str(v) for v in x['enum'])
        if 'const' in x:
            return f'« {x["const"]} »'
        if 'oneOf' in x:
            return ' ou '.join(typ(y) for y in x['oneOf'])
        t = x.get('type', '')
        t = ' ou '.join(t) if isinstance(t, list) else t
        return {'object': 'objet', 'array': 'liste', 'string': 'texte', 'number': 'nombre', 'integer': 'entier',
                'boolean': 'booléen'}.get(t, t)

    def parcourir(x, chemin, requis):
        for k, y in x.get('properties', {}).items():
            c = f'{chemin}.{k}' if chemin else k
            lignes.append([f'`{c}`', typ(y), 'oui' if k in requis else '', y.get('description', '')])
            if y.get('type') == 'object' and 'properties' in y:
                parcourir(y, c, y.get('required', []))
    parcourir(sch, '', sch['required'])
    out = [tableau(['Champ', 'Type', 'Obligatoire', 'Remarque'], lignes), '']
    for nom, d in sch['$defs'].items():
        ls = []
        for k, y in d.get('properties', {}).items():
            ls.append([f'`{k}`', typ(y), 'oui' if k in d.get('required', []) else '', y.get('description', '')])
        if not ls:
            ls = [['', typ(d), '', '']]
        out += [f'#### Définition `{nom}`', '', tableau(['Champ', 'Type', 'Obligatoire', 'Remarque'], ls), '']
    return out


def main():
    import json
    import sys
    sys.path.insert(0, RACINE)
    from opennat import rsnat
    rsnat.ecrire_schemas()
    schemas = os.path.join(RACINE, 'schemas')
    chemin_xsd = os.path.join(schemas, 'rsnat.xsd')
    xsd = etree.parse(chemin_xsd)
    d = exemple_moteur()
    el = rsnat.vers_xml(d)
    err = rsnat.valider_xml(el)
    doc = rsnat.vers_json(d)
    err_j = rsnat.valider_json(doc)
    if err or err_j:
        print(err, err_j)
        raise SystemExit(1)
    ex = etree.ElementTree(el)
    ex.write(os.path.join(schemas, 'exemple_annexe_C.rsnat.xml'), pretty_print=True, xml_declaration=True,
             encoding='UTF-8')
    with open(os.path.join(schemas, 'exemple_annexe_C.rsnat.json'), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    valide = True
    n_el = len(xsd.getroot().findall(f'.//{{{XS}}}element'))
    out = ['## Partie 7. Récapitulatif standardisé RSNat et fichier projet', '',
           'Le RSNat (nom provisoire) est au calcul OpenNAT ce que le RSEE est à l\'étude RE2020 : un fichier XML qui '
           'porte les données d\'entrée, les résultats et les attestations, validé par un schéma XSD publié avec la '
           'méthode, accompagné de sa copie JSON validée par un schéma JSON. Sa structure reprend celle du RSEE : un '
           'bloc d\'entrée, un bloc de sortie, et ici deux blocs d\'attestation. Le moteur l\'écrit à chaque calcul et '
           'le valide contre ses deux schémas (exigence E9).', '',
           '### 7.1 Fichiers', '',
           tableau(['Fichier', 'Contenu'], [
               ['`schemas/rsnat.xsd`', f'Schéma XSD, {n_el} éléments, {len(ENUMS)} énumérations'],
               ['`schemas/rsnat.schema.json`', 'Schéma JSON du même RSNat'],
               ['`schemas/projet.schema.json`', 'Schéma du fichier projet, entrée du moteur (section 7.6)'],
               ['`schemas/exemple_annexe_C.rsnat.xml` et `.json`', 'RSNat de l\'exemple de l\'annexe C de la partie 1, '
                                                               'écrit par le moteur et validé contre les deux schémas'],
               ['`opennat/rsnat_spec.py`', 'Spécification unique dont dérivent les deux schémas, ce dictionnaire et la '
                                           'sortie du moteur']]), '',
           '### 7.2 Règles d\'écriture', '',
           '- Encodage UTF-8, séparateur décimal point, dates au format AAAA-MM-JJ.',
           '- Les éléments sont écrits dans l\'ordre du schéma. Un élément facultatif sans valeur est omis.',
           '- Les valeurs sont celles du calcul aux valeurs centrales, avec la précision de la fiche A01 : une décimale '
           'pour les valeurs en m²HE, m²HE·an, m², m³, mm et points, quatre pour les facteurs ; les intervalles sont '
           'dans le bloc Incertitude.',
           '- Le bloc Attestation_Permis est le seul extrait déposé sur la plateforme d\'IRICE au dépôt du permis de '
           'construire ; il se lit sans le reste du fichier.',
           '- Le RSNat porte l\'empreinte SHA-256 de son bloc d\'entrée et de son bloc de sortie (forme canonique XML) : '
           'la plateforme recalcule l\'empreinte pour vérifier qu\'aucune valeur n\'a été modifiée après le calcul.', '',
           '### 7.3 Dictionnaire des données', '',
           'Un tableau par élément composé, dans l\'ordre du schéma. Cardinalité : 0..1 facultatif, 1..1 '
           'obligatoire, 0..n ou 1..n répété. La colonne « Origine » donne l\'élément du RSEE dont la donnée se '
           'reprend quand il existe.', '']
    out += dictionnaire()
    out += ['### 7.4 Énumérations', '',
            tableau(['Énumération', 'Valeurs admises'], [[k, ', '.join(v)] for k, v in ENUMS.items()]), '',
            '### 7.5 Exemple', '',
            'Extrait du fichier `schemas/exemple_annexe_C.rsnat.xml`, écrit par le moteur, blocs Indicateurs et '
            'Attestation_Permis :', '',
            '```', etree.tostring(el.find('Sortie_Projet/Variante_Resultat/Indicateurs'), pretty_print=True,
                                  encoding='unicode').strip(),
            etree.tostring(el.find('Attestation_Permis'), pretty_print=True, encoding='unicode').strip(), '```', '',
            '### 7.6 Fichier projet', '',
            'Le fichier projet est l\'entrée du moteur : un fichier JSON, validé contre `schemas/projet.schema.json` '
            'avant tout calcul. Il porte les données du chapitre 4 de la partie 1. Quand un RSEE est indiqué '
            '(`projet.rsee`), la parcelle, les bâtiments, les indicateurs d\'ACV, la zone climatique, le département et '
            'l\'altitude s\'en reprennent (fiche A05) ; une donnée saisie l\'emporte sur celle du RSEE. Les valeurs par '
            'défaut appliquées sont écrites au journal du calcul.', '']
    out += dictionnaire_projet()
    print(ecrire('07_rsnat.md', '\n'.join(out)), 'éléments :', n_el, 'exemple valide :', valide)


if __name__ == '__main__':
    main()
