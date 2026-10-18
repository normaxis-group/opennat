# Méthode de calcul OpenNAT, version 1

Méthode conventionnelle de calcul de la consommation de nature d'une opération de construction ou d'aménagement.

Éditeur : NORMATYS. Application dans la certification Effinature : IRICE. Moteur de calcul libre : le moteur OpenNAT, qui porte le nom de la méthode.
Version 1, 18 octobre 2026. Projet soumis à la validation du Biodiversity Standard Council : la méthode, ses conventions et ses seuils ne sont pas opposables tant que le conseil ne les a pas validés.
Texte et tables de données sous licence CC BY 4.0, chaque valeur portant la licence de sa source. Moteur sous licence AGPL-3.0-or-later.

---

## Sommaire

1. Objet, domaine d'application, exclusions
2. Termes, définitions, symboles et unités
3. Principes
4. Données d'entrée
5. Conventions de contexte
6. Algorithme général
7. Étapes et modules de calcul
8. Agrégation et indicateurs
9. Analyse d'incertitude
10. Seuils proposés et modulations
11. Récapitulatif standardisé RSNat et attestations
12. Annexes : A tables de coefficients, B correspondances de nomenclatures, C exemple de calcul complet

---

## 1. Objet, domaine d'application, exclusions

### 1.1 Objet

La méthode OpenNAT calcule, pour une opération de construction ou d'aménagement, ce que l'opération retire ou rend à la nature, sur sa parcelle et par les matériaux qu'elle consomme. Elle joue pour la biodiversité le rôle que la méthode Th-BCE 2020 joue pour l'énergie : des données d'entrée décrites de façon conventionnelle, des calculs intermédiaires enchaînés dans un ordre fixe, des indicateurs, des seuils et un récapitulatif standardisé.

Elle produit quatre indicateurs :

| Indicateur | Rôle | Pendant RE2020 | Unité |
|---|---|---|---|
| Bnat | Besoin de nature lié à la conception du plan masse, indépendamment des aménagements paysagers | Bbio | points |
| Cnat | Consommation de nature sur le site : écart, intégré sur 50 ans, entre la valeur écologique que le site aurait gardée sans le projet et celle qu'il a avec le projet | Cep | m²HE·an |
| Inat | Biodiversité grise : perte de nature causée par les matériaux et le chantier, sur leur cycle de vie | Ic construction | m²HE·an |
| Snat | Solde de nature : -(Cnat + Inat) | Ic bâtiment | m²HE·an |

### 1.2 Domaine d'application

Bâtiments neufs, extensions, réhabilitations lourdes qui modifient les abords, opérations d'aménagement, en France métropolitaine (zones biogéographiques atlantique, continentale, méditerranéenne et alpine).

### 1.3 Exclusions de la version 1

Habitats littoraux et marins (groupes EUNIS A et B hors milieux terrestres), outre-mer, complexes d'habitats (groupe X), grottes, glaciers et reliefs volcaniques actifs (H1, H4, H6). Saisie géométrique (maquette BIM, système d'information géographique) : la saisie est tabulaire, mais le fichier projet porte un identifiant géométrique facultatif par unité pour un import futur.

La méthode ne remplace ni l'étude d'impact, ni le diagnostic écologique, ni la séquence éviter, réduire, compenser du code de l'environnement. Elle les utilise comme données d'entrée.

---

## 2. Termes, définitions, symboles et unités

### 2.1 Termes

Habitat équivalent (HE) : unité de valeur écologique. Un m²HE est un m² d'écosystème de référence en pleine intégrité. Un m² d'habitat réel vaut de 0 à 1 m²HE, jusqu'à 1,15 m²HE quand sa situation dans la trame verte et bleue ou sa connectivité le justifient (convention C-H7).

Unité d'habitat : surface homogène du site, d'un seul type d'habitat, d'une seule position et d'un seul état. Une unité appartient à l'état initial, à l'état projet, ou aux deux quand elle est conservée.

Position : sol en pleine terre, sol sur dalle, hors-sol en toiture, hors-sol en façade, eau, arbre, linéaire.

Tache : ensemble d'unités végétalisées ou en eau contiguës, au sens de la contiguïté déclarée dans le fichier projet.

Période de référence : 50 ans, comme la période d'étude de référence de l'ACV de la RE2020.

Dette de maturité : valeur, en m²HE·an, que les habitats créés n'apportent pas encore pendant qu'ils mûrissent.

### 2.2 Symboles

| Symbole | Désignation | Unité |
|---|---|---|
| S_p | Surface de la parcelle | m² |
| A_u | Surface de l'unité u (houppier projeté pour un arbre, longueur x largeur pour une haie, surface de façade pour une façade) | m² |
| v_u | Valeur intrinsèque du type d'habitat de u | m²HE/m² |
| S_u | Score d'état de u | sans unité, 0 à 1 |
| f_u | Facteur d'état | sans unité, 0,5 à 1 |
| c_u | Coefficient de sol de la nature de surface de u | sans unité |
| f_sol,u | Facteur de support appliqué à la valeur d'habitat | sans unité |
| m_u | Multiplicateur de situation dans la trame verte et bleue | sans unité |
| k_C,u | Facteur de connectivité de la tache de u | sans unité |
| k_N,u | Facteur de nuisances de u | sans unité |
| k_E,u | Facteur hydrique de u | sans unité |
| V_u | Valeur de l'unité à maturité | m²HE |
| V_u(t) | Valeur de l'unité l'année t | m²HE |
| d_u | Délai de maturité | an |
| D_u | Difficulté de création ou d'amélioration | sans unité |
| d_ch | Durée du chantier | an |
| N | Période de référence (50) | an |
| I_0, I_1 | Valeur du site intégrée sur N ans, sans projet et avec projet | m²HE·an |
| CF | Facteur de caractérisation du climat | m²HE par kg CO2 éq. et par an |
| S_ref | Surface de référence du bâtiment (RE2020) | m² |

