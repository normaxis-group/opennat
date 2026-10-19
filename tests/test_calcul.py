# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Tests de bout en bout : fichier projet, RSEE, calcul complet, variantes, RSNat, déterminisme, reprise, banc."""
import copy
import json
import os
import shutil

import pytest

from opennat import calcul, projet, rsee
from opennat.__main__ import main
from opennat.donnees import Parametres, Tables

ICI = os.path.dirname(os.path.abspath(__file__))
BANC = os.path.join(os.path.dirname(ICI), 'banc')
ANNEXE_C = os.path.join(BANC, 'cas', 'exemple_de_l_annexe_c.json')


def lire(chemin):
    with open(chemin, encoding='utf-8') as f:
        return json.load(f)


def test_projet_invalide_refuse():
    p = lire(ANNEXE_C)
    p['contexte']['zone_climatique'] = 'H9'
    del p['parcelle']['surface']
    p['etat_initial'][0]['inconnu'] = 1
    err = projet.valider(p)
    assert any('H9' in e for e in err) and any('surface' in e for e in err) and any('inconnu' in e for e in err)
    with pytest.raises(projet.ErreurProjet):
        projet.normaliser(Parametres(Tables()), p)


def test_valeurs_par_defaut_au_journal():
    p = lire(ANNEXE_C)
    del p['gestion'], p['contexte']['sol']
    e, j = projet.normaliser(Parametres(Tables()), p)
    assert e['gestion']['plan_annees'] == 0 and e['contexte']['sol']['texture'] == 'limon'
    assert any('C-M3' in x for x in j) and any('C-W4' in x for x in j)


RSEE_FABRIQUE = '''<?xml version="1.0" encoding="UTF-8"?>
<projet><Datas_Comp><donnees_generales><operation><zone_climatique>Zone H1a</zone_climatique></operation>
</donnees_generales></Datas_Comp><RSET><Entree_Projet><Simu><Departement>78</Departement><Altitude>160</Altitude>
</Simu></Entree_Projet></RSET><RSEnv><entree_projet><batiment><index>1</index><nom>B</nom><sref>1400</sref>
<emprise_au_sol>700</emprise_au_sol><duree_chantier>18</duree_chantier></batiment><parcelle>
<surface_parcelle>2000</surface_parcelle><surface_veg>850</surface_veg><surface_imper>1000</surface_imper>
<surface_arrosee>0</surface_arrosee></parcelle><date_etude>2026-10-01</date_etude></entree_projet><sortie_projet>
<batiment><index>1</index><contributeur><composant><indicateurs_acv_collection><indicateur ref="101">
<valeur_phase_acv ref="A1-A3">350</valeur_phase_acv><valeur_phase_acv ref="A4-A5">100</valeur_phase_acv>
<valeur_phase_acv ref="B">400</valeur_phase_acv><valeur_phase_acv ref="C">55</valeur_phase_acv>
<valeur_phase_acv ref="D">-40</valeur_phase_acv></indicateur><indicateur ref="116">
<valeur_phase_acv ref="A1-A3">1.5</valeur_phase_acv></indicateur></indicateurs_acv_collection></composant>
<chantier><indicateurs_acv_collection><indicateur ref="101"><valeur_phase_acv ref="A4-A5">20</valeur_phase_acv>
</indicateur></indicateurs_acv_collection></chantier></contributeur></batiment></sortie_projet></RSEnv></projet>'''


def test_lecture_rsee_fabrique(tmp_path):
    f = tmp_path / 'r.xml'
    f.write_text(RSEE_FABRIQUE, encoding='utf-8')
    r = rsee.lire(str(f))
    assert r['zone_climatique'] == 'H1a' and r['departement'] == '78' and r['altitude'] == 160
    assert r['parcelle']['surface'] == 2000
    b = r['batiments'][0]
    assert b['ges']['A4-A5'] == 120 and b['pollution']['116']['A1-A3'] == 1.5


