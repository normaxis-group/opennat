# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Étape E1 (contexte, fiche A02) et étape E5 (conformité et attestations, fiche A40)."""
from __future__ import annotations

from . import numerique as nm
from . import unites as U
from .donnees import Parametres


def contexte(P: Parametres, entree: dict, emprise: float) -> dict:
    """Fiche A02 : multiplicateur de délai, part d'emprise, seuils applicables."""
    ctx = entree['contexte']
    sp = entree['parcelle']['surface']
    k_delai = P(f'zone_{ctx["zone_biogeographique"]}', 'multiplicateur_delai') * ctx.get('k_delai_etude', 1.0)  # (A02-2)
    e = emprise / sp                                                                       # (A02-3)
    er = round(e, 2)
    typo = ctx['typologie']
    if typo == 'logement':                                                                 # (A02-4)
        c1, c3 = P.central('emprise', 'classe_1_max'), P.central('emprise', 'classe_3_min')
        cle = 'logement_emprise_37' if er <= c1 else 'logement_emprise_38_49' if er < c3 else 'logement_emprise_50'
    elif typo == 'tertiaire':
        cle = 'tertiaire'
    else:
        cle = None
    bmin = P(cle, 'bnat_min') if cle else None
    if ctx.get('cbs_plu') is not None:                                                    # (A02-5)
        bmin = nm.maxi(bmin, U.POINTS_PAR_UNITE * ctx['cbs_plu']) if bmin is not None else U.POINTS_PAR_UNITE * ctx['cbs_plu']
    ptmin = P('*', 'pleine_terre_min')
    if ctx.get('pleine_terre_plu') is not None:                                           # (A02-6)
        ptmin = nm.maxi(ptmin, ctx['pleine_terre_plu'])
    return dict(k_delai=k_delai, part_emprise=e, classe_seuil=cle, bnat_min=bmin, pleine_terre_min=ptmin)


def conformite(P: Parametres, ind: dict, bn: dict, pt: float, i0, ctx_res: dict, ctx: dict) -> dict:
    """Fiche A40."""
    bmin = ctx_res['bnat_min']
    conf_b = None if bmin is None else bn['bnat'] >= bmin                                  # (A40-1)
    conf_pt = pt >= ctx_res['pleine_terre_min']                                           # (A40-2)
    conf_plu = None
    if ctx.get('cbs_plu') is not None or ctx.get('pleine_terre_plu') is not None:          # (A40-3)
        conf_plu = nm.et(ctx.get('cbs_plu') is None or bn['bnat'] >= U.POINTS_PAR_UNITE * ctx['cbs_plu'],
                         ctx.get('pleine_terre_plu') is None or pt >= ctx['pleine_terre_plu'])
    cnat = ind['cnat']
    s2, s1 = P('niveau_2', 'cnat_max_relatif'), P('niveau_1', 'cnat_max_relatif')
    gain2 = nm.si(i0 > 0, cnat <= s2 * i0, cnat < 0)                                      # (A40-4)
    niveau = nm.si(gain2, 2, nm.si(cnat <= s1 * i0, 1, 0))
    permis = all(x is not False for x in (conf_b, conf_pt, conf_plu))                      # (A40-5)
    return dict(bnat_conforme=conf_b, pleine_terre_conforme=conf_pt, plu_conforme=conf_plu, niveau_cnat=niveau,
                attestation_permis_conforme=permis)
