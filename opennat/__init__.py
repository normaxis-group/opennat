# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Moteur de calcul OpenNAT.

Le moteur applique la méthode de calcul OpenNAT, version 1 : un module de code par module de la méthode, dans
l'ordre du chapitre 6 de la partie 1 (E1, E2, S, H, C, N, E, W, T, G, E3, E4, E5). Les fiches algorithmes de la
partie 3 de l'édition complète en sont la spécification ; chaque fonction cite la fiche et l'équation qu'elle
applique. Aucune valeur de méthode n'est écrite dans le code : toutes viennent de `donnees/`.
"""
VERSION_METHODE = 'OpenNAT 1'
VERSION_MOTEUR = '0.1.0'
