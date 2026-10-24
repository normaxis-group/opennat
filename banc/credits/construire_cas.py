# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit les 20 cas du banc des crédits (`banc/credits/cas/`) à partir des trois exemples
(`banc/credits/exemples/`), puis écrit `banc/credits/attendus.json` avec le carnet de référence des crédits
(`outils/carnet_credits.py`), qui ne partage rien avec le moteur.

Usage : python banc/credits/construire_cas.py"""
import copy
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, 'outils'))
import carnet_credits as CC  # noqa: E402

EX, CAS = os.path.join(ICI, 'exemples'), os.path.join(ICI, 'cas')


def lire(nom):
    with open(os.path.join(EX, nom), encoding='utf-8') as f:
        return json.load(f)


def sc(a, n, e=False):
    return {'satisfaits': a, 'applicables': n, 'essentiel_echoue': e}


def rel(annee, scores):
    return {'annee': annee, 'unites': [dict(id=i, **({'score': s} if s else {})) for i, s in scores.items()]}


def ecrire(nom, base, projet, credits):
    p = copy.deepcopy(projet)
    p['projet']['identifiant'] = f'banc_credits_{nom}'
    c = copy.deepcopy(credits)
    c['identifiant'] = f'banc_credits_{nom}'
    c['projet'] = f'{nom}.projet.json'
    c['options'] = {'tirages': 0}
    for n, x in ((f'{nom}.projet.json', p), (f'{nom}.credits.json', c)):
        with open(os.path.join(CAS, n), 'w', encoding='utf-8') as f:
            json.dump(x, f, ensure_ascii=False, indent=1)
    return f'{nom}.credits.json'


def cas():
    pc, cc = lire('culture_prairie.projet.json'), lire('culture_prairie.credits.json')
    pf, cf = lire('friche_urbaine.projet.json'), lire('friche_urbaine.credits.json')
    pk, ck = lire('parking.projet.json'), lire('parking.credits.json')
    out = []
    out.append(('X01_culture_prairie', pc, cc))
    out.append(('X02_friche_urbaine', pf, cf))
    out.append(('X03_parking_obligations', pk, ck))
    calendrier = [1, 3, 5, 10, 15, 20, 30, 40, 50]
    c = copy.deepcopy(cc)
    c['releves'] = [rel(k, {'U1-1': sc(6, 7), 'U1-2': sc(6, 8)}) for k in calendrier]
    out.append(('X04_culture_calendrier_complet_plafond', pc, c))
    c = copy.deepcopy(cc)
    c['releves'] = [rel(k, {'U1-1': sc(6, 7), 'U1-2': sc(6, 8)}) for k in (1, 3, 5, 10)] + \
        [{'annee': 15, 'unites': [{'id': 'U1-1', 'code': 'VB.10'}, {'id': 'U1-2', 'score': sc(2, 8)}]}]
    out.append(('X05_culture_inversion', pc, c))
    c = copy.deepcopy(cc)
    c['releves'] = [rel(1, {'U1-1': sc(3, 7)}), rel(3, {'U1-1': sc(5, 7), 'U1-2': sc(5, 8)})]
    out.append(('X06_culture_unite_non_relevee', pc, c))
    c = copy.deepcopy(cc)
    c['obligations'] = {'gain_exige': 40000.0, 'liste': [{'objet': 'gain exigé par une certification',
                                                          'source': 'exemple du banc'}]}
    out.append(('X07_culture_gain_exige', pc, c))
    p = copy.deepcopy(pc)
    p['variantes'].append({'nom': 'Obligations', 'unites': [
        {'id': 'U2-1', 'code': 'E2.2', 'position': 'sol_pleine_terre', 'surface': 3000, 'tache': 'P1', 'score': sc(4, 7)},
        {'id': 'U2-2', 'code': 'I1.1', 'position': 'sol_pleine_terre', 'surface': 7000}]})
    c = copy.deepcopy(cc)
    c['obligations'] = {'variante': 'Obligations', 'liste': [{'objet': '3 000 m² de prairie', 'source': 'exemple'}]}
    out.append(('X08_culture_variante_obligations', p, c))
    c = copy.deepcopy(cf)
    c['scenario_reference'] = {'defaut': 'usage_maintenu'}
    out.append(('X09_friche_usage_maintenu', pf, c))
    c = copy.deepcopy(cf)
    c['scenario_reference']['unites']['U0-1']['annees_abandon'] = 0
    out.append(('X10_friche_abandon_recent', pf, c))
    c = copy.deepcopy(cf)
    c['scenario_reference']['unites']['U0-1']['annees_abandon'] = 20
    out.append(('X11_friche_abandon_ancien', pf, c))
    c = copy.deepcopy(ck)
    c['risque']['maitrise_fonciere'] = 'redhibitoire'
    out.append(('X12_parking_risque_redhibitoire', pk, c))
    c = copy.deepcopy(ck)
    c['risque'].update(financement_gestion='eleve', inondation_erosion='eleve')
    out.append(('X13_parking_reserve_maximale', pk, c))
    c = copy.deepcopy(ck)
    c['risque'].update(financement_gestion='eleve', inondation_erosion='eleve', gestionnaire='eleve')
    out.append(('X14_parking_risque_excessif', pk, c))
    c = copy.deepcopy(cc)
    c['releves'] = [rel(1, {'U1-1': sc(3, 7), 'U1-2': sc(3, 8)}), rel(2, {'U1-1': sc(4, 7), 'U1-2': sc(4, 8)}),
                    rel(3, {'U1-1': sc(5, 7), 'U1-2': sc(5, 8)})]
    out.append(('X15_culture_releve_hors_calendrier', pc, c))
    c = copy.deepcopy(cc)
    c['releves'] = []
    out.append(('X16_culture_previsionnel', pc, c))
    p = copy.deepcopy(pc)
    p['contexte'].update(zone_biogeographique='mediterraneenne', zone_climatique='H3')
    out.append(('X17_culture_mediterraneenne', p, cc))
    p = copy.deepcopy(pf)
    p['chantier']['mois_destruction'] = 5
    out.append(('X18_friche_destruction_en_mai', p, cf))
    c = copy.deepcopy(ck)
    del c['obligations']
    out.append(('X19_parking_sans_obligation', pk, c))
    c = copy.deepcopy(cc)
    c['releves'] = [rel(k, {'U1-1': sc(6, 7), 'U1-2': sc(6, 8)}) for k in (1, 3, 5)] + \
        [rel(10, {'U1-1': sc(3, 7), 'U1-2': sc(6, 8)}), rel(15, {'U1-1': sc(6, 7), 'U1-2': sc(6, 8)})]
    out.append(('X20_culture_degradation_puis_reprise', pc, c))
    return out


def main():
    os.makedirs(CAS, exist_ok=True)
    attendus = {}
    for nom, p, c in cas():
        f = ecrire(nom, None, p, c)
        attendus[f] = CC.calculer(os.path.join(CAS, f))
        print(f, round(attendus[f]['g_prev'], 1), attendus[f]['plafond'],
              [(round(l['gain'], 1), l['emis'], l['inversion']) for l in attendus[f]['verifications']])
    with open(os.path.join(ICI, 'attendus.json'), 'w', encoding='utf-8') as f:
        json.dump(attendus, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
