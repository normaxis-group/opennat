# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Tests de propriétés (lot 4, cahier des charges § 7) : sens de variation et invariances que toute version de la
méthode doit respecter, toutes choses égales par ailleurs. Chaque test part de l'exemple de l'annexe C, change une
seule donnée et vérifie le sens de l'effet, aux valeurs centrales ; le dernier vérifie la même propriété sur
chacun des tirages de l'analyse d'incertitude."""
import copy
import json
import os

import pytest

from opennat import chaine, incertitude, projet
from opennat.donnees import Parametres, Tables

ANNEXE_C = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'banc', 'cas',
                        'exemple_de_l_annexe_c.json')
EPS = 1e-9


@pytest.fixture(scope='module')
def T():
    return Tables()


def brut():
    with open(ANNEXE_C, encoding='utf-8') as f:
        return json.load(f)


def calcul(T, modifier=None) -> dict:
    """Calcule l'exemple de l'annexe C après `modifier(p)` ; rend les étapes de la variante de référence."""
    p = brut()
    if modifier:
        modifier(p)
    P = Parametres(T)
    e, j = projet.normaliser(P, p)
    return chaine.calculer(P, e, e['variantes'][0], j)


def ind(r, k):
    return r['etapes']['E3']['indicateurs'][k]


def unite(p, uid):
    for u in p['etat_initial'] + p['variantes'][0]['unites']:
        if u['id'] == uid:
            return u
    raise KeyError(uid)


@pytest.fixture(scope='module')
def ref(T):
    return calcul(T)


# Sens de variation sur le site (module E3)

def test_pleine_terre_ne_degrade_pas_cnat(T, ref):
    """Remplacer 100 m² de voirie par de la prairie urbaine : Cnat ne monte pas, Bnat ne baisse pas."""
    def m(p):
        unite(p, 'U1-2')['surface'] = 200
        p['variantes'][0]['unites'].append(dict(id='U1-9', code='VB.26', position='sol_pleine_terre', surface=100,
                                                tache='P2', score=dict(satisfaits=4, applicables=6)))
    r = calcul(T, m)
    assert ind(r, 'cnat') <= ind(ref, 'cnat') + EPS
    assert r['etapes']['E3']['bnat']['bnat'] >= ref['etapes']['E3']['bnat']['bnat'] - EPS
    assert r['etapes']['S']['pleine_terre'] >= ref['etapes']['S']['pleine_terre']


def test_meilleur_etat_initial_augmente_la_perte(T, ref):
    """Une prairie initiale en meilleur état vaut plus : V_0 et Cnat ne baissent pas."""
    r = calcul(T, lambda p: unite(p, 'U0-1').update(score=dict(satisfaits=4, applicables=4, essentiel_echoue=False)))
    assert r['etapes']['E3']['integration']['v0'] > ref['etapes']['E3']['integration']['v0']
    assert ind(r, 'cnat') >= ind(ref, 'cnat') - EPS


def test_meilleur_etat_projet_reduit_cnat(T, ref):
    r = calcul(T, lambda p: unite(p, 'U1-5').update(score=dict(satisfaits=3, applicables=3)))
    assert ind(r, 'cnat') <= ind(ref, 'cnat') + EPS


def test_chantier_plus_long_ne_reduit_pas_cnat(T, ref):
    r = calcul(T, lambda p: p['variantes'][0].update(chantier=dict(duree_mois=30)))
    assert ind(r, 'cnat') >= ind(ref, 'cnat') - EPS


def test_reservoir_accroit_la_perte(T, ref):
    """Le même site en réservoir de biodiversité : chaque valeur est multipliée, la perte aussi (Cnat > 0 ici)."""
    def m(p):
        for u in p['etat_initial'] + p['variantes'][0]['unites']:
            u['situation'] = 'reservoir'
    r = calcul(T, m)
    assert ind(ref, 'cnat') > 0 and ind(r, 'cnat') >= ind(ref, 'cnat') - EPS


def test_eclairage_plus_fort_ne_reduit_pas_cnat(T, ref):
    """Éclairage toute la nuit en 4 000 K (L2) au lieu de l'extinction à 1 h en 3 000 K (L1) ; puis sans éclairage."""
    r2 = calcul(T, lambda p: unite(p, 'U1-4').update(eclairage='L2'))
    r0 = calcul(T, lambda p: unite(p, 'U1-4').pop('eclairage'))
    assert ind(r0, 'cnat') <= ind(ref, 'cnat') + EPS <= ind(r2, 'cnat') + 2 * EPS


def test_plan_de_gestion_plus_long_ne_degrade_pas(T, ref):
    r = calcul(T, lambda p: p['gestion'].update(plan_annees=50))
    assert ind(r, 'cnat') <= ind(ref, 'cnat') + EPS


def test_substrat_plus_epais_ne_degrade_pas(T, ref):
    """Toiture de 30 cm au lieu de 15 : réserve utile plus grande, facteur hydrique au moins aussi bon."""
    r = calcul(T, lambda p: unite(p, 'U1-8').update(epaisseur=30))
    assert ind(r, 'cnat') <= ind(ref, 'cnat') + EPS


def test_destruction_en_periode_sensible_coute_plus(T):
    """Défricher en mai (nidification) coûte au moins autant qu'en janvier (fiche A57)."""
    mai = calcul(T, lambda p: p['chantier'].update(mois_debut=5, mois_destruction=5))
    janvier = calcul(T, lambda p: p['chantier'].update(mois_debut=5, mois_destruction=1))
    assert mai['etapes']['T']['supplement_destruction'] >= janvier['etapes']['T']['supplement_destruction']
    assert ind(mai, 'cnat') >= ind(janvier, 'cnat') - EPS


