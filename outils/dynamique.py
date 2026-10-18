# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Modules dynamiques de la méthode OpenNAT (partie 3, fiches A43 à A58).

- module W, bilan hydrique horaire (A43 à A50) : réservoir en eau du sol ou du substrat de chaque unité, pas
  horaire, sur les années types des trois niveaux de réchauffement ; indice de stress hydrique, arrosage,
  tenue en eau des mares ; facteur hydrique k_W de chaque année de la période ;
- module L, éclairage horaire (A51 à A53) : heures éclairées de nuit pendant la saison d'activité des
  chiroptères, température de couleur, distance ; facteur d'éclairage k_L ;
- module M, maturation et succession (A54 à A56) : courbe de maturation non linéaire, gestion et succession ;
- module K, chantier au pas mensuel (A57 et A58) : calendrier écologique des travaux et saison de plantation.

Tous les coefficients sont lus dans donnees/ (hydrique.csv, eclairage.csv, succession.csv, chantier.csv).
"""
import csv
import math
import os
from functools import lru_cache

import climat

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _table(nom):
    with open(os.path.join(RACINE, 'donnees', nom), encoding='utf-8') as f:
        return {(r['cle'], r['parametre']): float(r['valeur']) for r in csv.DictReader(f, delimiter=';')}


HYD, ECL, SUC, CHA = (_table(n) for n in ('hydrique.csv', 'eclairage.csv', 'succession.csv', 'chantier.csv'))
MINERAUX = {'VB.1', 'VB.2', 'VB.3', 'VB.4', 'VB.10', 'VB.25', 'H5.6', 'VB.21', 'VB.24', 'VB.15', 'VB.16'}


# ---------------------------------------------------------------- module W : bilan hydrique horaire

def groupe_hydrique(u):
    """Fiche A47 : groupe hydrique d'une unité, d'après son code et sa position."""
    c, p = u['code'], u['position']
    if c in MINERAUX or c.startswith(('J', 'I2')):
        return None
    if c == 'VB.20' or c.startswith('C1'):
        return 'mare'
    if c == 'VB.19':
        return 'humide_pluie'
    if c.startswith(('C2', 'C3', 'D', 'E3')):
        return None if u.get('alimentation', 'nappe') == 'nappe' else 'humide_pluie'
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


def reserve_utile(u, sol):
    """Fiche A48 : réserve utile en mm. Substrat hors sol ou sur dalle : épaisseur x réserve volumique du
    substrat ; pleine terre : (theta_cc - theta_pf) x profondeur d'enracinement, bornée par la profondeur de sol."""
    g = groupe_hydrique(u)
    if u['position'] in ('hors_sol_toiture', 'sol_sur_dalle'):
        return 10 * u.get('epaisseur', 10) * HYD[('substrat', 'reserve_volumique')], g
    tex = u.get('texture', sol.get('texture', 'limon'))
    ru_vol = HYD[(tex, 'theta_capacite_champ')] - HYD[(tex, 'theta_point_fletrissement')]
    prof = min(HYD[(g, 'profondeur_racinaire')], u.get('profondeur_sol', sol.get('profondeur', HYD[('*', 'profondeur_sol_defaut')])))
    return 1000 * ru_vol * prof, g


def _en_saison(temperatures, seuil, jours):
    """Saison de végétation (C-W7) : moyenne des températures horaires des `jours` derniers jours au-dessus du
    seuil. Renvoie une liste de booléens horaires."""
    res, fen, somme = [], [], 0.0
    n = 24 * jours
    for t in temperatures:
        fen.append(t)
        somme += t
        if len(fen) > n:
            somme -= fen.pop(0)
        res.append(somme / len(fen) > seuil)
    return res


