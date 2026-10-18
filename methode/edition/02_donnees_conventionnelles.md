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

### 2.11 Extraits des sources primaires utilisés

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
