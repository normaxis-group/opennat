# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Climat horaire conventionnel de la méthode OpenNAT (fiches A43 à A46).

Lit les années types horaires des fichiers climatiques prospectifs ADEME, Météo-France, CSTB et DHUP (juin 2025,
Licence Ouverte 2.0) aux trois niveaux de la trajectoire de réchauffement de référence (TRACC) : France +2 °C,
+2,7 °C et +4 °C. Les fichiers météorologiques de la RE2020 ne sont pas utilisés : leur licence les réserve au
calcul réglementaire RE2020.

Calcule l'évapotranspiration de référence horaire par l'équation 53 de la FAO-56 (Allen et al., 1998).
"""
import csv
import gzip
import math
import os
from functools import lru_cache

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEAUX = ('2_0', '2_7', '4_0')
RECHAUFFEMENT = {'2_0': 2.0, '2_7': 2.7, '4_0': 4.0}

# Stations de référence des zones climatiques (note technique Météo-France, tableau 1) : nom, latitude,
# longitude, altitude en m
STATIONS = {
    'H1a': ('TRAPPES', 48.7743, 2.0098, 167), 'H1b': ('NANCY', 48.6878, 6.2215, 212),
    'H1c': ('MACON', 46.2945, 4.7943, 219), 'H2a': ('RENNES', 48.0688, -1.7640, 36),
    'H2b': ('TOURS', 47.4445, 0.7273, 108), 'H2c': ('AGEN', 44.1721, 0.5946, 58),
    'H2d': ('CARPENTRAS', 44.0836, 5.2160, 98), 'H3': ('MARIGNANE', 43.4376, 5.2160, 9),
}
SIGMA_H = 4.903e-9 / 24          # constante de Stefan-Boltzmann, MJ K-4 m-2 h-1 (FAO-56, équation 39)
ALBEDO = 0.23                    # gazon de référence (FAO-56, équation 38)
GSC = 0.0820 * 60                # constante solaire, MJ m-2 h-1 (FAO-56, équation 28)
GRADIENT = 0.0065                # gradient thermique de l'atmosphère type, K/m (ISO 2533)


def _lire(niveau):
    chemin = os.path.join(RACINE, 'donnees', 'climat', f'tracc_{niveau}.csv.gz')
    par_station = {}
    with gzip.open(chemin, 'rt', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter=';'):
            par_station.setdefault(r['station'], []).append(r)
    return par_station


@lru_cache(maxsize=None)
def _fichier(niveau):
    return _lire(niveau)


def saturation(t):
    """Pression de vapeur saturante en kPa (FAO-56, équation 11)."""
    return 0.6108 * math.exp(17.27 * t / (t + 237.3))


@lru_cache(maxsize=None)
def _normales():
    with open(os.path.join(RACINE, 'donnees', 'climat.csv'), encoding='utf-8') as f:
        return {(r['cle'], r['parametre']): float(r['valeur']) for r in csv.DictReader(f, delimiter=';')}


def _jour_julien(mois, jour):
    return sum((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[:mois - 1]) + jour


@lru_cache(maxsize=None)
def annee(zone, niveau, altitude=None):
    """Année type horaire d'une zone climatique à un niveau de réchauffement, corrigée de l'altitude du site
    (fiches A43 à A45). Renvoie une liste de 8 760 dictionnaires : mois, jour, heure UTC, t (°C), rr (mm),
    et0 (mm), hs (hauteur du soleil à la station, degrés)."""
    nom, _, _, alt_st = STATIONS[zone]
    dz = 0.0 if altitude is None else altitude - alt_st
    lignes = _fichier(niveau)[nom]
    # fiche A45 : pluies horaires recalées mois par mois sur la normale 1991-2020 de la station (C-W3)
    cumul = {}
    for r in lignes:
        cumul[int(r['mois'])] = cumul.get(int(r['mois']), 0.0) + max(0.0, float(r['rr']))
    nm = _normales()
    recal = {m: (nm[(zone, f'pluie_normale_m{m:02d}')] / c if c > 0 else 0.0) for m, c in cumul.items()}
    res = []
    rapport = 0.7                                          # Rs/Rso de nuit : dernière valeur de jour (FAO-56)
    for r in lignes:
        mois, jour = int(r['mois']), int(r['jour'])
        t = float(r['t2m']) - GRADIENT * dz
        hur = float(r['hur'])
        # pression : valeur du fichier en hPa ramenée à l'altitude du site (FAO-56, forme de l'équation 7)
        p = float(r['ps']) / 10 * ((293 - GRADIENT * dz) / 293) ** 5.26
        es = saturation(t)
        ea = es * hur / 100                                # équation 54
        delta = 4098 * es / (t + 237.3) ** 2               # équation 13
        gamma = 0.665e-3 * p                               # équation 8
        u2 = float(r['ff']) * 4.87 / math.log(67.8 * 10 - 5.42)   # équation 47
        rs = max(0.0, float(r['rgh'])) * 0.0036            # W/m² -> MJ/m²/h
        hs = float(r['hs'])
        dr = 1 + 0.033 * math.cos(2 * math.pi * _jour_julien(mois, jour) / 365)   # équation 23
        ra = GSC * dr * max(0.0, math.sin(math.radians(hs)))                      # équation 28, hauteur du fichier
        rso = (0.75 + 2e-5 * ((altitude if altitude is not None else alt_st))) * ra   # équation 37
        if hs > 10 and rso > 0:
            rapport = min(1.0, max(0.3, rs / rso))
        tk = t + 273.16
        rns = (1 - ALBEDO) * rs                            # équation 38
        rnl = SIGMA_H * tk ** 4 * (0.34 - 0.14 * math.sqrt(ea)) * (1.35 * rapport - 0.35)   # équation 39
        rn = rns - rnl                                     # équation 40
        g = 0.1 * rn if hs > 0 else 0.5 * rn               # équations 45 et 46
        et0 = (0.408 * delta * (rn - g) + gamma * 37 / tk * u2 * max(0.0, es - ea)) / (
            delta + gamma * (1 + 0.34 * u2))               # équation 53
        res.append(dict(mois=mois, jour=jour, heure=int(r['heure_utc']), t=t,
                        rr=max(0.0, float(r['rr'])) * recal[mois], et0=max(0.0, et0), hs=hs))
    return res


def niveau_annee(an):
    """Niveau de réchauffement de la TRACC pour une année civile (fiche A46) : +2 °C en 2030, +2,7 °C en 2050,
    +4 °C en 2100 (arrêté du 23 janvier 2026), interpolation linéaire entre ces jalons, +2 °C avant 2030."""
    jalons = ((2030, 2.0), (2050, 2.7), (2100, 4.0))
    if an <= 2030:
        return 2.0
    for (a0, n0), (a1, n1) in zip(jalons, jalons[1:]):
        if an <= a1:
            return n0 + (n1 - n0) * (an - a0) / (a1 - a0)
    return 4.0


def ponderation(an):
    """Poids des trois années types pour une année civile : interpolation linéaire en niveau de réchauffement."""
    n = niveau_annee(an)
    if n <= 2.7:
        w = (n - 2.0) / 0.7
        return {'2_0': 1 - w, '2_7': w, '4_0': 0.0}
    w = (n - 2.7) / 1.3
    return {'2_0': 0.0, '2_7': 1 - w, '4_0': w}


if __name__ == '__main__':
    for z in STATIONS:
        ligne = [z, STATIONS[z][0]]
        for n in NIVEAUX:
            a = annee(z, n)
            ligne += [round(sum(h['et0'] for h in a)), round(sum(h['rr'] for h in a))]
        ligne.append(round(_normales()[(z, 'etp_penman_normale')]))
        print(*ligne)