def test_arbre_conserve_protege_vaut_mieux(T, ref):
    r = calcul(T, lambda p: unite(p, 'U1-7').update(protection=False))
    assert ind(r, 'cnat') >= ind(ref, 'cnat') - EPS


# Sens de variation de la biodiversité grise (module G)

def test_ges_lineaires(T, ref):
    """Inat_clim est proportionnel aux émissions : doubler les GES double Inat_clim."""
    def m(p):
        for b in p['batiments']:
            b['ges'] = {k: 2 * v for k, v in b['ges'].items()}
    r = calcul(T, m)
    assert r['etapes']['G']['inat_clim'] == pytest.approx(2 * ref['etapes']['G']['inat_clim'], rel=1e-12)
    assert ind(r, 'inat') > ind(ref, 'inat')


def test_bois_justifie_moins_couteux(T, ref):
    sel = calcul(T, lambda p: p['variantes'][0]['materiaux']['bois'][0].update(regime='coupe_selective',
                                                                                justification='certificat'))
    sans = calcul(T, lambda p: p['variantes'][0]['materiaux']['bois'][0].update(regime='coupe_selective'))
    assert sel['etapes']['G']['inat_bois'] < ref['etapes']['G']['inat_bois']
    assert sans['etapes']['G']['inat_bois'] == pytest.approx(ref['etapes']['G']['inat_bois'], rel=1e-12)


def test_plus_de_materiaux_plus_d_inat(T, ref):
    def m(p):
        p['variantes'][0]['materiaux']['bois'][0]['volume'] *= 2
        p['variantes'][0]['materiaux']['granulats']['masse'] *= 2
    r = calcul(T, m)
    assert r['etapes']['G']['inat_bois'] == pytest.approx(2 * ref['etapes']['G']['inat_bois'], rel=1e-12)
    assert r['etapes']['G']['inat_carr'] == pytest.approx(2 * ref['etapes']['G']['inat_carr'], rel=1e-12)


# Identités et invariances

def test_identites_des_indicateurs(ref):
    e3, t = ref['etapes']['E3'], ref['etapes']['T']
    assert ind(ref, 'cnat') == pytest.approx(e3['integration']['i0'] - e3['integration']['i1']
                                             + t['supplement_destruction'], rel=1e-12)
    assert ind(ref, 'snat') == pytest.approx(-(ind(ref, 'cnat') + ind(ref, 'inat')), rel=1e-12)
    g = ref['etapes']['G']
    assert g['inat'] == pytest.approx(g['inat_clim'] + g['inat_bois'] + g['inat_carr'], rel=1e-12)


def test_ordre_et_noms_des_unites_sans_effet(T, ref):
    def m(p):
        p['etat_initial'].reverse()
        p['variantes'][0]['unites'].reverse()
        for u in p['variantes'][0]['unites']:
            u['id'] = 'X' + u['id']
            if 'liee' in u:
                pass                                   # le lien pointe vers l'état initial, dont les noms restent
    r = calcul(T, m)
    for k in ('cnat', 'inat', 'snat', 'cnat_30'):
        assert ind(r, k) == pytest.approx(ind(ref, k), rel=1e-12)


@pytest.mark.parametrize('uid', ['U1-3', 'U1-5', 'U0-3'])
def test_decoupage_d_une_unite_sans_effet(T, ref, uid):
    """Une unité coupée en deux moitiés identiques (même tache, même état) donne le même résultat."""
    def m(p):
        u = unite(p, uid)
        liste = p['etat_initial'] if u in p['etat_initial'] else p['variantes'][0]['unites']
        u['surface'] /= 2
        v = copy.deepcopy(u)
        v['id'] += 'b'
        liste.append(v)
    r = calcul(T, m)
    for k in ('cnat', 'snat'):
        assert ind(r, k) == pytest.approx(ind(ref, k), rel=1e-9)


def test_variante_identique_ecart_nul_sur_chaque_tirage(T):
    """Deux variantes identiques : l'écart de chaque indicateur est nul sur chacun des tirages (mêmes tirages)."""
    p = brut()
    v = copy.deepcopy(p['variantes'][0])
    v.update(nom='Copie', reference=False)
    p['variantes'].append(v)
    p['options'] = dict(tirages=50)
    e, _ = projet.normaliser(Parametres(T), p)
    inc = incertitude.analyser(T, e, None)
    ecarts = [x for x in inc[2]['Intervalle'] if x['indicateur'].startswith('ecart_')]
    assert len(ecarts) == 4
    assert all(x['p5'] == x['p50'] == x['p95'] == 0 for x in ecarts)


def test_plan_de_gestion_sur_chaque_tirage(T):
    """La propriété « plan de gestion plus long, Cnat pas plus fort » tient sur chaque tirage, pas seulement en
    valeur centrale : le 95e centile de l'écart de Cnat est négatif ou nul."""
    p = brut()
    v = copy.deepcopy(p['variantes'][0])
    v.update(nom='Plan de 50 ans', reference=False, gestion=dict(plan_annees=50))
    p['variantes'].append(v)
    p['options'] = dict(tirages=100)
    e, _ = projet.normaliser(Parametres(T), p)
    inc = incertitude.analyser(T, e, None)
    ec = next(x for x in inc[2]['Intervalle'] if x['indicateur'] == 'ecart_cnat')
    assert ec['p95'] <= EPS
