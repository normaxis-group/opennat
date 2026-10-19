# Dossier de soumission de la méthode OpenNAT 1 au Biodiversity Standard Council

NORMATYS, éditeur de la méthode. Méthode OpenNAT 1 (révision du 19 octobre 2026), données 1.2.2, moteur 0.2.0. Projet de dossier du 19 octobre 2026, non transmis.

## Objet de la demande

NORMATYS soumet au Biodiversity Standard Council la méthode de calcul OpenNAT 1 et lui demande trois choses : valider la méthode et ses 70 conventions, ou dire lesquelles reprendre ; trancher les dix décisions ci-dessous, dont trois portent sur la biodiversité grise et changent les résultats ; fixer les seuils, aujourd'hui proposés. Tant que le conseil ne s'est pas prononcé, la méthode, ses seuils et ses résultats ne sont pas opposables, et chaque sortie du moteur le dit.

Le dossier ne reprend pas le texte de la méthode. Il renvoie à ses pièces : texte de la méthode (24 pages), édition complète (2 149 pages : données conventionnelles, 58 fiches algorithmes, 191 fiches habitats, fiches d'application, protocoles de relevé, récapitulatif standardisé, cas de validation), guide utilisateur, guide du contributeur, journal des versions, contrôle d'ordre de grandeur face à l'étude Carbone 4. Le moteur libre et ses tables sont dans le dépôt de la méthode.

## La méthode en bref

OpenNAT compare sur 50 ans la valeur écologique d'un site avant et après un projet de construction, en m²HE·an (un m²HE est un mètre carré d'habitat de qualité 1), et y ajoute la nature consommée ailleurs par les matériaux et le chantier. Quatre indicateurs : Cnat, consommation de nature sur le site ; Inat, biodiversité grise ; Snat = -(Cnat + Inat), solde de nature ; Bnat, coefficient de biotope de l'état projet. Le calcul suit le climat du site heure par heure sous la trajectoire de réchauffement de référence (bilan hydrique, éclairage nocturne, maturation des plantations, gestion après livraison, calendrier du chantier) et donne l'intervalle de chaque indicateur par 1 000 tirages.

Chaque nombre employé par le calcul est une ligne de table avec sa source : 2 274 valeurs dans 15 tables, dont 92 % lues dans une source primaire ou transposées d'une source primaire, et 8 % fixées par convention. Les 70 conventions se répartissent en 37 transpositions d'une source faite pour un autre objet, 28 valeurs de secours et 5 constats de source muette. L'annexe A les liste toutes.

## Ce qui a été vérifié

| Contrôle | Résultat |
|---|---|
| Huit situations types du cahier des charges, calculées par un carnet de référence écrit sans aucun code commun avec le moteur | le moteur retrouve le carnet à 0,1 % sur les huit situations, l'exemple de l'annexe C et 60 cas complémentaires, unité par unité et année par année |
| Non-régression | 38 930 grandeurs figées ; toute évolution doit être inscrite au journal des versions |
| Propriétés | 20 propriétés vérifiées (ajouter de la pleine terre ne dégrade pas Cnat, un chantier plus long ne le réduit pas, un plan de gestion plus long ne le dégrade sur aucun des tirages, etc.) |
| Cohérence des unités | 45 équations des fiches vérifiées automatiquement à partir des unités inscrites dans les tables ; une erreur d'étiquette trouvée et corrigée |
| Ordre de grandeur de la biodiversité grise | face à l'étude Carbone 4 (octobre 2026), au m² de plancher et au périmètre commun : 54 m²HE·an contre 44 PDF.m².yr, rapport de 1,0 à 1,5 |

L'analyse d'incertitude de l'exemple de l'annexe C désigne les paramètres qui pèsent le plus sur Snat : le facteur de caractérisation du climat (C-G2), le produit délai par vitesse de la maturation (C-M1), la production biologique des forêts et le rapport bois rond par produit (C-G4), puis la fraction de réserve facilement utilisable des arbustes (C-W6). Les décisions D1, D4 et D7 portent sur ces conventions.

## Décisions demandées

