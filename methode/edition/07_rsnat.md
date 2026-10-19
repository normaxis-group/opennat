## Partie 7. Récapitulatif standardisé RSNat et fichier projet

Le RSNat (nom provisoire) est au calcul OpenNAT ce que le RSEE est à l'étude RE2020 : un fichier XML qui porte les données d'entrée, les résultats et les attestations, validé par un schéma XSD publié avec la méthode, accompagné de sa copie JSON validée par un schéma JSON. Sa structure reprend celle du RSEE : un bloc d'entrée, un bloc de sortie, et ici deux blocs d'attestation. Le moteur l'écrit à chaque calcul et le valide contre ses deux schémas (exigence E9).

### 7.1 Fichiers

| Fichier | Contenu |
|---|---|
| `schemas/rsnat.xsd` | Schéma XSD, 322 éléments, 23 énumérations |
| `schemas/rsnat.schema.json` | Schéma JSON du même RSNat |
| `schemas/projet.schema.json` | Schéma du fichier projet, entrée du moteur (section 7.6) |
| `schemas/exemple_annexe_C.rsnat.xml` et `.json` | RSNat de l'exemple de l'annexe C de la partie 1, écrit par le moteur et validé contre les deux schémas |
| `opennat/rsnat_spec.py` | Spécification unique dont dérivent les deux schémas, ce dictionnaire et la sortie du moteur |

### 7.2 Règles d'écriture

- Encodage UTF-8, séparateur décimal point, dates au format AAAA-MM-JJ.
- Les éléments sont écrits dans l'ordre du schéma. Un élément facultatif sans valeur est omis.
- Les valeurs sont celles du calcul aux valeurs centrales, avec la précision de la fiche A01 : une décimale pour les valeurs en m²HE, m²HE·an, m², m³, mm et points, quatre pour les facteurs ; les intervalles sont dans le bloc Incertitude.
- Le bloc Attestation_Permis est le seul extrait déposé sur la plateforme d'IRICE au dépôt du permis de construire ; il se lit sans le reste du fichier.
- Le RSNat porte l'empreinte SHA-256 de son bloc d'entrée et de son bloc de sortie (forme canonique XML) : la plateforme recalcule l'empreinte pour vérifier qu'aucune valeur n'a été modifiée après le calcul.

### 7.3 Dictionnaire des données

Un tableau par élément composé, dans l'ordre du schéma. Cardinalité : 0..1 facultatif, 1..1 obligatoire, 0..n ou 1..n répété. La colonne « Origine » donne l'élément du RSEE dont la donnée se reprend quand il existe.

#### 7.3.1 `RSNat`

Récapitulatif standardisé de l'étude nature OpenNAT.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| version_methode | texte |  | 1..1 | Version de la méthode (OpenNAT 1) |  |
| version_donnees | texte |  | 1..1 | Empreinte SHA-256 des tables de donnees/ |  |
| graine | entier |  | 1..1 | Graine du générateur aléatoire |  |
| date_calcul | date |  | 1..1 | Date du calcul |  |
| Entree_Projet | élément composé |  | 1..1 | Données d'entrée (partie 1, chapitre 4) |  |
| Sortie_Projet | élément composé |  | 1..1 | Résultats (partie 1, chapitre 11) |  |
| Attestation_Permis | élément composé |  | 1..1 | Attestation de prise en compte de la biodiversité au dépôt du permis de construire (fiche A40, convention C-P1) |  |
| Attestation_Achevement | élément composé |  | 0..1 | Attestation à l'achèvement (fiche A40) |  |
| Empreinte | élément composé |  | 1..1 | Empreintes de contrôle (fiche A42) |  |

#### 7.3.2 `RSNat/Entree_Projet`

Données d'entrée (partie 1, chapitre 4).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Projet | élément composé |  | 1..1 | Identification et contexte |  |
| Parcelle | élément composé |  | 1..1 | Parcelle ou unité foncière |  |
| Batiment_Collection | élément composé |  | 0..1 | Bâtiments de l'opération |  |
| Tache_Collection | élément composé |  | 0..1 | Taches d'habitat et leur contexte (fiches A17 à A19) |  |
| Etat_Initial | élément composé |  | 1..1 | État initial du site |  |
| Variante_Collection | élément composé |  | 1..1 | Variantes de l'état projet (fiche A41) |  |

#### 7.3.3 `RSNat/Entree_Projet/Projet`

Identification et contexte.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| identifiant | texte |  | 1..1 | Identifiant du projet |  |
| nom | texte |  | 1..1 | Nom de l'opération |  |
| adresse | texte |  | 0..1 | Adresse | RSEE : adresse |
| commune_insee | texte |  | 0..1 | Code INSEE de la commune | RSEE : Datas_Comp |
| latitude | nombre décimal | ° | 0..1 | Latitude WGS 84 | RSEE : latitude |
| longitude | nombre décimal | ° | 0..1 | Longitude WGS 84 | RSEE : longitude |
| zone_biogeographique | énumération : atlantique, continentale, mediterraneenne, alpine |  | 1..1 | Zone biogéographique (fiche A02) |  |
| departement | texte |  | 0..1 | Département du site | RSET : Simu/Departement |
| altitude | nombre décimal | m | 0..1 | Altitude du site (fiche A43) | RSET : Simu/Altitude |
| zone_climatique | énumération : H1a, H1b, H1c, H2a, H2b, H2c, H2d, H3 |  | 1..1 | Zone climatique RE2020 (fiche A43) |  |
| texture_sol | énumération : sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |  | 0..1 | Texture du sol du site (fiche A48) |  |
| profondeur_sol | nombre décimal | m | 0..1 | Profondeur de sol du site (fiche A48) |  |
| annee_debut_chantier | entier |  | 1..1 | Année de début du chantier (fiche A58) |  |
| mois_debut_chantier | entier |  | 1..1 | Mois de début du chantier, 1 à 12 (fiche A58) |  |
| mois_destruction | entier |  | 0..1 | Mois des défrichements, abattages et comblements (fiche A57) |  |
| plan_gestion_annees | entier | an | 0..1 | Durée du plan de gestion écologique (fiche A55) |  |
| typologie | énumération : logement, tertiaire, industrie, amenagement |  | 1..1 | Typologie de l'opération |  |
| rsee_empreinte | texte |  | 0..1 | Empreinte SHA-256 du RSEE repris, s'il y en a un |  |
| date_etude | date |  | 1..1 | Date de l'étude |  |

