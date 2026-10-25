# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Crédits OpenNAT : banc des 20 cas, propriétés, reproductibilité, schémas du RSNat-C, table des crédits."""
import copy
import json
import os

import numpy as np
import pytest

from banc.credits import comparer
from opennat.credits import calcul, rsnatc
from opennat.credits.donnees import TableCredits

ICI = os.path.dirname(os.path.abspath(__file__))
CAS = os.path.join(os.path.dirname(ICI), 'banc', 'credits', 'cas')
EX = os.path.join(os.path.dirname(ICI), 'banc', 'credits', 'exemples')
ATT = comparer.attendus()


@pytest.mark.parametrize('nom', sorted(ATT))
def test_banc_des_credits(nom):
    assert comparer.ecarts_cas(nom, ATT[nom]) == []


def test_table_des_credits():
    t = TableCredits()
    assert t('credits', 'taille_credit') == 1000
    assert t.calendrier() == [1, 3, 5, 10, 15, 20, 30, 40, 50]
    assert t('credits', 'neutraliser_difficulte') == 1


def _variante(tmp_path, nom, modifier):
    """Copie un cas du banc dans tmp_path après modification du fichier crédits ; renvoie son chemin."""
    with open(os.path.join(CAS, nom), encoding='utf-8') as f:
        c = json.load(f)
    with open(os.path.join(CAS, c['projet']), encoding='utf-8') as f:
        p = json.load(f)
    modifier(c, p)
    (tmp_path / c['projet']).write_text(json.dumps(p, ensure_ascii=False), encoding='utf-8')
    chemin = tmp_path / nom
    chemin.write_text(json.dumps(c, ensure_ascii=False), encoding='utf-8')
    return str(chemin)


def test_meilleur_etat_jamais_moins_de_credits(tmp_path):
    def mieux(c, p):
        for r in c['releves']:
            for u in r['unites']:
                if 'score' in u:
                    u['score']['satisfaits'] = u['score']['applicables']
    a = calcul.calculer(os.path.join(CAS, 'X04_culture_calendrier_complet_plafond.credits.json'), tirages=0)
    b = calcul.calculer(_variante(tmp_path, 'X04_culture_calendrier_complet_plafond.credits.json', mieux), tirages=0)
    for x, y in zip(a['emissions']['verifications'], b['emissions']['verifications']):
        assert y['credits_emis_cumul'] >= x['credits_emis_cumul']
        assert y['gain'] >= x['gain'] - 1e-9


def test_obligation_plus_forte_jamais_plus_de_credits(tmp_path):
    def plus(c, p):
        c['obligations']['gain_exige'] = 80000.0
    a = calcul.calculer(os.path.join(CAS, 'X07_culture_gain_exige.credits.json'), tirages=0)
    b = calcul.calculer(_variante(tmp_path, 'X07_culture_gain_exige.credits.json', plus), tirages=0)
    assert b['emissions']['plafond'] <= a['emissions']['plafond']
    for x, y in zip(a['gains']['verifications'], b['gains']['verifications']):
        assert y['gain']['centrale'] <= x['gain']['centrale'] + 1e-9


def test_emissions_bornees_par_le_plafond():
    for nom in ATT:
        r = calcul.calculer(os.path.join(CAS, nom), tirages=0)
        em = r['emissions']
        for l in em['verifications']:
            assert l['credits_emis_cumul'] <= em['plafond']
            assert l['emission'] >= 0
        cumul = [l['credits_emis_cumul'] for l in em['verifications']]
        assert cumul == sorted(cumul)


def test_inversion_constatee():
    r = calcul.calculer(os.path.join(CAS, 'X05_culture_inversion.credits.json'), tirages=0)
    derniere = r['emissions']['verifications'][-1]
    assert derniere['inversion'] > 0 and derniere['emission'] == 0


def test_eligibilite_et_risque():
    r = calcul.calculer(os.path.join(CAS, 'X12_parking_risque_redhibitoire.credits.json'), tirages=0)
    assert not r['risque']['eligible'] and not r['eligibilite']['eligible']
    r = calcul.calculer(os.path.join(CAS, 'X13_parking_reserve_maximale.credits.json'), tirages=0)
    assert r['risque']['taux'] == pytest.approx(0.40) and r['risque']['eligible']
    r = calcul.calculer(os.path.join(CAS, 'X14_parking_risque_excessif.credits.json'), tirages=0)
    assert not r['risque']['eligible']