| N° | Objet | Conventions | Recommandation de l'éditeur |
|---|---|---|---|
| D1 | Recalibrage du bois | C-G4, C-G5 | option O2 dès maintenant ; O3 quand la source du rendement alloué aura été lue en entier |
| D2 | Occupation des usines | C-G7 | garder l'écart, le chiffrer et l'afficher ; pas de proxy |
| D3 | Pollution dans la biodiversité grise | C-G8 | intégrer l'eutrophisation terrestre par GLOBIO, publier les eutrophisations en espèce·an, ouvrir le chantier de l'écotoxicité |
| D4 | Facteur de caractérisation du climat | C-G2 | confirmer, avec sa plage |
| D5 | Seuils de Bnat, de pleine terre et de niveau ; pas de seuil d'Inat ni de Snat | C-E6, C-E7 | confirmer pour une période d'essai de deux ans |
| D6 | Valeurs d'habitat et grilles d'état | C-H1 à C-H8 | confirmer sous réserve de la relecture par un écologue |
| D7 | Maturation et gestion | C-M1 à C-M3 | confirmer |
| D8 | Climat futur | C-W1, C-W3, C-W13 | confirmer |
| D9 | Période de 50 ans sans actualisation | C-T1, C-T5 | confirmer |
| D10 | Gouvernance des versions et des contributions | | adopter les règles du guide du contributeur |

### D1. Recalibrage du bois

Avec les conventions actuelles, un bâtiment entièrement en bois a une biodiversité grise six fois plus forte que le même bâtiment en béton (cas 7 : 1 867 574 contre 301 754 m²HE·an). Le sens de l'écart est celui de la littérature ; son ampleur tient à deux conventions. C-G4 compte 2 m³ de bois rond par m³ de produit, c'est-à-dire toute la grume, sciure et plaquettes comprises, au produit. C-G5 compte la forêt exploitée à la perte de MSA de son régime (0,5 pour la coupe rase), soit 53 % de la perte d'une carrière (0,95).

Deux corrections sont possibles, chacune appuyée sur des sources :

- O1, rendement alloué : 1,15 m³ de bois rond par m³ de sciage, quand plaquettes, sciure et écorces portent leur part, comme le font les déclarations environnementales de produits en bois (EN 16485, qui renvoie à l'EN 15804 pour l'allocation). L'opérateur norvégien EPD-Norge relève deux pratiques, environ 1,15 et environ 1,7 m³ selon l'endroit de la chaîne où l'allocation se fait. Cette valeur a été lue dans un extrait ; la note complète est à lire avant adoption. Sans allocation, les facteurs de conversion de la CEE-ONU donnent un sciage d'environ la moitié du bois rond (Allemagne 1,67 ; Royaume-Uni 2,00), ce qui confirme la valeur actuelle de 2 pour la grume entière.
- O2, pondération relative : la perte d'une forêt exploitée est fixée par rapport à celle d'une carrière au rapport que donnent les méthodes d'ACV. LC-IMPACT v2 pour la France donne 0,23 (forêt intensive face à un site d'extraction minérale), ReCiPe 2016 0,41 (forêt gérée face à une surface artificielle), EF 3.1 pour la France 0,38. Avec la médiane, 0,38, la perte de la coupe rase passe de 0,50 à 0,36 ; les autres régimes suivent dans la même proportion (plantation 0,51, coupe sélective 0,22, exploitation à faible impact 0,11).

| Option | Inat 7a béton | Inat 7b bois non justifié | Rapport 7b / 7a | Rapport 7c / 7a | Exemple de l'annexe C | m²HE·an par m³ de coupe rase |
|---|---|---|---|---|---|---|
| O0, actuel | 301 754 | 1 867 574 | 6,2 | 4,0 | 141 843 | 1 852 |
| O1, rendement alloué | 286 013 | 1 159 241 | 4,1 | 2,7 | 118 232 | 1 065 |
| O2, pondération relative | 291 487 | 1 405 574 | 4,8 | 3,2 | 126 443 | 1 339 |
| O3, O1 et O2 | 280 109 | 893 591 | 3,2 | 2,2 | 109 377 | 770 |

Face à Carbone 4, l'option O3 rapproche les deux calculs : la hausse d'usage des sols de leur variante biosourcée (54 860 PDF.m².yr) correspond à 71 m³ de bois en O3, contre 30 m³ aujourd'hui, pour une variante dont le seul parquet massif fait 34 à 48 m³. Même en O3, le bâtiment tout bois reste trois fois au-dessus du béton, parce que l'occupation des forêts reste comptée et que celle des usines ne l'est pas (D2).

Recommandation : adopter O2, dont les trois sources ont été lues ; adopter O3 dès que la note d'EPD-Norge et les facteurs de conversion de la CEE-ONU auront été lus en entier.

### D2. Occupation des usines

C-G7 néglige l'occupation des sols des cimenteries, aciéries, verreries et usines d'isolants, faute d'inventaire ouvert. C'est ce qui avantage le béton. Face à Carbone 4, l'usage des sols de leur bâtiment béton vaut environ 10 PDF.m².yr par m² de plancher ; OpenNAT en compte 11, dont 9 pour les 15 m³ de bois supposés et 2 pour les carrières, les usines restant à zéro. Si l'usage des sols de Carbone 4 tient surtout aux matériaux minéraux et métalliques, comme l'étude l'indique pour le béton, il manque à OpenNAT de l'ordre de 8 m²HE·an par m². Un facteur proportionnel aux émissions comblerait l'écart en moyenne mais effacerait toute différence entre matériaux d'empreinte carbone égale.