#### 7.3.4 `RSNat/Entree_Projet/Parcelle`

Parcelle ou unité foncière.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| surface | nombre décimal | m² | 1..1 | Surface de la parcelle S_p | RSEE : parcelle/surface_parcelle |
| surface_vegetalisee_rsee | nombre décimal | m² | 0..1 | Surface végétalisée déclarée au RSEE (contrôle) | RSEE : parcelle/surface_veg |
| surface_impermeable_rsee | nombre décimal | m² | 0..1 | Surface imperméabilisée déclarée au RSEE (contrôle) | RSEE : parcelle/surface_imper |
| cbs_plu | nombre décimal |  | 0..1 | Coefficient de biotope imposé par le PLU |  |
| pleine_terre_plu | nombre décimal |  | 0..1 | Part de pleine terre imposée par le PLU |  |

#### 7.3.5 `RSNat/Entree_Projet/Batiment_Collection`

Bâtiments de l'opération.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Batiment | élément composé |  | 0..n | Bâtiment |  |

#### 7.3.6 `RSNat/Entree_Projet/Batiment_Collection/Batiment`

Bâtiment.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| index | entier |  | 1..1 | Index du bâtiment | RSEE : batiment/index |
| nom | texte |  | 0..1 | Nom | RSEE : batiment/nom |
| sref | nombre décimal | m² | 1..1 | Surface de référence | RSEE : batiment/sref |
| emprise_au_sol | nombre décimal | m² | 1..1 | Emprise au sol | RSEE : batiment/emprise_au_sol |
| duree_chantier | nombre décimal | mois | 1..1 | Durée du chantier | RSEE : batiment/duree_chantier |
| Ges_Collection | élément composé |  | 1..1 | Émissions des contributeurs composants et chantier (indicateur 101) |  |
| Pollution_Collection | élément composé |  | 0..1 | Indicateurs 106 à 109 et 116 |  |

#### 7.3.7 `RSNat/Entree_Projet/Batiment_Collection/Batiment/Ges_Collection`

Émissions des contributeurs composants et chantier (indicateur 101).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Ges | élément composé |  | 1..n | Émission d'une phase |  |

#### 7.3.8 `RSNat/Entree_Projet/Batiment_Collection/Batiment/Ges_Collection/Ges`

Émission d'une phase.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| phase | énumération : A1-A3, A4-A5, B, C, D |  | 1..1 | Phase du cycle de vie |  |
| valeur | nombre décimal | kg CO2 éq./m² Sref | 1..1 | Valeur de l'indicateur 101 | RSEE : sortie_projet/batiment/contributeur/{composant, chantier}/indicateurs_acv_collection |

#### 7.3.9 `RSNat/Entree_Projet/Batiment_Collection/Batiment/Pollution_Collection`

Indicateurs 106 à 109 et 116.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Pollution | élément composé |  | 0..n | Indicateur de pollution d'une phase |  |

#### 7.3.10 `RSNat/Entree_Projet/Batiment_Collection/Batiment/Pollution_Collection/Pollution`

Indicateur de pollution d'une phase.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| code | entier |  | 1..1 | Code de l'indicateur (106, 107, 108, 109, 116) |  |
| phase | énumération : A1-A3, A4-A5, B, C, D |  | 1..1 | Phase |  |
| valeur | nombre décimal | unité de l'annexe II par m² Sref | 1..1 | Valeur |  |

#### 7.3.11 `RSNat/Entree_Projet/Tache_Collection`

Taches d'habitat et leur contexte (fiches A17 à A19).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Tache | élément composé |  | 0..n | Tache |  |

#### 7.3.12 `RSNat/Entree_Projet/Tache_Collection/Tache`

Tache.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| identifiant | texte |  | 1..1 | Identifiant de tache |  |
| surface_exterieure | nombre décimal | m² | 0..1 | Surface végétalisée extérieure contiguë |  |
| connexion | énumération : forte, moyenne, faible |  | 0..1 | Connexion déclarée |  |
| distance_espace_naturel | nombre décimal | m | 0..1 | Distance bord à bord à l'espace naturel le plus proche |  |
| surface_espace_naturel | nombre décimal | m² | 0..1 | Surface de cet espace |  |
| cloture | énumération : aucune, permeable, etanche |  | 0..1 | Clôture de la tache |  |

#### 7.3.13 `RSNat/Entree_Projet/Etat_Initial`

État initial du site.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Unite_Collection | élément composé |  | 1..1 | Unités |  |

#### 7.3.14 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection`

Unités.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Unite | élément composé |  | 0..n | Unité d'habitat |  |

#### 7.3.15 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite`

