# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module N : nuisances (fiches A20 à A22) et éclairage horaire (fiches A51 à A53)."""
from __future__ import annotations

from . import climat
from . import numerique as nm
from . import unites as U
from .donnees import Parametres

# Fiche A21-1 : milieux boisés pour le seuil de bruit
BOISE = ('G', 'F', 'FA', 'VB.18', 'VB.9')
_NUITS: dict[tuple, list] = {}


def _heures_de_nuit(P: Parametres, zone: str):
    """Heures de nuit de l'année type +2 °C de la zone : (mois, heure légale). Fiche A51-1 et convention C-L2."""
    k = (P.tables.dossier, zone)
    if k not in _NUITS:
        an = climat.annee_type(P, zone, '2_0', None)
        h_nuit = P.central('*', 'hauteur_soleil_nuit')
        e0, e1 = P.central('heure_legale', 'premier_mois_ete'), P.central('heure_legale', 'dernier_mois_ete')
        de, dh = P.central('heure_legale', 'decalage_ete'), P.central('heure_legale', 'decalage_hiver')
        _NUITS[k] = [(m, int((h + (de if e0 <= m <= e1 else dh)) % U.HEURES_PAR_JOUR))
                     for m, h, hs in zip(an.mois, an.heure, an.hs) if hs <= h_nuit]
    return _NUITS[k]


def allumee(h: int, extinction, rallumage) -> bool:
    """Fiche A51-2 : l'éclairage est-il allumé à l'heure légale h ?"""
    if extinction is None:
        return True
    soir = h >= U.DEMI_JOURNEE
    if soir:
        ok = (extinction >= U.DEMI_JOURNEE and h < extinction) or extinction < U.DEMI_JOURNEE
    else:
        ok = extinction < U.DEMI_JOURNEE and h < extinction
    if not ok and rallumage is not None and not soir and h >= rallumage:
        ok = True
    return ok


def fraction_eclairee(P: Parametres, zone: str, extinction, rallumage):
    """Fiche A51-3 : part des heures de nuit de la saison des chiroptères pendant lesquelles l'éclairage est allumé.

    Les mois de début et de fin de saison sont des paramètres tirables : la fraction se calcule mois par mois."""
    nuit, allume = [0] * (U.MOIS_PAR_AN + 1), [0] * (U.MOIS_PAR_AN + 1)
    for m, h in _heures_de_nuit(P, zone):
        nuit[m] += 1
        allume[m] += allumee(h, extinction, rallumage)
    m0, m1 = P('*', 'saison_chiropteres_debut'), P('*', 'saison_chiropteres_fin')
    n_nuit = sum(nm.si((m0 <= m) & (m <= m1) if nm.tableau(m0, m1) else (m0 <= m <= m1), nuit[m], 0)
                 for m in range(1, U.MOIS_PAR_AN + 1))
    n_all = sum(nm.si((m0 <= m) & (m <= m1) if nm.tableau(m0, m1) else (m0 <= m <= m1), allume[m], 0)
                for m in range(1, U.MOIS_PAR_AN + 1))
    return n_all / nm.maxi(n_nuit, 1)


def facteur_spectral(P: Parametres, cct: float):
    """Fiche A52-1 : interpolation entre les points de `eclairage.csv`."""
    cles = [k for (k, p) in P.tables.lignes if p == 'temperature_couleur' and P.tables.lignes[(k, p)].table == 'eclairage.csv']
    pts = sorted(((P.central(k, 'temperature_couleur'), P(k, 'facteur_spectral')) for k in cles), key=lambda x: x[0])
    if cct <= pts[0][0]:
        return pts[0][1]
    for (t0, f0), (t1, f1) in zip(pts, pts[1:]):
        if cct <= t1:
            return f0 + (f1 - f0) * (cct - t0) / (t1 - t0)
    return pts[-1][1]


def facteur_distance(P: Parametres, d: float):
    """Fiche A52-2."""
    d0, d1 = P('*', 'distance_effet_plein'), P('*', 'distance_effet_nul')
    return nm.si(d <= d0, 1.0, nm.si(d >= d1, 0.0, (d1 - d) / nm.maxi(d1 - d0, 1e-9)))


def parametres_eclairage(P: Parametres, e) -> dict | None:
    """Fiche A53-2 : raccourcis L0, L1, L2, ou éclairage déclaré."""
    if e in (None, 'L0'):
        return None
    if e == 'L1':
        return dict(extinction=int(P.central('raccourci_L1', 'heure_extinction')), rallumage=None,
                    cct=P.central('raccourci_L1', 'temperature_couleur'), distance=0.0, taux_detection=1.0)
    if e == 'L2':
        return dict(extinction=None, rallumage=None, cct=P.central('raccourci_L2', 'temperature_couleur'),
                    distance=0.0, taux_detection=1.0)
    return dict(extinction=e.get('extinction'), rallumage=e.get('rallumage'), cct=e.get('cct', e.get('temperature_couleur')),
                distance=e.get('distance', 0.0), taux_detection=e.get('taux_detection', e.get('part_detection', 1.0)))


def k_lumiere(P: Parametres, u: dict, zone: str):
    """Fiche A53-1 : facteur d'éclairage, et détail."""
    e = parametres_eclairage(P, u.get('eclairage'))
    if e is None:
        return 1.0, None
    x = fraction_eclairee(P, zone, e['extinction'], e['rallumage']) * e['taux_detection']
    s = facteur_spectral(P, e['cct'])
    g = facteur_distance(P, e['distance'])
    return 1 - P('*', 'perte_maximale') * x * s * g, dict(fraction=x, spectral=s, distance=g)


def k_bruit(P: Parametres, u: dict):
    """Fiche A21-2."""
    niveau = u.get('niveau_sonore')
    if niveau is None:
        return 1.0
    seuil = P('*', 'seuil_bruit_milieu_boise') if u['code'].startswith(BOISE) else P('*', 'seuil_bruit_milieu_ouvert')
    return nm.si(niveau > seuil, P('*', 'facteur_bruit_au_dela_seuil'), 1.0)


def k_vitrage(P: Parametres, u: dict):
    """Fiche A22-2 : l'exposition est déclarée par unité (façade non traitée de plus de 10 m² à moins de 15 m)."""
    return P('*', 'facteur_vitrage_non_traite') if u.get('exposition_vitrage') else 1.0


def nuisances(P: Parametres, u: dict, zone: str) -> dict:
    """Fiche A25-1 : k_N = k_lum x k_bruit x k_vit."""
    kl, det = k_lumiere(P, u, zone)
    kb, kv = k_bruit(P, u), k_vitrage(P, u)
    return dict(k_lum=kl, lumiere=det, k_bruit=kb, k_vit=kv, k_N=kl * kb * kv)


def surface_vitree_non_traitee(facades: list[dict]) -> float:
    """Fiche A22-1."""
    return sum(f['surface'] for f in facades if not f.get('traitee'))