### 2.3 Unités et arrondis

Les surfaces sont en m², les valeurs en m²HE, les valeurs intégrées en m²HE·an, les émissions en kg CO2 éq. Les résultats intermédiaires sont conservés sans arrondi ; les résultats affichés portent une décimale, comme dans la méthode Th-BCE.

---

## 3. Principes

### 3.1 Valeur d'une unité

La valeur d'une unité est le produit de sa surface, de la valeur intrinsèque de son type, de son état et de facteurs de contexte. La valeur intrinsèque vient de la liste allemande des valeurs de biotopes (BKompV, 2020), ramenée à 1 (convention C-H1). L'état se mesure par une grille de critères observables, transposée des fiches d'état de la métrique statutaire anglaise (convention C-H6), et non par un choix direct entre bon, moyen et mauvais.

### 3.2 Temps

Le site se simule année par année sur 50 ans. Les habitats détruits disparaissent au début du chantier. Les habitats créés partent de zéro à la fin du chantier et gagnent leur valeur cible en un délai propre à chaque type, multipliée par la probabilité de réussite (difficulté) de la métrique anglaise. Les valeurs annuelles s'additionnent sans actualisation (convention C-T5) : la lenteur de la maturation est comptée en m²HE·an perdus.

### 3.3 Frontières du système

Le site : la parcelle ou l'unité foncière du projet, au sol, plus les surfaces hors-sol (toitures et façades végétalisées) qui s'ajoutent sans compter dans la surface au sol. Les espaces voisins n'entrent que par leur effet sur la connectivité et par la situation dans la trame verte et bleue.

L'amont : la production des matériaux, leur transport, le chantier, leur remplacement pendant 50 ans et leur fin de vie, tels que l'ACV de la RE2020 les décrit (contributeurs « composants » et « chantier », convention C-G1).

### 3.4 Additivité

Le site et les matériaux s'expriment dans la même unité, le m²HE·an, parce que la perte de MSA (abondance moyenne des espèces, Mean Species Abundance) sur une surface pendant une durée est, par construction, une perte d'habitat équivalent : 1 m² à MSA 1 pendant un an vaut 1 m²HE·an.

### 3.5 Trois familles de valeurs

Chaque coefficient vient de `donnees/`, avec sa source, sa référence précise et son type : primaire (lu tel quel), transposition (lu dans une source primaire et appliqué par une correspondance écrite), secondaire (lu dans une source qui en cite une autre), convention (fixé par la méthode et justifié). Aucune valeur numérique de méthode n'est écrite dans le moteur.

---

## 4. Données d'entrée

Les données d'entrée suivent la logique de la RE2020 : un projet, ses bâtiments, ses zones, et, pour OpenNAT, son site décrit en unités d'habitat. Toute donnée déjà saisie pour la RE2020 se reprend du RSEE du projet, sans nouvelle saisie.

### 4.1 Données reprises du RSEE

| Donnée OpenNAT | Élément du RSEE (branche RSEnv) | Usage |
|---|---|---|
| Surface de la parcelle S_p | `entree_projet/parcelle/surface_parcelle` | Fermeture des surfaces, Bnat, ratios |
| Surface végétalisée déclarée | `entree_projet/parcelle/surface_veg` | Contrôle de cohérence avec les unités saisies |
| Surface imperméabilisée déclarée | `entree_projet/parcelle/surface_imper` | Contrôle de cohérence |
| Surface arrosée | `entree_projet/parcelle/surface_arrosee` | Indicateur complémentaire |
| Emprise au sol du bâtiment | `entree_projet/batiment/emprise_au_sol` | Choix du seuil de Bnat (emprise en % de S_p) |
| Durée du chantier | `entree_projet/batiment/duree_chantier` (mois) | d_ch = durée / 12 |
| Surface de référence S_ref | `entree_projet/batiment/sref` | Inat par m² |
| Usage des zones, nombre de logements | `entree_projet/batiment/zone/usage`, `nb_logement` | Typologie, seuils |
| Adresse, commune, coordonnées | `Datas_Comp`, `adresse`, `latitude`, `longitude` | Zone biogéographique, contexte large |
| Émissions de gaz à effet de serre par phase | `sortie_projet/batiment/contributeur/{composant, chantier}/indicateurs_acv_collection`, indicateur 101, phases A1-A3, A4-A5, B, C, D | Inat climat (équation G2) |
| Indicateurs de pollution | mêmes collections, indicateurs 106 à 109 et 116 | Indicateurs complémentaires |

Les codes 101 à 136 des indicateurs suivent l'ordre de la liste de l'annexe II de l'arrêté du 4 août 2021 : 101 émissions de gaz à effet de serre totales, 106 acidification, 107 à 109 eutrophisation (eaux douces, marine, terrestre), 116 écotoxicité pour les eaux douces, 119 indice de qualité des sols. Seuls les RSEE qui portent la branche RSEnv fournissent ces données ; à défaut, elles se saisissent.

### 4.2 Données du site, par unité d'habitat

Pour l'état initial et pour l'état projet :