Recommandation : garder l'écart en v1, l'afficher avec cet ordre de grandeur dans la fiche de synthèse, et chercher un inventaire ouvert des emprises industrielles par tonne produite (registres d'installations classées, déclarations d'émissions des sites).

### D3. Pollution dans la biodiversité grise

Le RSEE porte cinq indicateurs de pollution : acidification (106, mol H+ éq.), eutrophisation des eaux douces (107, kg P éq.), marine (108, kg N éq.) et terrestre (109, dépassement cumulé, mol N éq.), écotoxicité pour l'eau douce (116, CTUe). OpenNAT les affiche à part, sans conversion (C-G8). Chez Carbone 4, la pollution fait 51 % de la biodiversité grise d'un bâtiment béton.

Sur neuf bâtiments de RSEE réels du groupe, les médianes par m² de surface de référence (phases A à C) sont : 805 kg CO2 éq., 0,21 mol H+ éq., 0,0081 kg P éq., 0,037 kg N éq., 0,38 mol N éq., 2,4 CTUe. Trois voies sourcées ont été chiffrées sur ce bâtiment médian :

| Voie | Source | Poids face au climat |
|---|---|---|
| P2, eutrophisation terrestre dans Inat | GLOBIO 3.5, tableau 4.1 : MSA = 1 - 0,220 ln(NE + 1) pour les forêts, NE étant l'azote déposé au-delà de la charge critique (g/m²/an) ; l'indicateur 109 mesure ce même excès, d'où 3,1 m²HE·an par mol N éq. | 0,6 à 1,2 m²HE·an par m², soit 0,8 à 1,6 % du climat |
| P3, eutrophisations en espèce·an, à part | ReCiPe 2016, facteurs de passage à l'effet : 6,7 × 10⁻⁷ par kg P éq., 1,7 × 10⁻⁹ par kg N éq. (mêmes unités que 107 et 108) | 0,24 % du climat en espèce·an |
| P4, forfait calé sur Carbone 4 | rapport pollution sur climat de leur bâtiment béton (51 / 38) | ajoute 1,34 fois le climat |

Le constat est net : les facteurs ouverts lus ne retrouvent pas la part de Carbone 4. Celle-ci tient à l'écotoxicité et à l'acidification, pour lesquelles aucun facteur ouvert ne part des unités du RSEE (CTUe, mol H+ éq.). Le forfait P4 reposerait sur une seule étude, sans licence, et rendrait la pollution proportionnelle au carbone : il est écarté.

Recommandation : intégrer P2 dans Inat (pont sourcé, faible poids, même unité) ; publier P3 en indicateur complémentaire ; ouvrir le chantier de l'écotoxicité, en partant de la conversion des unités toxiques comparatives (CTUe) en fraction d'espèces que pratique IMPACT World+ ; ne fixer aucun seuil d'Inat ni de Snat avant ce travail.

### D4. Facteur de caractérisation du climat

CF = 1,807 × 10⁻³ m²HE par kg CO2 éq., perdus chaque année tant que le réchauffement persiste (surface des terres émergées hors glaces et hors cultures du GIEC, perte de MSA par degré de GLOBIO divisée par 2 pour le retard de réponse, TCRE du sixième rapport du GIEC). C'est le paramètre le plus influent de la méthode ; sa plage va de 5,4 × 10⁻⁴ à 5,2 × 10⁻³. La perte par degré est la médiane non pondérée des 15 biomes de GLOBIO, faute de surfaces de biomes publiées sous licence libre. Face à Carbone 4, le climat d'OpenNAT et celui d'IMPACT World+ coïncident pour une empreinte de 480 kg CO2 éq./m² en A1-A3, plausible pour un bâtiment béton.

Recommandation : confirmer, et remplacer la médiane par une moyenne pondérée par surface dès qu'une source libre des surfaces de biomes existe.

### D5. Seuils

Bnat minimal selon la typologie et la part d'emprise (45, 35 ou 25 points en logement ; 25 en tertiaire ; pas de seuil en industrie et aménagement), raccordé au coefficient de biotope du référentiel Effinature 8.1 ; pleine terre d'au moins 15 % de l'emprise totale du projet ; niveau 1 du site pour Cnat nul ou négatif, niveau 2 pour un gain d'au moins 10 % de la valeur initiale intégrée. Inat et Snat n'ont pas de seuil : ils seront fixés sur la distribution d'opérations réelles, comme ceux de l'Ic construction, et après D3.

Recommandation : confirmer pour une période d'essai de deux ans, et revoir les seuils sur les opérations calculées pendant cette période.

