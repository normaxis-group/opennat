# Pollution et biodiversité grise : ponts depuis les indicateurs du RSEE

NORMATYS, éditeur de la méthode. Note de décision pour le Biodiversity Standard Council, complément du dossier de soumission (décision D3). Méthode OpenNAT 1, données 1.2.2, moteur 0.2.0. Projet du 19 octobre 2026, non transmis.

## Ce que la note établit

OpenNAT n'additionne pas la pollution à la biodiversité grise : les cinq indicateurs de pollution du RSEE sont affichés à part (convention C-G8). L'étude Carbone 4 attribue pourtant 51 % de la biodiversité grise d'un bâtiment béton à la pollution, soit 1,34 fois le climat. La note cherche, pour chaque indicateur du RSEE, un facteur publié et ouvert qui le convertisse en surface d'habitat perdue, puis chiffre le résultat sur des bâtiments réels.

Le résultat tient en une phrase : avec des facteurs ouverts appliqués aux indicateurs que déclare le RSEE, la pollution pèse de 4 à 13 % du climat, pas 134 %. L'écart avec Carbone 4 ne vient pas d'un oubli d'OpenNAT. Il vient d'un autre modèle de l'écotoxicité, fondé sur des inventaires ecoinvent et des facteurs à long terme pour les métaux, que les déclarations environnementales ne permettent pas de reproduire.

## Les cinq indicateurs du RSEE

L'annexe II de l'arrêté du 4 août 2021 fixe les unités, celles de la norme EN 15804+A2 et de la méthode européenne d'empreinte environnementale (EF) :

| Code | Indicateur | Unité |
|---|---|---|
| 106 | Acidification, dépassement cumulé | mol H+ éq. |
| 107 | Eutrophisation des eaux douces | kg P éq. |
| 108 | Eutrophisation marine | kg N éq. |
| 109 | Eutrophisation terrestre, dépassement cumulé | mol N éq. |
| 116 | Écotoxicité pour les eaux douces | CTUe |

Sur neuf bâtiments de RSEE réels d'études RE2020 du groupe, les médianes par m² de surface de référence, phases A à C, sont 805 kg CO2 éq. pour le climat, puis 0,207 ; 0,0081 ; 0,037 ; 0,383 et 2,37 dans l'ordre du tableau. L'écotoxicité varie de 1,1 à 450 CTUe par m² : l'indicateur est déclaré de façon très inégale d'un produit à l'autre.

## Les ponts

Une fraction d'espèces perdue (PDF) sur un m² pendant un an est rapprochée d'un m²HE·an, comme dans le contrôle Carbone 4 : aucune conversion publiée entre PDF et MSA n'a été lue. Les ponts passent par trois méthodes dont les facteurs sont publiés : IMPACT World+ (Bulle et al. 2019, article et supplément sous CC BY 4.0), ReCiPe 2016 (RIVM, tableur des facteurs v1.1) et GLOBIO 3.5 (PBL 2016).

| Code | Pont | Facteur, en PDF·m²·an par unité |
|---|---|---|
| 116 | IMPACT World+ : un CTUe vaut une fraction d'espèces affectées (PAF) par m³ et par jour ; facteur de gravité de 0,5 pour passer de PAF à PDF ; profondeur moyenne de 2,5 m pour passer des m³ aux m² ; 365 jours | 5,5 × 10⁻⁴ |
| 106 | Passage du dépassement cumulé en kg SO2 éq. par la composition du flux acide (facteurs EF de 1,31, 0,74 et 3,02 mol H+ éq. par kg de SO2, NOx et NH3, couramment cités, à vérifier sur le tableur du JRC ; facteurs ReCiPe de 1, 0,36 et 1,96 kg SO2 éq.), puis ReCiPe : 2,12 × 10⁻⁷ espèce·an par kg SO2 éq., divisé par la densité d'espèces terrestres de 1,48 × 10⁻⁸ par m² | 7,0 à 10,9 |
| 109 | GLOBIO 3.5, tableau 4.1 : MSA = 1 - 0,220 ln(NE + 1) en forêt, NE étant l'azote déposé au-delà de la charge critique en g/m²/an ; le dépassement cumulé mesure ce même excès ; pente à l'origine, puis là où la charge critique est déjà dépassée d'1 g/m²/an | 1,5 à 3,1 |
| 107 | ReCiPe : 6,71 × 10⁻⁷ espèce·an par kg P éq., divisé par la densité d'espèces d'eau douce (7,89 × 10⁻¹⁰ par m³) et la profondeur de 2,5 m ; borne basse : facteur d'effet d'IMPACT World+, 11,4 par kg PO4 éq. | 35 à 340 |
| 108 | IMPACT World+ : facteur d'effet empirique de 12,5 par kg d'azote déposé en zone côtière | 12,5 |

