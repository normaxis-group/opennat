# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Tests unitaires par module : chaque test reprend le cas élémentaire de la fiche algorithme qu'il cite."""
import pytest

from opennat import agregation, climat, connectivite, hydrique, materiaux, nuisances, pretraitement, sol, temps
from opennat import habitats as H
from opennat.donnees import Parametres, Tables


@pytest.fixture(scope='module')
def P():
    return Parametres(Tables())


def U(**k):
    base = dict(id='u', position='sol_pleine_terre', surface=100.0)
    base.update(k)
    return base


def test_a04_codes(P):
    assert pretraitement.code_opennat(P, 'J4.2') == 'VB.2'
    assert pretraitement.code_opennat(P, 'E2.22') == 'E2.2'
    with pytest.raises(H.ErreurSaisie):
        pretraitement.code_opennat(P, 'Z9.9')


def test_a14_houppier_par_defaut(P):
    u = pretraitement.classer(P, dict(id='a', code='VB.18a', nombre_arbres=2, classe_diametre='moyen'), [])
    assert u['surface'] == pytest.approx(325.7, abs=0.1) and u['stade'] == 'M'


def test_a15_haie(P):
    u = pretraitement.classer(P, dict(id='h', code='FA.3', longueur=40, largeur=2), [])
    assert u['surface'] == 80 and u['position'] == 'lineaire'


def test_a16_facade(P):
    u = pretraitement.classer(P, dict(id='f', code='VB.15', longueur=30, hauteur=14), [])
    assert u['surface'] == 300


def test_a06_natures(P):
    assert sol.nature(P, U(code='VB.5', position='sol_sur_dalle', epaisseur=40)) == 'S06'
    assert sol.nature(P, U(code='VB.12', position='hors_sol_toiture', epaisseur=15)) == 'S05'
    assert sol.nature(P, U(code='VB.19', position='eau')) == 'S11'
    assert sol.coefficient(P, 'S06') == 0.7


def test_a10_score_essentiel(P):
    u = U(code='VB.8', criteres=dict(A='oui', B='oui', C='non', D='oui', E1='sans_objet', E2='sans_objet',
                                      F='sans_objet', G='sans_objet'))
    assert H.score(P, u, 'EU1', []) == 0.5


def test_a10_grille_vide_tous_non(P):
    j = []
    assert H.score(P, U(code='VB.26'), 'EP2', j) == 0.0 and j


def test_a11_boisement(P):
    noms = H.indicateurs_de(P, 'EB1')
    notes = dict(zip(noms, (3, 2, 3, 2, 3, 2, 2, 3, 2, 2, 1, 2, 2)))
    assert H.score(P, U(code='G1.A', notes=notes), 'EB1', []) == pytest.approx(16 / 26)


def test_a12_classes(P):
    assert H.etat(P, 0.6667)[1] == 'moyen' and H.etat(P, 0.5) == (0.75, 'mauvais')
    assert H.etat(P, None) == (1.0, 'sans état')


def test_a18_effet_de_taille(P):
    for a, k in ((100, 0.35), (500, 0.3734), (850, 0.4197), (1400, 0.4684), (5000, 0.6197), (44000, 1)):
        assert connectivite.k_taille(P, a) == pytest.approx(k, abs=1e-4)


def test_a19_connexion_deduite(P):
    assert connectivite.connexion(P, dict(distance_espace_naturel=120, surface_espace_naturel=20000)) == 'moyenne'
    assert connectivite.connexion(P, dict(distance_espace_naturel=0, surface_espace_naturel=20000)) == 'forte'


def test_a33_a35_materiaux(P):
    c = materiaux.climat(P, 1400, {'A1-A3': 350, 'A4-A5': 120, 'B': 400, 'C': 55, 'D': -40})
    assert c['inat_clim'] == pytest.approx(84748, rel=1e-3)
    b = materiaux.bois(P, [dict(volume=30)], [])
    assert b['inat_bois'] == pytest.approx(40111, rel=1e-4)               # option O2 : qualité de la coupe rase 0,639
    j = []
    b2 = materiaux.bois(P, [dict(volume=30, regime='coupe_selective')], j)
    assert b2['inat_bois'] == pytest.approx(40111, rel=1e-4) and j        # sans pièce : coupe rase (C-G5)
    assert materiaux.carrieres(P, dict(masse=1800)) == pytest.approx(1539)


def test_a36_pollution_convertie(P):
    """Fiche A36-2 (option P5) : chaque indicateur du RSEE multiplié par son facteur, puis sommé."""
    pol = {'106': 100.0, '107': 1.0, '108': 10.0, '109': 200.0, '116': 2100.0}
    r = materiaux.pollution_convertie(P, pol)
    assert r['detail']['116'] == pytest.approx(2100 * 0.5 / 2.5 / 365, rel=1e-3)
    assert r['detail']['108'] == pytest.approx(125.0)
    assert r['inat_pol'] == pytest.approx(sum(r['detail'].values()))


def test_a32_ponderation_des_batiments():
    r = materiaux.lecture_acv([dict(sref=100, ges={'A1-A3': 300}), dict(sref=300, ges={'A1-A3': 500})])
    assert r['ges']['A1-A3'] == pytest.approx(450)


