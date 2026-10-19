# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Chargement et contrôle des tables de `donnees/` (fiche A01, exigences E1 et E2), paramètres tirables (fiche A39).

Au démarrage, toutes les tables sont lues et contrôlées : une ligne sans source, sans référence précise, sans
type connu, dont la convention n'est pas définie dans `methode/conventions.md` ou dont la valeur sort de sa plage
fait échouer le chargement, avec un message qui nomme la table, la ligne et la règle enfreinte.
"""
from __future__ import annotations

import csv
import glob
import gzip
import hashlib
import os
import re
import zlib

import numpy as np

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, 'donnees')
COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max', 'source',
            'reference_precise', 'url', 'licence', 'type', 'convention', 'justification']
TYPES = ('primaire', 'secondaire', 'transposition', 'convention')
HORS_REGISTRE = ('nomenclature_habitats.csv', 'conventions.csv')
# paramètres dont le tirage est arrondi à l'entier : un mois, une heure, une année n'ont pas de fraction
UNITES_ENTIERES = ('mois', 'heure', 'heure légale', 'année', 'jours', 'booléen', 'note', 'indicateurs')


class ErreurDonnees(Exception):
    """Table de données refusée au chargement."""


class ErreurParametre(KeyError):
    """Paramètre appelé par le calcul et absent des tables."""


def _conventions_definies():
    chemin = os.path.join(RACINE, 'methode', 'conventions.md')
    if not os.path.exists(chemin):
        return None
    with open(chemin, encoding='utf-8') as f:
        return set(re.findall(r'^#+\s*(C-[A-Z]+\d+)', f.read(), flags=re.M))


class Ligne:
    __slots__ = ('table', 'cle', 'parametre', 'valeur', 'a', 'b', 'unite', 'type', 'convention', 'source',
                 'reference')

    def __init__(self, table, r):
        self.table, self.cle, self.parametre = table, r['cle'], r['parametre']
        self.valeur, self.a, self.b = float(r['valeur']), float(r['incertitude_min']), float(r['incertitude_max'])
        self.unite, self.type, self.convention = r['unite'], r['type'], r['convention']
        self.source, self.reference = r['source'], r['reference_precise']


class Tables:
    """Toutes les tables de `donnees/`, contrôlées. `lignes[(clé, paramètre)]` donne la ligne."""

    def __init__(self, dossier: str = DONNEES):
        self.dossier = dossier
        self.lignes: dict[tuple[str, str], Ligne] = {}
        self.par_table: dict[str, list[Ligne]] = {}
        conv = _conventions_definies()
        erreurs = []
        for chemin in sorted(glob.glob(os.path.join(dossier, '*.csv'))):
            nom = os.path.basename(chemin)
            if nom in HORS_REGISTRE:
                continue
            with open(chemin, encoding='utf-8') as f:
                lecteur = csv.DictReader(f, delimiter=';')
                if lecteur.fieldnames != COLONNES:
                    erreurs.append(f'{nom} : colonnes {lecteur.fieldnames} au lieu de {COLONNES}')
                    continue
                self.par_table[nom] = []
                for i, r in enumerate(lecteur, 2):
                    ou = f'{nom}, ligne {i} ({r["cle"]} ; {r["parametre"]})'
                    if not r['source'].strip():
                        erreurs.append(f'{ou} : aucune source')
                    if not r['reference_precise'].strip():
                        erreurs.append(f'{ou} : aucune référence précise')
                    if r['type'] not in TYPES:
                        erreurs.append(f'{ou} : type « {r["type"]} » inconnu')
                    if r['type'] == 'convention' and not r['convention'].strip():
                        erreurs.append(f'{ou} : valeur de convention sans numéro de convention')
                    if r['convention'] and conv is not None and r['convention'] not in conv:
                        erreurs.append(f'{ou} : convention {r["convention"]} absente de methode/conventions.md')
                    try:
                        l = Ligne(nom, r)
                    except ValueError:
                        erreurs.append(f'{ou} : valeur ou plage non numérique')
                        continue
                    if not min(l.a, l.b) - 1e-12 <= l.valeur <= max(l.a, l.b) + 1e-12:
                        erreurs.append(f'{ou} : valeur {l.valeur} hors de sa plage [{l.a} ; {l.b}]')
                    if (l.cle, l.parametre) in self.lignes:
                        erreurs.append(f'{ou} : clé et paramètre déjà définis dans '
                                       f'{self.lignes[(l.cle, l.parametre)].table}')
                    self.lignes[(l.cle, l.parametre)] = l
                    self.par_table[nom].append(l)
        if erreurs:
            raise ErreurDonnees('Tables de données refusées :\n' + '\n'.join(erreurs))
        with open(os.path.join(dossier, 'nomenclature_habitats.csv'), encoding='utf-8') as f:
            self.nomenclature = {r['code_vinat']: r for r in csv.DictReader(f, delimiter=';')}
        self.empreinte = self._empreinte()

    def _empreinte(self) -> str:
        h = hashlib.sha256()
        fichiers = sorted(glob.glob(os.path.join(self.dossier, '*.csv')) +
                          glob.glob(os.path.join(self.dossier, 'climat', '*.gz')))
        for chemin in fichiers:
            h.update(os.path.relpath(chemin, self.dossier).replace('\\', '/').encode())
            with open(chemin, 'rb') as f:
                contenu = f.read()
            if chemin.endswith('.gz'):
                contenu = gzip.decompress(contenu)
            h.update(contenu.replace(b'\r\n', b'\n'))
        return h.hexdigest()

    def annee_type(self, niveau: str):
        """Lignes horaires d'une année type (fichier `donnees/climat/tracc_<niveau>.csv.gz`), par station."""
        par_station = {}
        with gzip.open(os.path.join(self.dossier, 'climat', f'tracc_{niveau}.csv.gz'), 'rt', encoding='utf-8') as f:
            for r in csv.DictReader(f, delimiter=';'):
                par_station.setdefault(r['station'], []).append(r)
        return par_station


