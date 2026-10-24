# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Table `donnees/credits/credits.csv`, contrôlée comme les tables d'OpenNAT 1 (fiche A01) : source, référence
précise, type connu, convention définie dans `methode/credits/conventions_credits.md`, valeur dans sa plage."""
from __future__ import annotations

import csv
import hashlib
import os
import re

from ..donnees import COLONNES, RACINE, TYPES, ErreurDonnees, ErreurParametre, Ligne

TABLE = os.path.join(RACINE, 'donnees', 'credits', 'credits.csv')
CONVENTIONS = os.path.join(RACINE, 'methode', 'credits', 'conventions_credits.md')


def _conventions() -> set[str]:
    with open(CONVENTIONS, encoding='utf-8') as f:
        return set(re.findall(r'^#+\s*(C-X\d+)', f.read(), flags=re.M))


class TableCredits:
    """Valeurs de la méthode OpenNAT Crédits. `self(clé, paramètre)` renvoie la valeur centrale : aucune valeur de
    cette table ne se tire (plages nulles)."""

    def __init__(self, chemin: str = TABLE):
        conv = _conventions()
        self.lignes: dict[tuple[str, str], Ligne] = {}
        erreurs = []
        nom = os.path.basename(chemin)
        with open(chemin, encoding='utf-8') as f:
            lec = csv.DictReader(f, delimiter=';')
            if lec.fieldnames != COLONNES:
                raise ErreurDonnees(f'{nom} : colonnes {lec.fieldnames} au lieu de {COLONNES}')
            for i, r in enumerate(lec, 2):
                ou = f'{nom}, ligne {i} ({r["cle"]} ; {r["parametre"]})'
                if not r['source'].strip():
                    erreurs.append(f'{ou} : aucune source')
                if not r['reference_precise'].strip():
                    erreurs.append(f'{ou} : aucune référence précise')
                if r['type'] not in TYPES:
                    erreurs.append(f'{ou} : type « {r["type"]} » inconnu')
                if not r['convention'] or r['convention'] not in conv:
                    erreurs.append(f'{ou} : convention « {r["convention"]} » absente de conventions_credits.md')
                l = Ligne(nom, r)
                if not min(l.a, l.b) - 1e-12 <= l.valeur <= max(l.a, l.b) + 1e-12:
                    erreurs.append(f'{ou} : valeur {l.valeur} hors de sa plage')
                if (l.cle, l.parametre) in self.lignes:
                    erreurs.append(f'{ou} : clé et paramètre déjà définis')
                self.lignes[(l.cle, l.parametre)] = l
        if erreurs:
            raise ErreurDonnees('Table des crédits refusée :\n' + '\n'.join(erreurs))
        with open(chemin, 'rb') as f:
            self.empreinte = hashlib.sha256(f.read().replace(b'\r\n', b'\n')).hexdigest()

    def __call__(self, cle: str, parametre: str) -> float:
        l = self.lignes.get((cle, parametre))
        if l is None:
            raise ErreurParametre(f'paramètre absent de la table des crédits : « {cle} », « {parametre} »')
        return l.valeur

    def calendrier(self) -> list[int]:
        """Années de relevé depuis la fin des travaux de restauration (convention C-X12)."""
        k = sorted(p for (c, p) in self.lignes if c == 'credits' and p.startswith('releve_'))
        return sorted(int(self('credits', p)) for p in k)
