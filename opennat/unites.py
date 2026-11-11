# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Conversions d'unités et grandeurs du calendrier.

Ce ne sont pas des valeurs de méthode : ce sont des définitions d'unités. Elles sont réunies ici pour que la
recherche automatique de constantes (exigence E2) n'ait qu'un fichier à exclure.
"""
MM_PAR_M = 1000.0                 # mm par m
MM_PAR_CM = 10.0                  # mm par cm
M2_PAR_HA = 10000.0               # m² par ha
MJ_PAR_WH = 0.0036                # MJ/m²/h par W/m²
KPA_PAR_HPA = 0.1                 # kPa par hPa
MOIS_PAR_AN = 12
HEURES_PAR_JOUR = 24
JOURS_PAR_AN = 365
HEURES_PAR_AN = 8760
POINTS_PAR_UNITE = 100.0          # Bnat en points pour un coefficient de 1 ; sensibilité « par 100 jours »
JOURS_PAR_SENSIBILITE = 100.0
DEMI_JOURNEE = 12                 # heure qui sépare le soir du matin (fiche A51)
MIDI_UTC = 12                     # heure du relevé quotidien des jours en eau d'une mare (fiche A49)
POURCENT = 100.0                  # humidité relative en %
JOURS_DES_MOIS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)   # année non bissextile des fichiers types