Trois réserves. Le pont 106 dépend de facteurs EF non relus sur leur source, mais il bouge peu avec la composition du flux (de 7,0 à 10,9). Le pont 107 couvre un facteur dix, selon qu'on suit ReCiPe ou IMPACT World+. Le pont 116 applique la conversion d'IMPACT World+ à des CTUe calculés selon la variante EF d'USEtox, qui ne fixe pas les facteurs d'effet sur la même base. Il donne donc un ordre de grandeur, pas une valeur.

## Ce que pèse la pollution

Sur le bâtiment médian, en m²HE·an par m² de surface de référence :

| Code | Bas | Haut |
|---|---|---|
| 106 acidification | 1,44 | 2,26 |
| 107 eutrophisation des eaux douces | 0,28 | 2,74 |
| 108 eutrophisation marine | 0,46 | 0,46 |
| 109 eutrophisation terrestre | 0,59 | 1,18 |
| 116 écotoxicité | 0,001 | 0,001 |
| Pollution | 2,8 | 6,6 |
| Climat compté dans Inat, borne haute | 72,7 | 72,7 |

La pollution fait donc de 3,8 à 9,1 % du climat sur le bâtiment médian. Bâtiment par bâtiment, la part va de 0 à 6 % en borne basse et de 0 à 13 % en borne haute. Le zéro est celui d'un RSEE qui ne déclare presque aucun indicateur de pollution. L'écotoxicité ne dépasse pas 0,25 m²HE·an par m², même pour le bâtiment qui déclare 450 CTUe par m².

Deux contrôles croisés vont dans le même sens. Avec la densité d'espèces de ReCiPe, son facteur climat vaut 0,19 PDF·m²·an par kg CO2 éq., contre 0,09 m²HE·an dans OpenNAT : le climat d'OpenNAT n'est pas surestimé face à ReCiPe. Et IMPACT World+ écrit lui-même que ses facteurs de normalisation de l'écotoxicité des eaux douces varient d'environ trois ordres de grandeur d'une méthode à l'autre.

## Pourquoi Carbone 4 trouve 51 %

Carbone 4 ne part pas des indicateurs de pollution des fiches. Pour les pressions que les fiches ne couvrent pas, dont l'écotoxicité, l'étude prend un jeu ecoinvent représentatif du produit, mis à l'échelle de son empreinte carbone, puis le caractérise par IMPACT World+. Elle attribue la pollution « très largement » au béton : métaux lourds de la cuisson du clinker et extraction. Les inventaires ecoinvent détaillent les émissions de métaux, et IMPACT World+ y applique des facteurs à long terme, au-delà de 100 ans, qui ne pèsent que pour les substances persistantes comme les métaux. Rien de cela ne passe par les CTUe déclarés dans les fiches. La part de 51 % est le résultat de ce modèle. Elle ne peut pas se reconstruire à partir des données dont dispose une étude RE2020.

## Options pour le conseil

