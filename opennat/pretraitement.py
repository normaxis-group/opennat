# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Étape E2 : prétraitement des surfaces (fiches A03 et A04), avec les règles de saisie des arbres, des haies, des
toitures et des façades (fiches A14 à A16) et les contrôles de cohérence avec le RSEE (fiche A05)."""
from __future__ import annotations

from .donnees import Parametres
from .habitats import ErreurSaisie
from .sol import AU_SOL

STADES = {'J': 'J', 'M': 'M', 'A': 'A', 'jeune': 'J', 'moyen': 'M', 'age': 'A'}
DIAMETRES = {'petit': 'J', 'moyen': 'M', 'grand': 'A', 'tres_grand': 'A'}               # convention C-H5


def code_opennat(P: Parametres, code: str) -> str:
    """Fiche A04-1."""
    nomen = P.tables.nomenclature
    if code in nomen:
        return code
    for c, n in nomen.items():
        if code == n['code_eunis_2012'] or code in n['alias_eunis_2012'].split():
            return c
    parent = code[:4] if len(code) > 4 and code[2] == '.' else None                      # niveau 3 : « E2.2 »
    if parent in nomen:
        return parent
    for c, n in nomen.items():
        if parent and n['code_eunis_2012'] == parent:
            return c
    raise ErreurSaisie(f'code d\'habitat inconnu : « {code} » (fiche A04)')


def classer(P: Parametres, u: dict, journal: list) -> dict:
    """Fiches A04, A14, A15, A16 : type, position, stade et surface de l'unité."""
    u = dict(u)
    saisi = u['code']
    u['code'] = code_opennat(P, saisi)
    if u['code'] != saisi:
        journal.append(f'unité {u["id"]} : code « {saisi} » saisi, type {u["code"]} retenu (fiche A04-1)')
    defaut = P.tables.nomenclature[u['code']]['position']
    pos = u.get('position')
    if defaut == 'sol':                                                                      # (A04-2)
        u['position'] = pos if pos in ('sol_pleine_terre', 'sol_sur_dalle') else 'sol_pleine_terre'
    else:
        u['position'] = defaut
    if pos and pos != u['position']:
        journal.append(f'unité {u["id"]} : position « {pos} » incompatible avec le type, « {u["position"]} » retenue')
    if u.get('stade'):
        u['stade'] = STADES[u['stade']]                                                      # (A04-3)
    elif u.get('classe_diametre'):
        u['stade'] = DIAMETRES[u['classe_diametre']]                                         # (A14-2)
    if u['position'] == 'arbre' and u.get('surface') is None:                                # (A14-1)
        cl = u.get('classe_diametre') or 'moyen'
        u['surface'] = u.get('nombre_arbres', 1) * P.central('VB.18', f'surface_defaut_houppier_{cl}')
        journal.append(f'unité {u["id"]} : houppier par défaut, {u.get("nombre_arbres", 1)} arbre(s) de classe {cl}')
    elif u['position'] == 'arbre' and u.get('classe_diametre'):
        ref = u.get('nombre_arbres', 1) * P.central('VB.18', f'surface_defaut_houppier_{u["classe_diametre"]}')
        if u['surface'] > P.central('controle', 'rapport_alerte_houppier') * ref:
            journal.append(f'unité {u["id"]} : houppier relevé de {u["surface"]:g} m², plus du double de la surface '
                           f'par défaut de sa classe (fiche A14)')
    if u['position'] == 'lineaire' and u.get('surface') is None:                             # (A15-1)
        lmin = P.central('haie', 'largeur_minimale')
        larg = u.get('largeur', lmin)
        if larg < lmin:
            journal.append(f'unité {u["id"]} : largeur de haie portée à {lmin:g} m (fiche A15)')
            larg = lmin
        u['surface'] = u['longueur'] * larg
    if u['position'] == 'hors_sol_facade' and u.get('surface') is None:                     # (A16-2)
        u['surface'] = u['longueur'] * min(u.get('hauteur', 0.0), P.central('facade', 'hauteur_maximale'))
    if u.get('surface') is None:
        raise ErreurSaisie(f'unité {u["id"]} : surface absente')
    if u['position'] in ('sol_sur_dalle', 'hors_sol_toiture') and u.get('epaisseur') is None \
            and u['code'] != 'VB.23':
        raise ErreurSaisie(f'unité {u["id"]} : épaisseur de substrat exigée sur dalle ou en toiture (fiche A04)')
    u['grille'] = P.tables.nomenclature[u['code']].get('grille_etat') or None
    return u


def fermeture(P: Parametres, unites: list[dict], sp: float) -> dict:
    """Fiche A03 [2]."""
    som = sum(u['surface'] for u in unites if u['position'] in AU_SOL)                       # (A03-1)
    eps = abs(som - sp)                                                                       # (A03-2)
    tol = max(P.central('*', 'tolerance_fermeture_absolue'), P.central('*', 'tolerance_fermeture_relative') * sp)
    return dict(somme=som, ecart=eps, tolerance=tol, conforme=eps <= tol)                    # (A03-3)


def coherence_rsee(P: Parametres, parcelle: dict, projet: list[dict], journal: list):
    """Fiche A05-5 et A05-6 : contrôles non bloquants."""
    sp = parcelle['surface']
    tol = P.central('controle', 'tolerance_coherence_rsee') * sp
    if 'surface_vegetalisee_rsee' in parcelle:
        veg = sum(u['surface'] for u in projet if u.get('nature') == 'S08')
        if abs(parcelle['surface_vegetalisee_rsee'] - veg) > tol:
            journal.append(f'surface végétalisée du RSEE {parcelle["surface_vegetalisee_rsee"]:g} m² contre {veg:g} m² '
                           f'en pleine terre à l\'état projet (fiche A05-5)')
    if 'surface_impermeable_rsee' in parcelle:
        imp = sum(u['surface'] for u in projet if u.get('nature') == 'S01')
        if abs(parcelle['surface_impermeable_rsee'] - imp) > tol:
            journal.append(f'surface imperméabilisée du RSEE {parcelle["surface_impermeable_rsee"]:g} m² contre '
                           f'{imp:g} m² scellés à l\'état projet (fiche A05-6)')
