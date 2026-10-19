# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module T : temps (fiches A26 à A31), maturation, gestion et calendrier du chantier (fiches A54 à A58)."""
from __future__ import annotations

from . import climat
from . import hydrique
from . import numerique as nm
from . import unites as U
from .donnees import Parametres

# Fiche A56-2 : types qui ne changent pas en gestion courante
SANS_CONVERSION = ('VB.5', 'VB.7', 'VB.22')
PRAIRIES_GEREES = ('prairie', 'xerophile')
HERBACES = ('gazon', 'prairie', 'xerophile')
REFERENCE_GESTION_COURANTE = 'VB.5'          # pelouse d'agrément tondue (convention C-M3)
FRICHE_ARBUSTIVE = 'VB.9'                    # stade d'embroussaillement (convention C-M2)


def delai(P: Parametres, u: dict, k_delai):
    """Fiche A28-1 : délai de maturité de la classe visée, multiplié par le multiplicateur de délai."""
    cl = u['classe']
    for p in (f'delai_maturite_{cl}', 'delai_maturite_sans_etat'):
        if P.existe(u['code'], p):
            return k_delai * P(u['code'], p), p
    if cl != 'sans état':
        for alt in ('moyen', 'mauvais'):
            if P.existe(u['code'], f'delai_maturite_{alt}'):
                return k_delai * P(u['code'], f'delai_maturite_{alt}'), f'delai_maturite_{alt}'
    return 0.0, 'aucun délai (C-T3)'


def forme(u: dict) -> str:
    """Fiche A54-1."""
    c = u['code']
    if c.startswith(('G', 'VB.18')):
        return 'arboree'
    if c.startswith(('F', 'FA', 'FB')) or c in ('VB.6', 'VB.9'):
        return 'arbustive'
    return 'herbacee'


def maturation(P: Parametres, tau, d, fo: str):
    """Fiche A54-2 [T3] : courbe de Chapman-Richards ramenée à 1 au délai d."""
    if nm.tableau(d) or nm.tableau(tau):
        pass
    elif tau <= 0:
        return 0.0
    elif d <= 0:
        return 1.0
    kd, c = P('*', 'produit_k_d'), P(fo, 'exposant_forme')
    dd = nm.maxi(d, 1e-9)
    tp = nm.maxi(tau, 0.0)
    g = ((1 - nm.exp(-kd * tp / dd)) / (1 - nm.exp(-kd))) ** c
    g = nm.mini(1.0, g)
    return nm.si(tau <= 0, 0.0, nm.si(d <= 0, 1.0, g))


def rang_plantation(P: Parametres, mois_debut: int, duree_mois: int):
    """Fiche A58-2 : rang du premier mois favorable aux plantations, au plus tôt `avance` mois avant la fin."""
    avance = P('*', 'avance_plantation')

    def un(av):
        rang = max(1, duree_mois - int(av) + 1)
        for i in range(rang, rang + U.MOIS_PAR_AN):
            mc = (mois_debut - 1 + i - 1) % U.MOIS_PAR_AN + 1
            if P.central('plantation', f'mois_favorable_m{mc:02d}'):
                return i
        return rang
    if nm.tableau(avance):
        import numpy as np
        return np.array([un(a) for a in avance])
    return un(avance)


def regime(u: dict, ans_livraison, plan) -> tuple:
    """Fiche A55-2 : régime de gestion et années écoulées dans ce régime."""
    pl = u.get('plan_gestion_annees', plan)
    if u.get('gestion') in ('courante', 'abandon'):
        return u['gestion'], ans_livraison
    if ans_livraison < pl:
        return 'plan', ans_livraison
    return u.get('apres_plan') or 'courante', ans_livraison - pl


def rapport_abandon(P: Parametres, u: dict):
    """Convention C-M2 : variante abandonnée de la BKompV, moyenne des couples à défaut."""
    code = P.tables.nomenclature.get(u['code'], {}).get('bkompv_code', '')
    for (cle, par) in P.tables.lignes:
        if par == 'rapport_abandon' and cle.split('>')[0] == code:
            return P(cle, par)
    return P('*', 'rapport_abandon_moyen')


def facteur_gestion(P: Parametres, u: dict, reg: str, duree):
    """Fiche A56 : rapport de la valeur sous le régime à la valeur sous plan de gestion."""
    if reg == 'plan' or u.get('S') is None:
        return 1.0
    g = hydrique.groupe(u)
    if reg == 'courante':                                                                  # (A56-2)
        cible = 1.0
        if g in PRAIRIES_GEREES and u['code'] not in SANS_CONVERSION and u['position'] != 'hors_sol_toiture':
            cible = nm.mini(1.0, P(REFERENCE_GESTION_COURANTE, 'valeur_intrinseque') / u['v'])
        elif u['position'] == 'lineaire' and P.existe(u['code'], 'valeur_intrinseque_stade_J'):
            cible = nm.mini(1.0, P(u['code'], 'valeur_intrinseque_stade_J') / u['v'])
        if u.get('gestion') in ('courante', 'abandon'):
            return cible
        n = P('*', 'transition_fin_plan')                                                   # (A56-4), C-M3
        return 1.0 - (1.0 - cible) * nm.mini(1.0, duree / nm.maxi(n, 1e-9))
    if reg == 'abandon' and g in HERBACES:                                                 # (A56-3)
        fmin = P('*', 'facteur_etat_minimum')
        friche = P(FRICHE_ARBUSTIVE, 'valeur_intrinseque') * (fmin + (1 - fmin) * P('*', 'score_friche_embroussaillee'))
        d1, d2 = P('*', 'delai_friche_herbacee'), P('*', 'delai_embroussaillement')
        return nm.si(duree < d1, 1.0, nm.si(duree < d2, rapport_abandon(P, u), friche / (u['v'] * u['f'])))
    return 1.0


