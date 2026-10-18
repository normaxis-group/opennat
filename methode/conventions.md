# Conventions de la méthode OpenNAT v1

Une convention est une règle ou une valeur que OpenNAT fixe parce qu'aucune source ne la donne telle quelle. Chacune est numérotée, citée dans le texte de la méthode et dans la colonne `convention` des tables de `donnees/`, et soumise au Biodiversity Standard Council avec la méthode. Toutes sont « proposées, en attente de validation ».

Familles : H habitats, S sols, E contexte, eau et seuils, C connectivité, N nuisances, T temps, G biodiversité grise, R relevés, I incertitude, B Bnat, P attestation au permis de construire.

Les conventions jouent le rôle des fiches d'application de la méthode Th-BCE : elles disent comment appliquer la méthode là où les sources se taisent. Le registre suit les trois catégories du registre des lectures d'OpenBCE : source muette (aucune source ne traite le point), convention de transposition (une source traite le point dans un autre cadre et la valeur est transposée), valeur de secours (une valeur est posée faute de mieux, avec une plage large).

## Habitats

### C-H1
Catégorie : convention de transposition.
La valeur intrinsèque d'un habitat, en m²HE par m², est la valeur de biotope de l'annexe 2 de la BKompV (ordonnance fédérale allemande de compensation, 2020) divisée par 24, valeur maximale de l'échelle. Le type BKompV est choisi par une correspondance écrite, type par type, dans `donnees/nomenclature_habitats.csv`, avec sa justification. La BKompV est la seule liste qui soit à la fois réglementaire, libre de droits (§ 5 de la loi allemande sur le droit d'auteur), fine en milieu urbain et graduée par stade d'âge (audit, point P2). Chaque correspondance est une lecture : elle peut être contestée ligne par ligne sans toucher à la méthode.

### C-H2
Catégorie : convention de transposition.
Le facteur d'état vaut f = 0,5 + 0,5 x S, où S est le score de la grille de critères, entre 0 et 1. La valeur intrinsèque retenue est celle de la variante en bon état du type BKompV (riche en espèces, exploitée extensivement, avec arbres anciens quand le type le distingue). Le facteur d'état ramène un habitat dégradé vers la moitié de cette valeur, ce qui reproduit l'écart observé dans la BKompV entre variantes riches et pauvres d'un même type (prairie fraîche riche 20, pauvre 8 à 11). Les classes affichées pour l'écologue sont : bon état si S est au moins 0,85, état moyen de 0,65 à 0,85, mauvais état sous 0,65. Ces classes choisissent aussi le délai de maturité de la métrique anglaise.

### C-H3
Catégorie : convention de transposition.
Les types sans équivalent dans la BKompV (toitures végétalisées VB.11 à VB.13, façades VB.15 et VB.16, jardinières VB.23) reçoivent la distinctivité de la métrique statutaire anglaise ramenée à 1 (divisée par 8), multipliée par le rapport médian entre les deux échelles. Ce rapport est calculé par `outils/construire_habitats.py` sur les 175 types de la nomenclature qui ont les deux valeurs : 1,056. Une toiture extensive (distinctivité 2) vaut ainsi 0,264 m²HE par m².

### C-H4
Catégorie : source muette.
La métrique anglaise traite les cours d'eau dans un module linéaire distinct et ne leur donne ni délai ni difficulté surfaciques. Les cours d'eau et sources (C2.1 à C2.6) reçoivent le délai et la difficulté de la mare prioritaire. La noue et le jardin de pluie (VB.19) reçoivent la valeur du fossé proche de l'état naturel de la BKompV (23.05.01a.01), seul type allemand d'ouvrage linéaire en eau végétalisé.

### C-H5
Catégorie : convention de transposition.
Pour les types ligneux, la BKompV distingue trois stades : jeune (J), moyen (M) et âgé (A). La valeur intrinsèque par défaut est celle du stade moyen. L'écologue peut déclarer le stade d'un peuplement existant ; un peuplement créé vise le stade moyen. Pour les arbres isolés (VB.18a, VB.18b, G5.1), le stade se déduit de la classe de diamètre de la métrique anglaise : petit, stade J ; moyen, stade M ; grand et très grand, stade A. Quand le houppier n'est pas relevé, sa surface est celle de la zone de protection racinaire de la classe (onglet G-3 de la métrique anglaise).