Unité d'habitat.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| identifiant | texte |  | 1..1 | Identifiant unique de l'unité dans le projet |  |
| identifiant_geometrique | texte |  | 0..1 | Identifiant de l'objet géométrique correspondant (import futur) |  |
| code_habitat | texte |  | 1..1 | Code de nomenclature_habitats.csv ou code EUNIS rattaché (fiche A04) |  |
| position | énumération : sol_pleine_terre, sol_sur_dalle, hors_sol_toiture, hors_sol_facade, eau, arbre, lineaire |  | 1..1 | Position de saisie (fiche A04) |  |
| surface | nombre décimal | m² | 1..1 | Surface ; houppier pour un arbre, longueur x largeur pour une haie (fiches A13 à A16) |  |
| epaisseur_substrat | nombre décimal | cm | 0..1 | Épaisseur de substrat, sur dalle ou hors-sol |  |
| hauteur_facade | nombre décimal | m | 0..1 | Hauteur végétalisée d'une façade |  |
| longueur | nombre décimal | m | 0..1 | Longueur d'une haie ou d'une façade |  |
| largeur | nombre décimal | m | 0..1 | Largeur d'une haie |  |
| nombre_arbres | entier |  | 0..1 | Nombre d'arbres d'une unité arbre |  |
| classe_diametre | énumération : petit, moyen, grand, tres_grand |  | 0..1 | Classe de diamètre des arbres |  |
| stade | énumération : J, M, A |  | 0..1 | Stade d'un type ligneux |  |
| situation | énumération : reservoir, corridor, hors_trame |  | 0..1 | Situation dans la trame verte et bleue (fiche A02) |  |
| tache | texte |  | 0..1 | Identifiant de tache (fiche A17) |  |
| eclairage | énumération : L0, L1, L2 |  | 0..1 | Raccourci d'éclairage L0, L1 ou L2 (fiche A53-2) |  |
| Eclairage_Horaire | élément composé |  | 0..1 | Éclairage déclaré heure par heure (fiches A51 à A53) |  |
| distance_lumiere | nombre décimal | m | 0..1 | Distance au point lumineux le plus proche |  |
| arrose | booléen |  | 0..1 | Arrosage automatique (fiche A49) |  |
| texture_sol | énumération : sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |  | 0..1 | Texture du sol de l'unité, si elle diffère de celle du site (fiche A48) |  |
| profondeur_sol | nombre décimal | m | 0..1 | Profondeur de sol de l'unité (fiche A48) |  |
| bassin_versant_impermeable | nombre décimal | m² | 0..1 | Surface imperméable raccordée (fiche A49) |  |
| bassin_versant_permeable | nombre décimal | m² | 0..1 | Surface perméable raccordée (fiche A49) |  |
| profondeur_mare | nombre décimal | m | 0..1 | Profondeur maximale d'une mare (fiche A49) |  |
| fond_mare | énumération : etanche, argile, naturel |  | 0..1 | Nature du fond d'une mare (fiche A49) |  |
| gites | booléen |  | 0..1 | Gîtes de chiroptères (fiche A57) |  |
| regime_gestion | énumération : plan, courante, abandon |  | 0..1 | Régime imposé dès la livraison (fiche A55) |  |
| regime_apres_plan | énumération : plan, courante, abandon |  | 0..1 | Régime après le plan de gestion (fiche A55) |  |
| plan_gestion_annees | entier | an | 0..1 | Durée du plan de gestion propre à l'unité (fiche A55) |  |
| niveau_sonore | nombre décimal | dB(A) | 0..1 | Niveau sonore à l'unité (fiche A21) |  |
| exposition_vitrage | booléen |  | 0..1 | À moins de 15 m d'une façade vitrée non traitée de plus de 10 m² (fiche A22) |  |
| alimentation_eau | énumération : naturelle, artificielle |  | 0..1 | Alimentation d'une unité en eau (fiche A23) |  |
| statut | énumération : conservee, creee, amelioree |  | 0..1 | Statut à l'état projet (fiches A27 à A29) |  |
| unite_liee | texte |  | 0..1 | Identifiant de l'unité initiale liée, pour une unité conservée ou améliorée |  |
| protection_chantier | booléen |  | 0..1 | Protection prévue pendant le chantier (fiche A27) |  |
| Critere_Collection | élément composé |  | 0..1 | Réponses à la grille d'état |  |
| Score_Declare | élément composé |  | 0..1 | Résumé de la grille quand le détail des critères n'est pas transmis (fiche A10) |  |
| alimentation_humide | énumération : nappe, pluie |  | 0..1 | Alimentation d'un milieu humide : nappe ou pluie (fiche A47) |  |
| Renouvellement_Collection | élément composé |  | 0..1 | Années de réfection (fiche A30) |  |

#### 7.3.16 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite/Eclairage_Horaire`

Éclairage déclaré heure par heure (fiches A51 à A53).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| extinction | entier | heure légale | 0..1 | Heure d'extinction, absente si allumé toute la nuit |  |
| rallumage | entier | heure légale | 0..1 | Heure de rallumage du matin |  |
| temperature_couleur | nombre décimal | K | 1..1 | Température de couleur |  |
| part_detection | nombre décimal |  | 0..1 | Part de temps allumé sous détection de présence |  |

#### 7.3.17 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite/Critere_Collection`

Réponses à la grille d'état.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Critere | élément composé |  | 0..n | Réponse à un critère de la grille d'état du type |  |

#### 7.3.18 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite/Critere_Collection/Critere`

Réponse à un critère de la grille d'état du type.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| code | texte |  | 1..1 | Code du critère dans la grille (A, B, A1, indicateur_bois_mort...) |  |
| reponse | énumération : oui, non, sans_objet |  | 0..1 | Réponse à un critère binaire |  |
| note | entier | note 1 à 3 | 0..1 | Note d'un indicateur de la grille des boisements |  |
| preuve | texte |  | 0..1 | Référence de la pièce qui justifie la réponse |  |

#### 7.3.19 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite/Score_Declare`

Résumé de la grille quand le détail des critères n'est pas transmis (fiche A10).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| satisfaits | entier |  | 1..1 | Critères satisfaits |  |
| applicables | entier |  | 1..1 | Critères applicables |  |
| essentiel_echoue | booléen |  | 0..1 | Un critère essentiel a échoué |  |

#### 7.3.20 `RSNat/Entree_Projet/Etat_Initial/Unite_Collection/Unite/Renouvellement_Collection`

Années de réfection (fiche A30).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| annee | entier | an | 0..n | Année de réfection, de 2 à 50 |  |

#### 7.3.21 `RSNat/Entree_Projet/Variante_Collection`

Variantes de l'état projet (fiche A41).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Variante | élément composé |  | 1..n | Variante |  |

#### 7.3.22 `RSNat/Entree_Projet/Variante_Collection/Variante`

Variante.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| index | entier |  | 1..1 | Index de la variante |  |
| nom | texte |  | 1..1 | Nom |  |
| reference | booléen |  | 1..1 | Variante de référence |  |
| Unite_Collection | élément composé |  | 1..1 | Unités de l'état projet |  |
| Bois_Collection | élément composé |  | 0..1 | Bois mis en œuvre (fiche A34) |  |
| Granulats | élément composé |  | 0..1 | Granulats, sables et roches (fiche A35) |  |
| Ouvrage_Pluvial_Collection | élément composé |  | 0..1 | Ouvrages de gestion des eaux pluviales (fiche A24) |  |
| Facade_Vitree_Collection | élément composé |  | 0..1 | Façades vitrées exposées (fiche A22) |  |

#### 7.3.23 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection`

Unités de l'état projet.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Unite | élément composé |  | 0..n | Unité d'habitat |  |

#### 7.3.24 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite`