def trajectoires(P: Parametres, projet: list[dict], initial: dict, chantier: dict, plan, k_delai, annees) -> int:
    """Fiches A26 à A30 et A54 à A58 : trajectoire de chaque unité du projet, au pas mensuel, moyennée par année,
    multipliée par le facteur hydrique de l'année (A50) et le facteur de gestion (A56). Renvoie le rang de plantation."""
    n = int(P('*', 'periode_reference'))
    d_mois = int(round(chantier['duree_mois']))
    rang_pl = rang_plantation(P, chantier['mois_debut'], d_mois)
    r_ch = P('*', 'reduction_chantier_sans_protection')
    d_ind = P('*', 'duree_indisponibilite_renouvellement')
    for u in projet:
        statut = u.get('statut', 'creee')
        D = P(u['code'], 'difficulte_creation' if statut == 'creee' else 'difficulte_amelioration') \
            if P.existe(u['code'], 'difficulte_creation' if statut == 'creee' else 'difficulte_amelioration') else 1.0
        if statut == 'creee':
            d, src = delai(P, u, k_delai)
        elif statut == 'amelioree':
            u0 = initial[u['liee']]
            par = f'delai_amelioration_{u0["classe"]}_{u["classe"]}'
            d = k_delai * P(u['code'], par) if P.existe(u['code'], par) else 0.0              # (A29-1)
            src = par
        else:
            d, src = 0.0, 'conservée'
        fo = forme(u)
        dsc = nm.scalaire(d)
        depart = d_mois if dsc == 0 else rang_pl - 1                                        # (A58-3)
        u.update(D=D if statut != 'conservee' else 1.0, d=d, source_delai=src, forme=fo, mois_depart=depart)
        renouv = sorted(u.get('renouvellements', []))
        r = 0.0 if u.get('protection') else r_ch
        base = []
        for t in range(1, n + 1):
            somme = 0.0
            for mm in range(U.MOIS_PAR_AN * (t - 1) + 1, U.MOIS_PAR_AN * t + 1):
                phi = 1.0 if mm <= d_mois else 0.0                                          # (A26) au pas mensuel
                tau = (mm - depart) / U.MOIS_PAR_AN
                g = maturation(P, tau, d, fo)
                if statut == 'conservee':
                    x = u['V'] * (1 - r * phi)                                              # (A27-2) [T2]
                elif statut == 'amelioree':
                    v0 = initial[u['liee']]['V']
                    x = v0 * (1 - r * phi) + nm.maxi(0.0, D * u['V'] - v0) * g              # (A29-2) [T4]
                else:
                    x = D * u['V'] * g                                                      # (A28-3) [T3]
                for R in renouv:                                                            # (A30)
                    debut_r = U.MOIS_PAR_AN * R
                    fin_r = U.MOIS_PAR_AN * (R + d_ind)
                    x = nm.si(mm <= debut_r, x, nm.si(mm <= fin_r, 0.0,
                              D * u['V'] * maturation(P, (mm - fin_r) / U.MOIS_PAR_AN, d, fo)))
                somme = somme + x
            base.append(somme / U.MOIS_PAR_AN)
        kw = climat.par_annee(P, u['kW_niveaux'], annees)
        traj, gest = [], []
        for t in range(1, n + 1):
            ans = t - 1 - d_mois / U.MOIS_PAR_AN                                            # (A55-1)
            if statut == 'conservee' or ans < 0:
                fg = 1.0
            else:
                reg, duree = regime(u, ans, plan)
                fg = facteur_gestion(P, u, reg, duree)
            gest.append(fg)
            traj.append(base[t - 1] * kw[t - 1] * fg)                                       # [T6]
        u.update(traj_base=base, kW=kw, f_gestion=gest, traj=traj)
    return rang_pl


def groupes_faune(u: dict) -> list[str]:
    """Fiche A57-1."""
    c = u['code']
    g = []
    if c.startswith(('F', 'FA', 'G', 'VB.18', 'VB.9', 'E', 'VB.8', 'VB.26')):
        g.append('oiseaux')
    if (c.startswith(('G', 'VB.18')) and u.get('stade') == 'A') or u.get('gites'):
        g.append('chiropteres')
    if c.startswith(('C1', 'C3', 'D')) or c in ('VB.19', 'VB.20'):
        g.append('amphibiens')
    return g


def destruction(P: Parametres, initial: list[dict], projet: list[dict], mois_destruction: int):
    """Fiche A57 [T9] : supplément de Cnat pour les unités initiales détruites en période sensible."""
    gardees = {u.get('liee') for u in projet if u.get('statut') in ('conservee', 'amelioree')}
    perte = P('*', 'perte_destruction_sensible')
    total, detail = 0.0, []
    for u in initial:
        if u['id'] in gardees or nm.scalaire(u['V']) == 0:
            continue
        gr = groupes_faune(u)
        s = max([P.central(g, f'sensibilite_m{mois_destruction:02d}') for g in gr] or [0.0])   # (A57-2)
        if s:
            x = u['V'] * s * perte                                                          # (A57-3)
            total = total + x
            detail.append(dict(unite=u['id'], groupes=gr, sensibilite=s, supplement=x))
    return total, detail