| Donnée | Valeurs admises | Défaut |
|---|---|---|
| Identifiant | texte | aucun |
| Identifiant géométrique | texte, facultatif | vide |
| Type d'habitat | code de `donnees/nomenclature_habitats.csv` (EUNIS 2012 de niveau 3 ou type urbain VB) | aucun |
| Position | sol pleine terre, sol sur dalle, hors-sol toiture, hors-sol façade, eau, arbre, linéaire | celle du type |
| Surface A_u | m² | aucun |
| Épaisseur de substrat | cm, pour les positions sur dalle et hors-sol | aucun |
| Hauteur de façade imputée | m, plafonnée à 10 m | 10 |
| Stade (types ligneux) | jeune, moyen, âgé ; ou classe de diamètre pour un arbre | moyen |
| Critères d'état | réponse oui ou non à chaque critère de la grille du type (ou note de 1 à 3 pour un boisement) | tous non |
| Situation | réservoir, corridor, hors trame | hors trame |
| Tache | identifiant de tache | une tache par unité |
| Éclairage | L0, L1, L2 | L0 |
| Niveau sonore | dB(A) | aucun effet |
| Exposition aux vitrages | oui ou non | non |
| Alimentation en eau (positions eau) | naturelle, artificielle | naturelle |

Pour l'état projet seulement :

| Donnée | Valeurs admises | Défaut |
|---|---|---|
| Statut | conservée, créée, améliorée | créée |
| Unité initiale liée (conservée, améliorée) | identifiant | aucun |
| Protection en chantier (conservée) | oui ou non | non |
| Critères d'état visés (créée, améliorée) | comme ci-dessus | aucun |
| Renouvellements | années de réfection | aucun |

### 4.3 Données de contexte

| Donnée | Valeurs admises | Défaut |
|---|---|---|
| Zone biogéographique | atlantique, continentale, méditerranéenne, alpine | zone majoritaire du département |
| Typologie | logement et équipement d'intérêt collectif, tertiaire, industrie, aménagement | logement |
| Coefficient de biotope et part de pleine terre imposés par le PLU | nombres, facultatifs | aucun |
| Surface végétalisée extérieure contiguë à chaque tache | m² | 0 |
| Connexion de chaque tache | contiguë à un espace naturel d'au moins 1 ha ou à la trame, à moins de 200 m, isolée | isolée |
| Clôture de chaque tache | perméable, étanche, sans clôture | sans clôture |
| Surface dont l'eau de pluie est infiltrée en surface | m² | 0 |

Les données de contexte large (trame verte et bleue, réservoirs, corridors, espaces naturels voisins, zonages) se lisent dans les couches publiques : SRADDET et SRCE, documents d'urbanisme, couches de l'IGN et de l'INPN. L'outil de saisie peut les préremplir à partir de l'adresse ; l'écologue les valide.

### 4.4 Données des matériaux pour l'occupation des sols

| Donnée | Unité | Défaut |
|---|---|---|
| Volume de bois mis en œuvre, par régime forestier déclaré | m³ | aucun |
| Régime forestier et pièce qui le justifie | plantation, coupe rase, coupe sélective, faible impact | coupe rase |
| Masse de granulats, sables et roches | t | aucune |
| Nombre de remplacements pendant 50 ans | entier | 0 |

### 4.5 Variantes

Un projet peut porter plusieurs variantes de l'état projet. L'état initial et le contexte sont communs ; chaque variante est calculée et comparée.

---

## 5. Conventions de contexte

### 5.1 Zone biogéographique