@lru_cache(maxsize=None)
def bilan_annee(zone, niveau, altitude, groupe, ru, arrose, apport, mare_param):
    """Fiche A49 : bilan hydrique horaire d'une unité sur une année type. Renvoie l'indice de stress de Granier
    (jours-équivalents), le déficit relatif de transpiration, le volume d'arrosage en mm et, pour une mare,
    l'assec précoce (booléen) et le nombre de jours en eau. L'année est jouée deux fois pour que l'état du
    réservoir au 1er janvier soit celui de fin d'année (régime établi)."""
    an = climat.annee(zone, niveau, altitude)
    if groupe == 'mare':
        prof, infil, bv = mare_param
        kc = HYD[('mare', 'kc_saison')]
        h = prof * 1000
        res = None
        for passe in (0, 1):
            assec, jours_eau, hmin = False, 0, h
            for i, x in enumerate(an):
                h += x['rr'] * (1 + bv) - kc * x['et0'] - infil / 24          # bv : apport par mm de pluie (A49-2)
                h = min(h, prof * 1000)
                if h <= 0:
                    h = 0.0
                    if 3 <= x['mois'] <= 6:
                        assec = True
                if h > 0 and x['heure'] == 12:
                    jours_eau += 1
            res = dict(assec_precoce=assec, jours_en_eau=jours_eau)
        return res
    kc_s, kc_h, p = HYD[(groupe, 'kc_saison')], HYD[(groupe, 'kc_hors_saison')], HYD[(groupe, 'fraction_p')]
    saison = _en_saison([x['t'] for x in an], HYD[('*', 'seuil_saison_temperature')],
                        int(HYD[('*', 'seuil_saison_jours')]))
    rew_s = HYD[('*', 'seuil_rew_stress')]
    rew_a = HYD[('*', 'seuil_rew_arrosage')]
    dr = 0.0                                                   # déplétion de la réserve, mm
    for passe in (0, 1):
        is_h, etc_tot, eta_tot, arros = 0.0, 0.0, 0.0, 0.0
        for i, x in enumerate(an):
            kc = kc_s if saison[i] else kc_h
            etc = kc * x['et0']
            rew = 1 - dr / ru if ru > 0 else 0.0
            ks = 1.0 if rew >= (1 - p) else max(0.0, rew / (1 - p))       # FAO-56, équation 84
            eta = ks * etc
            dr = dr - x['rr'] * (1 + apport) + eta
            if dr < 0:
                dr = 0.0                                                    # percolation au-delà de la réserve
            if dr > ru:
                dr = ru
            if arrose and saison[i] and 1 - dr / ru < rew_a and x['heure'] == 2:
                arros += dr                                                 # arrosage nocturne jusqu'à la réserve pleine
                dr = 0.0
            if saison[i]:
                etc_tot += etc
                eta_tot += eta
                rew = 1 - dr / ru if ru > 0 else 0.0
                if rew < rew_s:
                    is_h += (rew_s - rew) / rew_s / 24                       # Granier et al. (1999), au pas horaire
    return dict(IS=is_h, deficit=1 - eta_tot / etc_tot if etc_tot else 0.0, arrosage_mm=arros)


def _apport(u):
    """Fiche A49 : apport de ruissellement par mm de pluie tombée sur l'unité (bassins versants raccordés)."""
    if not u['surface']:
        return 0.0
    return (u.get('bassin_versant', 0.0) * HYD[('*', 'coefficient_ruissellement')] +
            u.get('bassin_versant_permeable', 0.0) * HYD[('*', 'coefficient_ruissellement_permeable')]) / u['surface']


def k_hydrique(u, sol, contexte, niveau):
    """Fiche A50 : facteur hydrique d'une unité pour un niveau de réchauffement. Le stress est compté au-delà
    de celui du même groupe dans la situation de référence de la zone : sol de référence (limon d'un mètre,
    substrat de 10 cm pour une toiture extensive), sans arrosage ni apport, année type France +2 °C (C-W9)."""
    g = groupe_hydrique(u)
    if g is None:
        return 1.0, None
    zone, alt = contexte.get('zone_climatique', 'H1a'), contexte.get('altitude')
    if g == 'mare':
        param = (u.get('profondeur', HYD[('*', 'profondeur_mare_defaut')]),
                 HYD[(f'fond_{u.get("fond", "argile")}', 'infiltration')], round(_apport(u), 4))
        r = bilan_annee(zone, niveau, alt, g, 0.0, False, 0.0, param)
        return (HYD[('*', 'facteur_assec_precoce')] if r['assec_precoce'] else 1.0), dict(r, groupe=g)
    ru, _ = reserve_utile(u, sol)
    r = bilan_annee(zone, niveau, alt, g, round(ru, 3), bool(u.get('arrose')), round(_apport(u), 4), None)
    if g == 'toiture_extensive':
        ru_ref = 10 * 10 * HYD[('substrat', 'reserve_volumique')]
    else:
        ru_ref = 1000 * (HYD[('limon', 'theta_capacite_champ')] - HYD[('limon', 'theta_point_fletrissement')]) * min(
            HYD[(g, 'profondeur_racinaire')], HYD[('*', 'profondeur_sol_defaut')])
    ref = bilan_annee(zone, '2_0', alt, g, round(ru_ref, 3), False, 0.0, None)
    exces = r['IS'] - ref['IS'] - HYD[('*', 'tolerance_stress')]
    k = max(HYD[('*', 'facteur_hydrique_minimum')], 1 - HYD[(g, 'sensibilite_stress')] * max(0.0, exces) / 100)
    return k, dict(r, RU=ru, groupe=g, IS_ref=ref['IS'])


