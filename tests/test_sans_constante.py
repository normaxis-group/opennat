# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Exigence E2 : aucune valeur numérique de méthode dans le code du moteur.

Les seuls nombres admis sont 0, 1, 2 et -1, les gardes numériques contre la division par zéro, et quelques nombres
sans rapport avec la méthode, listés ci-dessous avec leur raison. `unites.py` (conversions d'unités, calendrier) et
`rsnat_spec.py` (nombre d'occurrences des éléments du schéma) sont exclus."""
import ast
import glob
import os

import opennat

ADMIS = {0, 1, 2, -1, 1e-9, 1e-12, 1e-300}
JUSTIFIES = {
    ('climat.py', 3): 'nombre de jalons de la TRACC',
    ('climat.py', 4): 'exposant de la loi de Stefan-Boltzmann (T puissance 4)',
    ('incertitude.py', 4): 'quatre premiers indicateurs (Cnat, Inat, Snat, Bnat)',
    ('pretraitement.py', 4): 'longueur d\'un code EUNIS de niveau 3 (« E2.2 »)',
    ('recapitulatif.py', 4): 'quatre décimales des facteurs (fiche A01)',
    ('rsnat.py', 4): 'quatre décimales des facteurs (fiche A01)',
    ('__main__.py', 3): 'code de sortie de la ligne de commande',
}
EXCLUS = ('unites.py', 'rsnat_spec.py')


def test_aucune_valeur_de_methode_dans_le_code():
    trouves = []
    for chemin in sorted(glob.glob(os.path.join(os.path.dirname(opennat.__file__), '*.py'))):
        nom = os.path.basename(chemin)
        if nom in EXCLUS:
            continue
        with open(chemin, encoding='utf-8') as f:
            arbre = ast.parse(f.read())
        for n in ast.walk(arbre):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
                if n.value not in ADMIS and (nom, n.value) not in JUSTIFIES:
                    trouves.append(f'{nom}, ligne {n.lineno} : {n.value}')
    assert not trouves, 'valeurs numériques dans le code :\n' + '\n'.join(trouves)


def test_chaque_fonction_de_calcul_cite_sa_fiche():
    """Exigence E3 : chaque module de calcul nomme les fiches qu'il applique."""
    for nom in ('sol', 'habitats', 'connectivite', 'nuisances', 'eau', 'climat', 'hydrique', 'temps', 'materiaux',
                'agregation', 'conformite', 'incertitude', 'pretraitement'):
        with open(os.path.join(os.path.dirname(opennat.__file__), nom + '.py'), encoding='utf-8') as f:
            arbre = ast.parse(f.read())
        for n in arbre.body:
            if isinstance(n, ast.FunctionDef) and not n.name.startswith('_'):
                doc = ast.get_docstring(n) or ''
                corps = ast.get_source_segment(open(os.path.join(os.path.dirname(opennat.__file__), nom + '.py'),
                                                    encoding='utf-8').read(), n)
                assert 'Fiche' in doc or 'fiche' in doc or '(A' in corps or 'convention' in doc.lower() or \
                    'Convention' in doc, f'{nom}.{n.name} ne cite ni fiche ni équation'
