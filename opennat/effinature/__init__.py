# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Import d'un dossier Effinature 8.1 : fichier projet OpenNAT, fichier crédits et fiche de relevé.

L'entrée est un export de dossier (format « Effinature export 1 ») qui reprend les tables de la plateforme :
calculs CBS (état initial et projet, surfaces par nature), habitats de l'IVE, palette végétale, contrôles. Le
projet produit compare la variante « Projet » (l'opération certifiée) à la variante « Classique » (la même
opération réduite au minimum du PLU) : le gain créditable est ce que l'opération Effinature fait de plus.

Aucun état n'est inventé : les unités sortent sans grille renseignée (tous les critères à « non », fiche A10).
L'état réel est relevé au contrôle de conformité à la livraison puis à chaque contrôle HVE, sur la fiche de
relevé, et revient dans le fichier crédits par `releves_depuis_csv`.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re

from ..donnees import Tables

FORMAT_EXPORT = 'Effinature export 1'

# Années entre deux relevés après le premier contrôle HVE, au plus cinq (convention C-X12) ; à confirmer sur la
# périodicité réelle des contrôles HVE.
PERIODE_HVE = 5

# Natures de surface du calcul CBS d'Effinature (CbsCalculator::NATURES) : code OpenNAT, position, épaisseur (cm).
# None : espace vert, dont le type d'habitat vient de la répartition de l'IVE.
NATURES_CBS = {
    'vrd_semi_permeable': ('VB.3', 'sol_pleine_terre', None),
    'vrd_semi_permeable_vegetalise': ('VB.4', 'sol_pleine_terre', None),
    'dalle_moins_80': (None, 'sol_sur_dalle', 50),
    'dalle_plus_80': (None, 'sol_sur_dalle', 100),
    'pleine_terre': (None, 'sol_pleine_terre', None),
    'potager': ('VB.22', 'sol_pleine_terre', None),
    'infiltration': ('VB.19', 'eau', None),
    'mare': ('VB.20', 'eau', None),
    'bassin_agrement': ('VB.21', 'eau', None),
    'toiture_extensive': ('VB.11', 'hors_sol_toiture', 10),
    'toiture_semi_intensive': ('VB.12', 'hors_sol_toiture', 20),
    'toiture_intensive': ('VB.13', 'hors_sol_toiture', 40),
    'brown_roof': ('VB.12', 'hors_sol_toiture', 15),
    'facade_vegetalisee': ('VB.15', 'hors_sol_facade', None),
    'jardiniere': ('VB.23', None, None),
    'mobilier_urbain': ('VB.23', None, None),
}
NATURES_AU_SOL = {k for k, (_, pos, _) in NATURES_CBS.items() if pos in ('sol_pleine_terre', 'sol_sur_dalle', 'eau')}

# Habitats de l'IVE (libellé libre) : premier motif reconnu, code OpenNAT. Le défaut est la pelouse (VB.5), le
# type d'espace vert le moins valorisé, pour ne jamais prêter à l'opération un habitat qu'elle n'a pas déclaré.
HABITATS_IVE = [
    (r'haie', 'FA.2'),
    (r'prairie|fauche', 'VB.26'),
    (r'pelouse|gazon', 'VB.5'),
    (r'potager|jardin partag|jardin familial', 'VB.22'),
    (r'noue|jardin de pluie', 'VB.19'),
    (r'mare', 'VB.20'),
    (r'friche', 'VB.8'),
    (r'jardin', 'VB.7'),
    (r'massif|arbust|couvre.sol|vivace', 'VB.6'),
    (r'parking|voirie|enrob|imperm', 'VB.2'),
    (r'b[aâ]ti', 'VB.1'),
]
HABITAT_DEFAUT = 'VB.5'

TYPOLOGIES = [
    (r'logement|r[ée]sidenc|habitat', 'logement'),
    (r'industri|logisti|entrep[oô]t|activit', 'industrie'),
    (r'am[ée]nagement|zac|espace public|parc|voirie', 'amenagement'),
    (r'bureau|tertiaire|[ée]cole|enseignement|sant[ée]|commerce|[ée]quipement', 'tertiaire'),
]


class ErreurImport(ValueError):
    """Export de dossier incomplet ou incohérent."""


def code_habitat(libelle: str) -> tuple[str, bool]:
    """Code OpenNAT d'un habitat de l'IVE et indicateur « reconnu »."""
    t = libelle.lower()
    for motif, code in HABITATS_IVE:
        if re.search(motif, t):
            return code, True
    return HABITAT_DEFAUT, False


