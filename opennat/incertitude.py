# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Étape E4 : analyse d'incertitude (fiche A39).

Les tirages se calculent par blocs : chaque paramètre appelé reçoit, dans un bloc, le tableau de ses tirages de rang
début à fin, et la chaîne de calcul est jouée une fois sur ces tableaux. Les tirages d'un paramètre dépendent de la
graine et du paramètre seuls (pas de l'ordre d'appel ni du découpage) : un calcul interrompu reprend au premier bloc
non écrit et donne le même résultat au bit près (exigences E7, fiche A42)."""
from __future__ import annotations

import csv
import os

import numpy as np

from . import chaine
from .donnees import Parametres, Tables, tirages

INDICATEURS = (('cnat', ('E3', 'indicateurs', 'cnat')), ('inat', ('E3', 'indicateurs', 'inat')),
               ('snat', ('E3', 'indicateurs', 'snat')), ('bnat', ('E3', 'bnat', 'bnat')),
               ('niveau_cnat', ('E5', 'niveau_cnat')))


def _lire(d, chemin):
    for k in chemin:
        d = d[k]
    return d


def _vecteur(x, n):
    a = np.asarray(x, dtype=float)
    return np.full(n, float(a)) if a.ndim == 0 else a


def colonnes(e: dict) -> list[str]:
    """Fiche A42 : colonnes du fichier 12_E4_tirages.csv, une ligne par tirage."""
    return ['tirage'] + [f'v{v["index"]}_{k}' for v in e['variantes'] for k, _ in INDICATEURS]


def bloc(T: Tables, e: dict, graine: int, n_total: int, debut: int, fin: int) -> tuple[list[list], set]:
    """Fiche A39-2 : joue la chaîne sur les tirages de rang début à fin ; renvoie les lignes du fichier de tirages."""
    P = Parametres(T, graine, n_total, debut, fin)
    n = fin - debut
    cols = []
    cache = {}
    for v in e['variantes']:
        r = chaine.calculer(P, e, v, [], cache)
        for _, ch in INDICATEURS:
            cols.append(_vecteur(_lire(r['etapes'], ch), n))
    lignes = [[debut + i] + [float(c[i]) for c in cols] for i in range(n)]
    return lignes, P.utilises


def analyser(T: Tables, e: dict, dossier: str | None, progression=None) -> dict:
    """Fiche A39 : centiles et paramètres influents par variante, écarts entre variantes (fiche A41-2)."""
    opt = e['options']
    n_total, graine, taille = opt['tirages'], opt['graine'], opt['bloc']
    if n_total <= 0:
        return {}
    chemin = os.path.join(dossier, '12_E4_tirages.csv') if dossier else None
    lignes, utilises = [], set()
    if chemin and os.path.exists(chemin):                                             # reprise (fiche A42-2)
        with open(chemin, encoding='utf-8') as f:
            lec = csv.reader(f, delimiter=';')
            entete = next(lec, None)
            if entete == colonnes(e):
                lignes = [[int(r[0])] + [float(x) for x in r[1:]] for r in lec]
    if chemin and not lignes:
        with open(chemin, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f, delimiter=';').writerow(colonnes(e))
    debut = (len(lignes) // taille) * taille
    lignes = lignes[:debut]
    if chemin and debut:
        with open(chemin, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f, delimiter=';')
            w.writerow(colonnes(e))
            w.writerows(lignes)
    while debut < n_total:
        fin = min(n_total, debut + taille)
        nouv, u = bloc(T, e, graine, n_total, debut, fin)
        utilises |= u
        lignes += nouv
        if chemin:
            with open(chemin, 'a', newline='', encoding='utf-8') as f:
                csv.writer(f, delimiter=';').writerows(nouv)
        if progression:
            progression(fin, n_total)
        debut = fin
    if not utilises:                                              # reprise complète : liste des paramètres appelés
        _, utilises = bloc(T, e, graine, n_total, 0, 1)
    centiles = [T.lignes[('incertitude', k)].valeur for k in ('centile_bas', 'centile_median', 'centile_haut')]
    n_infl = int(T.lignes[('incertitude', 'nombre_parametres_influents')].valeur)
    m = np.array([l[1:] for l in lignes])
    noms = colonnes(e)[1:]
    res = {}
    params = [k for k in sorted(utilises) if T.lignes[k].a != T.lignes[k].b]
    rang = lambda x: np.argsort(np.argsort(x, kind='stable'), kind='stable').astype(float)   # noqa: E731
    ref = next(v for v in e['variantes'] if v.get('reference'))
    for v in e['variantes']:
        iv = {k: noms.index(f'v{v["index"]}_{k}') for k, _ in INDICATEURS}
        inter = []
        for k, _ in INDICATEURS[:4]:
            x = m[:, iv[k]]
            p = np.percentile(x, centiles)                                                  # (A39-3)
            inter.append(dict(indicateur=k, p5=float(p[0]), p50=float(p[1]), p95=float(p[2])))
        if v is not ref:
            ir = {k: noms.index(f'v{ref["index"]}_{k}') for k, _ in INDICATEURS}
            for k, _ in INDICATEURS[:4]:
                p = np.percentile(m[:, iv[k]] - m[:, ir[k]], centiles)                       # (A41-2)
                inter.append(dict(indicateur=f'ecart_{k}', p5=float(p[0]), p50=float(p[1]), p95=float(p[2])))
        snat = rang(m[:, iv['snat']])
        corr = []
        for cle in params:                                                                   # (A39-4)
            x = tirages(T.lignes[cle], graine, n_total)[:len(lignes)]
            if np.ptp(x) == 0:
                continue
            rx = rang(x)
            c = np.corrcoef(rx, snat)[0, 1]
            if np.isfinite(c):
                corr.append((abs(c), c, cle))
        corr.sort(key=lambda z: (-z[0], z[2]))
        influents = [dict(rang=i, table=T.lignes[cle].table, cle=cle[0], parametre=cle[1], correlation=float(c))
                     for i, (_, c, cle) in enumerate(corr[:n_infl], 1)]                      # (A39-5)
        res[v['index']] = dict(tirages=len(lignes), Intervalle=inter, Parametre_Influent=influents)
    return res
