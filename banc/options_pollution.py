# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Ponts entre les indicateurs de pollution du RSEE et la biodiversité grise (point P19, convention C-G8),
lots 5 et 6. Le script chiffre, sur un bâtiment médian, chaque indicateur converti en PDF·m²·an par un facteur
publié, et le compare au climat déjà compté dans Inat (une fraction d'espèces perdue sur un m² pendant un an est
rapprochée d'un m²HE·an, faute de conversion publiée entre PDF et MSA).

Bâtiment médian : médianes par m² de S_ref, phases A à C, de neuf bâtiments de RSEE réels d'études RE2020 du
groupe (fichiers clients hors dépôt ; seules les médianes et le maximum d'écotoxicité sont repris ici).

Ponts (sources dans le dépôt, sauf mention) :
- 116, écotoxicité (CTUe = PAF·m³·jour) : IMPACT World+ (Bulle et al. 2019, supplément, CC BY 4.0) convertit
  PAF en PDF par un facteur de gravité de 0,5 et les m³ en m² par une profondeur moyenne de 2,5 m ;
- 106, acidification (dépassement cumulé, mol H+ éq.) : passage en kg SO2 éq. par la composition du flux acide
  (facteurs EF de 1,31, 0,74 et 3,02 mol H+ éq. par kg de SO2, NOx et NH3, relus sur la méthode EF
  d'acidification par dépassement cumulé publiée par ÖKOBAU.DAT, version 01.03.010 ; facteurs ReCiPe 2016 de 1, 0,36 et 1,96 kg SO2 éq. par kg), puis ReCiPe 2016 : 2,12e-7
  espèce·an par kg SO2 éq., divisé par la densité d'espèces terrestres de 1,48e-8 espèce par m² ;
- 109, eutrophisation terrestre (dépassement cumulé, mol N éq.) : GLOBIO 3.5, tableau 4.1, pente de 0,220 MSA
  par g d'azote en excès par m² et par an (forêts), soit 0,220 × 14,007 m²HE·an par mol N éq. ; bornée par la
  pente là où la charge critique est déjà dépassée d'1 g/m²/an ;
- 107, eutrophisation des eaux douces (kg P éq.) : ReCiPe 2016, 6,71e-7 espèce·an par kg P éq., divisé par la
  densité d'espèces d'eau douce de 7,89e-10 espèce par m³ et la profondeur de 2,5 m d'IMPACT World+ ; borne
  basse : facteur d'effet d'IMPACT World+, 11,4 PDF·m²·an par kg PO4 éq. (3,066 kg PO4 par kg P) ;
- 108, eutrophisation marine (kg N éq.) : IMPACT World+, facteur d'effet empirique de 12,5 PDF·m²·an par kg
  d'azote déposé en zone côtière.

Usage : python -m banc.options_pollution   (écrit banc/options_pollution.json)
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat.donnees import Parametres, Tables  # noqa: E402

MEDIANES = {'101': 805.0, '106': 0.207, '107': 0.00805, '108': 0.0369, '109': 0.383, '116': 2.37}
MAXIMUM_116 = 450.0
UNITES = {'101': 'kg CO2 éq.', '106': 'mol H+ éq.', '107': 'kg P éq.', '108': 'kg N éq.', '109': 'mol N éq.',
          '116': 'CTUe'}

# Facteurs publiés
IW_GRAVITE, IW_PROFONDEUR, JOURS_PAR_AN = 0.5, 2.5, 365.0
EF_AE = {'SO2': 1.31, 'NOx': 0.74, 'NH3': 3.02}                  # mol H+ éq. par kg, méthode EF (ÖKOBAU.DAT 01.03.010)
RECIPE_AP = {'SO2': 1.0, 'NOx': 0.36, 'NH3': 1.96}               # kg SO2 éq. par kg
RECIPE_ACIDE = 2.12e-7                                           # espèce·an par kg SO2 éq.
RECIPE_CLIMAT_TERRESTRE = 2.8e-9                                 # espèce·an par kg CO2 éq. (hiérarchiste)
RECIPE_EAU_DOUCE_P = 6.710726087059383e-07                      # espèce·an par kg P éq.
DENSITE_TERRESTRE, DENSITE_EAU_DOUCE = 1.48e-8, 7.89e-10         # espèces par m², par m³
IW_EAU_DOUCE_PO4, PO4_PAR_P = 11.4, 3.066
IW_MARINE_N = 12.5
GLOBIO_PENTE_FORETS, MASSE_MOLAIRE_N, NE_DEPASSE = 0.220, 14.007, 1.0


def facteurs() -> dict:
    """PDF·m²·an (ou m²HE·an) par unité de chaque indicateur : (borne basse, borne haute)."""
    so2_par_mol = [RECIPE_AP[g] / EF_AE[g] for g in EF_AE]
    acide = RECIPE_ACIDE / DENSITE_TERRESTRE
    eau_douce_haut = RECIPE_EAU_DOUCE_P / DENSITE_EAU_DOUCE / IW_PROFONDEUR
    globio = GLOBIO_PENTE_FORETS * MASSE_MOLAIRE_N
    return {
        '116': (IW_GRAVITE / IW_PROFONDEUR / JOURS_PAR_AN,) * 2,
        '106': (min(so2_par_mol) * acide, max(so2_par_mol) * acide),
        '109': (globio / (1 + NE_DEPASSE), globio),
        '107': (IW_EAU_DOUCE_PO4 * PO4_PAR_P, eau_douce_haut),
        '108': (IW_MARINE_N,) * 2,
    }


def main():
    T = Tables()
    P = Parametres(T)
    cf = P.central('climat', 'facteur_caracterisation') * P.central('phase_A1_A5', 'annees_persistance')
    clim = MEDIANES['101'] * cf                      # borne haute : toutes les émissions comptées sur 50 ans
    f = facteurs()
    par_indicateur = {k: [MEDIANES[k] * x for x in v] for k, v in f.items()}
    total = [sum(v[i] for v in par_indicateur.values()) for i in (0, 1)]
    r = dict(medianes=MEDIANES, unites=UNITES, facteurs=f, par_m2=par_indicateur,
             ecotoxicite_maximum=MAXIMUM_116 * f['116'][0],
             total_pollution_par_m2=total, climat_inat_par_m2=clim,
             part_du_climat=[x / clim for x in total],
             climat_recipe_pdf_m2_an_par_kg=RECIPE_CLIMAT_TERRESTRE / DENSITE_TERRESTRE,
             climat_opennat_m2he_an_par_kg=cf,
             carbone4_pollution_sur_climat=0.51 / 0.38)
    with open(os.path.join(ICI, 'options_pollution.json'), 'w', encoding='utf-8') as fh:
        json.dump(r, fh, ensure_ascii=False, indent=1)
    for k, v in par_indicateur.items():
        print(f'{k} ({UNITES[k]}) : facteur {f[k][0]:.3g} à {f[k][1]:.3g} ; par m² {v[0]:.3g} à {v[1]:.3g}')
    print(f'pollution {total[0]:.2f} à {total[1]:.2f} par m², climat {clim:.1f} : {r["part_du_climat"][0]:.1%} à '
          f'{r["part_du_climat"][1]:.1%} ; écotoxicité au maximum {r["ecotoxicite_maximum"]:.3f} ; climat ReCiPe '
          f'{r["climat_recipe_pdf_m2_an_par_kg"]:.3f} PDF·m²·an/kg contre OpenNAT {cf:.4f}')
    return r


if __name__ == '__main__':
    main()
