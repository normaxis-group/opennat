# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Banc de validation et de non-régression (lot 4).

1. Les huit cas tests du cahier des charges (§ 7) et l'exemple de l'annexe C retrouvent le carnet de référence à
   0,1 % près, puis leurs résultats attendus qualitatifs (partie 8 de l'édition complète) sont vérifiés.
2. Les 73 cas du banc retrouvent le carnet de référence (exigence E10).
3. Les 38 930 grandeurs de l'instantané de non-régression n'ont pas bougé, et la version des données en vigueur
   figure au journal des versions.
4. Le contrôle dimensionnel (exigence E12) ne trouve aucune incohérence, et il en trouve une quand on en crée une.
"""
import json
import os
import shutil

import pytest

from banc import comparer, regression
from opennat import dimensions
from opennat.donnees import Tables

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATT = comparer.attendus()
HUIT = ['cas_1.json', 'cas_2.json', 'cas_3.json', 'cas_4.json', 'cas_5.json', 'cas_6.json', 'cas_7a.json',
        'cas_7b.json', 'cas_7c.json', 'cas_8a.json', 'cas_8b.json', 'cas_8c.json', 'exemple_de_l_annexe_c.json']


@pytest.fixture(scope='module')
def T():
    return Tables()


@pytest.mark.parametrize('nom', HUIT)
def test_huit_cas_du_cahier_des_charges(T, nom):
    assert comparer.ecarts_cas(T, nom, ATT[nom]) == []


def test_resultats_attendus_des_huit_cas():
    """Ce que le cahier des charges attend de chaque situation type (partie 8, « Résultat attendu »)."""
    a = {k[:-5]: v for k, v in ATT.items()}
    assert a['cas_1']['cnat'] < 0                                                    # friche : gain
    assert a['cas_2']['cnat'] > 0 and a['cas_2']['cnat_rel'] > 0.5                   # prairie : forte perte
    assert a['cas_3']['pt'] == 0 and a['cas_3']['cnat'] < 0                          # dalle et toiture
    assert -0.25 * abs(a['cas_1']['cnat']) < a['cas_4']['cnat'] < 0                   # réhabilitation : petit gain
    assert a['cas_5']['cnat'] > a['cas_2']['cnat']                                   # réservoir : perte plus forte
    assert a['cas_6']['cnat'] < 0 and a['cas_6']['dm'] > 0.25 * abs(a['cas_6']['cnat'])   # mare et haies : dette
    assert a['cas_7b']['inat'] > a['cas_7c']['inat'] > a['cas_7a']['inat']           # bois face au béton
    assert a['cas_7a']['cnat'] == a['cas_7b']['cnat'] == a['cas_7c']['cnat']          # même site
    assert a['cas_8a']['cnat'] < a['cas_8b']['cnat'] < a['cas_8c']['cnat'] < 0        # méditerranée face au continent


@pytest.mark.parametrize('nom', sorted(set(ATT) - set(HUIT)))
def test_banc_complet(T, nom):
    assert comparer.ecarts_cas(T, nom, ATT[nom]) == []


def test_non_regression():
    with open(regression.INSTANTANE, encoding='utf-8') as f:
        ancien = json.load(f)
    ecarts = regression.comparer(regression.calculer_tout(dire=lambda s: None), ancien)
    assert not ecarts, '\n'.join(ecarts[:20])


def test_version_des_donnees_au_journal(T):
    with open(os.path.join(RACINE, 'JOURNAL_DES_VERSIONS.md'), encoding='utf-8') as f:
        journal = f.read()
    assert T.empreinte in journal, 'tables modifiées : inscrire la nouvelle version des données au journal des versions'


def test_controle_dimensionnel(T):
    assert dimensions.verifier(T) == []


def test_controle_dimensionnel_detecte_une_incoherence(tmp_path):
    dossier = tmp_path / 'donnees'
    shutil.copytree(os.path.join(RACINE, 'donnees'), dossier)
    f = dossier / 'materiaux.csv'
    f.write_text(f.read_text(encoding='utf-8').replace('m²·an par t', 'm² par t'), encoding='utf-8')
    dimensions.CATALOGUE.setdefault('m² par t', dimensions.d(L=2, M=-1))
    err = dimensions.verifier(Tables(str(dossier)))
    assert any('A35-1' in x for x in err)
    g = dossier / 'nuisances.csv'
    g.write_text(g.read_text(encoding='utf-8').replace(';dB(A);', ';décibels;', 1), encoding='utf-8')
    err = dimensions.verifier(Tables(str(dossier)))
    assert any('décibels' in x and 'absente du catalogue' in x for x in err)
