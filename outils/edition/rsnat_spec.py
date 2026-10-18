# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Spécification du récapitulatif standardisé RSNat (nom provisoire).

Une seule description produit : le schéma XSD (`schemas/rsnat.xsd`), le dictionnaire des données de la
partie 7 de l'édition complète et un fichier d'exemple validé contre le schéma.

E(nom, description, enfants, min, max) : élément composé. F(nom, type, unité, description, min, max,
origine) : élément simple. Types : texte, entier, decimal, booleen, date, et les énumérations de ENUMS.
"""
from collections import namedtuple

E = namedtuple('E', 'nom description enfants min max')
F = namedtuple('F', 'nom type unite description min max origine')


def e(nom, description, enfants, mini=1, maxi=1):
    return E(nom, description, enfants, mini, maxi)


def f(nom, typ, unite, description, mini=1, maxi=1, origine=''):
    return F(nom, typ, unite, description, mini, maxi, origine)


ENUMS = {
    'zone': ['atlantique', 'continentale', 'mediterraneenne', 'alpine'],
    'typologie': ['logement', 'tertiaire', 'industrie', 'amenagement'],
    'position': ['sol_pleine_terre', 'sol_sur_dalle', 'hors_sol_toiture', 'hors_sol_facade', 'eau', 'arbre',
                 'lineaire'],
    'situation': ['reservoir', 'corridor', 'hors_trame'],
    'eclairage': ['L0', 'L1', 'L2'],
    'alimentation': ['naturelle', 'artificielle'],
    'statut': ['conservee', 'creee', 'amelioree'],
    'stade': ['J', 'M', 'A'],
    'classe_diametre': ['petit', 'moyen', 'grand', 'tres_grand'],
    'reponse': ['oui', 'non', 'sans_objet'],
    'connexion': ['forte', 'moyenne', 'faible'],
    'cloture': ['aucune', 'permeable', 'etanche'],
    'regime': ['plantation', 'coupe_rase', 'coupe_selective', 'faible_impact'],
    'phase': ['A1-A3', 'A4-A5', 'B', 'C', 'D'],
    'etat': ['initial', 'projet'],
    'classe_etat': ['bon', 'moyen', 'mauvais', 'sans_etat'],
    'zone_climatique': ['H1a', 'H1b', 'H1c', 'H2a', 'H2b', 'H2c', 'H2d', 'H3'],
    'texture': ['sable', 'sable_limoneux', 'limon_sableux', 'limon', 'limon_silteux', 'silt', 'limon_argilo_silteux',
                'argile_silteuse', 'argile'],
    'fond_mare': ['etanche', 'argile', 'naturel'],
    'regime_gestion': ['plan', 'courante', 'abandon'],
    'niveau_rechauffement': ['2_0', '2_7', '4_0'],
    'groupe_hydrique': ['gazon', 'prairie', 'xerophile', 'arbustif', 'arbore', 'conifere', 'toiture_extensive',
                        'humide_pluie', 'mare'],
}

CRITERE = e('Critere', 'Réponse à un critère de la grille d\'état du type', [
    f('code', 'texte', '', 'Code du critère dans la grille (A, B, A1, indicateur_bois_mort...)'),
    f('reponse', 'reponse', '', 'Réponse à un critère binaire', 0),
    f('note', 'entier', 'note 1 à 3', 'Note d\'un indicateur de la grille des boisements', 0),
    f('preuve', 'texte', '', 'Référence de la pièce qui justifie la réponse', 0),
], 0, 'unbounded')

UNITE = e('Unite', 'Unité d\'habitat', [
    f('identifiant', 'texte', '', 'Identifiant unique de l\'unité dans le projet'),
    f('identifiant_geometrique', 'texte', '', 'Identifiant de l\'objet géométrique correspondant (import futur)', 0),
    f('code_habitat', 'texte', '', 'Code de nomenclature_habitats.csv ou code EUNIS rattaché (fiche A04)'),
    f('position', 'position', '', 'Position de saisie (fiche A04)'),
    f('surface', 'decimal', 'm²', 'Surface ; houppier pour un arbre, longueur x largeur pour une haie (fiches A13 à A16)'),
    f('epaisseur_substrat', 'decimal', 'cm', 'Épaisseur de substrat, sur dalle ou hors-sol', 0),
    f('hauteur_facade', 'decimal', 'm', 'Hauteur végétalisée d\'une façade', 0),
    f('longueur', 'decimal', 'm', 'Longueur d\'une haie ou d\'une façade', 0),
    f('largeur', 'decimal', 'm', 'Largeur d\'une haie', 0),
    f('nombre_arbres', 'entier', '', 'Nombre d\'arbres d\'une unité arbre', 0),
    f('classe_diametre', 'classe_diametre', '', 'Classe de diamètre des arbres', 0),
    f('stade', 'stade', '', 'Stade d\'un type ligneux', 0),
    f('situation', 'situation', '', 'Situation dans la trame verte et bleue (fiche A02)', 0),
    f('tache', 'texte', '', 'Identifiant de tache (fiche A17)', 0),
    f('eclairage', 'eclairage', '', 'Raccourci d\'éclairage L0, L1 ou L2 (fiche A53-2)', 0),
    e('Eclairage_Horaire', 'Éclairage déclaré heure par heure (fiches A51 à A53)', [
        f('extinction', 'entier', 'heure légale', 'Heure d\'extinction, absente si allumé toute la nuit', 0),
        f('rallumage', 'entier', 'heure légale', 'Heure de rallumage du matin', 0),
        f('temperature_couleur', 'decimal', 'K', 'Température de couleur'),
        f('part_detection', 'decimal', '', 'Part de temps allumé sous détection de présence', 0),
    ], 0),
    f('distance_lumiere', 'decimal', 'm', 'Distance au point lumineux le plus proche', 0),
    f('arrose', 'booleen', '', 'Arrosage automatique (fiche A49)', 0),
    f('texture_sol', 'texture', '', 'Texture du sol de l\'unité, si elle diffère de celle du site (fiche A48)', 0),
    f('profondeur_sol', 'decimal', 'm', 'Profondeur de sol de l\'unité (fiche A48)', 0),
    f('bassin_versant_impermeable', 'decimal', 'm²', 'Surface imperméable raccordée (fiche A49)', 0),
    f('bassin_versant_permeable', 'decimal', 'm²', 'Surface perméable raccordée (fiche A49)', 0),
    f('profondeur_mare', 'decimal', 'm', 'Profondeur maximale d\'une mare (fiche A49)', 0),
    f('fond_mare', 'fond_mare', '', 'Nature du fond d\'une mare (fiche A49)', 0),
    f('gites', 'booleen', '', 'Gîtes de chiroptères (fiche A57)', 0),
    f('regime_gestion', 'regime_gestion', '', 'Régime imposé dès la livraison (fiche A55)', 0),
    f('regime_apres_plan', 'regime_gestion', '', 'Régime après le plan de gestion (fiche A55)', 0),
    f('plan_gestion_annees', 'entier', 'an', 'Durée du plan de gestion propre à l\'unité (fiche A55)', 0),
    f('niveau_sonore', 'decimal', 'dB(A)', 'Niveau sonore à l\'unité (fiche A21)', 0),
    f('exposition_vitrage', 'booleen', '', 'À moins de 15 m d\'une façade vitrée non traitée de plus de 10 m² (fiche A22)', 0),
    f('alimentation_eau', 'alimentation', '', 'Alimentation d\'une unité en eau (fiche A23)', 0),
    f('statut', 'statut', '', 'Statut à l\'état projet (fiches A27 à A29)', 0),
    f('unite_liee', 'texte', '', 'Identifiant de l\'unité initiale liée, pour une unité conservée ou améliorée', 0),
    f('protection_chantier', 'booleen', '', 'Protection prévue pendant le chantier (fiche A27)', 0),
    e('Critere_Collection', 'Réponses à la grille d\'état', [CRITERE], 0),
    e('Renouvellement_Collection', 'Années de réfection (fiche A30)', [
        f('annee', 'entier', 'an', 'Année de réfection, de 2 à 50', 0, 'unbounded')], 0),
], 0, 'unbounded')

ENTREE = e('Entree_Projet', 'Données d\'entrée (partie 1, chapitre 4)', [
    e('Projet', 'Identification et contexte', [
        f('identifiant', 'texte', '', 'Identifiant du projet'),
        f('nom', 'texte', '', 'Nom de l\'opération'),
        f('adresse', 'texte', '', 'Adresse', 0, 1, 'RSEE : adresse'),
        f('commune_insee', 'texte', '', 'Code INSEE de la commune', 0, 1, 'RSEE : Datas_Comp'),
        f('latitude', 'decimal', '°', 'Latitude WGS 84', 0, 1, 'RSEE : latitude'),
        f('longitude', 'decimal', '°', 'Longitude WGS 84', 0, 1, 'RSEE : longitude'),
        f('zone_biogeographique', 'zone', '', 'Zone biogéographique (fiche A02)'),
        f('departement', 'texte', '', 'Département du site', 0, 1, 'RSET : Simu/Departement'),
        f('altitude', 'decimal', 'm', 'Altitude du site (fiche A43)', 0, 1, 'RSET : Simu/Altitude'),
        f('zone_climatique', 'zone_climatique', '', 'Zone climatique RE2020 (fiche A43)'),
        f('texture_sol', 'texture', '', 'Texture du sol du site (fiche A48)', 0),
        f('profondeur_sol', 'decimal', 'm', 'Profondeur de sol du site (fiche A48)', 0),
        f('annee_debut_chantier', 'entier', '', 'Année de début du chantier (fiche A58)'),
        f('mois_debut_chantier', 'entier', '', 'Mois de début du chantier, 1 à 12 (fiche A58)'),
        f('mois_destruction', 'entier', '', 'Mois des défrichements, abattages et comblements (fiche A57)', 0),
        f('plan_gestion_annees', 'entier', 'an', 'Durée du plan de gestion écologique (fiche A55)', 0),
        f('typologie', 'typologie', '', 'Typologie de l\'opération'),
        f('rsee_empreinte', 'texte', '', 'Empreinte SHA-256 du RSEE repris, s\'il y en a un', 0),
        f('date_etude', 'date', '', 'Date de l\'étude'),
    ]),
    e('Parcelle', 'Parcelle ou unité foncière', [
        f('surface', 'decimal', 'm²', 'Surface de la parcelle S_p', 1, 1, 'RSEE : parcelle/surface_parcelle'),
        f('surface_vegetalisee_rsee', 'decimal', 'm²', 'Surface végétalisée déclarée au RSEE (contrôle)', 0, 1,
          'RSEE : parcelle/surface_veg'),
        f('surface_impermeable_rsee', 'decimal', 'm²', 'Surface imperméabilisée déclarée au RSEE (contrôle)', 0, 1,
          'RSEE : parcelle/surface_imper'),
        f('cbs_plu', 'decimal', '', 'Coefficient de biotope imposé par le PLU', 0),
        f('pleine_terre_plu', 'decimal', '', 'Part de pleine terre imposée par le PLU', 0),
    ]),
    e('Batiment_Collection', 'Bâtiments de l\'opération', [
        e('Batiment', 'Bâtiment', [
            f('index', 'entier', '', 'Index du bâtiment', 1, 1, 'RSEE : batiment/index'),
            f('nom', 'texte', '', 'Nom', 0, 1, 'RSEE : batiment/nom'),
            f('sref', 'decimal', 'm²', 'Surface de référence', 1, 1, 'RSEE : batiment/sref'),
            f('emprise_au_sol', 'decimal', 'm²', 'Emprise au sol', 1, 1, 'RSEE : batiment/emprise_au_sol'),
            f('duree_chantier', 'decimal', 'mois', 'Durée du chantier', 1, 1, 'RSEE : batiment/duree_chantier'),
            e('Ges_Collection', 'Émissions des contributeurs composants et chantier (indicateur 101)', [
                e('Ges', 'Émission d\'une phase', [
                    f('phase', 'phase', '', 'Phase du cycle de vie'),
                    f('valeur', 'decimal', 'kg CO2 éq./m² Sref', 'Valeur de l\'indicateur 101', 1, 1,
                      'RSEE : sortie_projet/batiment/contributeur/{composant, chantier}/indicateurs_acv_collection'),
                ], 1, 'unbounded')]),
            e('Pollution_Collection', 'Indicateurs 106 à 109 et 116', [
                e('Pollution', 'Indicateur de pollution d\'une phase', [
                    f('code', 'entier', '', 'Code de l\'indicateur (106, 107, 108, 109, 116)'),
                    f('phase', 'phase', '', 'Phase'),
                    f('valeur', 'decimal', 'unité de l\'annexe II par m² Sref', 'Valeur'),
                ], 0, 'unbounded')], 0),
        ], 0, 'unbounded')], 0),
    e('Tache_Collection', 'Taches d\'habitat et leur contexte (fiches A17 à A19)', [
        e('Tache', 'Tache', [
            f('identifiant', 'texte', '', 'Identifiant de tache'),
            f('surface_exterieure', 'decimal', 'm²', 'Surface végétalisée extérieure contiguë', 0),
            f('connexion', 'connexion', '', 'Connexion déclarée', 0),
            f('distance_espace_naturel', 'decimal', 'm', 'Distance bord à bord à l\'espace naturel le plus proche', 0),
            f('surface_espace_naturel', 'decimal', 'm²', 'Surface de cet espace', 0),
            f('cloture', 'cloture', '', 'Clôture de la tache', 0),
        ], 0, 'unbounded')], 0),
    e('Etat_Initial', 'État initial du site', [e('Unite_Collection', 'Unités', [UNITE])]),
    e('Variante_Collection', 'Variantes de l\'état projet (fiche A41)', [
        e('Variante', 'Variante', [
            f('index', 'entier', '', 'Index de la variante'),
            f('nom', 'texte', '', 'Nom'),
            f('reference', 'booleen', '', 'Variante de référence'),
            e('Unite_Collection', 'Unités de l\'état projet', [UNITE]),
            e('Bois_Collection', 'Bois mis en œuvre (fiche A34)', [
                e('Bois', 'Lot de bois', [
                    f('regime', 'regime', '', 'Régime forestier déclaré'),
                    f('volume', 'decimal', 'm³', 'Volume mis en œuvre'),
                    f('remplacements', 'entier', '', 'Nombre de remplacements en 50 ans', 0),
                    f('justification', 'texte', '', 'Pièce qui justifie le régime', 0),
                ], 0, 'unbounded')], 0),
            e('Granulats', 'Granulats, sables et roches (fiche A35)', [
                f('masse', 'decimal', 't', 'Masse mise en œuvre'),
                f('remplacements', 'entier', '', 'Nombre de remplacements en 50 ans', 0),
            ], 0),
            e('Ouvrage_Pluvial_Collection', 'Ouvrages de gestion des eaux pluviales (fiche A24)', [
                e('Ouvrage_Pluvial', 'Ouvrage', [
                    f('surface_drainee', 'decimal', 'm²', 'Surface imperméable conduite vers l\'ouvrage'),
                    f('infiltration_surface', 'booleen', '', 'Infiltration en surface'),
                ], 0, 'unbounded')], 0),
            e('Facade_Vitree_Collection', 'Façades vitrées exposées (fiche A22)', [
                e('Facade_Vitree', 'Façade', [
                    f('surface', 'decimal', 'm²', 'Surface vitrée exposée'),
                    f('traitee', 'booleen', '', 'Vitrage traité contre les collisions'),
                ], 0, 'unbounded')], 0),
        ], 1, 'unbounded')]),
])

INDIC = [
    f('cnat', 'decimal', 'm²HE·an', 'Consommation de nature sur 50 ans (fiche A37)'),
    f('cnat_moyen', 'decimal', 'm²HE', 'Consommation moyenne annuelle'),
    f('cnat_relatif', 'decimal', '', 'Cnat / I_0', 0),
    f('cnat_30', 'decimal', 'm²HE·an', 'Consommation sur 30 ans'),
    f('inat', 'decimal', 'm²HE·an', 'Biodiversité grise'),
    f('snat', 'decimal', 'm²HE·an', 'Solde de nature'),
    f('bnat', 'decimal', 'points', 'Besoin de nature de la conception (fiche A38)'),
    f('cbs', 'decimal', '', 'Coefficient de biotope équivalent'),
    f('cnat_par_m2_parcelle', 'decimal', 'm²HE·an/m²', 'Cnat / S_p'),
    f('inat_par_m2_sref', 'decimal', 'm²HE·an/m²', 'Inat / S_ref', 0),
]

SORTIE = e('Sortie_Projet', 'Résultats (partie 1, chapitre 11)', [
    e('Variante_Resultat', 'Résultats d\'une variante', [
        f('index', 'entier', '', 'Index de la variante'),
        e('Contexte', 'Sorties de l\'étape E1 (fiche A02)', [
            f('part_emprise', 'decimal', '', 'Part d\'emprise du bâti e'),
            f('bnat_min', 'decimal', 'points', 'Seuil de Bnat applicable', 0),
            f('pleine_terre_min', 'decimal', '', 'Seuil de pleine terre applicable'),
            f('multiplicateur_delai', 'decimal', '', 'Multiplicateur de délai de la zone'),
        ]),
        e('Fermeture_Collection', 'Contrôle de fermeture (fiche A03)', [
            e('Fermeture', 'Contrôle d\'un état', [
                f('etat', 'etat', '', 'État'), f('somme', 'decimal', 'm²', 'Somme des surfaces au sol'),
                f('ecart', 'decimal', 'm²', 'Écart avec S_p'), f('conforme', 'booleen', '', 'Contrôle satisfait'),
            ], 2, 2)]),
        e('Unite_Resultat_Collection', 'Résultats par unité', [
            e('Unite_Resultat', 'Résultats d\'une unité', [
                f('identifiant', 'texte', '', 'Identifiant de l\'unité'), f('etat', 'etat', '', 'État'),
                f('type', 'texte', '', 'Type OpenNAT retenu h_u'), f('nature_surface', 'texte', '', 'Nature S01 à S12', 0),
                f('coefficient_sol', 'decimal', '', 'c_u', 0), f('facteur_support', 'decimal', '', 'f_sol,u'),
                f('valeur_intrinseque', 'decimal', 'm²HE/m²', 'v_u'), f('score_etat', 'decimal', '', 'S_u', 0),
                f('facteur_etat', 'decimal', '', 'f_u'), f('classe_etat', 'classe_etat', '', 'cl_u'),
                f('multiplicateur_situation', 'decimal', '', 'm_u'), f('facteur_taille', 'decimal', '', 'k_taille', 0),
                f('facteur_connectivite', 'decimal', '', 'k_C,u'), f('facteur_eclairage', 'decimal', '', 'k_lum,u', 0),
                f('fraction_nuit_eclairee', 'decimal', '', 'x_nuit,u', 0), f('facteur_nuisances', 'decimal', '', 'k_N,u'),
                f('facteur_eau', 'decimal', '', 'k_E,u'), f('valeur_habitat', 'decimal', 'm²HE', 'V^H_u'),
                f('valeur_maturite', 'decimal', 'm²HE', 'V_u'), f('delai', 'decimal', 'an', 'd_u', 0),
                f('difficulte', 'decimal', '', 'D_u', 0),
                f('groupe_hydrique', 'groupe_hydrique', '', 'g_u (fiche A47)', 0),
                f('reserve_utile', 'decimal', 'mm', 'RU_u (fiche A48)', 0),
                e('Bilan_Hydrique', 'Bilan d\'un niveau de réchauffement (fiches A49, A50)', [
                    f('niveau', 'niveau_rechauffement', '', 'Année type'),
                    f('indice_stress', 'decimal', 'jours-équivalents', 'IS_u,n'),
                    f('indice_stress_reference', 'decimal', 'jours-équivalents', 'IS_ref,g'),
                    f('facteur_hydrique', 'decimal', '', 'k_W,u,n'),
                    f('arrosage', 'decimal', 'mm', 'Volume d\'arrosage annuel', 0),
                    f('assec_printemps', 'booleen', '', 'Mare à sec entre mars et juin', 0),
                ], 0, 3),
                f('mois_depart_maturation', 'entier', '', 'Rang du mois de départ (fiche A58)', 0),
                f('facteurs_hydriques', 'texte', '', '50 valeurs annuelles k_W,u(t)', 0),
                f('facteurs_gestion', 'texte', '', '50 valeurs annuelles f_g,u(t)', 0),
                f('trajectoire', 'texte', 'm²HE', '50 valeurs annuelles V_u(t) séparées par des espaces', 0),
                f('valeur_integree', 'decimal', 'm²HE·an', 'Somme de la trajectoire', 0),
            ], 0, 'unbounded')]),
        e('Site', 'Sorties des modules S et T (fiches A08, A24, A31)', [
            f('valeur_initiale', 'decimal', 'm²HE', 'V_0'), f('i0', 'decimal', 'm²HE·an', 'I_0'),
            f('i1', 'decimal', 'm²HE·an', 'I_1'), f('i0_30', 'decimal', 'm²HE·an', 'I_0,30'),
            f('i1_30', 'decimal', 'm²HE·an', 'I_1,30'), f('dette_maturite', 'decimal', 'm²HE·an', 'DM'),
            f('supplement_destruction', 'decimal', 'm²HE·an', 'ΔI_ch (fiche A57)'),
            f('arrosage_annuel', 'decimal', 'm³', 'Volume d\'arrosage annuel moyen de la période (fiche A49)'),
            f('rang_plantation', 'entier', '', 'm_pl (fiche A58)', 0),
            f('annees_periode', 'texte', '', 'Première et dernière années civiles de la période (fiche A46)', 0),
            f('trajectoire_reference', 'texte', 'm²HE', '50 valeurs annuelles de l\'état initial sous le même climat', 0),
            f('trajectoire_site', 'texte', 'm²HE', '50 valeurs annuelles V_1(t)'),
            f('pleine_terre', 'decimal', '', 'PT'), f('pleine_terre_initiale', 'decimal', '', 'PT_0'),
            f('impermeable_initial', 'decimal', 'm²', 'A_imp,0'), f('impermeable_projet', 'decimal', 'm²', 'A_imp,1'),
            f('impermeabilisation_nette', 'decimal', 'm²', 'ΔA_imp'),
            f('part_pluvial_infiltre', 'decimal', '', 'P_inf', 0),
            f('surface_vitree_non_traitee', 'decimal', 'm²', 'A_vit,nt', 0),
        ]),
        e('Materiaux', 'Sorties du module G (fiches A32 à A36)', [
            f('facteur_climat', 'decimal', 'm²HE/kg CO2 éq./an', 'CF'),
            f('inat_climat', 'decimal', 'm²HE·an', 'Inat_clim'),
            e('Inat_Climat_Phase', 'Inat_clim par phase', [
                f('phase', 'phase', '', 'Phase'), f('valeur', 'decimal', 'm²HE·an', 'Inat_clim,p')], 0, 5),
            f('inat_bois', 'decimal', 'm²HE·an', 'Inat_bois'), f('inat_carrieres', 'decimal', 'm²HE·an', 'Inat_carr'),
            e('Pollution_Resultat', 'Indicateurs de pollution', [
                f('code', 'entier', '', 'Code'), f('valeur', 'decimal', 'unité de l\'annexe II', 'POL_i')],
              0, 'unbounded'),
        ]),
        e('Indicateurs', 'Indicateurs de l\'opération (fiches A37, A38)', INDIC),
        e('Incertitude', 'Analyse d\'incertitude (fiche A39)', [
            f('tirages', 'entier', '', 'Nombre de tirages'),
            e('Intervalle', 'Intervalle d\'un indicateur', [
                f('indicateur', 'texte', '', 'Nom de l\'indicateur'), f('p5', 'decimal', '', 'Centile 5'),
                f('p50', 'decimal', '', 'Centile 50'), f('p95', 'decimal', '', 'Centile 95')], 0, 'unbounded'),
            e('Parametre_Influent', 'Paramètre parmi les cinq plus influents', [
                f('rang', 'entier', '', 'Rang'), f('table', 'texte', '', 'Table de donnees/'),
                f('cle', 'texte', '', 'Clé'), f('parametre', 'texte', '', 'Paramètre'),
                f('correlation', 'decimal', '', 'ρ de Spearman avec Snat')], 0, 5),
        ], 0),
        e('Conformite', 'Conformité (fiche A40)', [
            f('bnat_conforme', 'booleen', '', 'conf_Bnat', 0), f('pleine_terre_conforme', 'booleen', '', 'conf_PT'),
            f('plu_conforme', 'booleen', '', 'conf_PLU', 0), f('niveau_cnat', 'entier', '', 'Niveau 0, 1 ou 2'),
        ]),
    ], 1, 'unbounded'),
])

ATTESTATION_PERMIS = e('Attestation_Permis', 'Attestation de prise en compte de la biodiversité au dépôt du permis '
                       'de construire (fiche A40, convention C-P1)', [
    f('variante', 'entier', '', 'Index de la variante attestée'),
    f('bnat', 'decimal', 'points', 'Bnat'), f('bnat_min', 'decimal', 'points', 'Seuil de Bnat', 0),
    f('pleine_terre', 'decimal', '', 'Taux de pleine terre'), f('pleine_terre_min', 'decimal', '', 'Seuil'),
    f('cbs_plu', 'decimal', '', 'Coefficient de biotope du PLU', 0),
    f('pleine_terre_plu', 'decimal', '', 'Pleine terre du PLU', 0),
    f('conforme', 'booleen', '', 'Conclusion de conformité'),
    f('mention', 'texte', '', 'Mention, notamment l\'écart au minimum du PLU', 0),
])

ATTESTATION_ACHEVEMENT = e('Attestation_Achevement', 'Attestation à l\'achèvement (fiche A40)', [
    f('variante', 'entier', '', 'Index de la variante réalisée'),
    *INDIC,
    f('niveau_cnat', 'entier', '', 'Niveau atteint'),
], 0)

RACINE = e('RSNat', 'Récapitulatif standardisé de l\'étude nature OpenNAT', [
    f('version_methode', 'texte', '', 'Version de la méthode (OpenNAT 1)'),
    f('version_donnees', 'texte', '', 'Empreinte SHA-256 des tables de donnees/'),
    f('graine', 'entier', '', 'Graine du générateur aléatoire'),
    f('date_calcul', 'date', '', 'Date du calcul'),
    ENTREE, SORTIE, ATTESTATION_PERMIS, ATTESTATION_ACHEVEMENT,
    e('Empreinte', 'Empreintes de contrôle (fiche A42)', [
        f('entrees', 'texte', '', 'SHA-256 de Entree_Projet'), f('sorties', 'texte', '', 'SHA-256 de Sortie_Projet')]),
])