### C-H6
Catégorie : convention de transposition.
Les grilles d'état sont celles des fiches d'évaluation de la métrique statutaire anglaise (juillet 2025), traduites et adaptées. Chaque type OpenNAT relève de la grille de son groupe anglais : prairies de faible valeur EP1, prairies de valeur moyenne à très haute EP2, landes EL1, haies EH1, arbres EA1, mares et plans d'eau EM1, fourrés EF1, milieux peu végétalisés ER1, milieux urbains EU1, zones humides EZ1, boisements EB1, vergers EV1. Les cultures n'ont pas de grille (f = 1). Un type relève de la grille du groupe de sa ligne anglaise : prairie de distinctivité 2 au plus, EP1 ; prairie de distinctivité 4 et plus, EP2 ; landes, EL1 ; fourrés, EF1 ; lacs et mares, EM1 ; milieux peu végétalisés, ER1 ; urbain, EU1 ; zones humides et prés salés, EZ1 ; boisements, parcs boisés et coupes, EB1 ; arbres, EA1 ; haies, EH1 ; vergers traditionnels, EV1. Le score vaut S = (nombre de critères satisfaits) / (nombre de critères applicables). L'échec d'un critère essentiel plafonne S à 0,5, ce qui transpose la règle anglaise selon laquelle cet échec interdit le bon et le moyen état. Pour les boisements, chacun des 13 indicateurs est noté de 1 à 3 selon la fiche, et S = (total - 13) / 26.

### C-H7
Catégorie : valeur de secours.
La valeur d'un m² ne peut dépasser 1,15 m²HE, quel que soit le produit des facteurs. 1,15 est le plus fort multiplicateur de la métrique anglaise (importance stratégique ou connectivité élevée).

### C-H8
Catégorie : convention de transposition.
Les critères anglais renvoient aux espèces de l'annexe 9 du Wildlife and Countryside Act 1981 et, pour la grille urbaine, aux autres espèces nuisibles à la faune indigène « selon le jugement professionnel ». OpenNAT leur substitue : les espèces exotiques envahissantes préoccupantes pour l'Union (règlement (UE) n° 1143/2014 et règlements d'exécution qui fixent la liste, reproduite en partie 6), la liste nationale française, et les espèces que les listes régionales des conservatoires botaniques nationaux classent envahissantes avérées. Une espèce absente de la liste de l'Union, comme la renouée du Japon, compte dès qu'une liste régionale la classe envahissante avérée.

## Sols

### C-S1
Catégorie : convention de transposition.
Le coefficient de chaque nature de surface (`donnees/sols.csv`) est la médiane des coefficients publiés par les grilles de coefficient de biotope lues à la source : Berlin (facteurs des plans fixés après décembre 2019), Londres (Urban Greening Factor 2023), Strasbourg (PLU, article 9.2), Grand Annecy (PLUi-HMB), Paris (indice de végétalisation du bâti, 2025) et la Métropole européenne de Lille. La plage d'incertitude est l'étendue des valeurs. Une grille qui distingue plusieurs cas pour une même nature compte pour chacun. Les classes d'épaisseur (15, 30 et 80 cm) suivent l'audit (point P12) : 15 cm est la borne de l'extensif, 25 à 30 cm le seuil au-delà duquel la richesse floristique des toitures cesse de croître (GROOVES), 80 cm la borne au-delà de laquelle les grilles rapprochent la dalle du sol. Montreuil et le guide du SDAGE Seine-Normandie, cités par l'audit, ne sont pas retenus faute d'avoir été relus au lot 1.

### C-S2
Catégorie : convention de transposition.
Dans le calcul de la valeur d'habitat (module H), le coefficient de sol ne s'applique qu'aux unités d'un type d'habitat au sol posées sur dalle : une pelouse sur 40 cm de substrat vaut 0,7 fois une pelouse en pleine terre. Il vaut 1 en pleine terre et pour les types hors-sol (toitures, façades, jardinières), dont la valeur intrinsèque tient déjà compte du support. Dans Bnat, le coefficient de sol s'applique à toutes les surfaces.

## Contexte, eau et seuils

### C-E1
Catégorie : convention de transposition.
Le multiplicateur de situation de la métrique anglaise (importance stratégique 1,15, 1,10 ou 1) s'applique à la trame verte et bleue française : 1,15 dans un réservoir de biodiversité identifié par le SRADDET, le SRCE ou le PLU (article R. 371-19 du code de l'environnement), 1,10 dans un corridor identifié, 1 ailleurs. Il s'applique à l'état initial comme à l'état projet, pour ne jamais récompenser une destruction en réservoir.