def _typologie(texte: str | None, journal: list) -> str:
    for motif, typo in TYPOLOGIES:
        if texte and re.search(motif, texte.lower()):
            return typo
    journal.append(f'typologie « {texte} » non reconnue : logement retenu')
    return 'logement'


def _repartition(habitats: list[dict], journal: list) -> list[tuple[str, float]]:
    """Parts des espaces verts par type d'habitat, d'après l'IVE (haies et surfaces minérales exclues)."""
    parts: dict[str, float] = {}
    for h in habitats:
        code, connu = code_habitat(h['habitat_name'])
        if not connu:
            journal.append(f'habitat IVE « {h["habitat_name"]} » non reconnu : {HABITAT_DEFAUT} retenu')
        if code in ('FA.2', 'VB.1', 'VB.2', 'VB.19', 'VB.20', 'VB.22'):
            continue
        parts[code] = parts.get(code, 0.0) + float(h['surface_m2'])
    total = sum(parts.values())
    if not total:
        journal.append(f'aucun habitat d\'espace vert à l\'IVE : espaces verts en {HABITAT_DEFAUT}')
        return [(HABITAT_DEFAUT, 1.0)]
    return [(c, s / total) for c, s in sorted(parts.items(), key=lambda x: -x[1])]


def _unites_cbs(cbs: dict, repartition, prefixe: str, journal: list, haies: float = 0.0) -> list[dict]:
    """Unités d'un calcul CBS : bâti, natures de surface, reste de la parcelle imperméable. `haies` : emprise des
    haies décrites à part, prise sur la pleine terre."""
    n = iter(range(1, 1000))
    u = []

    def ajouter(code, surface, position=None, epaisseur=None, **autres):
        if surface <= 0:
            return
        d = dict(id=f'{prefixe}-{next(n)}', code=code, surface=round(surface, 2))
        if position:
            d['position'] = position
        if epaisseur:
            d['epaisseur'] = epaisseur
        d.update(autres)
        u.append(d)

    parcelle, emprise = float(cbs['surface_parcelle_m2']), float(cbs.get('emprise_bati_m2') or 0)
    ajouter('VB.1', emprise, 'sol_pleine_terre')
    au_sol = 0.0
    for nature, s in cbs['surfaces'].items():
        if nature not in NATURES_CBS:
            raise ErreurImport(f'nature de surface CBS inconnue : {nature}')
        code, pos, ep = NATURES_CBS[nature]
        s = float(s)
        if nature in NATURES_AU_SOL:
            au_sol += s
        if nature == 'pleine_terre' and haies:
            if s < haies:
                raise ErreurImport(f'haies de l\'IVE ({haies:g} m²) plus étendues que la pleine terre du CBS')
            s -= haies
        if code is None:
            for c, part in repartition:
                ajouter(c, s * part, pos, ep)
        else:
            ajouter(code, s, pos, ep)
    reste = parcelle - emprise - au_sol
    if reste < -0.01 * parcelle:
        raise ErreurImport(f'CBS {cbs["etat"]} : bâti et surfaces au sol ({emprise + au_sol:g} m²) dépassent la '
                           f'parcelle ({parcelle:g} m²)')
    if reste > 0:
        ajouter('VB.2', reste, 'sol_pleine_terre')
        journal.append(f'CBS {cbs["etat"]} : {reste:g} m² non décrits, comptés imperméabilisés (VB.2)')
    return u


def _arbres(palette: list[dict], prefixe: str, tables: Tables) -> list[dict]:
    """Arbres de la palette (strate arborée) : une unité par indigénat, jeunes plants de petite classe, houppier
    par défaut de la classe (fiche A14)."""
    nb = {'VB.18a': 0, 'VB.18b': 0}
    for p in palette:
        if p.get('strate') == 'arboree' and float(p.get('quantite') or 0) > 0:
            nb['VB.18a' if p.get('indigenat') == 'local' else 'VB.18b'] += int(round(float(p['quantite'])))
    houppier = tables.lignes[('VB.18', 'surface_defaut_houppier_petit')].valeur
    return [dict(id=f'{prefixe}-A{i}', code=c, position='arbre', surface=round(k * houppier, 2), nombre_arbres=k,
                 classe_diametre='petit', stade='J', statut='creee') for i, (c, k) in enumerate(nb.items(), 1) if k]


def _haies(habitats: list[dict], prefixe: str) -> list[dict]:
    return [dict(id=f'{prefixe}-H{i}', code='FA.2', position='lineaire', surface=float(h['surface_m2']))
            for i, h in enumerate((h for h in habitats if code_habitat(h['habitat_name'])[0] == 'FA.2'), 1)]