def test_a38_bnat(P):
    pro = [dict(surface=150, c=0.2), dict(surface=850, c=1.0), dict(surface=500, c=0.6), dict(surface=100, c=None)]
    assert agregation.bnat(P, pro, 0.0, 2000)['bnat'] == pytest.approx(59.0)


def test_a43_a45_climat(P):
    an = climat.annee_type(P, 'H1a', '2_0', None)
    assert len(an.t) == 8760
    assert sum(an.et0) == pytest.approx(666, abs=1)
    rho = climat.recalage(P, an)
    assert rho[6] == pytest.approx(0.3776, abs=1e-4)
    alt = climat.annee_type(P, 'H1a', '2_0', 300)
    assert an.t[4716] - alt.t[4716] == pytest.approx(0.0065 * 133)


def test_a46_ponderation(P):
    assert climat.poids(P, 2040) == pytest.approx({'2_0': 0.5, '2_7': 0.5, '4_0': 0.0})
    w = climat.poids(P, 2076)
    assert w['2_7'] == pytest.approx(0.48) and w['4_0'] == pytest.approx(0.52)


def test_a48_reserve_utile(P):
    sol_site = dict(texture='limon', profondeur=1.0)
    assert hydrique.reserve_utile(P, U(code='VB.26'), sol_site, 'prairie') == pytest.approx(130)
    assert hydrique.reserve_utile(P, U(code='VB.18a', position='arbre', texture='sable'), sol_site, 'arbore') == \
        pytest.approx(75)
    assert hydrique.reserve_utile(P, U(code='VB.12', position='hors_sol_toiture', epaisseur=15), sol_site,
                                  'prairie') == pytest.approx(30)


def test_a49_a50_toiture(P):
    ctx = dict(zone_climatique='H1a', sol=dict(texture='limon', profondeur=1.0))
    u = U(code='VB.12', position='hors_sol_toiture', epaisseur=15, surface=500)
    w = hydrique.facteurs(P, u, ctx['sol'], ctx, {})
    assert w['kW']['2_0'] == pytest.approx(0.902, abs=1e-3)
    assert w['kW']['4_0'] == pytest.approx(0.846, abs=1e-3)


def test_a49_mare_marignane(P):
    an = climat.annee_type(P, 'H3', '2_0', None)
    assert hydrique.bilan_mare(P, an, 0.8, 0.3, 0.0)['assec_precoce']
    assert not hydrique.bilan_mare(P, an, 0.8, 0.3, 0.9)['assec_precoce']


def test_a51_a53_eclairage(P):
    assert nuisances.fraction_eclairee(P, 'H1a', 1, None) == pytest.approx(0.3732, abs=1e-4)
    assert nuisances.k_lumiere(P, dict(eclairage='L1'), 'H1a')[0] == pytest.approx(0.9160, abs=1e-4)
    assert nuisances.k_lumiere(P, dict(eclairage='L2'), 'H1a')[0] == pytest.approx(0.75)
    assert nuisances.facteur_spectral(P, 2700) == pytest.approx(0.8)
    assert nuisances.facteur_distance(P, 35) == pytest.approx(0.375)


def test_a54_maturation(P):
    attendu = {'herbacee': (0.273, 0.555, 0.818, 0.941, 1.0), 'arbustive': (0.074, 0.308, 0.668, 0.886, 1.0),
               'arboree': (0.020, 0.171, 0.546, 0.834, 1.0)}
    for forme, valeurs in attendu.items():
        for tau, g in zip((1, 2.5, 5, 7.5, 10), valeurs):
            assert temps.maturation(P, tau, 10, forme) == pytest.approx(g, abs=1e-3)


def test_a56_gestion(P):
    prairie = dict(code='VB.26', position='sol_pleine_terre', v=0.625, f=0.8333, S=0.6667)
    # sortie d'un plan : transition linéaire sur deux ans (A56-4, C-M3)
    assert temps.facteur_gestion(P, prairie, 'courante', 0) == pytest.approx(1.0)
    assert temps.facteur_gestion(P, prairie, 'courante', 1) == pytest.approx(1 - 0.4667 / 2, abs=1e-4)
    assert temps.facteur_gestion(P, prairie, 'courante', 2) == pytest.approx(0.5333, abs=1e-4)
    # gestion courante déclarée dès la livraison : valeur courante d'emblée
    assert temps.facteur_gestion(P, dict(prairie, gestion='courante'), 'courante', 0) == pytest.approx(0.5333, abs=1e-4)
    assert temps.facteur_gestion(P, prairie, 'abandon', 5) == pytest.approx(0.733, abs=1e-3)
    haie = dict(code='FA.3', position='lineaire', v=0.6667, f=0.875, S=0.75)
    assert temps.facteur_gestion(P, haie, 'courante', 3) == pytest.approx(0.75, abs=1e-4)


def test_a58_plantation(P):
    assert [temps.rang_plantation(P, m, d) for m, d in ((9, 18), (1, 18), (4, 6), (11, 3))] == [17, 23, 8, 2]


def test_a57_destruction(P):
    ini = [dict(id='f', code='VB.8', V=210.77), dict(id='a', code='VB.18a', stade='M', V=26.83)]
    total, det = temps.destruction(P, ini, [dict(statut='conservee', liee='a')], 5)
    assert total == pytest.approx(210.77) and det[0]['groupes'] == ['oiseaux']
    assert temps.destruction(P, ini, [], 9)[0] == 0
