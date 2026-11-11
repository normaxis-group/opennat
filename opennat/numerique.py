# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Opérations qui acceptent un nombre (calcul aux valeurs centrales) ou un tableau numpy (un élément par tirage
de l'analyse d'incertitude, fiche A39). Le même code de calcul sert ainsi aux deux usages."""
import math

import numpy as np


def tableau(*x):
    return any(isinstance(v, np.ndarray) for v in x)


def mini(a, b):
    return np.minimum(a, b) if tableau(a, b) else min(a, b)


def maxi(a, b):
    return np.maximum(a, b) if tableau(a, b) else max(a, b)


def borne(x, a, b):
    return mini(maxi(x, a), b)


def et(a, b):
    return np.logical_and(a, b) if tableau(a, b) else a and b


def si(condition, a, b):
    """a là où la condition est vraie, b ailleurs."""
    if tableau(condition, a, b):
        return np.where(condition, a, b)
    return a if condition else b


def exp(x):
    return np.exp(x) if tableau(x) else math.exp(x)


def racine(x):
    return np.sqrt(x) if tableau(x) else math.sqrt(x)


def sinus_deg(x):
    return np.sin(np.radians(x)) if tableau(x) else math.sin(math.radians(x))


def cosinus(x):
    return np.cos(x) if tableau(x) else math.cos(x)


def log(x):
    return np.log(x) if tableau(x) else math.log(x)


def entier(x):
    """Arrondi à l'entier le plus proche (paramètres exprimés en mois, heures ou années)."""
    return np.rint(x).astype(int) if tableau(x) else int(round(x))


def scalaire(x):
    """Valeur d'affichage : le nombre lui-même, ou la moyenne d'un tableau."""
    return float(np.mean(x)) if tableau(x) else float(x)


def taille(x):
    return x.shape[0] if tableau(x) else 1
