# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module E : eau et valeur à maturité (fiches A23 à A25)."""
from __future__ import annotations

from . import numerique as nm
from .donnees import Parametres


def k_eau(P: Parametres, u: dict):
    """Fiche A23-1 [E1]."""
    if u['position'] == 'eau' and u.get('alimentation') == 'artificielle':
        return P('alimentation_artificielle', 'facteur_eau')
    return 1.0


def infiltration(ouvrages: list[dict], a_imp: float, toitures: float) -> dict:
    """Fiche A24 : surface infiltrée en surface et part des surfaces imperméables gérées à ciel ouvert."""
    a_inf = sum(o['surface_drainee'] for o in ouvrages if o.get('infiltration_surface'))  # (A24-1)
    denom = a_imp + toitures
    return dict(a_inf=a_inf, p_inf=a_inf / denom if denom else None)                     # (A24-2)


def valeur_maturite(P: Parametres, u: dict):
    """Fiche A25-2 [H5] : V = min(V_max x A ; V^H x k_C x k_N x k_E)."""
    return nm.mini(P('*', 'plafond_valeur_unitaire') * u['surface'], u['VH'] * u['kC'] * u['kN'] * u['kE'])