# ---------------------------------------------------------------- module L : éclairage horaire

def _heure_legale(mois):
    """C-L4 : heure légale = UTC + 2 d'avril à octobre, UTC + 1 sinon."""
    return 2 if 4 <= mois <= 10 else 1


@lru_cache(maxsize=None)
def fraction_eclairee(zone, extinction, rallumage):
    """Fiche A51 : part des heures de nuit de la saison d'activité des chiroptères pendant lesquelles
    l'éclairage est allumé. `extinction` et `rallumage` en heure légale (None : toute la nuit)."""
    an = climat.annee(zone, '2_0')
    m0, m1 = int(ECL[('*', 'saison_chiropteres_debut')]), int(ECL[('*', 'saison_chiropteres_fin')])
    nuit = allume = 0
    for x in an:
        if not m0 <= x['mois'] <= m1 or x['hs'] > ECL[('*', 'hauteur_soleil_nuit')]:
            continue
        nuit += 1
        h = (x['heure'] + _heure_legale(x['mois'])) % 24
        if extinction is None:
            allume += 1
            continue
        soir = h >= 12                                  # de midi à minuit : début de nuit
        if soir:
            ok = extinction >= 12 and h < extinction or extinction < 12
        else:
            ok = extinction < 12 and h < extinction
        if not ok and rallumage is not None and not soir and h >= rallumage:
            ok = True
        allume += ok
    return allume / nuit if nuit else 0.0


def facteur_spectral(cct):
    """Fiche A52 : interpolation linéaire entre les points de eclairage.csv."""
    pts = sorted((ECL[(k, 'temperature_couleur')], ECL[(k, 'facteur_spectral')])
                 for k, p in ECL if p == 'temperature_couleur')
    if cct <= pts[0][0]:
        return pts[0][1]
    for (t0, f0), (t1, f1) in zip(pts, pts[1:]):
        if cct <= t1:
            return f0 + (f1 - f0) * (cct - t0) / (t1 - t0)
    return pts[-1][1]


def facteur_distance(d):
    d0, d1 = ECL[('*', 'distance_effet_plein')], ECL[('*', 'distance_effet_nul')]
    return 1.0 if d <= d0 else 0.0 if d >= d1 else (d1 - d) / (d1 - d0)


PRESETS = {'L1': dict(extinction=1, rallumage=None, cct=3000, distance=0),
           'L2': dict(extinction=None, rallumage=None, cct=4000, distance=0)}


def k_lumiere(u, contexte):
    """Fiche A53 : k_L = 1 - perte_max x fraction éclairée x facteur spectral x facteur de distance."""
    e = u.get('eclairage', 'L0')
    if e == 'L0' or e is None:
        return 1.0, None
    p = PRESETS[e] if isinstance(e, str) else e
    x = fraction_eclairee(contexte.get('zone_climatique', 'H1a'), p.get('extinction'), p.get('rallumage'))
    x *= p.get('taux_detection', 1.0)
    s = facteur_spectral(p.get('cct', 3000))
    g = facteur_distance(p.get('distance', 0))
    return 1 - ECL[('*', 'perte_maximale')] * x * s * g, dict(fraction=x, spectral=s, distance=g)


# ---------------------------------------------------------------- module M : maturation et succession

def forme_maturation(u):
    c = u['code']
    if c.startswith(('G', 'VB.18')):
        return 'arboree'
    if c.startswith(('F', 'FA', 'FB')) or c in ('VB.6', 'VB.9'):
        return 'arbustive'
    return 'herbacee'


def maturation(tau, d, forme):
    """Fiche A54 : courbe de Chapman-Richards normée, g(d) = 1, pente initiale réglée par k x d."""
    if tau <= 0:
        return 0.0
    if d <= 0:
        return 1.0
    kd = SUC[('*', 'produit_k_d')]
    c = SUC[(forme, 'exposant_forme')]
    return min(1.0, ((1 - math.exp(-kd * tau / d)) / (1 - math.exp(-kd))) ** c)


HERBACES = ('gazon', 'prairie', 'xerophile')


