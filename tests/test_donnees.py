# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
import csv
import os
import shutil

import numpy as np
import pytest

from opennat.donnees import DONNEES, ErreurDonnees, ErreurParametre, Parametres, Tables, tirages


@pytest.fixture(scope='module')
def T():
    return Tables()


def _copie(tmp_path, modifier):
    d = tmp_path / 'donnees'
    shutil.copytree(DONNEES, d)
    chemin = d / 'connectivite.csv'
    with open(chemin, encoding='utf-8') as f:
        lignes = list(csv.DictReader(f, delimiter=';'))
        champs = list(lignes[0].keys())
    modifier(lignes)
    with open(chemin, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=champs, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    return str(d)


def test_chargement(T):
    assert len(T.lignes) > 2000
    assert len(T.empreinte) == 64
    assert T.nomenclature['VB.26']['grille_etat'] == 'EP2'


def test_ligne_sans_source_refusee(tmp_path):
    def sans_source(l):
        l[0]['source'] = ''
    with pytest.raises(ErreurDonnees, match=r'connectivite\.csv, ligne 2 .* aucune source'):
        Tables(_copie(tmp_path, sans_source))


def test_valeur_hors_plage_refusee(tmp_path):
    def hors(l):
        l[0]['valeur'] = '9'
    with pytest.raises(ErreurDonnees, match='hors de sa plage'):
        Tables(_copie(tmp_path, hors))


def test_convention_inconnue_refusee(tmp_path):
    def conv(l):
        l[0]['convention'] = 'C-Z9'
    with pytest.raises(ErreurDonnees, match='C-Z9 absente'):
        Tables(_copie(tmp_path, conv))


def test_parametre_absent(T):
    with pytest.raises(ErreurParametre):
        Parametres(T)('inconnu', 'rien')


def test_tirages_triangulaires_reproductibles(T):
    l = T.lignes[('*', 'exposant_aire_especes')]
    a = tirages(l, 7, 5000)
    b = tirages(l, 7, 5000)
    assert np.array_equal(a, b)
    assert a.min() >= l.a and a.max() <= l.b
    assert np.mean(a) == pytest.approx((l.a + l.b + l.valeur) / 3, rel=0.02)


def test_tirages_independants_du_decoupage(T):
    P1 = Parametres(T, 11, 10, 0, 10)
    P2 = Parametres(T, 11, 10, 4, 7)
    assert np.array_equal(P1('*', 'exposant_aire_especes')[4:7], P2('*', 'exposant_aire_especes'))


def test_mois_tires_entiers(T):
    x = Parametres(T, 3, 50, 0, 50)('*', 'saison_chiropteres_debut')
    assert np.all(x == np.rint(x))