Quatre zones terrestres (Agence européenne pour l'environnement, couche des régions biogéographiques de 2016). La zone est une donnée d'entrée ; une table d'aide par département sera livrée avec le moteur. En v1, la zone ne change pas les délais de maturation, dont la plage d'incertitude est élargie en zones méditerranéenne et alpine (convention C-E2).

### 5.2 Situation dans la trame verte et bleue

Multiplicateur m_u (convention C-E1, `donnees/contexte.csv`) :

(1) m_u = 1,15 si u est dans un réservoir de biodiversité identifié, 1,10 dans un corridor identifié, 1 ailleurs.

Le même multiplicateur s'applique à l'état initial et à l'état projet.

### 5.3 Typologie et emprise

La typologie et la part d'emprise du bâti (emprise / S_p) choisissent le seuil de Bnat (chapitre 10).

---

## 6. Algorithme général

Le calcul enchaîne cinq étapes et sept modules, dans un ordre fixe. Chaque étape lit les sorties des précédentes et écrit les siennes dans le dossier de résultats.

| Ordre | Étape ou module | Lit | Écrit |
|---|---|---|---|
| 1 | E1 Contexte | contexte, situation | m_u, zone, seuils applicables |
| 2 | E2 Prétraitement | unités | contrôle de fermeture, classement, correspondances |
| 3 | S Sol | unités, `sols.csv` | c_u, f_sol,u, pleine terre, imperméabilisation |
| 4 | H Habitats | unités, `habitats.csv`, `etat_criteres.csv` | v_u, S_u, f_u, V^H_u |
| 5 | C Connectivité | taches, contexte, `connectivite.csv` | k_C par tache |
| 6 | N Nuisances | unités, `nuisances.csv` | k_N,u |
| 7 | E Eau | unités, `eau.csv` | k_E,u, part infiltrée |
| 8 | T Temps | sorties 3 à 7, statuts, chantier | V_u(t), I_0, I_1, dette de maturité |
| 9 | G Biodiversité grise | RSEE, matériaux, `materiaux.csv` | Inat par phase et par poste |
| 10 | E3 Agrégation | sorties 3 à 9 | Cnat, Inat, Snat, Bnat, indicateurs complémentaires |
| 11 | E4 Incertitude | toutes les tables | intervalle à 90 %, paramètres influents |
| 12 | E5 Conformité | indicateurs, `seuils.csv` | niveaux atteints, attestations |

Le module T est le plus long : il simule chaque unité sur 50 ans. L'étape E4 refait toute la chaîne au moins 1 000 fois. Un calcul complet peut durer plusieurs minutes.

---

## 7. Étapes et modules de calcul

Chaque fiche suit le plan des fiches algorithmes de la méthode Th-BCE : objet, nomenclature (entrées, paramètres, sorties), description mathématique, cas limites.

### 7.1 Étape E1 : contexte

Objet : fixer les données qui valent pour tout le site.
Entrées : zone, typologie, situation de chaque unité, emprise, coefficient de biotope du PLU.
Paramètres : `contexte.csv`.
Sorties : m_u par unité (équation 1), seuil de Bnat applicable (chapitre 10).

### 7.2 Étape E2 : prétraitement des surfaces

Objet : vérifier et classer les unités.

(2) Fermeture : | somme des A_u des unités au sol - S_p | <= max(1 m², 0,005 x S_p)

La somme porte sur les positions sol pleine terre, sol sur dalle, eau et linéaire, à l'état initial et à l'état projet séparément. Les positions hors-sol et arbre n'y entrent pas : un houppier surplombe d'autres unités. Si l'écart dépasse la tolérance (convention C-E3), le calcul s'arrête.

Chaque unité reçoit son type de la nomenclature, sa position et, pour les types ligneux, son stade. Une unité dont le type est inconnu arrête le calcul.

Cas limites : surfaces nulles refusées ; une haie se saisit en longueur x largeur, largeur d'au moins 1 m.

### 7.3 Module S : sol

Objet : qualifier le support de chaque unité.
Paramètres : `sols.csv` (convention C-S1).

(S1) c_u = coefficient de la nature de surface de u :
- S01 surface scellée (VB.1, VB.2) ;
- S02 revêtement perméable non végétalisé (VB.3, H5.6) ;
- S03 revêtement perméable végétalisé (VB.4) ;
- S04 à S07 végétation sur dalle ou toiture, selon l'épaisseur de substrat : moins de 15 cm, 15 à 30 cm, plus de 30 cm et moins de 80 cm, 80 cm et plus ;
- S08 pleine terre (toute unité végétalisée au sol en pleine terre) ;
- S09 et S10 façade enracinée ou hors sol ;
- S11 eau alimentée par la pluie ou naturelle, S12 eau traitée ou bassin nu.

(S2) f_sol,u = c_u si u est d'un type au sol posé sur dalle, 1 sinon (convention C-S2).

(S3) Taux de pleine terre : PT = (somme des A_u en pleine terre et végétalisées) / S_p.

(S4) Imperméabilisation nette créée : somme des A_u en S01 à l'état projet - somme des A_u en S01 à l'état initial.

### 7.4 Module H : habitats

Objet : valeur de chaque unité hors contexte.
Paramètres : `habitats.csv`, `etat_criteres.csv`.

(H1) v_u = valeur intrinsèque du type de u (convention C-H1), ou du stade déclaré pour un type ligneux (convention C-H5).

(H2) S_u = (nombre de critères satisfaits) / (nombre de critères applicables) ; si un critère essentiel échoue, S_u = min(S_u, 0,5) (convention C-H6). Pour un boisement, S_u = (somme des 13 notes - 13) / 26. Pour un type sans grille (cultures, surfaces minérales), S_u n'est pas calculé et f_u = 1.

(H3) f_u = 0,5 + 0,5 x S_u (convention C-H2).

(H4) V^H_u = A_u x v_u x f_u x f_sol,u x m_u

La classe d'état affichée (bon si S_u >= 0,85, moyen si S_u >= 0,65, mauvais sinon) sert au module T pour choisir le délai de maturité.

Cas limites : un habitat créé est évalué sur les critères visés et justifiés dans le dossier (plan de gestion, cahier des charges des plantations) ; un habitat existant, sur les critères relevés.

### 7.5 Module C : connectivité

Objet : effet de la taille et de l'isolement des taches.
Paramètres : `connectivite.csv`.

(C1) A_k = somme des A_u des unités de la tache k (positions au sol, eau, linéaire et hors-sol ; les arbres ne s'ajoutent pas, ils surplombent) + surface végétalisée extérieure contiguë à k.

(C2) k_taille,k = min(1 ; max(0,35 ; (A_k / 44 000)^0,22)) (convention C-C1).

(C3) k_C,k = k_taille,k x m_conn,k x k_clot,k, avec m_conn,k = 1,15, 1,10 ou 1 (convention C-C2) et k_clot,k = 0,9 pour une tache close par une clôture étanche, 1 sinon (convention C-C3).

Toute unité de la tache k reçoit k_C,u = k_C,k. Les unités minérales et scellées ne forment pas de tache : k_C,u = 1.

Cas limites : une voirie interne coupe la contiguïté ; une toiture végétalisée isolée forme sa propre tache.

### 7.6 Module N : nuisances

Objet : effet de la lumière artificielle, du bruit et des vitrages.
Paramètres : `nuisances.csv`.

(N1) k_N,u = k_lum,u x k_bruit,u x k_vit,u

k_lum,u = 1 (L0), 0,9 (L1) ou 0,75 (L2) (convention C-N1). k_bruit,u = 0,7 si le niveau sonore dépasse 47 dB(A) en milieu ouvert ou 42 dB(A) en milieu boisé, 1 sinon (convention C-N2). k_vit,u = 0,95 si u est à moins de 15 m d'une façade exposant plus de 10 m² de vitrage non traité, 1 sinon (convention C-N3).

### 7.7 Module E : eau

Objet : alimentation des milieux en eau et gestion des eaux pluviales.
Paramètres : `eau.csv`.

(E1) k_E,u = 0,8 pour une unité en eau alimentée artificiellement, 1 sinon (convention C-E4).

Sortie complémentaire : part des eaux pluviales infiltrées ou gérées à ciel ouvert, qui entre dans Bnat par le bonus S13 (convention C-E5).

Valeur à maturité d'une unité :

(H5) V_u = min(1,15 x A_u ; V^H_u x k_C,u x k_N,u x k_E,u) (convention C-H7)

### 7.8 Module T : temps

Objet : trajectoire annuelle de chaque unité sur 50 ans.
Paramètres : `habitats.csv` (délais, difficultés), `contexte.csv`.

(T1) Part de l'année t occupée par le chantier : phi_t = min(1 ; max(0 ; d_ch - (t - 1))), t = 1 à 50.

(T2) Unité conservée : V_u(t) = V_u x (1 - r x phi_t), avec r = 0 si une protection en chantier est prévue, 0,25 sinon (convention C-T4).

(T3) Unité créée : V_u(t) = D_u x V_u x g(t), avec g(t) = 0 si t <= d_ch, 1 si d_u = 0, min(1 ; (t - d_ch) / d_u) sinon.

d_u est le délai de maturité du type pour la classe d'état visée (C-T1, C-T2), multiplié par le multiplicateur de zone (C-E2) ; pour un type sans évaluation d'état dans la métrique anglaise, le délai « sans état » ; pour un type minéral, 0 (C-T3). D_u est la difficulté de création (C-T7).

(T4) Unité améliorée : V_u(t) = V_u,0 + (D_u x V_u - V_u,0) x g(t) si D_u x V_u > V_u,0, et V_u,0 sinon, où V_u,0 est la valeur à l'état initial de l'unité liée et D_u la difficulté d'amélioration.

(T5) Renouvellement prévu l'année R : V_u(t) = 0 de R à R + 1 (convention C-T6), puis maturation selon (T3) depuis R + 1.

(T6) Valeurs intégrées : I_0 = N x somme des V_u de l'état initial ; I_1 = somme, pour t de 1 à N, des V_u(t) de l'état projet. Les mêmes sommes sur 30 ans donnent les sorties complémentaires.

(T7) Dette de maturité : somme, pour t de 1 à N, des (D_u x V_u - V_u(t)) des unités créées et améliorées.

Sorties : trajectoire de chaque unité (50 valeurs), trajectoire du site, I_0, I_1, dette de maturité.

### 7.9 Module G : biodiversité grise

Objet : perte de nature causée par les matériaux et le chantier.
Paramètres : `materiaux.csv`.

(G1) Inat = Inat_clim + Inat_sols

(G2) Inat_clim = CF x S_ref x somme sur les phases p de (GES_p x a_p)

GES_p est l'indicateur 101 du RSEE (kg CO2 éq. par m² de S_ref) des contributeurs composants et chantier pour la phase p. a_p est la durée pendant laquelle l'émission pèse sur la période de référence : 50 ans pour A1-A3 et A4-A5, 25 ans pour B, 0 pour C et D (convention C-G3).

(G3) CF = S_terres x (1 - p_cult) x (pente / 2) x TCRE = 1,807 x 10^-3 m²HE par kg CO2 éq. et par an (convention C-G2).

(G4) Inat_bois = somme sur les régimes r de Q_r x (1 + n_remp) x (10 000 x R / P) x (1 - MSA_r)

Q_r volume de bois du régime r (m³), n_remp nombre de remplacements, R = 2 m³ de bois rond par m³ de produit, P = 5,4 m³ par ha et par an, MSA_r qualité d'habitat de la forêt d'origine (conventions C-G4, C-G5).

(G5) Inat_carrières = M x (1 + n_remp) x o x (1 - 0,05), avec M masse de granulats et roches (t) et o = 0,9 m²·an par t (convention C-G6).

(G6) Inat_sols = Inat_bois + Inat_carrières (les autres matériaux sont négligés en v1, convention C-G7).

Sorties : Inat par phase, par poste (climat, bois, carrières), et, quand le RSEE le permet, par lot. Indicateurs complémentaires de pollution, en unités de l'annexe II (convention C-G8).

---

## 8. Agrégation et indicateurs

(A1) Cnat = I_0 - I_1 (m²HE·an). Cnat positif : le site perd de la nature ; négatif : il en gagne. Cnat moyen = Cnat / N (m²HE).

(A2) Snat = -(Cnat + Inat)

(A3) Bnat = 100 x (somme des A_u x c_u de l'état projet + 0,2 x surface dont l'eau de pluie est infiltrée en surface) / S_p (convention C-B1)

Bnat se calcule sur les seules données du plan masse : natures de surface, épaisseurs de substrat, toitures et façades végétalisées, eau. Il ignore le type d'habitat, l'état et le temps : il est à Cnat ce que le Bbio est au Cep. Bnat / 100 est un coefficient de biotope au sens de l'article L. 151-22 du code de l'urbanisme, comparable aux coefficients des PLU.

(A4) Ratios : Cnat / S_p (m²HE·an par m² de parcelle), Inat / S_ref (m²HE·an par m² de S_ref), Cnat relatif = Cnat / I_0.

Indicateurs complémentaires : Cnat et Snat sur 30 ans, dette de maturité, taux de pleine terre, imperméabilisation nette créée, part des eaux pluviales infiltrées, part de surfaces éclairées, surface vitrée exposée non traitée, part d'essences indigènes plantées (déclarée), indicateurs de pollution.

---

## 9. Analyse d'incertitude

Chaque valeur de `donnees/` porte une plage (incertitude_min, incertitude_max), lue dans la source quand elle en donne une, fixée sinon par la convention C-I1 : ± 10 % pour un texte réglementaire ou un outil officiel, ± 25 % pour un jugement d'expert publié, ± 50 % pour une convention.

(I1) Pour chaque tirage j de 1 à n (n >= 1 000) : chaque valeur est tirée selon une loi triangulaire (borne basse, valeur centrale, borne haute), toute la chaîne E1 à E3 est recalculée.

(I2) Sorties : valeur centrale (calcul aux valeurs centrales), 5e et 95e centiles (intervalle à 90 %) de Cnat, Inat, Snat et Bnat ; les cinq paramètres dont la corrélation de rang de Spearman avec Snat est la plus forte en valeur absolue (convention C-I2).

La graine du générateur est écrite dans le fichier projet et dans le RSNat : deux calculs à graine identique donnent des résultats identiques.

---

## 10. Seuils proposés et modulations

Tous les seuils de ce chapitre sont proposés et en attente de validation du Biodiversity Standard Council.

### 10.1 Bnat et pleine terre

Seuils raccordés au coefficient de biotope par surface harmonisé du référentiel Effinature 8.1 (critère SOL 01.2.5, convention C-E6), modulés par la typologie et l'emprise (Mnat) :

| Typologie | Emprise du bâti | Bnat minimal |
|---|---|---|
| Logements, équipements d'intérêt collectif | jusqu'à 37 % | 45 |
| Logements, équipements d'intérêt collectif | 38 à 49 % | 35 |
| Logements, équipements d'intérêt collectif | 50 % et plus | 25 |
| Commerces, bureaux, administrations, hébergements avec services | toutes | 25 |
| Industrie, aménagement | toutes | pas de seuil en v1 |

Pleine terre végétalisée : au moins 15 % de l'emprise totale du projet.

Garde-fou d'urbanisme : quand le PLU impose un coefficient de biotope ou une part de pleine terre plus exigeants, c'est le minimum du PLU qui s'applique, et l'attestation le compare au projet (convention C-P1).

### 10.2 Cnat

Niveau 1, absence de perte nette : Cnat <= 0.
Niveau 2, gain net : Cnat <= -0,10 x I_0 (convention C-E7).

### 10.3 Inat et Snat

Pas de seuil en v1. Inat et Snat sont calculés et affichés ; leurs seuils seront fixés après le banc de validation, sur la distribution des opérations réelles, comme l'ont été ceux de l'Ic construction.

---

## 11. Récapitulatif standardisé RSNat et attestations

Le nom RSNat (récapitulatif standardisé de l'étude nature) est provisoire.

### 11.1 Fichier

Un fichier XML, validé par un schéma XSD publié avec la méthode, et sa copie JSON. Sa structure reprend celle du RSEE : un bloc `Entree_Projet` (toutes les données du chapitre 4, dont l'identifiant du RSEE source quand il existe) et un bloc `Sortie_Projet` (résultats). Il porte la version de la méthode, la version des tables de données, la graine aléatoire et une empreinte de contrôle (SHA-256) des entrées et des sorties.

### 11.2 Contenu de `Sortie_Projet`

- Par étape et par module : les sorties listées au chapitre 7.
- Par unité : v_u, S_u, f_u, c_u, k_C,u, k_N,u, k_E,u, V_u, trajectoire sur 50 ans.
- Pour le site : I_0, I_1, Cnat, Cnat moyen, Cnat sur 30 ans, dette de maturité, PT, Bnat.
- Pour les matériaux : Inat par phase et par poste, indicateurs de pollution.
- Incertitude : centiles 5 et 95 de chaque indicateur, cinq paramètres les plus influents.
- Conformité : seuils applicables, niveaux atteints, minimum du PLU et écart éventuel.

### 11.3 Attestation au dépôt du permis de construire

Comme l'attestation de prise en compte de la RE2020 au dépôt du permis de construire, qui ne demande que le Bbio, l'attestation OpenNAT au permis porte sur les données du plan masse (convention C-P1) :
- Bnat, son seuil et sa conformité ;
- taux de pleine terre et son seuil ;
- coefficient de biotope et part de pleine terre imposés par le PLU, s'il y en a, et leur respect ;
- version de la méthode, empreinte de contrôle.

Si le projet ne respecte pas le minimum du PLU, l'attestation le mentionne et ne conclut pas à la conformité. L'extrait XML correspondant se dépose sur la plateforme d'IRICE, qui enregistre l'attestation.

### 11.4 Attestation à l'achèvement

Elle reprend le RSNat complet : Cnat, Inat, Snat, leurs intervalles à 90 %, les niveaux atteints, sur la base des surfaces réalisées et de l'état mesuré des unités conservées.

---

## 12. Annexes

### Annexe A : tables de coefficients

Les tables sont dans `donnees/`, une ligne par valeur, avec les colonnes `cle`, `parametre`, `valeur`, `unite`, `incertitude_min`, `incertitude_max`, `source`, `reference_precise`, `url`, `licence`, `type`, `convention`, `justification`. Le rapport de couverture (`donnees/rapport_couverture.md`) donne, table par table, la part de valeurs primaires, transposées, secondaires et conventionnelles.

| Table | Contenu | Construction |
|---|---|---|
| `nomenclature_habitats.csv` | 191 types : 165 types EUNIS 2012 de niveau 3 présents en France et 26 types urbains et hors-sol VB, avec leur correspondance BKompV et anglaise | écrite à la main, une justification par ligne |
| `habitats.csv` | valeurs intrinsèques, stades, délais de maturité, difficultés | `outils/construire_habitats.py`, depuis la BKompV et la métrique anglaise |
| `etat_criteres.csv` | 11 grilles d'état, règles de score | transposition des fiches anglaises de juillet 2025 |
| `sols.csv` | 13 natures de surface | `outils/construire_sols.py`, médiane de six grilles |
| `contexte.csv` | période, actualisation, fermeture, situation, zones, chantier | |
| `connectivite.csv` | effet de taille, connectivité, clôtures | |
| `nuisances.csv` | lumière, bruit, vitrages | |
| `eau.csv` | alimentation des milieux en eau | |
| `materiaux.csv` | facteur climat, bois, carrières, pollution | |
| `seuils.csv` | seuils proposés | |
| `conventions.csv` | index des 42 conventions | généré depuis `methode/conventions.md` |

### Annexe B : correspondances de nomenclatures

`donnees/nomenclature_habitats.csv` donne, pour chaque type OpenNAT : le code EUNIS 2012, les codes EUNIS 2012 qui s'y rattachent (pour les types VB), la position, le code BKompV retenu, la ligne de la métrique anglaise retenue et la justification. La correspondance vers CORINE Biotopes se lit dans HabRef v7 (PatriNat, fichier `CRSP_CB_EUNIS_2012_70.xlsx`), cité comme référence de lecture tant que sa licence n'est pas lue.

Les types EUNIS du groupe J (bâti, réseaux, décharges) se saisissent par le type VB correspondant : J1 et J2 bâtis en VB.1, J4.2 en VB.2, J4.3 en VB.25, J1.5 en VB.8, J1.6 en VB.10, J5 selon l'eau en VB.19 à VB.24.

### Annexe C : exemple de calcul complet

Opération : résidence de logements collectifs sur une friche urbaine, zone continentale, hors trame verte et bleue, sans éclairage ni bruit au-dessus des seuils à l'état initial. Parcelle de 2 000 m². Chantier de 18 mois (d_ch = 1,5 an). Les nombres ont été vérifiés par `outils/verifier_exemple.py`, indépendant du moteur.

**C.1 Étape E2, fermeture.** État initial : 1 200 + 600 + 200 = 2 000 m². État projet : 700 + 300 + 150 + 450 + 320 + 80 = 2 000 m². Écart nul (équation 2).

**C.2 État initial, modules S, H et C.**

| Unité | Type | A_u | v_u | Critères | S_u | f_u | V^H_u |
|---|---|---|---|---|---|---|---|
| U0-1 friche herbacée | VB.8 | 1 200 | 0,5000 (BKompV 51.04a.01 : 12/24) | EU1 : A, B, D satisfaits, C essentiel échoué (renouée du Japon) | 3/4 = 0,75, plafonné à 0,5 | 0,75 | 1 200 x 0,5 x 0,75 = 450,00 |
| U0-2 parking enrobé | VB.2 | 600 | 0 | sans grille | | 1 | 0 |
| U0-3 friche arbustive | VB.9 | 200 | 0,5000 (41.01.06 : 12/24) | EF1 : 2 sur 5 | 0,4 | 0,70 | 70,00 |
| U0-4 deux arbres indigènes, diamètre moyen | VB.18a, stade M | 100 (houppiers) | 0,6250 (41.05aM : 15/24) | EA1 : 5 sur 6 | 0,8333 | 0,9167 | 57,29 |

f_sol = 1 (pleine terre), m = 1 (hors trame), k_N = k_E = 1.

Tache unique : friche herbacée et arbustive, A = 1 200 + 200 = 1 400 m² (les houppiers surplombent et ne s'ajoutent pas, équation C1). k_taille = (1 400 / 44 000)^0,22 = 0,4684 (C2), au-dessus du plancher 0,35. Connexion faible (1), pas de clôture (1) : k_C = 0,4684 (C3).

V_u (équation H5) : U0-1 = 450,00 x 0,4684 = 210,77 ; U0-3 = 70,00 x 0,4684 = 32,79 ; U0-4 = 57,29 x 0,4684 = 26,83 ; U0-2 = 0.
Valeur du site sans projet : 270,39 m²HE. I_0 = 50 x 270,39 = 13 519,3 m²HE·an (T6).

**C.3 État projet, modules S, H, C et N.**

| Unité | Type, statut | A_u | v_u | Critères visés | S_u | f_u | k_C | k_N | V_u | d_u | D_u |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 bâtiment | VB.1, créée | 700 | 0 | | | 1 | 1 | 1 | 0 | 0 | 1 |
| U1-2 voirie, stationnement | VB.2, créée | 300 | 0 | | | 1 | 1 | 1 | 0 | 0 | 1 |
| U1-3 cheminements stabilisés | VB.3, créée | 150 | 0,1667 | sans grille | | 1 | 1 | 1 | 25,00 | 0 (C-T3) | 1 |
| U1-4 prairie urbaine extensive | VB.26, créée | 450 | 0,6250 | EP2 : 4 sur 6 | 0,6667 | 0,8333 | 0,4197 | 0,9 (L1) | 88,53 | 5 (moyen) | 1 |
| U1-5 jardins privatifs | VB.7, créée | 320 | 0,4583 | EU1 : 2 sur 3 | 0,6667 | 0,8333 | 0,4197 | 1 | 51,29 | 1 (sans état) | 1 |
| U1-6 haie champêtre 40 m x 2 m | FA.3, stade M, créée | 80 | 0,6667 | EH1 : 6 sur 8 | 0,75 | 0,875 | 0,4197 | 1 | 19,59 | 5 (moyen) | 1 |
| U1-7 deux arbres | VB.18a, conservée, protégée | 100 | 0,6250 | EA1 : 5 sur 6 | 0,8333 | 0,9167 | 0,4197 | 1 | 24,04 | | |
| U1-8 toiture biodiverse, 15 cm | VB.12, créée, hors-sol | 500 | 0,5278 | EU1 + G : 4 sur 4 | 1 | 1 | 0,3734 | 1 | 98,55 | 10 (bon) | 0,67 |

Taches : prairie, jardins et haie, contiguës : 450 + 320 + 80 = 850 m², k_taille = (850 / 44 000)^0,22 = 0,4197 ; toiture isolée : 500 m², k_taille = 0,3734. La prairie est éclairée par l'éclairage du stationnement, conforme à l'arrêté de 2018 et éteint la nuit : k_lum = 0,9.

Exemple de ligne : prairie, V_u = 450 x 0,6250 x 0,8333 x 1 x 1 x 0,4197 x 0,9 = 88,53 m²HE.

**C.4 Module T.** phi_1 = 1, phi_2 = 0,5, phi_t = 0 ensuite (T1). Les arbres protégés gardent 24,04 chaque année (T2). Les unités créées démarrent à t > 1,5 (T3) ; par exemple, la prairie vaut 88,53 x (2 - 1,5) / 5 = 8,85 l'année 2, puis 26,56 l'année 3, et atteint 88,53 l'année 7 ; la toiture vaut 0,67 x 98,55 x 0,05 = 3,30 l'année 2 et atteint 0,67 x 98,55 = 66,03 l'année 12.

| Année | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 | 11 | 12 à 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeur du site V_1(t), m²HE | 24,04 | 88,81 | 142,68 | 170,90 | 199,13 | 227,35 | 244,76 | 251,37 | 264,57 | 271,18 | 274,48 |

I_1 = 12 847,4 m²HE·an. Valeur à maturité : 274,48 m²HE. Dette de maturité (T7) : 876,5 m²HE·an.

**C.5 Agrégation du site.** Cnat = 13 519,3 - 12 847,4 = 671,9 m²HE·an (A1), soit 5,0 % de I_0 et 13,4 m²HE en moyenne annuelle. Sur 30 ans : 753,7 m²HE·an. À maturité, le site projet (274,48 m²HE) vaut un peu plus que le site initial (270,39) ; la perte nette sur 50 ans vient des années de chantier et de maturation. Le niveau 1 (Cnat <= 0) n'est pas atteint.

**C.6 Module G.** Données du RSEE : S_ref = 1 400 m² ; indicateur 101 des contributeurs composants et chantier : A1-A3 350, A4-A5 120, B 400, C 55, D -40 kg CO2 éq. par m².
Somme des GES_p x a_p = (350 + 120) x 50 + 400 x 25 + 55 x 0 + (-40) x 0 = 33 500 kg·an par m².
Inat_clim = 1,807 x 10^-3 x 1 400 x 33 500 = 84 748 m²HE·an (G2).
Bois : 30 m³, régime non justifié, donc coupe rase (MSA 0,50) : occupation = 10 000 x 2 / 5,4 = 3 703,7 m²·an par m³ ; Inat_bois = 30 x 3 703,7 x (1 - 0,50) = 55 556 m²HE·an (G4).
Granulats : 1 800 t ; Inat_carrières = 1 800 x 0,9 x 0,95 = 1 539 m²HE·an (G5).
Inat = 84 748 + 55 556 + 1 539 = 141 843 m²HE·an, soit 101,3 m²HE·an par m² de S_ref.

**C.7 Solde.** Snat = -(671,9 + 141 843) = -142 515 m²HE·an.

**C.8 Bnat.** Bâtiment et voirie : 1 000 m² x 0 ; cheminements : 150 x 0,2 = 30 ; pleine terre : 850 x 1 = 850 ; toiture de 15 cm (S05) : 500 x 0,6 = 300. Bnat = 100 x 1 180 / 2 000 = 59,0 (A3). Emprise 700 / 2 000 = 35 %, seuil 45 : atteint. Pleine terre 850 / 2 000 = 42,5 %, seuil 15 % : atteint.

**C.9 Lecture.** L'attestation au permis porte Bnat = 59,0 (seuil 45) et une pleine terre de 42,5 % (seuil 15 %) : le plan masse est conforme. À l'achèvement, le site reste en légère perte nette (5 % de sa valeur intégrée) : la friche herbacée initiale, même dégradée par une espèce envahissante, valait autant que les aménagements une fois mûrs. La biodiversité grise pèse plus de 200 fois la perte du site et dix fois la valeur intégrée du site entier : 60 % par le climat, 39 % par le bois d'origine non justifiée. Justifier une coupe sélective (MSA 0,70) ramènerait Inat_bois de 55 556 à 33 333 m²HE·an.
