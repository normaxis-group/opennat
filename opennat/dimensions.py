# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Contrôle dimensionnel automatique (exigence E12).

Chaque unité écrite dans les tables de `donnees/` et dans la spécification du RSNat est traduite en dimensions
de base : longueur L, masse M, temps T, température Θ et habitat équivalent HE (un m²HE est un m² d'habitat de
qualité 1 ; la MSA est donc un HE par m²). Une unité absente du catalogue est une erreur : toute unité nouvelle
doit y être déclarée.

Les équations des fiches sont ensuite vérifiées terme à terme : les unités de chaque facteur sont lues dans les
tables (colonne `unite`), si bien qu'une unité modifiée dans un CSV qui casse une équation est signalée. Une
somme exige des termes de même dimension ; un exposant ou l'argument d'une exponentielle, d'un logarithme ou d'une
racine non entière doit être sans dimension.

Usage : python -m opennat controle (les tables puis les dimensions), ou dimensions.verifier(Tables()).
"""
from __future__ import annotations

from fractions import Fraction as Fr

BASES = ('L', 'M', 'T', 'Θ', 'HE')


def d(L=0, M=0, T=0, Θ=0, HE=0) -> tuple:
    return tuple(Fr(x) for x in (L, M, T, Θ, HE))


UN = d()
KPA = d(L=-1, M=1, T=-2)
MJ = d(L=2, M=1, T=-2)

# Unité écrite -> dimensions. None : unité propre à chaque indicateur, jamais agrégée (indicateurs de pollution
# du RSEE, point P19), donc hors contrôle.
CATALOGUE = {
    # sans dimension
    '': UN, 'sans unité': UN, 'poids': UN, 'fraction': UN, 'score 1 à 3': UN, 'note 1 à 3': UN, 'booléen': UN,
    'centile': UN, 'm³/m³': UN, 'fraction de la parcelle': UN, 'tirages': UN, 'note': UN, 'score total': UN,
    'score S': UN, "part d'emprise du bâti": UN, 'paramètres': UN, 'indicateurs': UN, 'fraction de la valeur': UN,
    'points': UN, "code d'indicateur": UN, "fraction de l'emprise totale du projet": UN,
    'fraction de la valeur initiale intégrée': UN, 'm³ de bois rond par m³ de produit': UN, 'degré': UN, '°': UN,
    'dB(A)': UN, '%': UN,
    # temps et calendrier
    'an': d(T=1), 'année': d(T=1), 'mois': d(T=1), 'jours': d(T=1), 'heure': d(T=1), 'heure légale': d(T=1),
    'jours-équivalents': d(T=1), 'par an': d(T=-1), 'par 100 jours-équivalents': d(T=-1),
    # longueurs, surfaces, volumes, flux d'eau
    'm': d(L=1), 'cm': d(L=1), 'mm': d(L=1), 'm-1': d(L=-1), 'm²': d(L=2), 'm³': d(L=3), 'ha': d(L=2),
    'mm/mois': d(L=1, T=-1), 'mm/an': d(L=1, T=-1), 'mm/jour': d(L=1, T=-1), 'mm/h': d(L=1, T=-1),
    'm/s': d(L=1, T=-1), 's/m': d(L=-1, T=1), 'm³ par ha et par an': d(L=1, T=-1),
    # température, pression, rayonnement (FAO-56)
    '°C': d(Θ=1), 'K': d(Θ=1), 'K/m': d(L=-1, Θ=1), 'kPa': KPA, 'hPa': KPA,
    'kPa-0,5': tuple(-x / 2 for x in KPA), 'kPa/°C': d(L=-1, M=1, T=-2, Θ=-1), 'kPa-1 °C-1 x kPa': d(Θ=-1),
    'W/m²': d(M=1, T=-3), 'MJ m-2 h-1': d(M=1, T=-3), 'MJ K-4 m-2 h-1': d(M=1, T=-3, Θ=-4),
    'mm par MJ/m²': d(L=1, M=-1, T=2), 'K mm s³ Mg-1 h-1': d(L=1, M=-1, T=2, Θ=1),
    # habitat équivalent et biodiversité grise
    'MSA': d(HE=1), 'MSA par °C': d(HE=1, Θ=-1), 'm²HE/m²': d(HE=1), 'm²HE': d(L=2, HE=1),
    'm²HE·an': d(L=2, T=1, HE=1), 'm²HE·an/m²': d(T=1, HE=1),
    'm²HE par kg CO2 éq.': d(L=2, M=-1, HE=1), 'm²HE/kg CO2 éq.': d(L=2, M=-1, HE=1),
    'm²HE par kg CO2 éq. et par an': d(L=2, M=-1, T=-1, HE=1), 'm²HE/kg CO2 éq./an': d(L=2, M=-1, T=-1, HE=1),
    '°C par kg CO2': d(M=-1, Θ=1), 'kg CO2 éq./m² Sref': d(L=-2, M=1), 'kg': d(M=1), 't': d(M=1),
    'm²·an par t': d(L=2, M=-1, T=1), 'm²·an par m³': d(L=-1, T=1),
    "unité de l'annexe II": None, "unité de l'annexe II par m² Sref": None,
}

# Constantes de conversion de `unites.py` : ce sont des changements d'échelle (sans dimension), sauf celles qui
# portent une unité physique.
CONSTANTES = {'MM_PAR_M': UN, 'MM_PAR_CM': UN, 'M2_PAR_HA': UN, 'MJ_PAR_WH': UN, 'KPA_PAR_HPA': UN,
              'MOIS_PAR_AN': UN, 'POINTS_PAR_UNITE': UN, 'JOURS_PAR_SENSIBILITE': UN, 'POURCENT': UN}


class ErreurDimension(Exception):
    pass


def dimension(unite: str):
    if unite not in CATALOGUE:
        raise ErreurDimension(f'unité « {unite} » absente du catalogue dimensionnel (opennat/dimensions.py)')
    return CATALOGUE[unite]


def texte(dim) -> str:
    if dim is None:
        return 'non contrôlée'
    t = ' '.join(f'{b}{"" if e == 1 else e}' for b, e in zip(BASES, dim) if e)
    return t or 'sans dimension'


def _produit(T, facteurs) -> tuple:
    """facteurs : liste de (source, exposant) ; source 'D:clé:paramètre' (unité lue dans les tables),
    'U:unité' (unité d'une entrée) ou 'C:NOM' (constante de unites.py)."""
    tot = [Fr(0)] * len(BASES)
    for src, expo in facteurs:
        genre, _, reste = src.partition(':')
        if genre == 'D':
            cle, par = reste.rsplit(':', 1)
            dim = dimension(T.lignes[(cle, par)].unite)
        elif genre == 'U':
            dim = dimension(reste)
        else:
            dim = CONSTANTES[reste]
        if dim is None:
            raise ErreurDimension(f'{src} : unité non contrôlée dans une équation')
        tot = [a + Fr(expo) * b for a, b in zip(tot, dim)]
    return tuple(tot)


def D(cle, par, expo=1):
    return (f'D:{cle}:{par}', expo)


def U_(unite, expo=1):
    return (f'U:{unite}', expo)


def C(nom, expo=1):
    return (f'C:{nom}', expo)


# Équations : (fiche, libellé, unité du résultat (ou facteur 'D:' dont on lit l'unité), termes additifs, chacun
# produit de facteurs). Un terme 'sans dimension' sert aux arguments d'exposant, d'exponentielle et de logarithme.
EQUATIONS = [
    ('A08-1', 'pleine terre = A(S08) / S_p', 'fraction', [[U_('m²'), U_('m²', -1)]]),
    ('A10-3 et A12-1', 'f = f_min + (1 - f_min) x S', 'sans unité',
     [[D('*', 'facteur_etat_minimum')], [D('*', 'facteur_etat_minimum'), U_('fraction')]]),
    ('A13-1 [H4]', 'V^H = A x v x f x f_sol x m', 'm²HE',
     [[U_('m²'), D('VB.8', 'valeur_intrinseque'), U_('sans unité'), D('S01', 'coefficient_sol'),
       D('situation_reservoir', 'multiplicateur_situation')]]),
    ('A13-2', 'v plafonnée à v_max', 'm²HE/m²', [[D('VB.8', 'valeur_intrinseque')], [D('*', 'plafond_valeur_unitaire')]]),
    ('A17-3 et A18 [C1]', 'k_taille = (A_tache / A_ref) ^ z : base sans dimension', 'sans unité',
     [[U_('m²'), D('*', 'surface_reference', -1)], [D('*', 'exposant_aire_especes')]]),
    ('A21', 'bruit : L_projet comparé au seuil', 'dB(A)', [[U_('dB(A)')], [D('*', 'seuil_bruit_milieu_ouvert')]]),
    ('A22 et A53', 'éclairage : distance comparée aux distances d\'effet', 'm',
     [[U_('m')], [D('*', 'distance_effet_plein')], [D('*', 'distance_effet_nul')]]),
    ('A25-2 [H5]', 'V = min(V_max x A ; V^H x k_C x k_N x k_E)', 'm²HE',
     [[D('*', 'plafond_valeur_unitaire'), U_('m²')],
      [U_('m²HE'), D('connexion_forte', 'multiplicateur_connectivite'), D('lumiere_aucune', 'facteur_lumiere'),
       D('alimentation_naturelle', 'facteur_eau')]]),
    ('A29-1', 'délai d_u = k_délai x d_type', 'an', [[D('zone_atlantique', 'multiplicateur_delai'), U_('an')]]),
    ('A31-2 et A37 [A1]', 'I = somme des V(t) x Δt', 'm²HE·an', [[U_('m²HE'), U_('an')]]),
    ('A37-1 [A1]', 'Cnat = I_0 - I_1 + ΔI_ch', 'm²HE·an', [[U_('m²HE·an')], [U_('m²HE·an')], [U_('m²HE·an')]]),
    ('A37-2', 'Cnat moyen = Cnat / N', 'm²HE', [[U_('m²HE·an'), D('*', 'periode_reference', -1)]]),
    ('A37-3', 'Cnat relatif = Cnat / I_0, comparé au seuil de niveau', 'fraction de la valeur initiale intégrée',
     [[U_('m²HE·an'), U_('m²HE·an', -1)], [D('niveau_1', 'cnat_max_relatif')]]),
    ('A37-6 [A2]', 'Snat = -(Cnat + Inat)', 'm²HE·an', [[U_('m²HE·an')], [U_('m²HE·an')]]),
    ('A37-7', 'ratios Cnat / S_p et Inat / S_ref', 'm²HE·an/m²', [[U_('m²HE·an'), U_('m²', -1)]]),
    ('A38', 'Bnat = 100 x somme(A_u x n_u) / S_p, comparé au seuil', 'points',
     [[C('POINTS_PAR_UNITE'), U_('m²'), U_('sans unité'), U_('m²', -1)], [D('logement_emprise_37', 'bnat_min')]]),
    ('A33-1 [G3]', 'CF = S_terres x (1 - p_cult) x (π / δ) x TCRE', D('climat', 'facteur_caracterisation')[0],
     [[D('climat', 'surface_terres_emergees_hors_glaces'), D('climat', 'part_cultures_infrastructures'),
       D('climat', 'perte_msa_par_degre'), D('climat', 'facteur_retard_reponse', -1), D('climat', 'tcre')]]),
    ('A33-2 [G2]', 'Inat_clim,p = CF x S_ref x GES_p x a_p', 'm²HE·an',
     [[D('climat', 'facteur_caracterisation'), U_('m²'), U_('kg CO2 éq./m² Sref'),
       D('phase_A1_A5', 'annees_persistance')]]),
    ('A34-1', 'occupation = 10 000 / P_bio x r_rond', 'm²·an par m³',
     [[C('M2_PAR_HA'), D('foret', 'production_biologique', -1), D('foret', 'rapport_bois_rond_produit')]]),
    ('A34-2 [G4]', 'Inat_bois = V x (1 + R) x occupation x (1 - MSA_r)', 'm²HE·an',
     [[U_('m³'), U_('m²·an par m³'), D('foret_coupe_rase', 'msa_usage')]]),
    ('A35-1 [G5]', 'Inat_carr = m x (1 + R) x occ_t x (1 - MSA_carr)', 'm²HE·an',
     [[U_('t'), D('carriere', 'occupation_par_tonne'), D('carriere', 'msa_usage')]]),
    ('A35-2 [G1, G6]', 'Inat = Inat_clim + Inat_bois + Inat_carr', 'm²HE·an',
     [[U_('m²HE·an')], [U_('m²HE·an')], [U_('m²HE·an')]]),
    ('A43-2', 'T = T_station - gradient x Δz', '°C', [[U_('°C')], [D('iso2533', 'gradient_thermique'), U_('m')]]),
    ('A43-3', 'P = P_station x ((T0 - gradient x Δz) / T0) ^ 5,26', 'kPa',
     [[U_('hPa'), C('KPA_PAR_HPA')]]),
    ('A43-3', 'rapport de températures sans dimension', 'sans unité',
     [[D('iso2533', 'gradient_thermique'), U_('m'), D('fao56', 'pression_temperature_reference', -1)],
      [D('fao56', 'pression_exposant')]]),
    ('A44-1', 'Δ = 4 098 x e_s / (T + 237,3)²', 'kPa/°C',
     [[D('fao56', 'pente_saturation'), D('fao56', 'saturation_a'), D('fao56', 'saturation_c', -2)]]),
    ('A43-4 et A44-1', 'e_s = 0,6108 exp(17,27 T / (T + 237,3)) : argument sans dimension', 'sans unité',
     [[D('fao56', 'saturation_b'), U_('°C'), D('fao56', 'saturation_c', -1)]]),
    ('A44-2', 'u_2 = u_z x 4,87 / ln(67,8 z - 5,42) : argument sans dimension', 'sans unité',
     [[D('fao56', 'vent_b'), U_('m')], [D('fao56', 'vent_c')]]),
    ('A44-3', 'R_s = rayonnement x 0,0036', 'MJ m-2 h-1', [[U_('W/m²'), C('MJ_PAR_WH')]]),
    ('A44-4', 'R_so = (0,75 + 2 x 10^-5 z) R_a', 'MJ m-2 h-1',
     [[D('fao56', 'rso_a'), D('fao56', 'constante_solaire_horaire')],
      [D('fao56', 'rso_b'), U_('m'), D('fao56', 'constante_solaire_horaire')]]),
    ('A44-5', 'R_nl = σ T⁴ (0,34 - 0,14 √e_a)(1,35 R_s/R_so - 0,35)', 'MJ m-2 h-1',
     [[D('fao56', 'stefan_boltzmann_horaire'), U_('K', 4), D('fao56', 'rnl_a')],
      [D('fao56', 'stefan_boltzmann_horaire'), U_('K', 4), D('fao56', 'rnl_b'), U_('kPa', Fr(1, 2))]]),
    ('A44-6', 'γ = 0,665 x 10^-3 P', 'kPa/°C', [[D('fao56', 'psychrometrique'), U_('kPa')]]),
    ('A44-6', 'ET_0, premier terme : 0,408 Δ (R_n - G)', 'mm/h',
     [[D('fao56', 'coefficient_rayonnement'), U_('kPa/°C'), U_('MJ m-2 h-1'), U_('kPa/°C', -1)]]),
    ('A44-6', 'ET_0, second terme : γ C_n / (T + 273) u_2 (e_s - e_a)', 'mm/h',
     [[U_('kPa/°C'), D('fao56', 'cn_horaire'), D('fao56', 'decalage_kelvin', -1), U_('m/s'), U_('kPa'),
       U_('kPa/°C', -1)]]),
    ('A44-6', 'dénominateur Δ + γ (1 + C_d u_2)', 'kPa/°C',
     [[U_('kPa/°C')], [U_('kPa/°C'), D('fao56', 'cd_horaire'), U_('m/s')]]),
    ('A48-1', 'RU toiture = 10 x e (cm) x réserve volumique', 'mm',
     [[C('MM_PAR_CM'), U_('cm'), D('substrat', 'reserve_volumique')]]),
    ('A48-2', 'RU sol = 1 000 x (θ_cc - θ_pf) x min(z_r ; profondeur)', 'mm',
     [[C('MM_PAR_M'), D('sable', 'theta_capacite_champ'), D('gazon', 'profondeur_racinaire')],
      [C('MM_PAR_M'), D('sable', 'theta_point_fletrissement'), D('*', 'profondeur_sol_defaut')]]),
    ('A49-3', 'REW = 1 - D / RU, comparée au seuil', 'fraction',
     [[U_('mm'), U_('mm', -1)], [D('*', 'seuil_rew_stress')]]),
    ('A49-5', 'D = D - P x ρ x (1 + apport) + ET_a (pas horaire)', 'mm',
     [[U_('mm')], [U_('mm/h'), U_('heure'), D('*', 'coefficient_ruissellement')], [U_('mm/h'), U_('heure'),
                                                                                   D('gazon', 'kc_saison')]]),
    ('A49 (mare)', 'h = h + P (1 + bv) - ET - infiltration', 'mm',
     [[U_('mm')], [U_('mm/h'), U_('heure')], [D('fond_etanche', 'infiltration'), U_('jours')]]),
    ('A50-2', 'k_W = 1 - s x max(0 ; IS - tolérance) / 100', 'sans unité',
     [[D('gazon', 'sensibilite_stress'), D('*', 'tolerance_stress'), C('JOURS_PAR_SENSIBILITE', -1)],
      [D('*', 'facteur_hydrique_minimum')]]),
    ('A53', 'k_L = 1 - p_max x x_nuit x s(CCT) x g(d)', 'sans unité',
     [[D('*', 'perte_maximale'), U_('fraction'), D('ambre', 'facteur_spectral'), U_('sans unité')]]),
    ('A54', 'g = ((1 - exp(-3 τ / d)) / (1 - exp(-3))) ^ c : argument sans dimension', 'sans unité',
     [[U_('an'), D('*', 'delai_friche_herbacee', -1)], [D('herbacee', 'exposant_forme')]]),
    ('A55-1', 'âge à l\'année t = t - 1 - mois de chantier / 12', 'an', [[U_('an')], [U_('mois'), C('MOIS_PAR_AN', -1)]]),
    ('A57-3', 'ΔI_ch = V x s(mois) x perte', 'm²HE·an',
     [[U_('m²HE'), D('oiseaux', 'sensibilite_m05'), D('*', 'perte_destruction_sensible')]]),
]


def _resultat(T, res):
    if res.startswith('D:'):
        cle, par = res[2:].rsplit(':', 1)
        return dimension(T.lignes[(cle, par)].unite), T.lignes[(cle, par)].unite
    return dimension(res), res


def verifier_unites_tables(T) -> list[str]:
    err = []
    for (cle, par), l in sorted(T.lignes.items()):
        if l.unite not in CATALOGUE:
            err.append(f'{l.table} {cle} {par} : unité « {l.unite} » absente du catalogue dimensionnel')
    par_param = {}
    for (cle, par), l in T.lignes.items():
        if l.unite in CATALOGUE and CATALOGUE[l.unite] is not None:
            par_param.setdefault((l.table, par), set()).add(CATALOGUE[l.unite])
    for (table, par), dims in sorted(par_param.items()):
        if len(dims) > 1:
            err.append(f'{table} {par} : même paramètre, dimensions différentes selon la clé '
                       f'({", ".join(sorted(texte(x) for x in dims))})')
    return err


def verifier_equations(T) -> list[str]:
    err = []
    for fiche, libelle, res, termes in EQUATIONS:
        try:
            dim_res, unite_res = _resultat(T, res)
            for i, t in enumerate(termes, 1):
                dt = _produit(T, t)
                if dt != dim_res:
                    err.append(f'fiche {fiche}, {libelle} : terme {i} en {texte(dt)}, résultat attendu en '
                               f'« {unite_res} » ({texte(dim_res)})')
        except (ErreurDimension, KeyError) as x:
            err.append(f'fiche {fiche}, {libelle} : {x}')
    return err


def verifier_rsnat() -> list[str]:
    from . import rsnat_spec as S
    err = []

    def parcourir(n):
        if isinstance(n, S.F):
            if n.unite not in CATALOGUE:
                err.append(f'RSNat {n.nom} : unité « {n.unite} » absente du catalogue dimensionnel')
        else:
            for x in n.enfants:
                parcourir(x)
    parcourir(S.RACINE)
    attendu = {'cnat': 'm²HE·an', 'cnat_30': 'm²HE·an', 'inat': 'm²HE·an', 'snat': 'm²HE·an', 'cnat_moyen': 'm²HE',
               'valeur_habitat': 'm²HE', 'valeur_maturite': 'm²HE', 'i0': 'm²HE·an', 'i1': 'm²HE·an',
               'facteur_climat': 'm²HE par kg CO2 éq.', 'inat_climat': 'm²HE·an', 'inat_bois': 'm²HE·an'}

    def chercher(n):
        if isinstance(n, S.F):
            if n.nom in attendu and n.unite in CATALOGUE and CATALOGUE[n.unite] != CATALOGUE[attendu[n.nom]]:
                err.append(f'RSNat {n.nom} : unité « {n.unite} » ({texte(CATALOGUE[n.unite])}), attendue '
                           f'« {attendu[n.nom]} » ({texte(CATALOGUE[attendu[n.nom]])})')
        else:
            for x in n.enfants:
                chercher(x)
    chercher(S.RACINE)
    return err


def verifier(T) -> list[str]:
    """Contrôle complet : unités des tables, équations des fiches, unités du RSNat. Liste vide si tout est cohérent."""
    return verifier_unites_tables(T) + verifier_equations(T) + verifier_rsnat()