Unité d'habitat.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| identifiant | texte |  | 1..1 | Identifiant unique de l'unité dans le projet |  |
| identifiant_geometrique | texte |  | 0..1 | Identifiant de l'objet géométrique correspondant (import futur) |  |
| code_habitat | texte |  | 1..1 | Code de nomenclature_habitats.csv ou code EUNIS rattaché (fiche A04) |  |
| position | énumération : sol_pleine_terre, sol_sur_dalle, hors_sol_toiture, hors_sol_facade, eau, arbre, lineaire |  | 1..1 | Position de saisie (fiche A04) |  |
| surface | nombre décimal | m² | 1..1 | Surface ; houppier pour un arbre, longueur x largeur pour une haie (fiches A13 à A16) |  |
| epaisseur_substrat | nombre décimal | cm | 0..1 | Épaisseur de substrat, sur dalle ou hors-sol |  |
| hauteur_facade | nombre décimal | m | 0..1 | Hauteur végétalisée d'une façade |  |
| longueur | nombre décimal | m | 0..1 | Longueur d'une haie ou d'une façade |  |
| largeur | nombre décimal | m | 0..1 | Largeur d'une haie |  |
| nombre_arbres | entier |  | 0..1 | Nombre d'arbres d'une unité arbre |  |
| classe_diametre | énumération : petit, moyen, grand, tres_grand |  | 0..1 | Classe de diamètre des arbres |  |
| stade | énumération : J, M, A |  | 0..1 | Stade d'un type ligneux |  |
| situation | énumération : reservoir, corridor, hors_trame |  | 0..1 | Situation dans la trame verte et bleue (fiche A02) |  |
| tache | texte |  | 0..1 | Identifiant de tache (fiche A17) |  |
| eclairage | énumération : L0, L1, L2 |  | 0..1 | Raccourci d'éclairage L0, L1 ou L2 (fiche A53-2) |  |
| Eclairage_Horaire | élément composé |  | 0..1 | Éclairage déclaré heure par heure (fiches A51 à A53) |  |
| distance_lumiere | nombre décimal | m | 0..1 | Distance au point lumineux le plus proche |  |
| arrose | booléen |  | 0..1 | Arrosage automatique (fiche A49) |  |
| texture_sol | énumération : sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |  | 0..1 | Texture du sol de l'unité, si elle diffère de celle du site (fiche A48) |  |
| profondeur_sol | nombre décimal | m | 0..1 | Profondeur de sol de l'unité (fiche A48) |  |
| bassin_versant_impermeable | nombre décimal | m² | 0..1 | Surface imperméable raccordée (fiche A49) |  |
| bassin_versant_permeable | nombre décimal | m² | 0..1 | Surface perméable raccordée (fiche A49) |  |
| profondeur_mare | nombre décimal | m | 0..1 | Profondeur maximale d'une mare (fiche A49) |  |
| fond_mare | énumération : etanche, argile, naturel |  | 0..1 | Nature du fond d'une mare (fiche A49) |  |
| gites | booléen |  | 0..1 | Gîtes de chiroptères (fiche A57) |  |
| regime_gestion | énumération : plan, courante, abandon |  | 0..1 | Régime imposé dès la livraison (fiche A55) |  |
| regime_apres_plan | énumération : plan, courante, abandon |  | 0..1 | Régime après le plan de gestion (fiche A55) |  |
| plan_gestion_annees | entier | an | 0..1 | Durée du plan de gestion propre à l'unité (fiche A55) |  |
| niveau_sonore | nombre décimal | dB(A) | 0..1 | Niveau sonore à l'unité (fiche A21) |  |
| exposition_vitrage | booléen |  | 0..1 | À moins de 15 m d'une façade vitrée non traitée de plus de 10 m² (fiche A22) |  |
| alimentation_eau | énumération : naturelle, artificielle |  | 0..1 | Alimentation d'une unité en eau (fiche A23) |  |
| statut | énumération : conservee, creee, amelioree |  | 0..1 | Statut à l'état projet (fiches A27 à A29) |  |
| unite_liee | texte |  | 0..1 | Identifiant de l'unité initiale liée, pour une unité conservée ou améliorée |  |
| protection_chantier | booléen |  | 0..1 | Protection prévue pendant le chantier (fiche A27) |  |
| Critere_Collection | élément composé |  | 0..1 | Réponses à la grille d'état |  |
| Score_Declare | élément composé |  | 0..1 | Résumé de la grille quand le détail des critères n'est pas transmis (fiche A10) |  |
| alimentation_humide | énumération : nappe, pluie |  | 0..1 | Alimentation d'un milieu humide : nappe ou pluie (fiche A47) |  |
| Renouvellement_Collection | élément composé |  | 0..1 | Années de réfection (fiche A30) |  |

#### 7.3.25 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite/Eclairage_Horaire`

Éclairage déclaré heure par heure (fiches A51 à A53).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| extinction | entier | heure légale | 0..1 | Heure d'extinction, absente si allumé toute la nuit |  |
| rallumage | entier | heure légale | 0..1 | Heure de rallumage du matin |  |
| temperature_couleur | nombre décimal | K | 1..1 | Température de couleur |  |
| part_detection | nombre décimal |  | 0..1 | Part de temps allumé sous détection de présence |  |

#### 7.3.26 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite/Critere_Collection`

Réponses à la grille d'état.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Critere | élément composé |  | 0..n | Réponse à un critère de la grille d'état du type |  |

#### 7.3.27 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite/Critere_Collection/Critere`

Réponse à un critère de la grille d'état du type.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| code | texte |  | 1..1 | Code du critère dans la grille (A, B, A1, indicateur_bois_mort...) |  |
| reponse | énumération : oui, non, sans_objet |  | 0..1 | Réponse à un critère binaire |  |
| note | entier | note 1 à 3 | 0..1 | Note d'un indicateur de la grille des boisements |  |
| preuve | texte |  | 0..1 | Référence de la pièce qui justifie la réponse |  |

#### 7.3.28 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite/Score_Declare`

Résumé de la grille quand le détail des critères n'est pas transmis (fiche A10).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| satisfaits | entier |  | 1..1 | Critères satisfaits |  |
| applicables | entier |  | 1..1 | Critères applicables |  |
| essentiel_echoue | booléen |  | 0..1 | Un critère essentiel a échoué |  |

#### 7.3.29 `RSNat/Entree_Projet/Variante_Collection/Variante/Unite_Collection/Unite/Renouvellement_Collection`

Années de réfection (fiche A30).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| annee | entier | an | 0..n | Année de réfection, de 2 à 50 |  |

#### 7.3.30 `RSNat/Entree_Projet/Variante_Collection/Variante/Bois_Collection`

Bois mis en œuvre (fiche A34).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Bois | élément composé |  | 0..n | Lot de bois |  |

#### 7.3.31 `RSNat/Entree_Projet/Variante_Collection/Variante/Bois_Collection/Bois`