def _classique(projet_cbs: dict, plu: dict, journal: list) -> list[dict]:
    """Variante « Classique » : même bâti et mêmes VRD perméables, pleine terre ramenée au minimum du PLU en
    pelouse, le reste imperméabilisé. C'est l'opération que le maître d'ouvrage aurait faite sans Effinature."""
    parcelle = float(projet_cbs['surface_parcelle_m2'])
    pt = float(plu['pleine_terre']) * parcelle
    surfaces = {k: v for k, v in projet_cbs['surfaces'].items() if k in ('vrd_semi_permeable',)}
    surfaces['pleine_terre'] = pt
    journal.append(f'variante Classique : {pt:g} m² de pleine terre en pelouse ({plu["pleine_terre"]:.0%} de la '
                   f'parcelle, {plu.get("source", "PLU")}), aucune toiture ni façade végétalisée, aucun arbre')
    return _unites_cbs(dict(projet_cbs, surfaces=surfaces), [(HABITAT_DEFAUT, 1.0)], 'U2', [])


def _annees(debut: str, dates: list[str]) -> list[int]:
    d0 = dt.date.fromisoformat(debut)
    return [max(1, round((dt.date.fromisoformat(x) - d0).days / 365.25)) for x in dates]


def calendrier(export: dict, periode: int, journal: list) -> list[int]:
    """Calendrier propre (convention C-X12) : contrôle de conformité à la livraison en année 1, contrôles HVE à
    leur date, puis tous les `periode` ans jusqu'à l'année 50."""
    if not 1 <= periode <= 5:
        raise ErreurImport('la période entre deux relevés doit être de 1 à 5 ans (convention C-X12)')
    livraison = export['projet'].get('date_livraison')
    ctl = export.get('controles', [])
    ans = {1}
    hve = [c['date_visite'] for c in ctl if c.get('type') == 'hve' and c.get('date_visite')]
    if livraison and hve:
        ans |= set(_annees(livraison, hve))
    else:
        ans.add(2)
        journal.append('contrôle HVE sans date : relevé prévu à l\'année 2 (deux ans d\'exploitation)')
    a = max(ans)
    while a + periode < 50:
        a += periode
        ans.add(a)
    ans.add(50)
    cal = sorted(ans)
    if cal[0] > 3 or any(b - a > 5 for a, b in zip(cal, cal[1:])):
        raise ErreurImport(f'calendrier {cal} contraire à la convention C-X12')
    journal.append(f'calendrier : {cal} (livraison en 1, HVE, puis tous les {periode} ans)')
    return cal


