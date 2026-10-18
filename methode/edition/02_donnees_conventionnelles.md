## Partie 2. Données conventionnelles

Les données conventionnelles jouent ici le rôle du chapitre 2 de la méthode Th-BCE : elles sont séparées des fiches algorithmes, qui les appellent par leur clé et leur paramètre. Elles sont imprimées ci-dessous telles qu'elles figurent dans les tables `donnees/` de la version 1 ; la table fait foi en cas d'écart avec une transcription.

Chaque valeur porte une plage d'incertitude (borne basse et borne haute) utilisée par l'analyse d'incertitude, un type et, le cas échéant, le numéro de la convention qui la fixe. Types : primaire, valeur lue telle quelle dans la source ; transposée, valeur lue dans une source primaire et appliquée par une correspondance ou un changement d'échelle écrit en convention ; secondaire, valeur lue dans une source qui en cite une autre, à remplacer ; convention, valeur fixée et justifiée par la méthode.

### 2.1 Nomenclature des habitats

La nomenclature compte 191 types : 25 types urbains et hors-sol, codés VB, et 166 types EUNIS 2012 de niveau 3 présents en France métropolitaine (HabRef v7), hors milieux littoraux et marins, grottes, glaciers et reliefs volcaniques. Pour chaque type, la table donne le code BKompV d'où vient la valeur intrinsèque, la ligne de la métrique anglaise d'où viennent les délais et difficultés, et la justification de ces deux correspondances. Les codes EUNIS 2012 du groupe J se saisissent par le type VB indiqué en colonne « Rattachés ».

| Code | Libellé | EUNIS 2012 | Rattachés | Position | BKompV | Métrique anglaise |
|---|---|---|---|---|---|---|
| VB.1 | Surface bâtie (emprise de construction) | J1 | J1.1 J1.2 J1.3 J1.4 J1.7 J2.1 J2.2 J2.3 J2.4 | sol | 52.03.01 | Urban - Developed land; sealed surface |
| VB.2 | Surface imperméabilisée non bâtie (voirie, parking, dallage étanche) | J4.2 | J4.1 J4.4 J4.5 J4.7 | sol | 52.01.01a | Urban - Developed land; sealed surface |
| VB.3 | Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés) | J4.6 |  | sol | 52.03.03a | Urban - Artificial unvegetated, unsealed surface |
| VB.4 | Revêtement perméable végétalisé (dalles alvéolées engazonnées) | J4.6 |  | sol | 52.03.02 | Urban - Artificial unvegetated, unsealed surface |
| VB.5 | Pelouse d'agrément tondue, terrain de sport engazonné | E2.6 | E2.8 | sol | 34.09 | Grassland - Modified grassland |
| VB.6 | Massif ornemental horticole, couvre-sol planté | I2.1 |  | sol | 51.07a.02 | Urban - Introduced shrub |
| VB.7 | Jardin domestique végétalisé | I2.2 |  | sol | 51.08a.01 | Urban - Vegetated garden |
| VB.8 | Friche urbaine herbacée | J1.5 | J2.6 J3.3 J4.1 | sol | 51.04a.01 | Urban - Open mosaic habitats on previously developed land |
| VB.9 | Friche urbaine arbustive (plus de 50 % de ligneux) | J1.5 |  | sol | 41.01.06 | Heathland and shrub - Mixed scrub |
| VB.10 | Sol nu, chantier, terrassement | J1.6 | J2.7 J6.1 | sol | 32.11.09a | Urban - Bare ground |
| VB.11 | Toiture végétalisée extensive (substrat de moins de 15 cm) | J1 |  | hors sol toiture | aucun | Urban - Other green roof |
| VB.12 | Toiture végétalisée semi-intensive ou biodiverse (15 à 30 cm) | J1 |  | hors sol toiture | aucun | Urban - Biodiverse green roof |
| VB.13 | Toiture végétalisée intensive (plus de 30 cm) | J1 |  | hors sol toiture | aucun | Urban - Intensive green roof |
| VB.15 | Façade végétalisée enracinée au sol (plantes grimpantes) | J1 |  | hors sol facade | aucun | Urban - Ground based green wall |
| VB.16 | Façade végétalisée hors sol (bacs, modules) | J1 |  | hors sol facade | aucun | Urban - Facade-bound green wall |
| VB.18a | Arbre isolé ou alignement d'essence indigène | G5.1 |  | arbre | 41.05aM | Individual trees - Urban tree |
| VB.18b | Arbre isolé ou alignement d'essence non indigène | G5.1 |  | arbre | 41.05bM | Individual trees - Urban tree |
| VB.19 | Noue, jardin de pluie, bassin paysager alimenté en eau de pluie | J5.3 |  | eau | 23.05.01a.01 | Urban - Rain garden |
| VB.20 | Mare créée ou plan d'eau à berges naturelles | C1.3 |  | eau | 24.04c | Lakes - Ponds (non-priority habitat) |
| VB.21 | Bassin, fontaine ou plan d'eau à eau traitée | J5.5 | J5.1 J5.2 J5.4 | eau | 24.07.05 | Lakes - Ornamental lake or pond |
| VB.22 | Potager, jardin partagé, jardin familial | I1.2 |  | sol | 51.08a.01 | Urban - Allotments |
| VB.23 | Jardinière, bac et plantation hors sol au niveau du sol | J1 |  | hors sol toiture | aucun | Urban - Ground level planters |
| VB.24 | Bassin de rétention sec ou en eau, non paysager | J5.3 |  | eau | 24.07.08 | Urban - Sustainable drainage system |
| VB.25 | Voie ferrée, ballast | J4.3 |  | sol | 52.04.01 | Urban - Built linear features |
| VB.26 | Prairie urbaine extensive, fauche tardive | E2.2 |  | sol | 34.07b.01 | Grassland - Other neutral grassland |
| C1.1 | Lacs, étangs et mares oligotrophes permanents | C1.1 |  | eau | 24.02a | Lakes - Low alkalinity lakes |
| C1.2 | Lacs, étangs et mares mésotrophes permanents | C1.2 |  | eau | 24.03b | Lakes - Moderate alkalinity lakes |
| C1.3 | Lacs, étangs et mares eutrophes permanents | C1.3 |  | eau | 24.04b | Lakes - High alkalinity lakes |
| C1.4 | Lacs, étangs et mares permanents dystrophes | C1.4 |  | eau | 24.01a | Lakes - Peat lakes |
| C1.5 | Lacs, étangs et mares continentaux salés et saumâtres permanents | C1.5 |  | eau | 24.06.01 | Lakes - High alkalinity lakes |
| C1.6 | Lacs, étangs et mares temporaires | C1.6 |  | eau | 24.09a | Lakes - Temporary lakes ponds and pools (H3170) |
| C2.1 | Sources, ruisseaux de sources | C2.1 |  | eau | 22.02 | Lakes - Ponds (priority habitat) |
| C2.2 | Cours d'eau permanents à écoulement rapide | C2.2 |  | eau | 23.01 | Lakes - Ponds (priority habitat) |
| C2.3 | Cours d'eau permanents à débit régulier | C2.3 |  | eau | 23.01 | Lakes - Ponds (priority habitat) |
| C2.4 | Fleuves et rivières tidaux en amont de l'estuaire | C2.4 |  | eau | 23.01 | Lakes - Ponds (priority habitat) |
| C2.5 | Eaux courantes temporaires | C2.5 |  | eau | 23.09 | Lakes - Temporary lakes ponds and pools (H3170) |
| C2.6 | Films d'eau sur les marges rocheuses d'un cours d'eau | C2.6 |  | eau | 23.07.01 | Lakes - Ponds (priority habitat) |
| C3.1 | Formations à hélophytes riches en espèces | C3.1 |  | eau | 38.07 | Wetland - Reedbeds |
| C3.2 | Roselières et formations de bordure à grands hélophytes | C3.2 |  | eau | 38.02.01 | Wetland - Reedbeds |
| C3.3 | Formations riveraines à grandes cannes | C3.3 |  | eau | 38.07 | Wetland - Reedbeds |
| C3.4 | Végétations amphibies lentes, pauvres en espèces | C3.4 |  | eau | 24.08a.01 | Lakes - Temporary lakes ponds and pools (H3170) |
| C3.5 | Berges périodiquement inondées à végétation pionnière | C3.5 |  | eau | 24.08a.01 | Lakes - Temporary lakes ponds and pools (H3170) |
| C3.6 | Berges nues ou clairsemées à sédiments meubles | C3.6 |  | eau | 23.08a.01 | Sparsely vegetated land - Ruderal/Ephemeral |
| C3.7 | Berges nues ou clairsemées à sédiments non mobiles | C3.7 |  | eau | 23.08a.01 | Sparsely vegetated land - Ruderal/Ephemeral |
| C3.8 | Habitats continentaux dépendant de la bruine | C3.8 |  | sol | 22.03 | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| D1.1 | Tourbières hautes | D1.1 |  | sol | 36.01 | Wetland - Lowland raised bog |
| D1.2 | Tourbières de couverture | D1.2 |  | sol | 36.01 | Wetland - Blanket bog |
| D2.1 | Tourbières de vallée | D2.1 |  | sol | 35.01a | Wetland - Oceanic valley mire[1] (D2.1) |
| D2.2 | Bas-marais oligotrophes et tourbières des sources | D2.2 |  | sol | 35.01a | Wetland - Fens (upland and lowland) |
| D2.3 | Tourbières de transition et tremblantes | D2.3 |  | sol | 36.02 | Wetland - Transition mires and quaking bogs (H7140) |
| D4.1 | Bas-marais riches en bases | D4.1 |  | sol | 35.01a | Wetland - Fens (upland and lowland) |
| D4.2 | Communautés riveraines des sources calcaires de montagne | D4.2 |  | sol | 22.01.02 | Wetland - Fens (upland and lowland) |
| D5.1 | Roselières normalement sans eau libre | D5.1 |  | sol | 38.02.02 | Wetland - Reedbeds |
| D5.2 | Formations à grandes cypéracées sans eau libre | D5.2 |  | sol | 37.02 | Wetland - Fens (upland and lowland) |
| D5.3 | Zones marécageuses à grands joncs | D5.3 |  | sol | 35.02.06.03 | Wetland - Purple moor grass and rush pastures |
| D6.1 | Marais salés continentaux | D6.1 |  | sol | 35.03 | Coastal saltmarsh - Saltmarshes and saline reedbeds |
| D6.2 | Nappes d'hélophytes saumâtres pauvres en espèces | D6.2 |  | sol | 38.07 | Wetland - Reedbeds |
| E1.1 | Végétations ouvertes des substrats sableux et rocheux | E1.1 |  | sol | 34.04.01a | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| E1.2 | Pelouses calcaires vivaces et steppes riches en bases | E1.2 |  | sol | 34.02a | Grassland - Lowland calcareous grassland |
| E1.3 | Pelouses xériques méditerranéennes | E1.3 |  | sol | 34.01 | Grassland - Lowland calcareous grassland |
| E1.4 | Steppes méditerranéennes à grandes graminées et armoises | E1.4 |  | sol | 34.03.01a | Grassland - Lowland calcareous grassland |
| E1.5 | Pelouses méditerranéo-montagnardes | E1.5 |  | sol | 34.01 | Grassland - Upland calcareous grassland |
| E1.6 | Pelouses à annuelles subnitrophiles | E1.6 |  | sol | 39.06.02 | Sparsely vegetated land - Ruderal/Ephemeral |
| E1.7 | Pelouses sèches acides et neutres fermées non méditerranéennes | E1.7 |  | sol | 34.04.03.01a | Grassland - Lowland dry acid grassland |
| E1.8 | Pelouses fermées sèches acides et neutres méditerranéennes | E1.8 |  | sol | 34.04.03.01a | Grassland - Lowland dry acid grassland |
| E1.9 | Pelouses ouvertes sèches acides et neutres non méditerranéennes | E1.9 |  | sol | 34.04.01a | Grassland - Lowland dry acid grassland |
| E1.A | Pelouses sèches ouvertes acides et neutres méditerranéennes | E1.A |  | sol | 34.04.01a | Grassland - Lowland dry acid grassland |
| E1.B | Pelouses des sols métallifères | E1.B |  | sol | 34.05.01 | Sparsely vegetated land - Calaminarian grasslands |
| E1.C | Habitats méditerranéens secs à herbacées inappétentes | E1.C |  | sol | 39.07 | Grassland - Other neutral grassland |
| E1.D | Pelouses xériques non exploitées | E1.D |  | sol | 34.02b | Grassland - Lowland calcareous grassland |
| E1.E | Pelouses xériques piétinées à annuelles | E1.E |  | sol | 34.09 | Grassland - Modified grassland |
| E2.1 | Pâturages permanents mésotrophes | E2.1 |  | sol | 34.07b.02 | Grassland - Other neutral grassland |
| E2.2 | Prairies de fauche de basse et moyenne altitude | E2.2 |  | sol | 34.07a.01 | Grassland - Lowland meadows |
| E2.3 | Prairies de fauche montagnardes | E2.3 |  | sol | 34.07a.01 | Grassland - Upland hay meadows |
| E2.6 | Prairies améliorées, terrains de sport et pelouses ornementales | E2.6 |  | sol | 34.08a.01 | Grassland - Modified grassland |
| E2.7 | Prairies mésiques non gérées | E2.7 |  | sol | 34.07b.03 | Grassland - Other neutral grassland |
| E2.8 | Pelouses mésophiles piétinées à annuelles | E2.8 |  | sol | 34.09 | Grassland - Modified grassland |
| E3.1 | Prairies humides hautes méditerranéennes | E3.1 |  | sol | 35.02.03a.01 | Wetland - Purple moor grass and rush pastures |
| E3.2 | Prairies humides rases méditerranéennes | E3.2 |  | sol | 35.02.03a.01 | Wetland - Purple moor grass and rush pastures |
| E3.4 | Prairies eutrophes et mésotrophes humides | E3.4 |  | sol | 35.02.05.01 | Grassland - Floodplain wetland mosaic and CFGM |
| E3.5 | Prairies oligotrophes humides | E3.5 |  | sol | 35.02.01a | Wetland - Purple moor grass and rush pastures |
| E4.1 | Combes à neige avec végétation | E4.1 |  | sol | 64.01 | Heathland and shrub - Mountain heaths and willow scrub |
| E4.2 | Sommets et crêtes à mousses et lichens | E4.2 |  | sol | 68.01 | Heathland and shrub - Mountain heaths and willow scrub |
| E4.3 | Pelouses alpines et subalpines acidiphiles | E4.3 |  | sol | 66.09 | Grassland - Upland acid grassland |
| E4.4 | Pelouses alpines et subalpines calcicoles | E4.4 |  | sol | 66.02 | Grassland - Upland calcareous grassland |
| E4.5 | Prairies alpines et subalpines fertilisées | E4.5 |  | sol | 66.06 | Grassland - Upland hay meadows |
| E5.1 | Végétations herbacées anthropiques | E5.1 |  | sol | 39.06.03 | Sparsely vegetated land - Ruderal/Ephemeral |
| E5.2 | Ourlets forestiers thermophiles | E5.2 |  | sol | 39.01.01 | Sparsely vegetated land - Tall forbs |
| E5.3 | Formations à fougère aigle | E5.3 |  | sol | 39.07 | Grassland - Bracken |
| E5.4 | Lisières et prairies humides à grandes herbacées | E5.4 |  | sol | 39.04a.01 | Grassland - Tall herb communities (H6430) |
| E5.5 | Formations subalpines humides à grandes herbacées | E5.5 |  | sol | 67.01 | Grassland - Tall herb communities (H6430) |
| E6.1 | Steppes salées intérieures méditerranéennes | E6.1 |  | sol | 35.03 | Coastal saltmarsh - Saltmarshes and saline reedbeds |
| E7.1 | Parcs boisés atlantiques | E7.1 |  | sol | 42.04.01 | Woodland and forest - Wood-pasture and parkland |
| E7.2 | Parcs boisés subcontinentaux | E7.2 |  | sol | 42.04.01 | Woodland and forest - Wood-pasture and parkland |
| E7.3 | Dehesa | E7.3 |  | sol | 42.04.01 | Woodland and forest - Wood-pasture and parkland |
| F2.1 | Fourrés subarctiques et alpins à saules nains | F2.1 |  | sol | 69.07 | Heathland and shrub - Mountain heaths and willow scrub |
| F2.2 | Landes et fourrés sempervirents alpins et subalpins | F2.2 |  | sol | 69.05 | Heathland and shrub - Mountain heaths and willow scrub |
| F2.3 | Fourrés subalpins caducifoliés | F2.3 |  | sol | 69.02 | Heathland and shrub - Mountain heaths and willow scrub |
| F2.4 | Fourrés de conifères proches de la limite des arbres | F2.4 |  | sol | 69.04 | Heathland and shrub - Mountain heaths and willow scrub |
| F3.1 | Fourrés tempérés | F3.1 |  | sol | 41.01.04.02 | Heathland and shrub - Mixed scrub |
| F3.2 | Fourrés caducifoliés subméditerranéens | F3.2 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F4.1 | Landes humides | F4.1 |  | sol | 40.02.01 | Heathland and shrub - Lowland heathland |
| F4.2 | Landes sèches | F4.2 |  | sol | 40.03.01 | Heathland and shrub - Lowland heathland |
| F5.1 | Matorrals arborescents | F5.1 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F5.2 | Maquis | F5.2 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F5.3 | Pseudo-maquis | F5.3 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F5.4 | Fourrés à genêt d'Espagne | F5.4 |  | sol | 41.01.05.04a | Heathland and shrub - Gorse scrub |
| F5.5 | Fourrés thermoméditerranéens | F5.5 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F6.1 | Garrigues occidentales | F6.1 |  | sol | 41.01.05.03 | Heathland and shrub - Lowland heathland |
| F6.6 | Garrigues supraméditerranéennes | F6.6 |  | sol | 41.01.05.03 | Heathland and shrub - Lowland heathland |
| F6.8 | Fourrés xérohalophiles | F6.8 |  | sol | 41.01.05.04a | Heathland and shrub - Mixed scrub |
| F7.1 | Landes épineuses ouest-méditerranéennes | F7.1 |  | sol | 40.05 | Heathland and shrub - Upland heathland |
| F7.2 | Landes épineuses centro-méditerranéennes | F7.2 |  | sol | 40.05 | Heathland and shrub - Upland heathland |
| F7.4 | Landes-hérisson | F7.4 |  | sol | 40.05 | Heathland and shrub - Upland heathland |
| F9.1 | Fourrés ripicoles | F9.1 |  | sol | 41.01.02 | Heathland and shrub - Willow scrub |
| F9.2 | Saussaies marécageuses et fourrés de bas-marais | F9.2 |  | sol | 41.01.03.01 | Heathland and shrub - Willow scrub |
| F9.3 | Galeries et fourrés riverains méridionaux | F9.3 |  | sol | 41.01.02 | Heathland and shrub - Willow scrub |
| FA.1 | Haies d'espèces non indigènes | FA.1 |  | lineaire | 41.04M | Non-native and ornamental hedgerow |
| FA.2 | Haies d'espèces indigènes fortement gérées | FA.2 |  | lineaire | 41.03.03J | Native hedgerow |
| FA.3 | Haies d'espèces indigènes riches en espèces | FA.3 |  | lineaire | 41.03.03M | Species-rich native hedgerow |
| FA.4 | Haies d'espèces indigènes pauvres en espèces | FA.4 |  | lineaire | 41.03.03J | Native hedgerow |
| FB.1 | Plantations d'arbustes pour la récolte de la plante entière | FB.1 |  | sol | 41.07 | Cropland - Horticulture |
| FB.2 | Plantations d'arbustes pour la récolte de feuilles et de branches | FB.2 |  | sol | 41.07 | Cropland - Horticulture |
| FB.3 | Plantations d'arbustes ornementaux ou fruitiers | FB.3 |  | sol | 41.07 | Urban - Introduced shrub |
| FB.4 | Vignobles | FB.4 |  | sol | 41.08.02 | Cropland - Horticulture |
| G1.1 | Forêts riveraines à aulnes, peupliers ou saules | G1.1 |  | sol | 43.04.02.01M | Woodland and forest - Wet woodland |
| G1.2 | Forêts riveraines mixtes des plaines inondables | G1.2 |  | sol | 43.04.03.01M | Woodland and forest - Wet woodland |
| G1.3 | Forêts riveraines méditerranéennes | G1.3 |  | sol | 43.04.02.01M | Woodland and forest - Wet woodland |
| G1.4 | Forêts marécageuses de feuillus hors tourbe acide | G1.4 |  | sol | 43.02.02.01M | Woodland and forest - Wet woodland |
| G1.5 | Forêts marécageuses de feuillus sur tourbe acide | G1.5 |  | sol | 43.02.01.01M | Woodland and forest - Wet woodland |
| G1.6 | Hêtraies | G1.6 |  | sol | 43.07.04M | Woodland and forest - Lowland beech and yew woodland |
| G1.7 | Forêts caducifoliées thermophiles | G1.7 |  | sol | 43.08.05M | Woodland and forest - Lowland mixed deciduous woodland |
| G1.8 | Boisements acidophiles à chênes | G1.8 |  | sol | 43.07.03M | Woodland and forest - Lowland mixed deciduous woodland |
| G1.9 | Boisements non riverains à bouleaux, trembles ou sorbiers | G1.9 |  | sol | 42.03.02 | Woodland and forest - Upland birchwoods |
| G1.A | Boisements mésotrophes et eutrophes à chênes, charmes, frênes, érables | G1.A |  | sol | 43.07.02M | Woodland and forest - Lowland mixed deciduous woodland |
| G1.B | Aulnaies non riveraines | G1.B |  | sol | 43.03.01M | Woodland and forest - Wet woodland |
| G1.C | Plantations forestières très artificielles de feuillus caducifoliés | G1.C |  | sol | 43.10M | Woodland and forest - Other woodland; broadleaved |
| G1.D | Vergers d'arbres fruitiers et à noix | G1.D |  | sol | 41.06.01.MA | Grassland - Traditional orchards |
| G2.1 | Forêts méditerranéennes de chênes sempervirents | G2.1 |  | sol | 43.08.05M | Woodland and forest - Lowland mixed deciduous woodland |
| G2.2 | Forêts sclérophylles continentales | G2.2 |  | sol | 43.08.05M | Woodland and forest - Lowland mixed deciduous woodland |
| G2.4 | Boisements à caroubier et olivier | G2.4 |  | sol | 43.08.05M | Woodland and forest - Lowland mixed deciduous woodland |
| G2.6 | Bois de houx | G2.6 |  | sol | 43.07.04M | Woodland and forest - Lowland beech and yew woodland |
| G2.8 | Plantations forestières de feuillus sempervirents | G2.8 |  | sol | 43.10M | Woodland and forest - Other woodland; broadleaved |
| G2.9 | Vergers et bosquets sempervirents (oliveraies) | G2.9 |  | sol | 41.06.01.MA | Grassland - Traditional orchards |
| G3.1 | Boisements à épicéas et sapins | G3.1 |  | sol | 44.03.03M | Woodland and forest - Native pine woodlands |
| G3.2 | Boisements alpins à mélèze et pin cembro | G3.2 |  | sol | 70.03M | Woodland and forest - Native pine woodlands |
| G3.3 | Pinèdes à pin à crochets | G3.3 |  | sol | 44.02.01M | Woodland and forest - Native pine woodlands |
| G3.4 | Pinèdes à pin sylvestre | G3.4 |  | sol | 44.02.03M | Woodland and forest - Other Scot's pine woodland |
| G3.5 | Pinèdes à pin noir | G3.5 |  | sol | 44.02.01M | Woodland and forest - Other Scot's pine woodland |
| G3.7 | Pinèdes méditerranéennes hors pin noir | G3.7 |  | sol | 44.02.01M | Woodland and forest - Other Scot's pine woodland |
| G3.9 | Bois de cupressacées ou de taxacées | G3.9 |  | sol | 44.02.01M | Woodland and forest - Lowland beech and yew woodland |
| G3.E | Forêts de conifères des tourbières | G3.E |  | sol | 44.01.02M | Woodland and forest - Wet woodland |
| G3.F | Plantations très artificielles de conifères | G3.F |  | sol | 44.05M | Woodland and forest - Other coniferous woodland |
| G4.1 | Forêts mixtes marécageuses | G4.1 |  | sol | 43.03.01M | Woodland and forest - Wet woodland |
| G4.6 | Forêts mixtes à sapin, épicéa et hêtre | G4.6 |  | sol | 43.07.06M | Woodland and forest - Other woodland; mixed |
| G4.8 | Forêts mixtes non riveraines de feuillus et de conifères | G4.8 |  | sol | 43.07.04M | Woodland and forest - Other woodland; mixed |
| G4.9 | Forêts caducifoliées mixtes avec cupressacées ou taxacées | G4.9 |  | sol | 43.07.04M | Woodland and forest - Other woodland; mixed |
| G4.B | Forêts mixtes méditerranéennes de pins et de chênes | G4.B |  | sol | 43.08.05M | Woodland and forest - Other woodland; mixed |
| G4.C | Boisements mixtes à pin sylvestre et chênes thermophiles | G4.C |  | sol | 43.08.05M | Woodland and forest - Other woodland; mixed |
| G4.D | Forêts mixtes de pin noir et de chênes sempervirents | G4.D |  | sol | 43.08.05M | Woodland and forest - Other woodland; mixed |
| G4.E | Forêts mixtes de pins méditerranéens et de chênes sempervirents | G4.E |  | sol | 43.08.05M | Woodland and forest - Other woodland; mixed |
| G4.F | Plantations forestières mixtes | G4.F |  | sol | 44.04M | Woodland and forest - Other woodland; mixed |
| G5.1 | Alignements d'arbres hors milieu urbain | G5.1 |  | arbre | 41.05aM | Individual trees - Rural tree |
| G5.2 | Petits bois anthropiques de feuillus caducifoliés | G5.2 |  | sol | 41.02.02M | Woodland and forest - Other woodland; broadleaved |
| G5.3 | Petits bois anthropiques de feuillus sempervirents | G5.3 |  | sol | 41.02.03M | Woodland and forest - Other woodland; broadleaved |
| G5.4 | Petits bois anthropiques de conifères | G5.4 |  | sol | 44.04M | Woodland and forest - Other coniferous woodland |
| G5.5 | Petits bois anthropiques mixtes | G5.5 |  | sol | 41.02.02M | Woodland and forest - Other woodland; mixed |
| G5.6 | Stades initiaux et régénérations des forêts | G5.6 |  | sol | 42.03.02 | Woodland and forest - Other woodland; broadleaved |
| G5.7 | Taillis et stades initiaux des plantations | G5.7 |  | sol | 43.10J | Woodland and forest - Other woodland; broadleaved |
| G5.8 | Coupes forestières récentes | G5.8 |  | sol | 39.02 | Woodland and forest - Felled |
| H2.3 | Éboulis siliceux des montagnes tempérées | H2.3 |  | sol | 32.03a.01 | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H2.4 | Éboulis calcaires des montagnes tempérées | H2.4 |  | sol | 32.03a.01 | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H2.5 | Éboulis siliceux des expositions chaudes | H2.5 |  | sol | 32.03a.01 | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H2.6 | Éboulis calcaires des expositions chaudes | H2.6 |  | sol | 32.03a.01 | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H3.1 | Falaises continentales siliceuses | H3.1 |  | sol | 32.01a | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H3.2 | Falaises continentales basiques | H3.2 |  | sol | 32.01a | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H3.4 | Falaises continentales humides | H3.4 |  | sol | 32.01a | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H3.5 | Pavements rocheux, dont pavements calcaires | H3.5 |  | sol | 32.01a | Sparsely vegetated land - Limestone pavement |
| H3.6 | Affleurements et rochers érodés | H3.6 |  | sol | 32.01a | Sparsely vegetated land - Inland rock outcrop and scree habitats |
| H5.2 | Moraines glaciaires peu végétalisées | H5.2 |  | sol | 63.04 | Sparsely vegetated land - Other inland rock and scree |
| H5.3 | Substrats minéraux nus ou clairsemés d'origine naturelle | H5.3 |  | sol | 32.09 | Sparsely vegetated land - Other inland rock and scree |
| H5.4 | Substrats organiques secs peu végétalisés | H5.4 |  | sol | 36.04.04 | Sparsely vegetated land - Ruderal/Ephemeral |
| H5.5 | Zones incendiées peu végétalisées | H5.5 |  | sol | 39.02 | Woodland and forest - Felled |
| H5.6 | Zones piétinées | H5.6 |  | sol | 52.02.06 | Urban - Artificial unvegetated, unsealed surface |
| I1.1 | Monocultures intensives | I1.1 |  | sol | 33.04a.03 | Cropland - Cereal crops |
| I1.2 | Cultures maraîchères et horticulture | I1.2 |  | sol | 33.04a.03 | Cropland - Horticulture |
| I1.3 | Terres arables à monocultures extensives | I1.3 |  | sol | 33.04a.02 | Cropland - Arable field margins cultivated annually |
| I1.4 | Cultures inondées ou inondables | I1.4 |  | sol | 33.05.03 | Cropland - Non-cereal crops |
| I1.5 | Friches, jachères et terres arables récemment abandonnées | I1.5 |  | sol | 33.04a.04 | Sparsely vegetated land - Ruderal/Ephemeral |
| I2.1 | Grands jardins ornementaux et parcs | I2.1 |  | sol | 51.06a.03 | Urban - Vegetated garden |
| I2.3 | Zones de jardins abandonnées récemment | I2.3 |  | sol | 51.08a.01 | Urban - Vegetated garden |

#### Justification des correspondances

| Code | Justification |
|---|---|
| VB.1 | Surface scellée : valeur nulle commune à la BKompV (52.03.01) et à la métrique anglaise (u1b) ; les types BKompV 53.01 incluent leurs espaces libres et ne conviennent pas à une emprise seule |
| VB.2 | Voie ou aire scellée |
| VB.3 | Place à revêtement gravillonné ou à liant hydraulique (wassergebundene Decke) |
| VB.4 | Place partiellement stabilisée (Rasengitter) |
| VB.5 | Gazon piétiné et de parc (Tritt- und Parkrasen) |
| VB.6 | Autre espace vert sans arbres anciens |
| VB.7 | Jardins privés riches en structures : valeur de la variante en bon état, l'état est porté par le facteur d'état (convention C-H2) |
| VB.8 | Friche d'anciens sites bâtis, variante riche en structures ou en espèces |
| VB.9 | Fourré des stations rudérales riches en azote |
| VB.10 | Surfaces de chantier et d'installations de chantier |
| VB.11 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.12 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.13 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.15 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.16 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.18a | Arbres isolés, alignements et groupes d'essences autochtones ; stade jeune, moyen ou âgé selon la classe de diamètre (convention C-H5) |
| VB.18b | Arbres isolés, alignements et groupes d'essences non autochtones ; stade selon la classe de diamètre (convention C-H5) |
| VB.19 | Fossé à fonctionnement naturel, sans entretien ou à entretien extensif : seul type BKompV d'ouvrage linéaire en eau végétalisé (convention C-H4) |
| VB.20 | Plan d'eau eutrophe proche de l'état naturel |
| VB.21 | Bassin d'agrément et réserve incendie |
| VB.22 | Jardins familiaux et terres de jardinage riches en structures |
| VB.23 | Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3) |
| VB.24 | Bassin de rétention ouvert |
| VB.25 | Plate-forme ferroviaire |
| VB.26 | Prairie de fauche fraîche moyennement riche en espèces : une prairie semée en ville n'atteint pas le type riche en espèces 34.07a.01, réservé à E2.2 |
| C1.1 | Eaux stagnantes oligotrophes naturelles |
| C1.2 | Autres eaux mésotrophes naturelles |
| C1.3 | Autres eaux eutrophes naturelles |
| C1.4 | Eaux dystrophes naturelles |
| C1.5 | Eau stagnante salée pérenne de l'intérieur |
| C1.6 | Eaux stagnantes temporaires naturelles |
| C2.1 | Sources limnocrènes ; aucune ligne surfacique anglaise pour les cours d'eau (module rivières distinct) : délai et difficulté de la mare prioritaire (convention C-H4) |
| C2.2 | Cours d'eau naturels ; délai et difficulté par la convention C-H4 |
| C2.3 | Cours d'eau naturels ; délai et difficulté par la convention C-H4 |
| C2.4 | Cours d'eau naturels ; délai et difficulté par la convention C-H4 |
| C2.5 | Cours d'eau temporaires naturels |
| C2.6 | Cascade ; délai et difficulté par la convention C-H4 |
| C3.1 | Autre roselière |
| C3.2 | Roselière aquatique à roseau |
| C3.3 | Autre roselière |
| C3.4 | Milieux exondés temporairement au bord des eaux stagnantes, forme naturelle |
| C3.5 | Milieux exondés temporairement au bord des eaux stagnantes, forme naturelle |
| C3.6 | Milieux exondés temporairement au bord des eaux courantes, forme naturelle |
| C3.7 | Milieux exondés temporairement au bord des eaux courantes, forme naturelle |
| C3.8 | Sources rhéocrènes |
| D1.1 | Tourbières hautes intactes |
| D1.2 | Tourbières hautes intactes |
| D2.1 | Bas-marais et marécages intacts |
| D2.2 | Bas-marais et marécages intacts |
| D2.3 | Tourbières de transition intactes |
| D4.1 | Bas-marais et marécages intacts |
| D4.2 | Sources de suintement calcaires |
| D5.1 | Roselière terrestre à roseau |
| D5.2 | Magnocariçaie eutrophe |
| D5.3 | Prairie humide pauvre en espèces en déprise (jonchaies) |
| D6.1 | Prés salés de l'intérieur |
| D6.2 | Autre roselière |
| E1.1 | Pelouses sableuses annuelles |
| E1.2 | Pelouses mi-sèches pâturées ou fauchées |
| E1.3 | Pelouses sèches |
| E1.4 | Pelouses steppiques pâturées ou fauchées |
| E1.5 | Pelouses sèches |
| E1.6 | Stations rudérales sèches et chaudes sur sol limoneux |
| E1.7 | Pelouses sableuses vivaces fermées, pâturées ou fauchées |
| E1.8 | Pelouses sableuses vivaces fermées, pâturées ou fauchées |
| E1.9 | Pelouses sableuses annuelles |
| E1.A | Pelouses sableuses annuelles |
| E1.B | Pelouses métallicoles naturelles |
| E1.C | Peuplements monospécifiques pauvres en espèces |
| E1.D | Pelouses mi-sèches en déprise |
| E1.E | Gazon piétiné |
| E2.1 | Pâture fraîche moyennement riche en espèces |
| E2.2 | Prairie de fauche fraîche riche en espèces |
| E2.3 | Prairie de fauche fraîche riche en espèces |
| E2.6 | Prairie permanente intensive |
| E2.7 | Prairie fraîche en déprise moyennement riche en espèces |
| E2.8 | Gazon piétiné |
| E3.1 | Autre prairie humide extensive exploitée |
| E3.2 | Autre prairie humide extensive exploitée |
| E3.4 | Prairie inondable extensive |
| E3.5 | Prairie à molinie exploitée |
| E4.1 | Combe à neige calcaire |
| E4.2 | Lande alpine ventée |
| E4.3 | Pelouse à laîche courbée |
| E4.4 | Pelouse à laîche ferme |
| E4.5 | Pâturage gras alpin |
| E5.1 | Stations rudérales fraîches à humides |
| E5.2 | Lisières forestières oligo- à eutrophes |
| E5.3 | Peuplements monospécifiques (fougère aigle) |
| E5.4 | Ourlets riverains herbacés naturels |
| E5.5 | Mégaphorbiaie subalpine |
| E6.1 | Prés salés de l'intérieur |
| E7.1 | Forêt pâturée à usage traditionnel |
| E7.2 | Forêt pâturée à usage traditionnel |
| E7.3 | Forêt pâturée à usage traditionnel |
| F2.1 | Fourré de saules nains |
| F2.2 | Fourré à rhododendron |
| F2.3 | Aulnaie verte |
| F2.4 | Fourré de pin couché |
| F3.1 | Autre fourré des stations fraîches |
| F3.2 | Autre fourré des stations sèches et chaudes |
| F4.1 | Lande tourbeuse intacte |
| F4.2 | Lande à callune intacte |
| F5.1 | Autre fourré des stations sèches et chaudes |
| F5.2 | Autre fourré des stations sèches et chaudes |
| F5.3 | Autre fourré des stations sèches et chaudes |
| F5.4 | Autre fourré des stations sèches et chaudes, genêts compris |
| F5.5 | Autre fourré des stations sèches et chaudes |
| F6.1 | Fourré nain des stations sèches : aucun type BKompV de garrigue |
| F6.6 | Fourré nain des stations sèches : aucun type BKompV de garrigue |
| F6.8 | Autre fourré des stations sèches et chaudes |
| F7.1 | Lande de montagne |
| F7.2 | Lande de montagne |
| F7.4 | Lande de montagne |
| F9.1 | Fourré de saules alluvial |
| F9.2 | Fourré de tourbière |
| F9.3 | Fourré de saules alluvial |
| FA.1 | Plantations et haies d'essences non autochtones, stade moyen (convention C-H5) |
| FA.2 | Haie autochtone taillée, sans arbres de haut jet |
| FA.3 | Haie autochtone avec arbres de haut jet de stade moyen (convention C-H5) |
| FA.4 | Haie autochtone jeune, sans arbres de haut jet |
| FB.1 | Plantations ligneuses |
| FB.2 | Plantations ligneuses |
| FB.3 | Plantations ligneuses |
| FB.4 | Vigne en terrain plat ou faiblement incliné |
| G1.1 | Forêt alluviale à bois tendre à dynamique naturelle, stade moyen (convention C-H5) |
| G1.2 | Forêt alluviale à bois dur à dynamique naturelle, stade moyen |
| G1.3 | Forêt alluviale à bois tendre, stade moyen |
| G1.4 | Aulnaie marécageuse à régime hydrique intact, stade moyen |
| G1.5 | Boulaie marécageuse à régime hydrique intact, stade moyen |
| G1.6 | Hêtraie des stations fraîches, stade moyen |
| G1.7 | Chênaie sèche, stade moyen |
| G1.8 | Chênaie des stations fraîches à humides, stade moyen |
| G1.9 | Pré-bois des stations fraîches |
| G1.A | Chênaie-charmaie, stade moyen |
| G1.B | Forêt marécageuse intacte, stade moyen |
| G1.C | Plantation de feuillus d'essences introduites, stade moyen |
| G1.D | Verger de haute tige sur prairie, arbres moyens à âgés ; un verger intensif est saisi en FB.3 |
| G2.1 | Chênaie sèche, stade moyen : aucun type BKompV méditerranéen |
| G2.2 | Chênaie sèche, stade moyen |
| G2.4 | Chênaie sèche, stade moyen |
| G2.6 | Hêtraie des stations fraîches, stade moyen |
| G2.8 | Plantation de feuillus d'essences introduites, stade moyen |
| G2.9 | Verger traditionnel, arbres moyens à âgés |
| G3.1 | Sapinière-pessière montagnarde, stade moyen |
| G3.2 | Mélézein-cembraie subalpin, stade moyen |
| G3.3 | Pinède sèche des rochers, stade moyen |
| G3.4 | Pinède sèche sur sable, stade moyen |
| G3.5 | Pinède sèche des rochers, stade moyen |
| G3.7 | Pinède sèche des rochers, stade moyen |
| G3.9 | Pinède sèche des rochers, stade moyen : aucun type BKompV d'ifs ou de genévriers arborescents |
| G3.E | Pinède tourbeuse, stade moyen |
| G3.F | Plantation de résineux d'essences introduites, stade moyen |
| G4.1 | Forêt marécageuse intacte, stade moyen |
| G4.6 | Hêtraie-sapinière montagnarde, stade moyen |
| G4.8 | Hêtraie mêlée des stations fraîches, stade moyen |
| G4.9 | Hêtraie mêlée des stations fraîches, stade moyen |
| G4.B | Chênaie sèche, stade moyen |
| G4.C | Chênaie sèche, stade moyen |
| G4.D | Chênaie sèche, stade moyen |
| G4.E | Chênaie sèche, stade moyen |
| G4.F | Plantation mixte d'essences indigènes, stade moyen |
| G5.1 | Arbres isolés et alignements d'essences autochtones, stade moyen ; en ville, saisir VB.18a ou VB.18b |
| G5.2 | Bosquet des stations fraîches, stade moyen |
| G5.3 | Bosquet des stations sèches, stade moyen |
| G5.4 | Plantation de résineux indigènes, stade moyen |
| G5.5 | Bosquet des stations fraîches, stade moyen |
| G5.6 | Pré-bois des stations fraîches |
| G5.7 | Plantation de feuillus, stade jeune |
| G5.8 | Coupes et végétation des clairières |
| H2.3 | Éboulis naturels |
| H2.4 | Éboulis naturels |
| H2.5 | Éboulis naturels |
| H2.6 | Éboulis naturels |
| H3.1 | Rochers naturels |
| H3.2 | Rochers naturels |
| H3.4 | Rochers naturels |
| H3.5 | Rochers naturels |
| H3.6 | Rochers naturels |
| H5.2 | Éboulis siliceux subalpins à alpins |
| H5.3 | Surface sableuse sans ou presque sans végétation ; un sol nu de chantier est saisi en VB.10 |
| H5.4 | Dépôts de tourbe |
| H5.5 | Coupes et végétation des clairières |
| H5.6 | Chemin non stabilisé |
| I1.1 | Culture sur sol limoneux ou argileux à flore adventice appauvrie |
| I1.2 | Culture sur sol limoneux ou argileux à flore adventice appauvrie |
| I1.3 | Culture sur sol limoneux ou argileux à flore adventice riche |
| I1.4 | Culture sur sol tourbeux à flore adventice appauvrie |
| I1.5 | Jachère sur sol limoneux ou argileux |
| I2.1 | Parc entretenu intensivement avec arbres anciens |
| I2.3 | Jardins riches en structures |

### 2.2 Valeurs des habitats

Les valeurs des habitats sont construites par `outils/construire_habitats.py` depuis l'annexe 2 de la BKompV et le tableur statutaire anglais 1.0.4 : aucune n'est saisie à la main. Les tableaux synoptiques ci-dessous les regroupent par type ; le registre qui suit donne chaque valeur avec sa référence précise.

#### Valeurs intrinsèques et stades

| Code | Libellé | Valeur | Stade J | Stade M | Stade A | Difficulté de création | Difficulté d'amélioration |
|---|---|---|---|---|---|---|---|
| VB.1 | Surface bâtie (emprise de construction) | 0 |  |  |  | 1 | 1 |
| VB.2 | Surface imperméabilisée non bâtie (voirie, parking, dallage étanche) | 0 |  |  |  | 1 | 1 |
| VB.3 | Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés) | 0,1667 |  |  |  | 1 | 1 |
| VB.4 | Revêtement perméable végétalisé (dalles alvéolées engazonnées) | 0,125 |  |  |  | 1 | 1 |
| VB.5 | Pelouse d'agrément tondue, terrain de sport engazonné | 0,3333 |  |  |  | 1 | 1 |
| VB.6 | Massif ornemental horticole, couvre-sol planté | 0,375 |  |  |  | 1 | 1 |
| VB.7 | Jardin domestique végétalisé | 0,4583 |  |  |  | 1 | 1 |
| VB.8 | Friche urbaine herbacée | 0,5 |  |  |  | 0,67 | 0,67 |
| VB.9 | Friche urbaine arbustive (plus de 50 % de ligneux) | 0,5 |  |  |  | 1 | 1 |
| VB.10 | Sol nu, chantier, terrassement | 0,125 |  |  |  | 1 | 1 |
| VB.11 | Toiture végétalisée extensive (substrat de moins de 15 cm) | 0,2639 |  |  |  | 1 | 1 |
| VB.12 | Toiture végétalisée semi-intensive ou biodiverse (15 à 30 cm) | 0,5278 |  |  |  | 0,67 | 0,67 |
| VB.13 | Toiture végétalisée intensive (plus de 30 cm) | 0,2639 |  |  |  | 1 | 1 |
| VB.15 | Façade végétalisée enracinée au sol (plantes grimpantes) | 0,2639 |  |  |  | 0,67 | 0,67 |
| VB.16 | Façade végétalisée hors sol (bacs, modules) | 0,2639 |  |  |  | 0,67 | 0,67 |
| VB.18a | Arbre isolé ou alignement d'essence indigène | 0,625 | 0,4583 | 0,625 | 0,75 | 1 | 1 |
| VB.18b | Arbre isolé ou alignement d'essence non indigène | 0,4583 | 0,3333 | 0,4583 | 0,5833 | 1 | 1 |
| VB.19 | Noue, jardin de pluie, bassin paysager alimenté en eau de pluie | 0,5417 |  |  |  | 1 | 1 |
| VB.20 | Mare créée ou plan d'eau à berges naturelles | 0,625 |  |  |  | 1 | 0,67 |
| VB.21 | Bassin, fontaine ou plan d'eau à eau traitée | 0,2083 |  |  |  | 1 | 0,33 |
| VB.22 | Potager, jardin partagé, jardin familial | 0,4583 |  |  |  | 1 | 1 |
| VB.23 | Jardinière, bac et plantation hors sol au niveau du sol | 0,2639 |  |  |  | 1 | 1 |
| VB.24 | Bassin de rétention sec ou en eau, non paysager | 0,2083 |  |  |  | 0,67 | 0,67 |
| VB.25 | Voie ferrée, ballast | 0,0417 |  |  |  | 1 | 1 |
| VB.26 | Prairie urbaine extensive, fauche tardive | 0,625 |  |  |  | 1 | 1 |
| C1.1 | Lacs, étangs et mares oligotrophes permanents | 0,9167 |  |  |  | 0,33 | 0,67 |
| C1.2 | Lacs, étangs et mares mésotrophes permanents | 0,7917 |  |  |  | 0,33 | 0,33 |
| C1.3 | Lacs, étangs et mares eutrophes permanents | 0,6667 |  |  |  | 0,33 | 0,33 |
| C1.4 | Lacs, étangs et mares permanents dystrophes | 0,8333 |  |  |  | 0,33 | 0,33 |
| C1.5 | Lacs, étangs et mares continentaux salés et saumâtres permanents | 0,875 |  |  |  | 0,33 | 0,33 |
| C1.6 | Lacs, étangs et mares temporaires | 0,7917 |  |  |  | 0,67 | 0,67 |
| C2.1 | Sources, ruisseaux de sources | 0,9167 |  |  |  | 0,67 | 0,67 |
| C2.2 | Cours d'eau permanents à écoulement rapide | 0,9167 |  |  |  | 0,67 | 0,67 |
| C2.3 | Cours d'eau permanents à débit régulier | 0,9167 |  |  |  | 0,67 | 0,67 |
| C2.4 | Fleuves et rivières tidaux en amont de l'estuaire | 0,9167 |  |  |  | 0,67 | 0,67 |
| C2.5 | Eaux courantes temporaires | 0,8333 |  |  |  | 0,67 | 0,67 |
| C2.6 | Films d'eau sur les marges rocheuses d'un cours d'eau | 0,875 |  |  |  | 0,67 | 0,67 |
| C3.1 | Formations à hélophytes riches en espèces | 0,6667 |  |  |  | 0,67 | 0,67 |
| C3.2 | Roselières et formations de bordure à grands hélophytes | 0,7917 |  |  |  | 0,67 | 0,67 |
| C3.3 | Formations riveraines à grandes cannes | 0,6667 |  |  |  | 0,67 | 0,67 |
| C3.4 | Végétations amphibies lentes, pauvres en espèces | 0,75 |  |  |  | 0,67 | 0,67 |
| C3.5 | Berges périodiquement inondées à végétation pionnière | 0,75 |  |  |  | 0,67 | 0,67 |
| C3.6 | Berges nues ou clairsemées à sédiments meubles | 0,8333 |  |  |  | 1 | 0,67 |
| C3.7 | Berges nues ou clairsemées à sédiments non mobiles | 0,8333 |  |  |  | 1 | 0,67 |
| C3.8 | Habitats continentaux dépendant de la bruine | 0,9167 |  |  |  | 0,33 | 1 |
| D1.1 | Tourbières hautes | 1 |  |  |  | 0,1 | 0,33 |
| D1.2 | Tourbières de couverture | 1 |  |  |  | 0,1 | 0,33 |
| D2.1 | Tourbières de vallée | 1 |  |  |  | 0,1 | 0,33 |
| D2.2 | Bas-marais oligotrophes et tourbières des sources | 1 |  |  |  | 0,33 | 0,33 |
| D2.3 | Tourbières de transition et tremblantes | 0,9583 |  |  |  | 0,1 | 0,33 |
| D4.1 | Bas-marais riches en bases | 1 |  |  |  | 0,33 | 0,33 |
| D4.2 | Communautés riveraines des sources calcaires de montagne | 0,8333 |  |  |  | 0,33 | 0,33 |
| D5.1 | Roselières normalement sans eau libre | 0,625 |  |  |  | 0,67 | 0,67 |
| D5.2 | Formations à grandes cypéracées sans eau libre | 0,6667 |  |  |  | 0,33 | 0,33 |
| D5.3 | Zones marécageuses à grands joncs | 0,5 |  |  |  | 0,33 | 0,33 |
| D6.1 | Marais salés continentaux | 0,9167 |  |  |  | 0,33 | 0,67 |
| D6.2 | Nappes d'hélophytes saumâtres pauvres en espèces | 0,6667 |  |  |  | 0,67 | 0,67 |
| E1.1 | Végétations ouvertes des substrats sableux et rocheux | 0,8333 |  |  |  | 0,33 | 1 |
| E1.2 | Pelouses calcaires vivaces et steppes riches en bases | 0,875 |  |  |  | 0,33 | 0,33 |
| E1.3 | Pelouses xériques méditerranéennes | 0,875 |  |  |  | 0,33 | 0,33 |
| E1.4 | Steppes méditerranéennes à grandes graminées et armoises | 0,9167 |  |  |  | 0,33 | 0,33 |
| E1.5 | Pelouses méditerranéo-montagnardes | 0,875 |  |  |  | 0,33 | 0,33 |
| E1.6 | Pelouses à annuelles subnitrophiles | 0,5833 |  |  |  | 1 | 0,67 |
| E1.7 | Pelouses sèches acides et neutres fermées non méditerranéennes | 0,875 |  |  |  | 0,33 | 0,33 |
| E1.8 | Pelouses fermées sèches acides et neutres méditerranéennes | 0,875 |  |  |  | 0,33 | 0,33 |
| E1.9 | Pelouses ouvertes sèches acides et neutres non méditerranéennes | 0,8333 |  |  |  | 0,33 | 0,33 |
| E1.A | Pelouses sèches ouvertes acides et neutres méditerranéennes | 0,8333 |  |  |  | 0,33 | 0,33 |
| E1.B | Pelouses des sols métallifères | 0,875 |  |  |  | 0,1 | 0,67 |
| E1.C | Habitats méditerranéens secs à herbacées inappétentes | 0,4167 |  |  |  | 1 | 1 |
| E1.D | Pelouses xériques non exploitées | 0,7083 |  |  |  | 0,33 | 0,33 |
| E1.E | Pelouses xériques piétinées à annuelles | 0,3333 |  |  |  | 1 | 1 |
| E2.1 | Pâturages permanents mésotrophes | 0,5417 |  |  |  | 1 | 1 |
| E2.2 | Prairies de fauche de basse et moyenne altitude | 0,8333 |  |  |  | 0,33 | 0,67 |
| E2.3 | Prairies de fauche montagnardes | 0,8333 |  |  |  | 0,33 | 0,67 |
| E2.6 | Prairies améliorées, terrains de sport et pelouses ornementales | 0,3333 |  |  |  | 1 | 1 |
| E2.7 | Prairies mésiques non gérées | 0,4583 |  |  |  | 1 | 1 |
| E2.8 | Pelouses mésophiles piétinées à annuelles | 0,3333 |  |  |  | 1 | 1 |
| E3.1 | Prairies humides hautes méditerranéennes | 0,8333 |  |  |  | 0,33 | 0,33 |
| E3.2 | Prairies humides rases méditerranéennes | 0,8333 |  |  |  | 0,33 | 0,33 |
| E3.4 | Prairies eutrophes et mésotrophes humides | 0,75 |  |  |  | 0,33 | 0,67 |
| E3.5 | Prairies oligotrophes humides | 0,9583 |  |  |  | 0,33 | 0,33 |
| E4.1 | Combes à neige avec végétation | 0,7083 |  |  |  | 0,33 | 0,33 |
| E4.2 | Sommets et crêtes à mousses et lichens | 0,7917 |  |  |  | 0,33 | 0,33 |
| E4.3 | Pelouses alpines et subalpines acidiphiles | 0,7917 |  |  |  | 1 | 1 |
| E4.4 | Pelouses alpines et subalpines calcicoles | 0,7083 |  |  |  | 0,33 | 0,33 |
| E4.5 | Prairies alpines et subalpines fertilisées | 0,5833 |  |  |  | 0,33 | 0,67 |
| E5.1 | Végétations herbacées anthropiques | 0,5 |  |  |  | 1 | 0,67 |
| E5.2 | Ourlets forestiers thermophiles | 0,6667 |  |  |  | 1 | 0,67 |
| E5.3 | Formations à fougère aigle | 0,4167 |  |  |  | 1 | 1 |
| E5.4 | Lisières et prairies humides à grandes herbacées | 0,7083 |  |  |  | 0,33 | 0,33 |
| E5.5 | Formations subalpines humides à grandes herbacées | 0,6667 |  |  |  | 0,33 | 0,33 |
| E6.1 | Steppes salées intérieures méditerranéennes | 0,9167 |  |  |  | 0,33 | 0,67 |
| E7.1 | Parcs boisés atlantiques | 0,9167 |  |  |  | 0,1 | 0,33 |
| E7.2 | Parcs boisés subcontinentaux | 0,9167 |  |  |  | 0,1 | 0,33 |
| E7.3 | Dehesa | 0,9167 |  |  |  | 0,1 | 0,33 |
| F2.1 | Fourrés subarctiques et alpins à saules nains | 0,6667 |  |  |  | 0,33 | 0,33 |
| F2.2 | Landes et fourrés sempervirents alpins et subalpins | 0,7083 |  |  |  | 0,33 | 0,33 |
| F2.3 | Fourrés subalpins caducifoliés | 0,625 |  |  |  | 0,33 | 0,33 |
| F2.4 | Fourrés de conifères proches de la limite des arbres | 0,625 |  |  |  | 0,33 | 0,33 |
| F3.1 | Fourrés tempérés | 0,5417 |  |  |  | 1 | 1 |
| F3.2 | Fourrés caducifoliés subméditerranéens | 0,6667 |  |  |  | 1 | 1 |
| F4.1 | Landes humides | 0,9167 |  |  |  | 0,33 | 0,67 |
| F4.2 | Landes sèches | 0,7917 |  |  |  | 0,33 | 0,67 |
| F5.1 | Matorrals arborescents | 0,6667 |  |  |  | 1 | 1 |
| F5.2 | Maquis | 0,6667 |  |  |  | 1 | 1 |
| F5.3 | Pseudo-maquis | 0,6667 |  |  |  | 1 | 1 |
| F5.4 | Fourrés à genêt d'Espagne | 0,6667 |  |  |  | 1 | 1 |
| F5.5 | Fourrés thermoméditerranéens | 0,6667 |  |  |  | 1 | 1 |
| F6.1 | Garrigues occidentales | 0,75 |  |  |  | 0,33 | 0,67 |
| F6.6 | Garrigues supraméditerranéennes | 0,75 |  |  |  | 0,33 | 0,67 |
| F6.8 | Fourrés xérohalophiles | 0,6667 |  |  |  | 1 | 1 |
| F7.1 | Landes épineuses ouest-méditerranéennes | 0,75 |  |  |  | 0,67 | 0,67 |
| F7.2 | Landes épineuses centro-méditerranéennes | 0,75 |  |  |  | 0,67 | 0,67 |
| F7.4 | Landes-hérisson | 0,75 |  |  |  | 0,67 | 0,67 |
| F9.1 | Fourrés ripicoles | 0,6667 |  |  |  | 0,67 | 1 |
| F9.2 | Saussaies marécageuses et fourrés de bas-marais | 0,6667 |  |  |  | 0,67 | 1 |
| F9.3 | Galeries et fourrés riverains méridionaux | 0,6667 |  |  |  | 0,67 | 1 |
| FA.1 | Haies d'espèces non indigènes | 0,4583 | 0,3333 | 0,4583 | 0,5833 | 1 |  |
| FA.2 | Haies d'espèces indigènes fortement gérées | 0,5 | 0,5 | 0,6667 | 0,7917 | 1 |  |
| FA.3 | Haies d'espèces indigènes riches en espèces | 0,6667 | 0,5 | 0,6667 | 0,7917 | 1 |  |
| FA.4 | Haies d'espèces indigènes pauvres en espèces | 0,5 | 0,5 | 0,6667 | 0,7917 | 1 |  |
| FB.1 | Plantations d'arbustes pour la récolte de la plante entière | 0,25 |  |  |  | 1 | 1 |
| FB.2 | Plantations d'arbustes pour la récolte de feuilles et de branches | 0,25 |  |  |  | 1 | 1 |
| FB.3 | Plantations d'arbustes ornementaux ou fruitiers | 0,25 |  |  |  | 1 | 1 |
| FB.4 | Vignobles | 0,375 |  |  |  | 1 | 1 |
| G1.1 | Forêts riveraines à aulnes, peupliers ou saules | 0,8333 | 0,5833 | 0,8333 | 0,9583 | 0,67 | 0,67 |
| G1.2 | Forêts riveraines mixtes des plaines inondables | 0,8333 | 0,5833 | 0,8333 | 0,9167 | 0,67 | 0,67 |
| G1.3 | Forêts riveraines méditerranéennes | 0,8333 | 0,5833 | 0,8333 | 0,9583 | 0,67 | 0,67 |
| G1.4 | Forêts marécageuses de feuillus hors tourbe acide | 0,8333 | 0,5833 | 0,8333 | 0,9583 | 0,67 | 0,67 |
| G1.5 | Forêts marécageuses de feuillus sur tourbe acide | 0,8333 | 0,5833 | 0,8333 | 1 | 0,67 | 0,67 |
| G1.6 | Hêtraies | 0,7083 | 0,5833 | 0,7083 | 0,8333 | 0,33 | 0,33 |
| G1.7 | Forêts caducifoliées thermophiles | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G1.8 | Boisements acidophiles à chênes | 0,8333 | 0,625 | 0,8333 | 0,9583 | 0,33 | 0,33 |
| G1.9 | Boisements non riverains à bouleaux, trembles ou sorbiers | 0,5417 |  |  |  | 0,67 | 0,67 |
| G1.A | Boisements mésotrophes et eutrophes à chênes, charmes, frênes, érables | 0,8333 | 0,625 | 0,8333 | 0,9583 | 0,33 | 0,33 |
| G1.B | Aulnaies non riveraines | 0,75 | 0,625 | 0,75 | 0,875 | 0,67 | 0,67 |
| G1.C | Plantations forestières très artificielles de feuillus caducifoliés | 0,5 | 0,375 | 0,5 | 0,5833 | 1 | 1 |
| G1.D | Vergers d'arbres fruitiers et à noix | 0,7917 |  |  |  | 1 | 0,67 |
| G2.1 | Forêts méditerranéennes de chênes sempervirents | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G2.2 | Forêts sclérophylles continentales | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G2.4 | Boisements à caroubier et olivier | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G2.6 | Bois de houx | 0,7083 | 0,5833 | 0,7083 | 0,8333 | 0,33 | 0,33 |
| G2.8 | Plantations forestières de feuillus sempervirents | 0,5 | 0,375 | 0,5 | 0,5833 | 1 | 1 |
| G2.9 | Vergers et bosquets sempervirents (oliveraies) | 0,7917 |  |  |  | 1 | 0,67 |
| G3.1 | Boisements à épicéas et sapins | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G3.2 | Boisements alpins à mélèze et pin cembro | 0,75 | 0,625 | 0,75 | 0,875 | 0,33 | 0,33 |
| G3.3 | Pinèdes à pin à crochets | 0,7083 | 0,5833 | 0,7083 | 0,875 | 0,33 | 0,33 |
| G3.4 | Pinèdes à pin sylvestre | 0,7917 | 0,5833 | 0,7917 | 0,9167 | 0,67 | 0,67 |
| G3.5 | Pinèdes à pin noir | 0,7083 | 0,5833 | 0,7083 | 0,875 | 0,67 | 0,67 |
| G3.7 | Pinèdes méditerranéennes hors pin noir | 0,7083 | 0,5833 | 0,7083 | 0,875 | 0,67 | 0,67 |
| G3.9 | Bois de cupressacées ou de taxacées | 0,7083 | 0,5833 | 0,7083 | 0,875 | 0,33 | 0,33 |
| G3.E | Forêts de conifères des tourbières | 0,8333 | 0,5833 | 0,8333 | 0,9583 | 0,67 | 0,67 |
| G3.F | Plantations très artificielles de conifères | 0,4167 | 0,25 | 0,4167 | 0,5 | 1 | 1 |
| G4.1 | Forêts mixtes marécageuses | 0,75 | 0,625 | 0,75 | 0,875 | 0,67 | 0,67 |
| G4.6 | Forêts mixtes à sapin, épicéa et hêtre | 0,75 | 0,625 | 0,75 | 0,875 | 1 | 1 |
| G4.8 | Forêts mixtes non riveraines de feuillus et de conifères | 0,7083 | 0,5833 | 0,7083 | 0,8333 | 1 | 1 |
| G4.9 | Forêts caducifoliées mixtes avec cupressacées ou taxacées | 0,7083 | 0,5833 | 0,7083 | 0,8333 | 1 | 1 |
| G4.B | Forêts mixtes méditerranéennes de pins et de chênes | 0,75 | 0,625 | 0,75 | 0,875 | 1 | 1 |
| G4.C | Boisements mixtes à pin sylvestre et chênes thermophiles | 0,75 | 0,625 | 0,75 | 0,875 | 1 | 1 |
| G4.D | Forêts mixtes de pin noir et de chênes sempervirents | 0,75 | 0,625 | 0,75 | 0,875 | 1 | 1 |
| G4.E | Forêts mixtes de pins méditerranéens et de chênes sempervirents | 0,75 | 0,625 | 0,75 | 0,875 | 1 | 1 |
| G4.F | Plantations forestières mixtes | 0,4583 | 0,375 | 0,4583 | 0,5833 | 1 | 1 |
| G5.1 | Alignements d'arbres hors milieu urbain | 0,625 | 0,4583 | 0,625 | 0,75 | 1 | 1 |
| G5.2 | Petits bois anthropiques de feuillus caducifoliés | 0,5833 | 0,5417 | 0,5833 | 0,7083 | 1 | 1 |
| G5.3 | Petits bois anthropiques de feuillus sempervirents | 0,625 | 0,5833 | 0,625 | 0,75 | 1 | 1 |
| G5.4 | Petits bois anthropiques de conifères | 0,4583 | 0,375 | 0,4583 | 0,5833 | 1 | 1 |
| G5.5 | Petits bois anthropiques mixtes | 0,5833 | 0,5417 | 0,5833 | 0,7083 | 1 | 1 |
| G5.6 | Stades initiaux et régénérations des forêts | 0,5417 |  |  |  | 1 | 1 |
| G5.7 | Taillis et stades initiaux des plantations | 0,375 | 0,375 | 0,5 | 0,5833 | 1 | 1 |
| G5.8 | Coupes forestières récentes | 0,4167 |  |  |  | 0,33 | 1 |
| H2.3 | Éboulis siliceux des montagnes tempérées | 0,8333 |  |  |  | 0,33 | 1 |
| H2.4 | Éboulis calcaires des montagnes tempérées | 0,8333 |  |  |  | 0,33 | 1 |
| H2.5 | Éboulis siliceux des expositions chaudes | 0,8333 |  |  |  | 0,33 | 1 |
| H2.6 | Éboulis calcaires des expositions chaudes | 0,8333 |  |  |  | 0,33 | 1 |
| H3.1 | Falaises continentales siliceuses | 0,8333 |  |  |  | 0,33 | 1 |
| H3.2 | Falaises continentales basiques | 0,8333 |  |  |  | 0,33 | 1 |
| H3.4 | Falaises continentales humides | 0,8333 |  |  |  | 0,33 | 1 |
| H3.5 | Pavements rocheux, dont pavements calcaires | 0,8333 |  |  |  | 0,1 | 0,67 |
| H3.6 | Affleurements et rochers érodés | 0,8333 |  |  |  | 0,33 | 1 |
| H5.2 | Moraines glaciaires peu végétalisées | 0,5 |  |  |  | 0,67 | 0,67 |
| H5.3 | Substrats minéraux nus ou clairsemés d'origine naturelle | 0,75 |  |  |  | 0,67 | 0,67 |
| H5.4 | Substrats organiques secs peu végétalisés | 0,2083 |  |  |  | 1 | 0,67 |
| H5.5 | Zones incendiées peu végétalisées | 0,4167 |  |  |  | 0,33 | 1 |
| H5.6 | Zones piétinées | 0,4167 |  |  |  | 1 | 1 |
| I1.1 | Monocultures intensives | 0,25 |  |  |  | 1 | 1 |
| I1.2 | Cultures maraîchères et horticulture | 0,25 |  |  |  | 1 | 1 |
| I1.3 | Terres arables à monocultures extensives | 0,6667 |  |  |  | 1 | 1 |
| I1.4 | Cultures inondées ou inondables | 0,2083 |  |  |  | 1 | 1 |
| I1.5 | Friches, jachères et terres arables récemment abandonnées | 0,3333 |  |  |  | 1 | 0,67 |
| I2.1 | Grands jardins ornementaux et parcs | 0,5417 |  |  |  | 1 | 1 |
| I2.3 | Zones de jardins abandonnées récemment | 0,4583 |  |  |  | 1 | 1 |

#### Délais de maturité et d'amélioration, en années

| Code | Bon | Moyen | Mauvais | Sans état | Mauvais vers moyen | Mauvais vers bon | Moyen vers bon |
|---|---|---|---|---|---|---|---|
| VB.1 |  |  |  |  |  |  |  |
| VB.2 |  |  |  |  |  |  |  |
| VB.3 |  |  |  |  |  |  |  |
| VB.4 |  |  |  |  |  |  |  |
| VB.5 | 7 | 4 | 1 |  | 10 | 15 | 10 |
| VB.6 |  |  |  | 1 |  |  |  |
| VB.7 |  |  |  | 1 | 2 | 5 | 2 |
| VB.8 | 10 | 4 | 0 |  | 4 | 10 | 4 |
| VB.9 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| VB.10 | 5 | 3 | 1 |  | 1 | 1 | 1 |
| VB.11 |  |  |  | 1 |  |  |  |
| VB.12 | 10 | 5 | 1 |  | 5 | 10 | 5 |
| VB.13 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| VB.15 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| VB.16 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| VB.18a | 32 | 27 | 10 |  | 16 | 32 | 16 |
| VB.18b | 32 | 27 | 10 |  | 16 | 32 | 16 |
| VB.19 | 5 | 3 | 1 |  | 1 | 1 | 1 |
| VB.20 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| VB.21 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| VB.22 | 1 | 1 | 1 |  | 1 | 1 | 1 |
| VB.23 |  |  |  | 1 |  |  |  |
| VB.24 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| VB.25 |  |  |  |  |  |  |  |
| VB.26 | 10 | 5 | 2 |  | 10 | 15 | 10 |
| C1.1 | 30 | 10 | 5 |  | 10 | 20 | 10 |
| C1.2 | 30 | 10 | 5 |  | 10 | 30 | 20 |
| C1.3 | 30 | 10 | 5 |  | 10 | 30 | 20 |
| C1.4 | 30 | 10 | 5 |  | 10 | 30 | 20 |
| C1.5 | 30 | 10 | 5 |  | 10 | 30 | 20 |
| C1.6 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.1 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.2 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.3 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.4 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.5 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C2.6 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C3.1 | 12 | 7 | 3 |  | 7 | 12 | 7 |
| C3.2 | 12 | 7 | 3 |  | 7 | 12 | 7 |
| C3.3 | 12 | 7 | 3 |  | 7 | 12 | 7 |
| C3.4 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C3.5 | 5 | 3 | 1 |  | 4 | 8 | 4 |
| C3.6 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| C3.7 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| C3.8 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| D1.1 | 32 | 30 | 15 |  | 20 | 30 | 15 |
| D1.2 | 32 | 32 | 32 |  | 20 | 32 | 32 |
| D2.1 | 32 | 30 | 15 |  | 20 | 30 | 15 |
| D2.2 | 30 | 20 | 10 |  | 12 | 18 | 12 |
| D2.3 | 32 | 30 | 15 |  | 20 | 30 | 15 |
| D4.1 | 30 | 20 | 10 |  | 12 | 18 | 12 |
| D4.2 | 30 | 20 | 10 |  | 12 | 18 | 12 |
| D5.1 | 12 | 7 | 3 |  | 7 | 12 | 7 |
| D5.2 | 30 | 20 | 10 |  | 12 | 18 | 12 |
| D5.3 | 30 | 20 | 10 |  | 10 | 20 | 15 |
| D6.1 | 15 | 7 | 1 |  | 6 | 20 | 14 |
| D6.2 | 12 | 7 | 3 |  | 7 | 12 | 7 |
| E1.1 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| E1.2 | 20 | 10 | 5 |  | 10 | 20 | 10 |
| E1.3 | 20 | 10 | 5 |  | 10 | 20 | 10 |
| E1.4 | 20 | 10 | 5 |  | 10 | 20 | 10 |
| E1.5 | 25 | 15 | 10 |  | 15 | 20 | 10 |
| E1.6 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| E1.7 | 32 | 20 | 10 |  | 15 | 32 | 20 |
| E1.8 | 32 | 20 | 10 |  | 15 | 32 | 20 |
| E1.9 | 32 | 20 | 10 |  | 15 | 32 | 20 |
| E1.A | 32 | 20 | 10 |  | 15 | 32 | 20 |
| E1.B | 10 | 5 | 2 |  | 3 | 8 | 5 |
| E1.C | 10 | 5 | 2 |  | 10 | 15 | 10 |
| E1.D | 20 | 10 | 5 |  | 10 | 20 | 10 |
| E1.E | 7 | 4 | 1 |  | 10 | 15 | 10 |
| E2.1 | 10 | 5 | 2 |  | 10 | 15 | 10 |
| E2.2 | 15 | 10 | 5 |  | 8 | 15 | 8 |
| E2.3 | 20 | 15 | 10 |  | 15 | 20 | 15 |
| E2.6 | 7 | 4 | 1 |  | 10 | 15 | 10 |
| E2.7 | 10 | 5 | 2 |  | 10 | 15 | 10 |
| E2.8 | 7 | 4 | 1 |  | 10 | 15 | 10 |
| E3.1 | 30 | 20 | 10 |  | 10 | 20 | 15 |
| E3.2 | 30 | 20 | 10 |  | 10 | 20 | 15 |
| E3.4 | 20 | 10 | 5 |  | 10 | 15 | 4 |
| E3.5 | 30 | 20 | 10 |  | 10 | 20 | 15 |
| E4.1 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| E4.2 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| E4.3 | 15 | 10 | 1 |  | 10 | 15 | 10 |
| E4.4 | 25 | 15 | 10 |  | 15 | 20 | 10 |
| E4.5 | 20 | 15 | 10 |  | 15 | 20 | 15 |
| E5.1 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| E5.2 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| E5.3 |  |  |  | 1 |  |  |  |
| E5.4 | 30 | 20 | 10 |  | 20 | 30 | 10 |
| E5.5 | 30 | 20 | 10 |  | 20 | 30 | 10 |
| E6.1 | 15 | 7 | 1 |  | 6 | 20 | 14 |
| E7.1 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| E7.2 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| E7.3 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| F2.1 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| F2.2 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| F2.3 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| F2.4 | 32 | 25 | 15 |  | 32 | 32 | 32 |
| F3.1 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F3.2 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F4.1 | 32 | 20 | 10 |  | 10 | 25 | 15 |
| F4.2 | 32 | 20 | 10 |  | 10 | 25 | 15 |
| F5.1 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F5.2 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F5.3 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F5.4 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F5.5 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F6.1 | 32 | 20 | 10 |  | 10 | 25 | 15 |
| F6.6 | 32 | 20 | 10 |  | 10 | 25 | 15 |
| F6.8 | 10 | 5 | 1 |  | 5 | 10 | 3 |
| F7.1 | 30 | 20 | 10 |  | 20 | 32 | 20 |
| F7.2 | 30 | 20 | 10 |  | 20 | 32 | 20 |
| F7.4 | 30 | 20 | 10 |  | 20 | 32 | 20 |
| F9.1 | 15 | 10 | 5 |  | 7 | 15 | 7 |
| F9.2 | 15 | 10 | 5 |  | 7 | 15 | 7 |
| F9.3 | 15 | 10 | 5 |  | 7 | 15 | 7 |
| FA.1 |  |  | 1 |  |  |  |  |
| FA.2 | 12 | 5 | 1 |  |  |  |  |
| FA.3 | 12 | 5 | 1 |  |  |  |  |
| FA.4 | 12 | 5 | 1 |  |  |  |  |
| FB.1 |  |  |  | 1 |  |  |  |
| FB.2 |  |  |  | 1 |  |  |  |
| FB.3 |  |  |  | 1 |  |  |  |
| FB.4 |  |  |  | 1 |  |  |  |
| G1.1 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.2 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.3 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.4 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.5 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.6 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| G1.7 | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G1.8 | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G1.9 | 32 | 25 | 10 |  | 15 | 32 | 15 |
| G1.A | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G1.B | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G1.C | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G1.D | 30 | 20 | 5 |  | 15 | 25 | 10 |
| G2.1 | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G2.2 | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G2.4 | 32 | 32 | 10 |  | 20 | 32 | 20 |
| G2.6 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| G2.8 | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G2.9 | 30 | 20 | 5 |  | 15 | 25 | 10 |
| G3.1 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.2 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.3 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.4 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.5 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.7 | 32 | 32 | 10 |  | 15 | 32 | 15 |
| G3.9 | 32 | 32 | 10 |  | 32 | 32 | 32 |
| G3.E | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G3.F | 32 | 30 | 5 |  | 25 | 32 | 32 |
| G4.1 | 32 | 15 | 5 |  | 10 | 32 | 32 |
| G4.6 | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.8 | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.9 | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.B | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.C | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.D | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.E | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G4.F | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G5.1 | 32 | 27 | 10 |  | 16 | 32 | 16 |
| G5.2 | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G5.3 | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G5.4 | 32 | 30 | 5 |  | 25 | 32 | 32 |
| G5.5 | 32 | 30 | 5 |  | 10 | 20 | 10 |
| G5.6 | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G5.7 | 32 | 15 | 5 |  | 10 | 20 | 10 |
| G5.8 | 32 |  |  |  |  |  |  |
| H2.3 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H2.4 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H2.5 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H2.6 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H3.1 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H3.2 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H3.4 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H3.5 | 32 | 32 | 32 |  | 10 | 20 | 10 |
| H3.6 | 32 | 20 | 10 |  | 20 | 32 | 20 |
| H5.2 | 20 | 10 | 5 |  | 10 | 20 | 10 |
| H5.3 | 20 | 10 | 5 |  | 10 | 20 | 10 |
| H5.4 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| H5.5 | 32 |  |  |  |  |  |  |
| H5.6 |  |  |  |  |  |  |  |
| I1.1 |  |  |  | 1 |  |  |  |
| I1.2 |  |  |  | 1 |  |  |  |
| I1.3 |  |  |  | 1 |  |  |  |
| I1.4 |  |  |  | 1 |  |  |  |
| I1.5 | 5 | 3 | 1 |  | 2 | 5 | 2 |
| I2.1 |  |  |  | 1 | 2 | 5 | 2 |
| I2.3 |  |  |  | 1 | 2 | 5 | 2 |

Une case vide signifie que la métrique anglaise ne prévoit pas ce délai (« Not Possible ») : l'habitat ne peut pas être créé ou amélioré dans cette classe d'état. Un délai de 32 ans transpose le « 30+ » anglais (convention C-T2).

#### Registre des valeurs des habitats

**VB.1 Surface bâtie (emprise de construction)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0 | m²HE/m² | 0 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.03.01, « Versiegelter Platz oder sonstiger gepflasterter Platz », Biotoptypenwert 0 sur 24 (ligne 763 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |

**VB.2 Surface imperméabilisée non bâtie (voirie, parking, dallage étanche)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0 | m²HE/m² | 0 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.01.01a, « Versiegelter oder sonstiger gepflasterter Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) », Biotoptypenwert 0 sur 24 (ligne 747 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |

**VB.3 Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,1667 | m²HE/m² | 0,15 à 0,1833 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.03.03a, « Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) », Biotoptypenwert 4 sur 24 (ligne 765 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**VB.4 Revêtement perméable végétalisé (dalles alvéolées engazonnées)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,125 | m²HE/m² | 0,1125 à 0,1375 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.03.02, « Teilbefestigter Platz (z. B. Rasengitter) », Biotoptypenwert 3 sur 24 (ligne 764 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**VB.5 Pelouse d'agrément tondue, terrain de sport engazonné**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |
| délai, bon état | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| délai, état moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |

**VB.6 Massif ornemental horticole, couvre-sol planté**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.07a.02, « Sonstige Grünanlage ohne alten Baumbestand », Biotoptypenwert 9 sur 24 (ligne 731 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 72, « Urban - Introduced shrub », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 95, « Urban - Introduced shrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 95, « Urban - Introduced shrub » |

**VB.7 Jardin domestique végétalisé**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |

**VB.8 Friche urbaine herbacée**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.04a.01, « – Mit wesentlichen Anteilen struktur-/artenreicher Ausprägung », Biotoptypenwert 12 sur 24 (ligne 719 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible bon |
| délai, état moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible moyen |
| délai, mauvais état | 0 | an | 0 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 96, « Urban - Open mosaic habitats on previously developed land » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 96, « Urban - Open mosaic habitats on previously developed land » |

**VB.9 Friche urbaine arbustive (plus de 50 % de ligneux)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.06, « Gebüsch stickstoffreicher, ruderaler Standorte und stark verbuschte Grünlandbrache (Verbuschung > 50 %) », Biotoptypenwert 12 sur 24 (ligne 440 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**VB.10 Sol nu, chantier, terrassement**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,125 | m²HE/m² | 0,1125 à 0,1375 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.11.09a, « Bauflächen und Baustelleneinrichtungsflächen », Biotoptypenwert 3 sur 24 (ligne 289 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 80, « Urban - Bare ground », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 80, « Urban - Bare ground », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 80, « Urban - Bare ground », condition cible mauvais |
| amélioration, mauvais vers moyen | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 81, « Urban - Bare ground », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 81, « Urban - Bare ground », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 81, « Urban - Bare ground », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 82, « Urban - Bare ground » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 82, « Urban - Bare ground » |

**VB.11 Toiture végétalisée extensive (substrat de moins de 15 cm)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2639 | m²HE/m² | 0,1319 à 0,3958 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 66, « Urban - Other green roof », distinctivité 2 sur 8, multipliée par le rapport C-H3 |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 67, « Urban - Other green roof », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 90, « Urban - Other green roof » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 90, « Urban - Other green roof » |

**VB.12 Toiture végétalisée semi-intensive ou biodiverse (15 à 30 cm)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5278 | m²HE/m² | 0,2639 à 0,7917 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 70, « Urban - Biodiverse green roof », distinctivité 4 sur 8, multipliée par le rapport C-H3 |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 94, « Urban - Biodiverse green roof » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 94, « Urban - Biodiverse green roof » |

**VB.13 Toiture végétalisée intensive (plus de 30 cm)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2639 | m²HE/m² | 0,1319 à 0,3958 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 62, « Urban - Intensive green roof », distinctivité 2 sur 8, multipliée par le rapport C-H3 |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 86, « Urban - Intensive green roof » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 86, « Urban - Intensive green roof » |

**VB.15 Façade végétalisée enracinée au sol (plantes grimpantes)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2639 | m²HE/m² | 0,1319 à 0,3958 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 68, « Urban - Ground based green wall », distinctivité 2 sur 8, multipliée par le rapport C-H3 |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 92, « Urban - Ground based green wall » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 92, « Urban - Ground based green wall » |

**VB.16 Façade végétalisée hors sol (bacs, modules)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2639 | m²HE/m² | 0,1319 à 0,3958 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 67, « Urban - Facade-bound green wall », distinctivité 2 sur 8, multipliée par le rapport C-H3 |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 91, « Urban - Facade-bound green wall » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 91, « Urban - Facade-bound green wall » |

**VB.18a Arbre isolé ou alignement d'essence indigène**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aM, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 474 de l'extraction) |
| valeur, stade jeune | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aJ, « – Junge Ausprägung », 11 sur 24 |
| valeur, stade moyen | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aM, « – Mittlere Ausprägung », 15 sur 24 |
| valeur, stade âgé | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aA, « – Alte Ausprägung », 18 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible bon |
| délai, état moyen | 27 | an | 24,3 à 29,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible mauvais |
| amélioration, mauvais vers moyen | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 99, « Individual trees - Urban tree » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 99, « Individual trees - Urban tree » |

**VB.18b Arbre isolé ou alignement d'essence non indigène**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05bM, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 11 sur 24 (ligne 478 de l'extraction) |
| valeur, stade jeune | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05bJ, « – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken », 8 sur 24 |
| valeur, stade moyen | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05bM, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », 11 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05bA, « – Alte Ausprägung/– Mit Überhältern alter Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible bon |
| délai, état moyen | 27 | an | 24,3 à 29,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible mauvais |
| amélioration, mauvais vers moyen | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 99, « Individual trees - Urban tree » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 99, « Individual trees - Urban tree » |

**VB.19 Noue, jardin de pluie, bassin paysager alimenté en eau de pluie**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.05.01a.01, « – Naturnahe Ausbildung/ohne oder mit extensiver Unterhaltung », Biotoptypenwert 13 sur 24 (ligne 194 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 74, « Urban - Rain garden », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 74, « Urban - Rain garden », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 74, « Urban - Rain garden », condition cible mauvais |
| amélioration, mauvais vers moyen | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 75, « Urban - Rain garden », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 75, « Urban - Rain garden », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 75, « Urban - Rain garden », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 97, « Urban - Rain garden » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 97, « Urban - Rain garden » |

**VB.20 Mare créée ou plan d'eau à berges naturelles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.04c, « Naturnahe eutrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) », Biotoptypenwert 15 sur 24 (ligne 232 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 60, « Lakes - Ponds (non-priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 60, « Lakes - Ponds (non-priority habitat) » |

**VB.21 Bassin, fontaine ou plan d'eau à eau traitée**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2083 | m²HE/m² | 0,1875 à 0,2292 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.07.05, « Zier- und Löschteich », Biotoptypenwert 5 sur 24 (ligne 242 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 54, « Lakes - Ornamental lake or pond » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 54, « Lakes - Ornamental lake or pond » |

**VB.22 Potager, jardin partagé, jardin familial**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |
| délai, bon état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 59, « Urban - Allotments », condition cible bon |
| délai, état moyen | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 59, « Urban - Allotments », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 59, « Urban - Allotments », condition cible mauvais |
| amélioration, mauvais vers moyen | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 60, « Urban - Allotments », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 60, « Urban - Allotments », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 60, « Urban - Allotments », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 83, « Urban - Allotments » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 83, « Urban - Allotments » |

**VB.23 Jardinière, bac et plantation hors sol au niveau du sol**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2639 | m²HE/m² | 0,1319 à 0,3958 | convention | C-H3 | Statutory Biodiversity Metric 1.0.4 (Defra, Natural England), onglet G-1, ligne 69, « Urban - Ground level planters », distinctivité 2 sur 8, multipliée par le rapport C-H3 |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 70, « Urban - Ground level planters », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 93, « Urban - Ground level planters » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 93, « Urban - Ground level planters » |

**VB.24 Bassin de rétention sec ou en eau, non paysager**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2083 | m²HE/m² | 0,1875 à 0,2292 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.07.08, « Offene Wasserrückhaltebecken », Biotoptypenwert 5 sur 24 (ligne 245 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 100, « Urban - Sustainable drainage system » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 100, « Urban - Sustainable drainage system » |

**VB.25 Voie ferrée, ballast**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,0417 | m²HE/m² | 0,0375 à 0,0458 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.04.01, « Gleiskörper », Biotoptypenwert 1 sur 24 (ligne 768 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 87, « Urban - Built linear features » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 87, « Urban - Built linear features » |

**VB.26 Prairie urbaine extensive, fauche tardive**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.07b.01, « Mäßig artenreiche, frische Mähwiese », Biotoptypenwert 15 sur 24 (ligne 341 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| délai, mauvais état | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**C1.1 Lacs, étangs et mares oligotrophes permanents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.02a, « Natürliche oligotrophe Gewässer », Biotoptypenwert 22 sur 24 (ligne 223 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 56, « Lakes - Low alkalinity lakes » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 56, « Lakes - Low alkalinity lakes » |

**C1.2 Lacs, étangs et mares mésotrophes permanents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.03b, « Sonstige natürliche mesotrophe Gewässer », Biotoptypenwert 19 sur 24 (ligne 227 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 58, « Lakes - Moderate alkalinity lakes » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 58, « Lakes - Moderate alkalinity lakes » |

**C1.3 Lacs, étangs et mares eutrophes permanents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.04b, « Sonstige natürliche eutrophe Gewässer », Biotoptypenwert 16 sur 24 (ligne 231 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |

**C1.4 Lacs, étangs et mares permanents dystrophes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.01a, « Natürliche dystrophe Gewässer », Biotoptypenwert 20 sur 24 (ligne 220 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 59, « Lakes - Peat lakes » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 59, « Lakes - Peat lakes » |

**C1.5 Lacs, étangs et mares continentaux salés et saumâtres permanents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.06.01, « Salzhaltiges, perennierendes, stehendes Gewässer (Binnenlandsalzstellen) », Biotoptypenwert 21 sur 24 (ligne 235 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |

**C1.6 Lacs, étangs et mares temporaires**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.09a, « Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) », Biotoptypenwert 19 sur 24 (ligne 256 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**C2.1 Sources, ruisseaux de sources**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 22.02, « Grundquellen (Limnokrenen) », Biotoptypenwert 22 sur 24 (ligne 179 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**C2.2 Cours d'eau permanents à écoulement rapide**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**C2.3 Cours d'eau permanents à débit régulier**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**C2.4 Fleuves et rivières tidaux en amont de l'estuaire**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**C2.5 Eaux courantes temporaires**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.09, « Natürliche und naturnahe temporäre Fließgewässer », Biotoptypenwert 20 sur 24 (ligne 217 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**C2.6 Films d'eau sur les marges rocheuses d'un cours d'eau**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.07.01, « Wasserfall », Biotoptypenwert 21 sur 24 (ligne 209 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**C3.1 Formations à hélophytes riches en espèces**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| délai, mauvais état | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |

**C3.2 Roselières et formations de bordure à grands hélophytes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 38.02.01, « Schilf-Wasserröhricht », Biotoptypenwert 19 sur 24 (ligne 390 de l'extraction) |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| délai, mauvais état | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |

**C3.3 Formations riveraines à grandes cannes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| délai, mauvais état | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |

**C3.4 Végétations amphibies lentes, pauvres en espèces**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 18 sur 24 (ligne 254 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**C3.5 Berges périodiquement inondées à végétation pionnière**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 24.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 18 sur 24 (ligne 254 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| amélioration, mauvais vers moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**C3.6 Berges nues ou clairsemées à sédiments meubles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 20 sur 24 (ligne 215 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**C3.7 Berges nues ou clairsemées à sédiments non mobiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 23.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 20 sur 24 (ligne 215 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**C3.8 Habitats continentaux dépendant de la bruine**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 22.03, « Sturzquellen (Rheokrenen) (inkl. Kalktuff-Sturzquelle) », Biotoptypenwert 22 sur 24 (ligne 180 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**D1.1 Tourbières hautes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 36.01, « Hochmoore (weitgehend intakt) », Biotoptypenwert 24 sur 24 (ligne 374 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 106, « Wetland - Lowland raised bog » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 106, « Wetland - Lowland raised bog » |

**D1.2 Tourbières de couverture**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 36.01, « Hochmoore (weitgehend intakt) », Biotoptypenwert 24 sur 24 (ligne 374 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible moyen |
| délai, mauvais état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 103, « Wetland - Blanket bog » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 103, « Wetland - Blanket bog » |

**D2.1 Tourbières de vallée**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 107, « Wetland - Oceanic valley mire[1] (D2.1) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 107, « Wetland - Oceanic valley mire[1] (D2.1) » |

**D2.2 Bas-marais oligotrophes et tourbières des sources**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| amélioration, mauvais vers moyen | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 18 | an | 16,2 à 19,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**D2.3 Tourbières de transition et tremblantes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 36.02, « Übergangsmoore und Zwischenmoore (weitgehend intakt) », Biotoptypenwert 23 sur 24 (ligne 375 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 110, « Wetland - Transition mires and quaking bogs (H7140) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 110, « Wetland - Transition mires and quaking bogs (H7140) » |

**D4.1 Bas-marais riches en bases**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| amélioration, mauvais vers moyen | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 18 | an | 16,2 à 19,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**D4.2 Communautés riveraines des sources calcaires de montagne**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 22.01.02, « Kalkreiche Sicker- und Sumpfquellen (Helokrenen) (inkl. Kalktuff-Sicker- und -Sumpfquelle) », Biotoptypenwert 20 sur 24 (ligne 178 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| amélioration, mauvais vers moyen | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 18 | an | 16,2 à 19,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**D5.1 Roselières normalement sans eau libre**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 38.02.02, « Schilf-Landröhricht », Biotoptypenwert 15 sur 24 (ligne 391 de l'extraction) |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| délai, mauvais état | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |

**D5.2 Formations à grandes cypéracées sans eau libre**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 37.02, « Nährstoffreiches Großseggenried », Biotoptypenwert 16 sur 24 (ligne 386 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| amélioration, mauvais vers moyen | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 18 | an | 16,2 à 19,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**D5.3 Zones marécageuses à grands joncs**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.02.06.03, « Brachgefallenes, artenarmes Feuchtgrünland », Biotoptypenwert 12 sur 24 (ligne 371 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**D6.1 Marais salés continentaux**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.03, « Salzgrünland des Binnenlandes », Biotoptypenwert 22 sur 24 (ligne 372 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 6 | an | 5,4 à 6,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 14 | an | 12,6 à 15,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |

**D6.2 Nappes d'hélophytes saumâtres pauvres en espèces**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| délai, mauvais état | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 109, « Wetland - Reedbeds » |

**E1.1 Végétations ouvertes des substrats sableux et rocheux**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**E1.2 Pelouses calcaires vivaces et steppes riches en bases**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.02a, « Halbtrockenrasen, beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 318 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**E1.3 Pelouses xériques méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.01, « Trockenrasen auf karbonatischem oder silikatischem Untergrund », Biotoptypenwert 21 sur 24 (ligne 316 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**E1.4 Steppes méditerranéennes à grandes graminées et armoises**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.03.01a, « Steppenrasen, beweidet oder gemäht », Biotoptypenwert 22 sur 24 (ligne 321 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**E1.5 Pelouses méditerranéo-montagnardes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.01, « Trockenrasen auf karbonatischem oder silikatischem Untergrund », Biotoptypenwert 21 sur 24 (ligne 316 de l'extraction) |
| délai, bon état | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |

**E1.6 Pelouses à annuelles subnitrophiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.06.02, « Trocken-warme Ruderalstandorte auf bindigem Boden », Biotoptypenwert 14 sur 24 (ligne 412 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**E1.7 Pelouses sèches acides et neutres fermées non méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.04.03.01a, « – Beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 326 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**E1.8 Pelouses fermées sèches acides et neutres méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.04.03.01a, « – Beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 326 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**E1.9 Pelouses ouvertes sèches acides et neutres non méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**E1.A Pelouses sèches ouvertes acides et neutres méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**E1.B Pelouses des sols métallifères**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.05.01, « Natürlicher und halbnatürlicher Schwermetallrasen », Biotoptypenwert 21 sur 24 (ligne 329 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible moyen |
| délai, mauvais état | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible mauvais |
| amélioration, mauvais vers moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 72, « Sparsely vegetated land - Calaminarian grasslands » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 72, « Sparsely vegetated land - Calaminarian grasslands » |

**E1.C Habitats méditerranéens secs à herbacées inappétentes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.07, « Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) », Biotoptypenwert 10 sur 24 (ligne 414 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| délai, mauvais état | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**E1.D Pelouses xériques non exploitées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.02b, « Halbtrockenrasen, brachgefallen bzw. ungenutzt », Biotoptypenwert 17 sur 24 (ligne 319 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**E1.E Pelouses xériques piétinées à annuelles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |
| délai, bon état | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| délai, état moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |

**E2.1 Pâturages permanents mésotrophes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.07b.02, « Mäßig artenreiche, frische (Mäh-)Weide », Biotoptypenwert 13 sur 24 (ligne 342 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| délai, mauvais état | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**E2.2 Prairies de fauche de basse et moyenne altitude**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.07a.01, « Artenreiche, frische Mähwiese », Biotoptypenwert 20 sur 24 (ligne 337 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible mauvais |
| amélioration, mauvais vers moyen | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 8 | an | 7,2 à 8,8 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 20, « Grassland - Lowland meadows » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 20, « Grassland - Lowland meadows » |

**E2.3 Prairies de fauche montagnardes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.07a.01, « Artenreiche, frische Mähwiese », Biotoptypenwert 20 sur 24 (ligne 337 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 27, « Grassland - Upland hay meadows » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 27, « Grassland - Upland hay meadows » |

**E2.6 Prairies améliorées, terrains de sport et pelouses ornementales**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.08a.01, « Intensiv genutztes, frisches Dauergrünland », Biotoptypenwert 8 sur 24 (ligne 345 de l'extraction) |
| délai, bon état | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| délai, état moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |

**E2.7 Prairies mésiques non gérées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.07b.03, « Mäßig artenreiche, frische Grünlandbrache », Biotoptypenwert 11 sur 24 (ligne 343 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| délai, mauvais état | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**E2.8 Pelouses mésophiles piétinées à annuelles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |
| délai, bon état | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| délai, état moyen | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 21, « Grassland - Modified grassland » |

**E3.1 Prairies humides hautes méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.02.03a.01, « – Bewirtschaftet », Biotoptypenwert 20 sur 24 (ligne 362 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**E3.2 Prairies humides rases méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.02.03a.01, « – Bewirtschaftet », Biotoptypenwert 20 sur 24 (ligne 362 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**E3.4 Prairies eutrophes et mésotrophes humides**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.02.05.01, « – Extensiv bewirtschaftet », Biotoptypenwert 18 sur 24 (ligne 365 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 4 | an | 3,6 à 4,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM » |

**E3.5 Prairies oligotrophes humides**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.02.01a, « – Bewirtschaftet », Biotoptypenwert 23 sur 24 (ligne 356 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**E4.1 Combes à neige avec végétation**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 64.01, « Kalkschneeboden », Biotoptypenwert 17 sur 24 (ligne 843 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**E4.2 Sommets et crêtes à mousses et lichens**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 68.01, « Alpine „Windheide“ (z. B. mit Gamsheide) », Biotoptypenwert 19 sur 24 (ligne 863 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**E4.3 Pelouses alpines et subalpines acidiphiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 66.09, « Krummseggenrasen », Biotoptypenwert 19 sur 24 (ligne 858 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 25, « Grassland - Upland acid grassland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 25, « Grassland - Upland acid grassland » |

**E4.4 Pelouses alpines et subalpines calcicoles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 66.02, « Polsterseggenrasen », Biotoptypenwert 17 sur 24 (ligne 851 de l'extraction) |
| délai, bon état | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |

**E4.5 Prairies alpines et subalpines fertilisées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 66.06, « Alpenfettweide », Biotoptypenwert 14 sur 24 (ligne 855 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 27, « Grassland - Upland hay meadows » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 27, « Grassland - Upland hay meadows » |

**E5.1 Végétations herbacées anthropiques**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.06.03, « Frische bis nasse Ruderalstandorte », Biotoptypenwert 12 sur 24 (ligne 413 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**E5.2 Ourlets forestiers thermophiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.01.01, « Wald- und Gehölzsäume oligo- bis eutropher, trockener bis nasser Standorte », Biotoptypenwert 16 sur 24 (ligne 399 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 80, « Sparsely vegetated land - Tall forbs » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 80, « Sparsely vegetated land - Tall forbs » |

**E5.3 Formations à fougère aigle**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.07, « Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) », Biotoptypenwert 10 sur 24 (ligne 414 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 15, « Grassland - Bracken », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 16, « Grassland - Bracken » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 16, « Grassland - Bracken » |

**E5.4 Lisières et prairies humides à grandes herbacées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.04a.01, « – Naturnahe Ausprägung », Biotoptypenwert 17 sur 24 (ligne 407 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |

**E5.5 Formations subalpines humides à grandes herbacées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 67.01, « Hochstauden- und Hochgrasflur der hochmontanen bis alpinen Stufe », Biotoptypenwert 16 sur 24 (ligne 860 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |

**E6.1 Steppes salées intérieures méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 35.03, « Salzgrünland des Binnenlandes », Biotoptypenwert 22 sur 24 (ligne 372 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible bon |
| délai, état moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible mauvais |
| amélioration, mauvais vers moyen | 6 | an | 5,4 à 6,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 14 | an | 12,6 à 15,4 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |

**E7.1 Parcs boisés atlantiques**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**E7.2 Parcs boisés subcontinentaux**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**E7.3 Dehesa**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**F2.1 Fourrés subarctiques et alpins à saules nains**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 69.07, « Knieweidengebüsch », Biotoptypenwert 16 sur 24 (ligne 872 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**F2.2 Landes et fourrés sempervirents alpins et subalpins**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 69.05, « Alpenrosengebüsch », Biotoptypenwert 17 sur 24 (ligne 870 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**F2.3 Fourrés subalpins caducifoliés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 69.02, « Grünerlengebüsche », Biotoptypenwert 15 sur 24 (ligne 867 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**F2.4 Fourrés de conifères proches de la limite des arbres**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 69.04, « Latschengebüsch », Biotoptypenwert 15 sur 24 (ligne 869 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| délai, mauvais état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**F3.1 Fourrés tempérés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.04.02, « Sonstiges Gebüsch frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 434 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F3.2 Fourrés caducifoliés subméditerranéens**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F4.1 Landes humides**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 40.02.01, « – Weitgehend intakt », Biotoptypenwert 22 sur 24 (ligne 418 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**F4.2 Landes sèches**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 40.03.01, « – Weitgehend intakt », Biotoptypenwert 19 sur 24 (ligne 421 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**F5.1 Matorrals arborescents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F5.2 Maquis**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F5.3 Pseudo-maquis**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F5.4 Fourrés à genêt d'Espagne**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 30, « Heathland and shrub - Gorse scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 30, « Heathland and shrub - Gorse scrub » |

**F5.5 Fourrés thermoméditerranéens**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F6.1 Garrigues occidentales**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.03, « Trockenes Zwerg- und Weichselkirschen-Gebüsch », Biotoptypenwert 18 sur 24 (ligne 438 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**F6.6 Garrigues supraméditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.03, « Trockenes Zwerg- und Weichselkirschen-Gebüsch », Biotoptypenwert 18 sur 24 (ligne 438 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**F6.8 Fourrés xérohalophiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |
| délai, bon état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**F7.1 Landes épineuses ouest-méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**F7.2 Landes épineuses centro-méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**F7.4 Landes-hérisson**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**F9.1 Fourrés ripicoles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.02, « (Weiden-)Gebüsch in Auen », Biotoptypenwert 16 sur 24 (ligne 428 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**F9.2 Saussaies marécageuses et fourrés de bas-marais**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.03.01, « Moor-Gebüsch (z. B. mit Weiden, Gagel) », Biotoptypenwert 16 sur 24 (ligne 430 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**F9.3 Galeries et fourrés riverains méridionaux**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.01.02, « (Weiden-)Gebüsch in Auen », Biotoptypenwert 16 sur 24 (ligne 428 de l'extraction) |
| délai, bon état | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| amélioration, mauvais vers moyen | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 7 | an | 6,3 à 7,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**FA.1 Haies d'espèces non indigènes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.04M, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 11 sur 24 (ligne 469 de l'extraction) |
| valeur, stade jeune | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.04J, « – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken », 8 sur 24 |
| valeur, stade moyen | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.04M, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », 11 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.04A, « – Alte Ausprägung/– Mit Überhältern alter Ausprägung », 14 sur 24 |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 15, « Non-native and ornamental hedgerow », condition mauvais |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 15, difficulté Low ; onglet G-3, table Difficulty |

**FA.2 Haies d'espèces indigènes fortement gérées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », Biotoptypenwert 12 sur 24 (ligne 464 de l'extraction) |
| valeur, stade jeune | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| valeur, stade moyen | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| valeur, stade âgé | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition mauvais |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, difficulté Low ; onglet G-3, table Difficulty |

**FA.3 Haies d'espèces indigènes riches en espèces**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 16 sur 24 (ligne 465 de l'extraction) |
| valeur, stade jeune | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| valeur, stade moyen | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| valeur, stade âgé | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 7, « Species-rich native hedgerow », condition bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 7, « Species-rich native hedgerow », condition moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 7, « Species-rich native hedgerow », condition mauvais |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 7, difficulté Low ; onglet G-3, table Difficulty |

**FA.4 Haies d'espèces indigènes pauvres en espèces**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », Biotoptypenwert 12 sur 24 (ligne 464 de l'extraction) |
| valeur, stade jeune | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| valeur, stade moyen | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| valeur, stade âgé | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |
| délai, bon état | 12 | an | 10,8 à 13,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition bon |
| délai, état moyen | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, « Native hedgerow », condition mauvais |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-6, ligne 12, difficulté Low ; onglet G-3, table Difficulty |

**FB.1 Plantations d'arbustes pour la récolte de la plante entière**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |

**FB.2 Plantations d'arbustes pour la récolte de feuilles et de branches**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |

**FB.3 Plantations d'arbustes ornementaux ou fruitiers**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 72, « Urban - Introduced shrub », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 95, « Urban - Introduced shrub » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 95, « Urban - Introduced shrub » |

**FB.4 Vignobles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.08.02, « Rebkulturen in ebener bis schwach geneigter Lage », Biotoptypenwert 9 sur 24 (ligne 502 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |

**G1.1 Forêts riveraines à aulnes, peupliers ou saules**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 565 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.2 Forêts riveraines mixtes des plaines inondables**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 573 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.03.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.03.01M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.03.01A, « – Alte Ausprägung », 22 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.3 Forêts riveraines méditerranéennes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 565 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.04.02.01A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.4 Forêts marécageuses de feuillus hors tourbe acide**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 543 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.02.01A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.5 Forêts marécageuses de feuillus sur tourbe acide**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.01.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 535 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.01.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.01.01M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 1 | m²HE/m² | 0,9 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.02.01.01A, « – Alte Ausprägung », 24 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.6 Hêtraies**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**G1.7 Forêts caducifoliées thermophiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G1.8 Boisements acidophiles à chênes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.03M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 603 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.03J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.03M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.03A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G1.9 Boisements non riverains à bouleaux, trembles ou sorbiers**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 42.03.02, « Vorwald frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 510 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible bon |
| délai, état moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 119, « Woodland and forest - Upland birchwoods » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 119, « Woodland and forest - Upland birchwoods » |

**G1.A Boisements mésotrophes et eutrophes à chênes, charmes, frênes, érables**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.02M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 599 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.02J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.02M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.02A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G1.B Aulnaies non riveraines**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 552 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G1.C Plantations forestières très artificielles de feuillus caducifoliés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10M, « – Mittlere Ausprägung », Biotoptypenwert 12 sur 24 (ligne 644 de l'extraction) |
| valeur, stade jeune | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| valeur, stade moyen | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10A, « – Alte Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G1.D Vergers d'arbres fruitiers et à noix**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.06.01.MA, « – Mit mittlerem bis altem Baumbestand », Biotoptypenwert 19 sur 24 (ligne 495 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 15, « Grassland - Traditional orchards » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 15, « Grassland - Traditional orchards » |

**G2.1 Forêts méditerranéennes de chênes sempervirents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G2.2 Forêts sclérophylles continentales**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G2.4 Boisements à caroubier et olivier**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**G2.6 Bois de houx**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**G2.8 Plantations forestières de feuillus sempervirents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10M, « – Mittlere Ausprägung », Biotoptypenwert 12 sur 24 (ligne 644 de l'extraction) |
| valeur, stade jeune | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| valeur, stade moyen | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10A, « – Alte Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G2.9 Vergers et bosquets sempervirents (oliveraies)**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.06.01.MA, « – Mit mittlerem bis altem Baumbestand », Biotoptypenwert 19 sur 24 (ligne 495 de l'extraction) |
| délai, bon état | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 15, « Grassland - Traditional orchards » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 15, « Grassland - Traditional orchards » |

**G3.1 Boisements à épicéas et sapins**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.03.03M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 692 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.03.03J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.03.03M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.03.03A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**G3.2 Boisements alpins à mélèze et pin cembro**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 70.03M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 884 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 70.03J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 70.03M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 70.03A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**G3.3 Pinèdes à pin à crochets**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**G3.4 Pinèdes à pin sylvestre**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.03M, « – Mittlere Ausprägung », Biotoptypenwert 19 sur 24 (ligne 675 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.03J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7917 | m²HE/m² | 0,7125 à 0,8708 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.03M, « – Mittlere Ausprägung », 19 sur 24 |
| valeur, stade âgé | 0,9167 | m²HE/m² | 0,825 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.03A, « – Alte Ausprägung », 22 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**G3.5 Pinèdes à pin noir**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**G3.7 Pinèdes méditerranéennes hors pin noir**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**G3.9 Bois de cupressacées ou de taxacées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| difficulté d'amélioration | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**G3.E Forêts de conifères des tourbières**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.01.02M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 654 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.01.02J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.01.02M, « – Mittlere Ausprägung », 20 sur 24 |
| valeur, stade âgé | 0,9583 | m²HE/m² | 0,8625 à 1 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.01.02A, « – Alte Ausprägung », 23 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G3.F Plantations très artificielles de conifères**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.05M, « – Mittlere Ausprägung », Biotoptypenwert 10 sur 24 (ligne 712 de l'extraction) |
| valeur, stade jeune | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.05J, « – Junge Ausprägung », 6 sur 24 |
| valeur, stade moyen | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.05M, « – Mittlere Ausprägung », 10 sur 24 |
| valeur, stade âgé | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.05A, « – Alte Ausprägung », 12 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |

**G4.1 Forêts mixtes marécageuses**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 552 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.03.01A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**G4.6 Forêts mixtes à sapin, épicéa et hêtre**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.06M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 615 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.06J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.06M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.06A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.8 Forêts mixtes non riveraines de feuillus et de conifères**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.9 Forêts caducifoliées mixtes avec cupressacées ou taxacées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| valeur, stade âgé | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.B Forêts mixtes méditerranéennes de pins et de chênes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.C Boisements mixtes à pin sylvestre et chênes thermophiles**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.D Forêts mixtes de pin noir et de chênes sempervirents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.E Forêts mixtes de pins méditerranéens et de chênes sempervirents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| valeur, stade jeune | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| valeur, stade moyen | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| valeur, stade âgé | 0,875 | m²HE/m² | 0,7875 à 0,9625 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G4.F Plantations forestières mixtes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04M, « – Mittlere Ausprägung », Biotoptypenwert 11 sur 24 (ligne 708 de l'extraction) |
| valeur, stade jeune | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04J, « – Junge Ausprägung », 9 sur 24 |
| valeur, stade moyen | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04M, « – Mittlere Ausprägung », 11 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04A, « – Alte Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G5.1 Alignements d'arbres hors milieu urbain**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aM, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 474 de l'extraction) |
| valeur, stade jeune | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aJ, « – Junge Ausprägung », 11 sur 24 |
| valeur, stade moyen | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aM, « – Mittlere Ausprägung », 15 sur 24 |
| valeur, stade âgé | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.05aA, « – Alte Ausprägung », 18 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible bon |
| délai, état moyen | 27 | an | 24,3 à 29,7 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible mauvais |
| amélioration, mauvais vers moyen | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 16 | an | 14,4 à 17,6 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 134, « Individual trees - Rural tree » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 134, « Individual trees - Rural tree » |

**G5.2 Petits bois anthropiques de feuillus caducifoliés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02M, « – Mittlere Ausprägung », Biotoptypenwert 14 sur 24 (ligne 448 de l'extraction) |
| valeur, stade jeune | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02J, « – Junge Ausprägung », 13 sur 24 |
| valeur, stade moyen | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02M, « – Mittlere Ausprägung », 14 sur 24 |
| valeur, stade âgé | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02A, « – Alte Ausprägung », 17 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G5.3 Petits bois anthropiques de feuillus sempervirents**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.03M, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 452 de l'extraction) |
| valeur, stade jeune | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.03J, « – Junge Ausprägung », 14 sur 24 |
| valeur, stade moyen | 0,625 | m²HE/m² | 0,5625 à 0,6875 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.03M, « – Mittlere Ausprägung », 15 sur 24 |
| valeur, stade âgé | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.03A, « – Alte Ausprägung », 18 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G5.4 Petits bois anthropiques de conifères**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04M, « – Mittlere Ausprägung », Biotoptypenwert 11 sur 24 (ligne 708 de l'extraction) |
| valeur, stade jeune | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04J, « – Junge Ausprägung », 9 sur 24 |
| valeur, stade moyen | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04M, « – Mittlere Ausprägung », 11 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 44.04A, « – Alte Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible mauvais |
| amélioration, mauvais vers moyen | 25 | an | 22,5 à 27,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |

**G5.5 Petits bois anthropiques mixtes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02M, « – Mittlere Ausprägung », Biotoptypenwert 14 sur 24 (ligne 448 de l'extraction) |
| valeur, stade jeune | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02J, « – Junge Ausprägung », 13 sur 24 |
| valeur, stade moyen | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02M, « – Mittlere Ausprägung », 14 sur 24 |
| valeur, stade âgé | 0,7083 | m²HE/m² | 0,6375 à 0,7792 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 41.02.02A, « – Alte Ausprägung », 17 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| délai, état moyen | 30 | an | 27 à 33 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**G5.6 Stades initiaux et régénérations des forêts**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 42.03.02, « Vorwald frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 510 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G5.7 Taillis et stades initiaux des plantations**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10J, « – Junge Ausprägung », Biotoptypenwert 9 sur 24 (ligne 643 de l'extraction) |
| valeur, stade jeune | 0,375 | m²HE/m² | 0,3375 à 0,4125 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| valeur, stade moyen | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| valeur, stade âgé | 0,5833 | m²HE/m² | 0,525 à 0,6417 | transposée | C-H5 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 43.10A, « – Alte Ausprägung », 14 sur 24 |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| délai, état moyen | 15 | an | 13,5 à 16,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**G5.8 Coupes forestières récentes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.02, « Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) », Biotoptypenwert 10 sur 24 (ligne 401 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 90, « Woodland and forest - Felled », condition cible bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 111, « Woodland and forest - Felled » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 111, « Woodland and forest - Felled » |

**H2.3 Éboulis siliceux des montagnes tempérées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H2.4 Éboulis calcaires des montagnes tempérées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H2.5 Éboulis siliceux des expositions chaudes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H2.6 Éboulis calcaires des expositions chaudes**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H3.1 Falaises continentales siliceuses**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H3.2 Falaises continentales basiques**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H3.4 Falaises continentales humides**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H3.5 Pavements rocheux, dont pavements calcaires**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible bon |
| délai, état moyen | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible moyen |
| délai, mauvais état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration moyen vers bon |
| difficulté de création | 0,1 | sans unité | 0,09 à 0,11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 76, « Sparsely vegetated land - Limestone pavement » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 76, « Sparsely vegetated land - Limestone pavement » |

**H3.6 Affleurements et rochers érodés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,8333 | m²HE/m² | 0,75 à 0,9167 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| délai, état moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| délai, mauvais état | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| amélioration, mauvais vers moyen | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**H5.2 Moraines glaciaires peu végétalisées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5 | m²HE/m² | 0,45 à 0,55 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 63.04, « Silikatschutthalde der subalpinen bis alpinen Stufe », Biotoptypenwert 12 sur 24 (ligne 841 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |

**H5.3 Substrats minéraux nus ou clairsemés d'origine naturelle**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,75 | m²HE/m² | 0,675 à 0,825 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 32.09, « Vegetationslose bzw. -arme Sandfläche », Biotoptypenwert 18 sur 24 (ligne 274 de l'extraction) |
| délai, bon état | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible bon |
| délai, état moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible moyen |
| délai, mauvais état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible mauvais |
| amélioration, mauvais vers moyen | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 20 | an | 18 à 22 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 10 | an | 9 à 11 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration moyen vers bon |
| difficulté de création | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |

**H5.4 Substrats organiques secs peu végétalisés**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2083 | m²HE/m² | 0,1875 à 0,2292 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 36.04.04, « Torfhalden », Biotoptypenwert 5 sur 24 (ligne 383 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**H5.5 Zones incendiées peu végétalisées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 39.02, « Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) », Biotoptypenwert 10 sur 24 (ligne 401 de l'extraction) |
| délai, bon état | 32 | an | 28,8 à 35,2 | transposée | C-T2 | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 90, « Woodland and forest - Felled », condition cible bon |
| difficulté de création | 0,33 | sans unité | 0,297 à 0,363 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 111, « Woodland and forest - Felled » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 111, « Woodland and forest - Felled » |

**H5.6 Zones piétinées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4167 | m²HE/m² | 0,375 à 0,4583 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 52.02.06, « Unbefestigter Weg », Biotoptypenwert 10 sur 24 (ligne 759 de l'extraction) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**I1.1 Monocultures intensives**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 33.04a.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) », Biotoptypenwert 6 sur 24 (ligne 305 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 8, « Cropland - Cereal crops », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 9, « Cropland - Cereal crops » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 9, « Cropland - Cereal crops » |

**I1.2 Cultures maraîchères et horticulture**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,25 | m²HE/m² | 0,225 à 0,275 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 33.04a.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) », Biotoptypenwert 6 sur 24 (ligne 305 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 11, « Cropland - Horticulture » |

**I1.3 Terres arables à monocultures extensives**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,6667 | m²HE/m² | 0,6 à 0,7333 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 33.04a.02, « – Acker mit artenreicher Segetalvegetaion (Lehm- oder Tonboden) », Biotoptypenwert 16 sur 24 (ligne 304 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 4, « Cropland - Arable field margins cultivated annually », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 5, « Cropland - Arable field margins cultivated annually » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 5, « Cropland - Arable field margins cultivated annually » |

**I1.4 Cultures inondées ou inondables**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,2083 | m²HE/m² | 0,1875 à 0,2292 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 33.05.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Torf- oder Anmoorboden) », Biotoptypenwert 5 sur 24 (ligne 313 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 12, « Cropland - Non-cereal crops », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 13, « Cropland - Non-cereal crops » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 13, « Cropland - Non-cereal crops » |

**I1.5 Friches, jachères et terres arables récemment abandonnées**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,3333 | m²HE/m² | 0,3 à 0,3667 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 33.04a.04, « – Ackerbrache (Lehm- oder Tonboden) », Biotoptypenwert 8 sur 24 (ligne 306 de l'extraction) |
| délai, bon état | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| délai, état moyen | 3 | an | 2,7 à 3,3 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| délai, mauvais état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| difficulté d'amélioration | 0,67 | sans unité | 0,603 à 0,737 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**I2.1 Grands jardins ornementaux et parcs**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,5417 | m²HE/m² | 0,4875 à 0,5958 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.06a.03, « Intensiv gepflegte Parkanlage mit altem Baumbestand », Biotoptypenwert 13 sur 24 (ligne 725 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |

**I2.3 Zones de jardins abandonnées récemment**

| Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|
| valeur intrinsèque | 0,4583 | m²HE/m² | 0,4125 à 0,5042 | transposée | C-H1 | BKompV Anlage 2 (BGBl. I 2020, 1088), code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |
| délai, sans état | 1 | an | 0,9 à 1,1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| amélioration, mauvais vers moyen | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| amélioration, mauvais vers bon | 5 | an | 4,5 à 5,5 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| amélioration, moyen vers bon | 2 | an | 1,8 à 2,2 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| difficulté de création | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |
| difficulté d'amélioration | 1 | sans unité | 0,9 à 1 | transposée |  | Statutory Biodiversity Metric 1.0.4, onglet G-3, ligne 102, « Urban - Vegetated garden » |

**Valeurs communes et arbres**

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| * | rapport transposition uk | 1,0556 | sans unité | 0,5278 à 1,5833 | convention | C-H3 | BKompV Anlage 2 ; Statutory Biodiversity Metric 1.0.4, G-1, médiane sur 175 types appariés de la nomenclature |
| VB.18 | surface defaut houppier petit | 40,715 | m² | 36,6435 à 44,7865 | transposée | C-H5 | Statutory Biodiversity Metric 1.0.4, onglet G-3, table Individual trees, ligne 4, Small, diamètre 0.3 m, RPA 0.004071504079052367 ha |
| VB.18 | surface defaut houppier moyen | 162,8602 | m² | 146,5741 à 179,1462 | transposée | C-H5 | Statutory Biodiversity Metric 1.0.4, onglet G-3, table Individual trees, ligne 5, Medium, diamètre 0.6 m, RPA 0.01628601631620947 ha |
| VB.18 | surface defaut houppier grand | 366,4354 | m² | 329,7918 à 403,0789 | transposée | C-H5 | Statutory Biodiversity Metric 1.0.4, onglet G-3, table Individual trees, ligne 6, Large, diamètre 0.9 m, RPA 0.03664353671147131 ha |
| VB.18 | surface defaut houppier tres grand | 764,538 | m² | 688,0842 à 840,9918 | transposée | C-H5 | Statutory Biodiversity Metric 1.0.4, onglet G-3, table Individual trees, ligne 7, Very large, diamètre 1.3 m, RPA 0.07645379881776114 ha |

### 2.3 Contexte, période et temps (`contexte.csv`)

Période de référence, actualisation, fermeture des surfaces, situation dans la trame verte et bleue, zones biogéographiques, chantier.

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| * | periode reference | 50 | an | 50 | primaire | C-T1 | Arrêté du 4 août 2021, annexe II (méthode de calcul de l'ACV RE2020), § 1 (p. 5) : la période d'étude de référence est de 50 ans pour tous les bâtiments |
| * | periode complementaire | 30 | an | 30 | primaire | C-T1 | Environment Act 2021, Schedule 14, Schedule 7A inséré dans le Town and Country Planning Act 1990, paragraphe 9(3) : maintien pendant au moins 30 ans après l'achèvement (lu le 18/10/2026) |
| * | taux actualisation | 0 | par an | 0 à 0,035 | convention | C-T5 | Statutory Biodiversity Metric 1.0.4, onglet G-4, table Year / Time to target multiplier : 0,965 par an (3,5 %), retenu seulement comme option d'étude |
| * | tolerance fermeture relative | 0,005 | fraction de la parcelle | 0,005 | convention | C-E3 | OpenNAT, convention de saisie |
| * | tolerance fermeture absolue | 1 | m² | 1 | convention | C-E3 | OpenNAT, convention de saisie |
| * | plafond valeur unitaire | 1,15 | m²HE/m² | 1,15 | convention | C-H7 | Statutory Biodiversity Metric 1.0.4, onglet G-3, multiplicateur maximal d'importance stratégique (1,15) |
| situation_reservoir | multiplicateur situation | 1,15 | sans unité | 1,1 à 1,15 | transposée | C-E1 | Statutory Biodiversity Metric 1.0.4, onglet G-3, Strategic significance : Formally identified in local strategy, High, 1,15 |
| situation_corridor | multiplicateur situation | 1,1 | sans unité | 1 à 1,15 | transposée | C-E1 | Statutory Biodiversity Metric 1.0.4, onglet G-3, Strategic significance : Location ecologically desirable, Medium, 1,10 |
| situation_hors_trame | multiplicateur situation | 1 | sans unité | 1 | transposée | C-E1 | Statutory Biodiversity Metric 1.0.4, onglet G-3, Strategic significance : not in local strategy, Low, 1 |
| zone_atlantique | multiplicateur delai | 1 | sans unité | 1 | convention | C-E2 | OpenNAT, aucune source ne module les délais de maturation par zone biogéographique en France |
| zone_continentale | multiplicateur delai | 1 | sans unité | 1 | convention | C-E2 | OpenNAT, idem |
| zone_alpine | multiplicateur delai | 1 | sans unité | 1 à 1,25 | convention | C-E2 | OpenNAT, idem |
| zone_mediterraneenne | multiplicateur delai | 1 | sans unité | 1 à 1,25 | convention | C-E2 | OpenNAT, idem, délais plus longs supposés mais non chiffrés (audit § 3, trou nommé) |
| * | reduction chantier sans protection | 0,25 | fraction de la valeur | 0,1 à 0,5 | convention | C-T4 | OpenNAT, aucune source chiffrée |
| * | duree indisponibilite renouvellement | 1 | an | 1 à 2 | convention | C-T6 | OpenNAT, aucune source chiffrée |

### 2.4 Coefficients de sol (`sols.csv`)

Natures de surface du module S et de Bnat, médianes des grilles de coefficient de biotope relevées (convention C-S1).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| S01 | coefficient sol | 0 | sans unité | 0 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0 (Versiegelte Flächen) ; London Plan Guidance 0 (Sealed surfaces) ; PLU de l'Eurométropole de Strasbourg 0 (Surface minérale imperméable) ; PLUi-HMB du Grand Annecy 0 (Surfaces imperméables) ; PLU de la Métropole européenne de Lille 0 (Surface imperméable) |
| S02 | coefficient sol | 0,2 | sans unité | 0,1 à 0,3 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.1 (Teilversiegelte Flächen (pavés, stabilisé, wassergebundene Decke)) ; Berlin 0.2 (Durchlässige Belagsflächen (dalles drainantes, sable, gravier)) ; London Plan Guidance 0.1 (Permeable paving) ; PLU de l'Eurométropole de Strasbourg 0.2 (Surface minérale perméable) ; PLUi-HMB du Grand Annecy 0.3 (Surfaces semi-perméables) ; PLU de la Métropole européenne de Lille 0.25 (Surface perméable non végétalisée) |
| S03 | coefficient sol | 0,45 | sans unité | 0,2 à 0,5 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.4 (Begrünte Belagsflächen (Rasengitter, pavés à joints engazonnés)) ; PLU de l'Eurométropole de Strasbourg 0.2 (Surface minérale perméable (pavés joints gazon)) ; PLUi-HMB du Grand Annecy 0.5 (Surfaces semi-ouvertes) ; PLU de la Métropole européenne de Lille 0.5 (Surface perméable végétalisée) |
| S04 | coefficient sol | 0,5 | sans unité | 0,3 à 0,7 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.5 (Extensive Dachbegrünung (moins de 20 cm)) ; London Plan Guidance 0.7 (Extensive green roof, au moins 80 mm (GRO Code 2014)) ; London Plan Guidance 0.3 (Extensive green roof of sedum mat) ; PLU de l'Eurométropole de Strasbourg 0.5 (Toiture végétalisée extensive de moins de 10 cm) ; PLU de l'Eurométropole de Strasbourg 0.6 (Toiture extensive ou semi-intensive de 30 cm au plus) ; PLUi-HMB du Grand Annecy 0.5 (Espaces verts sur dalle 1 (moins de 80 cm)) ; PLU de la Métropole européenne de Lille 0.5 (Toiture extensive et dalle de 15 à 20 cm, gazon ou mousse) ; PLU de la Métropole européenne de Lille 0.7 (Toiture extensive et dalle de 15 à 20 cm, végétation hors gazon et mousse) |
| S05 | coefficient sol | 0,6 | sans unité | 0,5 à 0,8 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, règle UG.4, indice de végétalisation du bâti, p. 63 (coefficients sur 10 ramenés sur 1) ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.5 (Unterbaute Vegetationsfläche, 20 à 40 cm) ; Berlin 0.7 (Einfach-intensive Dachbegrünung, 15 à 50 cm) ; London Plan Guidance 0.8 (Intensive green roof or vegetation over structure, au moins 150 mm) ; PLU de l'Eurométropole de Strasbourg 0.6 (Toiture extensive ou semi-intensive de 30 cm au plus) ; PLUi-HMB du Grand Annecy 0.5 (Espaces verts sur dalle 1 (moins de 80 cm)) ; Ville de Paris 0.6 (S3, substrat d'au moins 25 cm) ; PLU de la Métropole européenne de Lille 0.6 (Toiture semi-intensive ou intensive et dalle de plus de 20 cm) |
| S06 | coefficient sol | 0,7 | sans unité | 0,5 à 0,8 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, règle UG.4, indice de végétalisation du bâti, p. 63 (coefficients sur 10 ramenés sur 1) ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.6 (Unterbaute Vegetationsfläche, 41 à 80 cm) ; Berlin 0.8 (Intensive Dachbegrünung, plus de 50 cm) ; London Plan Guidance 0.8 (Intensive green roof or vegetation over structure, au moins 150 mm) ; PLU de l'Eurométropole de Strasbourg 0.7 (Plantations sur dalle ou toiture intensive, plus de 30 cm) ; PLUi-HMB du Grand Annecy 0.5 (Espaces verts sur dalle 1 (moins de 80 cm)) ; Ville de Paris 0.8 (S2, substrat de 50 à 80 cm) ; PLU de la Métropole européenne de Lille 0.6 (Toiture semi-intensive ou intensive et dalle de plus de 20 cm) |
| S07 | coefficient sol | 0,9 | sans unité | 0,7 à 1 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, règle UG.4, indice de végétalisation du bâti, p. 63 (coefficients sur 10 ramenés sur 1) ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.7 (Unterbaute Vegetationsfläche, 81 à 150 cm) ; Berlin 0.9 (Unterbaute Vegetationsfläche, plus de 150 cm) ; London Plan Guidance 0.8 (Intensive green roof or vegetation over structure) ; PLU de l'Eurométropole de Strasbourg 0.9 (Plantations sur dalle ou toiture, 80 cm et plus) ; PLUi-HMB du Grand Annecy 0.7 (Espaces verts sur dalle 2 (plus de 80 cm)) ; Ville de Paris 1 (S1, substrat de 80 cm et plus) ; PLU de la Métropole européenne de Lille 1 (Espace vert sur dalle d'au moins 1 m) |
| S08 | coefficient sol | 1 | sans unité | 1 | convention | C-S1 | PLUi-HMB du Grand Annecy, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre, § 1.2 ; Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 1 (Vegetationsfläche mit Bodenanschluss) ; London Plan Guidance 1 (Semi-natural vegetation) ; PLU de l'Eurométropole de Strasbourg 1 (Espaces plantés en pleine terre) ; PLUi-HMB du Grand Annecy 1 (Espaces verts en pleine terre) ; PLU de la Métropole européenne de Lille 1 (Espace vert en continuité avec la terre naturelle) |
| S09 | coefficient sol | 0,4 | sans unité | 0,2 à 0,6 | convention | C-S1 | Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, règle UG.4, indice de végétalisation du bâti, p. 63 (coefficients sur 10 ramenés sur 1) ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.5 (Bodengebundene Vertikalbegrünung (10 m au plus)) ; London Plan Guidance 0.6 (Green wall, climbers rooted in soil) ; PLU de l'Eurométropole de Strasbourg 0.4 (Aménagement végétalisé en surface verticale) ; Ville de Paris 0.2 (S5, surfaces verticales végétalisées (15 m au plus)) ; PLU de la Métropole européenne de Lille 0.4 (Végétalisation des murs aveugles (10 m au plus)) |
| S10 | coefficient sol | 0,5 | sans unité | 0,4 à 0,7 | convention | C-S1 | Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du Pacte Lille Bas Carbone, version du 18/10/2022 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9 ; PLU de l'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, modification n° 4 (mai 2024), article 9.2, p. 33 et 34, Berlin 0.7 (Wandgebundene Vertikalbegrünung (10 m imputés au plus)) ; London Plan Guidance 0.6 (Green wall, modular system) ; PLU de l'Eurométropole de Strasbourg 0.4 (Aménagement végétalisé en surface verticale) ; PLU de la Métropole européenne de Lille 0.4 (Végétalisation des murs aveugles) |
| S11 | coefficient sol | 0,6 | sans unité | 0,5 à 1 | convention | C-S1 | Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019 ; London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9, Berlin 0.5 (Wasserfläche, alimentée par l'eau de pluie) ; Berlin 0.6 (Wasserfläche avec végétation établie (+0,1)) ; London Plan Guidance 1 (Wetland or open water (semi-natural; not chlorinated)) |
| S12 | coefficient sol | 0,2 | sans unité | 0,2 | transposée | C-S1 | London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9, London Plan Guidance 0.2 (Water features (chlorinated) or unplanted detention basins) |
| S13 | coefficient sol | 0,2 | sans unité | 0,2 | transposée | C-S1 | Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019, Berlin 0.2 (Versickerungsfläche, par m² de surface extérieure infiltrée) |

### 2.5 Connectivité (`connectivite.csv`)

Effet de taille des taches, connectivité, clôtures (module C).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| * | exposant aire especes | 0,22 | sans unité | 0,16 à 0,32 | secondaire | C-C1 | Matthews et al. 2016, On the form of species-area relationships in habitat islands and true islands, Global Ecology and Biogeography 25, valeur médiane de z pour les îles d'habitat, Q1 0,16 et Q3 0,32 (lu au lot 0, audit § 2.6.1, document non récupéré le 18/10/2026) |
| * | surface reference | 44 000 | m² | 27 000 à 61 000 | primaire | C-C1 | Beninde, Veith et Hochkirch 2015, Biodiversity in cities needs space, Ecology Letters 18, Area thresholds : seuil moyen de 4,4 ha (SE 0,85, n = 13) sous lequel les espèces adaptées à la ville déclinent, plage = moyenne plus ou moins 2 SE |
| * | facteur taille minimum | 0,35 | sans unité | 0,35 à 0,45 | transposée | C-C1 | PBL 2016, GLOBIO 3.5 Technical model description (publication 2369), Table 6.1 : MSA de fragmentation 0,35 pour les taches de 0 à 1 km² |
| connexion_forte | multiplicateur connectivite | 1,15 | sans unité | 1,1 à 1,15 | transposée | C-C2 | Statutory Biodiversity Metric 1.0.4, onglet G-3, connectivity : High, Highly connected habitat, 1,15 |
| connexion_moyenne | multiplicateur connectivite | 1,1 | sans unité | 1 à 1,15 | transposée | C-C2 | Statutory Biodiversity Metric 1.0.4, onglet G-3, connectivity : Medium, Moderately connected habitat, 1,10 |
| connexion_faible | multiplicateur connectivite | 1 | sans unité | 1 | transposée | C-C2 | Statutory Biodiversity Metric 1.0.4, onglet G-3, connectivity : Low, Unconnected habitat, 1 |
| * | distance connexion | 200 | m | 100 à 500 | convention | C-C2 | OpenNAT, aucune distance de connexion chiffrée trouvée pour les petites taches urbaines (audit § 3, trou nommé) |
| * | surface minimale espace exterieur | 10 000 | m² | 5 000 à 44 000 | convention | C-C2 | OpenNAT, borne basse retenue entre l'hectare et le seuil de Beninde (4,4 ha) |
| * | facteur cloture etanche | 0,9 | sans unité | 0,8 à 1 | convention | C-C3 | OpenNAT, aucune valeur publiée de perméabilité des clôtures (audit § 3, trou nommé) |
| * | passage petite faune section | 0,0225 | m² | 0,0225 | convention | C-C3 | OpenNAT, passage de 15 cm sur 15 cm |
| * | passage petite faune espacement | 20 | m | 10 à 50 | convention | C-C3 | OpenNAT, un passage au moins tous les 20 m de clôture |

### 2.6 Nuisances (`nuisances.csv`)

Lumière artificielle, bruit, vitrages (module N).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| lumiere_aucune | facteur lumiere | 1 | sans unité | 1 | convention | C-N1 | OpenNAT, unité sans point lumineux à moins de la distance d'influence |
| lumiere_conforme | facteur lumiere | 0,9 | sans unité | 0,8 à 1 | convention | C-N1 | Arrêté du 27 décembre 2018 relatif aux nuisances lumineuses , article 3 : température de couleur de 3 000 K au plus, extinction au plus tard 1 heure après la fin de l'activité, 2 400 K dans les espaces protégés (lu sur AIDA le 18/10/2026) |
| lumiere_non_conforme | facteur lumiere | 0,75 | sans unité | 0,5 à 0,9 | secondaire | C-N1 | Azam et al. 2018, cité par EUROBATS, Rowse et al. 2018, distances d'évitement des chiroptères de 10, 25 et 50 m (lu au lot 0, audit § 2.6.2) |
| * | distance influence lumiere | 50 | m | 25 à 100 | secondaire | C-N1 | Azam et al. 2018, cité par EUROBATS, distance d'évitement maximale de 50 m (lu au lot 0, audit § 2.6.2) |
| * | seuil bruit milieu ouvert | 47 | dB(A) | 42 à 52 | secondaire | C-N2 | Reijnen et al. 1997, Disturbance by traffic of breeding birds , seuil d'effet de 47 dB(A) en prairie (lu au lot 0, audit § 2.6.3) |
| * | seuil bruit milieu boise | 42 | dB(A) | 42 à 52 | secondaire | C-N2 | Reijnen et al. 1997, seuils de 42 à 52 dB(A) en boisement, borne basse retenue (lu au lot 0, audit § 2.6.3) |
| * | facteur bruit au dela seuil | 0,7 | sans unité | 0,6 à 0,8 | secondaire | C-N2 | Reijnen et al. 1997, réduction de densité d'au moins 30 % au-delà du seuil (lu au lot 0, audit § 2.6.3) |
| * | facteur vitrage non traite | 0,95 | sans unité | 0,9 à 1 | convention | C-N3 | OpenNAT, Loss et al. 2014 pour l'ordre de grandeur des collisions (lu au lot 0), aucune relation entre surface vitrée et valeur d'habitat publiée |
| * | distance vitrage | 15 | m | 10 à 30 | convention | C-N3 | OpenNAT, aucune source chiffrée |
| * | surface vitree minimale | 10 | m² | 5 à 20 | convention | C-N3 | OpenNAT, aucune source chiffrée |

### 2.7 Eau (`eau.csv`)

Alimentation des milieux en eau, gestion des eaux pluviales (module E).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| alimentation_naturelle | facteur eau | 1 | sans unité | 1 | convention | C-E4 | Berlin, Biotopflächenfaktor (2019) , Wasserfläche : surface en eau alimentée par la pluie (facteur 0,5, + 0,1 si végétalisée) |
| alimentation_artificielle | facteur eau | 0,8 | sans unité | 0,6 à 1 | convention | C-E4 | London Plan Guidance, Urban Greening Factor (2023) , Table 3.1 : eau semi-naturelle 1 contre eau chlorée ou bassin nu 0,2 |
| * | part infiltree cible | 1 | fraction | 1 | convention | C-E5 | OpenNAT, indicateur complémentaire |

### 2.8 Matériaux et climat (`materiaux.csv`)

Facteur de caractérisation du climat, occupation des sols du bois et des carrières, indicateurs de pollution (module G).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| climat | surface terres emergees hors glaces | 1,300 x 10^14 | m² | 1,300 x 10^14 | primaire | C-G2 | GIEC 2019, rapport spécial Changement climatique et terres émergées, résumé à l'intention des décideurs, figure SPM.1, volet C : surface terrestre libre de glace 100 % = 130 Mkm² |
| climat | part cultures infrastructures | 0,13 | fraction | 0,13 | primaire | C-G2 | GIEC 2019, SRCCL, résumé à l'intention des décideurs, figure SPM.1, volet C : infrastructures 1 %, cultures irriguées 2 %, cultures non irriguées 10 % |
| climat | perte msa par degre | 0,071 | MSA par °C | 0,0356 à 0,1457 | convention | C-G2 | PBL 2016, GLOBIO 3.5 Technical model description (publication 2369), Table 3.1 (Arets et al. 2014) : pertes de MSA par °C de 15 biomes, médiane 0,071 (forêt tempérée caducifoliée), étendue 0,0356 (glace) à 0,1457 (forêt mixte chaude) |
| climat | facteur retard reponse | 2 | sans unité | 2 | primaire | C-G2 | PBL 2016, GLOBIO 3.5 Technical model description, § 3.3 : facteur de retard de 2 appliqué aux relations d'Arets et al. 2014 |
| climat | tcre | 4,500 x 10^-16 | °C par kg CO2 | 2,700 x 10^-16 à 6,300 x 10^-16 | primaire | C-G2 | GIEC 2021, AR6 groupe I, résumé à l'intention des décideurs, D.1.1 : chaque 1 000 GtCO2 d'émissions cumulées cause probablement 0,27 à 0,63 °C de réchauffement, meilleure estimation 0,45 °C |
| climat | facteur caracterisation | 0,0018 | m²HE par kg CO2 éq. et par an | 5,430 x 10^-4 à 0,0052 | convention | C-G2 | Calcul OpenNAT à partir des 5 lignes précédentes, équation G5 : 1,30e14 x (1 - 0,13) x (0,071 / 2) x 4,5e-16, plage : mêmes termes aux bornes de la TCRE et de la perte de MSA |
| phase_A1_A5 | annees persistance | 50 | an | 50 | convention | C-G3 | OpenNAT, arrêté du 4 août 2021, annexe II, période d'étude de référence de 50 ans, phases de production et de chantier émises en début de période |
| phase_B | annees persistance | 25 | an | 25 | convention | C-G3 | OpenNAT, émissions de la phase d'exploitation des composants (remplacements, entretien) réparties uniformément sur la période |
| phase_C | annees persistance | 0 | an | 0 | convention | C-G3 | OpenNAT, émissions de fin de vie en fin de période |
| phase_D | annees persistance | 0 | an | 0 | convention | C-G3 | OpenNAT, arrêté du 4 août 2021, annexe II, le module D est hors du périmètre de l'Ic construction |
| foret | production biologique | 5,4 | m³ par ha et par an | 4 à 7,5 | primaire | C-G4 | IGN, Mémento de l'inventaire forestier, édition 2024, La production biologique des arbres, p. 38 et 39 : 5,4 m³/ha/an en moyenne dans les forêts françaises (2014-2022) |
| foret | rapport bois rond produit | 2 | m³ de bois rond par m³ de produit | 1,5 à 3,1 | convention | C-G4 | OpenNAT, FCBA, Mémento 2025-2026 pour la borne haute (récolte de bois ronds de 23,7 Mm³ pour 7,7 Mm³ de sciages, lu dans un extrait, à vérifier), aucun rendement matière de sciage publié sous licence libre trouvé |
| foret_plantation | msa usage | 0,3 | MSA | 0,3 | primaire | C-G5 | PBL 2016, GLOBIO 3.5, Table 2.2 : Forest - Plantation 0,30 |
| foret_coupe_rase | msa usage | 0,5 | MSA | 0,5 | primaire | C-G5 | PBL 2016, GLOBIO 3.5, Table 2.2 : Forest - Clear-cut harvesting 0,50 |
| foret_selective | msa usage | 0,7 | MSA | 0,7 | primaire | C-G5 | PBL 2016, GLOBIO 3.5, Table 2.2 : Forest - Selective logging 0,70 |
| foret_impact_reduit | msa usage | 0,85 | MSA | 0,85 | primaire | C-G5 | PBL 2016, GLOBIO 3.5, Table 2.2 : Forest - Reduced impact logging 0,85 |
| carriere | occupation par tonne | 0,9 | m²·an par t | 0,3 à 1,6 | secondaire | C-G6 | Dossiers d'enquête publique de carrières : Pouzilhac (Gard), Valliguières (Gard), Montreuil-au-Houlme (Orne), Saint-Colomban (Loire-Atlantique), emprises de 7,57 ha, 10 ha, 24 ha et plus de 100 ha pour 250 000, 250 000, 150 000 et 700 000 t/an, soit 0,30, 0,40, 1,60 et 1,43 m²·an/t, médiane 0,9 (lu dans des extraits, à vérifier) |
| carriere | msa usage | 0,05 | MSA | 0,05 à 0,3 | transposée | C-G6 | PBL 2016, GLOBIO 3.5, Table 2.2 : Urban area 0,05 (aucune classe carrière, la classe la plus artificialisée est retenue) |
| autres_materiaux | occupation par tonne | 0 | m²·an par t | 0 | convention | C-G7 | OpenNAT, aucun inventaire ouvert d'occupation des sols par masse de produit industriel (acier, verre, plastiques, isolants minéraux, plâtre), audit § 3, trou le plus grave du module G |
| pollution | indicateurs rsee | 106 | code d'indicateur | 106 à 116 | primaire | C-G8 | Arrêté du 4 août 2021, annexe II, liste des indicateurs , codes 106 (AP), 107 (EP eaux douces), 108 (EP marine), 109 (EP terrestre), 116 (ETP-fw) du RSEE, dans l'ordre de la liste de l'annexe II |

### 2.9 Seuils proposés (`seuils.csv`)

Seuils de Bnat, de la pleine terre et de Cnat, en attente de validation du Biodiversity Standard Council.

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| logement_emprise_37 | bnat min | 45 | points | 45 | transposée | C-E6 | Référentiel Effinature 8.1, NORMATYS (version à venir), critère SOL 01.2.5 : habitations et installations d'intérêt collectif, emprise du bâti jusqu'à 37 %, CBSh minimum 0,45 |
| logement_emprise_38_49 | bnat min | 35 | points | 35 | transposée | C-E6 | Référentiel Effinature 8.1, NORMATYS (version à venir), critère SOL 01.2.5 : emprise de 38 à 49 %, CBSh minimum 0,35 |
| logement_emprise_50 | bnat min | 25 | points | 25 | transposée | C-E6 | Référentiel Effinature 8.1, NORMATYS (version à venir), critère SOL 01.2.5 : emprise de 50 % et plus, CBSh minimum 0,25 |
| tertiaire | bnat min | 25 | points | 25 | transposée | C-E6 | Référentiel Effinature 8.1, NORMATYS (version à venir), critère SOL 01.2.5 : commerces, bureaux, administrations, hébergements avec services, CBSh minimum 0,25 |
| * | pleine terre min | 0,15 | fraction de l'emprise totale du projet | 0,15 | transposée | C-E6 | Référentiel Effinature 8.1, NORMATYS (version à venir), critère SOL 01.2.5 : au moins 15 % d'espaces végétalisés en pleine terre sur l'emprise totale du projet |
| niveau_1 | cnat max relatif | 0 | fraction de la valeur initiale intégrée | 0 | convention | C-E7 | OpenNAT, absence de perte nette sur le site |
| niveau_2 | cnat max relatif | -0,1 | fraction de la valeur initiale intégrée | -0,1 | transposée | C-E7 | Environment Act 2021, Schedule 14, Schedule 7A inséré dans le Town and Country Planning Act 1990, paragraphe 2(3) : The relevant percentage is 10% (lu le 18/10/2026) |

### 2.10 Grilles d'état (`etat_criteres.csv`)

Critères et règles des onze grilles d'état (module H).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| EP1 | critere A essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A Grassland low distinctiveness, critère A |
| EP1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère B |
| EP1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère C |
| EP1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère D |
| EP1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère E |
| EP1 | critere F | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère F |
| EP1 | critere G | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 5A, critère G |
| EP2 | critere A essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A Grassland medium, high and very high, critère A |
| EP2 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A, critère B |
| EP2 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A, critère C |
| EP2 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A, critère D |
| EP2 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A, critère E |
| EP2 | critere F essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 6A, critère F |
| EL1 | critere A essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A Heathland, critère A |
| EL1 | critere B essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère B |
| EL1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère C |
| EL1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère D |
| EL1 | critere E | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère E |
| EL1 | critere F | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère F |
| EL1 | critere G | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère G |
| EL1 | critere H | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère H |
| EL1 | critere I | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère I |
| EL1 | critere J | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère J |
| EL1 | critere K | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 7A, critère K |
| EH1 | critere A1 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A Hedgerow, attribut A1 |
| EH1 | critere A2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut A2 |
| EH1 | critere B1 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut B1 |
| EH1 | critere B2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut B2 |
| EH1 | critere C1 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut C1 |
| EH1 | critere C2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut C2 |
| EH1 | critere D1 | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut D1 |
| EH1 | critere D2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut D2 |
| EH1 | critere E1 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut E1 (haies avec arbres seulement) |
| EH1 | critere E2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 8A, attribut E2 (haies avec arbres seulement) |
| EA1 | critere A | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A Individual trees, critère A |
| EA1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A, critère B |
| EA1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A, critère C |
| EA1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A, critère D |
| EA1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A, critère E |
| EA1 | critere F | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 9A, critère F |
| EM1 | critere A | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A Pond, critère A |
| EM1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère B |
| EM1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère C |
| EM1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère D |
| EM1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère E |
| EM1 | critere F | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère F |
| EM1 | critere G | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère G |
| EM1 | critere H | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère H |
| EM1 | critere I | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 18A, critère I |
| EF1 | critere A | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 20A Scrub, critère A |
| EF1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 20A, critère B |
| EF1 | critere C | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 20A, critère C |
| EF1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 20A, critère D |
| EF1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 20A, critère E |
| ER1 | critere A | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 21A Sparsely vegetated land, critère A |
| ER1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 21A, critère B |
| ER1 | critere C | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 21A, critère C |
| ER1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 21A, critère D |
| EU1 | critere A | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A Urban, critère A |
| EU1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère B |
| EU1 | critere C essentiel | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère C |
| EU1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère D (friches urbaines VB.8 seulement) |
| EU1 | critere E1 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère E1 (noues et ouvrages VB.19 et VB.24 seulement) |
| EU1 | critere E2 | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère E2 (noues et ouvrages VB.19 et VB.24 seulement) |
| EU1 | critere F | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère F (toitures intensives VB.13 seulement) |
| EU1 | critere G | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 22A, critère G (toitures biodiverses VB.12 seulement) |
| EZ1 | critere A essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A Wetland, critère A |
| EZ1 | critere B | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère B |
| EZ1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère C |
| EZ1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère D |
| EZ1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère E |
| EZ1 | critere F | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère F |
| EZ1 | critere G | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 23A, critère G |
| EV1 | critere A essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère A |
| EV1 | critere B essentiel | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère B |
| EV1 | critere C | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère C |
| EV1 | critere D | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère D |
| EV1 | critere E | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère E |
| EV1 | critere F | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère F |
| EV1 | critere G | 1 | poids | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère G |
| EV1 | critere H | 1 | poids | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 17A Orchard, critère H |
| EB1 | indicateur age peuplement | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A Woodland, indicateur A |
| EB1 | indicateur degats herbivores | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur B |
| EB1 | indicateur especes envahissantes | 1 | score 1 à 3 | 1 | transposée | C-H8 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur C |
| EB1 | indicateur nombre essences indigenes | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur D |
| EB1 | indicateur couvert indigene | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur E |
| EB1 | indicateur espaces ouverts | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur F |
| EB1 | indicateur regeneration | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur G |
| EB1 | indicateur sante arbres | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur H |
| EB1 | indicateur flore sol | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur I |
| EB1 | indicateur structure verticale | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur J |
| EB1 | indicateur arbres veterans | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur K |
| EB1 | indicateur bois mort | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur L |
| EB1 | indicateur perturbations | 1 | score 1 à 3 | 1 | transposée | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, indicateur M |
| EB1 | seuil bon | 33 | score total | 33 | primaire |  | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, résultat : total supérieur à 32 (33 à 39) = bon |
| EB1 | seuil moyen | 26 | score total | 26 | primaire |  | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), fiche 24A, résultat : total de 26 à 32 = moyen |
| * | facteur etat minimum | 0,5 | sans unité | 0,5 | convention | C-H2 | Audit du lot 0, point P7, BKompV § 5, Statutory Biodiversity Metric, onglet G-8, audit § 5, P7, facteur d'état = 0,5 + 0,5 x S |
| * | plafond score si essentiel echoue | 0,5 | sans unité | 0,5 | convention | C-H6 | Statutory Biodiversity Metric, Condition Assessments (juillet 2025), règles de résultat des fiches 5A, 6A, 7A, 17A, 22A, 23A : l'échec d'un critère essentiel interdit l'état bon ou moyen |
| * | seuil classe bon | 0,85 | score S | 0,85 | convention | C-H2 | Audit du lot 0, point P7, audit § 5, P7 |
| * | seuil classe moyen | 0,65 | score S | 0,65 | convention | C-H2 | Audit du lot 0, point P7, audit § 5, P7 |

Le libellé de chaque critère est dans la colonne « justification » de la table ; il est repris en entier dans les fiches habitats (partie 4) et dans les protocoles de relevé (partie 6).

| Grille | Critère | Libellé |
|---|---|---|
| EP1 | A (essentiel) | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) |
| EP1 | B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus |
| EP1 | C | Fourrés sur moins de 20 % de la surface de la prairie |
| EP1 | D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface |
| EP1 | E | Sol nu entre 1 % et 10 % de la surface |
| EP1 | F | Fougère aigle sur moins de 20 % de la surface |
| EP1 | G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) |
| EP2 | A (essentiel) | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques |
| EP2 | B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus |
| EP2 | C | Sol nu entre 1 % et 5 % de la surface |
| EP2 | D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface |
| EP2 | E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface |
| EP2 | F (essentiel) | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type |
| EL1 | A (essentiel) | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes |
| EL1 | B (essentiel) | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine |
| EL1 | C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine |
| EL1 | D | Sol nu non ombragé entre 1 % et 10 % |
| EL1 | E | Absence d'espèces végétales exotiques envahissantes |
| EL1 | F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris |
| EL1 | G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne |
| EL1 | H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne |
| EL1 | I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % |
| EL1 | J | Fougère aigle sur moins de 5 % |
| EL1 | K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation |
| EH1 | A1 | Hauteur moyenne de la haie supérieure à 1,5 m |
| EH1 | A2 | Largeur moyenne de la haie supérieure à 1,5 m |
| EH1 | B1 | Espace entre le sol et la base du feuillage inférieur à 0,5 m sur plus de 90 % de la longueur |
| EH1 | B2 | Trouées sur moins de 10 % de la longueur et aucune trouée de plus de 5 m |
| EH1 | C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace sur au moins un côté et plus de 90 % de la longueur |
| EH1 | C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de la bande non perturbée |
| EH1 | D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes |
| EH1 | D2 | Plus de 90 % de la haie et de sa bande exempts de dégradations d'origine humaine |
| EH1 | E1 | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m |
| EH1 | E2 | Au moins 95 % des arbres de la haie en bonne santé |
| EA1 | A | Essence indigène (ou au moins 70 % d'essences indigènes dans un groupe) |
| EA1 | B | Couvert continu, trouées sur moins de 10 % et aucune de plus de 5 m (critère réputé satisfait pour un arbre isolé) |
| EA1 | C | Arbre mûr (ou plus de 50 % d'arbres mûrs dans un groupe) |
| EA1 | D | Pas d'atteinte humaine à la santé de l'arbre et pas de taille régulière : plus de 75 % du houppier naturel conservé |
| EA1 | E | Microhabitats présents : bois mort, cavités, lierre, écorce décollée |
| EA1 | F | Plus de 20 % du houppier au-dessus d'une végétation (et non d'un sol revêtu) |
| EM1 | A | Eau claire, sans signe évident de pollution |
| EM1 | B | Habitat semi-naturel sur au moins 10 m tout autour de la mare |
| EM1 | C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface |
| EM1 | D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) |
| EM1 | E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation |
| EM1 | F | Absence d'espèces végétales et animales exotiques envahissantes |
| EM1 | G | Pas d'empoissonnement artificiel |
| EM1 | H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur |
| EM1 | I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins |
| EF1 | A | Fourré représentatif de son type, au moins 80 % d'essences indigènes |
| EF1 | B | Semis, jeunes plants, arbustes jeunes et mûrs tous présents |
| EF1 | C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol |
| EF1 | D | Lisière étagée avec fourrés épars et ourlet herbacé haut vers l'habitat voisin |
| EF1 | E | Clairières ou layons ménageant des lisières abritées |
| ER1 | A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes |
| ER1 | B | Fougère aigle, fourrés et arbres sur moins de 25 % |
| ER1 | C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée |
| ER1 | D | Recouvrement végétal entre 5 % et 50 % |
| EU1 | A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface |
| EU1 | B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année |
| EU1 | C (essentiel) | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) |
| EU1 | D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) |
| EU1 | E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat |
| EU1 | E2 | Végétation composée d'espèces de milieux humides ou riverains |
| EU1 | F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise |
| EU1 | G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état |
| EZ1 | A (essentiel) | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel |
| EZ1 | B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes |
| EZ1 | C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution |
| EZ1 | D | Fourrés et arbres épars sur moins de 10 % |
| EZ1 | E | Sol nu sur moins de 5 % |
| EZ1 | F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol |
| EZ1 | G | Litière continue empêchant la régénération sur 25 % au plus de la surface |
| EV1 | A (essentiel) | Présence d'arbres anciens ou vétérans |
| EV1 | B (essentiel) | Bois mort dans ou sur les arbres, ou au sol, pour au moins 20 % des arbres mûrs |
| EV1 | C | Moins de 5 % des arbres fruitiers étouffés par les fourrés, fourrés sur moins de 10 % du sol |
| EV1 | D | Taille de formation ou de restauration qui prolonge la vie des arbres |
| EV1 | E | Au moins 95 % des arbres exempts de dégâts d'origine humaine ou animale (abroutissement, écorçage, liens non ajustés) |
| EV1 | F | Prairie non surpâturée, piétinement sous le houppier de 10 % des arbres au plus |
| EV1 | G | Prairie d'une richesse en espèces équivalente à une prairie de valeur moyenne ou plus |
| EV1 | H | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 10 % du sol |
| EB1 | indicateur age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche |
| EB1 | indicateur degats herbivores | Dégâts d'herbivores sauvages ou domestiques |
| EB1 | indicateur especes envahissantes | Espèces végétales envahissantes |
| EB1 | indicateur nombre essences indigenes | Nombre d'essences d'arbres indigènes |
| EB1 | indicateur couvert indigene | Couvert des arbres et arbustes indigènes |
| EB1 | indicateur espaces ouverts | Espaces ouverts dans le boisement |
| EB1 | indicateur regeneration | Régénération du boisement |
| EB1 | indicateur sante arbres | Santé des arbres |
| EB1 | indicateur flore sol | Végétation et flore du sol |
| EB1 | indicateur structure verticale | Structure verticale |
| EB1 | indicateur arbres veterans | Arbres vétérans |
| EB1 | indicateur bois mort | Quantité de bois mort |
| EB1 | indicateur perturbations | Perturbations du boisement |
| EB1 | seuil bon | Score total minimal du bon état |
| EB1 | seuil moyen | Score total minimal de l'état moyen |

### 2.11 Stations climatiques de référence (`climat.csv`)

Stations de référence des huit zones climatiques, normales mensuelles de pluie 1991-2020 sur lesquelles les années types sont recalées, ETP Penman de contrôle (module W, fiches A43 à A45).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| H1a | station latitude | 48,7743 | degré | 48,7743 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TRAPPES |
| H1a | station longitude | 2,0098 | degré | 2,0098 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TRAPPES |
| H1a | station altitude | 167 | m | 167 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TRAPPES |
| H1a | pluie normale m01 | 56,2 | mm/mois | 28,1 à 84,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m02 | 48,9 | mm/mois | 24,4 à 73,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m03 | 50,1 | mm/mois | 25,1 à 75,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m04 | 49,9 | mm/mois | 25 à 74,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m05 | 66 | mm/mois | 33 à 99 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m06 | 57 | mm/mois | 28,5 à 85,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m07 | 56,2 | mm/mois | 28,1 à 84,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m08 | 56,1 | mm/mois | 28 à 84,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m09 | 49,8 | mm/mois | 24,9 à 74,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m10 | 61,8 | mm/mois | 30,9 à 92,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m11 | 61,2 | mm/mois | 30,6 à 91,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | pluie normale m12 | 72 | mm/mois | 36 à 108 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1a | etp penman normale | 772 | mm/an | 695 à 849 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_78, poste 78621001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H1b | station latitude | 48,6878 | degré | 48,6878 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station NANCY |
| H1b | station longitude | 6,2215 | degré | 6,2215 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station NANCY |
| H1b | station altitude | 212 | m | 212 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station NANCY |
| H1b | pluie normale m01 | 64,4 | mm/mois | 32,2 à 96,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m02 | 54,8 | mm/mois | 27,4 à 82,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m03 | 54,1 | mm/mois | 27,1 à 81,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m04 | 44,3 | mm/mois | 22,2 à 66,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m05 | 67,9 | mm/mois | 33,9 à 101,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m06 | 56 | mm/mois | 28 à 83,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m07 | 63 | mm/mois | 31,5 à 94,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m08 | 67,2 | mm/mois | 33,6 à 100,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m09 | 61,1 | mm/mois | 30,6 à 91,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m10 | 66,5 | mm/mois | 33,3 à 99,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m11 | 68,9 | mm/mois | 34,5 à 103,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | pluie normale m12 | 78,1 | mm/mois | 39 à 117,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1b | etp penman normale | 819 | mm/an | 737 à 901 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_54, poste 54526001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H1c | station latitude | 46,2945 | degré | 46,2945 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MACON |
| H1c | station longitude | 4,7943 | degré | 4,7943 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MACON |
| H1c | station altitude | 219 | m | 219 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MACON |
| H1c | pluie normale m01 | 58,1 | mm/mois | 29,1 à 87,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m02 | 48,9 | mm/mois | 24,4 à 73,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m03 | 49,1 | mm/mois | 24,6 à 73,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m04 | 65,5 | mm/mois | 32,8 à 98,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m05 | 75,7 | mm/mois | 37,9 à 113,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m06 | 69,8 | mm/mois | 34,9 à 104,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m07 | 72,2 | mm/mois | 36,1 à 108,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m08 | 72,6 | mm/mois | 36,3 à 108,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m09 | 71,1 | mm/mois | 35,5 à 106,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m10 | 91,1 | mm/mois | 45,5 à 136,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m11 | 92,8 | mm/mois | 46,4 à 139,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | pluie normale m12 | 66,8 | mm/mois | 33,4 à 100,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ RR, moyenne 1991-2020 (30 années valides) |
| H1c | etp penman normale | 895 | mm/an | 805 à 984 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_71, poste 71105001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H2a | station latitude | 48,0688 | degré | 48,0688 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station RENNES |
| H2a | station longitude | -1,764 | degré | -1,764 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station RENNES |
| H2a | station altitude | 36 | m | 36 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station RENNES |
| H2a | pluie normale m01 | 66,6 | mm/mois | 33,3 à 100 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m02 | 51,6 | mm/mois | 25,8 à 77,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m03 | 48,9 | mm/mois | 24,4 à 73,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m04 | 51,2 | mm/mois | 25,6 à 76,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m05 | 58,1 | mm/mois | 29 à 87,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m06 | 50,9 | mm/mois | 25,4 à 76,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m07 | 44 | mm/mois | 22 à 66 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m08 | 43,5 | mm/mois | 21,7 à 65,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m09 | 56,6 | mm/mois | 28,3 à 85 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m10 | 73,1 | mm/mois | 36,5 à 109,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m11 | 73,2 | mm/mois | 36,6 à 109,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | pluie normale m12 | 73,3 | mm/mois | 36,6 à 109,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2a | etp penman normale | 839 | mm/an | 755 à 922 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_35, poste 35281001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H2b | station latitude | 47,4445 | degré | 47,4445 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TOURS |
| H2b | station longitude | 0,7273 | degré | 0,7273 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TOURS |
| H2b | station altitude | 108 | m | 108 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station TOURS |
| H2b | pluie normale m01 | 63 | mm/mois | 31,5 à 94,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m02 | 52,4 | mm/mois | 26,2 à 78,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m03 | 48,7 | mm/mois | 24,3 à 73 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m04 | 53 | mm/mois | 26,5 à 79,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m05 | 57,7 | mm/mois | 28,8 à 86,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m06 | 53,2 | mm/mois | 26,6 à 79,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m07 | 46,6 | mm/mois | 23,3 à 69,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m08 | 44 | mm/mois | 22 à 66 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m09 | 51,8 | mm/mois | 25,9 à 77,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m10 | 66 | mm/mois | 33 à 98,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m11 | 69,3 | mm/mois | 34,7 à 104 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | pluie normale m12 | 72,1 | mm/mois | 36 à 108,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2b | etp penman normale | 901 | mm/an | 811 à 991 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_37, poste 37179001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H2c | station latitude | 44,1721 | degré | 44,1721 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station AGEN |
| H2c | station longitude | 0,5946 | degré | 0,5946 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station AGEN |
| H2c | station altitude | 58 | m | 58 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station AGEN |
| H2c | pluie normale m01 | 59,6 | mm/mois | 29,8 à 89,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m02 | 44,2 | mm/mois | 22,1 à 66,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m03 | 49 | mm/mois | 24,5 à 73,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m04 | 70 | mm/mois | 35 à 104,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m05 | 73,3 | mm/mois | 36,6 à 109,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m06 | 62,2 | mm/mois | 31,1 à 93,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m07 | 49,4 | mm/mois | 24,7 à 74,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m08 | 50,4 | mm/mois | 25,2 à 75,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m09 | 60,6 | mm/mois | 30,3 à 90,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m10 | 58,7 | mm/mois | 29,4 à 88,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m11 | 70,1 | mm/mois | 35 à 105,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | pluie normale m12 | 60,7 | mm/mois | 30,4 à 91,1 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2c | etp penman normale | 940 | mm/an | 846 à 1 034 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_47, poste 47091001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H2d | station latitude | 44,0836 | degré | 44,0836 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station CARPENTRAS |
| H2d | station longitude | 5,216 | degré | 5,216 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station CARPENTRAS |
| H2d | station altitude | 98 | m | 98 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station CARPENTRAS |
| H2d | pluie normale m01 | 46,3 | mm/mois | 23,2 à 69,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m02 | 34,2 | mm/mois | 17,1 à 51,3 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m03 | 43,2 | mm/mois | 21,6 à 64,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m04 | 61,1 | mm/mois | 30,5 à 91,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m05 | 55,6 | mm/mois | 27,8 à 83,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m06 | 41,7 | mm/mois | 20,9 à 62,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m07 | 25,7 | mm/mois | 12,9 à 38,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m08 | 40,6 | mm/mois | 20,3 à 60,9 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m09 | 98,7 | mm/mois | 49,3 à 148 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m10 | 87,6 | mm/mois | 43,8 à 131,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m11 | 90,8 | mm/mois | 45,4 à 136,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | pluie normale m12 | 41,9 | mm/mois | 20,9 à 62,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ RR, moyenne 1991-2020 (30 années valides) |
| H2d | etp penman normale | 1 140 | mm/an | 1 026 à 1 254 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_84, poste 84031001, champ ETP, somme des moyennes mensuelles 1991-2020 |
| H3 | station latitude | 43,4376 | degré | 43,4376 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MARIGNANE |
| H3 | station longitude | 5,216 | degré | 5,216 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MARIGNANE |
| H3 | station altitude | 9 | m | 9 | primaire | C-W1 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence, station MARIGNANE |
| H3 | pluie normale m01 | 47,1 | mm/mois | 23,6 à 70,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m02 | 29,8 | mm/mois | 14,9 à 44,6 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m03 | 29,5 | mm/mois | 14,7 à 44,2 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m04 | 51,6 | mm/mois | 25,8 à 77,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m05 | 37,7 | mm/mois | 18,8 à 56,5 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m06 | 27,9 | mm/mois | 13,9 à 41,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m07 | 11,1 | mm/mois | 5,6 à 16,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (29 années valides) |
| H3 | pluie normale m08 | 25,8 | mm/mois | 12,9 à 38,7 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m09 | 82 | mm/mois | 41 à 123 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m10 | 73,3 | mm/mois | 36,7 à 110 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m11 | 75,9 | mm/mois | 37,9 à 113,8 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | pluie normale m12 | 40,9 | mm/mois | 20,5 à 61,4 | primaire | C-W3 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ RR, moyenne 1991-2020 (30 années valides) |
| H3 | etp penman normale | 1 377 | mm/an | 1 239 à 1 515 | primaire | C-W2 | Météo-France, données climatologiques de base mensuelles, fichier MENSQ_13, poste 13054001, champ ETP, somme des moyennes mensuelles 1991-2020 |

### 2.12 Bilan hydrique (`hydrique.csv`)

Textures et réserves utiles, substrats, groupes hydriques, saison de végétation, stress hydrique, arrosage, mares (module W, fiches A47 à A50).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| sable | theta capacite champ | 0,12 | m³/m³ | 0,07 à 0,17 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Sand », milieu de la plage |
| sable | theta point fletrissement | 0,045 | m³/m³ | 0,02 à 0,07 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Sand », milieu de la plage |
| sable_limoneux | theta capacite champ | 0,15 | m³/m³ | 0,11 à 0,19 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Loamy sand », milieu de la plage |
| sable_limoneux | theta point fletrissement | 0,065 | m³/m³ | 0,03 à 0,1 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Loamy sand », milieu de la plage |
| limon_sableux | theta capacite champ | 0,23 | m³/m³ | 0,18 à 0,28 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Sandy loam », milieu de la plage |
| limon_sableux | theta point fletrissement | 0,11 | m³/m³ | 0,06 à 0,16 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Sandy loam », milieu de la plage |
| limon | theta capacite champ | 0,25 | m³/m³ | 0,2 à 0,3 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Loam », milieu de la plage |
| limon | theta point fletrissement | 0,12 | m³/m³ | 0,07 à 0,17 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Loam », milieu de la plage |
| limon_silteux | theta capacite champ | 0,29 | m³/m³ | 0,22 à 0,36 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt loam », milieu de la plage |
| limon_silteux | theta point fletrissement | 0,15 | m³/m³ | 0,09 à 0,21 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt loam », milieu de la plage |
| silt | theta capacite champ | 0,32 | m³/m³ | 0,28 à 0,36 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt », milieu de la plage |
| silt | theta point fletrissement | 0,17 | m³/m³ | 0,12 à 0,22 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt », milieu de la plage |
| limon_argilo_silteux | theta capacite champ | 0,335 | m³/m³ | 0,3 à 0,37 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt clay loam », milieu de la plage |
| limon_argilo_silteux | theta point fletrissement | 0,205 | m³/m³ | 0,17 à 0,24 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silt clay loam », milieu de la plage |
| argile_silteuse | theta capacite champ | 0,36 | m³/m³ | 0,3 à 0,42 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silty clay », milieu de la plage |
| argile_silteuse | theta point fletrissement | 0,23 | m³/m³ | 0,17 à 0,29 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Silty clay », milieu de la plage |
| argile | theta capacite champ | 0,36 | m³/m³ | 0,32 à 0,4 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Clay », milieu de la plage |
| argile | theta point fletrissement | 0,22 | m³/m³ | 0,2 à 0,24 | primaire | C-W4 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 19, ligne « Clay », milieu de la plage |
| * | profondeur sol defaut | 1 | m | 0,5 à 1,5 | convention | C-W4 | OpenNAT, valeur de secours |
| substrat | reserve volumique | 0,2 | m³/m³ | 0,12 à 0,3 | convention | C-W5 | OpenNAT, valeur de secours pour les substrats de toiture et de dalle |
| gazon | kc saison | 0,95 | sans unité | 0,81 à 1,09 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Turf grass, cool season » (Kc ini 0,90, Kc mi 0,95) ; tableau 22 « Turf grass, cool season » (Zr 0,5 à 1,0 m, p 0,40) |
| gazon | kc hors saison | 0,9 | sans unité | 0,72 à 1,08 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Turf grass, cool season » (Kc ini 0,90, Kc mi 0,95) ; tableau 22 « Turf grass, cool season » (Zr 0,5 à 1,0 m, p 0,40) |
| gazon | profondeur racinaire | 0,75 | m | 0,5 à 1 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Turf grass, cool season » (Kc ini 0,90, Kc mi 0,95) ; tableau 22 « Turf grass, cool season » (Zr 0,5 à 1,0 m, p 0,40) |
| gazon | fraction p | 0,4 | fraction | 0,3 à 0,5 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Turf grass, cool season » (Kc ini 0,90, Kc mi 0,95) ; tableau 22 « Turf grass, cool season » (Zr 0,5 à 1,0 m, p 0,40) |
| prairie | kc saison | 0,75 | sans unité | 0,64 à 0,86 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Grazing pasture, extensive grazing » (Kc ini 0,30, Kc mi 0,75) ; tableau 22 « Grazing pasture, extensive » (Zr 0,5 à 1,5 m, p 0,60) |
| prairie | kc hors saison | 0,3 | sans unité | 0,24 à 0,36 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Grazing pasture, extensive grazing » (Kc ini 0,30, Kc mi 0,75) ; tableau 22 « Grazing pasture, extensive » (Zr 0,5 à 1,5 m, p 0,60) |
| prairie | profondeur racinaire | 1 | m | 0,67 à 1,33 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Grazing pasture, extensive grazing » (Kc ini 0,30, Kc mi 0,75) ; tableau 22 « Grazing pasture, extensive » (Zr 0,5 à 1,5 m, p 0,60) |
| prairie | fraction p | 0,6 | fraction | 0,5 à 0,7 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Grazing pasture, extensive grazing » (Kc ini 0,30, Kc mi 0,75) ; tableau 22 « Grazing pasture, extensive » (Zr 0,5 à 1,5 m, p 0,60) |
| xerophile | kc saison | 0,75 | sans unité | 0,64 à 0,86 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, mêmes valeurs que le groupe prairie (tableaux 12 et 22, « Grazing pasture, extensive ») |
| xerophile | kc hors saison | 0,3 | sans unité | 0,24 à 0,36 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, mêmes valeurs que le groupe prairie (tableaux 12 et 22, « Grazing pasture, extensive ») |
| xerophile | profondeur racinaire | 1 | m | 0,67 à 1,33 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, mêmes valeurs que le groupe prairie (tableaux 12 et 22, « Grazing pasture, extensive ») |
| xerophile | fraction p | 0,6 | fraction | 0,5 à 0,7 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, mêmes valeurs que le groupe prairie (tableaux 12 et 22, « Grazing pasture, extensive ») |
| arbustif | kc saison | 1,05 | sans unité | 0,89 à 1,21 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Berries (bushes) » (Kc ini 0,30, Kc mi 1,05) ; tableau 22 « Berries (bushes) » (Zr 0,6 à 1,2 m, p 0,50) |
| arbustif | kc hors saison | 0,3 | sans unité | 0,24 à 0,36 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Berries (bushes) » (Kc ini 0,30, Kc mi 1,05) ; tableau 22 « Berries (bushes) » (Zr 0,6 à 1,2 m, p 0,50) |
| arbustif | profondeur racinaire | 0,9 | m | 0,6 à 1,2 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Berries (bushes) » (Kc ini 0,30, Kc mi 1,05) ; tableau 22 « Berries (bushes) » (Zr 0,6 à 1,2 m, p 0,50) |
| arbustif | fraction p | 0,5 | fraction | 0,4 à 0,6 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Berries (bushes) » (Kc ini 0,30, Kc mi 1,05) ; tableau 22 « Berries (bushes) » (Zr 0,6 à 1,2 m, p 0,50) |
| arbore | kc saison | 1,2 | sans unité | 1,02 à 1,3 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Apples, Cherries, Pears, active ground cover, killing frost » (Kc ini 0,50, Kc mi 1,20) ; tableau 22 « Apples, cherries, pears » (Zr 1,0 à 2,0 m, p 0,50) |
| arbore | kc hors saison | 0,5 | sans unité | 0,4 à 0,6 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Apples, Cherries, Pears, active ground cover, killing frost » (Kc ini 0,50, Kc mi 1,20) ; tableau 22 « Apples, cherries, pears » (Zr 1,0 à 2,0 m, p 0,50) |
| arbore | profondeur racinaire | 1,5 | m | 1,01 à 2 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Apples, Cherries, Pears, active ground cover, killing frost » (Kc ini 0,50, Kc mi 1,20) ; tableau 22 « Apples, cherries, pears » (Zr 1,0 à 2,0 m, p 0,50) |
| arbore | fraction p | 0,5 | fraction | 0,4 à 0,6 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Apples, Cherries, Pears, active ground cover, killing frost » (Kc ini 0,50, Kc mi 1,20) ; tableau 22 « Apples, cherries, pears » (Zr 1,0 à 2,0 m, p 0,50) |
| conifere | kc saison | 1 | sans unité | 0,85 à 1,15 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Conifer Trees » (Kc 1,00) ; tableau 22 « Conifer trees » (Zr 1,0 à 1,5 m, p 0,70) |
| conifere | kc hors saison | 1 | sans unité | 0,8 à 1,2 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Conifer Trees » (Kc 1,00) ; tableau 22 « Conifer trees » (Zr 1,0 à 1,5 m, p 0,70) |
| conifere | profondeur racinaire | 1,25 | m | 0,84 à 1,66 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Conifer Trees » (Kc 1,00) ; tableau 22 « Conifer trees » (Zr 1,0 à 1,5 m, p 0,70) |
| conifere | fraction p | 0,7 | fraction | 0,6 à 0,8 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Conifer Trees » (Kc 1,00) ; tableau 22 « Conifer trees » (Zr 1,0 à 1,5 m, p 0,70) |
| humide_pluie | kc saison | 1,2 | sans unité | 1,02 à 1,3 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Reed Swamp, moist soil » (Kc ini 0,90, Kc mi 1,20) ; profondeur et fraction p fixées par convention |
| humide_pluie | kc hors saison | 0,9 | sans unité | 0,72 à 1,08 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Reed Swamp, moist soil » (Kc ini 0,90, Kc mi 1,20) ; profondeur et fraction p fixées par convention |
| humide_pluie | profondeur racinaire | 0,5 | m | 0,34 à 0,67 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Reed Swamp, moist soil » (Kc ini 0,90, Kc mi 1,20) ; profondeur et fraction p fixées par convention |
| humide_pluie | fraction p | 0,3 | fraction | 0,2 à 0,4 | transposée | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Reed Swamp, moist soil » (Kc ini 0,90, Kc mi 1,20) ; profondeur et fraction p fixées par convention |
| mare | kc saison | 1,05 | sans unité | 0,89 à 1,21 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Open Water, < 2 m depth » (Kc 1,05) |
| mare | kc hors saison | 1,05 | sans unité | 0,84 à 1,26 | primaire | C-W6 | Allen R. G., Pereira L. S., Raes D., Smith M. (1998), FAO-56, Crop evapotranspiration, tableau 12 « Open Water, < 2 m depth » (Kc 1,05) |
| toiture_extensive | kc saison | 0,5 | sans unité | 0,3 à 0,8 | convention | C-W6 | OpenNAT, valeur de secours |
| toiture_extensive | kc hors saison | 0,3 | sans unité | 0,2 à 0,5 | convention | C-W6 | OpenNAT, valeur de secours |
| toiture_extensive | profondeur racinaire | 0,15 | m | 0,1 à 0,15 | convention | C-W6 | OpenNAT, bornée par l'épaisseur du substrat |
| toiture_extensive | fraction p | 0,6 | fraction | 0,5 à 0,7 | convention | C-W6 | OpenNAT, valeur de secours |
| * | seuil rew stress | 0,4 | fraction | 0,3 à 0,5 | transposée | C-W8 | Granier A., Bréda N., Biron P., Villette S. (1999), A lumped water balance model to evaluate duration and intensity of drought constraints in forest stands, Ecological Modelling 116, seuil de réserve extractible relative sous lequel la transpiration est réduite (REW < 0,4) et indice de stress IS = somme de (0,4 - REW) / 0,4 |
| * | seuil saison temperature | 5 | °C | 5 | transposée | C-W7 | ETCCDI, indices climatiques extrêmes, indice GSL (durée de la saison de croissance) : température moyenne quotidienne supérieure à 5 °C |
| * | seuil saison jours | 6 | jours | 6 | transposée | C-W7 | ETCCDI, indices climatiques extrêmes, indice GSL : six jours consécutifs |
| * | tolerance stress | 5 | jours-équivalents | 0 à 15 | convention | C-W9 | OpenNAT, valeur de secours |
| gazon | sensibilite stress | 0,5 | par 100 jours-équivalents | 0,25 à 0,75 | convention | C-W9 | OpenNAT, valeur de secours |
| prairie | sensibilite stress | 0,4 | par 100 jours-équivalents | 0,2 à 0,6 | convention | C-W9 | OpenNAT, valeur de secours |
| xerophile | sensibilite stress | 0,3 | par 100 jours-équivalents | 0,15 à 0,45 | convention | C-W9 | OpenNAT, valeur de secours |
| arbustif | sensibilite stress | 0,6 | par 100 jours-équivalents | 0,3 à 0,9 | convention | C-W9 | OpenNAT, valeur de secours |
| arbore | sensibilite stress | 0,8 | par 100 jours-équivalents | 0,4 à 1,2 | convention | C-W9 | OpenNAT, valeur de secours |
| conifere | sensibilite stress | 0,8 | par 100 jours-équivalents | 0,4 à 1,2 | convention | C-W9 | OpenNAT, valeur de secours |
| toiture_extensive | sensibilite stress | 0,3 | par 100 jours-équivalents | 0,15 à 0,45 | convention | C-W9 | OpenNAT, valeur de secours |
| humide_pluie | sensibilite stress | 1 | par 100 jours-équivalents | 0,5 à 1,5 | convention | C-W9 | OpenNAT, valeur de secours |
| * | facteur hydrique minimum | 0,5 | sans unité | 0,3 à 0,7 | convention | C-W9 | OpenNAT, valeur de secours |
| * | seuil rew arrosage | 0,5 | fraction | 0,4 à 0,6 | convention | C-W10 | OpenNAT, valeur de secours |
| * | profondeur mare defaut | 0,8 | m | 0,5 à 1,2 | convention | C-W11 | OpenNAT, valeur de secours |
| fond_etanche | infiltration | 0 | mm/jour | 0 à 0,2 | convention | C-W11 | OpenNAT, valeur de secours |
| fond_argile | infiltration | 0,3 | mm/jour | 0,1 à 1 | convention | C-W11 | OpenNAT, valeur de secours |
| fond_naturel | infiltration | 1 | mm/jour | 0,5 à 5 | convention | C-W11 | OpenNAT, valeur de secours |
| * | coefficient ruissellement | 0,9 | fraction | 0,8 à 1 | convention | C-W11 | OpenNAT, valeur de secours |
| * | coefficient ruissellement permeable | 0,1 | fraction | 0,05 à 0,3 | convention | C-W11 | OpenNAT, valeur de secours |
| * | facteur assec precoce | 0,5 | sans unité | 0,3 à 0,8 | convention | C-W12 | OpenNAT, valeur de secours |

### 2.13 Éclairage horaire (`eclairage.csv`)

Saison d'activité des chiroptères, nuit, distances, facteur spectral (module N, fiches A51 à A53).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| * | distance effet plein | 10 | m | 0 à 25 | transposée | C-L3 | Azam C., Le Viol I., Bas Y., Zissis G., Vernet A., Julien J.-F., Kerbiriou C. (2018), Evidence for distance and illuminance thresholds in the effects of artificial lighting on bat activity, Landscape and Urban Planning 175, résumé : effet d'attraction limité à 10 m pour Pipistrellus et Nyctalus |
| * | distance effet nul | 50 | m | 25 à 100 | primaire | C-L3 | Azam C., Le Viol I., Bas Y., Zissis G., Vernet A., Julien J.-F., Kerbiriou C. (2018), Evidence for distance and illuminance thresholds in the effects of artificial lighting on bat activity, Landscape and Urban Planning 175, résumé : évitement jusqu'à 25 m (Myotis) et 50 m (Eptesicus serotinus) ; recommandation de 50 m entre luminaires et corridors |
| * | perte maximale | 0,25 | fraction | 0,15 à 0,4 | convention | C-L1 | OpenNAT, calage sur le facteur L2 de nuisances.csv (0,75) |
| * | saison chiropteres debut | 4 | mois | 3 à 4 | convention | C-L2 | OpenNAT, valeur de secours |
| * | saison chiropteres fin | 10 | mois | 10 à 11 | convention | C-L2 | OpenNAT, valeur de secours |
| * | hauteur soleil nuit | 0 | degré | -6 à 0 | convention | C-L2 | ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025), variable Hs (hauteur angulaire du soleil) de l'année type |
| ambre | temperature couleur | 1 800 | K | 1 800 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| ambre | facteur spectral | 0,5 | sans unité | 0,4 à 0,7 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |
| k2200 | temperature couleur | 2 200 | K | 2 200 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| k2200 | facteur spectral | 0,6 | sans unité | 0,5 à 0,8 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |
| k2400 | temperature couleur | 2 400 | K | 2 400 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| k2400 | facteur spectral | 0,7 | sans unité | 0,6 à 0,85 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |
| k2700 | temperature couleur | 2 700 | K | 2 700 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| k2700 | facteur spectral | 0,8 | sans unité | 0,7 à 0,9 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |
| k3000 | temperature couleur | 3 000 | K | 3 000 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| k3000 | facteur spectral | 0,9 | sans unité | 0,8 à 1 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |
| k4000 | temperature couleur | 4 000 | K | 4 000 | primaire | C-L4 | Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, articles 3 et 4 : plafonds de 3 000 K, 2 700 K et 2 400 K selon les sites |
| k4000 | facteur spectral | 1 | sans unité | 1 | convention | C-L4 | Longcore T. et al. (2018), Rapid assessment of lamp spectrum to quantify ecological effects of light at night, Journal of Experimental Zoology A 329, résumé : les sources riches en bleu (2 200 K et plus) ont plus d'effets que les LED ambre filtrées |

### 2.14 Maturation, gestion et succession (`succession.csv`)

Courbe de Chapman-Richards, couples exploité et abandonné de la BKompV, délais de succession (module T, fiches A54 à A56).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| * | produit k d | 3 | sans unité | 2 à 4 | convention | C-M1 | Richards F. J. (1959), A flexible growth function for empirical use, Journal of Experimental Botany 10, fonction de croissance de Chapman-Richards |
| herbacee | exposant forme | 1 | sans unité | 1 à 1,5 | convention | C-M1 | Pienaar L. V., Turnbull K. J. (1973), The Chapman-Richards generalization of Von Bertalanffy's growth model, Forest Science 19, exposant de forme de la fonction de Chapman-Richards |
| arbustive | exposant forme | 2 | sans unité | 1,5 à 2,5 | convention | C-M1 | Pienaar L. V., Turnbull K. J. (1973), The Chapman-Richards generalization of Von Bertalanffy's growth model, Forest Science 19, exposant de forme de la fonction de Chapman-Richards |
| arboree | exposant forme | 3 | sans unité | 2,5 à 4 | convention | C-M1 | Pienaar L. V., Turnbull K. J. (1973), The Chapman-Richards generalization of Von Bertalanffy's growth model, Forest Science 19, exposant de forme de la fonction de Chapman-Richards |
| 34.02a>34.02b | rapport abandon | 0,81 | sans unité | 0,81 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.02a (21) exploité, 34.02b (17) abandonné |
| 34.03.01a>34.03.03 | rapport abandon | 0,864 | sans unité | 0,864 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.03.01a (22) exploité, 34.03.03 (19) abandonné |
| 34.04.03.01a>34.04.03.03 | rapport abandon | 0,762 | sans unité | 0,762 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.04.03.01a (21) exploité, 34.04.03.03 (16) abandonné |
| 34.06.01a>34.06.01b | rapport abandon | 0,857 | sans unité | 0,857 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.06.01a (21) exploité, 34.06.01b (18) abandonné |
| 34.06.02a>34.06.02b | rapport abandon | 0,864 | sans unité | 0,864 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.06.02a (22) exploité, 34.06.02b (19) abandonné |
| 34.07a.01>34.07a.03 | rapport abandon | 0,8 | sans unité | 0,8 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.07a.01 (20) exploité, 34.07a.03 (16) abandonné |
| 34.07b.01>34.07b.03 | rapport abandon | 0,733 | sans unité | 0,733 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 34.07b.01 (15) exploité, 34.07b.03 (11) abandonné |
| 35.02.01a>35.02.01.03 | rapport abandon | 0,87 | sans unité | 0,87 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 35.02.01a (23) exploité, 35.02.01.03 (20) abandonné |
| 35.02.02a>35.02.02.03 | rapport abandon | 0,913 | sans unité | 0,913 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 35.02.02a (23) exploité, 35.02.02.03 (21) abandonné |
| 35.02.03a.01>35.02.03a.02 | rapport abandon | 0,8 | sans unité | 0,8 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 35.02.03a.01 (20) exploité, 35.02.03a.02 (16) abandonné |
| 35.02.05.01>35.02.05.01a | rapport abandon | 0,889 | sans unité | 0,889 | primaire | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), 35.02.05.01 (18) exploité, 35.02.05.01a (16) abandonné |
| * | rapport abandon moyen | 0,833 | sans unité | 0,733 à 0,913 | transposée | C-M2 | BKompV, annexe 2 (Bundeskompensationsverordnung, 2020), moyenne des onze couples ci-dessus |
| * | delai friche herbacee | 2 | an | 1 à 3 | convention | C-M2 | OpenNAT, valeur de secours |
| * | delai embroussaillement | 15 | an | 10 à 30 | convention | C-M2 | OpenNAT, valeur de secours |
| * | score friche embroussaillee | 0,75 | fraction | 0,65 à 0,85 | convention | C-M2 | OpenNAT, valeur de secours |

### 2.15 Calendrier du chantier (`chantier.csv`)

Sensibilité mensuelle des oiseaux nicheurs, des chiroptères et des amphibiens, saison de plantation, année de début par défaut (module T, fiches A57 et A58).

| Clé | Paramètre | Valeur | Unité | Plage | Type | Conv. | Source et référence précise |
|---|---|---|---|---|---|---|---|
| oiseaux | sensibilite m01 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m02 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m03 | 0,5 | fraction | 0,5 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m04 | 1 | fraction | 1 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m05 | 1 | fraction | 1 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m06 | 1 | fraction | 1 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m07 | 1 | fraction | 1 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m08 | 0,5 | fraction | 0,5 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m09 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m10 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m11 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| oiseaux | sensibilite m12 | 0 | fraction | 0 | transposée | C-K1 | Ministère de l'Agriculture, conditionnalité de la PAC 2023-2027, BCAE 8 (maintien des particularités topographiques), interdiction de tailler haies et arbres du 16 mars au 15 août (nidification) |
| chiropteres | sensibilite m01 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m02 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m03 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m04 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m05 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m06 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m07 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m08 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m09 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m10 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m11 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| chiropteres | sensibilite m12 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : hibernation de novembre à février, mise bas et élevage des jeunes de mai à août |
| amphibiens | sensibilite m01 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m02 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m03 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m04 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m05 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m06 | 1 | fraction | 1 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m07 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m08 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m09 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m10 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m11 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| amphibiens | sensibilite m12 | 0 | fraction | 0 | convention | C-K1 | OpenNAT, valeur de secours : reproduction et développement larvaire de février à juin |
| * | perte destruction sensible | 1 | an | 0,5 à 2 | convention | C-K1 | OpenNAT, valeur de secours |
| plantation | mois favorable m01 | 1 | booléen | 1 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m02 | 1 | booléen | 1 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m03 | 1 | booléen | 1 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m04 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m05 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m06 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m07 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m08 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m09 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m10 | 0 | booléen | 0 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m11 | 1 | booléen | 1 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| plantation | mois favorable m12 | 1 | booléen | 1 | convention | C-K2 | OpenNAT, valeur de secours : plantation à racines nues ou en motte hors gel, de novembre à mars |
| * | avance plantation | 2 | mois | 0 à 4 | convention | C-K2 | OpenNAT, valeur de secours |
| * | annee debut defaut | 2027 | année | 2027 à 2030 | convention | C-K3 | OpenNAT, valeur de secours |

### 2.16 Années types horaires : synthèse mensuelle

Le module W lit, pour chaque zone, trois années types horaires de 8 760 heures : France +2 °C (2030), +2,7 °C (2050) et +4 °C (2100), tirées des fichiers climatiques prospectifs de l'ADEME, de Météo-France, du CSTB et de la DHUP (juin 2025, Licence Ouverte 2.0) et réduites dans `donnees/climat/` aux variables utilisées. Le tableau de chaque station donne, mois par mois, la température moyenne, la pluie après recalage sur la normale 1991-2020 (fiche A45) et l'évapotranspiration de référence calculée par la fiche A44, à l'altitude de la station.

#### Zone H1a, station de Trappes (167 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 6,9 | 3,0 | 8,8 | 9,2 | 13,4 | 17,8 | 19,5 | 18,7 | 16,0 | 12,8 | 8,9 | 5,5 | 11,8 |
| P +2 | 56 | 49 | 50 | 50 | 66 | 57 | 56 | 56 | 50 | 62 | 61 | 72 | 685 |
| ET0 +2 | 15 | 21 | 46 | 56 | 91 | 102 | 110 | 97 | 66 | 36 | 15 | 13 | 666 |
| T +2,7 | 6,9 | 3,0 | 8,8 | 9,2 | 13,8 | 17,2 | 20,4 | 20,8 | 17,8 | 12,8 | 8,9 | 5,5 | 12,1 |
| P +2,7 | 56 | 49 | 50 | 50 | 66 | 57 | 56 | 56 | 50 | 62 | 61 | 72 | 685 |
| ET0 +2,7 | 15 | 21 | 46 | 56 | 96 | 103 | 126 | 100 | 66 | 36 | 15 | 13 | 693 |
| T +4 | 6,9 | 6,8 | 8,8 | 12,9 | 18,6 | 20,8 | 24,3 | 20,8 | 20,2 | 14,7 | 10,6 | 8,7 | 14,5 |
| P +4 | 56 | 49 | 50 | 50 | 66 | 57 | 56 | 56 | 50 | 62 | 61 | 72 | 685 |
| ET0 +4 | 15 | 23 | 46 | 71 | 106 | 133 | 137 | 100 | 78 | 38 | 14 | 15 | 776 |

#### Zone H1b, station de Nancy (212 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 3,2 | 4,4 | 7,9 | 12,7 | 14,6 | 17,3 | 20,4 | 20,9 | 15,7 | 13,4 | 6,8 | 5,7 | 12,0 |
| P +2 | 64 | 55 | 54 | 44 | 68 | 56 | 63 | 67 | 61 | 66 | 69 | 78 | 746 |
| ET0 +2 | 16 | 20 | 44 | 74 | 102 | 114 | 124 | 101 | 68 | 37 | 18 | 13 | 730 |
| T +2,7 | 3,2 | 4,4 | 7,9 | 12,7 | 14,6 | 20,9 | 22,7 | 20,9 | 15,7 | 13,4 | 8,5 | 4,4 | 12,5 |
| P +2,7 | 64 | 55 | 54 | 44 | 68 | 56 | 63 | 67 | 61 | 66 | 69 | 78 | 746 |
| ET0 +2,7 | 16 | 20 | 44 | 74 | 102 | 123 | 133 | 101 | 68 | 37 | 16 | 14 | 748 |
| T +4 | 6,6 | 6,2 | 7,9 | 12,7 | 17,1 | 21,0 | 22,7 | 24,4 | 19,5 | 13,4 | 8,1 | 4,4 | 13,7 |
| P +4 | 64 | 55 | 54 | 44 | 68 | 56 | 63 | 67 | 61 | 66 | 69 | 78 | 746 |
| ET0 +4 | 17 | 28 | 44 | 74 | 104 | 123 | 133 | 119 | 82 | 37 | 18 | 14 | 793 |

#### Zone H1c, station de Mâcon (219 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 7,0 | 7,1 | 9,6 | 13,5 | 15,6 | 23,1 | 23,2 | 22,2 | 18,7 | 13,7 | 8,6 | 4,8 | 14,0 |
| P +2 | 58 | 49 | 49 | 66 | 76 | 70 | 72 | 73 | 71 | 91 | 93 | 67 | 834 |
| ET0 +2 | 19 | 30 | 56 | 82 | 112 | 150 | 151 | 125 | 89 | 42 | 19 | 13 | 887 |
| T +2,7 | 7,0 | 7,1 | 9,6 | 13,5 | 15,6 | 22,3 | 25,4 | 21,6 | 18,7 | 14,1 | 8,7 | 5,4 | 14,1 |
| P +2,7 | 58 | 49 | 49 | 66 | 76 | 70 | 72 | 73 | 71 | 91 | 93 | 67 | 834 |
| ET0 +2,7 | 19 | 30 | 56 | 82 | 112 | 154 | 158 | 110 | 89 | 43 | 20 | 10 | 882 |
| T +4 | 7,0 | 7,1 | 9,6 | 13,6 | 18,3 | 22,8 | 25,5 | 23,6 | 20,1 | 14,1 | 10,5 | 5,2 | 14,8 |
| P +4 | 58 | 49 | 49 | 66 | 76 | 70 | 72 | 73 | 71 | 91 | 93 | 67 | 834 |
| ET0 +4 | 19 | 30 | 56 | 81 | 121 | 152 | 158 | 129 | 82 | 43 | 20 | 14 | 905 |

#### Zone H2a, station de Rennes (36 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 7,3 | 8,8 | 9,7 | 13,4 | 14,4 | 17,7 | 18,7 | 20,9 | 18,3 | 15,5 | 11,3 | 7,5 | 13,6 |
| P +2 | 67 | 52 | 49 | 51 | 58 | 51 | 44 | 44 | 57 | 73 | 73 | 73 | 691 |
| ET0 +2 | 19 | 31 | 54 | 74 | 94 | 115 | 107 | 97 | 82 | 43 | 20 | 15 | 750 |
| T +2,7 | 8,6 | 8,8 | 9,7 | 13,4 | 15,4 | 17,7 | 23,3 | 21,9 | 18,8 | 15,5 | 11,3 | 7,5 | 14,4 |
| P +2,7 | 67 | 52 | 49 | 51 | 58 | 51 | 44 | 44 | 57 | 73 | 73 | 73 | 691 |
| ET0 +2,7 | 20 | 31 | 54 | 74 | 94 | 115 | 137 | 112 | 70 | 43 | 20 | 15 | 784 |
| T +4 | 7,3 | 8,8 | 9,7 | 13,2 | 15,4 | 20,2 | 24,3 | 22,0 | 20,4 | 15,7 | 11,3 | 7,5 | 14,7 |
| P +4 | 67 | 52 | 49 | 51 | 58 | 51 | 44 | 44 | 57 | 73 | 73 | 73 | 691 |
| ET0 +4 | 19 | 31 | 54 | 73 | 110 | 125 | 144 | 112 | 98 | 45 | 20 | 15 | 845 |

#### Zone H2b, station de Tours (108 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 6,6 | 5,7 | 9,3 | 12,8 | 15,8 | 21,3 | 22,8 | 21,0 | 17,8 | 14,5 | 9,6 | 6,5 | 13,7 |
| P +2 | 63 | 52 | 49 | 53 | 58 | 53 | 47 | 44 | 52 | 66 | 69 | 72 | 678 |
| ET0 +2 | 21 | 25 | 55 | 73 | 99 | 131 | 152 | 119 | 88 | 44 | 20 | 15 | 842 |
| T +2,7 | 6,5 | 9,2 | 9,3 | 12,8 | 15,8 | 21,3 | 22,8 | 22,7 | 17,8 | 14,5 | 9,6 | 6,5 | 14,1 |
| P +2,7 | 63 | 52 | 49 | 53 | 58 | 53 | 47 | 44 | 52 | 66 | 69 | 72 | 678 |
| ET0 +2,7 | 17 | 33 | 55 | 73 | 99 | 131 | 152 | 132 | 88 | 44 | 20 | 15 | 860 |
| T +4 | 6,5 | 9,4 | 9,3 | 12,8 | 18,9 | 21,3 | 24,3 | 23,2 | 20,1 | 14,5 | 11,6 | 7,5 | 15,0 |
| P +4 | 63 | 52 | 49 | 53 | 58 | 53 | 47 | 44 | 52 | 66 | 69 | 72 | 678 |
| ET0 +4 | 21 | 31 | 55 | 73 | 127 | 131 | 155 | 141 | 103 | 44 | 23 | 17 | 921 |

#### Zone H2c, station de Agen (58 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 7,2 | 8,3 | 10,9 | 14,0 | 16,7 | 20,6 | 22,4 | 23,2 | 20,9 | 15,7 | 9,3 | 7,7 | 14,8 |
| P +2 | 60 | 44 | 49 | 70 | 73 | 62 | 49 | 50 | 61 | 59 | 70 | 61 | 708 |
| ET0 +2 | 21 | 37 | 61 | 77 | 118 | 140 | 143 | 126 | 92 | 47 | 23 | 16 | 900 |
| T +2,7 | 7,2 | 8,3 | 10,9 | 14,0 | 16,7 | 20,6 | 22,4 | 23,2 | 20,9 | 15,8 | 11,9 | 7,7 | 15,0 |
| P +2,7 | 60 | 44 | 49 | 70 | 73 | 62 | 49 | 50 | 61 | 59 | 70 | 61 | 708 |
| ET0 +2,7 | 21 | 37 | 61 | 77 | 118 | 140 | 143 | 126 | 92 | 49 | 22 | 16 | 902 |
| T +4 | 8,8 | 8,3 | 10,7 | 14,0 | 21,0 | 23,3 | 26,5 | 23,2 | 21,8 | 16,4 | 11,9 | 7,7 | 16,2 |
| P +4 | 60 | 44 | 49 | 70 | 73 | 62 | 49 | 50 | 61 | 59 | 70 | 61 | 708 |
| ET0 +4 | 19 | 38 | 68 | 77 | 121 | 152 | 160 | 126 | 95 | 54 | 22 | 16 | 948 |

#### Zone H2d, station de Carpentras (98 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 7,1 | 7,6 | 11,1 | 15,5 | 19,3 | 23,9 | 24,5 | 25,4 | 22,3 | 16,0 | 10,7 | 6,1 | 15,8 |
| P +2 | 46 | 34 | 43 | 61 | 56 | 42 | 26 | 41 | 99 | 88 | 91 | 42 | 667 |
| ET0 +2 | 31 | 44 | 72 | 101 | 143 | 178 | 181 | 159 | 111 | 59 | 32 | 27 | 1136 |
| T +2,7 | 7,1 | 8,7 | 11,1 | 15,5 | 19,3 | 23,9 | 27,4 | 25,9 | 22,3 | 16,0 | 10,7 | 6,1 | 16,2 |
| P +2,7 | 46 | 34 | 43 | 61 | 56 | 42 | 26 | 41 | 99 | 88 | 91 | 42 | 667 |
| ET0 +2,7 | 31 | 43 | 72 | 101 | 143 | 178 | 207 | 171 | 111 | 59 | 32 | 27 | 1173 |
| T +4 | 7,1 | 8,7 | 11,1 | 15,5 | 19,3 | 24,5 | 27,4 | 25,9 | 22,9 | 17,4 | 10,8 | 6,1 | 16,4 |
| P +4 | 46 | 34 | 43 | 61 | 56 | 42 | 26 | 41 | 99 | 88 | 91 | 42 | 667 |
| ET0 +4 | 31 | 43 | 72 | 101 | 143 | 178 | 207 | 171 | 119 | 67 | 32 | 27 | 1191 |

#### Zone H3, station de Marignane (9 m)

| Var. | J | F | M | A | M | J | J | A | S | O | N | D | An |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T +2 | 8,9 | 10,6 | 11,7 | 16,0 | 21,1 | 22,8 | 27,8 | 26,1 | 21,2 | 17,8 | 13,3 | 8,4 | 17,2 |
| P +2 | 47 | 30 | 29 | 52 | 38 | 28 | 11 | 26 | 82 | 73 | 76 | 41 | 533 |
| ET0 +2 | 38 | 52 | 81 | 110 | 159 | 182 | 229 | 179 | 106 | 74 | 41 | 34 | 1286 |
| T +2,7 | 9,0 | 10,6 | 11,7 | 16,0 | 21,1 | 24,4 | 27,8 | 26,1 | 21,2 | 18,5 | 13,4 | 9,0 | 17,4 |
| P +2,7 | 47 | 30 | 29 | 52 | 38 | 28 | 11 | 26 | 82 | 73 | 76 | 41 | 533 |
| ET0 +2,7 | 38 | 52 | 81 | 110 | 159 | 194 | 229 | 179 | 106 | 73 | 41 | 30 | 1293 |
| T +4 | 9,0 | 10,6 | 12,7 | 16,9 | 21,5 | 25,6 | 29,4 | 26,1 | 23,9 | 18,5 | 13,4 | 10,4 | 18,2 |
| P +4 | 47 | 30 | 30 | 52 | 38 | 28 | 11 | 26 | 82 | 73 | 76 | 41 | 533 |
| ET0 +4 | 38 | 52 | 88 | 119 | 160 | 203 | 247 | 179 | 138 | 73 | 41 | 33 | 1371 |

Var. : variable. T : température moyenne (°C) ; P : pluie recalée (mm) ; ET0 : évapotranspiration de référence (mm). +2, +2,7, +4 : niveau de réchauffement de l'année type (°C). Mois de janvier (J) à décembre (D).

### 2.17 Extraits des sources primaires utilisés

Les deux tableaux suivants reproduisent les lignes des sources primaires effectivement appelées par la nomenclature : la liste allemande des valeurs de biotopes (texte réglementaire libre de droits) et les lignes de la métrique anglaise (Open Government Licence v3.0).

#### Annexe 2 de la BKompV, types appelés

| Code | Biotoptyp (libellé de l'annexe 2) | Biotoptypenwert (sur 24) | Valeur OpenNAT (sur 1) |
|---|---|---|---|
| 22.01.02 | Kalkreiche Sicker- und Sumpfquellen (Helokrenen) (inkl. Kalktuff-Sicker- und -Sumpfquelle) | 20 | 0,8333 |
| 22.02 | Grundquellen (Limnokrenen) | 22 | 0,9167 |
| 22.03 | Sturzquellen (Rheokrenen) (inkl. Kalktuff-Sturzquelle) | 22 | 0,9167 |
| 23.01 | Natürliche und naturnahe Fließgewässer | 22 | 0,9167 |
| 23.05.01a.01 | – Naturnahe Ausbildung/ohne oder mit extensiver Unterhaltung | 13 | 0,5417 |
| 23.07.01 | Wasserfall | 21 | 0,875 |
| 23.08a.01 | – Natürliche oder naturnahe Ausprägung | 20 | 0,8333 |
| 23.09 | Natürliche und naturnahe temporäre Fließgewässer | 20 | 0,8333 |
| 24.01a | Natürliche dystrophe Gewässer | 20 | 0,8333 |
| 24.02a | Natürliche oligotrophe Gewässer | 22 | 0,9167 |
| 24.03b | Sonstige natürliche mesotrophe Gewässer | 19 | 0,7917 |
| 24.04b | Sonstige natürliche eutrophe Gewässer | 16 | 0,6667 |
| 24.04c | Naturnahe eutrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) | 15 | 0,625 |
| 24.06.01 | Salzhaltiges, perennierendes, stehendes Gewässer (Binnenlandsalzstellen) | 21 | 0,875 |
| 24.07.05 | Zier- und Löschteich | 5 | 0,2083 |
| 24.07.08 | Offene Wasserrückhaltebecken | 5 | 0,2083 |
| 24.08a.01 | – Natürliche oder naturnahe Ausprägung | 18 | 0,75 |
| 24.09a | Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) | 19 | 0,7917 |
| 32.01a | Natürliche Felsen | 20 | 0,8333 |
| 32.03a.01 | Natürliche Block- und Schutthalden | 20 | 0,8333 |
| 32.09 | Vegetationslose bzw. -arme Sandfläche | 18 | 0,75 |
| 32.11.09a | Bauflächen und Baustelleneinrichtungsflächen | 3 | 0,125 |
| 33.04a.02 | – Acker mit artenreicher Segetalvegetaion (Lehm- oder Tonboden) | 16 | 0,6667 |
| 33.04a.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) | 6 | 0,25 |
| 33.04a.04 | – Ackerbrache (Lehm- oder Tonboden) | 8 | 0,3333 |
| 33.05.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Torf- oder Anmoorboden) | 5 | 0,2083 |
| 34.01 | Trockenrasen auf karbonatischem oder silikatischem Untergrund | 21 | 0,875 |
| 34.02a | Halbtrockenrasen, beweidet oder gemäht | 21 | 0,875 |
| 34.02b | Halbtrockenrasen, brachgefallen bzw. ungenutzt | 17 | 0,7083 |
| 34.03.01a | Steppenrasen, beweidet oder gemäht | 22 | 0,9167 |
| 34.04.01a | Annuelle Sandtrockenrasen und Silbergrasfluren | 20 | 0,8333 |
| 34.04.03.01a | – Beweidet oder gemäht | 21 | 0,875 |
| 34.05.01 | Natürlicher und halbnatürlicher Schwermetallrasen | 21 | 0,875 |
| 34.07a.01 | Artenreiche, frische Mähwiese | 20 | 0,8333 |
| 34.07b.01 | Mäßig artenreiche, frische Mähwiese | 15 | 0,625 |
| 34.07b.02 | Mäßig artenreiche, frische (Mäh-)Weide | 13 | 0,5417 |
| 34.07b.03 | Mäßig artenreiche, frische Grünlandbrache | 11 | 0,4583 |
| 34.08a.01 | Intensiv genutztes, frisches Dauergrünland | 8 | 0,3333 |
| 34.09 | Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) | 8 | 0,3333 |
| 35.01a | – Weitgehend intakt | 24 | 1 |
| 35.02.01a | – Bewirtschaftet | 23 | 0,9583 |
| 35.02.03a.01 | – Bewirtschaftet | 20 | 0,8333 |
| 35.02.05.01 | – Extensiv bewirtschaftet | 18 | 0,75 |
| 35.02.06.03 | Brachgefallenes, artenarmes Feuchtgrünland | 12 | 0,5 |
| 35.03 | Salzgrünland des Binnenlandes | 22 | 0,9167 |
| 36.01 | Hochmoore (weitgehend intakt) | 24 | 1 |
| 36.02 | Übergangsmoore und Zwischenmoore (weitgehend intakt) | 23 | 0,9583 |
| 36.04.04 | Torfhalden | 5 | 0,2083 |
| 37.02 | Nährstoffreiches Großseggenried | 16 | 0,6667 |
| 38.02.01 | Schilf-Wasserröhricht | 19 | 0,7917 |
| 38.02.02 | Schilf-Landröhricht | 15 | 0,625 |
| 38.07 | Sonstiges Röhricht | 16 | 0,6667 |
| 39.01.01 | Wald- und Gehölzsäume oligo- bis eutropher, trockener bis nasser Standorte | 16 | 0,6667 |
| 39.02 | Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) | 10 | 0,4167 |
| 39.04a.01 | – Naturnahe Ausprägung | 17 | 0,7083 |
| 39.06.02 | Trocken-warme Ruderalstandorte auf bindigem Boden | 14 | 0,5833 |
| 39.06.03 | Frische bis nasse Ruderalstandorte | 12 | 0,5 |
| 39.07 | Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) | 10 | 0,4167 |
| 40.02.01 | – Weitgehend intakt | 22 | 0,9167 |
| 40.03.01 | – Weitgehend intakt | 19 | 0,7917 |
| 40.05 | Bergheiden („Hochheiden“) | 18 | 0,75 |
| 41.01.02 | (Weiden-)Gebüsch in Auen | 16 | 0,6667 |
| 41.01.03.01 | Moor-Gebüsch (z. B. mit Weiden, Gagel) | 16 | 0,6667 |
| 41.01.04.02 | Sonstiges Gebüsch frischer Standorte | 13 | 0,5417 |
| 41.01.05.03 | Trockenes Zwerg- und Weichselkirschen-Gebüsch | 18 | 0,75 |
| 41.01.05.04a | Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) | 16 | 0,6667 |
| 41.01.06 | Gebüsch stickstoffreicher, ruderaler Standorte und stark verbuschte Grünlandbrache (Verbuschung > 50 %) | 12 | 0,5 |
| 41.02.02J | – Junge Ausprägung | 13 | 0,5417 |
| 41.02.02M | – Mittlere Ausprägung | 14 | 0,5833 |
| 41.02.02A | – Alte Ausprägung | 17 | 0,7083 |
| 41.02.03J | – Junge Ausprägung | 14 | 0,5833 |
| 41.02.03M | – Mittlere Ausprägung | 15 | 0,625 |
| 41.02.03A | – Alte Ausprägung | 18 | 0,75 |
| 41.03.03J | – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken | 12 | 0,5 |
| 41.03.03M | – Mit Überhältern mittlerer Ausprägung | 16 | 0,6667 |
| 41.03.03A | – Mit Überhältern alter Ausprägung | 19 | 0,7917 |
| 41.03.03J | – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken | 12 | 0,5 |
| 41.03.03M | – Mit Überhältern mittlerer Ausprägung | 16 | 0,6667 |
| 41.03.03A | – Mit Überhältern alter Ausprägung | 19 | 0,7917 |
| 41.04J | – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken | 8 | 0,3333 |
| 41.04M | – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung | 11 | 0,4583 |
| 41.04A | – Alte Ausprägung/– Mit Überhältern alter Ausprägung | 14 | 0,5833 |
| 41.05aJ | – Junge Ausprägung | 11 | 0,4583 |
| 41.05aM | – Mittlere Ausprägung | 15 | 0,625 |
| 41.05aA | – Alte Ausprägung | 18 | 0,75 |
| 41.05bJ | – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken | 8 | 0,3333 |
| 41.05bM | – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung | 11 | 0,4583 |
| 41.05bA | – Alte Ausprägung/– Mit Überhältern alter Ausprägung | 14 | 0,5833 |
| 41.06.01.MA | – Mit mittlerem bis altem Baumbestand | 19 | 0,7917 |
| 41.07 | Gehölzplantagen und Hopfenkulturen | 6 | 0,25 |
| 41.08.02 | Rebkulturen in ebener bis schwach geneigter Lage | 9 | 0,375 |
| 42.03.02 | Vorwald frischer Standorte | 13 | 0,5417 |
| 42.04.01 | – Hudewald mit traditioneller Weidenutzung | 22 | 0,9167 |
| 43.02.01.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.02.01.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.02.01.01A | – Alte Ausprägung | 24 | 1 |
| 43.02.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.02.02.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.02.02.01A | – Alte Ausprägung | 23 | 0,9583 |
| 43.03.01J | – Junge Ausprägung | 15 | 0,625 |
| 43.03.01M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.03.01A | – Alte Ausprägung | 21 | 0,875 |
| 43.04.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.04.02.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.04.02.01A | – Alte Ausprägung | 23 | 0,9583 |
| 43.04.03.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.04.03.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.04.03.01A | – Alte Ausprägung | 22 | 0,9167 |
| 43.07.02J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.02M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.07.02A | – Alte Ausprägung | 23 | 0,9583 |
| 43.07.03J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.03M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.07.03A | – Alte Ausprägung | 23 | 0,9583 |
| 43.07.04J | – Junge Ausprägung | 14 | 0,5833 |
| 43.07.04M | – Mittlere Ausprägung | 17 | 0,7083 |
| 43.07.04A | – Alte Ausprägung | 20 | 0,8333 |
| 43.07.06J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.06M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.07.06A | – Alte Ausprägung | 21 | 0,875 |
| 43.08.05J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.05M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.08.05A | – Alte Ausprägung | 21 | 0,875 |
| 43.10J | – Junge Ausprägung | 9 | 0,375 |
| 43.10M | – Mittlere Ausprägung | 12 | 0,5 |
| 43.10A | – Alte Ausprägung | 14 | 0,5833 |
| 43.10J | – Junge Ausprägung | 9 | 0,375 |
| 43.10M | – Mittlere Ausprägung | 12 | 0,5 |
| 43.10A | – Alte Ausprägung | 14 | 0,5833 |
| 44.01.02J | – Junge Ausprägung | 14 | 0,5833 |
| 44.01.02M | – Mittlere Ausprägung | 20 | 0,8333 |
| 44.01.02A | – Alte Ausprägung | 23 | 0,9583 |
| 44.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.01M | – Mittlere Ausprägung | 17 | 0,7083 |
| 44.02.01A | – Alte Ausprägung | 21 | 0,875 |
| 44.02.03J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.03M | – Mittlere Ausprägung | 19 | 0,7917 |
| 44.02.03A | – Alte Ausprägung | 22 | 0,9167 |
| 44.03.03J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.03M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.03A | – Alte Ausprägung | 21 | 0,875 |
| 44.04J | – Junge Ausprägung | 9 | 0,375 |
| 44.04M | – Mittlere Ausprägung | 11 | 0,4583 |
| 44.04A | – Alte Ausprägung | 14 | 0,5833 |
| 44.05J | – Junge Ausprägung | 6 | 0,25 |
| 44.05M | – Mittlere Ausprägung | 10 | 0,4167 |
| 44.05A | – Alte Ausprägung | 12 | 0,5 |
| 51.04a.01 | – Mit wesentlichen Anteilen struktur-/artenreicher Ausprägung | 12 | 0,5 |
| 51.06a.03 | Intensiv gepflegte Parkanlage mit altem Baumbestand | 13 | 0,5417 |
| 51.07a.02 | Sonstige Grünanlage ohne alten Baumbestand | 9 | 0,375 |
| 51.08a.01 | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich | 11 | 0,4583 |
| 52.01.01a | Versiegelter oder sonstiger gepflasterter Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) | 0 | 0 |
| 52.02.06 | Unbefestigter Weg | 10 | 0,4167 |
| 52.03.01 | Versiegelter Platz oder sonstiger gepflasterter Platz | 0 | 0 |
| 52.03.02 | Teilbefestigter Platz (z. B. Rasengitter) | 3 | 0,125 |
| 52.03.03a | Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) | 4 | 0,1667 |
| 52.04.01 | Gleiskörper | 1 | 0,0417 |
| 63.04 | Silikatschutthalde der subalpinen bis alpinen Stufe | 12 | 0,5 |
| 64.01 | Kalkschneeboden | 17 | 0,7083 |
| 66.02 | Polsterseggenrasen | 17 | 0,7083 |
| 66.06 | Alpenfettweide | 14 | 0,5833 |
| 66.09 | Krummseggenrasen | 19 | 0,7917 |
| 67.01 | Hochstauden- und Hochgrasflur der hochmontanen bis alpinen Stufe | 16 | 0,6667 |
| 68.01 | Alpine „Windheide“ (z. B. mit Gamsheide) | 19 | 0,7917 |
| 69.02 | Grünerlengebüsche | 15 | 0,625 |
| 69.04 | Latschengebüsch | 15 | 0,625 |
| 69.05 | Alpenrosengebüsch | 17 | 0,7083 |
| 69.07 | Knieweidengebüsch | 16 | 0,6667 |
| 70.03J | – Junge Ausprägung | 15 | 0,625 |
| 70.03M | – Mittlere Ausprägung | 18 | 0,75 |
| 70.03A | – Alte Ausprägung | 21 | 0,875 |

#### Métrique statutaire anglaise, lignes appelées

| Ligne de la métrique | Types OpenNAT qui y renvoient |
|---|---|
| Coastal saltmarsh - Saltmarshes and saline reedbeds | D6.1, E6.1 |
| Cropland - Arable field margins cultivated annually | I1.3 |
| Cropland - Cereal crops | I1.1 |
| Cropland - Horticulture | FB.1, FB.2, FB.4, I1.2 |
| Cropland - Non-cereal crops | I1.4 |
| Grassland - Bracken | E5.3 |
| Grassland - Floodplain wetland mosaic and CFGM | E3.4 |
| Grassland - Lowland calcareous grassland | E1.2, E1.3, E1.4, E1.D |
| Grassland - Lowland dry acid grassland | E1.7, E1.8, E1.9, E1.A |
| Grassland - Lowland meadows | E2.2 |
| Grassland - Modified grassland | VB.5, E1.E, E2.6, E2.8 |
| Grassland - Other neutral grassland | VB.26, E1.C, E2.1, E2.7 |
| Grassland - Tall herb communities (H6430) | E5.4, E5.5 |
| Grassland - Traditional orchards | G1.D, G2.9 |
| Grassland - Upland acid grassland | E4.3 |
| Grassland - Upland calcareous grassland | E1.5, E4.4 |
| Grassland - Upland hay meadows | E2.3, E4.5 |
| Heathland and shrub - Gorse scrub | F5.4 |
| Heathland and shrub - Lowland heathland | F4.1, F4.2, F6.1, F6.6 |
| Heathland and shrub - Mixed scrub | VB.9, F3.1, F3.2, F5.1, F5.2, F5.3, F5.5, F6.8 |
| Heathland and shrub - Mountain heaths and willow scrub | E4.1, E4.2, F2.1, F2.2, F2.3, F2.4 |
| Heathland and shrub - Upland heathland | F7.1, F7.2, F7.4 |
| Heathland and shrub - Willow scrub | F9.1, F9.2, F9.3 |
| Individual trees - Rural tree | G5.1 |
| Individual trees - Urban tree | VB.18a, VB.18b |
| Lakes - High alkalinity lakes | C1.3, C1.5 |
| Lakes - Low alkalinity lakes | C1.1 |
| Lakes - Moderate alkalinity lakes | C1.2 |
| Lakes - Ornamental lake or pond | VB.21 |
| Lakes - Peat lakes | C1.4 |
| Lakes - Ponds (non-priority habitat) | VB.20 |
| Lakes - Ponds (priority habitat) | C2.1, C2.2, C2.3, C2.4, C2.6 |
| Lakes - Temporary lakes ponds and pools (H3170) | C1.6, C2.5, C3.4, C3.5 |
| Native hedgerow | FA.2, FA.4 |
| Non-native and ornamental hedgerow | FA.1 |
| Sparsely vegetated land - Calaminarian grasslands | E1.B |
| Sparsely vegetated land - Inland rock outcrop and scree habitats | C3.8, E1.1, H2.3, H2.4, H2.5, H2.6, H3.1, H3.2, H3.4, H3.6 |
| Sparsely vegetated land - Limestone pavement | H3.5 |
| Sparsely vegetated land - Other inland rock and scree | H5.2, H5.3 |
| Sparsely vegetated land - Ruderal/Ephemeral | C3.6, C3.7, E1.6, E5.1, H5.4, I1.5 |
| Sparsely vegetated land - Tall forbs | E5.2 |
| Species-rich native hedgerow | FA.3 |
| Urban - Allotments | VB.22 |
| Urban - Artificial unvegetated, unsealed surface | VB.3, VB.4, H5.6 |
| Urban - Bare ground | VB.10 |
| Urban - Biodiverse green roof | VB.12 |
| Urban - Built linear features | VB.25 |
| Urban - Developed land; sealed surface | VB.1, VB.2 |
| Urban - Facade-bound green wall | VB.16 |
| Urban - Ground based green wall | VB.15 |
| Urban - Ground level planters | VB.23 |
| Urban - Intensive green roof | VB.13 |
| Urban - Introduced shrub | VB.6, FB.3 |
| Urban - Open mosaic habitats on previously developed land | VB.8 |
| Urban - Other green roof | VB.11 |
| Urban - Rain garden | VB.19 |
| Urban - Sustainable drainage system | VB.24 |
| Urban - Vegetated garden | VB.7, I2.1, I2.3 |
| Wetland - Blanket bog | D1.2 |
| Wetland - Fens (upland and lowland) | D2.2, D4.1, D4.2, D5.2 |
| Wetland - Lowland raised bog | D1.1 |
| Wetland - Oceanic valley mire[1] (D2.1) | D2.1 |
| Wetland - Purple moor grass and rush pastures | D5.3, E3.1, E3.2, E3.5 |
| Wetland - Reedbeds | C3.1, C3.2, C3.3, D5.1, D6.2 |
| Wetland - Transition mires and quaking bogs (H7140) | D2.3 |
| Woodland and forest - Felled | G5.8, H5.5 |
| Woodland and forest - Lowland beech and yew woodland | G1.6, G2.6, G3.9 |
| Woodland and forest - Lowland mixed deciduous woodland | G1.7, G1.8, G1.A, G2.1, G2.2, G2.4 |
| Woodland and forest - Native pine woodlands | G3.1, G3.2, G3.3 |
| Woodland and forest - Other Scot's pine woodland | G3.4, G3.5, G3.7 |
| Woodland and forest - Other coniferous woodland | G3.F, G5.4 |
| Woodland and forest - Other woodland; broadleaved | G1.C, G2.8, G5.2, G5.3, G5.6, G5.7 |
| Woodland and forest - Other woodland; mixed | G4.6, G4.8, G4.9, G4.B, G4.C, G4.D, G4.E, G4.F, G5.5 |
| Woodland and forest - Upland birchwoods | G1.9 |
| Woodland and forest - Wet woodland | G1.1, G1.2, G1.3, G1.4, G1.5, G1.B, G3.E, G4.1 |
| Woodland and forest - Wood-pasture and parkland | E7.1, E7.2, E7.3 |
### 2.18 Annexe 2 de la BKompV, liste complète

Liste complète des types de biotopes de l'annexe 2 de la BKompV et de leur valeur sur 24, dans l'ordre du texte (extraction du 18/10/2026). Les intitulés de rubrique, sans valeur, structurent la liste. Les types appelés par la nomenclature OpenNAT sont repris plus haut.

| Code | Biotoptyp | Valeur sur 24 | Valeur sur 1 |
|---|---|---|---|
|  | BIOTOPTYPEN DER MEERE UND KÜSTEN |  |  |
| 02. | BENTHAL DER NORDSEE |  |  |
| 02.01 | Eulitorales Benthal der Nordsee (Wattflächen, kurz: EBN) |  |  |
| 02.01.01.01 | EBN Felsen- und Steingrund mit Epibenthos | 17 | 0,7083 |
| 02.01.01.01.02 | EBN Felsen- und Steingrund mit epibenthischen Muscheln (Bivalvia) | 19 | 0,7917 |
| 02.01.01.02 | EBN Felsen- und Steingrund mit vereinzeltem Epibenthos, Weidegängern oder ohne epibenthische Makroflora oder -fauna | 15 | 0,625 |
| 02.01.02.01 | EBN Schillgrund mit Epibenthos | 21 | 0,875 |
| 02.01.02.02 | EBN Schillgrund mit Infauna | 15 | 0,625 |
| 02.01.02.03 | EBN Schillgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 15 | 0,625 |
| 02.01.03 | EBN Torfgrund – ausschließlich Wattenmeer und Ästuare | 18 | 0,75 |
| 02.01.04.01 | EBN Sandgrund mit Epibenthos (ggf. mit Queller oder Schlickgras) | 17 | 0,7083 |
| 02.01.04.01.01.03 | EBN Sandgrund mit Seegras (Zostera-Seegraswiesen) | 18 | 0,75 |
| 02.01.04.01.02 | EBN Sandgrund mit (lagestabilen) epibenthischen Muscheln (Bivalvia) | 21 | 0,875 |
| 02.01.04.02 | EBN Sandgrund mit Infauna | 16 | 0,6667 |
| 02.01.04.03 | EBN Sandgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora und -fauna | 15 | 0,625 |
| 02.01.05.01 | EBN Schlickgrund mit Epibenthos (ggf. mit Queller oder Schlickgras) | 17 | 0,7083 |
| 02.01.05.01.01.03 | EBN Schlickgrund mit Seegras (Zostera-Seegraswiesen) | 18 | 0,75 |
| 02.01.05.01.02 | EBN Schlickgrund mit (lagestabilen) epibenthischen Muscheln (Bivalvia) | 21 | 0,875 |
| 02.01.05.02 | EBN Schlickgrund mit Infauna | 17 | 0,7083 |
| 02.01.05.03 | EBN Schlickgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 16 | 0,6667 |
| 02.01.06a | EBN Biogenes Riff mit Europäischen Austern | 23 | 0,9583 |
| 02.01.07a | EBN Biogenes Riff mit (lagestabilen) Pazifischen Austern | 16 | 0,6667 |
| 02.01.08a | EBN Biogenes Riff mit (lagestabilen) Miesmuscheln (Mytilus edulis) | 22 | 0,9167 |
| 02.01.09a | EBN Muschelkulturen | 8 | 0,3333 |
| 02.02 | Sublitorales Benthal der Nordsee (kurz: SBN) |  |  |
| 02.02.01.01 | SBN Felsen- und Steingrund mit Epibenthos | 13 | 0,5417 |
| 02.02.01.02 | SBN Felsen- und Steingrund mit vereinzeltem Epibenthos, Weidegängern oder ohne epibenthische Makroflora oder -fauna | 11 | 0,4583 |
| 02.02.02a | SBN Geschiebemergel-/Kleigrund – vorwiegend an exponierten Küstenabschnitten | 13 | 0,5417 |
| 02.02.04.01 | SBN Schillgrund mit Epibenthos | 15 | 0,625 |
| 02.02.04.01.02 | SBN Schillgrund mit Nesseltieren (Cnidaria) | 16 | 0,6667 |
| 02.02.04.02 | SBN Schillgrund mit Infauna | 11 | 0,4583 |
| 02.02.04.03 | SBN Schillgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 11 | 0,4583 |
| 02.02.05 | SBN Torfgrund – vorwiegend Wattenmeer und Ästuare | 14 | 0,5833 |
| 02.02.06.01 | SBN Mischsubstrat mit Epibenthos | 15 | 0,625 |
| 02.02.06.02 | SBN Mischsubstrat mit vereinzeltem Epibenthos, Weidegängern oder ohne epibenthische Makroflora oder -fauna | 11 | 0,4583 |
| 02.02.07 | SBN Grobsedimentbank (Sandbank-Komplex) | 14 | 0,5833 |
| 02.02.08.01 | SBN Ebenes Grobsediment mit Epibenthos | 15 | 0,625 |
| 02.02.08.02 | SBN Ebenes Grobsediment mit Infauna | 14 | 0,5833 |
| 02.02.08.02.01.02 | SBN Ebenes Grobsediment mit Goniadella-Spisula-Gemeinschaft, dominiert von Trogmuscheln (Mactra/Spisula) | 15 | 0,625 |
| 02.02.08.03 | SBN Ebenes Grobsediment mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 11 | 0,4583 |
| 02.02.09 | SBN Sandbank (inkl. Megarippelfelder) | 13 | 0,5417 |
| 02.02.10.01 | SBN Ebener Sandgrund mit Epibenthos | 15 | 0,625 |
| 02.02.10.01.01a | SBN Ebener Sandgrund mit Makrophytenbeständen oder Seegraswiesen (wurzelnden Pflanzen, Laichkräutern, Meersalden, Zostera-Seegraswiesen oder Teichfaden) – nur Wattenmeer und Ästuare | 18 | 0,75 |
| 02.02.10.02 | SBN Ebener Sandgrund mit Infauna | 13 | 0,5417 |
| 02.02.10.02.01.01 | SBN Sandgrund mit Amphiura filiformis-Gemeinschaft, dominiert von Callianassa/Nephrops/Upogebia | 14 | 0,5833 |
| 02.02.10.02.01.02 | SBN Ebener Sandgrund mit Amphiura filiformis-Gemeinschaft, dominiert von Islandmuscheln (Arctica islandica) | 17 | 0,7083 |
| 02.02.10.02.03 | SBN Ebener Sandgrund mit Bathyporaia-Tellina-Gemeinschaft – nur offene Nordsee | 14 | 0,5833 |
| 02.02.10.03 | SBN Ebener Sandgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 11 | 0,4583 |
| 02.02.11.01 | SBN Schlickgrund mit Epibenthos, vor allem mit wurzelnden Pflanzen – nur gering exponierte, flache Buchten des Wattenmeeres und der Ästuare | 17 | 0,7083 |
| 02.02.11.02 | SBN Schlickgrund mit Infauna | 13 | 0,5417 |
| 02.02.11.02.01.01 | SBN Schlickgrund mit Amphiura filiformis-Gemeinschaft, dominiert von Calianassa/Nephrops/Upogebia | 14 | 0,5833 |
| 02.02.11.02.01.02 | SBN Schlickgrund mit Amphiura filiformis-Gemeinschaft, dominiert von Islandmuscheln (Arctica islandica) | 17 | 0,7083 |
| 02.02.11.02.02.04 | SBN Schlickgrund mit Nucula nitidosa-Gemeinschaft, dominiert von Islandmuscheln (Arctica islandica) | 17 | 0,7083 |
| 02.02.11.03 | SBN Schlickgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora und -fauna – vorwiegend gering exponierte, flache Buchten des Wattenmeeres und der Ästuare | 11 | 0,4583 |
| 02.02.12a | SBN Geogenes Riff inkl. Steinfeld/Blockfeld, mariner Findling, Restsediment mit vereinzelten Steinen oder Blöcken | 17 | 0,7083 |
| 02.02.13a.01 | SBN Biogenes Riff mit (lagestabilen) Miesmuscheln (Mytilus edulis) | 20 | 0,8333 |
| 02.02.13a.02 | SBN Biogenes Riff mit epibenthischen Vielborstern, v. a. Sandkoralle (Sabellaria) | 22 | 0,9167 |
| 02.02.13a.03 | SBN Biogenes Riff mit Europäischen Austern | 22 | 0,9167 |
| 02.02.13a.04 | SBN Biogenes Riff mit Pazifischen Austern | 13 | 0,5417 |
| 02.02.13a.05 | SBN Artenreiche Kies-, Grobsand- und Schillgründe | 15 | 0,625 |
| 02.02.13a.06 | SBN Muschelkulturen | 7 | 0,2917 |
| 05. | BENTHAL DER OSTSEE |  |  |
| 05.01 | Hydrolitorales Benthal der Ostsee (Windwatt, kurz: HBO) |  |  |
| 05.01.01 | HBO Felsen- und Steingrund | 12 | 0,5 |
| 05.01.01.01.01 | HBO Felsen- und Steingrund mit mehrjährigen (festsitzenden) Makroalgen, v. a. Fucus vesiculosus | 16 | 0,6667 |
| 05.01.02 | HBO Torfgrund | 15 | 0,625 |
| 05.01.03 | HBO Mischsubstrat | 12 | 0,5 |
| 05.01.03.01.01 | HBO Mischsubstrat mit wurzelnden Pflanzen – überwiegend in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 16 | 0,6667 |
| 05.01.03.01.02 | HBO Mischsubstrat mit mehrjährigen (festsitzenden) Makroalgen, v. a. Fucus vesiculosus | 16 | 0,6667 |
| 05.01.04 | HBO Grobsediment | 12 | 0,5 |
| 05.01.04.01.01 | HBO Grobsediment mit wurzelnden Pflanzen – überwiegend in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 16 | 0,6667 |
| 05.01.04.01.01 | HBO Grobsediment mit mehrjährigen (festsitzenden) Makroalgen, v. a. Fucus vesiculosus | 16 | 0,6667 |
| 05.01.05.01.01 | HBO Sandgrund mit wurzelnden Pflanzen – überwiegend in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 16 | 0,6667 |
| 05.01.05.02 | HBO Sandgrund mit Infauna | 14 | 0,5833 |
| 05.01.05.03a | HBO Hydrolitoraler Sandgrund der Ostsee mit (vereinzeltem) Epibenthos oder ohne Makroflora oder -fauna | 12 | 0,5 |
| 05.01.06.02 | HBO Schlickgrund mit Infauna | 14 | 0,5833 |
| 05.01.06.03a | HBO Schlickgrund mit (vereinzeltem) Epibenthos oder ohne Makroflora oder -fauna | 12 | 0,5 |
| 05.02 | Sublitorales Benthal der Ostsee (kurz: SBO) |  |  |
| 05.02.01.01 | SBO Felsen- und Steingrund mit Epibenthos | 13 | 0,5417 |
| 05.02.01.01.01a | SBO Felsen- und Steingrund mit Fucus oder Furcellaria lumbricalis | 15 | 0,625 |
| 05.02.01.02 | SBO Felsen- und Steingrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora und -fauna | 11 | 0,4583 |
| 05.02.02a | SBO aufragender oder ebener Geschiebemergelgrund – vorwiegend an exponierten Küstenabschnitten der offenen Ostsee | 13 | 0,5417 |
| 05.02.04 | SBO Schillgrund | 13 | 0,5417 |
| 05.02.05 | SBO Torfgrund | 14 | 0,5833 |
| 05.02.06.01 | SBO Mischsubstrat mit Epibenthos | 13 | 0,5417 |
| 05.02.06.01.01.01 | SBO Mischsubstrat mit Armleuchteralgen (Characeae) – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.06.01.01.04a | SBO Mischsubstrat mit Seegräsern (Zostera-Seegraswiesen) | 16 | 0,6667 |
| 05.02.06.01.02.01a | SBO Mischsubstrat mit Fucus oder Furcellaria lumbricalis | 15 | 0,625 |
| 05.02.06.02 | SBO Mischsubstrat mit vereinzeltem Epibenthos, Weidegängern oder ohne epibenthische Makroflora oder -fauna | 11 | 0,4583 |
| 05.02.07 | SBO Grobsedimentbank (Sandbank-Komplex) | 13 | 0,5417 |
| 05.02.08.01.01.03 | SBO Ebenes Grobsediment mit Seegräsern (Zostera-Seegraswiesen) | 16 | 0,6667 |
| 05.02.08.01.02 | SBO Ebenes Grobsediment mit mehrjährigen (festsitzenden) Makroalgen | 15 | 0,625 |
| 05.02.08.02 | SBO Ebenes Grobsediment der Ostsee mit Infauna | 13 | 0,5417 |
| 05.02.08.03a | SBO Ebenes Grobsediment mit (vereinzeltem) Epibenthos, Weidegängern oder ohne epibenthische Makroflora oder -fauna | 11 | 0,4583 |
| 05.02.09 | SBO Sandbank (Sandbank-Komplex, inkl. Megarippelfelder) | 11 | 0,4583 |
| 05.02.10.01 | SBO Ebener Sandgrund mit Epibenthos oder wurzelnden Pflanzen | 14 | 0,5833 |
| 05.02.10.01.01.01 | SBO Ebener Sandgrund mit Armleuchteralgen (Characeae) – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.10.01.01.04 | SBO Ebener Sandgrund mit Nixkraut (Najas marina) – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.10.01.01.05 | SBO Sandgrund mit Seegräsern (Zostera-Seegraswiesen) | 16 | 0,6667 |
| 05.02.10.01.03 | SBO Ebener Sandgrund mit mehrjährigen (nicht festsitzenden) Makroalgen – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.10.02 | SBO Ebener Sandgrund mit Infauna | 11 | 0,4583 |
| 05.02.10.03 | SBO Ebener Sandgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora oder -fauna | 11 | 0,4583 |
| 05.02.11.01 | SBO Schlickgrund mit Epibenthos oder wurzelnden Pflanzen | 13 | 0,5417 |
| 05.02.11.01.01.01 | SBO Schlickgrund mit Armleuchteralgen (Characeae) – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.11.01.01.04 | SBO Schlickgrund mit Nixkraut (Najas marina) – nur in flachen Buchten (Bodden, Haffe), Förden, Lagunen und Ästuaren | 15 | 0,625 |
| 05.02.11.01.01.05 | SBO Sandgrund mit Seegräsern (Zostera-Seegraswiesen) | 16 | 0,6667 |
| 05.02.11.02 | SBO Schlickgrund mit Infauna | 11 | 0,4583 |
| 05.02.11.03 | SBO Schlickgrund mit vereinzeltem Epibenthos, Weidegängern oder ohne Makroflora und -fauna | 11 | 0,4583 |
| 05.02.12a | SBO Geogenes Riff inkl. Steinfeld/Blockfeld, mariner Findling, Restsediment mit vereinzelten Steinen oder Blöcken | 16 | 0,6667 |
| 05.02.13a | SBO Biogenes Riff mit (lagestabilen) Miesmuscheln (Mytilus edulis) | 15 | 0,625 |
| 05.02.14a | SBO Artenreiche Kies-, Grobsand- und Schillgründe | 15 | 0,625 |
| 06a. | ANTHROPOGENE STRUKTUREN IM MEERES- UND KÜSTENBEREICH |  |  |
| 06a.01. | Künstliche Strukturen im Meeres- und Küstenbereich |  |  |
| 06a.01.01 | Hafenbecken und Marinas | 6 | 0,25 |
| 06a.01.02 | Hafenanlage an Land, Kai | 1 | 0,0417 |
| 06a.01.03 | Küstenschutzbauwerk (inkl. Steinschüttungen, Deckwerke) | 4 | 0,1667 |
| 06a.01.04 | Buhne, Mole | 5 | 0,2083 |
| 06a.01.05 | Lahnung | 9 | 0,375 |
| 06a.01.06 | Schiffswrack | 9 | 0,375 |
| 06a.02 | Sonstige technische Bauwerke über Meeresboden |  |  |
| 06a.02.01 | Technisches Bauwerk aus Naturstein/natürlichem Substrat in gleichartigem natürlichen Umgebungssubstrat | 9 | 0,375 |
| 06a.02.02 | Technisches Bauwerk aus Naturstein/natürlichem Material in anderem natürlichen Substrat | 4 | 0,1667 |
| 06a.02.03 | Technisches Bauwerk aus sonstigen Materialien | 2 | 0,0833 |
| 06a.03 | Naturfernes Salz- und Brackgewässer im Küstenbereich |  |  |
| 06a.03.01 | Fahrrinne im Wattenmeer | 5 | 0,2083 |
| 06a.03.02 | Ausgebauter Brackwasserbach | 8 | 0,3333 |
| 06a.03.03 | Salz- und Brackwassergraben im Küstenbereich | 8 | 0,3333 |
| 06a.03.04 | Naturfernes salzhaltiges Abgrabungsgewässer der Küste | 5 | 0,2083 |
| 06a.03.05 | Sonstiges anthropogenes Salz- und Brackgewässer im Küstenbereich | 6 | 0,25 |
| 06a.04 | Anthropogene Sand-, Spül- und Verlandungsflächen |  |  |
| 06a.04.01 | Spülfläche mit Wattvegetation | 10 | 0,4167 |
| 06a.04.02 | Spülfläche mit Salzwiese | 10 | 0,4167 |
| 06a.04.03 | Sonstige Spül- und Verlandungsflächen | 8 | 0,3333 |
| 07. | SALZGRÜNLAND DER NORDSEEKÜSTE (Supralitoral) |  |  |
| 07.01 | Unteres Salzgrünland der Nordseeküste (z. B. Andelrasen) | 18 | 0,75 |
| 07.02 | Höhergelegenes Salzgrünland der Nordseeküste (z. B. Rotschwingel- und Bottenbinsenrasen) | 16 | 0,6667 |
| 07.03 | Strandwiesen der Nordseeküste [Komplex] | 19 | 0,7917 |
| 07.04 | Brack- und Salzwasserröhricht der Nordseeküste und der Ästuare | 18 | 0,75 |
| 07.05 | Brackwasser-Hochstaudenflur der Nordseeküste und der Ästuare | 20 | 0,8333 |
| 07.06 | Brackwasserbeeinflusstes Grünland der Nordseeküste und der Ästuare | 20 | 0,8333 |
| 08. | SALZGRÜNLAND, BRACKWASSERRÖHRICHTE UND HOCHSTAUDENFLUREN DES GEOLITORALS DER OSTSEEKÜSTE |  |  |
| 08.01 | Salzgrünland des Geolitorals der Ostseeküste (ohne Röhrichte) | 21 | 0,875 |
| 08.02 | Brackwasserröhrichte der Ostseeküste (Übergangsbereich Hydro- und Geolitoral) | 17 | 0,7083 |
| 08.03 | Brackwasser-Hochstaudenfluren der Ostseeküste | 18 | 0,75 |
| 08.04 | Schlenke, Kolk und Rinne des Geolitorals der Ostseeküste mit Pioniervegetation (u. a. Queller) | 18 | 0,75 |
| 08.05 | Strandwiesen der Ostseeküste [Komplex] | 18 | 0,75 |
| 09. | SÄNDE, SAND-, GERÖLL- UND BLOCKSTRÄNDE |  |  |
| 09.01 | Sandbank, Außensand und Nehrungshaken | 18 | 0,75 |
| 09.02 | Sandstrände und Sandplaten | 18 | 0,75 |
| 09.03 | Kies- und Geröllstrände | 17 | 0,7083 |
| 09.04 | Blockstrände | 17 | 0,7083 |
| 09.05 | Strandwälle | 18 | 0,75 |
| 09.06 | Strandgewässer | 20 | 0,8333 |
| 10. | KÜSTENDÜNEN |  |  |
| 10.01 | Vordüne | 20 | 0,8333 |
| 10.02 | Weißdüne | 18 | 0,75 |
| 10.03 | Graudünen (Dünenrasen) | 20 | 0,8333 |
| 10.04 | Braundünen (Küstendünenheiden) | 20 | 0,8333 |
| 10.05 | Feuchte/nasse Dünentäler, inkl. Dünenmoore [Komplex] | 24 | 1 |
| 10.06 | Dünengebüsche | 18 | 0,75 |
| 10.07 | Wanderdüne | 22 | 0,9167 |
| 11. | FELS- UND STEILKÜSTEN |  |  |
| 11.01 | Sandstein-Felsküste (nur Helgoland) | 22 | 0,9167 |
| 11.02 | Kreide-Felsküste (Ostsee) | 18 | 0,75 |
| 11.03 | Geestkliff der Nordseeküste und -inseln | 19 | 0,7917 |
| 11.04 | Moränensteilküsten der Ostsee | 17 | 0,7083 |
| 12a. | FLIESSGEWÄSSER DER BRACKWASSER-ÄSTUARE |  |  |
| 12a.01 | Unverändertes und gering verändertes Fließgewässer der Brackwasser- Ästuare | 23 | 0,9583 |
| 12a.02 | Mäßig verändertes Fließgewässer der Brackwasser-Ästuare | 15 | 0,625 |
| 12a.03 | Stark verändertes Fließgewässer der Brackwasser-Ästuare | 6 | 0,25 |
| 12a.04 | Zeitweilig trockenfallende Lebensräume unterhalb des Mittelwasserbereichs an Ästuaren einschließlich Brackwasserwatt |  |  |
| 12a.04.01 | – Natürliche oder naturnahe Ausprägung | 20 | 0,8333 |
| 12a.04.02 | – Bedingt naturnahe Ausprägung | 14 | 0,5833 |
|  | BIOTOPTYPEN DES BINNENLANDES |  |  |
| 22. | QUELLEN (inkl. Quellabfluss [Krenal]) |  |  |
| 22.01.01 | Kalkarme Sicker- und Sumpfquellen (Helokrenen) | 22 | 0,9167 |
| 22.01.02 | Kalkreiche Sicker- und Sumpfquellen (Helokrenen) (inkl. Kalktuff-Sicker- und -Sumpfquelle) | 20 | 0,8333 |
| 22.02 | Grundquellen (Limnokrenen) | 22 | 0,9167 |
| 22.03 | Sturzquellen (Rheokrenen) (inkl. Kalktuff-Sturzquelle) | 22 | 0,9167 |
| 22.04 | Salz- oder Solquellen | 23 | 0,9583 |
| 22.05 | künstlich gefasste Quellen | 11 | 0,4583 |
| 23. | FLIESSENDE GEWÄSSER |  |  |
| 23.01 | Natürliche und naturnahe Fließgewässer | 22 | 0,9167 |
| 23.02 | Anthropogen mäßig beeinträchtigte Fließgewässer | 17 | 0,7083 |
| 23.03 | Anthropogen stark beeinträchtigte Fließgewässer |  |  |
| 23.03a.01 | – Typische Ausprägung | 8 | 0,3333 |
| 23.03a.02 | – Besondere Ausprägung mit Flachwasserzonen oder Wasserpflanzen | 13 | 0,5417 |
| 23.04 | Anthropogen sehr stark veränderte Fließgewässer |  |  |
| 23.04a.01 | – Typische Ausprägung | 5 | 0,2083 |
| 23.04a.02 | – Besondere Ausprägung mit Flachwasserzonen oder Wasserpflanzen | 9 | 0,375 |
| 23.05 | Künstliche lineare Gewässerstrukturen |  |  |
| 23.05.01a | Graben mit periodischer oder dauerhafter Wasserführung (fließendes oder stehendes Gewässer) |  |  |
| 23.05.01a.01 | – Naturnahe Ausbildung/ohne oder mit extensiver Unterhaltung | 13 | 0,5417 |
| 23.05.01a.02 | – Naturferne Ausbildung/intensive Unterhaltung | 8 | 0,3333 |
| 23.05.02 | Technische Rinne, Halbschale | 3 | 0,125 |
| 23.05.03 | Verrohrung | 1 | 0,0417 |
| 23.05.04a | Kanäle |  |  |
| 23.05.04a.01 | – Naturnahe Ausprägung | 10 | 0,4167 |
| 23.05.04a.02 | – Naturferne Ausprägung | 4 | 0,1667 |
| 23.05.05a | Technische Uferbefestigungen und -vorschüttungen, Regelungsbauwerke | 3 | 0,125 |
| 23.05.06a | Technische-biologische Ufersicherungen | 8 | 0,3333 |
| 23.05.07a | Spundwand | 1 | 0,0417 |
| 23.05.08a | Sonstige lineare Gewässerstrukturen, z. B. Fischpässe und Umgehungsgerinne |  |  |
| 23.05.08a.01 | – Naturnahe Ausbildung | 11 | 0,4583 |
| 23.05.08a.02 | – Naturferne Ausbildung | 4 | 0,1667 |
| 23.06 | Mündungen in Binnengewässer | 17 | 0,7083 |
| 23.07 | Sonderformen im Fließgewässerverlauf |  |  |
| 23.07.01 | Wasserfall | 21 | 0,875 |
| 23.07.02 | Altarm | 21 | 0,875 |
| 23.07.03 | Seeabfluss (natürlich oder naturnah) | 17 | 0,7083 |
| 23.07.04 | Staustrecke | 6 | 0,25 |
| 23.07.05 | Salzbach | 22 | 0,9167 |
| 23.08 | Zeitweilig trockenfallende Lebensräume unterhalb des Mittelwasserbereichs an fließenden Gewässern (einschließlich Süßwasserwatt) |  |  |
| 23.08a.01 | – Natürliche oder naturnahe Ausprägung | 20 | 0,8333 |
| 23.08a.02 | – Bedingt naturnahe Ausprägung | 14 | 0,5833 |
| 23.09 | Natürliche und naturnahe temporäre Fließgewässer | 20 | 0,8333 |
| 24. | STEHENDE GEWÄSSER |  |  |
| 24.01 | Dystrophe stehende Gewässer/Moorgewässer (natürliche oder naturnahe) |  |  |
| 24.01a | Natürliche dystrophe Gewässer | 20 | 0,8333 |
| 24.01b | Naturnahe dystrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) | 16 | 0,6667 |
| 24.02 | Oligotrophe stehende Gewässer (natürliche oder naturnahe) |  |  |
| 24.02a | Natürliche oligotrophe Gewässer | 22 | 0,9167 |
| 24.02b | Naturnahe oligotrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) | 17 | 0,7083 |
| 24.03 | Mesotrophe stehende Gewässer (natürliche oder naturnahe) |  |  |
| 24.03a | Natürliche mesotrophe Altwasser | 20 | 0,8333 |
| 24.03b | Sonstige natürliche mesotrophe Gewässer | 19 | 0,7917 |
| 24.03c | Naturnahe mesotrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) | 17 | 0,7083 |
| 24.04 | Eutrophe stehende Gewässer (natürliche oder naturnahe) |  |  |
| 24.04a | Natürliches eutrophes Altwasser und eutrophe Tümpel | 19 | 0,7917 |
| 24.04b | Sonstige natürliche eutrophe Gewässer | 16 | 0,6667 |
| 24.04c | Naturnahe eutrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) | 15 | 0,625 |
| 24.05 | Poly-hypertrophe stehende Gewässer | 7 | 0,2917 |
| 24.06 | Salzhaltige Binnengewässer (natürliche oder naturnahe) |  |  |
| 24.06.01 | Salzhaltiges, perennierendes, stehendes Gewässer (Binnenlandsalzstellen) | 21 | 0,875 |
| 24.06.02 | Gipshaltiges, perennierendes, stehendes Gewässer | 20 | 0,8333 |
| 24.06.03 | Salztümpel des Binnenlandes | 21 | 0,875 |
| 24.07 | Weitere stehende Gewässer |  |  |
| 24.07.01 | Naturferner, wassergefüllter Torfstich (aktuell im Abbau) | 4 | 0,1667 |
| 24.07.02 | Fischzuchtgewässer (intensive Nutzung) | 6 | 0,25 |
| 24.07.02a | Naturnahe Fischzuchtgewässer (extensive Nutzung) | 11 | 0,4583 |
| 24.07.05 | Zier- und Löschteich | 5 | 0,2083 |
| 24.07.06 | Klär- bzw. Schönungsteich | 4 | 0,1667 |
| 24.07.07 | Industrielles Absetzbecken, Spülfeld und Flüssigdeponie | 3 | 0,125 |
| 24.07.08 | Offene Wasserrückhaltebecken | 5 | 0,2083 |
| 24.07.10 | Speicherseen mit hohen Wasserstandsschwankungen | 6 | 0,25 |
| 24.07.11 | Wasseraufbereitungsanlage (offener Sickerteich) | 5 | 0,2083 |
| 24.07.12 | Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) |  |  |
| 24.07.12a | Abbaugewässer, im Abbau befindlich | 4 | 0,1667 |
| 24.07.12b | Abbaugewässer nach Beendigung des Abbaus mit extremem Chemismus (z. B. mit sehr niedrigem pH-Wert) | 3 | 0,125 |
| 24.07.12c | Junge Abbaugewässer nach Beendigung des Abbaus mit Flachwasserzonen oder Tümpeln mit naturnaher Entwicklung, vgl. 24.01b, 24.02b, 24.03c, 24.04c | 10 | 0,4167 |
| 24.07.13a | Sonstige stehende Gewässer (naturfern) | 5 | 0,2083 |
| 24.08 | Zeitweilig trockenfallende Lebensräume unterhalb des Mittelwasserbereichs an stehenden Gewässern |  |  |
| 24.08a.01 | – Natürliche oder naturnahe Ausprägung | 18 | 0,75 |
| 24.08a.02 | – Bedingt naturnahe Ausprägung | 13 | 0,5417 |
| 24.09a | Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) | 19 | 0,7917 |
| 31. | HÖHLEN (einschl. Stollen, Brunnenschächte, Bunkerruinen etc.) |  |  |
| 31.01a | Natürliche Höhlen, Höhlengewässer und Balmen (Halbhöhlen) sowie Eingangsbereiche von Höhlen | 20 | 0,8333 |
| 31.02 | Stollen, Schächte und Bunkerruinen |  |  |
| 31.02.01 | Sich selbst überlassene Stollen, Schächte und Bunkerruinen | 12 | 0,5 |
| 31.02.02 | In Betrieb befindliche Stollen bzw. Schächte (inkl. Besucherbergwerke) | 6 | 0,25 |
| 32. | FELSEN, BLOCK- UND SCHUTTHALDEN, GERÖLLFELDER, OFFENE BEREICHE MIT SANDIGEM ODER BINDIGEM SUBSTRAT |  |  |
| 32.01 | Natürliche und naturnah entwickelte Felsen |  |  |
| 32.01a | Natürliche Felsen | 20 | 0,8333 |
| 32.01b | Naturnah entwickelte Felsen in alten, stillgelegten Steinbrüchen | 16 | 0,6667 |
| 32.01c | Naturnah entwickelte Felsen an Verkehrsanlagen | 12 | 0,5 |
| 32.02 | Solitärer Felsblock, Findling | 16 | 0,6667 |
| 32.03a | Natürliche und naturnah entwickelte Block- und Schutthalden |  |  |
| 32.03a.01 | Natürliche Block- und Schutthalden | 20 | 0,8333 |
| 32.03a.02 | Naturnah entwickelte Block- und Schutthalden (insbes. in alten, stillgelegten Abbaugebieten) | 15 | 0,625 |
| 32.06 | Wände aus Sand und Lockergestein | 18 | 0,75 |
| 32.07 | Lehm- und Lösswände | 18 | 0,75 |
| 32.08 | Vegetationslose bzw. -arme Kies- und Schotterfläche | 18 | 0,75 |
| 32.09 | Vegetationslose bzw. -arme Sandfläche | 18 | 0,75 |
| 32.10 | Vegetationslose bzw. -arme Fläche mit bindigem Substrat | 18 | 0,75 |
| 32.11 | Abbaubereiche und Abraumhalden sowie sonstige Bauflächen |  |  |
| 32.11.01a | Block- und Schutthalden sowie Halden aus sandig-kiesigem oder bindigem Substrat (Teilabschnitte können getrennt betrachtet werden) |  |  |
| 32.11.01a.01 | Junge Halden nach Beendigung der Aufschüttung mit naturnaher Entwicklung, vgl. 32.03a.02 | 10 | 0,4167 |
| 32.11.01a.02 | Junge Halden unmittelbar nach Beendigung des Abbaus oder neue, in Aufschüttung befindliche Halden | 3 | 0,125 |
| 32.11.04 | Felswände oder felsige Abbausohlen in Steinbrüchen (Teilabschnitte können getrennt betrachtet werden) |  |  |
| 32.11.04a | Junge Felswände oder junge felsige Abbausohlen in Steinbrüchen nach Beendigung des Abbaus mit naturnaher Entwicklung, vgl. 32.01b | 12 | 0,5 |
| 32.11.04b | Felswände und felsige Abbausohlen unmittelbar nach Beendigung des Abbaus oder neue, im Abbau befindliche Felswände und felsige Abbausohlen | 4 | 0,1667 |
| 32.11.06a | Ebenerdige Abbauflächen aus Blöcken, Schutt, Sand, Kies oder bindigem Substrat im Abbau (Teilabschnitte können getrennt betrachtet werden) |  |  |
| 32.11.06a.01 | Junge ebenerdige Abbauflächen nach Beendigung des Abbaus mit naturnaher Entwicklung, vgl. 32.08 bis 32.10 | 10 | 0,4167 |
| 32.11.06a.02 | Ebenerdige Abbauflächen unmittelbar nach Beendigung des Abbaus oder neue, im Abbau befindliche ebenerdige Abbauflächen | 3 | 0,125 |
| 32.11.08a | Steilwände aus Sand und Lockergestein in Abbaubereichen (Teilabschnitte können getrennt betrachtet werden) |  |  |
| 32.11.08a.01 | Junge Steilwände aus Sand und Lockergestein nach Beendigung des Abbaus bei vorgesehener naturnaher Entwicklung, vgl. 32.06 | 12 | 0,5 |
| 32.11.08a.02 | Steilwände aus Sand und Lockergestein unmittelbar nach Beendigung des Abbaus oder neue, im Abbau befindliche Steilwände aus Lockergestein | 4 | 0,1667 |
| 32.11.09a | Bauflächen und Baustelleneinrichtungsflächen | 3 | 0,125 |
| 33. | ÄCKER UND ACKERBRACHE |  |  |
| 33.01 | Flachgründige, skelettreiche Kalkäcker und Kalkackerbrache |  |  |
| 33.01.02 | – Acker mit artenreicher Segetalvegetaion (Kalkboden) | 17 | 0,7083 |
| 33.01.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Kalkboden) | 6 | 0,25 |
| 33.01.04 | – Ackerbrache (Kalkboden) | 11 | 0,4583 |
| 33.02 | Äcker und Ackerbrache auf flachgründigem, skelettreichem Silikatverwitterungsboden |  |  |
| 33.02.02 | – Acker mit artenreicher Segetalvegetaion (Silikatverwitterungsboden) | 16 | 0,6667 |
| 33.02.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Silikatverwitterungsboden) | 6 | 0,25 |
| 33.02.04 | – Ackerbrache (Silikatverwitterungsboden) | 11 | 0,4583 |
| 33.03 | Äcker und Ackerbrache auf Sandboden |  |  |
| 33.03.02 | – Acker mit artenreicher Segetalvegetaion (Sandboden) | 16 | 0,6667 |
| 33.03.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Sandboden) | 6 | 0,25 |
| 33.03.04 | – Ackerbrache (Sandboden) | 11 | 0,4583 |
| 33.04a | Äcker und Ackerbrache auf Lehm- oder Tonboden |  |  |
| 33.04a.02 | – Acker mit artenreicher Segetalvegetaion (Lehm- oder Tonboden) | 16 | 0,6667 |
| 33.04a.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) | 6 | 0,25 |
| 33.04a.04 | – Ackerbrache (Lehm- oder Tonboden) | 8 | 0,3333 |
| 33.04b | Äcker und Ackerbrache auf Lössboden |  |  |
| 33.04b.02 | – Acker mit artenreicher Segetalvegetaion (Lössboden) | 17 | 0,7083 |
| 33.04b.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Lössboden) | 7 | 0,2917 |
| 33.04b.04 | – Ackerbrache (Lössboden) | 9 | 0,375 |
| 33.05 | Äcker und Ackerbrache auf Torf- oder Anmoorboden |  |  |
| 33.05.02 | – Acker mit artenreicher Segetalvegetation (Torf- oder Anmoorboden) | 8 | 0,3333 |
| 33.05.03 | – Acker mit stark verarmter oder fehlender Segetalvegetation (Torf- oder Anmoorboden) | 5 | 0,2083 |
| 33.05.04 | – Ackerbrache (Torf- oder Anmoorboden) | 8 | 0,3333 |
| 34. | TROCKENRASEN SOWIE GRÜNLAND TROCKENER BIS FRISCHER STANDORTE |  |  |
| 34.01 | Trockenrasen auf karbonatischem oder silikatischem Untergrund | 21 | 0,875 |
| 34.02 | Halbtrockenrasen auf karbonatischem oder sonstigem basenreichen Untergrund inkl. Wacholderheiden |  |  |
| 34.02a | Halbtrockenrasen, beweidet oder gemäht | 21 | 0,875 |
| 34.02b | Halbtrockenrasen, brachgefallen bzw. ungenutzt | 17 | 0,7083 |
| 34.03 | Steppenrasen (subkontinental, auf tiefgründigem Boden) |  |  |
| 34.03.01a | Steppenrasen, beweidet oder gemäht | 22 | 0,9167 |
| 34.03.03 | Steppenrasen, brachgefallen bzw. ungenutzt | 19 | 0,7917 |
| 34.04 | Sandtrockenrasen und Silbergrasfluren |  |  |
| 34.04.01a | Annuelle Sandtrockenrasen und Silbergrasfluren | 20 | 0,8333 |
| 34.04.03 | Ausdauernde Sandtrockenrasen mit weitgehend geschlossener Narbe |  |  |
| 34.04.03.01a | – Beweidet oder gemäht | 21 | 0,875 |
| 34.04.03.03 | – Ungenutzt | 16 | 0,6667 |
| 34.05 | Schwermetallrasen |  |  |
| 34.05.01 | Natürlicher und halbnatürlicher Schwermetallrasen | 21 | 0,875 |
| 34.05.02 | Schwermetallrasen junger Abraumhalden des Bergbaus | 15 | 0,625 |
| 34.06 | Borstgrasrasen |  |  |
| 34.06.01a | Borstgrasrasen trockener bis frischer Standorte, beweidet oder gemäht | 21 | 0,875 |
| 34.06.01b | Borstgrasrasen trockener bis frischer Standorte, brachgefallen | 18 | 0,75 |
| 34.06.02a | Borstgrasrasen feuchter Standorte, beweidet oder gemäht | 22 | 0,9167 |
| 34.06.02b | Borstgrasrasen feuchter Standorte, brachgefallen | 19 | 0,7917 |
| 34.07a | Artenreiches Grünland frischer Standorte |  |  |
| 34.07a.01 | Artenreiche, frische Mähwiese | 20 | 0,8333 |
| 34.07a.02 | Artenreiche, frische (Mäh-)Weide | 18 | 0,75 |
| 34.07a.03 | Artenreiche, frische Grünlandbrache | 16 | 0,6667 |
| 34.07b | Mäßig artenreiches Grünland frischer Standorte |  |  |
| 34.07b.01 | Mäßig artenreiche, frische Mähwiese | 15 | 0,625 |
| 34.07b.02 | Mäßig artenreiche, frische (Mäh-)Weide | 13 | 0,5417 |
| 34.07b.03 | Mäßig artenreiche, frische Grünlandbrache | 11 | 0,4583 |
| 34.08 | Artenarmes Grünland frischer Standorte |  |  |
| 34.08a.01 | Intensiv genutztes, frisches Dauergrünland | 8 | 0,3333 |
| 34.08a.02 | Extensiv genutztes, frisches Dauergrünland | 11 | 0,4583 |
| 34.08.02 | Frisches Ansaatgrünland | 7 | 0,2917 |
| 34.08.03 | Artenarme, frische Grünlandbrache | 9 | 0,375 |
| 34.09 | Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) | 8 | 0,3333 |
| 35. | WALDFREIE NIEDERMOORE UND SÜMPFE, GRÜNLAND NASSER BIS FEUCHTER STANDORTE (ohne Röhrichte und Großseggenriede) |  |  |
| 35.01 | waldfreie, oligo- bis mesotrophe kalkarme oder kalkreiche Niedermoore und Sümpfe |  |  |
| 35.01a | – Weitgehend intakt | 24 | 1 |
| 35.01b | – Degeneriert (teilentwässert) | 16 | 0,6667 |
| 35.02 | Grünland nasser bis (wechsel-)feuchter Standorte |  |  |
| 35.02.01 | Pfeifengraswiesen (auf mineralischen und organischen Böden) |  |  |
| 35.02.01a | – Bewirtschaftet | 23 | 0,9583 |
| 35.02.01.03 | – Brachgefallen | 20 | 0,8333 |
| 35.02.02 | Brenndolden-Auenwiesen |  |  |
| 35.02.02a | – Bewirtschaftet | 23 | 0,9583 |
| 35.02.02.03 | – Brachgefallen | 21 | 0,875 |
| 35.02.03a | Sonstiges extensives Feucht- und Nassgrünland |  |  |
| 35.02.03a.01 | – Bewirtschaftet | 20 | 0,8333 |
| 35.02.03a.02 | – Brachgefallen | 16 | 0,6667 |
| 35.02.05 | Flutrasen |  |  |
| 35.02.05.01 | – Extensiv bewirtschaftet | 18 | 0,75 |
| 35.02.05.01a | – Brachgefallen | 16 | 0,6667 |
| 35.02.05.02 | – Intensiv bewirtschaftet | 12 | 0,5 |
| 35.02.06 | Artenarmes, intensiv genutztes Feuchtgrünland |  |  |
| 35.02.06.01 | Feuchtes, intensiv genutztes Dauergrünland | 10 | 0,4167 |
| 35.02.06.02 | Feuchtes Ansaatgrünland | 10 | 0,4167 |
| 35.02.06.03 | Brachgefallenes, artenarmes Feuchtgrünland | 12 | 0,5 |
| 35.03 | Salzgrünland des Binnenlandes | 22 | 0,9167 |
| 36. | HOCH-, ZWISCHEN- UND ÜBERGANGSMOORE |  |  |
| 36.01 | Hochmoore (weitgehend intakt) | 24 | 1 |
| 36.02 | Übergangsmoore und Zwischenmoore (weitgehend intakt) | 23 | 0,9583 |
| 36.03 | Moordegenerationsstadien |  |  |
| 36.03a | – Geschädigt, noch regenerierbar | 17 | 0,7083 |
| 36.03b | – Geschädigt, nicht regenerierbar | 12 | 0,5 |
| 36.04 | Torfabbaubereiche |  |  |
| 36.04.01 | Handtorfstich im Abbau | 9 | 0,375 |
| 36.04.02 | Abtorfungsflächen im Fräsverfahren | 3 | 0,125 |
| 36.04.03 | Bunkerde-Halde | 6 | 0,25 |
| 36.04.04 | Torfhalden | 5 | 0,2083 |
| 37. | GROßSEGGENRIEDE |  |  |
| 37.01 | Nährstoffarmes Großseggenried | 20 | 0,8333 |
| 37.02 | Nährstoffreiches Großseggenried | 16 | 0,6667 |
| 38. | RÖHRICHTE (ohne Brackwasserröhrichte) |  |  |
| 38.01 | Teichsimsenröhricht | 19 | 0,7917 |
| 38.02 | Schilfröhrichte |  |  |
| 38.02.01 | Schilf-Wasserröhricht | 19 | 0,7917 |
| 38.02.02 | Schilf-Landröhricht | 15 | 0,625 |
| 38.03 | Rohrkolbenröhricht | 16 | 0,6667 |
| 38.04 | Schneidenröhricht | 20 | 0,8333 |
| 38.05 | Wasserschwadenröhricht | 13 | 0,5417 |
| 38.06 | Rohrglanzgrasröhricht | 13 | 0,5417 |
| 38.07 | Sonstiges Röhricht | 16 | 0,6667 |
| 39. | WALD- UND UFERSÄUME, STAUDENFLUREN |  |  |
| 39.01 | Wald- und Gehölzsäume |  |  |
| 39.01.01 | Wald- und Gehölzsäume oligo- bis eutropher, trockener bis nasser Standorte | 16 | 0,6667 |
| 39.01.02 | Wald- und Gehölzsäume hypertropher, trockener bis nasser Standorte | 10 | 0,4167 |
| 39.02 | Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) | 10 | 0,4167 |
| 39.03 | Krautige und grasige Säume und Fluren der offenen Landschaft (ohne Ufersäume und Grünlandbrachen) |  |  |
| 39.03.01a | – Trocken-warmer Standorte mit wertgebenden Merkmalen z. B. struktur- oder artenreich | 17 | 0,7083 |
| 39.03.01b | – Frischer bis nasser Standorte mit wertgebenden Merkmalen z. B. struktur- oder artenreich | 16 | 0,6667 |
| 39.03.02 | Sonstige krautige und grasige Säume und Fluren der offenen Landschaft | 8 | 0,3333 |
| 39.04 | Krautige Ufersäume oder -fluren an Gewässern |  |  |
| 39.04a.01 | – Naturnahe Ausprägung | 17 | 0,7083 |
| 39.04a.02 | – Naturferne Ausprägung | 8 | 0,3333 |
| 39.05 | Neophyten-Staudenfluren | 7 | 0,2917 |
| 39.06 | Ruderalstandorte |  |  |
| 39.06.01 | Trocken-warme Ruderalstandorte auf Sand-, Kies- und Schotterböden | 16 | 0,6667 |
| 39.06.02 | Trocken-warme Ruderalstandorte auf bindigem Boden | 14 | 0,5833 |
| 39.06.03 | Frische bis nasse Ruderalstandorte | 12 | 0,5 |
| 39.07 | Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) | 10 | 0,4167 |
| 40. | ZWERGSTRAUCHHEIDEN |  |  |
| 40.01 | Felsbandheide | 19 | 0,7917 |
| 40.02 | Moor- oder Sumpfheiden |  |  |
| 40.02.01 | – Weitgehend intakt | 22 | 0,9167 |
| 40.02.02a | – Degeneriert | 16 | 0,6667 |
| 40.03 | Heiden auf sandigen oder Silikat-Böden (Calluna-Heiden) |  |  |
| 40.03.01 | – Weitgehend intakt | 19 | 0,7917 |
| 40.03.02a | – Degeneriert | 13 | 0,5417 |
| 40.04 | Lehmheide | 20 | 0,8333 |
| 40.05 | Bergheiden („Hochheiden“) | 18 | 0,75 |
| 41. | FELDGEHÖLZE, GEBÜSCHE, HECKEN UND GEHÖLZKULTUREN |  |  |
| 41.01 | Gebüsche mit überwiegend autochthonen Arten |  |  |
| 41.01.01 | Gebüsch nasser bis feuchter mineralischer Standorte außerhalb von Auen | 16 | 0,6667 |
| 41.01.02 | (Weiden-)Gebüsch in Auen | 16 | 0,6667 |
| 41.01.03 | Gebüsche nasser bis feuchter organischer Standorte |  |  |
| 41.01.03.01 | Moor-Gebüsch (z. B. mit Weiden, Gagel) | 16 | 0,6667 |
| 41.01.03.02 | Zwergbirken-Gebüsch | 18 | 0,75 |
| 41.01.04 | Gebüsche frischer Standorte |  |  |
| 41.01.04.01 | Wacholder- und Besenginster-Gebüsch | 16 | 0,6667 |
| 41.01.04.02 | Sonstiges Gebüsch frischer Standorte | 13 | 0,5417 |
| 41.01.05 | Gebüsch trocken-warmer Standorte |  |  |
| 41.01.05.01 | Buxus-Gebüsch | 20 | 0,8333 |
| 41.01.05.02 | Wacholder-Gebüsch | 19 | 0,7917 |
| 41.01.05.03 | Trockenes Zwerg- und Weichselkirschen-Gebüsch | 18 | 0,75 |
| 41.01.05.04a | Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) | 16 | 0,6667 |
| 41.01.06 | Gebüsch stickstoffreicher, ruderaler Standorte und stark verbuschte Grünlandbrache (Verbuschung > 50 %) | 12 | 0,5 |
| 41.02 | Feldgehölze mit überwiegend autochthonen Arten |  |  |
| 41.02.01 | Feldgehölz nasser bis feuchter Standorte |  |  |
| 41.02.01J | – Junge Ausprägung | 13 | 0,5417 |
| 41.02.01M | – Mittlere Ausprägung | 15 | 0,625 |
| 41.02.01A | – Alte Ausprägung | 18 | 0,75 |
| 41.02.02 | Feldgehölz frischer Standorte |  |  |
| 41.02.02J | – Junge Ausprägung | 13 | 0,5417 |
| 41.02.02M | – Mittlere Ausprägung | 14 | 0,5833 |
| 41.02.02A | – Alte Ausprägung | 17 | 0,7083 |
| 41.02.03 | Feldgehölz trocken-warmer Standorte |  |  |
| 41.02.03J | – Junge Ausprägung | 14 | 0,5833 |
| 41.02.03M | – Mittlere Ausprägung | 15 | 0,625 |
| 41.02.03A | – Alte Ausprägung | 18 | 0,75 |
| 41.03 | Hecken mit überwiegend autochthonen Arten |  |  |
| 41.03.01 | Wallhecke, Knick |  |  |
| 41.03.01J | – Junge Ausprägung (ohne Überhälter) | 12 | 0,5 |
| 41.03.01M | – Mit Überhältern mittlerer Ausprägung | 16 | 0,6667 |
| 41.03.01A | – Mit Überhältern alter Ausprägung | 19 | 0,7917 |
| 41.03.02 | Hecke auf Lesesteinriegel |  |  |
| 41.03.02J | – Junge Ausprägung (ohne Überhälter) | 12 | 0,5 |
| 41.03.02M | – Mit Überhältern mittlerer Ausprägung | 16 | 0,6667 |
| 41.03.02A | – Mit Überhältern alter Ausprägung | 19 | 0,7917 |
| 41.03.03 | Sonstige Hecken (insbesondere auf ebenerdigen Rainen oder Böschungen) |  |  |
| 41.03.03J | – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken | 12 | 0,5 |
| 41.03.03M | – Mit Überhältern mittlerer Ausprägung | 16 | 0,6667 |
| 41.03.03A | – Mit Überhältern alter Ausprägung | 19 | 0,7917 |
| 41.04 | Gehölzanpflanzungen und Hecken aus überwiegend nicht autochthonen Arten |  |  |
| 41.04J | – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken | 8 | 0,3333 |
| 41.04M | – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung | 11 | 0,4583 |
| 41.04A | – Alte Ausprägung/– Mit Überhältern alter Ausprägung | 14 | 0,5833 |
| 41.05 | Einzelbäume, Baumreihen und Baumgruppen |  |  |
| 41.05a | Einzelbäume, Baumreihen und Baumgruppen aus überwiegend autochtonen Arten |  |  |
| 41.05aJ | – Junge Ausprägung | 11 | 0,4583 |
| 41.05aM | – Mittlere Ausprägung | 15 | 0,625 |
| 41.05aA | – Alte Ausprägung | 18 | 0,75 |
| 41.05b | Einzelbäume, Baumreihen und Baumgruppen aus überwiegend nicht autochthonen Arten (mit Ausnahme von Kopfbäumen, Alleen, Obst- und Nussbäumen) |  |  |
| 41.05bJ | – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken | 8 | 0,3333 |
| 41.05bM | – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung | 11 | 0,4583 |
| 41.05bA | – Alte Ausprägung/– Mit Überhältern alter Ausprägung | 14 | 0,5833 |
| 41.05.02 | Kopfbaum/Kopfbaumreihe |  |  |
| 41.05.02J | – Junge Ausprägung | 12 | 0,5 |
| 41.05.02M | – Mittlere Ausprägung | 15 | 0,625 |
| 41.05.02A | – Alte Ausprägung | 18 | 0,75 |
| 41.05.04 | Allee |  |  |
| 41.05.04J | – Junge Ausprägung | 11 | 0,4583 |
| 41.05.04M | – Mittlere Ausprägung | 16 | 0,6667 |
| 41.05.04A | – Alte Ausprägung | 19 | 0,7917 |
| 41.05.05 | Obstbaumallee, -reihe oder einzelner Obst- bzw. Nussbaum |  |  |
| 41.05.05J | – Junge Ausprägung | 11 | 0,4583 |
| 41.05.05M | – Mittlere Ausprägung | 19 | 0,7917 |
| 41.05.05A | – Alte Ausprägung | 21 | 0,875 |
| 41.06 | Streuobstbestand [Komplex] |  |  |
| 41.06.01 | Streuobstbestand auf Grünland |  |  |
| 41.06.01.J | – Mit jungem Baumbestand | 12 | 0,5 |
| 41.06.01.MA | – Mit mittlerem bis altem Baumbestand | 19 | 0,7917 |
| 41.06.02 | Streuobstbestand auf Acker |  |  |
| 41.06.02J | – Mit jungem Baumbestand | 12 | 0,5 |
| 41.06.02MA | – Mit mittlerem bis altem Baumbestand | 18 | 0,75 |
| 41.07 | Gehölzplantagen und Hopfenkulturen | 6 | 0,25 |
| 41.08 | Rebkulturen und Rebbrachen |  |  |
| 41.08.01 | Rebkulturen in Steillage | 17 | 0,7083 |
| 41.08.02 | Rebkulturen in ebener bis schwach geneigter Lage | 9 | 0,375 |
| 41.08.03 | Rebbrachen in Steillage | 14 | 0,5833 |
| 41.08.04 | Rebbrachen in ebener bis schwach geneigter Lage | 10 | 0,4167 |
| 42. | WALDMÄNTEL UND VORWÄLDER, SPEZIELLE WALDNUTZUNGSFORMEN |  |  |
| 42.01 | Waldmäntel | 17 | 0,7083 |
| 42.02 | Rubus-Gestrüppe und -Vormäntel | 12 | 0,5 |
| 42.03 | Vorwälder |  |  |
| 42.03.01 | Vorwald nasser bis feuchter Standorte | 14 | 0,5833 |
| 42.03.02 | Vorwald frischer Standorte | 13 | 0,5417 |
| 42.03.03 | Vorwald trocken-warmer Standorte | 13 | 0,5417 |
| 42.04 | Hudewald [Komplex] |  |  |
| 42.04.01 | – Hudewald mit traditioneller Weidenutzung | 22 | 0,9167 |
| 42.04.02 | – Hudewald, aufgelassen | 20 | 0,8333 |
| 42.05 | Niederwald [Komplex] |  |  |
| 42.05.01 | – Mit traditioneller Nutzung | 19 | 0,7917 |
| 42.05.02 | – Aufgelassen bzw. durchwachsend | 18 | 0,75 |
| 42.06a | Kurzumtriebsplantagen mit heimischen oder nicht heimischen Baumarten | 6 | 0,25 |
| 42.07 | Mittelwald [Komplex] |  |  |
| 42.07.01 | – Mit traditioneller Nutzung | 21 | 0,875 |
| 42.07.02 | – Aufgelassen bzw. durchwachsend | 17 | 0,7083 |
| 43. | LAUB(MISCH)WÄLDER UND -FORSTE (Laubbaumanteil > 50 %) |  |  |
| 43.01 | Birken-Moorwälder |  |  |
| 43.01.01 | Birken-Moorwälder mit intaktem Wasserhaushalt |  |  |
| 43.01.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.01.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.01.01A | – Alte Ausprägung | 24 | 1 |
| 43.01.02 | Degradierter Birken-Moorwald |  |  |
| 43.01.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.01.02M | – Mittlere Ausprägung | 14 | 0,5833 |
| 43.01.02A | – Alte Ausprägung | 17 | 0,7083 |
| 43.02 | Bruchwälder |  |  |
| 43.02.01.01 | Birken- und Birken-Erlenbruchwälder nährstoffärmerer Standorte mit intaktem Wasserhaushalt |  |  |
| 43.02.01.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.02.01.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.02.01.01A | – Alte Ausprägung | 24 | 1 |
| 43.02.01.02 | Degradierter Birken- und Birken-Erlenbruchwälder nährstoffärmerer Standorte |  |  |
| 43.02.01.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.02.01.02M | – Mittlere Ausprägung | 15 | 0,625 |
| 43.02.01.02A | – Alte Ausprägung | 18 | 0,75 |
| 43.02.02.01 | Erlenbruchwälder nährstoffreicherer Standorte mit intaktem Wasserhaushalt |  |  |
| 43.02.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.02.02.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.02.02.01A | – Alte Ausprägung | 23 | 0,9583 |
| 43.02.02.02 | Degradierter Erlenbruchwald |  |  |
| 43.02.02.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.02.02.02M | – Mittlere Ausprägung | 14 | 0,5833 |
| 43.02.02.02A | – Alte Ausprägung | 17 | 0,7083 |
| 43.03 | Sumpfwälder (auf mineralogenen Böden) |  |  |
| 43.03.01 | Intakter Sumpfwald |  |  |
| 43.03.01J | – Junge Ausprägung | 15 | 0,625 |
| 43.03.01M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.03.01A | – Alte Ausprägung | 21 | 0,875 |
| 43.03.02 | Degradierter Sumpfwald |  |  |
| 43.03.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.03.02M | – Mittlere Ausprägung | 13 | 0,5417 |
| 43.03.02A | – Alte Ausprägung | 15 | 0,625 |
| 43.04 | Auenwälder |  |  |
| 43.04.01 | Fließgewässerbegleitende Erlen- und Eschenwälder |  |  |
| 43.04.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.04.01M | – Mittlere Ausprägung | 17 | 0,7083 |
| 43.04.01A | – Alte Ausprägung | 20 | 0,8333 |
| 43.04.02.01 | Weichholzauenwälder mit natürlicher oder naturnaher Überflutungsdynamik |  |  |
| 43.04.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.04.02.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.04.02.01A | – Alte Ausprägung | 23 | 0,9583 |
| 43.04.02.02 | Weichholzauenwälder ohne oder mit gestörter Überflutungsdynamik |  |  |
| 43.04.02.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.04.02.02M | – Mittlere Ausprägung | 14 | 0,5833 |
| 43.04.02.02A | – Alte Ausprägung | 17 | 0,7083 |
| 43.04.03.01 | Hartholzauenwälder mit natürlicher oder naturnaher Überflutungsdynamik |  |  |
| 43.04.03.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.04.03.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.04.03.01A | – Alte Ausprägung | 22 | 0,9167 |
| 43.04.03.02 | Hartholzauenwälder ohne oder mit gestörter Überflutungsdynamik |  |  |
| 43.04.03.02J | – Junge Ausprägung | 11 | 0,4583 |
| 43.04.03.02M | – Mittlere Ausprägung | 15 | 0,625 |
| 43.04.03.02A | – Alte Ausprägung | 18 | 0,75 |
| 43.05 | Tideauenwälder |  |  |
| 43.05.01 | Weichholz-Tideauenwälder |  |  |
| 43.05.01J | – Junge Ausprägung | 14 | 0,5833 |
| 43.05.01M | – Mittlere Ausprägung | 21 | 0,875 |
| 43.05.01A | – Alte Ausprägung | 24 | 1 |
| 43.05.02 | Hartholz-Tideauenwälder |  |  |
| 43.05.02J | – Junge Ausprägung | 14 | 0,5833 |
| 43.05.02M | – Mittlere Ausprägung | 19 | 0,7917 |
| 43.05.02A | – Alte Ausprägung | 22 | 0,9167 |
| 43.06 | Schlucht-, Blockhalden- und Hangschuttwälder |  |  |
| 43.06J | – Junge Ausprägung | 15 | 0,625 |
| 43.06M | – Mittlere Ausprägung | 17 | 0,7083 |
| 43.06A | – Alte Ausprägung | 20 | 0,8333 |
| 43.07 | Laub- und Mischwälder feuchter bis frischer Standorte |  |  |
| 43.07.01 | Eschen- und Eschen-Bergahornwald feuchter Standorte |  |  |
| 43.07.01J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.01M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.07.01A | – Alte Ausprägung | 21 | 0,875 |
| 43.07.02 | Eichen-Hainbuchenwald staunasser bis frischer Standorte |  |  |
| 43.07.02J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.02M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.07.02A | – Alte Ausprägung | 23 | 0,9583 |
| 43.07.03 | Eichenwald feuchter bis frischer Standorte |  |  |
| 43.07.03J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.03M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.07.03A | – Alte Ausprägung | 23 | 0,9583 |
| 43.07.04 | Buchen(misch)wälder frischer, basenarmer Standorte |  |  |
| 43.07.04J | – Junge Ausprägung | 14 | 0,5833 |
| 43.07.04M | – Mittlere Ausprägung | 17 | 0,7083 |
| 43.07.04A | – Alte Ausprägung | 20 | 0,8333 |
| 43.07.05 | Buchen(misch)wälder frischer, basenreicher Standorte |  |  |
| 43.07.05J | – Junge Ausprägung | 14 | 0,5833 |
| 43.07.05M | – Mittlere Ausprägung | 16 | 0,6667 |
| 43.07.05A | – Alte Ausprägung | 18 | 0,75 |
| 43.07.06 | Montane Buchen-Tannen-/Fichtenwälder (Buchenanteil > 50 %) |  |  |
| 43.07.06J | – Junge Ausprägung | 15 | 0,625 |
| 43.07.06M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.07.06A | – Alte Ausprägung | 21 | 0,875 |
| 43.08 | Laub(misch)wälder trockener bzw. trocken-warmer Standorte |  |  |
| 43.08.01 | Trockene Eichen-Hainbuchenwälder |  |  |
| 43.08.01J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.08.01A | – Alte Ausprägung | 23 | 0,9583 |
| 43.08.02 | Seggen-Buchenwald (Orchideen-Buchenwald) |  |  |
| 43.08.02J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.02M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.08.02A | – Alte Ausprägung | 21 | 0,875 |
| 43.08.03 | Blaugras-Buchenwald |  |  |
| 43.08.03J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.03M | – Mittlere Ausprägung | 20 | 0,8333 |
| 43.08.03A | – Alte Ausprägung | 23 | 0,9583 |
| 43.08.04 | Buchenbuschwald (auf Ostseedünen) |  |  |
| 43.08.04J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.04M | – Mittlere Ausprägung | 21 | 0,875 |
| 43.08.04A | – Alte Ausprägung | 24 | 1 |
| 43.08.05 | Eichen-Trockenwälder |  |  |
| 43.08.05J | – Junge Ausprägung | 15 | 0,625 |
| 43.08.05M | – Mittlere Ausprägung | 18 | 0,75 |
| 43.08.05A | – Alte Ausprägung | 21 | 0,875 |
| 43.09 | Laub(misch)holzforste einheimischer Baumarten |  |  |
| 43.09J | – Junge Ausprägung | 11 | 0,4583 |
| 43.09M | – Mittlere Ausprägung | 13 | 0,5417 |
| 43.09A | – Alte Ausprägung | 16 | 0,6667 |
| 43.10 | Laub(misch)holzforste eingeführter Baumarten |  |  |
| 43.10J | – Junge Ausprägung | 9 | 0,375 |
| 43.10M | – Mittlere Ausprägung | 12 | 0,5 |
| 43.10A | – Alte Ausprägung | 14 | 0,5833 |
| 44. | NADEL(MISCH)WÄLDER UND -FORSTE |  |  |
| 44.01 | Moorwälder (Nadelwälder) |  |  |
| 44.01.01 | Fichten-Moorwälder |  |  |
| 44.01.01J | – Junge Ausprägung | 14 | 0,5833 |
| 44.01.01M | – Mittlere Ausprägung | 20 | 0,8333 |
| 44.01.01A | – Alte Ausprägung | 23 | 0,9583 |
| 44.01.02 | Waldkiefern-Moorwälder |  |  |
| 44.01.02J | – Junge Ausprägung | 14 | 0,5833 |
| 44.01.02M | – Mittlere Ausprägung | 20 | 0,8333 |
| 44.01.02A | – Alte Ausprägung | 23 | 0,9583 |
| 44.01.03 | Spirken-Moorwälder |  |  |
| 44.01.03J | – Junge Ausprägung | 14 | 0,5833 |
| 44.01.03M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.01.03A | – Alte Ausprägung | 21 | 0,875 |
| 44.01.04 | Latschen-Moorwälder |  |  |
| 44.01.04J | – Junge Ausprägung | 14 | 0,5833 |
| 44.01.04M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.01.04A | – Alte Ausprägung | 21 | 0,875 |
| 44.02 | Natürliche bzw. naturnahe, trockene bis wechselfeuchte Kiefernwälder |  |  |
| 44.02.01 | Trockene Fels-Kiefernwälder |  |  |
| 44.02.01J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.01M | – Mittlere Ausprägung | 17 | 0,7083 |
| 44.02.01A | – Alte Ausprägung | 21 | 0,875 |
| 44.02.02 | Kalk-Kiefernwald auf Schotterflächen und Schwemmkegeln |  |  |
| 44.02.02J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.02M | – Mittlere Ausprägung | 17 | 0,7083 |
| 44.02.02A | – Alte Ausprägung | 21 | 0,875 |
| 44.02.03 | Trockene Sandkiefernwälder |  |  |
| 44.02.03J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.03M | – Mittlere Ausprägung | 19 | 0,7917 |
| 44.02.03A | – Alte Ausprägung | 22 | 0,9167 |
| 44.02.04 | Sonstiger (wechsel)feuchter Kiefern- bzw. Birken-/Kiefernwald (z. B. auf Mergel) |  |  |
| 44.02.04J | – Junge Ausprägung | 14 | 0,5833 |
| 44.02.04M | – Mittlere Ausprägung | 17 | 0,7083 |
| 44.02.04A | – Alte Ausprägung | 20 | 0,8333 |
| 44.03 | Fichten-/Tannen(misch)wälder und Fichten(misch)wälder |  |  |
| 44.03.01 | Montaner Fichten-Blockschuttwald |  |  |
| 44.03.01J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.01M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.01A | – Alte Ausprägung | 21 | 0,875 |
| 44.03.02 | Montane bis hochmontane Fichtenwälder |  |  |
| 44.03.02J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.02J | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.02A | – Alte Ausprägung | 21 | 0,875 |
| 44.03.03 | Montane Tannen-Fichtenwälder |  |  |
| 44.03.03J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.03M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.03A | – Alte Ausprägung | 21 | 0,875 |
| 44.03.04 | Montane Tannen-/Fichten-Buchenwälder (Nadelbaumanteil > 50 %) |  |  |
| 44.03.04J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.04M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.04A | – Alte Ausprägung | 21 | 0,875 |
| 44.03.05 | Montane Tannenwälder |  |  |
| 44.03.05J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.05M | – Mittlere Ausprägung | 18 | 0,75 |
| 44.03.05A | – Alte Ausprägung | 21 | 0,875 |
| 44.03.06 | Autochthone Fichten-Tannenwälder der planaren und collinen Stufe |  |  |
| 44.03.06J | – Junge Ausprägung | 15 | 0,625 |
| 44.03.06M | – Mittlere Ausprägung | 19 | 0,7917 |
| 44.03.06A | – Alte Ausprägung | 22 | 0,9167 |
| 44.04 | Nadel(misch)forste einheimischer Baumarten |  |  |
| 44.04J | – Junge Ausprägung | 9 | 0,375 |
| 44.04M | – Mittlere Ausprägung | 11 | 0,4583 |
| 44.04A | – Alte Ausprägung | 14 | 0,5833 |
| 44.05 | Nadel(misch)forste eingeführter Baumarten |  |  |
| 44.05J | – Junge Ausprägung | 6 | 0,25 |
| 44.05M | – Mittlere Ausprägung | 10 | 0,4167 |
| 44.05A | – Alte Ausprägung | 12 | 0,5 |
|  | BIOTOPTYPEN DES BESIEDELTEN BEREICHS UND VERKEHRSANLAGEN |  |  |
| 51. | FREIFLÄCHEN DES BESIEDELTEN BEREICHS |  |  |
| 51.01 | Kleine vegetationsfreie Freiflächen | 5 | 0,2083 |
| 51.02 | Kleine unbefestigte Freiflächen mit Spontanvegetation | 11 | 0,4583 |
| 51.04a | Brachflächen z. B. ehemalige Baukomplexe, Industrie- und Verkehrsanlagen |  |  |
| 51.04a.01 | – Mit wesentlichen Anteilen struktur-/artenreicher Ausprägung | 12 | 0,5 |
| 51.04a.02 | – Ohne wesentliche Anteile struktur-/artenreicher Ausprägung | 7 | 0,2917 |
| 51.06a | Parkanlagen |  |  |
| 51.06a.01 | Historische Garten- und Parkanlage | 19 | 0,7917 |
| 51.06a.02.01 | Extensiv gepflegte Parkanlage mit altem Baumbestand | 16 | 0,6667 |
| 51.06a.02.02 | Extensiv gepflegte Parkanlage ohne alten Baumbestand | 13 | 0,5417 |
| 51.06a.03 | Intensiv gepflegte Parkanlage mit altem Baumbestand | 13 | 0,5417 |
| 51.06a.04 | Intensiv gepflegte Parkanlage ohne alten Baumbestand | 10 | 0,4167 |
| 51.06a.05 | Parkwald | 14 | 0,5833 |
| 51.06a.06 | Botanischer Garten (differenzierte Objektbewertung) | 13 | 0,5417 |
| 51.07a | Sonstige Grünanlage |  |  |
| 51.07a.01 | Sonstige Grünanlage mit altem Baumbestand | 13 | 0,5417 |
| 51.07a.02 | Sonstige Grünanlage ohne alten Baumbestand | 9 | 0,375 |
| 51.08a | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen |  |  |
| 51.08a.01 | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich | 11 | 0,4583 |
| 51.08a.02 | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturarm | 7 | 0,2917 |
| 51.09a | Friedhöfe |  |  |
| 51.09a.01 | Friedhof mit altem Baumbestand | 14 | 0,5833 |
| 51.09a.02 | Friedhof ohne alten Baumbestand | 9 | 0,375 |
| 51.10a | Zoo/Tierpark/Tiergehege (differenzierte Objektbewertung) | 11 | 0,4583 |
| 51.11a | Sport-/Spiel-/Erholungsanlage mit geringem Versiegelungsgrad |  |  |
| 51.11a.01 | Sportrasenplatz | 7 | 0,2917 |
| 51.11a.02 | Freibad | 7 | 0,2917 |
| 51.11a.03 | Golfplatz | 9 | 0,375 |
| 51.11a.04 | Campingplatz | 7 | 0,2917 |
| 51.11a.05 | Sonstige Sport-, Spiel- und Freizeitanlage | 7 | 0,2917 |
| 52. | VERKEHRSANLAGEN UND PLÄTZE |  |  |
| 52.01 | Straßen und Verkehrswege (einschließlich der Land- und Forstwirtschaft) |  |  |
| 52.01.01a | Versiegelter oder sonstiger gepflasterter Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) | 0 | 0 |
| 52.01.03 | Teilbefestigter Verkehrsweg (z. B. Rasengitter, Spurplatten) | 2 | 0,0833 |
| 52.01.04a | Unbefestigte Straße/Feld- und Forstweg bzw. Verkehrsweg mit wassergebundener Decke | 3 | 0,125 |
| 52.01.07a | Verkehrsweg mit Natursteinpflaster | 6 | 0,25 |
| 52.01.08a | Funktionsgrün an Verkehrswegen |  |  |
| 52.01.08a.01 | Bankette, Mittelstreifen | 3 | 0,125 |
| 52.01.08a.02 | Funktionsgrün mit artenarmer Krautschicht oder mit Gehölzbestand junger Ausprägung | 7 | 0,2917 |
| 52.01.08n.03 | Funktionsgrün mit artenreicher Krautschicht oder mit Gehölzbestand mittlerer bis alter Ausprägung | 11 | 0,4583 |
| 52.02 | Rad- und Fußwege bzw. Pfade |  |  |
| 52.02.01a | Versiegelter oder sonstiger gepflasterter Weg | 0 | 0 |
| 52.02.03 | Teilbefestigter Weg (z. B. Rasengitter, Spurplatten) | 3 | 0,125 |
| 52.02.04a | Geschotterter Weg oder Weg mit wassergebundener Decke | 4 | 0,1667 |
| 52.02.06 | Unbefestigter Weg | 10 | 0,4167 |
| 52.02.07 | Hohlweg [Komplex] | 18 | 0,75 |
| 52.02.08a | Weg mit Natursteinpflaster | 7 | 0,2917 |
| 52.03 | Plätze, befestigte Freiflächen |  |  |
| 52.03.01 | Versiegelter Platz oder sonstiger gepflasterter Platz | 0 | 0 |
| 52.03.02 | Teilbefestigter Platz (z. B. Rasengitter) | 3 | 0,125 |
| 52.03.03a | Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) | 4 | 0,1667 |
| 52.03.05a | Platz mit Natursteinpflaster | 7 | 0,2917 |
| 52.04 | Übrige Verkehrsanlagen in Betrieb |  |  |
| 52.04.01 | Gleiskörper | 1 | 0,0417 |
| 52.04.02 | Hafenanlage an Land, Kai | 1 | 0,0417 |
| 52.04.04a | Hafenbecken und Marinas | 6 | 0,25 |
| 52.04.05a | Wasserbauliche Anlagen z. B. Schleusen, Wehre, Leitwerke | 2 | 0,0833 |
| 52.04.06a | Sonstige Verkehrsanlagen | 0 | 0 |
| 53 | BAUWERKE MIT ZUGEORDNETER TYPISCHER FREIRAUMSTRUKTUR |  |  |
| 53.01 | Gebäude |  |  |
| 53.01.01a | Historischer Gebäudekomplex, z. B. Kirche, Kloster, Burg, Schloss | 13 | 0,5417 |
| 53.01.03 | Einzel- und Reihenhausbebauung inkl. typischen Freiräumen |  |  |
| 53.01.03a | – Altes Villengebiet mit altem Baumbestand | 13 | 0,5417 |
| 53.01.03b | – Lockeres Einzelhausgebiet | 5 | 0,2083 |
| 53.01.03c | – Verdichtetes Einzel- und Reihenhausgebiet | 4 | 0,1667 |
| 53.01.05 | Hochhaus- und Großformbebauung inkl. typischen Freiräumen |  |  |
| 53.01.05a | – Wohnnutzung in Hochhaus- und Großformbauten | 4 | 0,1667 |
| 53.01.05b | – Öffentliche oder gewerbliche Hochhaus- und Großformbauten | 4 | 0,1667 |
| 53.01.07a | Sonstige Einzelgebäude z. B. Scheunen, Stallungen, Speichergebäude |  |  |
| 53.01.07a.01 | – Alt bzw. traditionelle Bauweise (genutzt) oder verfallen (ungenutzt) | 11 | 0,4583 |
| 53.01.07a.02 | – Moderne Bauweise | 2 | 0,0833 |
| 53.01.14a | Industrie- und Gewerbefläche inkl. typischen Freiräumen | 2 | 0,0833 |
| 53.01.15a | Kerngebiet inkl. typischen Freiräumen |  |  |
| 53.01.15a.01 | – Historische Altstadt | 12 | 0,5 |
| 53.01.15a.02 | – Moderne Innenstadt | 3 | 0,125 |
| 53.01.16a | Block- und Zeilenbebauung inkl. typischen Freiräumen |  |  |
| 53.01.16a.01 | – Historische Blockbebauung | 9 | 0,375 |
| 53.01.16a.02 | – Sonstige Blockbebauung | 4 | 0,1667 |
| 53.01.16a.03 | – Zeilenbebauung | 5 | 0,2083 |
| 53.01.17a | Dorfgebiet |  |  |
| 53.01.17a.01 | – Historisches Dorfgebiet z. B. Dorfkern, Dorfanger, Dorfplatz | 13 | 0,5417 |
| 53.01.17a.02 | – Sonstiges Dorfgebiet inkl. Neubaugebiete | 4 | 0,1667 |
| 53.01.18a | Einzelgebäude im Außenbereich |  |  |
| 53.01.18a.01 | – Historische Einzelgebäude/-gehöfte | 10 | 0,4167 |
| 53.01.18a.02 | – Sonstige Einzelgebäude/-gehöfte | 2 | 0,0833 |
| 53.01.19a | Tierproduktionsanlage und Gewächshäuser | 0 | 0 |
| 53.01.20a | Ver- und Entsorgungsanlage, z. B. Kläranlage, Wasserwerk, Staudamm | 2 | 0,0833 |
| 53.02 | Mauern und Steinriegel |  |  |
| 53.02.01 | Ziegelsteinmauern |  |  |
| 53.02.01.01 | – Alt bzw. traditionelle Bauweise | 10 | 0,4167 |
| 53.02.01.02 | – Moderne Bauweise | 4 | 0,1667 |
| 53.02.02 | Betonmauer | 0 | 0 |
| 53.02.03a | Unverfugte Natursteinmauer bzw. Trockenmauer | 17 | 0,7083 |
| 53.02.04a | Verfugte Natursteinmauer (auch von Ruinen) | 9 | 0,375 |
| 53.02.05a | Steinriegel | 17 | 0,7083 |
| 53.02.06a | Gabionen | 2 | 0,0833 |
| 54. | DEPONIEN UND RIESELFELDER |  |  |
| 54.01 | Feststoffdeponien (z. B. Hausmüll, Bauschuttdeponie) |  |  |
| 54.01a | – In Betrieb | 0 | 0 |
| 54.01b | – Begrünte Bereiche | 2 | 0,0833 |
| 54.02 | Deponien flüssiger Stoffe (z. B. Schlammdeponie) | 0 | 0 |
| 54.03 | Rieselfelder [Komplex] | 8 | 0,3333 |
| 54.04 | Kanalisation | 0 | 0 |
|  | BIOTOPTYPEN MIT SCHWERPUNKT IN DEN ALPEN |  |  |
| 60. | GEWÄSSER DER SUBALPINEN BIS ALPINEN STUFE |  |  |
| 60.01 | Quellen der subalpinen bis alpinen Stufe |  |  |
| 60.01.01 | Sicker- und Sumpfquelle der subalpinen bis alpinen Stufe (Helokrene) | 18 | 0,75 |
| 60.01.02 | Grundquelle der subalpinen bis alpinen Stufe (Limnokrene) | 17 | 0,7083 |
| 60.01.03 | Sturzquelle der subalpinen bis alpinen Stufe (Rheokrene) | 19 | 0,7917 |
| 60.02 | Fließgewässer der subalpinen bis alpinen Stufe |  |  |
| 60.02.01 | Gletscherbach | 22 | 0,9167 |
| 60.02.02 | Fließgewässeroberlauf (Rhitral) der subalpinen bis alpinen Stufe | 20 | 0,8333 |
| 60.03 | Stillgewässer der subalpinen bis alpinen Stufe |  |  |
| 60.03.01 | See der subalpinen bis alpinen Stufe | 17 | 0,7083 |
| 60.03.02 | Weiher der subalpinen bis alpinen Stufe | 17 | 0,7083 |
| 60.03.03 | Tümpel der subalpinen bis alpinen Stufe | 17 | 0,7083 |
| 61. | FIRN, PERMANENTE SCHNEEFELDER UND GLETSCHER |  |  |
| 61.01 | Firn und permanentes Schneefeld | 16 | 0,6667 |
| 61.02 | Gletscher | 21 | 0,875 |
| 62. | FELSEN DER SUBALPINEN BIS NIVALEN STUFE |  |  |
| 62.01 | Felswände der subalpinen bis nivalen Stufe | 14 | 0,5833 |
| 62.02 | Felsblöcke der subalpinen bis nivalen Stufe | 13 | 0,5417 |
| 63. | STEINSCHUTTHALDEN UND SCHOTTERFLÄCHEN DER SUBALPINEN BIS ALPINEN STUFE |  |  |
| 63.01 | Schotterfläche an Gewässern der subalpinen bis alpinen Stufe | 16 | 0,6667 |
| 63.02 | Kalkschutthalde der subalpinen bis alpinen Stufe | 12 | 0,5 |
| 63.03 | Mergelschutthalde der subalpinen bis alpinen Stufe | 12 | 0,5 |
| 63.04 | Silikatschutthalde der subalpinen bis alpinen Stufe | 12 | 0,5 |
| 64. | SCHNEEBÖDEN, SCHNEETÄLCHEN |  |  |
| 64.01 | Kalkschneeboden | 17 | 0,7083 |
| 64.02 | Schwemmboden der subalpinen bis alpinen Stufe | 19 | 0,7917 |
| 64.03 | Silikatschneeboden | 18 | 0,75 |
| 65. | MOORE DER SUBALPINEN BIS ALPINEN STUFE |  |  |
| 65.01 | Hoch- und Übergangsmoor der subalpinen bis alpinen Stufe | 20 | 0,8333 |
| 65.02 | Flachmoor oder Sumpf der subalpinen bis alpinen Stufe | 20 | 0,8333 |
| 66. | GEBIRGSRASEN (SUBALPINE BIS ALPINE STUFE) |  |  |
| 66.01 | Nacktriedrasen | 19 | 0,7917 |
| 66.02 | Polsterseggenrasen | 17 | 0,7083 |
| 66.03 | Borstgrasrasen der subalpinen bis alpinen Stufe | 18 | 0,75 |
| 66.04 | Blaugrashalde bzw. -rasen | 15 | 0,625 |
| 66.05 | Rostseggenrasen | 15 | 0,625 |
| 66.06 | Alpenfettweide | 14 | 0,5833 |
| 66.07 | Goldhaferwiese der Kalkalpen | 21 | 0,875 |
| 66.08 | Subalpiner Trittrasen | 13 | 0,5417 |
| 66.09 | Krummseggenrasen | 19 | 0,7917 |
| 67. | STAUDEN- UND LÄGERFLUREN DER HOCHMONTANEN BIS ALPINEN STUFE |  |  |
| 67.01 | Hochstauden- und Hochgrasflur der hochmontanen bis alpinen Stufe | 16 | 0,6667 |
| 67.02 | Lägerfluren der subalpinen bis alpinen Stufe | 9 | 0,375 |
| 68. | ZWERGSTRAUCHHEIDEN DER SUBALPINEN BIS ALPINEN STUFE |  |  |
| 68.01 | Alpine „Windheide“ (z. B. mit Gamsheide) | 19 | 0,7917 |
| 68.02 | Krähenbeer-Rauschbeerheide und Zwergwacholdergebüsche | 21 | 0,875 |
| 69. | GEBÜSCHE DER HOCHMONTANEN BIS SUBALPINEN STUFE |  |  |
| 69.01 | Auenweidengebüsche der hochmontanen bis subalpinen Stufe | 20 | 0,8333 |
| 69.02 | Grünerlengebüsche | 15 | 0,625 |
| 69.03 | Schluchtweidengebüsch | 16 | 0,6667 |
| 69.04 | Latschengebüsch | 15 | 0,625 |
| 69.05 | Alpenrosengebüsch | 17 | 0,7083 |
| 69.06 | Fichten-Ebereschengebüsch | 14 | 0,5833 |
| 69.07 | Knieweidengebüsch | 16 | 0,6667 |
| 70. | SUBALPINE WÄLDER |  |  |
| 70.01 | Subalpiner (hochmontaner) Bergahorn-Buchenwald |  |  |
| 70.01J | – Junge Ausprägung | 16 | 0,6667 |
| 70.01M | – Mittlere Ausprägung | 19 | 0,7917 |
| 70.01A | – Alte Ausprägung | 22 | 0,9167 |
| 70.02 | Subalpiner Fichtenwald |  |  |
| 70.02J | – Junge Ausprägung | 15 | 0,625 |
| 70.02M | – Mittlere Ausprägung | 18 | 0,75 |
| 70.02A | – Alte Ausprägung | 21 | 0,875 |
| 70.03 | Subalpiner Lärchen-Arvenwald |  |  |
| 70.03J | – Junge Ausprägung | 15 | 0,625 |
| 70.03M | – Mittlere Ausprägung | 18 | 0,75 |
| 70.03A | – Alte Ausprägung | 21 | 0,875 |
| 70.04 | Subalpiner Lärchenwald |  |  |
| 70.04J | – Junge Ausprägung | 15 | 0,625 |
| 70.04M | – Mittlere Ausprägung | 18 | 0,75 |
| 70.04A | – Alte Ausprägung | 21 | 0,875 |

### 2.19 Métrique statutaire anglaise, onglets utilisés

Reproduction des colonnes utilisées des onglets G-1, G-4 et G-5 du tableur statutaire 1.0.4 (Defra et Natural England, Open Government Licence v3.0). « Not Possible » signifie que la création ou l'amélioration n'est pas admise par la métrique pour cette classe d'état.

#### Onglet G-1, habitats, distinctivité et difficultés

| Habitat | Distinctivité | Score | Difficulté de création | Multiplicateur | Difficulté d'amélioration | Multiplicateur |
|---|---|---|---|---|---|---|
| Cropland - Arable field margins cultivated annually | Medium | 4 | Low | 1 | Low | 1 |
| Cropland - Arable field margins game bird mix | Medium | 4 | Low | 1 | Low | 1 |
| Cropland - Arable field margins pollen and nectar | Medium | 4 | Low | 1 | Low | 1 |
| Cropland - Arable field margins tussocky | Medium | 4 | Low | 1 | Low | 1 |
| Cropland - Cereal crops | Low | 2 | Low | 1 | Low | 1 |
| Cropland - Winter stubble | Low | 2 | Low | 1 | Low | 1 |
| Cropland - Horticulture | Low | 2 | Low | 1 | Low | 1 |
| Cropland - Intensive orchards | Low | 2 | Low | 1 | Low | 1 |
| Cropland - Non-cereal crops | Low | 2 | Low | 1 | Low | 1 |
| Cropland - Temporary grass and clover leys | Low | 2 | Low | 1 | Low | 1 |
| Grassland - Traditional orchards | High | 6 | Low | 1 | Medium | 0.67 |
| Grassland - Bracken | Low | 2 | Low | 1 | Low | 1 |
| Grassland - Floodplain wetland mosaic and CFGM | High | 6 | High | 0.33 | Medium | 0.67 |
| Grassland - Lowland calcareous grassland | High | 6 | High | 0.33 | High | 0.33 |
| Grassland - Lowland dry acid grassland | V.High | 8 | High | 0.33 | High | 0.33 |
| Grassland - Lowland meadows | V.High | 8 | High | 0.33 | Medium | 0.67 |
| Grassland - Modified grassland | Low | 2 | Low | 1 | Low | 1 |
| Grassland - Other lowland acid grassland | Medium | 4 | Low | 1 | Low | 1 |
| Grassland - Other neutral grassland | Medium | 4 | Low | 1 | Low | 1 |
| Grassland - Tall herb communities (H6430) | High | 6 | High | 0.33 | High | 0.33 |
| Grassland - Upland acid grassland | Medium | 4 | Low | 1 | Low | 1 |
| Grassland - Upland calcareous grassland | High | 6 | High | 0.33 | High | 0.33 |
| Grassland - Upland hay meadows | V.High | 8 | High | 0.33 | Medium | 0.67 |
| Heathland and shrub - Blackthorn scrub | Medium | 4 | Low | 1 | Low | 1 |
| Heathland and shrub - Bramble scrub | Medium | 4 | Low | 1 | Low | 1 |
| Heathland and shrub - Gorse scrub | Medium | 4 | Low | 1 | Low | 1 |
| Heathland and shrub - Hawthorn scrub | Medium | 4 | Low | 1 | Low | 1 |
| Heathland and shrub - Hazel scrub | Medium | 4 | Medium | 0.67 | Low | 1 |
| Heathland and shrub - Lowland heathland | High | 6 | High | 0.33 | Medium | 0.67 |
| Heathland and shrub - Mixed scrub | Medium | 4 | Low | 1 | Low | 1 |
| Heathland and shrub - Mountain heaths and willow scrub | V.High | 8 | High | 0.33 | High | 0.33 |
| Heathland and shrub - Rhododendron scrub | Low | 2 | Low | 1 | Low | 1 |
| Heathland and shrub - Dunes with sea buckthorn (H2160) | High | 6 | Medium | 0.67 | Low | 1 |
| Heathland and shrub - Other sea buckthorn scrub | Low | 2 | Low | 1 | Low | 1 |
| Heathland and shrub - Willow scrub | Medium | 4 | Medium | 0.67 | Low | 1 |
| Heathland and shrub - Upland heathland | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Lakes - Aquifer fed naturally fluctuating water bodies | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Lakes - Ornamental lake or pond | Low | 2 | Low | 1 | High | 0.33 |
| Lakes - High alkalinity lakes | High | 6 | High | 0.33 | High | 0.33 |
| Lakes - Low alkalinity lakes | High | 6 | High | 0.33 | Medium | 0.67 |
| Lakes - Marl lakes | High | 6 | High | 0.33 | High | 0.33 |
| Lakes - Moderate alkalinity lakes | High | 6 | High | 0.33 | High | 0.33 |
| Lakes - Peat lakes | High | 6 | High | 0.33 | High | 0.33 |
| Lakes - Ponds (priority habitat) | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Lakes - Ponds (non-priority habitat) | Medium | 4 | Low | 1 | Medium | 0.67 |
| Lakes - Reservoirs | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Lakes - Temporary lakes ponds and pools (H3170) | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Sparsely vegetated land - Calaminarian grasslands | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Sparsely vegetated land - Coastal sand dunes | High | 6 | Very High | 0.1 | Medium | 0.67 |
| Sparsely vegetated land - Coastal vegetated shingle | High | 6 | Very High | 0.1 | Medium | 0.67 |
| Sparsely vegetated land - Ruderal/Ephemeral | Low | 2 | Low | 1 | Medium | 0.67 |
| Sparsely vegetated land - Tall forbs | Low | 2 | Low | 1 | Medium | 0.67 |
| Sparsely vegetated land - Inland rock outcrop and scree habitats | High | 6 | High | 0.33 | Low | 1 |
| Sparsely vegetated land - Limestone pavement | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Sparsely vegetated land - Maritime cliff and slopes | High | 6 | High | 0.33 | Medium | 0.67 |
| Sparsely vegetated land - Other inland rock and scree | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Urban - Allotments | Low | 2 | Low | 1 | Low | 1 |
| Urban - Artificial unvegetated, unsealed surface | V.Low | 0 | Low | 1 | Low | 1 |
| Urban - Bioswale | Low | 2 | Medium | 0.67 | Low | 1 |
| Urban - Intensive green roof | Low | 2 | Low | 1 | Low | 1 |
| Urban - Built linear features | V.Low | 0 | Low | 1 | Low | 1 |
| Urban - Cemeteries and churchyards | Medium | 4 | Medium | 0.67 | Low | 1 |
| Urban - Developed land; sealed surface | V.Low | 0 | Low | 1 | Low | 1 |
| Urban - Other green roof | Low | 2 | Low | 1 | Low | 1 |
| Urban - Facade-bound green wall | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Urban - Ground based green wall | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Urban - Ground level planters | Low | 2 | Low | 1 | Low | 1 |
| Urban - Biodiverse green roof | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Urban - Introduced shrub | Low | 2 | Low | 1 | Low | 1 |
| Urban - Open mosaic habitats on previously developed land | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Urban - Rain garden | Low | 2 | Low | 1 | Low | 1 |
| Urban - Actively worked sand pit quarry or open cast mine | Low | 2 | Medium | 0.67 | Low | 1 |
| Urban - Sustainable drainage system | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Urban - Unvegetated garden | V.Low | 0 | Low | 1 | Low | 1 |
| Urban - Vacant or derelict land | Low | 2 | Low | 1 | Low | 1 |
| Urban - Bare ground | Low | 2 | Low | 1 | Low | 1 |
| Urban - Vegetated garden | Low | 2 | Low | 1 | Low | 1 |
| Individual trees - Urban tree | Medium | 4 | Low | 1 | Low | 1 |
| Individual trees - Rural tree | Medium | 4 | Low | 1 | Low | 1 |
| Wetland - Blanket bog | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Wetland - Depressions on peat substrates (H7150) | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Wetland - Fens (upland and lowland) | V.High | 8 | High | 0.33 | High | 0.33 |
| Wetland - Lowland raised bog | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Wetland - Oceanic valley mire[1] (D2.1) | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Wetland - Purple moor grass and rush pastures | V.High | 8 | High | 0.33 | High | 0.33 |
| Wetland - Reedbeds | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Wetland - Transition mires and quaking bogs (H7140) | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Woodland and forest - Felled | High | 6 | High | 0.33 | Low | 1 |
| Woodland and forest - Lowland beech and yew woodland | High | 6 | High | 0.33 | High | 0.33 |
| Woodland and forest - Lowland mixed deciduous woodland | High | 6 | High | 0.33 | High | 0.33 |
| Woodland and forest - Native pine woodlands | High | 6 | High | 0.33 | High | 0.33 |
| Woodland and forest - Other coniferous woodland | Low | 2 | Low | 1 | Low | 1 |
| Woodland and forest - Other Scot's pine woodland | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Woodland and forest - Other woodland; broadleaved | Medium | 4 | Low | 1 | Low | 1 |
| Woodland and forest - Other woodland; mixed | Medium | 4 | Low | 1 | Low | 1 |
| Woodland and forest - Upland birchwoods | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Woodland and forest - Upland mixed ashwoods | High | 6 | High | 0.33 | High | 0.33 |
| Woodland and forest - Upland oakwood | High | 6 | High | 0.33 | High | 0.33 |
| Woodland and forest - Wet woodland | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Woodland and forest - Wood-pasture and parkland | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Woodland and forest - Felled | High | 6 | High | 0.33 | Low | 1 |
| Coastal lagoons - Coastal lagoons | High | 6 | Medium | 0.67 | Medium | 0.67 |
| Rocky shore - High energy littoral rock | High | 6 | High | 0.33 | Medium | 0.67 |
| Rocky shore - High energy littoral rock - on peat, clay or chalk | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Rocky shore - Moderate energy littoral rock | High | 6 | High | 0.33 | Medium | 0.67 |
| Rocky shore - Moderate energy littoral rock - on peat, clay or chalk | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Rocky shore - Low energy littoral rock | High | 6 | High | 0.33 | Medium | 0.67 |
| Rocky shore - Low energy littoral rock - on peat, clay or chalk | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Rocky shore - Features of littoral rock | High | 6 | High | 0.33 | Medium | 0.67 |
| Rocky shore - Features of littoral rock - on peat, clay or chalk | V.High | 8 | Very High | 0.1 | Medium | 0.67 |
| Coastal saltmarsh - Saltmarshes and saline reedbeds | High | 6 | High | 0.33 | Medium | 0.67 |
| Coastal saltmarsh - Artificial saltmarshes and saline reedbeds | Low | 2 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Littoral coarse sediment | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Intertidal sediment - Littoral mud | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Littoral mixed sediments | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Littoral seagrass | High | 6 | High | 0.33 | High | 0.33 |
| Intertidal sediment - Littoral seagrass on peat, clay or chalk | V.High | 8 | Very High | 0.1 | High | 0.33 |
| Intertidal sediment - Littoral biogenic reefs - Mussels | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Littoral biogenic reefs - Sabellaria | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Features of littoral sediment | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral coarse sediment | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral mud | Low | 2 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral sand | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral muddy sand | Low | 2 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral mixed sediments | Low | 2 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Artificial littoral seagrass | Low | 2 | High | 0.33 | High | 0.33 |
| Intertidal sediment - Artificial littoral biogenic reefs | Low | 2 | High | 0.33 | Medium | 0.67 |
| Intertidal sediment - Littoral sand | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Intertidal sediment - Littoral muddy sand | High | 6 | High | 0.33 | Medium | 0.67 |
| Intertidal hard structures - Artificial hard structures | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Intertidal hard structures - Artificial features of hard structures | Low | 2 | Medium | 0.67 | Medium | 0.67 |
| Intertidal hard structures - Artificial hard structures with integrated greening of grey infrastructure (IGGI) | Medium | 4 | Medium | 0.67 | Medium | 0.67 |
| Watercourse footprint - Watercourse footprint | V.low | 0 | Low | 1 | Low | 1 |

#### Onglet G-4, délais de création par condition visée (années)

| Habitat | Bon | Assez bon | Moyen | Assez mauvais | Mauvais | Sans état |
|---|---|---|---|---|---|---|
| Cropland - Arable field margins game bird mix | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Arable field margins pollen and nectar | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Arable field margins tussocky | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Cereal crops | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Winter stubble | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Horticulture | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Intensive orchards | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Non-cereal crops | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Cropland - Temporary grass and clover leys | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Grassland - Traditional orchards | 30 | 25 | 20 | 10 | 5 | Not Possible ▲ |
| Grassland - Bracken | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Grassland - Floodplain wetland mosaic and CFGM | 20 | 15 | 10 | 8 | 5 | Not Possible ▲ |
| Grassland - Lowland calcareous grassland | 20 | 15 | 10 | 8 | 5 | Not Possible ▲ |
| Grassland - Lowland dry acid grassland | 30+ | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Grassland - Lowland meadows | 15 | 12 | 10 | 8 | 5 | Not Possible ▲ |
| Grassland - Modified grassland | 7 | 5 | 4 | 2 | 1 | Not Possible ▲ |
| Grassland - Other lowland acid grassland | 15 | 12 | 10 | 5 | 1 | Not Possible ▲ |
| Grassland - Other neutral grassland | 10 | 7 | 5 | 3 | 2 | Not Possible ▲ |
| Grassland - Tall herb communities (H6430) | 30 | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Grassland - Upland acid grassland | 15 | 12 | 10 | 5 | 1 | Not Possible ▲ |
| Grassland - Upland calcareous grassland | 25 | 20 | 15 | 12 | 10 | Not Possible ▲ |
| Grassland - Upland hay meadows | 20 | 18 | 15 | 12 | 10 | Not Possible ▲ |
| Heathland and shrub - Blackthorn scrub | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Heathland and shrub - Bramble scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Heathland and shrub - Gorse scrub | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Heathland and shrub - Hawthorn scrub | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Heathland and shrub - Hazel scrub | 15 | 12 | 10 | 7 | 5 | Not Possible ▲ |
| Heathland and shrub - Willow scrub | 15 | 12 | 10 | 7 | 5 | Not Possible ▲ |
| Heathland and shrub - Lowland heathland | 30+ | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Heathland and shrub - Mixed scrub | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Heathland and shrub - Mountain heaths and willow scrub | 30+ | 30+ | 25 | 23 | 15 | Not Possible ▲ |
| Heathland and shrub - Rhododendron scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Heathland and shrub - Dunes with sea buckthorn (H2160) | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Heathland and shrub - Other sea buckthorn scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Heathland and shrub - Upland heathland | 30 | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Lakes - Aquifer fed naturally fluctuating water bodies | 30 | 20 | 15 | 10 | 1 | Not Possible ▲ |
| Lakes - High alkalinity lakes | 30 | 20 | 10 | 7 | 5 | Not Possible ▲ |
| Lakes - Low alkalinity lakes | 30 | 20 | 10 | 7 | 5 | Not Possible ▲ |
| Lakes - Marl lakes | 30 | 20 | 10 | 7 | 5 | Not Possible ▲ |
| Lakes - Moderate alkalinity lakes | 30 | 20 | 10 | 7 | 5 | Not Possible ▲ |
| Lakes - Peat lakes | 30 | 20 | 10 | 7 | 5 | Not Possible ▲ |
| Lakes - Ponds (priority habitat) | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Lakes - Ponds (non-priority habitat) | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Lakes - Reservoirs | 10 | 7 | 5 | 3 | 1 | Not Possible ▲ |
| Lakes - Temporary lakes ponds and pools (H3170) | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Sparsely vegetated land - Calaminarian grasslands | 10 | 7 | 5 | 3 | 2 | Not Possible ▲ |
| Sparsely vegetated land - Coastal sand dunes | 20 | 15 | 10 | 7 | 5 | Not Possible ▲ |
| Sparsely vegetated land - Coastal vegetated shingle | 20 | 15 | 10 | 7 | 5 | Not Possible ▲ |
| Sparsely vegetated land - Ruderal/Ephemeral | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Sparsely vegetated land - Tall forbs | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Sparsely vegetated land - Inland rock outcrop and scree habitats | 30+ | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Sparsely vegetated land - Limestone pavement | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Sparsely vegetated land - Maritime cliff and slopes | 20 | 15 | 10 | 7 | 5 | Not Possible ▲ |
| Sparsely vegetated land - Other inland rock and scree | 20 | 15 | 10 | 7 | 5 | Not Possible ▲ |
| Urban - Allotments | 1 | 1 | 1 | 1 | 1 | Not Possible ▲ |
| Lakes - Ornamental lake or pond | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Artificial unvegetated, unsealed surface | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Bioswale | 3 | 2 | 1 | 1 | 1 | Not Possible ▲ |
| Urban - Intensive green roof | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Built linear features | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Cemeteries and churchyards | 20 | 17 | 15 | 12 | 10 | Not Possible ▲ |
| Urban - Developed land; sealed surface | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Other green roof | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Urban - Facade-bound green wall | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Ground based green wall | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Ground level planters | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Urban - Biodiverse green roof | 10 | 8 | 5 | 3 | 1 | Not Possible ▲ |
| Urban - Introduced shrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Urban - Open mosaic habitats on previously developed land | 10 | 7 | 4 | 2 | 0 | Not Possible ▲ |
| Urban - Rain garden | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Actively worked sand pit quarry or open cast mine | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Individual trees - Urban tree | 30+ | 30+ | 27 | 19 | 10 | Not Possible ▲ |
| Urban - Sustainable drainage system | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Unvegetated garden | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Vacant or derelict land | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Bare ground | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Urban - Vegetated garden | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | 1 |
| Wetland - Blanket bog | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Wetland - Depressions on peat substrates (H7150) | 30+ | 30+ | 30 | 25 | 15 | Not Possible ▲ |
| Wetland - Fens (upland and lowland) | 30 | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Wetland - Lowland raised bog | 30+ | 30+ | 30 | 20 | 15 | Not Possible ▲ |
| Wetland - Oceanic valley mire[1] (D2.1) | 30+ | 30+ | 30 | 20 | 15 | Not Possible ▲ |
| Wetland - Purple moor grass and rush pastures | 30 | 25 | 20 | 15 | 10 | Not Possible ▲ |
| Wetland - Reedbeds | 12 | 10 | 7 | 5 | 3 | Not Possible ▲ |
| Wetland - Transition mires and quaking bogs (H7140) | 30+ | 30+ | 30 | 25 | 15 | Not Possible ▲ |
| Woodland and forest - Felled | 30+ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Woodland and forest - Lowland beech and yew woodland | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Lowland mixed deciduous woodland | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Native pine woodlands | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Other coniferous woodland | 30+ | 30+ | 30 | 10 | 5 | Not Possible ▲ |
| Woodland and forest - Other Scot's pine woodland | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Other woodland; broadleaved | 30+ | 25 | 15 | 7 | 5 | Not Possible ▲ |
| Woodland and forest - Other woodland; mixed | 30+ | 30+ | 30 | 10 | 5 | Not Possible ▲ |
| Woodland and forest - Upland birchwoods | 30+ | 30 | 25 | 20 | 10 | Not Possible ▲ |
| Woodland and forest - Upland mixed ashwoods | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Upland oakwood | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Woodland and forest - Wet woodland | 30+ | 30 | 15 | 10 | 5 | Not Possible ▲ |
| Woodland and forest - Wood-pasture and parkland | 30+ | 30+ | 30+ | 25 | 10 | Not Possible ▲ |
| Coastal lagoons - Coastal lagoons | 10 | 8 | 5 | 3 | 1 | Not Possible ▲ |
| Rocky shore - High energy littoral rock | 10 | 7 | 4 | 2 | 1 | Not Possible ▲ |
| Rocky shore - High energy littoral rock - on peat, clay or chalk | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Rocky shore - Moderate energy littoral rock | 13 | 8 | 4 | 2 | 1 | Not Possible ▲ |
| Rocky shore - Moderate energy littoral rock - on peat, clay or chalk | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Rocky shore - Low energy littoral rock | 15 | 10 | 5 | 1 | 1 | Not Possible ▲ |
| Rocky shore - Low energy littoral rock - on peat, clay or chalk | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Rocky shore - Features of littoral rock | 13 | 8 | 4 | 2 | 1 | Not Possible ▲ |
| Rocky shore - Features of littoral rock - on peat, clay or chalk | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Intertidal sediment - Littoral coarse sediment | 3 | 2 | 1 | 1 | 1 | Not Possible ▲ |
| Intertidal sediment - Littoral mud | 6 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Intertidal sediment - Littoral mixed sediments | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Coastal saltmarsh - Saltmarshes and saline reedbeds | 15 | 10 | 7 | 3 | 1 | Not Possible ▲ |
| Coastal saltmarsh - Artificial saltmarshes and saline reedbeds | 15 | 10 | 7 | 3 | 1 | Not Possible ▲ |
| Intertidal sediment - Littoral seagrass | 20 | 15 | 10 | 5 | 2 | Not Possible ▲ |
| Intertidal sediment - Littoral seagrass on peat, clay or chalk | 30+ | 30+ | 30+ | 30+ | 30+ | Not Possible ▲ |
| Intertidal sediment - Littoral biogenic reefs - Mussels | 15 | 10 | 5 | 3 | 3 | Not Possible ▲ |
| Intertidal sediment - Littoral biogenic reefs - Sabellaria | 15 | 10 | 5 | 3 | 3 | Not Possible ▲ |
| Intertidal sediment - Features of littoral sediment | 10 | 7 | 5 | 3 | 3 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral coarse sediment | 3 | 2 | 1 | 1 | 1 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral mud | 6 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral sand | 4 | 2 | 1 | 1 | 1 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral muddy sand | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral mixed sediments | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral seagrass | 20 | 15 | 10 | 5 | 2 | Not Possible ▲ |
| Intertidal sediment - Artificial littoral biogenic reefs | 15 | 10 | 5 | 3 | 3 | Not Possible ▲ |
| Intertidal sediment - Littoral sand | 4 | 2 | 1 | 1 | 1 | Not Possible ▲ |
| Intertidal sediment - Littoral muddy sand | 5 | 4 | 3 | 2 | 1 | Not Possible ▲ |
| Intertidal hard structures - Artificial hard structures | 15 | 10 | 5 | 2 | 1 | Not Possible ▲ |
| Intertidal hard structures - Artificial features of hard structures | 13 | 8 | 4 | 2 | 1 | Not Possible ▲ |
| Intertidal hard structures - Artificial hard structures with integrated greening of grey infrastructure (IGGI) | 13 | 8 | 4 | 2 | 1 | Not Possible ▲ |
| Watercourse footprint - Watercourse footprint | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Individual trees - Rural tree | 30+ | 30+ | 27 | 19 | 10 | Not Possible ▲ |

#### Onglet G-4, multiplicateur temporel par année (option d'actualisation, convention C-T5)

| Année | % de l'unité d'origine | Multiplicateur |
|---|---|---|
| 1 | 96.5 | 0.965 |
| 2 | 93.1225 | 0.931225 |
| 3 | 89.8632125 | 0.898632125 |
| 4 | 86.71800006 | 0.8671800005999999 |
| 5 | 83.68287006 | 0.8368287006 |
| 6 | 80.75396961 | 0.8075396961 |
| 7 | 77.92758067 | 0.7792758067 |
| 8 | 75.20011535 | 0.7520011535000001 |
| 9 | 72.56811131 | 0.7256811131 |
| 10 | 70.02822742 | 0.7002822741999999 |
| 11 | 67.57723946 | 0.6757723946 |
| 12 | 65.21203607 | 0.6521203607 |
| 13 | 62.92961481 | 0.6292961481 |
| 14 | 60.72707829 | 0.6072707829 |
| 15 | 58.60163055 | 0.5860163055000001 |
| 16 | 56.55057348 | 0.5655057348 |
| 17 | 54.57130341 | 0.5457130340999999 |
| 18 | 52.66130779 | 0.5266130779 |
| 19 | 50.81816202 | 0.5081816202 |
| 20 | 49.03952635 | 0.4903952635 |
| 21 | 47.32314293 | 0.4732314293 |
| 22 | 45.66683292 | 0.4566683292 |
| 23 | 44.06849377 | 0.44068493770000006 |
| 24 | 42.52609649 | 0.4252609649 |
| 25 | 41.03768311 | 0.4103768311 |
| 26 | 39.6013642 | 0.396013642 |
| 27 | 38.21531646 | 0.3821531646 |
| 28 | 36.87778038 | 0.36877780379999997 |
| 29 | 35.58705807 | 0.3558705807 |
| 30 | 34.34151104 | 0.3434151104 |
| 31 | 33.13955815 | 0.3313955815 |
| 30+ | 31.97967361 | 0.3197967361 |
| Not Possible ▲ | N/A | N/A |
| Habitat banking dropdown list |  |  |
| 0 |  |  |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |
| 9 |  |  |
| 10 |  |  |
| 11 |  |  |
| 12 |  |  |
| 13 |  |  |
| 14 |  |  |
| 15 |  |  |
| 16 |  |  |
| 17 |  |  |
| 18 |  |  |
| 19 |  |  |
| 20 |  |  |
| 21 |  |  |
| 22 |  |  |
| 23 |  |  |
| 24 |  |  |
| 25 |  |  |
| 26 |  |  |
| 27 |  |  |
| 28 |  |  |
| 29 |  |  |
| 30 |  |  |
| 30+ |  |  |

#### Onglet G-5, délais d'amélioration (années)

| Habitat | Mauvais vers moyen | Mauvais vers bon | Moyen vers bon |
|---|---|---|---|
| Cropland - Arable field margins cultivated annually | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Arable field margins game bird mix | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Arable field margins pollen and nectar | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Arable field margins tussocky | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Cereal crops | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Winter stubble | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Horticulture | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Intensive orchards | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Non-cereal crops | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Cropland - Temporary grass and clover leys | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Grassland - Traditional orchards | 15 | 25 | 10 |
| Grassland - Bracken | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Grassland - Floodplain wetland mosaic and CFGM | 10 | 15 | 4 |
| Grassland - Lowland calcareous grassland | 10 | 20 | 10 |
| Grassland - Lowland dry acid grassland | 15 | 30+ | 20 |
| Grassland - Lowland meadows | 8 | 15 | 8 |
| Grassland - Modified grassland | 10 | 15 | 10 |
| Grassland - Other lowland acid grassland | 10 | 15 | 10 |
| Grassland - Other neutral grassland | 10 | 15 | 10 |
| Grassland - Tall herb communities (H6430) | 20 | 30 | 10 |
| Grassland - Upland acid grassland | 10 | 15 | 10 |
| Grassland - Upland calcareous grassland | 15 | 20 | 10 |
| Grassland - Upland hay meadows | 15 | 20 | 15 |
| Heathland and shrub - Blackthorn scrub | 5 | 10 | 3 |
| Heathland and shrub - Bramble scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Heathland and shrub - Gorse scrub | 5 | 10 | 3 |
| Heathland and shrub - Hawthorn scrub | 5 | 10 | 3 |
| Heathland and shrub - Hazel scrub | 7 | 15 | 7 |
| Heathland and shrub - Willow scrub | 7 | 15 | 7 |
| Heathland and shrub - Lowland heathland | 10 | 25 | 15 |
| Heathland and shrub - Mixed scrub | 5 | 10 | 3 |
| Heathland and shrub - Mountain heaths and willow scrub | 30+ | 30+ | 30+ |
| Heathland and shrub - Rhododendron scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Heathland and shrub - Dunes with sea buckthorn (H2160) | 7 | 12 | 7 |
| Heathland and shrub - Other sea buckthorn scrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Heathland and shrub - Upland heathland | 20 | 30+ | 20 |
| Lakes - Aquifer fed naturally fluctuating water bodies | 10 | 30 | 20 |
| Lakes - High alkalinity lakes | 10 | 30 | 20 |
| Lakes - Low alkalinity lakes | 10 | 20 | 10 |
| Lakes - Marl lakes | 10 | 30 | 20 |
| Lakes - Moderate alkalinity lakes | 10 | 30 | 20 |
| Lakes - Peat lakes | 10 | 30 | 20 |
| Lakes - Ponds (priority habitat) | 4 | 8 | 4 |
| Lakes - Ponds (non-priority habitat) | 4 | 8 | 4 |
| Lakes - Reservoirs | 10 | 30 | 20 |
| Lakes - Temporary lakes ponds and pools (H3170) | 4 | 8 | 4 |
| Sparsely vegetated land - Calaminarian grasslands | 3 | 8 | 5 |
| Sparsely vegetated land - Coastal sand dunes | 8 | 20 | 12 |
| Sparsely vegetated land - Coastal vegetated shingle | 8 | 20 | 12 |
| Sparsely vegetated land - Ruderal/Ephemeral | 2 | 5 | 2 |
| Sparsely vegetated land - Tall forbs | 2 | 5 | 2 |
| Sparsely vegetated land - Inland rock outcrop and scree habitats | 20 | 30+ | 20 |
| Sparsely vegetated land - Limestone pavement | 10 | 20 | 10 |
| Sparsely vegetated land - Maritime cliff and slopes | 8 | 20 | 12 |
| Sparsely vegetated land - Other inland rock and scree | 10 | 20 | 10 |
| Urban - Allotments | 1 | 1 | 1 |
| Lakes - Ornamental lake or pond | 4 | 8 | 4 |
| Urban - Artificial unvegetated, unsealed surface | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Bioswale | 2 | 3 | 2 |
| Urban - Intensive green roof | 2 | 5 | 2 |
| Urban - Built linear features | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Cemeteries and churchyards | 10 | 20 | 15 |
| Urban - Developed land; sealed surface | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Other green roof | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Facade-bound green wall | 2 | 5 | 2 |
| Urban - Ground based green wall | 2 | 5 | 2 |
| Urban - Ground level planters | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Biodiverse green roof | 5 | 10 | 5 |
| Urban - Introduced shrub | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Open mosaic habitats on previously developed land | 4 | 10 | 4 |
| Urban - Rain garden | 1 | 1 | 1 |
| Urban - Actively worked sand pit quarry or open cast mine | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Individual trees - Urban tree | 16 | 30+ | 16 |
| Urban - Sustainable drainage system | 2 | 5 | 2 |
| Urban - Unvegetated garden | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Urban - Vacant or derelict land | 1 | 1 | 1 |
| Urban - Bare ground | 1 | 1 | 1 |
| Urban - Vegetated garden | 2 | 5 | 2 |
| Wetland - Blanket bog | 20 | 30+ | 30+ |
| Wetland - Depressions on peat substrates (H7150) | 20 | 30 | 20 |
| Wetland - Fens (upland and lowland) | 12 | 18 | 12 |
| Wetland - Lowland raised bog | 20 | 30 | 15 |
| Wetland - Oceanic valley mire[1] (D2.1) | 20 | 30 | 15 |
| Wetland - Purple moor grass and rush pastures | 10 | 20 | 15 |
| Wetland - Reedbeds | 7 | 12 | 7 |
| Wetland - Transition mires and quaking bogs (H7140) | 20 | 30 | 15 |
| Woodland and forest - Felled | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Woodland and forest - Lowland beech and yew woodland | 30+ | 30+ | 30+ |
| Woodland and forest - Lowland mixed deciduous woodland | 20 | 30+ | 20 |
| Woodland and forest - Native pine woodlands | 15 | 30+ | 15 |
| Woodland and forest - Other coniferous woodland | 25 | 30+ | 30+ |
| Woodland and forest - Other Scot's pine woodland | 15 | 30+ | 15 |
| Woodland and forest - Other woodland; broadleaved | 10 | 20 | 10 |
| Woodland and forest - Other woodland; mixed | 10 | 20 | 10 |
| Woodland and forest - Upland birchwoods | 15 | 30+ | 15 |
| Woodland and forest - Upland mixed ashwoods | 15 | 30+ | 15 |
| Woodland and forest - Upland oakwood | 30+ | 30+ | 30+ |
| Woodland and forest - Wet woodland | 10 | 30+ | 30+ |
| Woodland and forest - Wood-pasture and parkland | 30+ | 30+ | 30+ |
| Coastal lagoons - Coastal lagoons | 4 | 12 | 8 |
| Rocky shore - High energy littoral rock | 4 | 10 | 6 |
| Rocky shore - High energy littoral rock - on peat, clay or chalk | 4 | 10 | 6 |
| Rocky shore - Moderate energy littoral rock | 4 | 11 | 7 |
| Rocky shore - Moderate energy littoral rock - on peat, clay or chalk | 4 | 11 | 7 |
| Rocky shore - Low energy littoral rock | 4 | 12 | 8 |
| Rocky shore - Low energy littoral rock - on peat, clay or chalk | 4 | 12 | 8 |
| Rocky shore - Features of littoral rock | 4 | 11 | 7 |
| Rocky shore - Features of littoral rock - on peat, clay or chalk | 4 | 11 | 7 |
| Intertidal sediment - Littoral coarse sediment | 2 | 4 | 2 |
| Intertidal sediment - Littoral mud | 4 | 8 | 4 |
| Intertidal sediment - Littoral mixed sediments | 2 | 4 | 2 |
| Coastal saltmarsh - Saltmarshes and saline reedbeds | 6 | 20 | 14 |
| Coastal saltmarsh - Artificial saltmarshes and saline reedbeds | 6 | 20 | 14 |
| Intertidal sediment - Littoral seagrass | 13 | 30+ | 20 |
| Intertidal sediment - Littoral seagrass on peat, clay or chalk | 13 | 30+ | 20 |
| Intertidal sediment - Littoral biogenic reefs - Mussels | 4 | 10 | 6 |
| Intertidal sediment - Littoral biogenic reefs - Sabellaria | 4 | 10 | 6 |
| Intertidal sediment - Features of littoral sediment | 2 | 5 | 3 |
| Intertidal sediment - Artificial littoral coarse sediment | 2 | 4 | 2 |
| Intertidal sediment - Artificial littoral mud | 4 | 8 | 4 |
| Intertidal sediment - Artificial littoral sand | 3 | 6 | 3 |
| Intertidal sediment - Artificial littoral muddy sand | 4 | 8 | 4 |
| Intertidal sediment - Artificial littoral mixed sediments | 2 | 4 | 2 |
| Intertidal sediment - Artificial littoral seagrass | 13 | 30+ | 20 |
| Intertidal sediment - Artificial littoral biogenic reefs | 4 | 10 | 6 |
| Intertidal sediment - Littoral sand | 3 | 6 | 3 |
| Intertidal sediment - Littoral muddy sand | 4 | 8 | 4 |
| Intertidal hard structures - Artificial hard structures | 4 | 12 | 8 |
| Intertidal hard structures - Artificial features of hard structures | 4 | 11 | 7 |
| Intertidal hard structures - Artificial hard structures with integrated greening of grey infrastructure (IGGI) | 4 | 11 | 7 |
| Watercourse footprint - Watercourse footprint | Not Possible ▲ | Not Possible ▲ | Not Possible ▲ |
| Individual trees - Rural tree | 16 | 30+ | 16 |