Lot de bois.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| regime | énumération : plantation, coupe_rase, coupe_selective, faible_impact |  | 1..1 | Régime forestier déclaré |  |
| volume | nombre décimal | m³ | 1..1 | Volume mis en œuvre |  |
| remplacements | entier |  | 0..1 | Nombre de remplacements en 50 ans |  |
| justification | texte |  | 0..1 | Pièce qui justifie le régime |  |

#### 7.3.32 `RSNat/Entree_Projet/Variante_Collection/Variante/Granulats`

Granulats, sables et roches (fiche A35).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| masse | nombre décimal | t | 1..1 | Masse mise en œuvre |  |
| remplacements | entier |  | 0..1 | Nombre de remplacements en 50 ans |  |

#### 7.3.33 `RSNat/Entree_Projet/Variante_Collection/Variante/Ouvrage_Pluvial_Collection`

Ouvrages de gestion des eaux pluviales (fiche A24).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Ouvrage_Pluvial | élément composé |  | 0..n | Ouvrage |  |

#### 7.3.34 `RSNat/Entree_Projet/Variante_Collection/Variante/Ouvrage_Pluvial_Collection/Ouvrage_Pluvial`

Ouvrage.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| surface_drainee | nombre décimal | m² | 1..1 | Surface imperméable conduite vers l'ouvrage |  |
| infiltration_surface | booléen |  | 1..1 | Infiltration en surface |  |

#### 7.3.35 `RSNat/Entree_Projet/Variante_Collection/Variante/Facade_Vitree_Collection`

Façades vitrées exposées (fiche A22).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Facade_Vitree | élément composé |  | 0..n | Façade |  |

#### 7.3.36 `RSNat/Entree_Projet/Variante_Collection/Variante/Facade_Vitree_Collection/Facade_Vitree`

Façade.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| surface | nombre décimal | m² | 1..1 | Surface vitrée exposée |  |
| traitee | booléen |  | 1..1 | Vitrage traité contre les collisions |  |

#### 7.3.37 `RSNat/Sortie_Projet`

Résultats (partie 1, chapitre 11).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Variante_Resultat | élément composé |  | 1..n | Résultats d'une variante |  |

#### 7.3.38 `RSNat/Sortie_Projet/Variante_Resultat`

Résultats d'une variante.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| index | entier |  | 1..1 | Index de la variante |  |
| Contexte | élément composé |  | 1..1 | Sorties de l'étape E1 (fiche A02) |  |
| Fermeture_Collection | élément composé |  | 1..1 | Contrôle de fermeture (fiche A03) |  |
| Unite_Resultat_Collection | élément composé |  | 1..1 | Résultats par unité |  |
| Site | élément composé |  | 1..1 | Sorties des modules S et T (fiches A08, A24, A31) |  |
| Materiaux | élément composé |  | 1..1 | Sorties du module G (fiches A32 à A36) |  |
| Indicateurs | élément composé |  | 1..1 | Indicateurs de l'opération (fiches A37, A38) |  |
| Incertitude | élément composé |  | 0..1 | Analyse d'incertitude (fiche A39) |  |
| Conformite | élément composé |  | 1..1 | Conformité (fiche A40) |  |

#### 7.3.39 `RSNat/Sortie_Projet/Variante_Resultat/Contexte`

Sorties de l'étape E1 (fiche A02).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| part_emprise | nombre décimal |  | 1..1 | Part d'emprise du bâti e |  |
| bnat_min | nombre décimal | points | 0..1 | Seuil de Bnat applicable |  |
| pleine_terre_min | nombre décimal |  | 1..1 | Seuil de pleine terre applicable |  |
| multiplicateur_delai | nombre décimal |  | 1..1 | Multiplicateur de délai de la zone |  |

#### 7.3.40 `RSNat/Sortie_Projet/Variante_Resultat/Fermeture_Collection`

Contrôle de fermeture (fiche A03).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Fermeture | élément composé |  | 2..2 | Contrôle d'un état |  |

#### 7.3.41 `RSNat/Sortie_Projet/Variante_Resultat/Fermeture_Collection/Fermeture`

Contrôle d'un état.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| etat | énumération : initial, projet |  | 1..1 | État |  |
| somme | nombre décimal | m² | 1..1 | Somme des surfaces au sol |  |
| ecart | nombre décimal | m² | 1..1 | Écart avec S_p |  |
| conforme | booléen |  | 1..1 | Contrôle satisfait |  |

#### 7.3.42 `RSNat/Sortie_Projet/Variante_Resultat/Unite_Resultat_Collection`

Résultats par unité.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| Unite_Resultat | élément composé |  | 0..n | Résultats d'une unité |  |

#### 7.3.43 `RSNat/Sortie_Projet/Variante_Resultat/Unite_Resultat_Collection/Unite_Resultat`

Résultats d'une unité.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| identifiant | texte |  | 1..1 | Identifiant de l'unité |  |
| etat | énumération : initial, projet |  | 1..1 | État |  |
| type | texte |  | 1..1 | Type OpenNAT retenu h_u |  |
| nature_surface | texte |  | 0..1 | Nature S01 à S12 |  |
| coefficient_sol | nombre décimal |  | 0..1 | c_u |  |
| facteur_support | nombre décimal |  | 1..1 | f_sol,u |  |
| valeur_intrinseque | nombre décimal | m²HE/m² | 1..1 | v_u |  |
| score_etat | nombre décimal |  | 0..1 | S_u |  |
| facteur_etat | nombre décimal |  | 1..1 | f_u |  |
| classe_etat | énumération : bon, moyen, mauvais, sans_etat |  | 1..1 | cl_u |  |
| multiplicateur_situation | nombre décimal |  | 1..1 | m_u |  |
| facteur_taille | nombre décimal |  | 0..1 | k_taille |  |
| facteur_connectivite | nombre décimal |  | 1..1 | k_C,u |  |
| facteur_eclairage | nombre décimal |  | 0..1 | k_lum,u |  |
| fraction_nuit_eclairee | nombre décimal |  | 0..1 | x_nuit,u |  |
| facteur_nuisances | nombre décimal |  | 1..1 | k_N,u |  |
| facteur_eau | nombre décimal |  | 1..1 | k_E,u |  |
| valeur_habitat | nombre décimal | m²HE | 1..1 | V^H_u |  |
| valeur_maturite | nombre décimal | m²HE | 1..1 | V_u |  |
| delai | nombre décimal | an | 0..1 | d_u |  |
| difficulte | nombre décimal |  | 0..1 | D_u |  |
| groupe_hydrique | énumération : gazon, prairie, xerophile, arbustif, arbore, conifere, toiture_extensive, humide_pluie, mare |  | 0..1 | g_u (fiche A47) |  |
| reserve_utile | nombre décimal | mm | 0..1 | RU_u (fiche A48) |  |
| Bilan_Hydrique | élément composé |  | 0..3 | Bilan d'un niveau de réchauffement (fiches A49, A50) |  |
| mois_depart_maturation | entier |  | 0..1 | Rang du mois de départ (fiche A58) |  |
| facteurs_hydriques | texte |  | 0..1 | 50 valeurs annuelles k_W,u(t) |  |
| facteurs_gestion | texte |  | 0..1 | 50 valeurs annuelles f_g,u(t) |  |
| trajectoire | texte | m²HE | 0..1 | 50 valeurs annuelles V_u(t) séparées par des espaces |  |
| valeur_integree | nombre décimal | m²HE·an | 0..1 | Somme de la trajectoire |  |