def importer(export: dict, periode_hve: int = PERIODE_HVE) -> dict:
    """Export de dossier → fichier projet, fichier crédits (squelette) et journal des hypothèses."""
    if export.get('format') != FORMAT_EXPORT:
        raise ErreurImport(f'format attendu : « {FORMAT_EXPORT} »')
    journal: list[str] = []
    p = export['projet']
    ident = 'effinature_' + re.sub(r'[^A-Za-z0-9]+', '_', str(p['dossier_number'])).strip('_')
    cbs = {c['etat']: c for c in export.get('cbs', [])}
    if 'projet' not in cbs:
        raise ErreurImport('calcul CBS de l\'état projet absent')
    ctx = export.get('contexte', {})
    for k in ('zone_biogeographique', 'zone_climatique'):
        if not ctx.get(k):
            raise ErreurImport(f'contexte : {k} à renseigner dans l\'export')
    ive = export.get('ive_habitats', [])
    phase = 'realisation' if any(h['phase'] == 'realisation' for h in ive) else 'projet'
    hab_projet = [h for h in ive if h['phase'] == phase]
    hab_initial = [h for h in ive if h['phase'] == 'initial']

    # État initial : CBS initial s'il existe (rénovation), sinon habitats de l'IVE et reste déclaré.
    if 'initial' in cbs:
        initial = _unites_cbs(cbs['initial'], _repartition(hab_initial, journal), 'U0', journal)
    else:
        if not hab_initial:
            raise ErreurImport('état initial absent : ni CBS initial ni habitats initiaux à l\'IVE')
        initial = []
        for i, h in enumerate(hab_initial, 1):
            code, connu = code_habitat(h['habitat_name'])
            if not connu:
                journal.append(f'habitat initial « {h["habitat_name"]} » non reconnu : {code} retenu')
            initial.append(dict(id=f'U0-{i}', code=code, surface=float(h['surface_m2'])))
        reste = float(cbs['projet']['surface_parcelle_m2']) - sum(u['surface'] for u in initial)
        if reste > 0.01:
            code = export.get('reste_initial')
            if not code:
                raise ErreurImport(f'{reste:g} m² de l\'état initial non décrits : déclarer « reste_initial » '
                                   f'(code OpenNAT) dans l\'export')
            initial.append(dict(id=f'U0-{len(initial) + 1}', code=code, surface=round(reste, 2)))
            journal.append(f'état initial : {reste:g} m² non décrits à l\'IVE, déclarés {code}')

    # Les haies de l'IVE occupent le sol (fiche A03) : leur emprise est prise sur la pleine terre du CBS.
    tables = Tables()
    haies = _haies(hab_projet, 'U1')
    h = sum(u['surface'] for u in haies)
    if h:
        journal.append(f'haies : {h:g} m² pris sur la pleine terre du CBS')
    projet_u = (_unites_cbs(cbs['projet'], _repartition(hab_projet, journal), 'U1', journal, h)
                + haies + _arbres(export.get('palette', []), 'U1', tables))
    variantes = [dict(nom='Projet', reference=True, unites=projet_u)]
    plu = export.get('plu')
    if plu and plu.get('pleine_terre') is not None:
        variantes.append(dict(nom='Classique', unites=_classique(cbs['projet'], plu, journal)))
    else:
        journal.append('PLU sans taux de pleine terre : pas de variante Classique, fichier crédits non produit')

    contexte = dict(zone_biogeographique=ctx['zone_biogeographique'], zone_climatique=ctx['zone_climatique'],
                    typologie=_typologie(p.get('typologie_batiment'), journal))
    if p.get('departement'):
        contexte['departement'] = str(p['departement'])
    if plu and plu.get('pleine_terre') is not None:
        contexte['pleine_terre_plu'] = float(plu['pleine_terre'])
    if plu and plu.get('cbs') is not None:
        contexte['cbs_plu'] = float(plu['cbs'])
    # Position explicite partout (le RSNat l'exige) : position par défaut du type quand le CBS n'en donne pas.
    nomenclature = tables.nomenclature
    for u in initial + [u for v in variantes for u in v['unites']]:
        if 'position' not in u:
            pos = nomenclature[u['code']]['position']
            u['position'] = 'sol_pleine_terre' if pos == 'sol' else pos

    projet = {
        'format': 'OpenNAT projet 1',
        'projet': {k: v for k, v in dict(identifiant=ident, nom=p.get('name'),
                                          adresse=', '.join(x for x in (p.get('address'), p.get('postal_code'),
                                                                        p.get('city')) if x),
                                          commune_insee=p.get('code_insee')).items() if v},
        'contexte': contexte,
        'parcelle': dict(surface=float(cbs['projet']['surface_parcelle_m2']),
                         emprise=float(cbs['projet'].get('emprise_bati_m2') or 0)),
        'etat_initial': initial,
        'variantes': variantes,
        'options': dict(tirages=0),
    }
    journal.append('aucune grille d\'état renseignée : tous les critères à « non » (fiche A10) jusqu\'au premier '
                   'relevé ; l\'état se relève au contrôle de livraison puis à chaque contrôle HVE')

    credits = None
    if len(variantes) == 2:
        mineral = sum(u['surface'] for u in initial if u['code'] in ('VB.1', 'VB.2')) > 0.5 * projet['parcelle']['surface']
        credits = {
            'format': 'OpenNAT crédits 1',
            'identifiant': ident + '_credits',
            'projet': ident + '.projet.json',
            'variante_projet': 'Projet',
            'scenario_reference': dict(defaut='mineral' if mineral else 'usage_maintenu'),
            'obligations': dict(variante='Classique', liste=[dict(
                objet=f'{plu["pleine_terre"]:.0%} de pleine terre', source=plu.get('source', 'PLU'),
                traduction='variante Classique : pleine terre minimale en pelouse, le reste imperméabilisé')]),
            'certification': (f'Effinature 8.1, dossier {p["dossier_number"]}'
                              + (f', niveau {p["niveau_vise"]}' if p.get('niveau_vise') else '')
                              + ' ; suivi Effinature HVE 8.1'),
            'calendrier': calendrier(export, periode_hve, journal),
            'releves': [],
            'options': dict(tirages=0),
        }
        if export.get('risque'):
            credits['risque'] = dict(export['risque'])
        else:
            journal.append('risque non déclaré dans l\'export : chaque facteur sera noté élevé (annexe A) tant que le '
                           'porteur ne l\'a pas déclaré')
    return dict(identifiant=ident, projet=projet, credits=credits, journal=journal)


