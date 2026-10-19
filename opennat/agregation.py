# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Étape E3 : agrégation des indicateurs (fiche A37) et Bnat (fiche A38)."""
from __future__ import annotations

from . import unites as U
from .donnees import Parametres


def integration(initial: list[dict], projet: list[dict], n: int, n30: int) -> dict:
    """Fiche A31 : valeurs intégrées, trajectoires du site, dette de maturité."""
    ref = [sum(u['V'] * u['kW'][t] for u in initial) for t in range(n)]                     # (A31-3) [T7]
    site = [sum(u['traj'][t] for u in projet) for t in range(n)]                            # (A31-2)
    dm = sum(u['D'] * u['V'] - x for u in projet if u.get('statut', 'creee') in ('creee', 'amelioree')
             for x in u['traj_base'])                                                        # (A31-5) [T8]
    return dict(v0=sum(u['V'] for u in initial), ref=ref, site=site, i0=sum(ref), i1=sum(site),
                i0_30=sum(ref[:n30]), i1_30=sum(site[:n30]), dm=dm)


def indicateurs(it: dict, faune, inat, sp: float, sref: float, n: int) -> dict:
    """Fiche A37."""
    cnat = it['i0'] - it['i1'] + faune                                                      # (A37-1) [A1]
    return dict(cnat=cnat, cnat_moyen=cnat / n,                                             # (A37-2)
                cnat_relatif=cnat / it['i0'] if _positif(it['i0']) else None,               # (A37-3)
                cnat_30=it['i0_30'] - it['i1_30'] + faune,                                   # (A37-4)
                inat=inat, snat=-(cnat + inat),                                              # (A37-6) [A2]
                cnat_par_m2_parcelle=cnat / sp, inat_par_m2_sref=inat / sref if sref else None)


def _positif(x) -> bool:
    try:
        return bool(x > 0) if not hasattr(x, 'shape') else bool((x > 0).all())
    except TypeError:
        return False


def bnat(P: Parametres, projet: list[dict], a_inf: float, sp: float) -> dict:
    """Fiche A38 [A3] : Bnat = 100 x (somme des A x c hors arbres + c(S13) x A_inf) / S_p."""
    num = sum(u['surface'] * u['c'] for u in projet if u['c'] is not None) + P('S13', 'coefficient_sol') * a_inf
    b = U.POINTS_PAR_UNITE * num / sp
    return dict(bnat=b, numerateur=num, cbs=b / U.POINTS_PAR_UNITE)