def test_tirages_et_centile_prudent():
    r = calcul.calculer(os.path.join(EX, 'culture_prairie.credits.json'), tirages=200)
    g = r['gains']['prevision']['gain']
    assert g['p10'] < g['p50'] and g['retenu'] == pytest.approx(g['p10'])
    assert r['eligibilite']['indicatif']                                     # moins de 1 000 tirages


def test_tirages_independants_du_decoupage():
    a = calcul.calculer(os.path.join(EX, 'culture_prairie.credits.json'), tirages=60)
    prep_bloc = os.path.join(EX, 'culture_prairie.credits.json')
    with open(prep_bloc, encoding='utf-8') as f:
        c = json.load(f)
    p = calcul.preparer(prep_bloc, 60)
    p['e']['options']['bloc'] = 7
    g = calcul.calculer_gains(p)
    assert g['prevision']['gain']['p10'] == pytest.approx(a['gains']['prevision']['gain']['p10'], rel=1e-12)
    assert c['options']['tirages'] == 1000


def test_rsnatc_reproductible_et_conforme(tmp_path):
    d1 = rsnatc.construire(calcul.calculer(os.path.join(CAS, 'X05_culture_inversion.credits.json'), tirages=0),
                           '2026-10-24')
    d2 = rsnatc.construire(calcul.calculer(os.path.join(CAS, 'X05_culture_inversion.credits.json'), tirages=0),
                           '2026-10-25')
    assert d1['Empreinte'] == d2['Empreinte']
    err = rsnatc.ecrire(d1, str(tmp_path))
    assert err == {'json': [], 'xml': []}


def test_cout_de_revient():
    prep = {'c': {'couts': {'restauration': 100.0, 'gestion_annuelle': 2.0, 'releve': 1.0, 'verification': 3.0}},
            'TC': TableCredits(), 'calendrier': TableCredits().calendrier()}
    k = calcul.cout(prep, 10)
    assert k['total'] == pytest.approx(100 + 2 * 50 + 9 * 1 + 9 * 3)
    assert k['par_credit'] == pytest.approx(k['total'] / 10)


def test_calendrier_propre_cale_sur_une_certification(tmp_path):
    """Convention C-X12 : calendrier propre accepté s'il commence au plus tard à l'année 3, laisse cinq ans au plus
    entre deux relevés et finit à l'année 50 ; la certification et le calendrier sont publiés dans le RSNat-C."""
    hve = [3] + list(range(6, 51, 3))[:-1] + [50]

    def propre(c, p):
        c['calendrier'] = hve
        c['certification'] = 'Effinature HVE'
    r = calcul.calculer(_variante(tmp_path, 'X05_culture_inversion.credits.json', propre), tirages=0)
    assert r['prep']['calendrier'] == hve
    d = rsnatc.construire(r, '2026-10-24')
    assert d['Projet']['Certification'] == 'Effinature HVE'
    assert d['Projet']['Calendrier'] == ' '.join(map(str, hve))
    assert rsnatc.ecrire(d, str(tmp_path)) == {'json': [], 'xml': []}
    for mauvais in ([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 3, 10, 50], [1, 3, 5, 10, 15, 20], [3, 1, 50]):
        def faux(c, p, k=mauvais):
            c['calendrier'] = k
        with pytest.raises(calcul.ErreurCredits):
            calcul.calculer(_variante(tmp_path, 'X05_culture_inversion.credits.json', faux), tirages=0)


def test_difficulte_neutralisee_seulement_dans_les_credits():
    """La convention C-X19 ne touche pas OpenNAT 1 : sans la clé interne, la difficulté s'applique."""
    from opennat import chaine, projet
    from opennat.donnees import Parametres, Tables
    P = Parametres(Tables())
    e, j = projet.normaliser(P, projet.lire(os.path.join(EX, 'culture_prairie.projet.json')))
    r = chaine.calculer(P, e, e['variantes'][0], j)
    assert any(u['D'] < 1 for u in r['projet'])
    v = copy.deepcopy(e['variantes'][0])
    for u in v['unites']:
        u['difficulte_neutralisee'] = True
    r2 = chaine.calculer(P, e, v, [])
    assert all(u['D'] == 1 for u in r2['projet'])
    assert np.isclose(r['etapes']['E3']['integration']['i0'], r2['etapes']['E3']['integration']['i0'])