### C-E2
Catégorie : source muette.
Aucune source ne module les délais de maturation par zone biogéographique en France. Les délais anglais s'appliquent tels quels dans les quatre zones. Pour les zones méditerranéenne et alpine, la plage d'incertitude du multiplicateur monte à 1,25, sans changer la valeur centrale.

### C-E3
Catégorie : valeur de secours.
La somme des surfaces des unités au sol doit égaler la surface de la parcelle à 0,5 % près, et au moins à 1 m² près. Au-delà, le calcul s'arrête à l'étape E2.

### C-E4
Catégorie : convention de transposition.
Un milieu en eau alimenté artificiellement (réseau d'eau potable, pompage) avec une eau non traitée voit sa valeur multipliée par 0,8. La borne basse vient de l'écart londonien entre eau semi-naturelle (1) et bassin nu ou eau chlorée (0,2), qui relève ici du type VB.21.

### C-E5
Catégorie : convention de transposition.
La part des eaux pluviales infiltrées ou gérées à ciel ouvert est un indicateur complémentaire. Elle entre dans Bnat par le bonus d'infiltration de Berlin (0,2 par m² de surface extérieure dont l'eau est infiltrée en surface).

### C-E6
Catégorie : convention de transposition.
Les seuils de Bnat sont ceux du coefficient de biotope par surface harmonisé du référentiel Effinature 8.1 (critère SOL 01.2.5), appliqués à Bnat / 100 : logements et équipements d'intérêt collectif, 45 si l'emprise du bâti va jusqu'à 37 %, 35 de 38 à 49 %, 25 au-delà ; commerces, bureaux et hébergements avec services, 25. S'y ajoute au moins 15 % de pleine terre végétalisée. Bnat et le CBSh n'emploient pas les mêmes coefficients (ceux du CBSh sont exclus pour leur licence) : l'écart entre les deux sur des projets réels sera mesuré au banc du lot 4.

### C-E7
Catégorie : convention de transposition.
Deux niveaux pour le site : niveau 1, absence de perte nette (Cnat au plus 0) ; niveau 2, gain net d'au moins 10 % de la valeur initiale intégrée sur 50 ans, transposé de l'objectif anglais (Town and Country Planning Act 1990, Schedule 7A, paragraphe 2(3)). Aucun seuil n'est proposé pour Inat en v1 : il sera fixé après le banc du lot 4, comme les seuils de l'Ic construction l'ont été après l'expérimentation E+C-.

## Connectivité

### C-C1
Catégorie : convention de transposition.
Facteur de taille d'une tache d'habitat : k = (A / A_ref)^z, borné entre 0,35 et 1. z = 0,22 (îles d'habitat, Matthews et al. 2016). A_ref = 4,4 ha (Beninde et al. 2015 : seuil moyen sous lequel les espèces adaptées à la ville déclinent). Le plancher 0,35 est la plus petite classe de fragmentation de GLOBIO 3.5 (taches de moins de 1 km²). A est la surface de la tache, augmentée des espaces végétalisés extérieurs au site qui lui sont contigus.

### C-C2
Catégorie : convention de transposition.
Multiplicateur de connectivité de la métrique anglaise : 1,15 pour une tache contiguë à un réservoir, à un corridor ou à un espace naturel extérieur d'au moins 1 ha ; 1,10 si un tel espace est à moins de 200 m, bord à bord, sans obstacle infranchissable ; 1 ailleurs. La distance de 200 m et la surface de 1 ha sont des valeurs de secours.

### C-C3
Catégorie : source muette.
Une tache entièrement close par une clôture sans passage pour la petite faune voit sa valeur multipliée par 0,9. Une clôture est perméable si elle offre au moins un passage de 15 x 15 cm tous les 20 m. Un muret plein de plus de 20 cm de haut est une clôture étanche.

## Nuisances

### C-N1
Catégorie : valeur de secours.
Trois classes d'éclairage par unité : L0, aucun point lumineux à moins de 50 m (facteur 1) ; L1, éclairage conforme à l'arrêté du 27 décembre 2018 et éteint en milieu de nuit (0,9) ; L2, éclairage non conforme ou permanent (0,75). Aucune relation dose-effet n'a été publiée (méta-analyse de Sanders et al. 2021) ; les distances d'évitement des chiroptères (Azam et al. 2018) bornent la distance d'influence.

### C-N2
Catégorie : convention de transposition.
Une unité exposée à un niveau sonore supérieur à 47 dB(A) en milieu ouvert, ou à 42 dB(A) en milieu boisé, voit sa valeur multipliée par 0,7, d'après la baisse de densité d'oiseaux nicheurs d'au moins 30 % au-delà de ces seuils (Reijnen et al. 1997).

### C-N3
Catégorie : source muette.
Une unité végétalisée à moins de 15 m d'une façade qui expose plus de 10 m² de vitrage non traité contre les collisions voit sa valeur multipliée par 0,95. La surface vitrée exposée non traitée est aussi affichée en indicateur.

## Temps

### C-T1
Catégorie : convention de transposition.
Simulation au pas annuel sur la période de référence de 50 ans de l'ACV de la RE2020 (annexe II de l'arrêté du 4 août 2021), avec une sortie complémentaire à 30 ans. Un habitat créé gagne sa valeur de façon linéaire, de 0 à la fin du chantier jusqu'à sa valeur cible au bout de son délai de maturité.