#### 7.3.44 `RSNat/Sortie_Projet/Variante_Resultat/Unite_Resultat_Collection/Unite_Resultat/Bilan_Hydrique`

Bilan d'un niveau de réchauffement (fiches A49, A50).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| niveau | énumération : 2_0, 2_7, 4_0 |  | 1..1 | Année type |  |
| indice_stress | nombre décimal | jours-équivalents | 0..1 | IS_u,n |  |
| indice_stress_reference | nombre décimal | jours-équivalents | 0..1 | IS_ref,g |  |
| facteur_hydrique | nombre décimal |  | 1..1 | k_W,u,n |  |
| arrosage | nombre décimal | mm | 0..1 | Volume d'arrosage annuel |  |
| assec_printemps | booléen |  | 0..1 | Mare à sec entre mars et juin |  |

#### 7.3.45 `RSNat/Sortie_Projet/Variante_Resultat/Site`

Sorties des modules S et T (fiches A08, A24, A31).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| valeur_initiale | nombre décimal | m²HE | 1..1 | V_0 |  |
| i0 | nombre décimal | m²HE·an | 1..1 | I_0 |  |
| i1 | nombre décimal | m²HE·an | 1..1 | I_1 |  |
| i0_30 | nombre décimal | m²HE·an | 1..1 | I_0,30 |  |
| i1_30 | nombre décimal | m²HE·an | 1..1 | I_1,30 |  |
| dette_maturite | nombre décimal | m²HE·an | 1..1 | DM |  |
| supplement_destruction | nombre décimal | m²HE·an | 1..1 | ΔI_ch (fiche A57) |  |
| arrosage_annuel | nombre décimal | m³ | 1..1 | Volume d'arrosage annuel moyen de la période (fiche A49) |  |
| rang_plantation | entier |  | 0..1 | m_pl (fiche A58) |  |
| annees_periode | texte |  | 0..1 | Première et dernière années civiles de la période (fiche A46) |  |
| trajectoire_reference | texte | m²HE | 0..1 | 50 valeurs annuelles de l'état initial sous le même climat |  |
| trajectoire_site | texte | m²HE | 1..1 | 50 valeurs annuelles V_1(t) |  |
| pleine_terre | nombre décimal |  | 1..1 | PT |  |
| pleine_terre_initiale | nombre décimal |  | 1..1 | PT_0 |  |
| impermeable_initial | nombre décimal | m² | 1..1 | A_imp,0 |  |
| impermeable_projet | nombre décimal | m² | 1..1 | A_imp,1 |  |
| impermeabilisation_nette | nombre décimal | m² | 1..1 | ΔA_imp |  |
| part_pluvial_infiltre | nombre décimal |  | 0..1 | P_inf |  |
| surface_vitree_non_traitee | nombre décimal | m² | 0..1 | A_vit,nt |  |

#### 7.3.46 `RSNat/Sortie_Projet/Variante_Resultat/Materiaux`

Sorties du module G (fiches A32 à A36).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| facteur_climat | nombre décimal | m²HE/kg CO2 éq. | 1..1 | CF |  |
| inat_climat | nombre décimal | m²HE·an | 1..1 | Inat_clim |  |
| Inat_Climat_Phase | élément composé |  | 0..5 | Inat_clim par phase |  |
| inat_bois | nombre décimal | m²HE·an | 1..1 | Inat_bois |  |
| inat_carrieres | nombre décimal | m²HE·an | 1..1 | Inat_carr |  |
| Pollution_Resultat | élément composé |  | 0..n | Indicateurs de pollution |  |

#### 7.3.47 `RSNat/Sortie_Projet/Variante_Resultat/Materiaux/Inat_Climat_Phase`

Inat_clim par phase.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| phase | énumération : A1-A3, A4-A5, B, C, D |  | 1..1 | Phase |  |
| valeur | nombre décimal | m²HE·an | 1..1 | Inat_clim,p |  |

#### 7.3.48 `RSNat/Sortie_Projet/Variante_Resultat/Materiaux/Pollution_Resultat`

Indicateurs de pollution.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| code | entier |  | 1..1 | Code |  |
| valeur | nombre décimal | unité de l'annexe II | 1..1 | POL_i |  |

#### 7.3.49 `RSNat/Sortie_Projet/Variante_Resultat/Indicateurs`

Indicateurs de l'opération (fiches A37, A38).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| cnat | nombre décimal | m²HE·an | 1..1 | Consommation de nature sur 50 ans (fiche A37) |  |
| cnat_moyen | nombre décimal | m²HE | 1..1 | Consommation moyenne annuelle |  |
| cnat_relatif | nombre décimal |  | 0..1 | Cnat / I_0 |  |
| cnat_30 | nombre décimal | m²HE·an | 1..1 | Consommation sur 30 ans |  |
| inat | nombre décimal | m²HE·an | 1..1 | Biodiversité grise |  |
| snat | nombre décimal | m²HE·an | 1..1 | Solde de nature |  |
| bnat | nombre décimal | points | 1..1 | Besoin de nature de la conception (fiche A38) |  |
| cbs | nombre décimal |  | 1..1 | Coefficient de biotope équivalent |  |
| cnat_par_m2_parcelle | nombre décimal | m²HE·an/m² | 1..1 | Cnat / S_p |  |
| inat_par_m2_sref | nombre décimal | m²HE·an/m² | 0..1 | Inat / S_ref |  |

#### 7.3.50 `RSNat/Sortie_Projet/Variante_Resultat/Incertitude`

