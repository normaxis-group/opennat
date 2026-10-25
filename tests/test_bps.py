# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Import d'un export du BPS (« BPS export 1 ») : projet valide, référence en usage maintenu, unités liées (fiche A41),
calendrier C-X12, crédits calculables, erreurs."""
import copy
import json
import os

import pytest

from opennat import effinature, projet
from opennat.credits import calcul
from opennat.effinature import bps

ICI = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.join(os.path.dirname(ICI), 'banc', 'effinature', 'bps_demonstration.export.json')


@pytest.fixture(scope='module')
def export():
    with open(EXPORT, encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture(scope='module')
def produit(export, tmp_path_factory):
    d = tmp_path_factory.mktemp('bps')
    return effinature.executer(EXPORT, str(d), dire=lambda s: None)


def test_projet_valide_et_ferme(produit):
    p = produit['projet']
    assert projet.valider(p) == []
    sp = p['parcelle']['surface']
    for unites in (p['etat_initial'], p['variantes'][0]['unites']):
        au_sol = sum(u['surface'] for u in unites if u['position'] in ('sol_pleine_terre', 'sol_sur_dalle', 'eau', 'lineaire'))
        assert au_sol == pytest.approx(sp, abs=1)


def test_reference_usage_maintenu_sans_obligation(produit):
    c = produit['credits']
    assert c['scenario_reference'] == {'defaut': 'usage_maintenu'}
    assert 'obligations' not in c
    assert len(produit['projet']['variantes']) == 1
    assert c['certification'].endswith('évalué, hors accréditation')
    assert 'certifi' not in c['certification'].replace('certification', '')


def test_unites_conservees_liees_a_l_etat_initial(produit):
    initiaux = {u['id'] for u in produit['projet']['etat_initial']}
    assert all(i.startswith(bps.PREFIXE_INITIAL) for i in initiaux)
    for u in produit['projet']['variantes'][0]['unites']:
        if u.get('statut') in ('conservee', 'amelioree'):
            assert u['liee'] in initiaux
    prairie = next(u for u in produit['projet']['variantes'][0]['unites'] if u['code'] == 'VB.26')
    assert prairie['liee'] == 'I-U-04'                                     # pelouse améliorée en prairie


def test_unite_liee_introuvable_comptee_creee(export):
    e = copy.deepcopy(export)
    u = next(x for x in e['projet_prevu']['unites'] if x['code'] == 'VB.26')
    u['liee'] = 'U-99'
    r = bps.importer_bps(e)
    v = next(x for x in r['projet']['variantes'][0]['unites'] if x['code'] == 'VB.26')
    assert v['statut'] == 'creee' and 'liee' not in v
    assert any('introuvable' in j for j in r['journal'])


def test_releves_et_calendrier(produit):
    c = produit['credits']
    assert [r['annee'] for r in c['releves']] == [1, 2]
    assert c['calendrier'][0] <= 3 and c['calendrier'][-1] == 50
    assert max(b - a for a, b in zip(c['calendrier'], c['calendrier'][1:])) <= 5
    assert all(u.get('criteres') or u.get('notes') for u in c['releves'][1]['unites']
               if u['code'] not in ('VB.1', 'VB.2', 'VB.3', 'VB.4'))


def test_credits_calculables(produit, tmp_path):
    for nom in ('projet', 'credits'):
        with open(tmp_path / f'{produit["identifiant"]}.{nom}.json', 'w', encoding='utf-8') as f:
            json.dump(produit[nom], f, ensure_ascii=False)
    res = calcul.calculer(str(tmp_path / f'{produit["identifiant"]}.credits.json'), tirages=40, graine=1)
    assert res is not None


@pytest.mark.parametrize('champ,valeur,message', [
    ('format', 'BPS export 0', 'format attendu'),
    ('contexte', {'zone_climatique': 'H3', 'typologie': 'tertiaire'}, 'zone_biogeographique'),
    ('etat_initial', {'unites': []}, 'état initial absent'),
    ('calendrier', [1, 2, 9, 50], 'C-X12'),
])
def test_erreurs(export, champ, valeur, message):
    e = copy.deepcopy(export)
    e[champ] = valeur
    with pytest.raises(effinature.ErreurImport, match=message):
        bps.importer_bps(e)


def test_type_inconnu(export):
    e = copy.deepcopy(export)
    e['projet_prevu']['unites'][0]['code'] = 'ZZ.9'
    with pytest.raises(bps.ErreurBps, match='inconnu'):
        bps.importer_bps(e)
