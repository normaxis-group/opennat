# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module W, première partie : climat horaire conventionnel (fiches A43 à A46).

Années types horaires des fichiers climatiques prospectifs (ADEME, Météo-France, CSTB, DHUP, 2025, Licence
Ouverte 2.0) aux niveaux de réchauffement de la TRACC, corrigées de l'altitude du site ; évapotranspiration de
référence horaire de la FAO-56 ; recalage des pluies sur les normales 1991-2020 ; poids de chaque niveau pour
chaque année civile de la période.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

from . import numerique as nm
from . import unites as U
from .donnees import Parametres, Tables

NIVEAUX = ('2_0', '2_7', '4_0')
ZONES = ('H1a', 'H1b', 'H1c', 'H2a', 'H2b', 'H2c', 'H2d', 'H3')
_FICHIERS: dict[tuple, dict] = {}
_ANNEES: dict[tuple, 'AnneeType'] = {}


@dataclass
class AnneeType:
    """Année type horaire d'une zone, à un niveau, à une altitude (sorties de la fiche A43 et de la fiche A44)."""
    zone: str
    niveau: str
    mois: list[int]
    jour: list[int]
    heure: list[int]
    t: list[float]
    rr_brut: list[float]
    et0: list[float]
    hs: list[float]
    cumul_mois: list[float]          # cumul des pluies brutes de chaque mois de l'année type (fiche A45)


# noms des stations dans les fichiers prospectifs (note technique Météo-France, tableau des stations)
_NOM_STATION = {'H1a': 'TRAPPES', 'H1b': 'NANCY', 'H1c': 'MACON', 'H2a': 'RENNES', 'H2b': 'TOURS', 'H2c': 'AGEN',
                'H2d': 'CARPENTRAS', 'H3': 'MARIGNANE'}


def _fichier(tables: Tables, niveau: str):
    k = (tables.dossier, niveau)
    if k not in _FICHIERS:
        _FICHIERS[k] = tables.annee_type(niveau)
    return _FICHIERS[k]


def saturation(t, P: Parametres):
    """Fiche A44-1 : pression de vapeur saturante, kPa (FAO-56, équation 11)."""
    a, b, c = P.central('fao56', 'saturation_a'), P.central('fao56', 'saturation_b'), P.central('fao56', 'saturation_c')
    return a * math.exp(b * t / (t + c))