Analyse d'incertitude (fiche A39).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| tirages | entier |  | 1..1 | Nombre de tirages |  |
| Intervalle | élément composé |  | 0..n | Intervalle d'un indicateur |  |
| Parametre_Influent | élément composé |  | 0..5 | Paramètre parmi les cinq plus influents |  |

#### 7.3.51 `RSNat/Sortie_Projet/Variante_Resultat/Incertitude/Intervalle`

Intervalle d'un indicateur.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| indicateur | texte |  | 1..1 | Nom de l'indicateur |  |
| p5 | nombre décimal |  | 1..1 | Centile 5 |  |
| p50 | nombre décimal |  | 1..1 | Centile 50 |  |
| p95 | nombre décimal |  | 1..1 | Centile 95 |  |

#### 7.3.52 `RSNat/Sortie_Projet/Variante_Resultat/Incertitude/Parametre_Influent`

Paramètre parmi les cinq plus influents.

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| rang | entier |  | 1..1 | Rang |  |
| table | texte |  | 1..1 | Table de donnees/ |  |
| cle | texte |  | 1..1 | Clé |  |
| parametre | texte |  | 1..1 | Paramètre |  |
| correlation | nombre décimal |  | 1..1 | ρ de Spearman avec Snat |  |

#### 7.3.53 `RSNat/Sortie_Projet/Variante_Resultat/Conformite`

Conformité (fiche A40).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| bnat_conforme | booléen |  | 0..1 | conf_Bnat |  |
| pleine_terre_conforme | booléen |  | 1..1 | conf_PT |  |
| plu_conforme | booléen |  | 0..1 | conf_PLU |  |
| niveau_cnat | entier |  | 1..1 | Niveau 0, 1 ou 2 |  |

#### 7.3.54 `RSNat/Attestation_Permis`

Attestation de prise en compte de la biodiversité au dépôt du permis de construire (fiche A40, convention C-P1).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| variante | entier |  | 1..1 | Index de la variante attestée |  |
| bnat | nombre décimal | points | 1..1 | Bnat |  |
| bnat_min | nombre décimal | points | 0..1 | Seuil de Bnat |  |
| pleine_terre | nombre décimal |  | 1..1 | Taux de pleine terre |  |
| pleine_terre_min | nombre décimal |  | 1..1 | Seuil |  |
| cbs_plu | nombre décimal |  | 0..1 | Coefficient de biotope du PLU |  |
| pleine_terre_plu | nombre décimal |  | 0..1 | Pleine terre du PLU |  |
| conforme | booléen |  | 1..1 | Conclusion de conformité |  |
| mention | texte |  | 0..1 | Mention, notamment l'écart au minimum du PLU |  |

#### 7.3.55 `RSNat/Attestation_Achevement`

Attestation à l'achèvement (fiche A40).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| variante | entier |  | 1..1 | Index de la variante réalisée |  |
| cnat | nombre décimal | m²HE·an | 1..1 | Consommation de nature sur 50 ans (fiche A37) |  |
| cnat_moyen | nombre décimal | m²HE | 1..1 | Consommation moyenne annuelle |  |
| cnat_relatif | nombre décimal |  | 0..1 | Cnat / I_0 |  |
| cnat_30 | nombre décimal | m²HE·an | 1..1 | Consommation sur 30 ans |  |
| inat | nombre décimal | m²HE·an | 1..1 | Biodiversité grise |  |
| snat | nombre décimal | m²HE·an | 1..1 | Solde de nature |  |
| bnat | nombre décimal | points | 1..1 | Besoin de nature de la conception (fiche A38) |  |
| cbs | nombre décimal |  | 1..1 | Coefficient de biotope équivalent |  |
| cnat_par_m2_parcelle | nombre décimal | m²HE·an/m² | 1..1 | Cnat / S_p |  |
| inat_par_m2_sref | nombre décimal | m²HE·an/m² | 0..1 | Inat / S_ref |  |
| niveau_cnat | entier |  | 1..1 | Niveau atteint |  |

#### 7.3.56 `RSNat/Empreinte`

Empreintes de contrôle (fiche A42).

| Élément | Type | Unité | Card. | Description | Origine |
|---|---|---|---|---|---|
| entrees | texte |  | 1..1 | SHA-256 de Entree_Projet |  |
| sorties | texte |  | 1..1 | SHA-256 de Sortie_Projet |  |

### 7.4 Énumérations

| Énumération | Valeurs admises |
|---|---|
| zone | atlantique, continentale, mediterraneenne, alpine |
| typologie | logement, tertiaire, industrie, amenagement |
| position | sol_pleine_terre, sol_sur_dalle, hors_sol_toiture, hors_sol_facade, eau, arbre, lineaire |
| situation | reservoir, corridor, hors_trame |
| eclairage | L0, L1, L2 |
| alimentation | naturelle, artificielle |
| statut | conservee, creee, amelioree |
| stade | J, M, A |
| classe_diametre | petit, moyen, grand, tres_grand |
| reponse | oui, non, sans_objet |
| connexion | forte, moyenne, faible |
| cloture | aucune, permeable, etanche |
| regime | plantation, coupe_rase, coupe_selective, faible_impact |
| phase | A1-A3, A4-A5, B, C, D |
| etat | initial, projet |
| classe_etat | bon, moyen, mauvais, sans_etat |
| zone_climatique | H1a, H1b, H1c, H2a, H2b, H2c, H2d, H3 |
| texture | sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |
| fond_mare | etanche, argile, naturel |
| alimentation_humide | nappe, pluie |
| regime_gestion | plan, courante, abandon |
| niveau_rechauffement | 2_0, 2_7, 4_0 |
| groupe_hydrique | gazon, prairie, xerophile, arbustif, arbore, conifere, toiture_extensive, humide_pluie, mare |

### 7.5 Exemple

Extrait du fichier `schemas/exemple_annexe_C.rsnat.xml`, écrit par le moteur, blocs Indicateurs et Attestation_Permis :

```
<Indicateurs>
  <cnat>3217.2</cnat>
  <cnat_moyen>64.3</cnat_moyen>
  <cnat_relatif>0.2423</cnat_relatif>
  <cnat_30>1988.1</cnat_30>
  <inat>141842.9</inat>
  <snat>-145060.0</snat>
  <bnat>59.0</bnat>
  <cbs>0.5900</cbs>
  <cnat_par_m2_parcelle>1.6086</cnat_par_m2_parcelle>
  <inat_par_m2_sref>101.3163</inat_par_m2_sref>
</Indicateurs>
<Attestation_Permis>
  <variante>1</variante>
  <bnat>59.0</bnat>
  <bnat_min>45.0</bnat_min>
  <pleine_terre>0.4250</pleine_terre>
  <pleine_terre_min>0.1500</pleine_terre_min>
  <conforme>true</conforme>
</Attestation_Permis>
```

