# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit donnees/constantes.csv : constantes des équations publiées que le moteur applique (FAO-56,
atmosphère type ISO 2533), et valeurs de règle des modules dynamiques qui n'avaient pas encore de ligne
(raccourcis d'éclairage, heure légale, heure d'arrosage, fenêtre d'assec, jalons de la TRACC), ainsi que
quelques seuils de contrôle des fiches A05, A14 à A16 et A49.

Le moteur n'écrit aucune valeur de méthode dans son code (exigence E2) : il lit tout ici ou dans les autres tables.
"""
import csv
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max', 'source',
            'reference_precise', 'url', 'licence', 'type', 'convention', 'justification']
FAO = 'Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration'
URL_FAO = 'https://www.fao.org/4/x0490e/x0490e00.htm'
LIC_FAO = 'citation de valeurs publiées'
OPENNAT = 'OpenNAT'
CC = 'CC BY 4.0'


def ligne(cle, par, val, unite, source, ref, url, lic, typ, conv, just):
    return dict(cle=cle, parametre=par, valeur=val, unite=unite, incertitude_min=val, incertitude_max=val,
                source=source, reference_precise=ref, url=url, licence=lic, type=typ, convention=conv,
                justification=just)


def fao(par, val, unite, eq, just):
    return ligne('fao56', par, val, unite, FAO, f'équation {eq}', URL_FAO, LIC_FAO, 'primaire', 'C-W2', just)


def regle(cle, par, val, unite, conv, just):
    return ligne(cle, par, val, unite, OPENNAT, 'valeur de règle', '', CC, 'convention', conv, just)


def main():
    t = [
        fao('albedo_reference', 0.23, 'sans unité', 38, 'Albédo du gazon de référence'),
        fao('cn_horaire', 37, 'K mm s³ Mg-1 h-1', 53, 'Constante Cn de l\'équation horaire, gazon de référence'),
        fao('cd_horaire', 0.34, 's/m', 53, 'Constante Cd de l\'équation horaire, gazon de référence'),
        fao('coefficient_rayonnement', 0.408, 'mm par MJ/m²', 53, 'Conversion de l\'énergie en lame d\'eau'),
        fao('saturation_a', 0.6108, 'kPa', 11, 'Pression de vapeur saturante, facteur'),
        fao('saturation_b', 17.27, 'sans unité', 11, 'Pression de vapeur saturante, coefficient'),
        fao('saturation_c', 237.3, '°C', 11, 'Pression de vapeur saturante, décalage'),
        fao('pente_saturation', 4098, '°C', 13, 'Pente de la courbe de pression de vapeur saturante'),
        fao('psychrometrique', 0.000665, 'kPa-1 °C-1 x kPa', 8, 'Constante psychrométrique par kPa de pression'),
        fao('vent_a', 4.87, 'sans unité', 47, 'Conversion du vent à 2 m, facteur'),
        fao('vent_b', 67.8, 'm-1', 47, 'Conversion du vent à 2 m, coefficient'),
        fao('vent_c', 5.42, 'sans unité', 47, 'Conversion du vent à 2 m, décalage'),
        fao('stefan_boltzmann_horaire', 2.043e-10, 'MJ K-4 m-2 h-1', 39, 'Constante de Stefan-Boltzmann au pas horaire '
            '(4,903 x 10^-9 / 24)'),
        fao('constante_solaire_horaire', 4.92, 'MJ m-2 h-1', 28, 'Constante solaire (0,0820 MJ/m²/min x 60)'),
        fao('excentricite', 0.033, 'sans unité', 23, 'Distance relative Terre-Soleil'),
        fao('rso_a', 0.75, 'sans unité', 37, 'Rayonnement par ciel clair, facteur'),
        fao('rso_b', 2e-5, 'm-1', 37, 'Rayonnement par ciel clair, effet de l\'altitude'),
        fao('rnl_a', 0.34, 'sans unité', 39, 'Rayonnement net de grande longueur d\'onde, terme a'),
        fao('rnl_b', 0.14, 'kPa-0,5', 39, 'Rayonnement net de grande longueur d\'onde, terme b'),
        fao('rnl_c', 1.35, 'sans unité', 39, 'Rayonnement net de grande longueur d\'onde, terme c'),
        fao('rnl_d', 0.35, 'sans unité', 39, 'Rayonnement net de grande longueur d\'onde, terme d'),
        fao('rapport_rs_rso_min', 0.3, 'sans unité', 39, 'Borne basse du rapport Rs/Rso'),
        fao('rapport_rs_rso_max', 1.0, 'sans unité', 39, 'Borne haute du rapport Rs/Rso'),
        ligne('fao56', 'rapport_rs_rso_initial', 0.7, 'sans unité', FAO, 'chapitre 4, rayonnement horaire de nuit',
              URL_FAO, LIC_FAO, 'convention', 'C-W2', 'Rapport Rs/Rso des premières heures de nuit du 1er janvier, '
              'avant tout relevé de jour'),
        fao('flux_sol_jour', 0.1, 'sans unité', 45, 'Flux de chaleur du sol de jour, part de Rn'),
        fao('flux_sol_nuit', 0.5, 'sans unité', 46, 'Flux de chaleur du sol de nuit, part de Rn'),
        fao('pression_temperature_reference', 293, 'K', 7, 'Température de référence de la formule de pression'),
        fao('pression_exposant', 5.26, 'sans unité', 7, 'Exposant de la formule de pression'),
        fao('decalage_kelvin', 273.16, 'K', 39, 'Conversion des °C en K, telle que la FAO-56 l\'écrit'),
        ligne('fao56', 'hauteur_soleil_rapport_nuit', 10, 'degré', FAO, 'chapitre 4, rayonnement horaire de nuit : '
              'rapport Rs/Rso pris en fin d\'après-midi', URL_FAO, LIC_FAO, 'convention', 'C-W2',
              'Hauteur du soleil au-dessus de laquelle le rapport Rs/Rso est relevé pour servir la nuit'),
        ligne('iso2533', 'gradient_thermique', 0.0065, 'K/m', 'ISO 2533:1975, atmosphère type',
              'gradient vertical de température de la troposphère', 'https://www.iso.org/standard/7472.html',
              'citation d\'une valeur normalisée', 'primaire', 'C-W1', 'Correction de température par l\'altitude'),
        ligne('fichiers_prospectifs', 'hauteur_anemometre', 10, 'm', 'ADEME, Météo-France, CSTB, DHUP, fichiers '
              'climatiques prospectifs (2025)', 'variable FF : force du vent à 10 mètres', '', 'Licence Ouverte 2.0',
              'primaire', 'C-W1', 'Hauteur de mesure du vent des années types'),
        regle('raccourci_L1', 'heure_extinction', 1, 'heure légale', 'C-L1', 'Raccourci L1 : extinction à 1 h, '
              'heure limite de l\'arrêté du 27 décembre 2018 pour les parcs, jardins et bâtiments non résidentiels'),
        regle('raccourci_L1', 'temperature_couleur', 3000, 'K', 'C-L1', 'Raccourci L1 : plafond de l\'arrêté'),
        regle('raccourci_L2', 'temperature_couleur', 4000, 'K', 'C-L1', 'Raccourci L2 : lumière froide toute la nuit'),
        regle('heure_legale', 'decalage_ete', 2, 'heure', 'C-L2', 'Heure légale d\'été : UTC + 2'),
        regle('heure_legale', 'decalage_hiver', 1, 'heure', 'C-L2', 'Heure légale d\'hiver : UTC + 1'),
        regle('heure_legale', 'premier_mois_ete', 4, 'mois', 'C-L2', 'Premier mois compté en heure d\'été'),
        regle('heure_legale', 'dernier_mois_ete', 10, 'mois', 'C-L2', 'Dernier mois compté en heure d\'été'),
        regle('arrosage', 'heure_utc', 2, 'heure', 'C-W10', 'Heure de l\'arrosage automatique nocturne'),
        regle('mare', 'premier_mois_assec', 3, 'mois', 'C-W12', 'Début de la fenêtre d\'assec pénalisé'),
        regle('mare', 'dernier_mois_assec', 6, 'mois', 'C-W12', 'Fin de la fenêtre d\'assec pénalisé'),
        regle('reference_hydrique', 'epaisseur_toiture', 10, 'cm', 'C-W9', 'Substrat de référence d\'une toiture '
              'extensive'),
        regle('tracc', 'jalon_1_annee', 2030, 'année', 'C-W13', 'Premier jalon de la TRACC'),
        regle('tracc', 'jalon_1_rechauffement', 2.0, '°C', 'C-W13', 'Réchauffement du premier jalon'),
        regle('tracc', 'jalon_2_annee', 2050, 'année', 'C-W13', 'Deuxième jalon de la TRACC'),
        regle('tracc', 'jalon_2_rechauffement', 2.7, '°C', 'C-W13', 'Réchauffement du deuxième jalon'),
        regle('tracc', 'jalon_3_annee', 2100, 'année', 'C-W13', 'Troisième jalon de la TRACC'),
        regle('tracc', 'jalon_3_rechauffement', 4.0, '°C', 'C-W13', 'Réchauffement du troisième jalon'),
        regle('controle', 'tolerance_coherence_rsee', 0.05, 'fraction de la parcelle', 'C-E3',
              'Écart toléré entre les surfaces déclarées au RSEE et les unités saisies (fiche A05, non bloquant)'),
        regle('controle', 'rapport_alerte_houppier', 2, 'sans unité', 'C-H5', 'Houppier relevé au-delà de ce multiple '
              'de la surface par défaut : signalé au journal (fiche A14)'),
        regle('controle', 'apport_alerte_ruissellement', 20, 'sans unité', 'C-W11', 'Surface raccordée au-delà de ce '
              'multiple de la surface de l\'unité : signalée au journal (fiche A49)'),
        regle('haie', 'largeur_minimale', 1, 'm', 'C-H5', 'Largeur minimale d\'une haie et de son ourlet (fiche A15)'),
        regle('facade', 'hauteur_maximale', 10, 'm', 'C-B1', 'Hauteur de façade végétalisée imputable (fiche A16)'),
        regle('toiture', 'epaisseur_semi_intensive', 15, 'cm', 'C-H3', 'Épaisseur à partir de laquelle une toiture '
              'est semi-intensive (fiche A16)'),
        regle('toiture', 'epaisseur_intensive', 30, 'cm', 'C-H3', 'Épaisseur au-delà de laquelle une toiture est '
              'intensive (fiche A16)'),
        regle('substrat', 'epaisseur_s05', 15, 'cm', 'C-S1', 'Borne basse de la classe S05 (fiche A06)'),
        regle('substrat', 'epaisseur_s06', 30, 'cm', 'C-S1', 'Borne haute de la classe S05 (fiche A06)'),
        regle('substrat', 'epaisseur_s07', 80, 'cm', 'C-S1', 'Borne basse de la classe S07 (fiche A06)'),
        regle('chantier', 'mois_debut_defaut', 1, 'mois', 'C-K3', 'Mois de début du chantier quand il n\'est pas '
              'déclaré : janvier'),
        regle('incertitude', 'tirages_defaut', 1000, 'tirages', 'C-I2', 'Nombre de tirages de l\'analyse '
              'd\'incertitude quand il n\'est pas déclaré'),
        regle('incertitude', 'graine_defaut', 20261018, 'sans unité', 'C-I2', 'Graine du générateur quand elle '
              'n\'est pas déclarée ; elle est écrite dans le RSNat'),
        regle('incertitude', 'centile_bas', 5, 'centile', 'C-I2', 'Borne basse de l\'intervalle à 90 % (fiche A39-3)'),
        regle('incertitude', 'centile_median', 50, 'centile', 'C-I2', 'Médiane des tirages (fiche A39-3)'),
        regle('incertitude', 'centile_haut', 95, 'centile', 'C-I2', 'Borne haute de l\'intervalle à 90 % (fiche A39-3)'),
        regle('incertitude', 'nombre_parametres_influents', 5, 'paramètres', 'C-I2', 'Paramètres les plus influents '
              'affichés (fiche A39-5)'),
        regle('incertitude', 'taille_bloc', 100, 'tirages', 'C-I2', 'Tirages calculés ensemble et écrits par bloc '
              '(reprise au premier bloc non écrit, fiche A42)'),
        regle('boisement', 'nombre_indicateurs', 13, 'indicateurs', 'C-H6', 'Indicateurs de la grille EB1 (fiche A11)'),
        regle('boisement', 'note_minimale', 1, 'note', 'C-H6', 'Note minimale d\'un indicateur de la grille EB1'),
        regle('boisement', 'note_maximale', 3, 'note', 'C-H6', 'Note maximale d\'un indicateur de la grille EB1'),
    ]
    with open(os.path.join(RACINE, 'donnees', 'constantes.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        w.writerows(t)
    print('constantes.csv', len(t))


if __name__ == '__main__':
    main()
