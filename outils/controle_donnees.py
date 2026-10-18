# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Contrôle les tables de donnees/ et écrit le rapport de couverture.

Exigence E1 du cahier des charges : une ligne sans source fait échouer le chargement.
Le contrôle vérifie, pour chaque ligne de chaque table :
- les 13 colonnes du format commun ;
- une source, une référence précise et un type parmi primaire, secondaire,
  transposition, convention ;
- un numéro de convention pour toute ligne de type convention, et l'existence de ce
  numéro dans methode/conventions.md ;
- une valeur numérique comprise entre ses bornes d'incertitude.
Code de sortie 1 au premier défaut, avec la liste complète des défauts.
"""
import csv
import glob
import os
import re
import sys
from collections import Counter, defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DON = os.path.join(RACINE, 'donnees')
COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max',
            'source', 'reference_precise', 'url', 'licence', 'type', 'convention',
            'justification']
TYPES = ('primaire', 'secondaire', 'transposition', 'convention')
HORS_CONTROLE = ('nomenclature_habitats.csv', 'conventions.csv')


def conventions_definies():
    chemin = os.path.join(RACINE, 'methode', 'conventions.md')
    if not os.path.exists(chemin):
        return set()
    with open(chemin, encoding='utf-8') as f:
        return set(re.findall(r'^#+\s*(C-[A-Z]+\d+)', f.read(), flags=re.M))


def charger(chemin):
    with open(chemin, encoding='utf-8') as f:
        lecteur = csv.DictReader(f, delimiter=';')
        if lecteur.fieldnames != COLONNES:
            return None, [f'colonnes {lecteur.fieldnames} au lieu de {COLONNES}']
        return list(lecteur), []


def controler():
    defauts = []
    stats = {}
    conv_utilisees = Counter()
    conv_def = conventions_definies()
    for chemin in sorted(glob.glob(os.path.join(DON, '*.csv'))):
        nom = os.path.basename(chemin)
        if nom in HORS_CONTROLE:
            continue
        lignes, err = charger(chemin)
        defauts += [f'{nom} : {e}' for e in err]
        if lignes is None:
            continue
        compte = Counter()
        for i, l in enumerate(lignes, 2):
            ou = f'{nom} ligne {i} ({l["cle"]}, {l["parametre"]})'
            if not l['source'].strip():
                defauts.append(f'{ou} : aucune source')
            if not l['reference_precise'].strip():
                defauts.append(f'{ou} : aucune référence précise')
            if l['type'] not in TYPES:
                defauts.append(f'{ou} : type « {l["type"]} » inconnu')
            if l['type'] == 'convention' and not l['convention'].strip():
                defauts.append(f'{ou} : convention sans numéro')
            if l['convention']:
                conv_utilisees[l['convention']] += 1
                if conv_def and l['convention'] not in conv_def:
                    defauts.append(f'{ou} : convention {l["convention"]} absente de conventions.md')
            try:
                v, a, b = (float(l['valeur']), float(l['incertitude_min']),
                           float(l['incertitude_max']))
                if not (min(a, b) - 1e-12 <= v <= max(a, b) + 1e-12):
                    defauts.append(f'{ou} : valeur {v} hors de sa plage [{a}, {b}]')
            except ValueError:
                defauts.append(f'{ou} : valeur ou plage non numérique')
            compte[l['type']] += 1
        stats[nom] = compte
    return defauts, stats, conv_utilisees, conv_def


def rapport(stats, conv_utilisees, conv_def):
    total = Counter()
    for c in stats.values():
        total.update(c)
    lignes = ['# Rapport de couverture des tables de données OpenNAT', '',
              'Produit par `outils/controle_donnees.py`. Une ligne = une valeur.', '',
              '| Table | Lignes | Primaire | Transposition | Secondaire | Convention |',
              '|---|---|---|---|---|---|']
    for nom, c in stats.items():
        n = sum(c.values())
        lignes.append(f'| `{nom}` | {n} | {c["primaire"]} | {c["transposition"]} | '
                      f'{c["secondaire"]} | {c["convention"]} |')
    n = sum(total.values())
    lignes.append(f'| **Total** | {n} | {total["primaire"]} | {total["transposition"]} | '
                  f'{total["secondaire"]} | {total["convention"]} |')
    part = lambda k: f'{100 * total[k] / n:.0f} %' if n else '0 %'
    lignes += ['', f'Part des valeurs lues dans une source primaire ou transposées d\'une source '
                   f'primaire : {100 * (total["primaire"] + total["transposition"]) / n:.0f} %. '
                   f'Sources secondaires : {part("secondaire")}. Conventions : {part("convention")}.',
               '', 'Types : primaire = valeur lue telle quelle dans la source ; transposition = '
                   'valeur lue dans une source primaire et appliquée à OpenNAT par une '
                   'correspondance ou un changement d\'échelle écrit en convention ; secondaire = '
                   'valeur lue dans une source qui en cite une autre, à remplacer par la source '
                   'primaire ; convention = valeur fixée par OpenNAT et justifiée.', '',
               '## Conventions citées par les tables', '',
               '| Convention | Lignes |', '|---|---|']
    for c, k in sorted(conv_utilisees.items()):
        lignes.append(f'| {c} | {k} |')
    non_citees = sorted(conv_def - set(conv_utilisees))
    if non_citees:
        lignes += ['', 'Conventions de `conventions.md` sans ligne de données (elles portent sur '
                       'l\'algorithme) : ' + ', '.join(non_citees) + '.']
    with open(os.path.join(DON, 'rapport_couverture.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes) + '\n')


def index_conventions(conv_utilisees):
    """Écrit donnees/conventions.csv, index des conventions de methode/conventions.md."""
    chemin = os.path.join(RACINE, 'methode', 'conventions.md')
    with open(chemin, encoding='utf-8') as f:
        texte = f.read()
    blocs = re.split(r'^### ', texte, flags=re.M)[1:]
    familles = {'H': 'habitats', 'S': 'sols', 'E': 'contexte, eau et seuils',
                'C': 'connectivité', 'N': 'nuisances', 'T': 'temps',
                'G': 'biodiversité grise', 'I': 'incertitude', 'B': 'Bnat',
                'P': 'attestation au permis de construire'}
    lignes = []
    for b in blocs:
        num, reste = b.split('\n', 1)
        num = num.strip()
        cat = re.search(r'Catégorie : ([^.]+)\.', reste)
        corps = re.sub(r'Catégorie : [^.]+\.\s*', '', reste).strip()
        premiere = re.split(r'(?<=\.)\s', corps.replace('\n', ' '), maxsplit=1)[0]
        lignes.append({'numero': num, 'famille': familles[num[2]],
                       'categorie': cat.group(1) if cat else '',
                       'enonce': premiere.strip(), 'lignes_de_donnees': conv_utilisees.get(num, 0),
                       'statut': 'proposée, en attente de validation du Biodiversity Standard Council'})
    with open(os.path.join(DON, 'conventions.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0]), delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    return len(lignes)


def main():
    defauts, stats, conv_utilisees, conv_def = controler()
    rapport(stats, conv_utilisees, conv_def)
    print(f'conventions.csv : {index_conventions(conv_utilisees)} conventions')
    for nom, c in stats.items():
        print(f'{nom:24} {sum(c.values()):5} lignes  {dict(c)}')
    if defauts:
        print(f'\n{len(defauts)} défaut(s) :', file=sys.stderr)
        print('\n'.join(defauts), file=sys.stderr)
        sys.exit(1)
    print('\nAucun défaut : toutes les lignes ont une source et une référence.')


if __name__ == '__main__':
    main()
