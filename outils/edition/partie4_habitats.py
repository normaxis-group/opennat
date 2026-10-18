# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 4 de l'édition complète : une fiche par type d'habitat de la nomenclature.

Chaque fiche assemble : la définition (EUNIS 2012 de l'AEE traduite, ou définition OpenNAT pour les types
VB), les correspondances lues dans HabRef v7 (EUNIS 2022, CORINE Biotopes, habitats d'intérêt communautaire),
les espèces caractéristiques que HabRef rattache au type et à ses subdivisions, la valeur intrinsèque et sa
source, la grille d'état, les délais et difficultés, et des valeurs de référence calculées par les équations
de la méthode avec les coefficients de donnees/.
"""
import collections
import csv
import os

from commun import DON, EDITION, SOURCES, ecrire, lire, nombre, tableau

csv.field_size_limit(10 ** 9)
HABREF = os.path.join(SOURCES, 'cadre_fr', 'habref', 'HABREF_07')
GROUPES = OrderedGroups = collections.OrderedDict([
    ('VB', 'Types urbains et hors-sol (VB)'), ('C', 'Eaux de surface continentales (EUNIS C)'),
    ('D', 'Tourbières hautes et bas-marais (EUNIS D)'),
    ('E', 'Prairies, pelouses et formations de hautes herbes (EUNIS E)'),
    ('F', 'Landes, fourrés et toundras (EUNIS F)'),
    ('G', 'Boisements, forêts et autres habitats boisés (EUNIS G)'),
    ('H', 'Habitats continentaux sans végétation ou à végétation clairsemée (EUNIS H)'),
    ('I', 'Habitats agricoles, horticoles et domestiques régulièrement cultivés (EUNIS I)')])
POSITION = {'sol': 'au sol', 'eau': 'eau', 'arbre': 'arbre (houppier projeté)',
            'lineaire': 'linéaire (longueur x largeur)', 'hors_sol_toiture': 'hors-sol (toiture ou bac)',
            'hors_sol_facade': 'hors-sol (façade)'}
GRILLES = {'EP1': 'prairies de faible valeur', 'EP2': 'prairies de valeur moyenne à très haute',
           'EL1': 'landes', 'EF1': 'fourrés', 'EM1': 'mares et plans d\'eau',
           'ER1': 'milieux peu végétalisés', 'EU1': 'milieux urbains', 'EZ1': 'zones humides',
           'EB1': 'boisements', 'EA1': 'arbres', 'EH1': 'haies', 'EV1': 'vergers'}


def grille_de(uk, distinctivite, position):
    """Convention C-H6 : grille du groupe de la ligne anglaise."""
    if position == 'lineaire':
        return 'EH1'
    g = uk.split(' - ')[0]
    if 'orchard' in uk.lower():
        return 'EV1'
    if g == 'Grassland':
        return 'EP1' if distinctivite <= 2 else 'EP2'
    if g == 'Heathland and shrub':
        return 'EF1' if 'scrub' in uk.lower() and 'heath' not in uk.lower() else 'EL1'
    return {'Lakes': 'EM1', 'Sparsely vegetated land': 'ER1', 'Urban': 'EU1', 'Wetland': 'EZ1',
            'Coastal saltmarsh': 'EZ1', 'Woodland and forest': 'EB1', 'Individual trees': 'EA1',
            'Cropland': None}.get(g)


def charger_habref():
    hab, enfants = {}, collections.defaultdict(set)
    with open(os.path.join(HABREF, 'HABREF_70.csv'), encoding='utf-8-sig') as f:
        for r in csv.DictReader(f, delimiter=';'):
            hab[r['CD_HAB']] = r
    par_code = {}
    for cd, r in hab.items():
        if r['CD_TYPO'] == '7':
            par_code.setdefault(r['LB_CODE'].strip(), cd)
        for anc in r['PATH_CD_HAB'].strip('/').split('/'):
            enfants[anc].add(cd)
    corr = collections.defaultdict(list)
    with open(os.path.join(HABREF, 'HABREF_CORRESP_HAB_70.csv'), encoding='utf-8-sig') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['VALIDITE'] == 'true':
                corr[(r['CD_TYPO_ENTRE'], r['CD_TYPO_SORTIE'])].append((r['CD_HAB_ENTRE'], r['CD_HAB_SORTIE']))
    taxons = collections.defaultdict(collections.Counter)
    relation = {}
    libelles = {'19': 'caractéristique', '20': 'diagnostique', '21': 'dominante', '32': 'indicatrice'}
    garder = ('subsp.', 'var.', 'sp.', 'f.', 'agg.', 'x', 'ssp.')
    with open(os.path.join(HABREF, 'HABREF_CORRESP_TAXON_70.csv'), encoding='utf-8-sig') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['VALIDITE'] == 'true' and r['CD_TYPE_RELATION'] in libelles:
                mots = r['NOM_CITE'].split()
                if not mots:
                    continue
                nom = [mots[0]]
                for m in mots[1:]:
                    if m in garder or (m[:1].islower() and ',' not in m):
                        nom.append(m)
                    else:
                        break
                cle = ' '.join(nom)
                taxons[r['CD_HAB_ENTRE']][cle] += 1
                relation.setdefault(cle, set()).add(libelles[r['CD_TYPE_RELATION']])
    return hab, par_code, enfants, corr, (taxons, relation)


def correspondances(cds, hab, corr, entree, sortie, sens='direct'):
    """Codes et libellés de la typologie de sortie reliés aux habitats cds."""
    res = {}
    for a, b in corr[(entree, sortie)] if sens == 'direct' else corr[(sortie, entree)]:
        src, cible = (a, b) if sens == 'direct' else (b, a)
        if src in cds and cible in hab:
            h = hab[cible]
            res[h['LB_CODE'].strip()] = h['LB_HAB_FR'] or h['LB_HAB_EN']
    return sorted(res.items())


def trajectoire(v, d, D, d_ch=1.0, annees=(1, 2, 3, 5, 10, 15, 20, 30, 50)):
    vals, total = [], 0.0
    for t in range(1, 51):
        g = 0.0 if t <= d_ch else (1.0 if d == 0 else min(1.0, (t - d_ch) / d))
        x = D * v * g
        total += x
        if t in annees:
            vals.append(x)
    return vals, total


def main():
    hab, par_code, enfants, corr, (taxons, relation) = charger_habref()
    nomen = list(csv.DictReader(open(os.path.join(DON, 'nomenclature_habitats.csv'), encoding='utf-8'),
                                delimiter=';'))
    defs = {r['code']: r['definition'] for r in csv.DictReader(
        open(os.path.join(EDITION, 'definitions_habitats.csv'), encoding='utf-8'), delimiter=';')}
    val = collections.defaultdict(dict)
    for r in lire('habitats.csv'):
        val[r['cle']][r['parametre']] = r
    crit = collections.defaultdict(list)
    for r in lire('etat_criteres.csv'):
        if r['cle'] != '*':
            crit[r['cle']].append(r)
    sols = {r['cle']: float(r['valeur']) for r in lire('sols.csv')}
    uk_dist = {}
    with open(os.path.join(SOURCES, 'uk_metric', 'extraits', 'G-1 All Habitats.csv'), encoding='utf-8') as f:
        for r in csv.reader(f):
            if r[0] not in ('1', '2') and r[2]:
                uk_dist.setdefault(r[2], float(r[12] or 0))

    out = ['## Partie 4. Fiches habitats', '',
           'Une fiche par type de la nomenclature, dans l\'ordre des groupes EUNIS, précédés des types urbains et '
           'hors-sol. Chaque fiche se lit avec les fiches algorithmes de la partie 3. Ses valeurs viennent des '
           'tables de `donnees/` ; ses correspondances et ses espèces caractéristiques, de HabRef v7 (PatriNat, '
           '07/08/2025), dont la licence reste à lire avant toute publication ; ses définitions EUNIS, de la '
           'classification EUNIS 2012 de l\'Agence européenne pour l\'environnement (CC BY 4.0), traduites et '
           'adaptées pour OpenNAT.', '',
           'Les valeurs de référence de chaque fiche sont calculées pour 100 m² d\'habitat, hors trame verte et '
           'bleue (m = 1), sans effet de taille, de connectivité ni de nuisance (k = 1), en pleine terre sauf '
           'mention contraire. Trois états servent d\'exemple : bon (S = 1, f = 1), moyen (S = 0,75, f = 0,875) '
           'et mauvais (S = 0,4, f = 0,7). La trajectoire d\'un habitat créé suppose un chantier d\'un an.', '']
    num = 0
    for g, titre in GROUPES.items():
        membres = [n for n in nomen if (n['code_vinat'].startswith('VB') if g == 'VB'
                                        else (not n['code_vinat'].startswith('VB') and n['code_vinat'][0] == g))]
        if not membres:
            continue
        out += [f'### 4.{list(GROUPES).index(g) + 1} {titre}', '']
        for n in membres:
            num += 1
            c = n['code_vinat']
            v = val[c]
            uk = n['uk_habitat']
            dist = uk_dist.get(uk, 0)
            grille = grille_de(uk, dist, n['position'])
            out += [f'#### Fiche H{num:03d}. {c} : {n["libelle_fr"]}', '']
            # identification
            codes_eunis = [n['code_eunis_2012']] if not c.startswith('VB') else \
                [x for x in ([n['code_eunis_2012']] + n['alias_eunis_2012'].split()) if x]
            cds = set()
            for e in codes_eunis:
                cd = par_code.get(e)
                if cd:
                    cds |= enfants.get(cd, {cd}) | {cd}
            e2022 = correspondances({par_code[e] for e in codes_eunis if e in par_code}, hab, corr, '7', '107')
            cb = correspondances(cds, hab, corr, '7', '22', sens='inverse')
            hic = correspondances(cds, hab, corr, '7', '8')
            out += ['**Identification**', '',
                    tableau(['Élément', 'Valeur'], [
                        ['Code OpenNAT', c],
                        ['EUNIS 2012', ', '.join(codes_eunis)],
                        ['Position de saisie', POSITION[n['position']]],
                        ["Grille d'état", f'{grille} ({GRILLES[grille]})' if grille else 'aucune (f = 1)'],
                        ['Correspondances HabRef', f'{len(e2022)} type(s) EUNIS 2022, {len(cb)} type(s) CORINE '
                                                   f"Biotopes, {len(hic)} habitat(s) d'intérêt communautaire"]]),
                    '', '**Définition**', '', defs.get(c, ''), '']
            for titre_c, liste in (('EUNIS 2022', e2022), ('CORINE Biotopes', cb),
                                   ("Habitats d'intérêt communautaire (annexe I de la directive 92/43/CEE)", hic)):
                if liste:
                    out += [f'**Correspondances {titre_c} (HabRef v7)**', '',
                            tableau(['Code', 'Libellé'], [[k, l] for k, l in liste]), '']
            # espèces
            cpt = collections.Counter()
            for cd in cds:
                cpt.update(taxons.get(cd, {}))
            if cpt:
                out += ['**Espèces citées par HabRef**', '',
                        f'Taxons que HabRef donne comme caractéristiques, diagnostiques, dominants ou indicateurs du '
                        f'type et de ses subdivisions ({len(cpt)} taxons), classés par nombre de subdivisions qui les '
                        "citent. La liste sert à la reconnaissance du type et au critère A des grilles d'état ; elle "
                        'ne vaut pas inventaire.', '',
                        tableau(['Taxon', 'Statut dans HabRef', 'Citations'],
                                [[k, ', '.join(sorted(relation.get(k, []))), str(v)]
                                 for k, v in sorted(cpt.items(), key=lambda x: (-x[1], x[0]))]), '']
            # valeur intrinsèque
            vi = v.get('valeur_intrinseque')
            lignes = [['Valeur intrinsèque', nombre(vi['valeur']) + ' m²HE/m²',
                       f'{nombre(vi["incertitude_min"])} à {nombre(vi["incertitude_max"])}',
                       vi['reference_precise']]]
            for st, lib in (('J', 'stade jeune'), ('M', 'stade moyen'), ('A', 'stade âgé')):
                p = v.get(f'valeur_intrinseque_stade_{st}')
                if p:
                    lignes.append([f'Valeur, {lib}', nombre(p['valeur']) + ' m²HE/m²',
                                   f'{nombre(p["incertitude_min"])} à {nombre(p["incertitude_max"])}',
                                   p['reference_precise']])
            out += ['**Valeur intrinsèque (module H, équation H1)**', '',
                    tableau(['Paramètre', 'Valeur', 'Plage', 'Source'], lignes), '',
                    f'Correspondance retenue : {n["justification"]}.', '']
            # grille
            if grille:
                lc = crit[grille]
                out += [f'**Grille d\'état {grille} (module H, équations H2 et H3)**', '',
                        tableau(['Critère', 'Libellé', 'Essentiel'],
                                [[r['parametre'].replace('critere_', '').replace('_essentiel', '')
                                  .replace('indicateur_', '').replace('_', ' '), r['justification'],
                                  'oui' if 'essentiel' in r['parametre'] else 'non'] for r in lc]), '']
            # délais et difficultés
            dl = []
            for p, lib in (('delai_maturite_bon', 'Création, bon état visé'),
                           ('delai_maturite_moyen', 'Création, état moyen visé'),
                           ('delai_maturite_mauvais', 'Création, mauvais état visé'),
                           ('delai_maturite_sans_etat', 'Création, type sans état'),
                           ('delai_amelioration_mauvais_moyen', 'Amélioration, mauvais vers moyen'),
                           ('delai_amelioration_mauvais_bon', 'Amélioration, mauvais vers bon'),
                           ('delai_amelioration_moyen_bon', 'Amélioration, moyen vers bon'),
                           ('difficulte_creation', 'Difficulté de création'),
                           ('difficulte_amelioration', 'Difficulté d\'amélioration')):
                if p in v:
                    unite = 'ans' if p.startswith('delai') else ''
                    dl.append([lib, f'{nombre(v[p]["valeur"])} {unite}'.strip(), v[p]['reference_precise']])
            if dl:
                out += ['**Délais et difficultés (module T, équations T3 et T4)**', '',
                        tableau(['Paramètre', 'Valeur', 'Source'], dl), '']
            else:
                out += ['**Délais et difficultés**', '', 'La métrique anglaise ne prévoit ni création ni '
                        'amélioration pour la ligne correspondante : le type atteint sa valeur dès la fin du '
                        'chantier (convention C-T3).', '']
            # valeurs de référence
            x = float(vi['valeur'])
            ref = [['Bon état', nombre(100 * x * 1.0, 2)], ['État moyen', nombre(100 * x * 0.875, 2)],
                   ['Mauvais état', nombre(100 * x * 0.7, 2)]]
            if not grille:
                ref = [['Sans grille (f = 1)', nombre(100 * x, 2)]]
            out += ['**Valeurs de référence pour 100 m² (équations H4 et H5)**', '',
                    tableau(['État', 'V, m²HE'], ref), '']
            if n['position'] == 'sol' and not c.startswith(('VB.1', 'VB.2', 'VB.3', 'VB.4', 'VB.10', 'VB.25')):
                out += ['Posé sur dalle (convention C-S2), en bon état, 100 m² valent : '
                        + ', '.join(f'{lib} {nombre(100 * x * sols[s], 2)} m²HE' for s, lib in (
                            ('S04', 'moins de 15 cm de substrat'), ('S05', '15 à 30 cm'),
                            ('S06', '30 à 80 cm'), ('S07', '80 cm et plus'))) + '.', '']
            # trajectoire
            D = float(v['difficulte_creation']['valeur']) if 'difficulte_creation' in v else 1.0
            traj = []
            for p, lib, f in (('delai_maturite_bon', 'bon', 1.0), ('delai_maturite_moyen', 'moyen', 0.875),
                              ('delai_maturite_mauvais', 'mauvais', 0.7), ('delai_maturite_sans_etat',
                                                                           'sans état', 1.0)):
                if p in v:
                    vals, tot = trajectoire(100 * x * f, float(v[p]['valeur']), D)
                    traj.append([lib] + [nombre(y, 1) for y in vals] + [nombre(tot, 0)])
            if traj:
                out += ['**Trajectoire de 100 m² créés (équation T3)**', '',
                        f'Difficulté de création D = {nombre(D)} ; valeurs annuelles en m²HE et valeur intégrée '
                        'sur 50 ans en m²HE·an.', '',
                        tableau(['État visé', 'An 1', 'An 2', 'An 3', 'An 5', 'An 10', 'An 15', 'An 20', 'An 30',
                                 'An 50', 'Intégrée'], traj), '']
            if traj and n['position'] == 'sol' and grille and c not in ('VB.10',) and 'delai_maturite_bon' in v:
                dal = []
                for snat_c, lib in (('S04', 'moins de 15 cm'), ('S05', '15 à 30 cm'), ('S06', '30 à 80 cm'),
                                    ('S07', '80 cm et plus')):
                    vals, tot = trajectoire(100 * x * sols[snat_c], float(v['delai_maturite_bon']['valeur']), D)
                    dal.append([lib] + [nombre(y, 1) for y in vals] + [nombre(tot, 0)])
                out += ['**Trajectoire de 100 m² créés sur dalle, bon état visé (équations S2 et T3)**', '',
                        tableau(['Substrat', 'An 1', 'An 2', 'An 3', 'An 5', 'An 10', 'An 15', 'An 20', 'An 30',
                                 'An 50', 'Intégrée'], dal), '']
            pos_x = {'sol': 'sol_pleine_terre', 'eau': 'eau', 'arbre': 'arbre', 'lineaire': 'lineaire',
                     'hors_sol_toiture': 'hors_sol_toiture', 'hors_sol_facade': 'hors_sol_facade'}[n['position']]
            xml = ['<Unite>', f'  <identifiant>U-{c}</identifiant>', f'  <code_habitat>{c}</code_habitat>',
                   f'  <position>{pos_x}</position>', '  <surface>100</surface>']
            if n['position'] == 'hors_sol_toiture':
                xml.append('  <epaisseur_substrat>20</epaisseur_substrat>')
            if 'valeur_intrinseque_stade_M' in v:
                xml.append('  <stade>M</stade>')
            xml.append('  <statut>creee</statut>')
            if grille:
                xml.append('  <Critere_Collection>')
                for r_c in crit[grille]:
                    code_c = (r_c['parametre'].replace('critere_', '').replace('_essentiel', ''))
                    if code_c.startswith('indicateur_'):
                        xml += ['    <Critere>', f'      <code>{code_c}</code>', '      <note>2</note>', '    </Critere>']
                    else:
                        xml += ['    <Critere>', f'      <code>{code_c}</code>', '      <reponse>oui</reponse>',
                                '    </Critere>']
                xml.append('  </Critere_Collection>')
            xml.append('</Unite>')
            out += ['**Exemple de saisie dans le fichier projet (partie 7)**', '', '```'] + xml + ['```', '']
            # Bnat
            if n['position'] in ('sol', 'eau', 'hors_sol_toiture', 'hors_sol_facade'):
                out += ['**Contribution à Bnat**', '',
                        'Bnat ne dépend pas du type d\'habitat mais de la nature de surface et du support : en '
                        'pleine terre, 100 m² apportent 100 points-m² au numérateur de l\'équation A3 ; sur dalle '
                        'ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe '
                        'd\'épaisseur (`sols.csv`).', '']
    print(ecrire('04_fiches_habitats.md', '\n'.join(out)), num)


if __name__ == '__main__':
    main()
