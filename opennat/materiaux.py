# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module G : biodiversité grise (fiches A32 à A36)."""
from __future__ import annotations

from . import unites as U
from .donnees import Parametres

PHASES = ('A1-A3', 'A4-A5', 'B', 'C', 'D')
PERSISTANCE = {'A1-A3': 'phase_A1_A5', 'A4-A5': 'phase_A1_A5', 'B': 'phase_B', 'C': 'phase_C', 'D': 'phase_D'}
REGIMES = {'plantation': 'foret_plantation', 'coupe_rase': 'foret_coupe_rase', 'coupe_selective': 'foret_selective',
           'faible_impact': 'foret_impact_reduit'}
POLLUTION = ('106', '107', '108', '109', '116')


def lecture_acv(batiments: list[dict]) -> dict:
    """Fiche A32 : émissions et pollution par phase, par m² de S_ref de l'opération."""
    sref = sum(b.get('sref', 0.0) for b in batiments)
    ges = {p: 0.0 for p in PHASES}
    pol = {i: {p: 0.0 for p in PHASES} for i in POLLUTION}
    if sref:
        for b in batiments:
            for p, v in b.get('ges', {}).items():
                ges[p] += v * b['sref'] / sref                                                 # (A32-1)
            for i, par_phase in b.get('pollution', {}).items():
                for p, v in par_phase.items():
                    pol[str(i)][p] += v * b['sref'] / sref                                     # (A32-2)
    return dict(sref=sref, ges=ges, pollution=pol)


def climat(P: Parametres, sref: float, ges: dict) -> dict:
    """Fiche A33 [G2] : Inat_clim = CF x S_ref x somme des GES_p x a_p."""
    cf = P('climat', 'facteur_caracterisation')
    par_phase = {p: cf * sref * g * P(PERSISTANCE[p], 'annees_persistance') for p, g in ges.items() if g}
    return dict(CF=cf, par_phase=par_phase, inat_clim=sum(par_phase.values()))


def bois(P: Parametres, lots: list[dict], journal: list) -> dict:
    """Fiche A34 [G4]."""
    occ = U.M2_PAR_HA / P('foret', 'production_biologique') * P('foret', 'rapport_bois_rond_produit')   # (A34-1)
    total = 0.0
    for lot in lots:
        reg = lot.get('regime', 'coupe_rase')
        if reg != 'coupe_rase' and not lot.get('justification'):
            journal.append(f'bois de régime « {reg} » sans pièce justificative : compté en coupe rase (C-G5)')
            reg = 'coupe_rase'                                                                  # (A34-2)
        total = total + lot['volume'] * (1 + lot.get('remplacements', 0)) * occ * (1 - P(REGIMES[reg], 'msa_usage'))
    return dict(occupation=occ, inat_bois=total)


def carrieres(P: Parametres, granulats: dict | None) -> float:
    """Fiche A35-1 [G5]."""
    if not granulats:
        return 0.0
    return granulats['masse'] * (1 + granulats.get('remplacements', 0)) * P('carriere', 'occupation_par_tonne') * \
        (1 - P('carriere', 'msa_usage'))


def pollution(sref: float, pol: dict) -> dict:
    """Fiche A36-1 : indicateurs de pollution, phases A à C."""
    return {i: sref * sum(v for p, v in par_phase.items() if p != 'D') for i, par_phase in pol.items()}


def module_g(P: Parametres, batiments: list[dict], materiaux: dict, journal: list) -> dict:
    acv = lecture_acv(batiments)
    cl = climat(P, acv['sref'], acv['ges'])
    bo = bois(P, materiaux.get('bois', []), journal)
    ca = carrieres(P, materiaux.get('granulats'))
    return dict(sref=acv['sref'], ges=acv['ges'], CF=cl['CF'], inat_clim_phase=cl['par_phase'],
                inat_clim=cl['inat_clim'], occupation_bois=bo['occupation'], inat_bois=bo['inat_bois'],
                inat_carr=ca, inat_sols=bo['inat_bois'] + ca,                                    # (A35-2) [G6]
                inat=cl['inat_clim'] + bo['inat_bois'] + ca,                                     # [G1]
                pollution=pollution(acv['sref'], acv['pollution']))
