# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit les tables des modules dynamiques : donnees/hydrique.csv, eclairage.csv, succession.csv et
chantier.csv. Chaque ligne porte sa source, sa référence précise, sa licence, son type et, s'il y a lieu, sa
convention, comme les autres tables de donnees/.
"""
import csv
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max', 'source',
            'reference_precise', 'url', 'licence', 'type', 'convention', 'justification']

FAO = 'Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration'
URL_FAO = 'https://www.fao.org/4/x0490e/x0490e00.htm'
LIC_FAO = 'citation de valeurs publiées (FAO, reproduction autorisée à des fins non commerciales)'
GRANIER = ('Granier A., Bréda N., Biron P., Villette S. (1999), A lumped water balance model to evaluate '
           'duration and intensity of drought constraints in forest stands, Ecological Modelling 116')
URL_GRANIER = 'https://doi.org/10.1016/S0304-3800(98)00205-1'
OPENNAT = 'OpenNAT'
CC = 'CC BY 4.0'


def L(cle, parametre, valeur, unite, imin, imax, source, ref, url, licence, typ, conv, just):
    return dict(cle=cle, parametre=parametre, valeur=valeur, unite=unite, incertitude_min=imin,
                incertitude_max=imax, source=source, reference_precise=ref, url=url, licence=licence, type=typ,
                convention=conv, justification=just)


def hydrique():
    t = []
    # FAO-56, tableau 19 : teneurs en eau à la capacité au champ et au point de flétrissement (milieu de plage)
    textures = [('sable', 'Sand', (0.07, 0.17), (0.02, 0.07)),
                ('sable_limoneux', 'Loamy sand', (0.11, 0.19), (0.03, 0.10)),
                ('limon_sableux', 'Sandy loam', (0.18, 0.28), (0.06, 0.16)),
                ('limon', 'Loam', (0.20, 0.30), (0.07, 0.17)),
                ('limon_silteux', 'Silt loam', (0.22, 0.36), (0.09, 0.21)),
                ('silt', 'Silt', (0.28, 0.36), (0.12, 0.22)),
                ('limon_argilo_silteux', 'Silt clay loam', (0.30, 0.37), (0.17, 0.24)),
                ('argile_silteuse', 'Silty clay', (0.30, 0.42), (0.17, 0.29)),
                ('argile', 'Clay', (0.32, 0.40), (0.20, 0.24))]
    for cle, en, cc, pf in textures:
        for par, (a, b) in (('theta_capacite_champ', cc), ('theta_point_fletrissement', pf)):
            t.append(L(cle, par, round((a + b) / 2, 3), 'm³/m³', a, b, FAO, f'tableau 19, ligne « {en} », milieu de '
                       f'la plage', URL_FAO, LIC_FAO, 'primaire', 'C-W4',
                       'Classe de texture de la classification américaine, déclarée par le bureau d\'études '
                       '(étude de sol ou géotechnique) ; à défaut, limon'))
    t.append(L('*', 'profondeur_sol_defaut', 1.0, 'm', 0.5, 1.5, OPENNAT, 'valeur de secours', '', CC, 'convention',
               'C-W4', 'Profondeur de sol explorable par les racines en pleine terre quand elle n\'est pas déclarée'))
    t.append(L('substrat', 'reserve_volumique', 0.20, 'm³/m³', 0.12, 0.30, OPENNAT,
               'valeur de secours pour les substrats de toiture et de dalle', '', CC, 'convention', 'C-W5',
               'Eau utile d\'un substrat de toiture ou de dalle par unité de volume, faute de valeur déclarée par '
               'le fabricant ; la couche de drainage n\'est pas comptée'))
    # groupes hydriques : coefficients culturaux (tableau 12), profondeur racinaire et fraction p (tableau 22)
    groupes = [
        ('gazon', 0.95, 0.90, 0.75, 0.40, 'tableau 12 « Turf grass, cool season » (Kc ini 0,90, Kc mi 0,95) ; '
         'tableau 22 « Turf grass, cool season » (Zr 0,5 à 1,0 m, p 0,40)', 'primaire'),
        ('prairie', 0.75, 0.30, 1.0, 0.60, 'tableau 12 « Grazing pasture, extensive grazing » (Kc ini 0,30, Kc mi '
         '0,75) ; tableau 22 « Grazing pasture, extensive » (Zr 0,5 à 1,5 m, p 0,60)', 'transposition'),
        ('xerophile', 0.75, 0.30, 1.0, 0.60, 'mêmes valeurs que le groupe prairie (tableaux 12 et 22, « Grazing '
         'pasture, extensive »)', 'transposition'),
        ('arbustif', 1.05, 0.30, 0.9, 0.50, 'tableau 12 « Berries (bushes) » (Kc ini 0,30, Kc mi 1,05) ; tableau 22 '
         '« Berries (bushes) » (Zr 0,6 à 1,2 m, p 0,50)', 'transposition'),
        ('arbore', 1.20, 0.50, 1.5, 0.50, 'tableau 12 « Apples, Cherries, Pears, active ground cover, killing '
         'frost » (Kc ini 0,50, Kc mi 1,20) ; tableau 22 « Apples, cherries, pears » (Zr 1,0 à 2,0 m, p 0,50)',
         'transposition'),
        ('conifere', 1.00, 1.00, 1.25, 0.70, 'tableau 12 « Conifer Trees » (Kc 1,00) ; tableau 22 « Conifer '
         'trees » (Zr 1,0 à 1,5 m, p 0,70)', 'primaire'),
        ('humide_pluie', 1.20, 0.90, 0.5, 0.30, 'tableau 12 « Reed Swamp, moist soil » (Kc ini 0,90, Kc mi 1,20) ; '
         'profondeur et fraction p fixées par convention', 'transposition'),
        ('mare', 1.05, 1.05, 0.0, 0.0, 'tableau 12 « Open Water, < 2 m depth » (Kc 1,05)', 'primaire'),
    ]
    for g, kcs, kch, zr, p, ref, typ in groupes:
        conv = 'C-W6'
        just = f'Groupe hydrique {g} (fiche A47)'
        t.append(L(g, 'kc_saison', kcs, 'sans unité', round(kcs * 0.85, 2), round(min(1.3, kcs * 1.15), 2), FAO, ref,
                   URL_FAO, LIC_FAO, typ, conv, just + ' : coefficient cultural en saison de végétation'))
        t.append(L(g, 'kc_hors_saison', kch, 'sans unité', round(kch * 0.8, 2), round(kch * 1.2, 2), FAO, ref,
                   URL_FAO, LIC_FAO, typ, conv, just + ' : coefficient cultural hors saison'))
        if g != 'mare':
            t.append(L(g, 'profondeur_racinaire', zr, 'm', round(zr * 0.67, 2), round(zr * 1.33, 2), FAO, ref, URL_FAO,
                       LIC_FAO, typ, conv, just + ' : profondeur racinaire, milieu de la plage FAO'))
            t.append(L(g, 'fraction_p', p, 'fraction', round(max(0.1, p - 0.1), 2), round(min(0.8, p + 0.1), 2), FAO,
                       ref, URL_FAO, LIC_FAO, typ, conv, just + ' : fraction de la réserve utile consommée sans '
                       'réduction de la transpiration'))
    t.append(L('toiture_extensive', 'kc_saison', 0.50, 'sans unité', 0.30, 0.80, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W6', 'Végétation de toiture extensive (orpins, mousses, graminées basses) : la FAO-56 '
               'ne donne pas de coefficient ; demi-valeur du gazon, plage large'))
    t.append(L('toiture_extensive', 'kc_hors_saison', 0.30, 'sans unité', 0.20, 0.50, OPENNAT, 'valeur de secours',
               '', CC, 'convention', 'C-W6', 'Comme ci-dessus, hors saison de végétation'))
    t.append(L('toiture_extensive', 'profondeur_racinaire', 0.15, 'm', 0.10, 0.15, OPENNAT,
               'bornée par l\'épaisseur du substrat', '', CC, 'convention', 'C-W6',
               'Sans objet en pratique : la réserve d\'un substrat se calcule sur son épaisseur (fiche A48)'))
    t.append(L('toiture_extensive', 'fraction_p', 0.60, 'fraction', 0.50, 0.70, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W6', 'Végétation succulente tolérante au dessèchement : fraction du groupe prairie'))
    # stress hydrique : seuil de Granier, saison de végétation, lien avec la valeur
    t.append(L('*', 'seuil_rew_stress', 0.4, 'fraction', 0.3, 0.5, GRANIER, 'seuil de réserve extractible relative '
               'sous lequel la transpiration est réduite (REW < 0,4) et indice de stress IS = somme de (0,4 - REW) / 0,4',
               URL_GRANIER, 'citation d\'une méthode publiée', 'transposition', 'C-W8',
               'Indice établi pour les peuplements forestiers (modèle BILJOU), étendu à tous les groupes et calculé '
               'au pas horaire'))
    t.append(L('*', 'seuil_saison_temperature', 5.0, '°C', 5.0, 5.0,
               'ETCCDI, indices climatiques extrêmes', 'indice GSL (durée de la saison de croissance) : température '
               'moyenne quotidienne supérieure à 5 °C', 'https://etccdi.pacificclimate.org/list_27_indices.shtml',
               'citation d\'une définition publiée', 'transposition', 'C-W7',
               'Seuil de la saison de végétation'))
    t.append(L('*', 'seuil_saison_jours', 6, 'jours', 6, 6, 'ETCCDI, indices climatiques extrêmes',
               'indice GSL : six jours consécutifs', 'https://etccdi.pacificclimate.org/list_27_indices.shtml',
               'citation d\'une définition publiée', 'transposition', 'C-W7',
               'Fenêtre glissante de la moyenne de température'))
    t.append(L('*', 'tolerance_stress', 5, 'jours-équivalents', 0, 15, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W9', "Écart d'indice de stress à la référence de la zone en deçà duquel la valeur "
               "n'est pas réduite"))
    sens = {'gazon': 0.5, 'prairie': 0.4, 'xerophile': 0.3, 'arbustif': 0.6, 'arbore': 0.8, 'conifere': 0.8,
            'toiture_extensive': 0.3, 'humide_pluie': 1.0}
    for g, b in sens.items():
        t.append(L(g, 'sensibilite_stress', b, 'par 100 jours-équivalents', round(b * 0.5, 2), round(b * 1.5, 2),
                   OPENNAT, 'valeur de secours', '', CC, 'convention', 'C-W9',
                   f'Perte de valeur du groupe {g} par 100 jours-équivalents de stress au-delà de la référence de la '
                   f'zone et de la tolérance'))
    t.append(L('*', 'facteur_hydrique_minimum', 0.5, 'sans unité', 0.3, 0.7, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W9', 'Plancher du facteur hydrique : un milieu en stress chronique garde la moitié '
               'de sa valeur, comme un milieu en mauvais état (C-H2)'))
    t.append(L('*', 'seuil_rew_arrosage', 0.5, 'fraction', 0.4, 0.6, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W10', 'Un arrosage automatique remplit la réserve chaque nuit où la réserve '
               'extractible relative passe sous 0,5, en saison de végétation'))
    # mares
    t.append(L('*', 'profondeur_mare_defaut', 0.8, 'm', 0.5, 1.2, OPENNAT, 'valeur de secours', '', CC, 'convention',
               'C-W11', 'Profondeur maximale d\'une mare quand elle n\'est pas déclarée'))
    for fond, v, a, b in (('etanche', 0.0, 0.0, 0.2), ('argile', 0.3, 0.1, 1.0), ('naturel', 1.0, 0.5, 5.0)):
        t.append(L(f'fond_{fond}', 'infiltration', v, 'mm/jour', a, b, OPENNAT, 'valeur de secours', '', CC,
                   'convention', 'C-W11', f"Infiltration par le fond d'une mare ({fond}) ; une mare créée a par défaut un fond argileux"))
    t.append(L('*', 'coefficient_ruissellement', 0.9, 'fraction', 0.8, 1.0, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W11', 'Part de la pluie tombée sur une surface imperméable raccordée qui atteint '
               'la noue, la mare ou le jardin de pluie'))
    t.append(L('*', 'coefficient_ruissellement_permeable', 0.1, 'fraction', 0.05, 0.3, OPENNAT, 'valeur de secours',
               '', CC, 'convention', 'C-W11', 'Part de la pluie tombée sur un sol perméable raccordé (talus, prairie) '
               'qui atteint la mare ou la noue'))
    t.append(L('*', 'facteur_assec_precoce', 0.5, 'sans unité', 0.3, 0.8, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-W12', 'Une mare à sec entre mars et juin manque la reproduction des amphibiens de '
               'l\'année ; un assec de fin d\'été n\'est pas pénalisé'))
    return t


def eclairage():
    t = []
    azam = ('Azam C., Le Viol I., Bas Y., Zissis G., Vernet A., Julien J.-F., Kerbiriou C. (2018), Evidence for '
            'distance and illuminance thresholds in the effects of artificial lighting on bat activity, '
            'Landscape and Urban Planning 175')
    url_azam = 'https://doi.org/10.1016/j.landurbplan.2018.02.011'
    t.append(L('*', 'distance_effet_plein', 10, 'm', 0, 25, azam, 'résumé : effet d\'attraction limité à 10 m pour '
               'Pipistrellus et Nyctalus', url_azam, 'citation d\'un résultat publié', 'transposition', 'C-L3',
               'Distance au luminaire jusqu\'à laquelle l\'effet est entier'))
    t.append(L('*', 'distance_effet_nul', 50, 'm', 25, 100, azam, 'résumé : évitement jusqu\'à 25 m (Myotis) et '
               '50 m (Eptesicus serotinus) ; recommandation de 50 m entre luminaires et corridors', url_azam,
               'citation d\'un résultat publié', 'primaire', 'C-L3', 'Distance au-delà de laquelle l\'effet est nul '
               '(même distance que nuisances.csv)'))
    t.append(L('*', 'perte_maximale', 0.25, 'fraction', 0.15, 0.40, OPENNAT, 'calage sur le facteur L2 de '
               'nuisances.csv (0,75)', '', CC, 'convention', 'C-L1', 'Perte de valeur d\'une unité éclairée toute la '
               'nuit, en lumière froide, au pied du luminaire'))
    t.append(L('*', 'saison_chiropteres_debut', 4, 'mois', 3, 4, OPENNAT, 'valeur de secours', '', CC, 'convention',
               'C-L2', 'Premier mois de la saison d\'activité des chiroptères, hors hibernation'))
    t.append(L('*', 'saison_chiropteres_fin', 10, 'mois', 10, 11, OPENNAT, 'valeur de secours', '', CC, 'convention',
               'C-L2', 'Dernier mois de la saison d\'activité des chiroptères'))
    t.append(L('*', 'hauteur_soleil_nuit', 0, 'degré', -6, 0, 'ADEME, Météo-France, CSTB, DHUP, fichiers climatiques '
               'prospectifs (2025)', 'variable Hs (hauteur angulaire du soleil) de l\'année type', '',
               'Licence Ouverte 2.0', 'convention', 'C-L2', 'Une heure est de nuit quand le soleil est sous '
               'l\'horizon à la station de référence'))
    longcore = ('Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of '
                'light at night, Journal of Experimental Zoology A 329')
    arr = 'Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses'
    for nom, k, f, a, b in (('ambre', 1800, 0.5, 0.4, 0.7), ('k2200', 2200, 0.6, 0.5, 0.8),
                            ('k2400', 2400, 0.7, 0.6, 0.85), ('k2700', 2700, 0.8, 0.7, 0.9),
                            ('k3000', 3000, 0.9, 0.8, 1.0), ('k4000', 4000, 1.0, 1.0, 1.0)):
        t.append(L(nom, 'temperature_couleur', k, 'K', k, k, arr, 'articles 3 et 4 : plafonds de 3 000 K, 2 700 K et '
                   '2 400 K selon les sites', 'https://www.legifrance.gouv.fr/loda/id/JORFTEXT000037864346',
                   'texte réglementaire', 'primaire', 'C-L4', 'Points de la courbe du facteur spectral'))
        t.append(L(nom, 'facteur_spectral', f, 'sans unité', a, b, longcore, 'résumé : les sources riches en bleu '
                   '(2 200 K et plus) ont plus d\'effets que les LED ambre filtrées', 'https://doi.org/10.1002/jez.2184',
                   'citation d\'un résultat publié', 'convention', 'C-L4',
                   'Facteur croissant avec la température de couleur, 1 à 4 000 K ; échelonnement fixé par convention'))
    return t


def succession():
    t = []
    t.append(L('*', 'produit_k_d', 3.0, 'sans unité', 2.0, 4.0,
               'Richards F. J. (1959), A flexible growth function for empirical use, Journal of Experimental Botany 10',
               'fonction de croissance de Chapman-Richards', 'https://doi.org/10.1093/jxb/10.2.290',
               'citation d\'une méthode publiée', 'convention', 'C-M1',
               'Produit du taux de croissance et du délai de maturité : la courbe atteint 95 % de son asymptote au '
               'délai de la métrique anglaise, ramenée à 1 à ce délai'))
    for forme, c, a, b, j in (('herbacee', 1.0, 1.0, 1.5, 'courbe concave : une prairie semée donne vite l\'essentiel '
                               'de sa valeur'), ('arbustive', 2.0, 1.5, 2.5, 'courbe en S modérée'),
                              ('arboree', 3.0, 2.5, 4.0, 'courbe en S : un boisement planté vaut peu les premières '
                               'années')):
        t.append(L(forme, 'exposant_forme', c, 'sans unité', a, b,
                   'Pienaar L. V., Turnbull K. J. (1973), The Chapman-Richards generalization of Von Bertalanffy\'s '
                   'growth model, Forest Science 19', 'exposant de forme de la fonction de Chapman-Richards',
                   'https://doi.org/10.1093/forestscience/19.1.2', 'citation d\'une méthode publiée', 'convention',
                   'C-M1', f'Forme de maturation {forme} : {j}'))
    # gestion : couples BKompV exploité / abandonné (annexe 2)
    bk = 'BKompV, annexe 2 (Bundeskompensationsverordnung, 2020)'
    url_bk = 'https://www.gesetze-im-internet.de/bkompv/anlage_2.html'
    couples = [('34.02a', '34.02b', 21, 17, 'pelouse calcicole mi-sèche'), ('34.03.01a', '34.03.03', 22, 19, 'pelouse steppique'),
               ('34.04.03.01a', '34.04.03.03', 21, 16, 'pelouse sableuse'),
               ('34.06.01a', '34.06.01b', 21, 18, 'nardaie sèche à fraîche'), ('34.06.02a', '34.06.02b', 22, 19, 'nardaie humide'),
               ('34.07a.01', '34.07a.03', 20, 16, 'prairie fraîche riche'), ('34.07b.01', '34.07b.03', 15, 11, 'prairie fraîche moyenne'),
               ('35.02.01a', '35.02.01.03', 23, 20, 'prairie à molinie'), ('35.02.02a', '35.02.02.03', 23, 21, 'prairie alluviale'),
               ('35.02.03a.01', '35.02.03a.02', 20, 16, 'prairie humide extensive'), ('35.02.05.01', '35.02.05.01a', 18, 16, 'prairie inondable')]
    for a, b, va, vb, nom in couples:
        t.append(L(f'{a}>{b}', 'rapport_abandon', round(vb / va, 3), 'sans unité', round(vb / va, 3), round(vb / va, 3),
                   bk, f'{a} ({va}) exploité, {b} ({vb}) abandonné', url_bk, 'texte réglementaire (§ 5 UrhG)',
                   'primaire', 'C-M2', f'Rapport des valeurs de biotope abandonnée et exploitée : {nom}'))
    moy = sum(vb / va for _, _, va, vb, _ in couples) / len(couples)
    t.append(L('*', 'rapport_abandon_moyen', round(moy, 3), 'sans unité',
               round(min(vb / va for _, _, va, vb, _ in couples), 3), round(max(vb / va for _, _, va, vb, _ in couples), 3),
               bk, 'moyenne des onze couples ci-dessus', url_bk, 'texte réglementaire (§ 5 UrhG)', 'transposition',
               'C-M2', 'Rapport appliqué à un milieu herbacé dont la fauche ou le pâturage cesse'))
    t.append(L('*', 'delai_friche_herbacee', 2, 'an', 1, 3, OPENNAT, 'valeur de secours', '', CC, 'convention', 'C-M2',
               'Années sans fauche après lesquelles un milieu herbacé prend la valeur de sa variante abandonnée'))
    t.append(L('*', 'transition_fin_plan', 2, 'an', 1, 3, OPENNAT, 'valeur de secours', '', CC, 'convention', 'C-M3',
               "Années pendant lesquelles un milieu sorti de son plan de gestion perd progressivement sa valeur jusqu'à "
               "celle de la gestion courante (même durée que le délai d'abandon de C-M2)"))
    t.append(L('*', 'delai_embroussaillement', 15, 'an', 10, 30, OPENNAT, 'valeur de secours', '', CC, 'convention',
               'C-M2', 'Années sans gestion après lesquelles un milieu herbacé devient une friche arbustive (VB.9)'))
    t.append(L('*', 'score_friche_embroussaillee', 0.75, 'fraction', 0.65, 0.85, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-M2', "Score d'état de la friche arbustive issue de l'embroussaillement : milieu de "
               "la classe d'état moyen (C-H2)"))
    return t


def chantier():
    t = []
    bcae = ("Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités "
            "topographiques)")
    url_bcae = 'https://agriculture.gouv.fr/telecharger/135138'
    # sensibilité mensuelle : 1 période sensible entière, 0,5 mois en partie sensible
    cal = {
        'oiseaux': ([0, 0, 0.5, 1, 1, 1, 1, 0.5, 0, 0, 0, 0], bcae,
                    'interdiction de tailler haies et arbres du 16 mars au 15 août (nidification)', url_bcae,
                    'texte réglementaire', 'transposition', 'Destruction de haies, de fourrés, d\'arbres ou de '
                    'prairies hautes pendant la nidification'),
        'chiropteres': ([1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1], OPENNAT, 'valeur de secours : hibernation de novembre '
                        'à février, mise bas et élevage des jeunes de mai à août', '', CC, 'convention',
                        'Abattage d\'arbres à cavités ou démolition de bâtis à gîtes ; périodes favorables : mars, '
                        'avril, septembre, octobre'),
        'amphibiens': ([0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], OPENNAT, 'valeur de secours : reproduction et '
                       'développement larvaire de février à juin', '', CC, 'convention',
                       'Comblement ou vidange d\'une mare, d\'un fossé ou d\'une zone humide'),
    }
    for g, (mois, src, ref, url, lic, typ, just) in cal.items():
        for m, v in enumerate(mois, 1):
            t.append(L(g, f'sensibilite_m{m:02d}', v, 'fraction', v, v, src, ref, url, lic, typ, 'C-K1', just))
    t.append(L('*', 'perte_destruction_sensible', 1.0, 'an', 0.5, 2.0, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-K1', 'Une destruction en période sensible ajoute à Cnat la valeur initiale de '
               'l\'unité détruite pendant une année, pondérée par la sensibilité du mois'))
    for m, v in enumerate([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1], 1):
        t.append(L('plantation', f'mois_favorable_m{m:02d}', v, 'booléen', v, v, OPENNAT,
                   'valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars', '', CC,
                   'convention', 'C-K2', 'Mois où les plantations et les semis peuvent être faits'))
    t.append(L('*', 'avance_plantation', 2, 'mois', 0, 4, OPENNAT, 'valeur de secours', '', CC, 'convention', 'C-K2',
               'Les plantations peuvent commencer jusqu\'à deux mois avant la fin du chantier'))
    t.append(L('*', 'annee_debut_defaut', 2027, 'année', 2027, 2030, OPENNAT, 'valeur de secours', '', CC,
               'convention', 'C-K3', 'Année de début du chantier quand elle n\'est pas déclarée'))
    return t


def ecrire(nom, lignes):
    with open(os.path.join(RACINE, 'donnees', nom), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        for l in lignes:
            w.writerow({k: ('' if v == '' else str(v)) for k, v in l.items()})
    print(nom, len(lignes))


if __name__ == '__main__':
    ecrire('hydrique.csv', hydrique())
    ecrire('eclairage.csv', eclairage())
    ecrire('succession.csv', succession())
    ecrire('chantier.csv', chantier())
