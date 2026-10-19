# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Ajoute à donnees/nomenclature_habitats.csv la colonne `grille_etat` : grille d'état de chaque type
(convention C-H6), déduite du groupe de sa ligne dans la métrique anglaise et de sa distinctivité.

La règle est celle de la fonction `grille_de` de outils/edition/partie4_habitats.py ; la distinctivité se lit
dans l'onglet G-1 du tableur anglais (sources/, hors dépôt). Une fois la colonne écrite, le moteur ne lit plus
les sources : il lit la nomenclature.
"""
import csv
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'edition'))
from partie4_habitats import grille_de  # noqa: E402


def main():
    uk_dist = {}
    with open(os.path.join(RACINE, 'sources', 'uk_metric', 'extraits', 'G-1 All Habitats.csv'), encoding='utf-8') as f:
        for r in csv.reader(f):
            if r[0] not in ('1', '2') and r[2]:
                uk_dist.setdefault(r[2], float(r[12] or 0))
    chemin = os.path.join(RACINE, 'donnees', 'nomenclature_habitats.csv')
    with open(chemin, encoding='utf-8') as f:
        lecteur = csv.DictReader(f, delimiter=';')
        champs = [c for c in lecteur.fieldnames if c != 'grille_etat']
        lignes = list(lecteur)
    champs.insert(champs.index('uk_habitat') + 1, 'grille_etat')
    for n in lignes:
        n['grille_etat'] = grille_de(n['uk_habitat'], uk_dist.get(n['uk_habitat'], 0), n['position']) or ''
    with open(chemin, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=champs, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    from collections import Counter
    print(Counter(n['grille_etat'] or 'aucune' for n in lignes))


if __name__ == '__main__':
    main()
