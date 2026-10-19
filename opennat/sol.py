# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module S : sol (fiches A06 à A08)."""
from __future__ import annotations

from .donnees import Parametres

AU_SOL = ('sol_pleine_terre', 'sol_sur_dalle', 'eau', 'lineaire')        # fiche A03-1


def nature(P: Parametres, u: dict) -> str | None:
    """Fiche A06-1 : nature de surface S01 à S12 ; None pour un arbre, qui surplombe une autre unité."""
    h, p = u['code'], u['position']
    if h in ('VB.1', 'VB.2'):
        return 'S01'
    if h in ('VB.3', 'VB.10', 'VB.25', 'H5.6'):
        return 'S02'
    if h == 'VB.4':
        return 'S03'
    if h in ('VB.21', 'VB.24'):
        return 'S12'
    if p == 'eau':
        return 'S11'
    if h == 'VB.15':
        return 'S09'
    if h == 'VB.16':
        return 'S10'
    if p in ('sol_sur_dalle', 'hors_sol_toiture'):
        e = u.get('epaisseur') or 0
        if e < P.central('substrat', 'epaisseur_s05'):
            return 'S04'
        if e <= P.central('substrat', 'epaisseur_s06'):
            return 'S05'
        return 'S06' if e < P.central('substrat', 'epaisseur_s07') else 'S07'
    if p == 'arbre':
        return None
    return 'S08'


def coefficient(P: Parametres, n: str | None):
    """Fiche A06-2 [S1]."""
    return None if n is None else P(n, 'coefficient_sol')


def facteur_support(u: dict, c):
    """Fiche A07-1 [S2] : f_sol = c sur dalle, 1 sinon."""
    return c if u['position'] == 'sol_sur_dalle' else 1.0


def indicateurs(initial: list[dict], projet: list[dict], sp: float) -> dict:
    """Fiche A08 : pleine terre et imperméabilisation."""
    pt = sum(u['surface'] for u in projet if u['nature'] == 'S08') / sp                   # (A08-1) [S3]
    pt0 = sum(u['surface'] for u in initial if u['nature'] == 'S08') / sp
    a0 = sum(u['surface'] for u in initial if u['nature'] == 'S01')                       # (A08-2)
    a1 = sum(u['surface'] for u in projet if u['nature'] == 'S01')
    return dict(pleine_terre=pt, pleine_terre_initiale=pt0, impermeable_initial=a0, impermeable_projet=a1,
                impermeabilisation_nette=a1 - a0)                                        # (A08-3) [S4]