def annee_type(P: Parametres, zone: str, niveau: str, altitude: float | None) -> AnneeType:
    """Fiches A43 et A44 : année type horaire corrigée de l'altitude, avec l'ET0 de chaque heure.

    Les constantes des équations (`constantes.csv`) n'ont pas de plage : l'année type ne dépend pas des tirages
    et se calcule une fois par zone, niveau et altitude."""
    k = (P.tables.dossier, zone, niveau, altitude)
    if k in _ANNEES:
        return _ANNEES[k]
    c = lambda p: P.central('fao56', p)                                                    # noqa: E731
    nom = _NOM_STATION[zone]
    alt_st = P.central(zone, 'station_altitude')
    gradient = P.central('iso2533', 'gradient_thermique')
    dz = 0.0 if altitude is None else altitude - alt_st                                     # (A43-1)
    alt = alt_st if altitude is None else altitude
    z_vent = P.central('fichiers_prospectifs', 'hauteur_anemometre')
    t0, expo, kel = c('pression_temperature_reference'), c('pression_exposant'), c('decalage_kelvin')
    sigma, gsc = c('stefan_boltzmann_horaire'), c('constante_solaire_horaire')
    r_min, r_max, h_nuit = c('rapport_rs_rso_min'), c('rapport_rs_rso_max'), c('hauteur_soleil_rapport_nuit')
    mois, jour, heure, t_l, rr, et0_l, hs_l = [], [], [], [], [], [], []
    cumul = [0.0] * U.MOIS_PAR_AN
    rapport = c('rapport_rs_rso_initial')
    for r in _fichier(P.tables, niveau)[nom]:
        m, j = int(r['mois']), int(r['jour'])
        t = float(r['t2m']) - gradient * dz                                                  # (A43-2)
        p = float(r['ps']) * U.KPA_PAR_HPA * ((t0 - gradient * dz) / t0) ** expo             # (A43-3)
        es = saturation(t, P)
        ea = es * float(r['hur']) / U.POURCENT                                                      # (A43-4)
        delta = c('pente_saturation') * es / (t + c('saturation_c')) ** 2                   # (A44-1)
        gamma = c('psychrometrique') * p
        u2 = float(r['ff']) * c('vent_a') / math.log(c('vent_b') * z_vent - c('vent_c'))   # (A44-2)
        rs = max(0.0, float(r['rgh'])) * U.MJ_PAR_WH                                         # (A44-3)
        hs = float(r['hs'])
        jj = sum(U.JOURS_DES_MOIS[:m - 1]) + j
        dr = 1 + c('excentricite') * math.cos(2 * math.pi * jj / U.JOURS_PAR_AN)
        ra = gsc * dr * max(0.0, math.sin(math.radians(hs)))
        rso = (c('rso_a') + c('rso_b') * alt) * ra
        if hs > h_nuit and rso > 0:
            rapport = min(r_max, max(r_min, rs / rso))
        tk = t + kel
        rns = (1 - c('albedo_reference')) * rs                                                # (A44-4)
        rnl = sigma * tk ** 4 * (c('rnl_a') - c('rnl_b') * math.sqrt(ea)) * (c('rnl_c') * rapport - c('rnl_d'))
        rn = rns - rnl                                                                       # (A44-5)
        g = (c('flux_sol_jour') if hs > 0 else c('flux_sol_nuit')) * rn
        et0 = (c('coefficient_rayonnement') * delta * (rn - g) + gamma * c('cn_horaire') / tk * u2 *
               max(0.0, es - ea)) / (delta + gamma * (1 + c('cd_horaire') * u2))           # (A44-6)
        brut = max(0.0, float(r['rr']))
        cumul[m - 1] += brut
        mois.append(m), jour.append(j), heure.append(int(r['heure_utc'])), t_l.append(t)
        rr.append(brut), et0_l.append(max(0.0, et0)), hs_l.append(hs)
    a = AnneeType(zone, niveau, mois, jour, heure, t_l, rr, et0_l, hs_l, cumul)
    _ANNEES[k] = a
    return a


def recalage(P: Parametres, an: AnneeType):
    """Fiche A45 : rapport de recalage de chaque mois (liste de 12 nombres ou tableaux)."""
    return [nm.si(an.cumul_mois[m - 1] > 0, P(an.zone, f'pluie_normale_m{m:02d}') / max(an.cumul_mois[m - 1], 1e-300),
                  0.0) for m in range(1, U.MOIS_PAR_AN + 1)]


def niveau_annee(P: Parametres, annee: int):
    """Fiche A46-1 : réchauffement de l'année civile selon les jalons de la TRACC."""
    j = [(P('tracc', f'jalon_{i}_annee'), P('tracc', f'jalon_{i}_rechauffement')) for i in (1, 2, 3)]
    if annee <= j[0][0]:
        return j[0][1]
    for (a0, n0), (a1, n1) in zip(j, j[1:]):
        if annee <= a1:
            return n0 + (n1 - n0) * (annee - a0) / (a1 - a0)
    return j[-1][1]


def poids(P: Parametres, annee: int) -> dict:
    """Fiche A46-2 : poids des trois années types pour une année civile."""
    dt = niveau_annee(P, annee)
    n2, n27, n4 = (P('tracc', f'jalon_{i}_rechauffement') for i in (1, 2, 3))
    if dt <= n27:
        w = (dt - n2) / (n27 - n2)
        return {'2_0': 1 - w, '2_7': w, '4_0': 0.0}
    w = (dt - n27) / (n4 - n27)
    return {'2_0': 0.0, '2_7': 1 - w, '4_0': w}


def par_annee(P: Parametres, valeurs: dict, annees: list[int]) -> list:
    """Fiche A46-3 : grandeur de chaque année de la période, à partir de ses valeurs par niveau."""
    return [sum(w * valeurs[n] for n, w in poids(P, a).items()) for a in annees]