def _graine_parametre(graine: int, cle: str, parametre: str) -> list[int]:
    """Graine propre à un paramètre : les tirages d'un paramètre ne dépendent ni de l'ordre d'appel des autres, ni
    du découpage des tirages en blocs (fiche A42, reprise au premier tirage non écrit)."""
    return [int(graine), zlib.crc32(f'{cle}\x1f{parametre}'.encode())]


class Parametres:
    """Accès aux valeurs de `donnees/` par clé et paramètre.

    Sans tirage, renvoie la valeur centrale. Avec un plan de tirage (graine, nombre total, début, fin), renvoie
    pour chaque paramètre de plage non nulle le tableau de ses tirages triangulaires de rang début à fin (fiche
    A39-1). Garde la liste des paramètres appelés, pour les corrélations de rang (fiche A39-4).
    """

    def __init__(self, tables: Tables, graine: int | None = None, n_total: int = 0, debut: int = 0, fin: int = 0):
        self.tables = tables
        self.graine, self.n_total, self.debut, self.fin = graine, n_total, debut, fin
        self.utilises: set[tuple[str, str]] = set()
        self._cache: dict[tuple[str, str], object] = {}

    @property
    def tirage(self) -> bool:
        return self.graine is not None

    def __call__(self, cle: str, parametre: str):
        k = (cle, parametre)
        if k in self._cache:
            return self._cache[k]
        l = self.tables.lignes.get(k)
        if l is None:
            raise ErreurParametre(f'paramètre absent des tables : clé « {cle} », paramètre « {parametre} »')
        self.utilises.add(k)
        if not self.tirage or l.a == l.b:
            v = l.valeur
        else:
            v = tirages(l, self.graine, self.n_total)[self.debut:self.fin]
        self._cache[k] = v
        return v

    def central(self, cle: str, parametre: str) -> float:
        """Valeur centrale, même en mode tirage (choix discrets qui ne se tirent pas)."""
        l = self.tables.lignes.get((cle, parametre))
        if l is None:
            raise ErreurParametre(f'paramètre absent des tables : clé « {cle} », paramètre « {parametre} »')
        return l.valeur

    def existe(self, cle: str, parametre: str) -> bool:
        return (cle, parametre) in self.tables.lignes


_TIRAGES: dict[tuple, np.ndarray] = {}


def tirages(l: Ligne, graine: int, n: int) -> np.ndarray:
    """Tous les tirages d'un paramètre : loi triangulaire de mode la valeur centrale (fiche A39-1, convention C-I2)."""
    k = (l.cle, l.parametre, graine, n)
    if k not in _TIRAGES:
        rng = np.random.default_rng(_graine_parametre(graine, l.cle, l.parametre))
        a, b = min(l.a, l.b), max(l.a, l.b)
        x = rng.triangular(a, min(max(l.valeur, a), b), b, size=n)
        if l.unite in UNITES_ENTIERES:
            x = np.rint(x)
        _TIRAGES[k] = x
    return _TIRAGES[k]
