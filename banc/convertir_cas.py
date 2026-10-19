# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Banc de validation : convertit les cas du carnet de référence (outils/edition/cas_*.py) en fichiers projet
(`banc/cas/*.json`) et écrit les résultats attendus calculés par le carnet (`banc/attendus.json`).

Le carnet de référence (`outils/carnet_reference.py`) applique les fiches sans rien partager avec le moteur ; le
moteur doit retrouver ses résultats à 0,1 % près (exigence E10)."""
import json
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, 'outils'))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'edition'))
import carnet_reference as C  # noqa: E402
from cas_complementaires import CAS_SUPP  # noqa: E402
from cas_dynamiques import CAS_DYN  # noqa: E402
from cas_validation import ANNEXE_C, CAS  # noqa: E402

CLES_UNITE = {'id', 'code', 'position', 'surface', 'tache', 'criteres', 'stade', 'statut', 'liee', 'protection',
              'eclairage', 'epaisseur', 'situation', 'renouvellements', 'arrose', 'bassin_versant',
              'bassin_versant_permeable', 'fond', 'profondeur', 'gites', 'gestion', 'apres_plan', 'alimentation',
              'vitrage', 'bruit', 'texture', 'profondeur_sol', 'plan_gestion_annees'}


def nom_fichier(cas):
    t = unicodedata.normalize('NFKD', cas['nom'].split('.')[0]).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '_', t).strip('_') + '.json'


def unite(u):
    inconnues = set(u) - CLES_UNITE
    if inconnues:
        raise ValueError(f'clés non converties : {inconnues}')
    x = {k: v for k, v in u.items() if k not in ('criteres', 'vitrage', 'bruit')}
    if 'criteres' in u:
        ok, n, ess = u['criteres']
        x['score'] = dict(satisfaits=ok, applicables=n, essentiel_echoue=bool(ess))
    if u.get('vitrage'):
        x['exposition_vitrage'] = True
    if 'bruit' in u:
        x['niveau_sonore'] = u['bruit']
    if isinstance(x.get('eclairage'), dict):
        x['eclairage'] = {k: v for k, v in x['eclairage'].items()}
    return x


def projet(cas):
    ctx = cas['contexte']
    ges = cas.get('ges', {})
    p = {
        'format': 'OpenNAT projet 1',
        'projet': {'identifiant': nom_fichier(cas)[:-5], 'nom': cas['nom']},
        'contexte': {'zone_biogeographique': ctx['zone'], 'typologie': ctx['typologie'],
                     'zone_climatique': ctx.get('zone_climatique', 'H1a')},
        'parcelle': {'surface': cas['parcelle']},
        'chantier': {'annee_debut': cas.get('annee_debut', 2027), 'mois_debut': cas.get('mois_debut', 1)},
        'gestion': {'plan_annees': cas.get('plan_gestion_annees', 0)},
        'taches': {t: {k: v for k, v in info.items()} for t, info in cas.get('taches', {}).items()},
        'etat_initial': [unite(u) for u in cas['initial']],
        'options': {'tirages': 0},
    }
    if ctx.get('altitude') is not None:
        p['contexte']['altitude'] = ctx['altitude']
    if 'k_delai_etude' in ctx:
        p['contexte']['k_delai_etude'] = ctx['k_delai_etude']
    if cas.get('sol'):
        p['contexte']['sol'] = dict(cas['sol'])
    if 'mois_destruction' in cas:
        p['chantier']['mois_destruction'] = cas['mois_destruction']
    v = {'nom': 'Projet', 'reference': True, 'unites': [unite(u) for u in cas['projet']]}
    if ges or cas.get('sref'):
        bat = {'nom': 'Bâtiment', 'sref': cas.get('sref', 0.0), 'emprise_au_sol': cas.get('emprise', 0.0),
               'duree_chantier': cas['duree_chantier_mois'], 'ges': {}}
        conv = {'phase_A1_A5': 'A1-A3', 'phase_B': 'B', 'phase_C': 'C', 'phase_D': 'D'}
        for k, g in ges.items():
            bat['ges'][conv[k]] = g
        if cas.get('pollution'):                                     # indicateurs par m² de S_ref, phases A à C
            bat['pollution'] = {code: {'A1-A3': x} for code, x in cas['pollution'].items()}
        p['batiments'] = [bat]
    else:
        p['parcelle']['emprise'] = cas.get('emprise', 0.0)
        p['chantier']['duree_mois'] = cas['duree_chantier_mois']
    mat = {}
    if cas.get('bois'):
        mat['bois'] = [dict(regime=r, volume=q, remplacements=n,
                            **({'justification': 'pièce déclarée'} if r != 'coupe_rase' else {}))
                       for r, q, n in cas['bois']]
    if cas.get('granulats'):
        mat['granulats'] = {'masse': cas['granulats']}
    if mat:
        v['materiaux'] = mat
    if cas.get('infiltration'):
        v['ouvrages_pluviaux'] = [{'surface_drainee': cas['infiltration'], 'infiltration_surface': True}]
    p['variantes'] = [v]
    return p


def attendu(r):
    a = {k: r[k] for k in ('v0', 'i0', 'i1', 'i0_30', 'i1_30', 'dm', 'faune', 'cnat', 'cnat_30', 'inat', 'snat',
                           'bnat', 'pt', 'arrosage_m3_an', 'niveau')}
    a['cnat_rel'] = r['cnat_rel']
    a['site'] = r['site']
    a['ref'] = r['ref']
    a['unites'] = {u['id']: dict(V=u['V'], traj=u['traj']) for u in r['projet']}
    a['unites_initiales'] = {u['id']: u['V'] for u in r['initial']}
    return a


def main():
    dossier = os.path.join(ICI, 'cas')
    os.makedirs(dossier, exist_ok=True)
    attendus = {}
    tous = [ANNEXE_C] + CAS + CAS_SUPP + CAS_DYN
    for cas in tous:
        nom = nom_fichier(cas)
        with open(os.path.join(dossier, nom), 'w', encoding='utf-8') as f:
            json.dump(projet(cas), f, ensure_ascii=False, indent=1)
        attendus[nom] = dict(nom=cas['nom'], **attendu(C.calculer(cas)))
    with open(os.path.join(ICI, 'attendus.json'), 'w', encoding='utf-8') as f:
        json.dump(attendus, f, ensure_ascii=False, indent=0)
    print(len(tous), 'cas convertis')


if __name__ == '__main__':
    main()