### D6. Valeurs d'habitat et grilles d'état

Les valeurs intrinsèques sont les valeurs de biotope de l'annexe 2 de l'ordonnance fédérale allemande de compensation (BKompV) ramenées à 1 (C-H1) ; les grilles d'état sont celles de la métrique statutaire anglaise, traduites (C-H6) ; les types sans équivalent allemand (toitures, façades, jardinières) reçoivent la distinctivité anglaise (C-H3). Ces transpositions touchent 191 types d'habitat et plus de 400 lignes de données.

Recommandation : confirmer, sous réserve de la relecture des 191 fiches habitats et des grilles par un écologue ; les corrections passeraient par le guide du contributeur.

### D7. Maturation et gestion

Un milieu créé mûrit selon une courbe de Chapman-Richards ramenée à 1 au délai de la métrique anglaise (C-M1) ; un milieu herbacé abandonné prend la valeur de sa variante non entretenue de la BKompV (C-M2) ; sans plan de gestion déclaré, la gestion courante commence à la livraison (C-M3), une prairie tondue valant comme un gazon d'agrément. Sur l'exemple de l'annexe C, un plan de gestion de 50 ans ramène Cnat de 3 217 à 1 476 m²HE·an, sur chacun des tirages : la gestion pèse plus que le choix des espèces.

Recommandation : confirmer ; c'est la décision qui a le plus d'effet sur les projets, et elle récompense un engagement vérifiable à l'achèvement.

### D8. Climat futur

Le calcul emploie les fichiers climatiques prospectifs libres de l'ADEME, de Météo-France, du CSTB et de la DHUP (C-W1), et non la météo conventionnelle de la RE2020, réservée au calcul réglementaire ; leurs pluies sont recalées sur les normales 1991-2020, leur note technique reconnaissant des cumuls proches des maxima (C-W3) ; chaque année de la période reçoit le niveau de réchauffement de la trajectoire de référence pour l'adaptation (C-W13).

Recommandation : confirmer.

### D9. Période et actualisation

Période de 50 ans, celle de l'ACV de la RE2020, avec une sortie à 30 ans pour la comparaison avec la métrique anglaise et les méthodes allemandes (C-T1) ; aucune actualisation, le délai de maturation étant déjà compté (C-T5).

Recommandation : confirmer.

### D10. Gouvernance

Le guide du contributeur propose : chaque valeur avec sa source, sur un format de treize colonnes ; décision d'intégrer une valeur par l'éditeur, NORMATYS ; toute convention nouvelle et tout seuil soumis au conseil ; une version des données identifiée par l'empreinte de ses tables et inscrite au journal des versions ; une méthode qui ne change d'équation qu'en changeant de numéro. La publication du texte et des tables sous CC BY 4.0 et du moteur sous AGPL suppose que la licence entre NORMATYS et IRICE soit compatible avec une diffusion libre.

Recommandation : adopter ces règles.

## Calendrier proposé

| Étape | Contenu |
|---|---|
| Séance 1 | présentation de la méthode et des vérifications ; décisions D4, D6 à D9 |
| Entre les séances | lecture des sources du rendement alloué ; relecture écologue des fiches habitats ; travail sur l'écotoxicité |
| Séance 2 | décisions D1 à D3, D5 et D10 ; validation de la version OpenNAT 1 avec les données qui en résultent |
| Après validation | publication de la méthode, des tables et du moteur ; période d'essai des seuils |

## Annexe A. Les 70 conventions

Statut de chacune : proposée, en attente de validation du Biodiversity Standard Council. La lettre du numéro donne la famille (H habitats, S sols, E contexte, eau et seuils, C connectivité, N nuisances, T temps, G biodiversité grise, R relevés, I incertitude, B Bnat, P permis de construire, W bilan hydrique et climat, L éclairage, M maturation et gestion, K calendrier du chantier). Catégorie : transposition d'une source faite pour un autre objet, valeur de secours, ou constat de source muette. Lignes : nombre de lignes de données qui l'appliquent. L'énoncé complet et le motif de chaque convention sont dans la partie 9 de l'édition complète.

