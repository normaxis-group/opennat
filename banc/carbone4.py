# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Contrôle d'ordre de grandeur du module G face à l'étude Carbone 4 (cahier des charges, § 7).

Carbone 4, « La biodiversité grise dans le bâtiment », position paper, octobre 2026 (IMPACT World+ par la
plateforme Darwin, métrique PDF.m².yr). Valeurs lues (audit, § 2.4) : bâtiment type de 50 logements, 3 000 m²,
structure béton, phases A1-A3, éléments modélisés couvrant environ 80 % de l'empreinte carbone des matériaux ;
272 000 PDF.m².yr dont pollution 51 %, changement climatique 38 %, changement d'usage des sols 11 % ; variante
biosourcée (façade ossature bois, fenêtres bois, parquet massif) 314 000 PDF.m².yr dont usage des sols 27 % ;
impact in situ d'environ 58 000 PDF.m².yr pour 1 250 m² de terrain naturel sur 50 ans.

Carbone 4 n'imprime ni l'empreinte carbone du bâtiment type ni ses quantités de matériaux. Le contrôle passe donc
par le m² de plancher et par des hypothèses OpenNAT déclarées ci-dessous, dont on donne la plage. Les deux
métriques (PDF d'IMPACT World+, m²HE fondés sur la MSA) ne sont pas commensurables : aucune conversion publiée n'a
été lue. On les rapproche ici à 1 pour 1, ce qui n'a de sens que pour un ordre de grandeur.

Usage : python -m banc.carbone4   (écrit banc/carbone4.json)
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat import materiaux  # noqa: E402
from opennat.donnees import Parametres, Tables  # noqa: E402

C4 = dict(surface=3000.0, total=272000.0, pollution=0.51, climat=0.38, sols=0.11, couverture_carbone=0.80,
          bio_total=314000.0, bio_sols=0.27, in_situ=58000.0, in_situ_parcelle=1250.0)

# Hypothèses OpenNAT (pas des données de Carbone 4)
GES_A1A3 = 470.0                 # kg CO2 éq./m² S_ref, valeur de l'exemple de l'annexe C ; plage étudiée ci-dessous
GES_PLAGE = (350.0, 600.0)
GRANULATS_PAR_M2 = 9500 / 4000   # t par m² S_ref, ratio du cas 7a (bâtiment béton)
BOIS_BETON_PAR_M2 = 20 / 4000    # m³ par m² S_ref, ratio du cas 7a
SURFACE_PARQUET = 2400.0         # m² de parquet massif : surface habitable d'environ 80 % des 3 000 m²
EPAISSEURS_PARQUET = (0.014, 0.020)   # m, lames de parquet massif courantes


def inat(P, sref, ges, bois_m3, granulats_t, regime='coupe_rase'):
    lots = [dict(regime=regime, volume=bois_m3, justification='x' if regime != 'coupe_rase' else '')] if bois_m3 else []
    bat = [dict(sref=sref, ges={'A1-A3': ges})]
    return materiaux.module_g(P, bat, dict(bois=lots, granulats=dict(masse=granulats_t)), [])


def main():
    T = Tables()
    P = Parametres(T)
    s = C4['surface']
    r = {}
    # 1. Carbone 4, par m² de plancher
    c4 = {k: C4['total'] * C4[k] / s for k in ('pollution', 'climat', 'sols')}
    c4['total'] = C4['total'] / s
    c4['perimetre_opennat'] = c4['climat'] + c4['sols']
    r['carbone4_par_m2'] = c4
    # 2. OpenNAT, bâtiment type béton, phases A1-A3 comme Carbone 4
    g = inat(P, s, GES_A1A3, BOIS_BETON_PAR_M2 * s, GRANULATS_PAR_M2 * s)
    on = dict(climat=g['inat_clim'] / s, bois=g['inat_bois'] / s, carrieres=g['inat_carr'] / s, total=g['inat'] / s)
    on['sols'] = on['bois'] + on['carrieres']
    r['opennat_beton_par_m2'] = on
    r['rapport_perimetre_commun'] = on['total'] / c4['perimetre_opennat']
    r['rapport_climat'] = on['climat'] / c4['climat']
    r['rapport_sols'] = on['sols'] / c4['sols']
    plage = [inat(P, s, x, BOIS_BETON_PAR_M2 * s, GRANULATS_PAR_M2 * s)['inat'] / s for x in GES_PLAGE]
    r['opennat_beton_plage_ges'] = dict(ges=GES_PLAGE, total_par_m2=plage,
                                        rapport=[x / c4['perimetre_opennat'] for x in plage])
    # GES A1-A3 pour lesquels le climat d'OpenNAT égale celui de Carbone 4, toutes choses égales
    cf_a = g['CF'] * P('phase_A1_A5', 'annees_persistance')
    r['cf_par_kg_a1a3'] = cf_a
    r['ges_equivalence_climat'] = c4['climat'] / cf_a
    r['ges_equivalence_climat_80'] = c4['climat'] / C4['couverture_carbone'] / cf_a
    # 3. Bois : coût OpenNAT par m³ de produit, et volume qui égalerait la hausse d'usage des sols de Carbone 4
    par_m3 = {reg: inat(P, s, 0, 1.0, 0, reg)['inat_bois'] for reg in ('coupe_rase', 'coupe_selective')}
    hausse_c4 = C4['bio_total'] * C4['bio_sols'] - C4['total'] * C4['sols']
    r['bois'] = dict(inat_par_m3=par_m3, hausse_sols_carbone4=hausse_c4,
                     volume_equivalent=hausse_c4 / par_m3['coupe_rase'],
                     volume_parquet_seul=[SURFACE_PARQUET * e for e in EPAISSEURS_PARQUET])
    r['bois']['rapport_minimal'] = min(r['bois']['volume_parquet_seul']) / r['bois']['volume_equivalent']
    # 4. In situ : Carbone 4 par m² de terrain naturel, face à OpenNAT sur une prairie construite (cas 2)
    with open(os.path.join(ICI, 'attendus.json'), encoding='utf-8') as f:
        cas2 = json.load(f)['cas_2.json']
    r['in_situ'] = dict(carbone4_par_m2_parcelle=C4['in_situ'] / C4['in_situ_parcelle'],
                        opennat_cas2_par_m2_parcelle=cas2['cnat'] / 10000.0,
                        carbone4_part_in_situ=C4['in_situ'] / (C4['in_situ'] + C4['total']),
                        opennat_cas2_part=cas2['cnat'] / (cas2['cnat'] + cas2['inat']))
    with open(os.path.join(ICI, 'carbone4.json'), 'w', encoding='utf-8') as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return r


if __name__ == '__main__':
    main()
