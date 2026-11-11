# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module W, seconde partie : bilan hydrique horaire (fiches A47 à A50).

Le bilan suit, heure par heure, l'eau du réservoir de chaque unité végétalisée sur les trois années types ; il en
tire l'indice de stress de Granier, l'arrosage, la tenue en eau des mares et le facteur hydrique k_W.
"""
from __future__ import annotations

from . import climat
from . import numerique as nm
from . import unites as U
from .donnees import Parametres

# Fiche A47-1 : types sans bilan hydrique
SANS_BILAN = {'VB.1', 'VB.2', 'VB.3', 'VB.4', 'VB.10', 'VB.25', 'H5.6', 'VB.21', 'VB.24', 'VB.15', 'VB.16'}
_SAISONS: dict[tuple, list[bool]] = {}


def groupe(u: dict) -> str | None:
    """Fiche A47 : groupe hydrique d'une unité."""
    c, p = u['code'], u['position']
    if c in SANS_BILAN or c.startswith(('J', 'I2')):
        return None
    if c == 'VB.20' or c.startswith('C1'):
        return 'mare'
    if c == 'VB.19':
        return 'humide_pluie'
    if c.startswith(('C2', 'C3', 'D', 'E3')):
        return None if u.get('alimentation_humide', 'nappe') == 'nappe' else 'humide_pluie'
    if c == 'VB.11':
        return 'toiture_extensive'
    if c in ('VB.5', 'VB.22'):
        return 'gazon'
    if c.startswith(('E1', 'F5', 'F6', 'H')):
        return 'xerophile'
    if c.startswith('G3'):
        return 'conifere'
    if c.startswith(('G', 'VB.18')):
        return 'arbore'
    if c.startswith(('F', 'FA', 'FB')) or c in ('VB.6', 'VB.9'):
        return 'arbustif'
    return 'prairie'


def reserve_utile(P: Parametres, u: dict, sol: dict, g: str):
    """Fiche A48 : réserve utile en mm."""
    if u['position'] in ('hors_sol_toiture', 'sol_sur_dalle'):
        return U.MM_PAR_CM * u['epaisseur'] * P('substrat', 'reserve_volumique')                # (A48-1)
    tex = u.get('texture') or sol['texture']
    prof = u.get('profondeur_sol') or sol['profondeur']
    return U.MM_PAR_M * (P(tex, 'theta_capacite_champ') - P(tex, 'theta_point_fletrissement')) * \
        nm.mini(P(g, 'profondeur_racinaire'), prof)                                              # (A48-2)


def apport(P: Parametres, u: dict):
    """Fiche A49-2 : apport de ruissellement par mm de pluie tombée sur l'unité."""
    if not u['surface']:
        return 0.0
    return (u.get('bassin_versant', 0.0) * P('*', 'coefficient_ruissellement') +
            u.get('bassin_versant_permeable', 0.0) * P('*', 'coefficient_ruissellement_permeable')) / u['surface']


def saison(P: Parametres, an: climat.AnneeType) -> list[bool]:
    """Fiche A49-1 : heures de la saison de végétation (moyenne glissante des températures, convention C-W7)."""
    k = (id(an),)
    if k not in _SAISONS:
        seuil = P.central('*', 'seuil_saison_temperature')
        n = int(P.central('*', 'seuil_saison_jours')) * U.HEURES_PAR_JOUR
        res, fen, somme = [], [], 0.0
        for t in an.t:
            fen.append(t)
            somme += t
            if len(fen) > n:
                somme -= fen.pop(0)
            res.append(somme / len(fen) > seuil)
        _SAISONS[k] = res
    return _SAISONS[k]


def bilan_sol(P: Parametres, an: climat.AnneeType, g: str, ru, arrose: bool, app):
    """Fiche A49-3 à A49-7 : bilan horaire d'une unité au sol ou sur substrat, sur une année type jouée deux fois."""
    rho = climat.recalage(P, an)
    kc_s, kc_h, p = P(g, 'kc_saison'), P(g, 'kc_hors_saison'), P(g, 'fraction_p')
    rew_s, rew_a = P('*', 'seuil_rew_stress'), P('*', 'seuil_rew_arrosage')
    h_arr = P.central('arrosage', 'heure_utc')
    sais = saison(P, an)
    d = 0.0 * ru
    for _ in (0, 1):
        is_h, etc_tot, eta_tot, arros = 0.0, 0.0, 0.0, 0.0
        for i in range(len(an.t)):
            s = sais[i]
            etc = (kc_s if s else kc_h) * an.et0[i]
            rew = 1 - d / ru                                                                     # (A49-3)
            ks = nm.si(rew >= 1 - p, 1.0, nm.maxi(0.0, rew / (1 - p)))
            eta = ks * etc                                                                       # (A49-4)
            d = nm.borne(d - an.rr_brut[i] * rho[an.mois[i] - 1] * (1 + app) + eta, 0.0, ru)    # (A49-5)
            if arrose and s and an.heure[i] == h_arr:                                            # (A49-6)
                besoin = (1 - d / ru) < rew_a
                arros = arros + nm.si(besoin, d, 0.0)
                d = nm.si(besoin, 0.0, d)
            if s:
                etc_tot = etc_tot + etc
                eta_tot = eta_tot + eta
                is_h = is_h + nm.maxi(0.0, (rew_s - (1 - d / ru)) / rew_s) / U.HEURES_PAR_JOUR      # (A49-7)
    return dict(IS=is_h, deficit=1 - eta_tot / etc_tot, arrosage_mm=arros)