def regime_gestion(u, annee_depuis_livraison, plan_annees):
    """Fiche A55 : régime de gestion d'une unité créée ou améliorée une année donnée. Pendant le plan de
    gestion déclaré, le régime est celui du plan ; ensuite, celui déclaré pour l'après-plan (par défaut,
    gestion courante, C-M3). Renvoie (régime, années écoulées dans ce régime)."""
    plan = u.get('plan_gestion_annees', plan_annees)
    if u.get('gestion') in ('courante', 'abandon'):
        return u['gestion'], annee_depuis_livraison
    if annee_depuis_livraison < plan:
        return 'plan', annee_depuis_livraison
    return u.get('apres_plan', 'courante'), annee_depuis_livraison - plan


HAB = _table('habitats.csv')
with open(os.path.join(RACINE, 'donnees', 'nomenclature_habitats.csv'), encoding='utf-8') as _f:
    BKOMPV = {r['code_vinat']: r['bkompv_code'] for r in csv.DictReader(_f, delimiter=';')}
PRAIRIES_GEREES = ('prairie', 'xerophile')
SANS_CONVERSION = ('VB.5', 'VB.7', 'VB.22')


def rapport_abandon(u):
    """C-M2 : rapport de la variante abandonnée de la BKompV au type exploité de l'unité ; moyenne des couples
    quand le type n'a pas de variante abandonnée."""
    code = BKOMPV.get(u['code'], '')
    for (cle, par), v in SUC.items():
        if par == 'rapport_abandon' and cle.split('>')[0] == code:
            return v
    return SUC[('*', 'rapport_abandon_moyen')]


def facteur_gestion(u, regime, duree, v_friche_arbustive):
    """Fiche A56 : rapport entre la valeur de l'unité sous un régime de gestion et sa valeur sous plan de
    gestion écologique.
    Gestion courante (C-M3) : une prairie ou une pelouse sèche est tondue comme une pelouse d'agrément (valeur
    intrinsèque de VB.5) ; une haie est taillée chaque année et reste au stade jeune de la BKompV.
    Abandon d'un milieu herbacé (C-M2) : variante abandonnée de la BKompV après deux ans, friche arbustive
    (VB.9) en état moyen après quinze ans."""
    if regime == 'plan' or u.get('S') is None:
        return 1.0
    g = groupe_hydrique(u)
    if regime == 'courante':
        if g in PRAIRIES_GEREES and u['code'] not in SANS_CONVERSION and u['position'] != 'hors_sol_toiture':
            return min(1.0, HAB[('VB.5', 'valeur_intrinseque')] / u['v'])
        if u['position'] == 'lineaire' and (u['code'], 'valeur_intrinseque_stade_J') in HAB:
            return min(1.0, HAB[(u['code'], 'valeur_intrinseque_stade_J')] / u['v'])
        return 1.0
    if regime == 'abandon' and g in HERBACES:
        if duree < SUC[('*', 'delai_friche_herbacee')]:
            return 1.0
        if duree < SUC[('*', 'delai_embroussaillement')]:
            return rapport_abandon(u)
        return v_friche_arbustive * (0.5 + 0.5 * SUC[('*', 'score_friche_embroussaillee')]) / (u['v'] * u['f'])
    return 1.0


# ---------------------------------------------------------------- module K : chantier au pas mensuel

def groupes_faune(u):
    """Fiche A57 : groupes de faune exposés à la destruction d'une unité."""
    c = u['code']
    g = []
    if c.startswith(('F', 'FA', 'G', 'VB.18', 'VB.9', 'E', 'VB.8', 'VB.26')):
        g.append('oiseaux')
    if (c.startswith(('G', 'VB.18')) and u.get('stade') == 'A') or u.get('gites'):
        g.append('chiropteres')
    if c.startswith(('C1', 'C3', 'D')) or c in ('VB.19', 'VB.20'):
        g.append('amphibiens')
    return g


def sensibilite(u, mois_calendaire):
    """Fiche A57 : sensibilité la plus forte des groupes de faune de l'unité au mois de la destruction."""
    return max([CHA[(g, f'sensibilite_m{mois_calendaire:02d}')] for g in groupes_faune(u)] or [0.0])


def mois_plantation(mois_debut, duree_mois):
    """Fiche A58 : rang (1 = premier mois du chantier) du premier mois favorable aux plantations, au plus tôt
    `avance_plantation` mois avant la fin du chantier."""
    rang = max(1, duree_mois - int(CHA[('*', 'avance_plantation')]) + 1)
    for i in range(rang, rang + 12):
        mc = (mois_debut - 1 + i - 1) % 12 + 1
        if CHA[('plantation', f'mois_favorable_m{mc:02d}')]:
            return i
    return rang