| Option | Contenu | Effet sur Inat |
|---|---|---|
| P1, actuel | indicateurs affichés à part, non convertis | aucun |
| P5, ponts ouverts | les cinq indicateurs convertis par les ponts ci-dessus et additionnés à Inat, chacun avec sa plage d'incertitude | + 4 à 13 % du climat selon le bâtiment |
| P6, modèle Carbone 4 | inventaires ecoinvent et facteurs IMPACT World+ par produit | impossible : ecoinvent n'est pas ouvert, et la licence du service INIES interdit la notation des fiches |
| P4, forfait | pollution = 1,34 fois le climat | écarté : une seule étude, sans licence, et la pollution deviendrait proportionnelle au carbone |

Recommandation de l'éditeur : adopter P5. Inat couvrirait alors toutes les pressions que décrit le RSEE, avec des facteurs ouverts et reproductibles, et une incertitude affichée. La note de méthode dirait en clair que l'écotoxicité à long terme des métaux n'est pas comptée. P5 remplace la recommandation de la première version du dossier, qui n'intégrait que l'eutrophisation terrestre : elle la contient. Elle lève aussi la réserve qui bloquait les seuils d'Inat et de Snat, puisque la pollution calculable est connue et faible. Reste à vérifier les facteurs EF de l'acidification avant l'adoption.

## Annexe. Transposition prête à appliquer

Si le conseil retient P5, la modification tient en une convention, cinq lignes de table et une équation ; aucune autre fiche ne change.

Convention C-G8, nouvelle rédaction : « Les indicateurs de pollution du RSEE (106, 107, 108, 109, 116) sont convertis en m²HE·an par les facteurs de la table `materiaux.csv` (clé `pollution_<code>`, paramètre `facteur_biodiversite`), une fraction d'espèces perdue sur un m² pendant un an valant un m²HE·an, et additionnés à Inat en un poste Inat_pol. L'écotoxicité à long terme des métaux n'est pas comptée. »

Lignes de `donnees/materiaux.csv` (valeur centrale, bornes ; type transposition, convention C-G8, licence de chaque source) :

| Clé | Unité | Valeur | Borne basse | Borne haute | Source |
|---|---|---|---|---|---|
| pollution_106 | m²HE·an par mol H+ éq. | 8,7 | 7,0 | 10,9 | ReCiPe 2016 v1.1 (acidification terrestre, densité d'espèces) ; facteurs EF de dépassement cumulé |
| pollution_107 | m²HE·an par kg P éq. | 109 | 35 | 340 | ReCiPe 2016 v1.1 ; IMPACT World+ (Bulle et al. 2019) |
| pollution_108 | m²HE·an par kg N éq. | 12,5 | 9,4 | 15,6 | IMPACT World+, supplément, eutrophisation marine ; bornes de ± 25 % (convention C-I1) |
| pollution_109 | m²HE·an par mol N éq. | 2,2 | 1,5 | 3,1 | GLOBIO 3.5, tableau 4.1 |
| pollution_116 | m²HE·an par CTUe | 5,5 × 10⁻⁴ | 1,4 × 10⁻⁴ | 2,2 × 10⁻³ | IMPACT World+, supplément, écotoxicité des eaux douces ; plage d'un facteur 4 de part et d'autre, faute de base commune avec la variante EF d'USEtox |

Valeurs centrales : moyenne géométrique des bornes quand les sources divergent.

Fiche A36, équation ajoutée : (A36-2) Inat_pol = somme sur i de POL_i × F_i, avec F_i le facteur de l'indicateur i ; Inat = Inat_clim + Inat_sols + Inat_pol. Le récapitulatif standardisé reçoit un élément `inat_pollution` en m²HE·an, et le catalogue dimensionnel cinq unités « m²HE·an par unité d'indicateur ».

Effet sur les cas du banc : nul pour les cas sans indicateurs de pollution, qui sont tous les cas actuels ; un cas portant les indicateurs médians est à ajouter au banc.