def bilan_mare(P: Parametres, an: climat.AnneeType, prof, infil, app):
    """Fiche A49-8 : hauteur d'eau horaire d'une mare ; assec de printemps et jours en eau."""
    rho = climat.recalage(P, an)
    kc = P('mare', 'kc_saison')
    m0, m1 = P.central('mare', 'premier_mois_assec'), P.central('mare', 'dernier_mois_assec')
    h = U.MM_PAR_M * prof
    hmax = h
    for _ in (0, 1):
        assec, jours = False, 0.0
        for i in range(len(an.t)):
            h = nm.mini(h + an.rr_brut[i] * rho[an.mois[i] - 1] * (1 + app) - kc * an.et0[i] -
                        infil / U.HEURES_PAR_JOUR, hmax)
            h = nm.maxi(h, 0.0)
            if m0 <= an.mois[i] <= m1:
                assec = assec | (h <= 0) if nm.tableau(h) else (assec or h <= 0)
            if an.heure[i] == U.MIDI_UTC:
                jours = jours + nm.si(h > 0, 1.0, 0.0)
    return dict(assec_precoce=assec, jours_en_eau=jours)


def _cle(u, sol, g, niveau):
    return (g, niveau, u['position'], u.get('epaisseur'), u.get('texture') or sol['texture'],
            u.get('profondeur_sol') or sol['profondeur'], bool(u.get('arrose')), u.get('bassin_versant', 0.0),
            u.get('bassin_versant_permeable', 0.0), u['surface'], u.get('profondeur'), u.get('fond'))


def facteurs(P: Parametres, u: dict, sol: dict, ctx: dict, cache: dict) -> dict:
    """Fiche A50 : facteur hydrique de l'unité pour chaque niveau, avec le détail du bilan."""
    g = groupe(u)
    if g is None:
        return dict(groupe=None, kW={n: 1.0 for n in climat.NIVEAUX}, bilan={n: None for n in climat.NIVEAUX},
                    RU=None, arrosage_m3={n: 0.0 for n in climat.NIVEAUX})
    zone, alt = ctx['zone_climatique'], ctx.get('altitude')
    res = dict(groupe=g, kW={}, bilan={}, RU=None, arrosage_m3={})
    if g == 'mare':
        prof = u.get('profondeur') or P('*', 'profondeur_mare_defaut')
        infil = P(f'fond_{u.get("fond") or "argile"}', 'infiltration')
        for n in climat.NIVEAUX:
            k = _cle(u, sol, g, n)
            if k not in cache:
                cache[k] = bilan_mare(P, climat.annee_type(P, zone, n, alt), prof, infil, apport(P, u))
            r = cache[k]
            res['bilan'][n] = r
            res['kW'][n] = nm.si(r['assec_precoce'], P('*', 'facteur_assec_precoce'), 1.0)         # (A50-3)
            res['arrosage_m3'][n] = 0.0
        return res
    ru = reserve_utile(P, u, sol, g)
    res['RU'] = ru
    if g == 'toiture_extensive':                                                                 # (A50-1)
        ru_ref = U.MM_PAR_CM * P.central('reference_hydrique', 'epaisseur_toiture') * P('substrat', 'reserve_volumique')
    else:
        ru_ref = U.MM_PAR_M * (P('limon', 'theta_capacite_champ') - P('limon', 'theta_point_fletrissement')) * \
            nm.mini(P(g, 'profondeur_racinaire'), P('*', 'profondeur_sol_defaut'))
    k_ref = ('reference', g, zone, alt)
    if k_ref not in cache:
        cache[k_ref] = bilan_sol(P, climat.annee_type(P, zone, '2_0', alt), g, ru_ref, False, 0.0)
    is_ref = cache[k_ref]['IS']
    for n in climat.NIVEAUX:
        k = _cle(u, sol, g, n)
        if k not in cache:
            cache[k] = bilan_sol(P, climat.annee_type(P, zone, n, alt), g, ru, bool(u.get('arrose')), apport(P, u))
        r = dict(cache[k], IS_ref=is_ref)
        res['bilan'][n] = r
        exces = r['IS'] - is_ref - P('*', 'tolerance_stress')
        res['kW'][n] = nm.maxi(P('*', 'facteur_hydrique_minimum'),
                               1 - P(g, 'sensibilite_stress') * nm.maxi(0.0, exces) / U.JOURS_PAR_SENSIBILITE)  # (A50-2)
        res['arrosage_m3'][n] = r['arrosage_mm'] * u['surface'] / U.MM_PAR_M
    return res