| N° | Catégorie | Lignes | Énoncé |
|---|---|---|---|
| C-H1 | transposition | 185 | La valeur intrinsèque d'un habitat, en m²HE par m², est la valeur de biotope de l'annexe 2 de la BKompV (ordonnance fédérale allemande de compensation, 2020) divisée par 24, valeur maximale de l'échelle. |
| C-H2 | transposition | 3 | Le facteur d'état vaut f = 0,5 + 0,5 x S, où S est le score de la grille de critères, entre 0 et 1. |
| C-H3 | transposition | 9 | Les types sans équivalent dans la BKompV (toitures végétalisées VB.11 à VB.13, façades VB.15 et VB.16, jardinières VB.23) reçoivent la distinctivité de la métrique statutaire anglaise ramenée à 1 (divisée par 8), multipliée par le rapport médian entre les deux échelles. |
| C-H4 | source muette | 0 | La métrique anglaise traite les cours d'eau dans un module linéaire distinct et ne leur donne ni délai ni difficulté surfaciques. |
| C-H5 | transposition | 144 | Pour les types ligneux, la BKompV distingue trois stades : jeune (J), moyen (M) et âgé (A). |
| C-H6 | transposition | 88 | Les grilles d'état sont celles des fiches d'évaluation de la métrique statutaire anglaise (juillet 2025), traduites et adaptées. |
| C-H7 | secours | 1 | La valeur d'un m² ne peut dépasser 1,15 m²HE, quel que soit le produit des facteurs. 1,15 est le plus fort multiplicateur de la métrique anglaise (importance stratégique ou connectivité élevée). |
| C-H8 | transposition | 10 | Les critères anglais renvoient aux espèces de l'annexe 9 du Wildlife and Countryside Act 1981 et, pour la grille urbaine, aux autres espèces nuisibles à la faune indigène « selon le jugement professionnel ». |
| C-S1 | transposition | 16 | Le coefficient de chaque nature de surface (`donnees/sols.csv`) est la médiane des coefficients publiés par les grilles de coefficient de biotope lues à la source : Berlin (facteurs des plans fixés après décembre 2019), Londres (Urban Greening Factor 2023), Strasbourg (PLU, article 9.2), Grand Annecy (PLUi-HMB), Paris (indice de (…) |
| C-S2 | transposition | 0 | Dans le calcul de la valeur d'habitat (module H), le coefficient de sol ne s'applique qu'aux unités d'un type d'habitat au sol posées sur dalle : une pelouse sur 40 cm de substrat vaut 0,7 fois une pelouse en pleine terre. |
| C-E1 | transposition | 3 | Le multiplicateur de situation de la métrique anglaise (importance stratégique 1,15, 1,10 ou 1) s'applique à la trame verte et bleue française : 1,15 dans un réservoir de biodiversité identifié par le SRADDET, le SRCE ou le PLU (article R. 371-19 du code de l'environnement), 1,10 dans un corridor identifié, 1 ailleurs. |
| C-E2 | source muette | 4 | Aucune source ne module les délais de maturation par zone biogéographique en France. |
| C-E3 | secours | 3 | La somme des surfaces des unités au sol doit égaler la surface de la parcelle à 0,5 % près, et au moins à 1 m² près. |
| C-E4 | transposition | 2 | Un milieu en eau alimenté artificiellement (réseau d'eau potable, pompage) avec une eau non traitée voit sa valeur multipliée par 0,8. |
| C-E5 | transposition | 1 | La part des eaux pluviales infiltrées ou gérées à ciel ouvert est un indicateur complémentaire. |
| C-E6 | transposition | 7 | Les seuils de Bnat sont ceux du coefficient de biotope par surface harmonisé du référentiel Effinature 8.1 (critère SOL 01.2.5), appliqués à Bnat / 100 : logements et équipements d'intérêt collectif, 45 si l'emprise du bâti va jusqu'à 37 %, 35 de 38 à 49 %, 25 au-delà ; commerces, bureaux et hébergements avec services, 25. |
| C-E7 | transposition | 2 | Deux niveaux pour le site : niveau 1, absence de perte nette (Cnat au plus 0) ; niveau 2, gain net d'au moins 10 % de la valeur initiale intégrée sur 50 ans, transposé de l'objectif anglais (Town and Country Planning Act 1990, Schedule 7A, paragraphe 2(3)). |
| C-C1 | transposition | 3 | Facteur de taille d'une tache d'habitat : k = (A / A_ref)^z, borné entre 0,35 et 1. z = 0,22 (îles d'habitat, Matthews et al. 2016). |
| C-C2 | transposition | 5 | Multiplicateur de connectivité de la métrique anglaise : 1,15 pour une tache contiguë à un réservoir, à un corridor ou à un espace naturel extérieur d'au moins 1 ha ; 1,10 si un tel espace est à moins de 200 m, bord à bord, sans obstacle infranchissable ; 1 ailleurs. |
| C-C3 | source muette | 3 | Une tache entièrement close par une clôture sans passage pour la petite faune voit sa valeur multipliée par 0,9. |
| C-N1 | secours | 4 | Trois classes d'éclairage par unité : L0, aucun point lumineux à moins de 50 m (facteur 1) ; L1, éclairage conforme à l'arrêté du 27 décembre 2018 et éteint en milieu de nuit (0,9) ; L2, éclairage non conforme ou permanent (0,75). |
| C-N2 | transposition | 3 | Une unité exposée à un niveau sonore supérieur à 47 dB(A) en milieu ouvert, ou à 42 dB(A) en milieu boisé, voit sa valeur multipliée par 0,7, d'après la baisse de densité d'oiseaux nicheurs d'au moins 30 % au-delà de ces seuils (Reijnen et al. 1997). |
| C-N3 | source muette | 3 | Une unité végétalisée à moins de 15 m d'une façade qui expose plus de 10 m² de vitrage non traité contre les collisions voit sa valeur multipliée par 0,95. |
| C-T1 | transposition | 2 | Simulation au pas annuel sur la période de référence de 50 ans de l'ACV de la RE2020 (annexe II de l'arrêté du 4 août 2021), avec une sortie complémentaire à 30 ans. |
| C-T2 | transposition | 191 | Le délai « 30+ » de la métrique anglaise vaut 32 ans : c'est l'année que la table des multiplicateurs temporels de l'onglet G-4 associe à « 30+ ». |
| C-T3 | transposition | 0 | Les types minéraux et scellés (VB.1 à VB.4, VB.25, H5.6), pour lesquels la métrique anglaise ne prévoit aucun délai, atteignent leur valeur dès la fin du chantier. |
| C-T4 | secours | 1 | Une unité conservée perd 25 % de sa valeur pendant la durée du chantier quand aucune mesure de protection (clôture, balisage, interdiction de stockage et de circulation) n'est prévue. |
| C-T5 | transposition | 1 | Taux d'actualisation nul. |
| C-T6 | secours | 1 | La réfection d'une unité (toiture végétalisée refaite, par exemple) annule sa valeur pendant un an, puis la maturation reprend depuis 0. |
| C-T7 | transposition | 0 | La difficulté de création ou d'amélioration de la métrique anglaise (1 ; 0,67 ; 0,33 ; 0,1) multiplie la valeur cible d'un habitat créé ou amélioré : elle exprime le risque d'échec. |
| C-G1 | transposition | 0 | Inat porte sur les contributeurs « composants » et « chantier » de l'ACV de la RE2020, tels que le RSEE les donne (branche RSEnv). |
| C-G2 | transposition | 6 | Facteur de caractérisation du climat, en m²HE par kg CO2 éq. (habitat équivalent perdu chaque année tant que le réchauffement dû à ce kg persiste ; multiplié par la durée de persistance en années, il donne des m²HE·an) : CF = S_terres x (1 - p) x (perte de MSA par °C / 2) x TCRE = 1,30e14 x 0,87 x (0,071 / 2) x 4,5e-16 = 1,807e-3. |
| C-G3 | secours | 4 | Une émission pèse sur le reste de la période de référence : 50 ans pour la production et le chantier (A1 à A5), 25 ans en moyenne pour l'exploitation des composants (B), 0 pour la fin de vie (C). |
| C-G4 | transposition | 2 | Occupation des sols du bois : 10 000 / P x R m²·an par m³ de produit, avec P = 5,4 m³ par ha et par an (production biologique moyenne des forêts françaises, IGN 2024) et R = 2 m³ de bois rond par m³ de produit (valeur de secours, plage 1,5 à 3,1). |
| C-G5 | transposition | 4 | La qualité d'habitat de la forêt d'origine dépend du régime déclaré (GLOBIO 3.5, table 2.2) : plantation 0,30, coupe rase 0,50, coupe sélective 0,70, exploitation à faible impact 0,85. |
| C-G6 | secours | 2 | Occupation des sols des granulats et roches : 0,9 m²·an par tonne (médiane de quatre carrières françaises, plage 0,3 à 1,6), avec une qualité d'habitat de 0,05 (classe la plus artificialisée de GLOBIO, aucune classe carrière n'existant). |
| C-G7 | source muette | 1 | L'occupation des sols des usines (acier, verre, plastiques, isolants minéraux, plâtre) est négligée en v1, faute d'inventaire ouvert. |
| C-G8 | transposition | 1 | Les indicateurs de pollution du RSEE (acidification 106, eutrophisation 107 à 109, écotoxicité pour l'eau douce 116) sont repris tels quels et affichés à part, en unités de l'annexe II, faute de conversion sourcée vers la MSA. |
| C-R1 | secours | 0 | Les critères floristiques se relèvent pendant la période où les espèces caractéristiques sont identifiables : en plaine, d'avril à juillet pour les prairies et pelouses, de mai à septembre pour les zones humides et mégaphorbiaies. |
| C-R2 | secours | 0 | Les couverts et les nombres d'espèces par m² s'estiment sur au moins 5 quadrats de 1 m² par hectare, répartis sur un transect en W, et au moins 3 par unité de moins d'un hectare. |
| C-R3 | secours | 0 | Les indicateurs de la grille des boisements se notent sur placettes de 10 m de rayon, au moins une par hectare et au moins trois par unité. |
| C-R4 | secours | 0 | Les jardins privatifs d'une même opération se relèvent par échantillon d'au moins un jardin sur cinq ; les haies, par tronçons homogènes de 100 m au plus. |
| C-R5 | secours | 0 | Un état initial dégradé volontairement dans les deux ans précédant le dépôt du permis (débroussaillage, labour, décapage) se saisit avec l'état antérieur documenté, pour ne pas récompenser une destruction préalable. |
| C-I1 | secours | 0 | Quand la source ne donne pas d'incertitude, la plage d'une valeur est de ± 10 % pour un texte réglementaire ou un outil officiel, ± 25 % pour un jugement d'expert publié, ± 50 % pour une convention OpenNAT. |
| C-I2 | secours | 7 | L'analyse d'incertitude tire au moins 1 000 jeux de valeurs, chaque valeur suivant une loi triangulaire (borne basse, valeur centrale, borne haute). |
| C-B1 | transposition | 1 | Bnat = 100 x (somme des surfaces x coefficient de sol + bonus d'infiltration) / surface de la parcelle. |
| C-P1 | transposition | 0 | Comme l'attestation de la RE2020 au dépôt du permis de construire, qui ne demande que le Bbio, l'attestation OpenNAT au permis porte sur les seules données du plan masse : Bnat et son seuil, le taux de pleine terre et, quand le PLU impose un coefficient de biotope ou une part de pleine terre, la comparaison avec ce minimum. |
| C-W1 | transposition | 26 | Le climat du calcul est l'année type horaire des fichiers climatiques prospectifs publiés en juin 2025 par l'ADEME, Météo-France, le CSTB et la DHUP (Licence Ouverte 2.0), à la station de référence de la zone climatique RE2020 du projet (H1a Trappes, H1b Nancy, H1c Mâcon, H2a Rennes, H2b Tours, H2c Agen, H2d Carpentras, H3 Marignane). |
| C-W2 | transposition | 38 | L'évapotranspiration de référence horaire suit l'équation 53 de la FAO-56 (gazon de référence, résistance de surface de 70 s/m). |
| C-W3 | secours | 96 | La note technique des fichiers prospectifs indique que leurs cumuls de pluie sont proches des maxima des simulations, pas des médianes. |
| C-W4 | secours | 19 | La réserve utile d'un sol en pleine terre se calcule avec les teneurs en eau à la capacité au champ et au point de flétrissement du tableau 19 de la FAO-56 (milieu de plage) pour la classe de texture déclarée par le bureau d'études, et avec la profondeur d'enracinement, bornée par la profondeur de sol. |
| C-W5 | secours | 1 | L'eau utile d'un substrat de toiture ou de dalle vaut 0,20 m³ par m³ (plage 0,12 à 0,30) quand le fabricant ne la déclare pas. |
| C-W6 | transposition | 34 | Chaque unité végétalisée appartient à un groupe hydrique (fiche A47) : gazon, prairie, végétation xérophile, arbustif, arboré, conifères, toiture extensive, milieu humide alimenté par la pluie, mare. |
| C-W7 | transposition | 2 | La saison de végétation est l'ensemble des heures où la moyenne des températures des six jours précédents dépasse 5 °C, d'après l'indice de durée de la saison de croissance de l'ETCCDI. |
| C-W8 | transposition | 1 | Le stress hydrique d'une unité est l'indice de Granier et al. (1999), établi pour les peuplements forestiers : somme, sur la saison de végétation, de (0,4 - REW) / 0,4 quand la réserve extractible relative REW passe sous 0,4. |
| C-W9 | secours | 11 | Le facteur hydrique vaut k_W = max(0,5 ; 1 - beta x (IS - IS_ref - 5) / 100), où IS_ref est l'indice du même groupe dans la situation de référence de la zone : limon d'un mètre (substrat de 10 cm pour une toiture extensive), sans arrosage ni apport, année type France +2 °C. |
| C-W10 | secours | 2 | Une unité déclarée arrosée reçoit chaque nuit, en saison de végétation, l'eau qui ramène sa réserve à la capacité au champ dès que la réserve extractible relative passe sous 0,5. |
| C-W11 | secours | 7 | Une mare a par défaut 0,8 m de profondeur et un fond argileux qui laisse s'infiltrer 0,3 mm par jour (fond étanche : 0 ; fond naturel : 1 mm par jour). |
| C-W12 | secours | 3 | Une mare à sec à un moment quelconque entre le 1er mars et le 30 juin manque la reproduction des amphibiens de l'année : sa valeur est multipliée par 0,5 pour l'année type concernée. |
| C-W13 | transposition | 6 | Chaque année civile de la période reçoit le niveau de réchauffement de la trajectoire de référence pour l'adaptation au changement climatique (TRACC, arrêté du 23 janvier 2026) : +2 °C en 2030, +2,7 °C en 2050, +4 °C en 2100, interpolation linéaire entre ces jalons, +2 °C avant 2030. |
| C-L1 | secours | 4 | Le facteur d'éclairage d'une unité vaut k_L = 1 - 0,25 x x_nuit x s x g, où x_nuit est la part des heures de nuit de la saison d'activité des chiroptères pendant lesquelles l'éclairage est allumé, s le facteur spectral et g le facteur de distance. |
| C-L2 | secours | 7 | La saison d'activité des chiroptères va d'avril à octobre. |
| C-L3 | transposition | 2 | Le facteur de distance vaut 1 jusqu'à 10 m du luminaire le plus proche, 0 au-delà de 50 m, et décroît linéairement entre les deux, d'après les distances d'attraction et d'évitement mesurées par Azam et al. (2018) sur six espèces et deux genres de chiroptères. |
| C-L4 | secours | 12 | Le facteur spectral croît avec la température de couleur : 0,5 en ambre (1 800 K), 0,6 à 2 200 K, 0,7 à 2 400 K, 0,8 à 2 700 K, 0,9 à 3 000 K, 1 à 4 000 K et au-delà, interpolé entre ces points. |
| C-M1 | transposition | 4 | La maturation d'un milieu créé suit une courbe de Chapman-Richards (Richards, 1959 ; Pienaar et Turnbull, 1973) ramenée à 1 au délai de maturité d de la métrique anglaise : g(tau) = [(1 - e^(-3 tau / d)) / (1 - e^(-3))]^c. |
| C-M2 | transposition | 15 | Un milieu herbacé dont l'entretien cesse prend, après deux ans, la valeur de sa variante abandonnée dans l'annexe 2 de la BKompV (rapport du type « brachgefallen » au type exploité, onze couples de 0,73 à 0,91, moyenne appliquée aux types sans couple), puis devient après quinze ans une friche arbustive (VB.9) en état moyen (score 0,75). |
| C-M3 | secours | 0 | Le plan de gestion écologique déclaré couvre un nombre d'années compté depuis la livraison. |
| C-K1 | secours | 37 | La destruction d'une unité de l'état initial pendant une période sensible ajoute à Cnat sa valeur pendant une année, multipliée par la sensibilité du mois de destruction : oiseaux nicheurs (ligneux, prairies et friches) du 16 mars au 15 août, d'après la BCAE 8 de la conditionnalité de la PAC ; chiroptères (arbres âgés, gîtes déclarés) (…) |
| C-K2 | secours | 13 | Les plantations et les semis se font de novembre à mars, au plus tôt deux mois avant la fin du chantier : la maturation d'un milieu planté ou semé commence au premier mois favorable. |
| C-K3 | secours | 2 | La période de 50 ans commence au premier mois du chantier, déclaré par son année et son mois (à défaut, janvier 2027). |

## Annexe B. Sources lues pour ce dossier

| Source | Emploi | État de lecture |
|---|---|---|
| IGN, Mémento de l'inventaire forestier, édition 2024, p. 36 à 39 | production biologique (5,4 m³/ha/an) et prélèvements (53,1 Mm³/an, 60 % de la production) | lu |
| LC-IMPACT v2.0, facteurs d'usage des sols, France (Zenodo 18670560) | rapport forêt intensive sur site d'extraction, 0,23 | lu par l'audit |
| ReCiPe 2016 v1.1, tableur des facteurs (RIVM) | rapport forêt gérée sur surface artificielle, 0,41 ; facteurs d'effet des eutrophisations | lu |
| EF 3.1, usage des sols, France | rapport forêt intensive sur site d'extraction, 0,38 | lu par l'audit |
| GLOBIO 3.5, description technique (PBL 2016), tableau 4.1 | effet du dépôt d'azote en excès sur la MSA | lu |
| Arrêté du 4 août 2021, annexe II | unités des indicateurs 106 à 109 et 116 | lu |
| EPD-Norge, note du 1er mars 2024 sur les pratiques divergentes pour les produits en bois | rendement alloué de 1,15 m³ de bois rond par m³ de sciage | extrait seulement, document à lire |
| CEE-ONU et FAO, facteurs de conversion des produits forestiers | rendement matière du sciage (environ la moitié du bois rond) | extrait seulement, le site refuse la lecture automatique |
| Carbone 4, « La biodiversité grise dans le bâtiment », octobre 2026 | ordre de grandeur et parts par pression | lu en entier par l'audit |