### C-T2
Catégorie : convention de transposition.
Le délai « 30+ » de la métrique anglaise vaut 32 ans : c'est l'année que la table des multiplicateurs temporels de l'onglet G-4 associe à « 30+ ».

### C-T3
Catégorie : convention de transposition.
Les types minéraux et scellés (VB.1 à VB.4, VB.25, H5.6), pour lesquels la métrique anglaise ne prévoit aucun délai, atteignent leur valeur dès la fin du chantier.

### C-T4
Catégorie : valeur de secours.
Une unité conservée perd 25 % de sa valeur pendant la durée du chantier quand aucune mesure de protection (clôture, balisage, interdiction de stockage et de circulation) n'est prévue.

### C-T5
Catégorie : convention de transposition.
Taux d'actualisation nul. Le taux anglais de 3,5 % par an est codé en option d'étude inactive.

### C-T6
Catégorie : valeur de secours.
La réfection d'une unité (toiture végétalisée refaite, par exemple) annule sa valeur pendant un an, puis la maturation reprend depuis 0.

### C-T7
Catégorie : convention de transposition.
La difficulté de création ou d'amélioration de la métrique anglaise (1 ; 0,67 ; 0,33 ; 0,1) multiplie la valeur cible d'un habitat créé ou amélioré : elle exprime le risque d'échec.

## Biodiversité grise

### C-G1
Catégorie : convention de transposition.
Inat porte sur les contributeurs « composants » et « chantier » de l'ACV de la RE2020, tels que le RSEE les donne (branche RSEnv). Les consommations d'énergie et d'eau en exploitation n'y entrent pas.

### C-G2
Catégorie : convention de transposition.
Facteur de caractérisation du climat, en m²HE par kg CO2 éq. et par an : CF = S_terres x (1 - p) x (perte de MSA par °C / 2) x TCRE = 1,30e14 x 0,87 x (0,071 / 2) x 4,5e-16 = 1,807e-3. S_terres et p viennent du rapport spécial du GIEC sur les terres émergées (2019), la perte de MSA par °C et le facteur de retard de 2 de GLOBIO 3.5, la TCRE du sixième rapport du GIEC (2021). La perte par °C est la médiane non pondérée des 15 biomes de GLOBIO, faute de surfaces de biomes publiées sous licence libre.

### C-G3
Catégorie : valeur de secours.
Une émission pèse sur le reste de la période de référence : 50 ans pour la production et le chantier (A1 à A5), 25 ans en moyenne pour l'exploitation des composants (B), 0 pour la fin de vie (C). Le module D est exclu, comme pour l'Ic construction.

### C-G4
Catégorie : convention de transposition.
Occupation des sols du bois : 10 000 / P x R m²·an par m³ de produit, avec P = 5,4 m³ par ha et par an (production biologique moyenne des forêts françaises, IGN 2024) et R = 2 m³ de bois rond par m³ de produit (valeur de secours, plage 1,5 à 3,1).

