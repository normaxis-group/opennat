# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module C : connectivité (fiches A17 à A19)."""
from __future__ import annotations

from . import numerique as nm
from .donnees import Parametres


def taches(unites: list[dict]) -> dict[str, float]:
    """Fiche A17 : affecte une tache à chaque unité de valeur non nulle et somme les surfaces (sans les arbres)."""
    for u in unites:                                                                       # (A17-1), (A17-2)
        if not u.get('tache') and u['position'] != 'arbre' and u['nature'] != 'S01':
            u['tache'] = 'isolee_' + u['id']
    surf = {}
    for u in unites:
        if u.get('tache') and u['position'] != 'arbre' and u['nature'] != 'S01':
            surf[u['tache']] = surf.get(u['tache'], 0.0) + u['surface']
    return surf


def k_taille(P: Parametres, a):
    """Fiche A18-1 [C2]."""
    z, aref, kmin = P('*', 'exposant_aire_especes'), P('*', 'surface_reference'), P('*', 'facteur_taille_minimum')
    return nm.mini(1.0, nm.maxi(kmin, (a / aref) ** z))


def connexion(P: Parametres, info: dict) -> str:
    """Fiche A19-1 : connexion déduite de la distance et de la surface de l'espace naturel quand elles sont
    saisies, déclarée sinon."""
    d = info.get('distance_espace_naturel')
    if d is None:
        return info.get('connexion') or 'faible'
    a = info.get('surface_espace_naturel', 0.0)
    if d == 0 and (a >= P.central('*', 'surface_minimale_espace_exterieur') or info.get('trame')):
        return 'forte'
    return 'moyenne' if d <= P.central('*', 'distance_connexion') else 'faible'


def facteurs(P: Parametres, surf: dict, infos: dict) -> dict:
    """Fiche A19-2 et A19-3 [C3] : facteur de chaque tache, avec son détail."""
    res = {}
    for t, a in surf.items():
        info = infos.get(t, {})
        a_eff = a + info.get('exterieur', 0.0)                                             # (A17-3) [C1]
        conn = connexion(P, info)
        m = P(f'connexion_{conn}', 'multiplicateur_connectivite')
        kclot = P('*', 'facteur_cloture_etanche') if info.get('cloture') == 'etanche' else 1.0
        kt = k_taille(P, a_eff)
        res[t] = dict(surface=a_eff, k_taille=kt, connexion=conn, m_conn=m, k_clot=kclot, k_C=kt * m * kclot)
    return res
