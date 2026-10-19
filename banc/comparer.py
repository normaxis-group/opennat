# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Banc de validation (exigence E10) : calcule chaque cas de `banc/cas/` avec le moteur, aux valeurs centrales, et
compare aux résultats du carnet de référence (`banc/attendus.json`). Tolérance : 0,1 % en relatif, ou 0,05 en
absolu pour les grandeurs proches de zéro.

Usage : python -m banc.comparer [motif]
"""
import json
import os
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat import chaine, projet  # noqa: E402
from opennat.donnees import Parametres, Tables  # noqa: E402

TOL_REL, TOL_ABS = 1e-3, 0.05
GRANDEURS = (('v0', ('E3', 'integration', 'v0')), ('i0', ('E3', 'integration', 'i0')),
             ('i1', ('E3', 'integration', 'i1')), ('dm', ('E3', 'integration', 'dm')),
             ('faune', ('T', 'supplement_destruction')), ('cnat', ('E3', 'indicateurs', 'cnat')),
             ('cnat_30', ('E3', 'indicateurs', 'cnat_30')), ('inat', ('E3', 'indicateurs', 'inat')),
             ('snat', ('E3', 'indicateurs', 'snat')), ('bnat', ('E3', 'bnat', 'bnat')),
             ('pt', ('S', 'pleine_terre')), ('arrosage_m3_an', ('E3', 'arrosage_m3_an')),
             ('niveau', ('E5', 'niveau_cnat')))


def lire(d, chemin):
    for k in chemin:
        d = d[k]
    return d


def ecart_ok(a, b):
    return abs(a - b) <= max(TOL_ABS, TOL_REL * abs(b))


def attendus() -> dict:
    with open(os.path.join(ICI, 'attendus.json'), encoding='utf-8') as f:
        return json.load(f)


def ecarts_cas(T: Tables, nom: str, att: dict) -> list[str]:
    """Écarts entre le moteur et le carnet de référence pour un cas ; liste vide si le cas passe."""
    P = Parametres(T)
    e, journal = projet.normaliser(P, projet.lire(os.path.join(ICI, 'cas', nom)))
    r = chaine.calculer(P, e, e['variantes'][0], journal)
    et = r['etapes']
    ecarts = []
    for cle, chemin in GRANDEURS:
        x, y = lire(et, chemin), att[cle]
        if not ecart_ok(float(x), float(y)):
            ecarts.append(f'{cle} {x:.4f} contre {y:.4f}')
    for u in r['projet']:
        a = att['unites'][u['id']]
        if not ecart_ok(u['V'], a['V']):
            ecarts.append(f'{u["id"]} V {u["V"]:.4f} contre {a["V"]:.4f}')
        for t, (x, y) in enumerate(zip(u['traj'], a['traj']), 1):
            if not ecart_ok(x, y):
                ecarts.append(f'{u["id"]} année {t} {x:.4f} contre {y:.4f}')
                break
    return ecarts


def main(motif=''):
    T = Tables()
    n_ok = n = 0
    t0 = time.time()
    defauts = []
    for nom, att in attendus().items():
        if motif not in nom:
            continue
        n += 1
        ecarts = ecarts_cas(T, nom, att)
        if ecarts:
            defauts.append((nom, ecarts))
        else:
            n_ok += 1
    for nom, ec in defauts:
        print(f'ÉCHEC {nom} : ' + ' ; '.join(ec[:6]))
    print(f'{n_ok} cas sur {n} retrouvent le carnet de référence à 0,1 % ({time.time() - t0:.0f} s)')
    return n_ok == n


if __name__ == '__main__':
    sys.exit(0 if main(sys.argv[1] if len(sys.argv) > 1 else '') else 1)