def fiche_releve(projet: dict, tables: Tables | None = None) -> list[dict]:
    """Lignes de la fiche de relevé : une par critère (ou indicateur noté de 1 à 3) de chaque unité du projet."""
    t = tables or Tables()
    lignes = []
    for u in projet['variantes'][0]['unites']:
        grille = t.nomenclature[u['code']].get('grille_etat') or ''
        if not grille:
            continue
        for (cle, par) in t.lignes:
            if cle != grille or not par.startswith(('critere_', 'indicateur_')):
                continue
            nom = par.split('_', 1)[1]
            ess = nom.endswith('_essentiel')
            lignes.append(dict(annee='', date='', releve_par='', unite=u['id'], code=u['code'],
                               libelle=t.nomenclature[u['code']]['libelle_fr'], grille=grille,
                               critere=nom[:-len('_essentiel')] if ess else nom,
                               essentiel='oui' if ess else '', reponse='',
                               attendu='1, 2 ou 3' if par.startswith('indicateur_') else 'oui, non ou sans_objet'))
    return lignes


CHAMPS_FICHE = ['annee', 'date', 'releve_par', 'unite', 'code', 'libelle', 'grille', 'critere', 'essentiel',
                'reponse', 'attendu']


def releves_depuis_csv(chemin: str) -> list[dict]:
    """Fiche de relevé remplie → entrées `releves` du fichier crédits (une par année)."""
    par_annee: dict[int, dict] = {}
    with open(chemin, encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if not (r.get('annee') or '').strip() or not (r.get('reponse') or '').strip():
                continue
            a = int(r['annee'])
            rel = par_annee.setdefault(a, dict(annee=a, unites={}))
            if r.get('date'):
                rel['date'] = r['date']
            if r.get('releve_par'):
                rel['ecologue'] = r['releve_par']
            u = rel['unites'].setdefault(r['unite'], dict(id=r['unite']))
            rep = r['reponse'].strip()
            if rep in ('1', '2', '3'):
                u.setdefault('notes', {})[r['critere']] = int(rep)
            elif rep in ('oui', 'non', 'sans_objet'):
                u.setdefault('criteres', {})[r['critere']] = rep
            else:
                raise ErreurImport(f'fiche de relevé, unité {r["unite"]}, critère {r["critere"]} : réponse « {rep} »')
    return [dict(rel, unites=list(rel['unites'].values())) for _, rel in sorted(par_annee.items())]


def executer(chemin_export: str, sortie: str, periode_hve: int = PERIODE_HVE, chemin_releves: str | None = None,
             dire=print) -> dict:
    """Commande `opennat effinature` : écrit `<id>.projet.json`, `<id>.credits.json`, la fiche de relevé et le
    journal dans `sortie`."""
    with open(chemin_export, encoding='utf-8') as f:
        export = json.load(f)
    if export.get('format') == 'BPS export 1':                 # projet du BPS (bâtiment en exploitation), voir bps.py
        from .bps import importer_bps
        r = importer_bps(export)
    else:
        r = importer(export, periode_hve)
    os.makedirs(sortie, exist_ok=True)
    ident = r['identifiant']
    fichiers = {}

    def ecrire(nom, contenu):
        fichiers[nom] = os.path.join(sortie, nom)
        with open(fichiers[nom], 'w', encoding='utf-8') as f:
            json.dump(contenu, f, ensure_ascii=False, indent=1)
            f.write('\n')

    ecrire(f'{ident}.projet.json', r['projet'])
    if r['credits']:
        if chemin_releves:
            r['credits']['releves'] = releves_depuis_csv(chemin_releves)
            r['journal'].append(f'{len(r["credits"]["releves"])} relevé(s) repris de {os.path.basename(chemin_releves)}')
        ecrire(f'{ident}.credits.json', r['credits'])
    fiche = os.path.join(sortie, f'{ident}.fiche_releve.csv')
    with open(fiche, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, CHAMPS_FICHE, delimiter=';')
        w.writeheader()
        w.writerows(fiche_releve(r['projet']))
    fichiers['fiche'] = fiche
    with open(os.path.join(sortie, f'{ident}.journal.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(r['journal']) + '\n')
    for l in r['journal']:
        dire(l)
    dire(f'fichiers écrits dans {sortie}')
    return dict(r, fichiers=fichiers)
