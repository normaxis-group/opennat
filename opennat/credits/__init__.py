# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module des crédits OpenNAT (méthode OpenNAT Crédits, version 1) : gain créditable, émissions, réserve, suivi
par relevés, grille de risque, coût de revient, récapitulatif RSNat-C.

Le module appelle la chaîne de calcul d'OpenNAT 1 sans la modifier. Ses valeurs de méthode sont dans
`donnees/credits/credits.csv`, hors des tables d'OpenNAT 1, pour que l'empreinte des tables et la non-régression
d'OpenNAT 1 ne bougent pas."""

VERSION_METHODE_CREDITS = 'OpenNAT Crédits 1'
