# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Options de recalibrage du bois (conventions C-G4 et C-G5), à soumettre au Biodiversity Standard Council (lot 5).

Chaque option est appliquée à une copie des tables de `donnees/` ; les tables en vigueur ne sont pas modifiées.
Pour chaque option, le script calcule par le moteur : Inat des cas 7a (béton), 7b (bois non justifié) et 7c (bois
de coupe sélective justifiée), Inat de l'exemple de l'annexe C, le coût d'un m³ de bois, et l'écart avec l'étude
Carbone 4 (`banc/carbone4.py`).

Options :
- O0, référence : R = 2 m³ de bois rond par m³ de produit, qualités d'habitat des régimes de GLOBIO 3.5 ;
- O1, rendement alloué : R = 1,15, part du bois rond attribuée au sciage quand les coproduits (plaquettes, sciure,
  écorces) portent leur part, selon la pratique des déclarations environnementales de produits en bois ;
- O2, pondération relative : la perte d'habitat d'une forêt exploitée est fixée par rapport à celle d'une carrière,
  au rapport médian des trois méthodes d'ACV lues par l'audit (LC-IMPACT v2 France, ReCiPe 2016, EF 3.1 France) ;
- O3 : O1 et O2 ensemble.

Usage : python -m banc.options_bois   (écrit banc/options_bois.json)
"""
import csv
import json
import os
import shutil
import statistics
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)
from opennat import chaine, materiaux, projet  # noqa: E402
from opennat.donnees import Parametres, Tables  # noqa: E402

# Rapports « forêt exploitée / surface artificielle » en occupation, lus par l'audit (§ 2.4)
RAPPORTS = {
    'LC-IMPACT v2, France (forest, intensive / mineral extraction site), PDF par m²': 1.397e-14 / 6.089e-14,
    'ReCiPe 2016 (managed forest / artificial area), équivalent culture annuelle': 0.30 / 0.73,
    'EF 3.1, France (forest, intensive / mineral extraction site), points par m²·a': 77.936 / 204.88,
}
REGIMES = ('foret_plantation', 'foret_coupe_rase', 'foret_selective', 'foret_impact_reduit')
R_ALLOUE = 1.15
CAS = ('cas_7a', 'cas_7b', 'cas_7c', 'exemple_de_l_annexe_c')


def copier_tables(modifs: dict) -> str:
    """Copie donnees/ dans un dossier temporaire et remplace {(clé, paramètre): (valeur, min, max)}."""
    d = tempfile.mkdtemp(prefix='opennat_option_')
    dest = os.path.join(d, 'donnees')
    shutil.copytree(os.path.join(RACINE, 'donnees'), dest)
    f = os.path.join(dest, 'materiaux.csv')
    with open(f, encoding='utf-8') as fh:
        lignes = list(csv.DictReader(fh, delimiter=';'))
        champs = list(lignes[0].keys())
    for l in lignes:
        k = (l['cle'], l['parametre'])
        if k in modifs:
            v, a, b = modifs[k]
            l['valeur'], l['incertitude_min'], l['incertitude_max'] = (f'{x:.4g}' for x in (v, a, b))
    with open(f, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=champs, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    return dest


def options(T0: Tables) -> dict:
    perte_carriere = 1 - T0.lignes[('carriere', 'msa_usage')].valeur
    rapport = statistics.median(RAPPORTS.values())
    perte_ref = 1 - T0.lignes[('foret_coupe_rase', 'msa_usage')].valeur
    k = rapport * perte_carriere / perte_ref                 # multiplicateur des pertes de tous les régimes
    msa = {r: 1 - k * (1 - T0.lignes[(r, 'msa_usage')].valeur) for r in REGIMES}
    o2 = {(r, 'msa_usage'): (v, v, v) for r, v in msa.items()}
    o1 = {('foret', 'rapport_bois_rond_produit'): (R_ALLOUE, R_ALLOUE, 1.7)}
    return {'O0': ({}, 'référence (R = 2, régimes GLOBIO)'),
            'O1': (o1, f'rendement alloué (R = {R_ALLOUE})'),
            'O2': (o2, f'pondération relative (perte de la coupe rase {1 - msa["foret_coupe_rase"]:.3f})'),
            'O3': ({**o1, **o2}, 'O1 et O2')}, dict(rapport_median=rapport, multiplicateur=k, msa=msa)


def calculer(T: Tables) -> dict:
    res = {}
    for nom in CAS:
        P = Parametres(T)
        e, j = projet.normaliser(P, projet.lire(os.path.join(ICI, 'cas', nom + '.json')))
        g = chaine.calculer(P, e, e['variantes'][0], j)['etapes']['G']
        res[nom] = dict(inat=g['inat'], clim=g['inat_clim'], bois=g['inat_bois'], carr=g['inat_carr'])
    P = Parametres(T)
    par_m3 = materiaux.bois(P, [dict(regime='coupe_rase', volume=1.0)], [])['inat_bois']
    res['inat_par_m3_coupe_rase'] = par_m3
    res['rapport_7b_7a'] = res['cas_7b']['inat'] / res['cas_7a']['inat']
    res['rapport_7c_7a'] = res['cas_7c']['inat'] / res['cas_7a']['inat']
    # Carbone 4 : hausse d'usage des sols de la variante biosourcée (54 860 PDF.m².yr), volume OpenNAT équivalent,
    # et ajout du parquet massif seul (34 à 48 m³) au bâtiment béton de 3 000 m² (53,8 m²HE·an par m² en O0)
    res['volume_equivalent_carbone4'] = 54860.0 / par_m3
    res['parquet_par_m2'] = [v * par_m3 / 3000.0 for v in (33.6, 48.0)]
    return res


def main():
    T0 = Tables()
    opts, info = options(T0)
    sortie = dict(rapports=RAPPORTS, **info, options={})
    for code, (modifs, libelle) in opts.items():
        dest = copier_tables(modifs) if modifs else None
        try:
            T = Tables(dest) if dest else T0
            sortie['options'][code] = dict(libelle=libelle, **calculer(T))
        finally:
            if dest:
                shutil.rmtree(os.path.dirname(dest), ignore_errors=True)
    beton = sortie['options']['O0']['cas_7a']['inat']
    for o in sortie['options'].values():
        o['beton_inchange'] = abs(o['cas_7a']['inat'] - beton) / beton
    with open(os.path.join(ICI, 'options_bois.json'), 'w', encoding='utf-8') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    for code, o in sortie['options'].items():
        print(f"{code} {o['libelle']} : 7a {o['cas_7a']['inat']:.0f} ; 7b {o['cas_7b']['inat']:.0f} "
              f"({o['rapport_7b_7a']:.2f}) ; 7c {o['cas_7c']['inat']:.0f} ({o['rapport_7c_7a']:.2f}) ; annexe C "
              f"{o['exemple_de_l_annexe_c']['inat']:.0f} ; m³ {o['inat_par_m3_coupe_rase']:.0f} ; équivalent C4 "
              f"{o['volume_equivalent_carbone4']:.1f} m³ ; parquet {o['parquet_par_m2'][0]:.1f} à {o['parquet_par_m2'][1]:.1f}")
    print(json.dumps(info, ensure_ascii=False))
    return sortie


if __name__ == '__main__':
    main()