### 7.6 Fichier projet

Le fichier projet est l'entrée du moteur : un fichier JSON, validé contre `schemas/projet.schema.json` avant tout calcul. Il porte les données du chapitre 4 de la partie 1. Quand un RSEE est indiqué (`projet.rsee`), la parcelle, les bâtiments, les indicateurs d'ACV, la zone climatique, le département et l'altitude s'en reprennent (fiche A05) ; une donnée saisie l'emporte sur celle du RSEE. Les valeurs par défaut appliquées sont écrites au journal du calcul.

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `format` | « OpenNAT projet 1 » | oui |  |
| `projet` | objet | oui |  |
| `projet.identifiant` | texte | oui |  |
| `projet.nom` | texte |  |  |
| `projet.adresse` | texte |  |  |
| `projet.commune_insee` | texte |  |  |
| `projet.date_etude` | texte |  |  |
| `projet.rsee` | texte |  | Chemin d'un RSEE à reprendre (fiche A05) |
| `contexte` | objet | oui |  |
| `contexte.zone_biogeographique` | un de : atlantique, continentale, mediterraneenne, alpine | oui |  |
| `contexte.typologie` | un de : logement, tertiaire, industrie, amenagement | oui |  |
| `contexte.zone_climatique` | un de : H1a, H1b, H1c, H2a, H2b, H2c, H2d, H3 | oui |  |
| `contexte.departement` | texte |  |  |
| `contexte.altitude` | number ou null |  |  |
| `contexte.sol` | objet |  |  |
| `contexte.sol.texture` | un de : sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |  |  |
| `contexte.sol.profondeur` | nombre |  |  |
| `contexte.cbs_plu` | nombre |  |  |
| `contexte.pleine_terre_plu` | nombre |  |  |
| `contexte.k_delai_etude` | nombre |  | Étude de sensibilité des délais (cas 8c) |
| `parcelle` | objet | oui |  |
| `parcelle.surface` | nombre | oui |  |
| `parcelle.emprise` | nombre |  | Emprise du bâti quand aucun bâtiment n'est décrit |
| `parcelle.surface_vegetalisee_rsee` | nombre |  |  |
| `parcelle.surface_impermeable_rsee` | nombre |  |  |
| `parcelle.surface_arrosee_rsee` | nombre |  |  |
| `chantier` | voir chantier |  |  |
| `gestion` | voir gestion |  |  |
| `taches` | objet |  |  |
| `batiments` | liste |  |  |
| `etat_initial` | liste | oui |  |
| `variantes` | liste | oui |  |
| `options` | objet |  |  |
| `options.tirages` | entier |  |  |
| `options.graine` | entier |  |  |
| `options.bloc` | entier |  |  |

#### Définition `chantier`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `annee_debut` | entier |  |  |
| `mois_debut` | entier |  |  |
| `duree_mois` | nombre |  |  |
| `mois_destruction` | entier |  |  |

#### Définition `gestion`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `plan_annees` | nombre |  |  |

#### Définition `tache`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `connexion` | un de : forte, moyenne, faible |  |  |
| `exterieur` | nombre |  |  |
| `cloture` | un de : aucune, permeable, etanche |  |  |
| `distance_espace_naturel` | nombre |  |  |
| `surface_espace_naturel` | nombre |  |  |
| `trame` | booléen |  |  |

#### Définition `batiment`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `nom` | texte |  |  |
| `sref` | nombre |  |  |
| `emprise_au_sol` | nombre |  |  |
| `duree_chantier` | nombre |  |  |
| `ges` | objet |  |  |
| `pollution` | objet |  |  |

#### Définition `eclairage`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
|  | un de : L0, L1, L2 ou objet |  |  |

#### Définition `unite`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `id` | texte | oui |  |
| `code` | texte | oui |  |
| `position` | un de : sol_pleine_terre, sol_sur_dalle, hors_sol_toiture, hors_sol_facade, eau, arbre, lineaire |  |  |
| `surface` | nombre |  |  |
| `epaisseur` | nombre |  |  |
| `longueur` | nombre |  |  |
| `largeur` | nombre |  |  |
| `hauteur` | nombre |  |  |
| `nombre_arbres` | entier |  |  |
| `classe_diametre` | un de : petit, moyen, grand, tres_grand |  |  |
| `stade` | un de : J, M, A, jeune, moyen, age |  |  |
| `situation` | un de : reservoir, corridor, hors_trame |  |  |
| `tache` | texte |  |  |
| `criteres` | objet |  |  |
| `notes` | objet |  |  |
| `score` | objet |  |  |
| `eclairage` | voir eclairage |  |  |
| `niveau_sonore` | nombre |  |  |
| `exposition_vitrage` | booléen |  |  |
| `alimentation` | un de : naturelle, artificielle |  |  |
| `alimentation_humide` | un de : nappe, pluie |  |  |
| `statut` | un de : conservee, creee, amelioree |  |  |
| `liee` | texte |  |  |
| `protection` | booléen |  |  |
| `renouvellements` | liste |  |  |
| `arrose` | booléen |  |  |
| `texture` | un de : sable, sable_limoneux, limon_sableux, limon, limon_silteux, silt, limon_argilo_silteux, argile_silteuse, argile |  |  |
| `profondeur_sol` | nombre |  |  |
| `bassin_versant` | nombre |  |  |
| `bassin_versant_permeable` | nombre |  |  |
| `profondeur` | nombre |  |  |
| `fond` | un de : etanche, argile, naturel |  |  |
| `gites` | booléen |  |  |
| `gestion` | un de : plan, courante, abandon |  |  |
| `apres_plan` | un de : courante, abandon |  |  |
| `plan_gestion_annees` | nombre |  |  |

#### Définition `variante`

| Champ | Type | Obligatoire | Remarque |
|---|---|---|---|
| `nom` | texte | oui |  |
| `reference` | booléen |  |  |
| `unites` | liste | oui |  |
| `batiments` | liste |  |  |
| `materiaux` | objet |  |  |
| `ouvrages_pluviaux` | liste |  |  |
| `facades_vitrees` | liste |  |  |
| `taches` | objet |  |  |
| `chantier` | voir chantier |  |  |
| `gestion` | voir gestion |  |  |
| `emprise` | nombre |  |  |
