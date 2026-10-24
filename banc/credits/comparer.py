# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Banc des crédits : calcule chaque cas de `banc/credits/cas/` avec le moteur, aux valeurs centrales, et le compare
au carnet de référence des crédits (`banc/credits/attendus.json`). Tolérance : 10⁻⁶ en relatif, ou 10⁻⁶ en absolu
pour une grandeur proche de zéro (le carnet d'OpenNAT 1 et le moteur divergent déjà de 10⁻⁸ sur les trajectoires) ;
égalité stricte pour les nombres de crédits.

Usage : python -m banc.credits.comparer [motif]"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(ICI)))
from opennat.credits import calcul  # noqa: E402

TOL_REL, TOL_ABS = 1e-6, 1e-6


def proche(a, b):
    return abs(a - b) <= max(TOL_ABS, TOL_REL * abs(b))


def attendus() -> dict:
    with open(os.path.join(ICI, 'attendus.json'), encoding='utf-8') as f:
        return json.load(f)


def ecarts_cas(nom: str, att: dict) -> list[str]:
    r = calcul.calculer(os.path.join(ICI, 'cas', nom), tirages=0)
    g, em = r['gains'], r['emissions']
    e = []
    if not proche(g['prevision']['gain']['centrale'], att['g_prev']):
        e.append(f'gain prévu {g["prevision"]["gain"]["centrale"]} contre {att["g_prev"]}')
    if not proche(g['prevision']['i_projet']['centrale'], att['i_prev']):
        e.append(f'I_projet prévu {g["prevision"]["i_projet"]["centrale"]} contre {att["i_prev"]}')
    if not proche(g['prevision']['i_reference']['centrale'], att['i_ref']):
        e.append(f'I_ref {g["prevision"]["i_reference"]["centrale"]} contre {att["i_ref"]}')
    if not proche(r['risque']['taux'], att['taux']):
        e.append(f'taux de réserve {r["risque"]["taux"]} contre {att["taux"]}')
    for k in ('unites_previsionnelles', 'plafond'):
        if em[k] != att[{'unites_previsionnelles': 'up', 'plafond': 'plafond'}[k]]:
            e.append(f'{k} {em[k]} contre {att[k if k == "plafond" else "up"]}')
    if len(em['verifications']) != len(att['verifications']):
        return e + ['nombre de vérifications différent']
    for i, (v, l, a) in enumerate(zip(g['verifications'], em['verifications'], att['verifications']), 1):
        if not proche(v['gain']['centrale'], a['gain']):
            e.append(f'vérification {i} : gain {v["gain"]["centrale"]} contre {a["gain"]}')
        for k, ka in (('credits_emis_cumul', 'emis'), ('emission', 'emission'), ('inversion', 'inversion')):
            if l[k] != a[ka]:
                e.append(f'vérification {i} : {k} {l[k]} contre {a[ka]}')
        if not proche(l['reserve_cumul'], a['reserve']):
            e.append(f'vérification {i} : réserve {l["reserve_cumul"]} contre {a["reserve"]}')
    return e


def main(motif: str = '') -> int:
    att = attendus()
    echecs = 0
    for nom in sorted(att):
        if motif not in nom:
            continue
        e = ecarts_cas(nom, att[nom])
        print(f'{nom} : ' + ('conforme' if not e else '; '.join(e)))
        echecs += bool(e)
    print(f'{len(att) - echecs} cas conformes sur {len(att)}' if not motif else '')
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ''))
