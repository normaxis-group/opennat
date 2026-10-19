# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Voies de traitement de la pollution dans Inat (point P19, convention C-G8), à soumettre au Biodiversity Standard
Council (lot 5). Le script chiffre, sur un bâtiment médian, le poids de chaque indicateur de pollution du RSEE
quand on lui applique un facteur publié et ouvert, face au climat déjà compté dans Inat.

Bâtiment médian : médianes par m² de S_ref, phases A à C, de neuf bâtiments de RSEE réels d'études RE2020 du
groupe (fichiers clients hors dépôt, seules les médianes sont reprises ici).

Facteurs :
- GLOBIO 3.5 (PBL 2016), tableau 4.1 : MSA_N = 1 - 0,220 ln(NE + 1) pour les forêts, 0,189 pour les prairies, NE
  étant le dépôt d'azote au-delà de la charge critique en g/m²/an. Pente à NE = 0 : 0,220 m²HE·an par g d'azote
  en excès ; l'indicateur 109 (eutrophisation terrestre, dépassement cumulé, mol N éq.) mesure un excès d'azote
  au-delà des charges critiques, d'où 0,220 × 14,007 m²HE·an par mol N éq. Pente plus faible là où la charge
  critique est déjà dépassée (0,220 / (1 + NE)).
- ReCiPe 2016 v1.1, facteurs de passage à l'effet (perspective hiérarchiste) : climat sur les écosystèmes
  terrestres 2,8e-9, eutrophisation des eaux douces 6,71e-7 par kg P éq., eutrophisation marine 1,7e-9 par kg N
  éq., en espèce·an. Les indicateurs 107 et 108 du RSEE ont les mêmes unités que ces points médians ; 106
  (mol H+ éq.) et 116 (CTUe) n'en ont pas d'équivalent.

Usage : python -m banc.options_pollution   (écrit banc/options_pollution.json)
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat.donnees import Parametres, Tables  # noqa: E402

MEDIANES = {'101': 805.0, '106': 0.207, '107': 0.00805, '108': 0.0369, '109': 0.383, '116': 2.37}
UNITES = {'101': 'kg CO2 éq.', '106': 'mol H+ éq.', '107': 'kg P éq.', '108': 'kg N éq.', '109': 'mol N éq.',
          '116': 'CTUe'}
GLOBIO_PENTE = {'forets': 0.220, 'prairies': 0.189}
MASSE_MOLAIRE_N = 14.007
NE_FRANCE = (0.0, 1.0)            # excès de dépôt d'hypothèse, g/m²/an, pour borner la pente marginale
RECIPE = {'101': 2.8e-9, '107': 6.710726087059383e-07, '108': 1.7e-9}


def main():
    T = Tables()
    P = Parametres(T)
    cf = P.central('climat', 'facteur_caracterisation')
    # climat compté dans Inat pour ce bâtiment, toutes phases réunies au plus long (50 ans, borne haute)
    clim = MEDIANES['101'] * cf * P.central('phase_A1_A5', 'annees_persistance')
    eutro = {}
    for milieu, s in GLOBIO_PENTE.items():
        eutro[milieu] = [MEDIANES['109'] * s / (1 + ne) * MASSE_MOLAIRE_N for ne in NE_FRANCE]
    recipe = {k: MEDIANES[k] * v for k, v in RECIPE.items()}
    r = dict(medianes=MEDIANES, unites=UNITES, climat_inat_borne_haute=clim,
             eutrophisation_terrestre_m2he_an=eutro,
             part_du_climat=[x / clim for x in eutro['forets']],
             recipe_especes_an=recipe,
             recipe_part_du_climat={k: v / recipe['101'] for k, v in recipe.items() if k != '101'},
             m2he_an_par_mol_n=GLOBIO_PENTE['forets'] * MASSE_MOLAIRE_N)
    with open(os.path.join(ICI, 'options_pollution.json'), 'w', encoding='utf-8') as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return r


if __name__ == '__main__':
    main()
