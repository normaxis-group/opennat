# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Fonctions communes aux générateurs de l'édition complète de la méthode OpenNAT."""
import csv
import os

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DON = os.path.join(RACINE, 'donnees')
EDITION = os.path.join(RACINE, 'methode', 'edition')
SOURCES = os.path.join(RACINE, 'sources')


def lire(nom, cle=None):
    with open(os.path.join(DON, nom), encoding='utf-8') as f:
        lignes = list(csv.DictReader(f, delimiter=';'))
    return lignes


def valeurs(nom):
    return {(r['cle'], r['parametre']): r for r in lire(nom)}


def nombre(x, dec=4):
    """Écriture française d'un nombre : virgule décimale, espace des milliers, zéros inutiles ôtés."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return str(x)
    if v != 0 and (abs(v) < 1e-3 or abs(v) >= 1e7):
        m, e = f'{v:.3e}'.split('e')
        return f'{m.replace(".", ",")} x 10^{int(e)}'
    s = f'{v:.{dec}f}'
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    ent, _, frac = s.partition('.')
    signe = '-' if ent.startswith('-') else ''
    ent = f'{int(ent.lstrip("-")):,}'.replace(',', ' ')
    return signe + ent + (',' + frac if frac else '')


def cellule(t):
    return str(t).replace('|', '/').replace('\n', ' ').strip()


def tableau(entetes, lignes):
    out = ['| ' + ' | '.join(entetes) + ' |', '|' + '---|' * len(entetes)]
    for l in lignes:
        out.append('| ' + ' | '.join(cellule(c) for c in l) + ' |')
    return '\n'.join(out)


def ecrire(nom, texte):
    os.makedirs(EDITION, exist_ok=True)
    chemin = os.path.join(EDITION, nom)
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(texte.rstrip() + '\n')
    return chemin


TYPES = {'primaire': 'primaire', 'transposition': 'transposée', 'secondaire': 'secondaire',
         'convention': 'convention'}
