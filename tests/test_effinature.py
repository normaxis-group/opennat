# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Import d'un dossier Effinature 8.1 : projet valide et calculable, crédits, calendrier C-X12, fiche de relevé."""
import copy
import csv
import json
import os

import pytest

from opennat import effinature, projet
from opennat.credits import calcul

ICI = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.join(os.path.dirname(ICI), 'banc', 'effinature', 'dossier_fictif.export.json')


@pytest.fixture(scope='module')
def export():
    with open(EXPORT, encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture(scope='module')
def produit(export, tmp_path_factory):
    d = tmp_path_factory.mktemp('effinature')
    return effinature.executer(EXPORT, str(d), dire=lambda s: None)


def test_projet_valide_et_ferme(produit):
    p = produit['projet']
    assert projet.valider(p) == []
    sp = p['parcelle']['surface']
    for v in [dict(unites=p['etat_initial'])] + p['variantes']:
        au_sol = sum(u['surface'] for u in v['unites']
                     if u['position'] in ('sol_pleine_terre', 'sol_sur_dalle', 'eau', 'lineaire'))
        assert au_sol == pytest.approx(sp, abs=1)


def test_correspondance_cbs(produit):
    u = {x['code']: x for x in produit['projet']['variantes'][0]['unites'] if x['id'].startswith('U1-') and x['id'][3:].isdigit()}
    assert u['VB.12']['position'] == 'hors_sol_toiture' and u['VB.12']['surface'] == 900
    assert u['VB.19']['surface'] == 150 and u['VB.3']['surface'] == 600
    arbres = [x for x in produit['projet']['variantes'][0]['unites'] if x['position'] == 'arbre']
    assert {a['code']: a['nombre_arbres'] for a in arbres} == {'VB.18a': 25, 'VB.18b': 5}


def test_aucun_etat_invente(produit):
    for v in produit['projet']['variantes']:
        assert not any(k in u for u in v['unites'] for k in ('score', 'criteres', 'notes'))


def test_calendrier_c_x12(produit):
    cal = produit['credits']['calendrier']
    assert cal[:2] == [1, 2] and cal[-1] == 50 and cal[0] <= 3
    assert all(b - a <= 5 for a, b in zip(cal, cal[1:]))


def test_calendrier_periode_hors_bornes(export):
    with pytest.raises(effinature.ErreurImport):
        effinature.importer(export, periode_hve=6)


def test_credits_calculables(produit):
    res = calcul.calculer(produit['fichiers'][f'{produit["identifiant"]}.credits.json'], tirages=100, graine=1)
    assert res['emissions']['plafond'] > 0


def test_fiche_aller_retour(produit, tmp_path):
    with open(produit['fichiers']['fiche'], encoding='utf-8-sig', newline='') as f:
        lignes = list(csv.DictReader(f, delimiter=';'))
    assert lignes and {l['grille'] for l in lignes} >= {'EP2', 'EU1'}
    for l in lignes:
        l.update(annee='1', date='2028-06-15', releve_par='Évaluateur fictif', reponse='oui')
    rempli = tmp_path / 'fiche.csv'
    with open(rempli, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, effinature.CHAMPS_FICHE, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    rel = effinature.releves_depuis_csv(str(rempli))
    assert [r['annee'] for r in rel] == [1] and rel[0]['ecologue'] == 'Évaluateur fictif'
    ids = {u['id'] for u in rel[0]['unites']}
    assert ids <= {u['id'] for u in produit['projet']['variantes'][0]['unites']}


@pytest.mark.parametrize('modif, message', [
    (lambda e: e.pop('reste_initial'), 'non décrits'),
    (lambda e: e['cbs'][0]['surfaces'].update(inconnue=10), 'nature de surface CBS inconnue'),
    (lambda e: e['contexte'].pop('zone_climatique'), 'zone_climatique'),
    (lambda e: e['cbs'][0]['surfaces'].update(pleine_terre=100), 'haies'),
])
def test_erreurs(export, modif, message):
    e = copy.deepcopy(export)
    modif(e)
    with pytest.raises(effinature.ErreurImport, match=message):
        effinature.importer(e)


def test_sans_plu_pas_de_credits(export):
    e = copy.deepcopy(export)
    e.pop('plu')
    r = effinature.importer(e)
    assert r['credits'] is None and len(r['projet']['variantes']) == 1