def test_calcul_avec_rsee_et_variantes(tmp_path):
    (tmp_path / 'r.xml').write_text(RSEE_FABRIQUE, encoding='utf-8')
    p = lire(ANNEXE_C)
    del p['batiments']
    p['projet']['rsee'] = 'r.xml'
    del p['contexte']['zone_climatique']
    p['contexte']['zone_climatique'] = 'H1a'
    v2 = copy.deepcopy(p['variantes'][0])
    v2.update(nom='Bois justifié', reference=False)
    v2['materiaux']['bois'] = [dict(regime='coupe_selective', volume=30, justification='certificat')]
    p['variantes'].append(v2)
    p['options'] = dict(tirages=4, bloc=2, graine=5)
    (tmp_path / 'p.json').write_text(json.dumps(p), encoding='utf-8')
    r = calcul.calculer(str(tmp_path / 'p.json'), str(tmp_path / 'res'), dire=lambda s: None)
    assert not any(r['erreurs_schema'].values())
    i1 = r['resultats'][0]['etapes']['G']['inat_bois']
    i2 = r['resultats'][1]['etapes']['G']['inat_bois']
    assert i2 - i1 == pytest.approx(-22222, abs=1)                          # fiche A41, cas élémentaire
    assert any(x['indicateur'] == 'ecart_inat' for x in r['incertitude'][2]['Intervalle'])
    d = r['dossier']
    for f in ('00_entrees.json', '12_E4_tirages.csv', 'rsnat.xml', 'rsnat.json', 'journal.txt', 'empreinte.txt',
              'variante_2/09_T_trajectoires.csv', 'variante_1/08_W_hydrique.json'):
        assert os.path.exists(os.path.join(d, f)), f


def test_ligne_de_commande_deterministe_et_reprise(tmp_path):
    p = lire(ANNEXE_C)
    p['options'] = dict(tirages=6, bloc=2, graine=9)
    (tmp_path / 'p.json').write_text(json.dumps(p), encoding='utf-8')
    a = calcul.calculer(str(tmp_path / 'p.json'), str(tmp_path / 'a'), dire=lambda s: None)
    b = calcul.calculer(str(tmp_path / 'p.json'), str(tmp_path / 'b'), dire=lambda s: None)
    ta = open(os.path.join(a['dossier'], '12_E4_tirages.csv'), encoding='utf-8').read()
    tb = open(os.path.join(b['dossier'], '12_E4_tirages.csv'), encoding='utf-8').read()
    assert ta == tb                                                            # exigence E7
    lignes = ta.splitlines()
    with open(os.path.join(b['dossier'], '12_E4_tirages.csv'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes[:3]) + '\n')                                   # calcul interrompu après un bloc
    c = calcul.calculer(str(tmp_path / 'p.json'), reprendre=b['dossier'], dire=lambda s: None)
    assert open(os.path.join(c['dossier'], '12_E4_tirages.csv'), encoding='utf-8').read() == ta
    p['parcelle']['surface'] = 2001
    (tmp_path / 'p.json').write_text(json.dumps(p), encoding='utf-8')
    with pytest.raises(calcul.ErreurReprise):
        calcul.calculer(str(tmp_path / 'p.json'), reprendre=b['dossier'], dire=lambda s: None)
    assert main(['controle']) == 0


def test_fermeture_bloquante(tmp_path):
    p = lire(ANNEXE_C)
    p['etat_initial'][0]['surface'] = 1100
    p['options'] = dict(tirages=0)
    (tmp_path / 'p.json').write_text(json.dumps(p), encoding='utf-8')
    assert main(['calcul', str(tmp_path / 'p.json'), '--sortie', str(tmp_path)]) == 2


@pytest.mark.parametrize('cas', ['exemple_de_l_annexe_c', 'cas_6', 'cas_7b', 'cas_d17', 'cas_d25', 'cas_d28'])
def test_banc_extrait(cas):
    from banc import comparer
    assert comparer.main(cas + '.json')


def test_propriete_pleine_terre():
    """Lot 4, test de propriété : remplacer de la voirie par de la prairie ne dégrade pas Cnat."""
    from opennat import chaine
    P = Parametres(Tables())
    e, j = projet.normaliser(P, lire(ANNEXE_C))
    v = e['variantes'][0]
    r0 = chaine.calculer(P, e, v, [])
    v2 = copy.deepcopy(v)
    for u in v2['unites']:
        if u['id'] == 'U1-2':
            u['surface'] = 200
    v2['unites'].append(dict(id='U1-9', code='VB.26', surface=100, tache='P2',
                             score=dict(satisfaits=4, applicables=6)))
    r1 = chaine.calculer(P, e, v2, [])
    assert r1['etapes']['E3']['indicateurs']['cnat'] < r0['etapes']['E3']['indicateurs']['cnat']
    assert r1['etapes']['E3']['bnat']['bnat'] > r0['etapes']['E3']['bnat']['bnat']