### C-G5
Catégorie : convention de transposition.
La qualité d'habitat de la forêt d'origine dépend du régime déclaré (GLOBIO 3.5, table 2.2) : plantation 0,30, coupe rase 0,50, coupe sélective 0,70, exploitation à faible impact 0,85. La certification de gestion forestière n'apporte pas de coefficient : elle justifie le régime déclaré. Sans justification, le régime est la coupe rase.

### C-G6
Catégorie : valeur de secours.
Occupation des sols des granulats et roches : 0,9 m²·an par tonne (médiane de quatre carrières françaises, plage 0,3 à 1,6), avec une qualité d'habitat de 0,05 (classe la plus artificialisée de GLOBIO, aucune classe carrière n'existant).

### C-G7
Catégorie : source muette.
L'occupation des sols des usines (acier, verre, plastiques, isolants minéraux, plâtre) est négligée en v1, faute d'inventaire ouvert. C'est le principal écart connu du module G.

### C-G8
Catégorie : convention de transposition.
Les indicateurs de pollution du RSEE (acidification 106, eutrophisation 107 à 109, écotoxicité pour l'eau douce 116) sont repris tels quels et affichés à part, en unités de l'annexe II, faute de conversion sourcée vers la MSA.

## Relevés

### C-R1
Catégorie : valeur de secours.
Les critères floristiques se relèvent pendant la période où les espèces caractéristiques sont identifiables : en plaine, d'avril à juillet pour les prairies et pelouses, de mai à septembre pour les zones humides et mégaphorbiaies. Un relevé hors période répond « non » aux critères floristiques, sauf preuve contraire.

### C-R2
Catégorie : valeur de secours.
Les couverts et les nombres d'espèces par m² s'estiment sur au moins 5 quadrats de 1 m² par hectare, répartis sur un transect en W, et au moins 3 par unité de moins d'un hectare.

### C-R3
Catégorie : valeur de secours.
Les indicateurs de la grille des boisements se notent sur placettes de 10 m de rayon, au moins une par hectare et au moins trois par unité.

### C-R4
Catégorie : valeur de secours.
Les jardins privatifs d'une même opération se relèvent par échantillon d'au moins un jardin sur cinq ; les haies, par tronçons homogènes de 100 m au plus.

### C-R5
Catégorie : valeur de secours.
Un état initial dégradé volontairement dans les deux ans précédant le dépôt du permis (débroussaillage, labour, décapage) se saisit avec l'état antérieur documenté, pour ne pas récompenser une destruction préalable.

## Incertitude

### C-I1
Catégorie : valeur de secours.
Quand la source ne donne pas d'incertitude, la plage d'une valeur est de ± 10 % pour un texte réglementaire ou un outil officiel, ± 25 % pour un jugement d'expert publié, ± 50 % pour une convention OpenNAT.

### C-I2
Catégorie : valeur de secours.
L'analyse d'incertitude tire au moins 1 000 jeux de valeurs, chaque valeur suivant une loi triangulaire (borne basse, valeur centrale, borne haute). La graine du générateur est écrite dans le fichier projet et dans le RSNat. Les cinq paramètres les plus influents sont classés par la valeur absolue de leur corrélation de rang (Spearman) avec Snat.

## Bnat

### C-B1
Catégorie : convention de transposition.
Bnat = 100 x (somme des surfaces x coefficient de sol + bonus d'infiltration) / surface de la parcelle. Les surfaces hors-sol (toitures, façades) entrent au numérateur sans entrer au dénominateur, comme à Berlin et à Londres : Bnat peut dépasser 100. Les façades comptent pour 10 m de hauteur au plus.

## Attestation au permis de construire

### C-P1
Catégorie : convention de transposition.
Comme l'attestation de la RE2020 au dépôt du permis de construire, qui ne demande que le Bbio, l'attestation OpenNAT au permis porte sur les seules données du plan masse : Bnat et son seuil, le taux de pleine terre et, quand le PLU impose un coefficient de biotope ou une part de pleine terre, la comparaison avec ce minimum. Si le projet ne respecte pas le minimum du PLU, l'attestation le dit et ne conclut pas à la conformité. Les indicateurs Cnat, Inat et Snat sont attestés à l'achèvement des travaux.
