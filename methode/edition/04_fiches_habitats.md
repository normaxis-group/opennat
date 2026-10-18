## Partie 4. Fiches habitats

Une fiche par type de la nomenclature, dans l'ordre des groupes EUNIS, précédés des types urbains et hors-sol. Chaque fiche se lit avec les fiches algorithmes de la partie 3. Ses valeurs viennent des tables de `donnees/` ; ses correspondances et ses espèces caractéristiques, de HabRef v7 (PatriNat, 07/08/2025), dont la licence reste à lire avant toute publication ; ses définitions EUNIS, de la classification EUNIS 2012 de l'Agence européenne pour l'environnement (CC BY 4.0), traduites et adaptées pour OpenNAT.

Les valeurs de référence de chaque fiche sont calculées pour 100 m² d'habitat, hors trame verte et bleue (m = 1), sans effet de taille, de connectivité ni de nuisance (k = 1), en pleine terre sauf mention contraire. Trois états servent d'exemple : bon (S = 1, f = 1), moyen (S = 0,75, f = 0,875) et mauvais (S = 0,4, f = 0,7). La trajectoire d'un habitat créé suppose un chantier d'un an.

### 4.1 Types urbains et hors-sol (VB)

#### Fiche H001. VB.1 : Surface bâtie (emprise de construction)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.1 |
| EUNIS 2012 | J1, J1.1, J1.2, J1.3, J1.4, J1.7, J2.1, J2.2, J2.3, J2.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité, 86.5 Serres et constructions agricoles |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Emprise au sol des constructions : bâtiments, annexes, ouvrages couverts. Surface scellée, sans sol vivant ni végétation, quelle que soit l'occupation de la toiture (une toiture végétalisée se saisit en plus, en VB.11 à VB.13).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0 m²HE/m² | 0 à 0 | code 52.03.01, « Versiegelter Platz oder sonstiger gepflasterter Platz », Biotoptypenwert 0 sur 24 (ligne 763 de l'extraction) |

Correspondance retenue : Surface scellée : valeur nulle commune à la BKompV (52.03.01) et à la métrique anglaise (u1b) ; les types BKompV 53.01 incluent leurs espaces libres et ne conviennent pas à une emprise seule.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 0 |
| État moyen | 0 |
| Mauvais état | 0 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H002. VB.2 : Surface imperméabilisée non bâtie (voirie, parking, dallage étanche)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.2 |
| EUNIS 2012 | J4.2, J4.1, J4.4, J4.5, J4.7 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 89.1 Lagunes industrielles et canaux salins, 89.11 Ports maritimes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Surfaces revêtues d'un matériau étanche à l'air et à l'eau, hors bâtiments : voiries, stationnements, cours et dallages posés sur mortier ou à joints étanches, aires techniques.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0 m²HE/m² | 0 à 0 | code 52.01.01a, « Versiegelter oder sonstiger gepflasterter Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) », Biotoptypenwert 0 sur 24 (ligne 747 de l'extraction) |

Correspondance retenue : Voie ou aire scellée.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 89, « Urban - Developed land; sealed surface » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 0 |
| État moyen | 0 |
| Mauvais état | 0 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H003. VB.3 : Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.3 |
| EUNIS 2012 | J4.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Surfaces minérales perméables sans végétation prévue : stabilisés, graviers, sables compactés, pavés ou dalles à joints sablés posés sur lit drainant, cheminements à liant hydraulique.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,1667 m²HE/m² | 0,15 à 0,1833 | code 52.03.03a, « Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) », Biotoptypenwert 4 sur 24 (ligne 765 de l'extraction) |

Correspondance retenue : Place à revêtement gravillonné ou à liant hydraulique (wassergebundene Decke).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 16,67 |
| État moyen | 14,59 |
| Mauvais état | 11,67 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H004. VB.4 : Revêtement perméable végétalisé (dalles alvéolées engazonnées)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.4 |
| EUNIS 2012 | J4.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Surfaces stabilisées perméables conçues pour porter une végétation durable sous une faible fréquentation : dalles alvéolées engazonnées, pavés à joints engazonnés, mélange terre-pierre engazonné.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,125 m²HE/m² | 0,1125 à 0,1375 | code 52.03.02, « Teilbefestigter Platz (z. B. Rasengitter) », Biotoptypenwert 3 sur 24 (ligne 764 de l'extraction) |

Correspondance retenue : Place partiellement stabilisée (Rasengitter).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 12,5 |
| État moyen | 10,94 |
| Mauvais état | 8,75 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H005. VB.5 : Pelouse d'agrément tondue, terrain de sport engazonné

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.5 |
| EUNIS 2012 | E2.6, E2.8 |
| EUNIS 2022 (HabRef) | V3-1 Prairies améliorées, réensemencées et fortement fertilisées, y compris les terrains de sport et les gazons, V3-5 Pelouses mésophiles piétinées à espèces annuelles |
| CORINE Biotopes (HabRef) | 81 Prairies améliorées, 81.1 Prairies sèches améliorées, 81.2 Prairies humides améliorées, 85.1 Grands parcs, 85.12 Pelouses de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP1 (prairies de faible valeur) |

**Définition**

Pelouses à forte fréquentation ou tondues ras et souvent : gazons d'agrément, aires de jeux et terrains de sport engazonnés, accotements tondus. Flore pauvre, dominée par quelques graminées semées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (6 taxons ; les 40 plus cités) : Juncus bufonius, Poa supina, Sagina apetala, Sagina procumbens, Spergularia rubra, Veronica serpyllifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |

Correspondance retenue : Gazon piétiné et de parc (Tritt- und Parkrasen).

**Grille d'état EP1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Fourrés sur moins de 20 % de la surface de la prairie | non |
| D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface | non |
| E | Sol nu entre 1 % et 10 % de la surface | non |
| F | Fougère aigle sur moins de 20 % de la surface | non |
| G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 7 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| Création, état moyen visé | 4 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 33,33 |
| État moyen | 29,16 |
| Mauvais état | 23,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 16,66 m²HE, 15 à 30 cm 20 m²HE, 30 à 80 cm 23,33 m²HE, 80 cm et plus 30 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,8 | 9,5 | 19 | 33,3 | 33,3 | 33,3 | 33,3 | 33,3 | 1 533 |
| moyen | 0 | 7,3 | 14,6 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 385 |
| mauvais | 0 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 1 143 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H006. VB.6 : Massif ornemental horticole, couvre-sol planté

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.6 |
| EUNIS 2012 | I2.1 |
| EUNIS 2022 (HabRef) | V2-1 Grands jardins ornementaux |
| CORINE Biotopes (HabRef) | 85.1 Grands parcs, 85.14 Parterre de fleurs, avec arbres et avec bosquets en parc |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Plantations ornementales de vivaces, d'arbustes ou de couvre-sols, entretenues : massifs, bordures, talus plantés. Espèces souvent horticoles ou exotiques, structure végétale simple.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 51.07a.02, « Sonstige Grünanlage ohne alten Baumbestand », Biotoptypenwert 9 sur 24 (ligne 731 de l'extraction) |

Correspondance retenue : Autre espace vert sans arbres anciens.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 72, « Urban - Introduced shrub », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 95, « Urban - Introduced shrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 95, « Urban - Introduced shrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 37,5 |
| État moyen | 32,81 |
| Mauvais état | 26,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 18,75 m²HE, 15 à 30 cm 22,5 m²HE, 30 à 80 cm 26,25 m²HE, 80 cm et plus 33,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 1 838 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H007. VB.7 : Jardin domestique végétalisé

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.7 |
| EUNIS 2012 | I2.2 |
| EUNIS 2022 (HabRef) | V2-2 Petits jardins ornementaux et domestiques |
| CORINE Biotopes (HabRef) | 85.2 Petits parcs et squares citadins, 85.3 Jardins, 85.31 Jardins ornementaux, 85.32 Jardins potagers de subsistance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Jardins privatifs ou communs associés à l'habitat : mosaïque de pelouse, de massifs, d'arbustes et parfois d'arbres, entretenue par les occupants.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |

Correspondance retenue : Jardins privés riches en structures : valeur de la variante en bon état, l'état est porté par le facteur d'état (convention C-H2).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 22,91 m²HE, 15 à 30 cm 27,5 m²HE, 30 à 80 cm 32,08 m²HE, 80 cm et plus 41,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 2 246 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H008. VB.8 : Friche urbaine herbacée

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.8 |
| EUNIS 2012 | J1.5, J2.6, J3.3, J4.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86.4 Sites industriels anciens, 86.41 Carrières, 86.411 Carrières de sable, d'argile et de kaolin, 86.412 Carrières de graviers, 86.413 Carrières de pierres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Végétation herbacée spontanée d'anciens terrains bâtis, industriels ou ferroviaires, en mosaïque avec du sol nu, des gravats et des communautés pionnières. Peut abriter une flore et une faune remarquables quand la mosaïque est variée.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 51.04a.01, « – Mit wesentlichen Anteilen struktur-/artenreicher Ausprägung », Biotoptypenwert 12 sur 24 (ligne 719 de l'extraction) |

Correspondance retenue : Friche d'anciens sites bâtis, variante riche en structures ou en espèces.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible bon |
| Création, état moyen visé | 4 ans | onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible moyen |
| Création, mauvais état visé | 0 ans | onglet G-4, ligne 73, « Urban - Open mosaic habitats on previously developed land », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 74, « Urban - Open mosaic habitats on previously developed land », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 96, « Urban - Open mosaic habitats on previously developed land » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 96, « Urban - Open mosaic habitats on previously developed land » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,4 | 6,7 | 13,4 | 30,2 | 33,5 | 33,5 | 33,5 | 33,5 | 1 491 |
| moyen | 0 | 7,3 | 14,7 | 29,3 | 29,3 | 29,3 | 29,3 | 29,3 | 29,3 | 1 392 |
| mauvais | 0 | 23,5 | 23,5 | 23,5 | 23,5 | 23,5 | 23,5 | 23,5 | 23,5 | 1 149 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H009. VB.9 : Friche urbaine arbustive (plus de 50 % de ligneux)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.9 |
| EUNIS 2012 | J1.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Friche colonisée par les ligneux (plus de 50 % de couvert d'arbustes ou de jeunes arbres), sur sol remanié et souvent enrichi.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.01.06, « Gebüsch stickstoffreicher, ruderaler Standorte und stark verbuschte Grünlandbrache (Verbuschung > 50 %) », Biotoptypenwert 12 sur 24 (ligne 440 de l'extraction) |

Correspondance retenue : Fourré des stations rudérales riches en azote.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5 | 10 | 20 | 45 | 50 | 50 | 50 | 50 | 2 225 |
| moyen | 0 | 8,8 | 17,5 | 35 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 056 |
| mauvais | 0 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 1 715 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H010. VB.10 : Sol nu, chantier, terrassement

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.10 |
| EUNIS 2012 | J1.6, J2.7, J6.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Sol mis à nu par un chantier, un terrassement ou une démolition, sans couvert végétal établi.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,125 m²HE/m² | 0,1125 à 0,1375 | code 32.11.09a, « Bauflächen und Baustelleneinrichtungsflächen », Biotoptypenwert 3 sur 24 (ligne 289 de l'extraction) |

Correspondance retenue : Surfaces de chantier et d'installations de chantier.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 80, « Urban - Bare ground », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 80, « Urban - Bare ground », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 80, « Urban - Bare ground », condition cible mauvais |
| Amélioration, mauvais vers moyen | 1 ans | onglet G-5, ligne 81, « Urban - Bare ground », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 1 ans | onglet G-5, ligne 81, « Urban - Bare ground », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 1 ans | onglet G-5, ligne 81, « Urban - Bare ground », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 82, « Urban - Bare ground » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 82, « Urban - Bare ground » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 12,5 |
| État moyen | 10,94 |
| Mauvais état | 8,75 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,5 | 5 | 10 | 12,5 | 12,5 | 12,5 | 12,5 | 12,5 | 588 |
| moyen | 0 | 3,6 | 7,3 | 10,9 | 10,9 | 10,9 | 10,9 | 10,9 | 10,9 | 525 |
| mauvais | 0 | 8,8 | 8,8 | 8,8 | 8,8 | 8,8 | 8,8 | 8,8 | 8,8 | 429 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H011. VB.11 : Toiture végétalisée extensive (substrat de moins de 15 cm)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.11 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (toiture ou bac) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Toiture végétalisée à faible épaisseur de substrat (moins de 15 cm), le plus souvent plantée d'orpins, de mousses et de graminées basses, sans arrosage.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2639 m²HE/m² | 0,1319 à 0,3958 | onglet G-1, ligne 66, « Urban - Other green roof », distinctivité 2 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 67, « Urban - Other green roof », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 90, « Urban - Other green roof » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 90, « Urban - Other green roof » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 26,39 |
| État moyen | 23,09 |
| Mauvais état | 18,47 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 1 293 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H012. VB.12 : Toiture végétalisée semi-intensive ou biodiverse (15 à 30 cm)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.12 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (toiture ou bac) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Toiture végétalisée de 15 à 30 cm de substrat, ou toiture dite biodiverse : substrat d'épaisseur variée, semis de plantes sauvages, éléments d'habitat (tas de sable, pierres, bois).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5278 m²HE/m² | 0,2639 à 0,7917 | onglet G-1, ligne 70, « Urban - Biodiverse green roof », distinctivité 4 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 71, « Urban - Biodiverse green roof », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 5 ans | onglet G-5, ligne 72, « Urban - Biodiverse green roof », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 94, « Urban - Biodiverse green roof » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 94, « Urban - Biodiverse green roof » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 52,78 |
| État moyen | 46,18 |
| Mauvais état | 36,95 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,5 | 7,1 | 14,1 | 31,8 | 35,4 | 35,4 | 35,4 | 35,4 | 1 574 |
| moyen | 0 | 6,2 | 12,4 | 24,8 | 30,9 | 30,9 | 30,9 | 30,9 | 30,9 | 1 454 |
| mauvais | 0 | 24,8 | 24,8 | 24,8 | 24,8 | 24,8 | 24,8 | 24,8 | 24,8 | 1 213 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H013. VB.13 : Toiture végétalisée intensive (plus de 30 cm)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.13 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (toiture ou bac) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Toiture ou dalle aménagée en jardin, à plus de 30 cm de substrat, portant pelouses, vivaces, arbustes, parfois petits arbres, généralement arrosée.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2639 m²HE/m² | 0,1319 à 0,3958 | onglet G-1, ligne 62, « Urban - Intensive green roof », distinctivité 2 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 63, « Urban - Intensive green roof », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 64, « Urban - Intensive green roof », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 86, « Urban - Intensive green roof » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 86, « Urban - Intensive green roof » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 26,39 |
| État moyen | 23,09 |
| Mauvais état | 18,47 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5,3 | 10,6 | 21,1 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 1 240 |
| moyen | 0 | 7,7 | 15,4 | 23,1 | 23,1 | 23,1 | 23,1 | 23,1 | 23,1 | 1 108 |
| mauvais | 0 | 18,5 | 18,5 | 18,5 | 18,5 | 18,5 | 18,5 | 18,5 | 18,5 | 905 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H014. VB.15 : Façade végétalisée enracinée au sol (plantes grimpantes)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.15 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (façade) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Façade couverte de plantes grimpantes enracinées dans le sol, avec ou sans support.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2639 m²HE/m² | 0,1319 à 0,3958 | onglet G-1, ligne 68, « Urban - Ground based green wall », distinctivité 2 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 69, « Urban - Ground based green wall », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 70, « Urban - Ground based green wall », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 92, « Urban - Ground based green wall » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 92, « Urban - Ground based green wall » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 26,39 |
| État moyen | 23,09 |
| Mauvais état | 18,47 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,5 | 7,1 | 14,1 | 17,7 | 17,7 | 17,7 | 17,7 | 17,7 | 831 |
| moyen | 0 | 5,2 | 10,3 | 15,5 | 15,5 | 15,5 | 15,5 | 15,5 | 15,5 | 743 |
| mauvais | 0 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 606 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H015. VB.16 : Façade végétalisée hors sol (bacs, modules)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.16 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (façade) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Mur végétalisé par des modules, bacs ou nappes de culture fixés à la façade, alimentés par un système d'irrigation.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2639 m²HE/m² | 0,1319 à 0,3958 | onglet G-1, ligne 67, « Urban - Facade-bound green wall », distinctivité 2 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 68, « Urban - Facade-bound green wall », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 69, « Urban - Facade-bound green wall », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 91, « Urban - Facade-bound green wall » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 91, « Urban - Facade-bound green wall » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 26,39 |
| État moyen | 23,09 |
| Mauvais état | 18,47 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,5 | 7,1 | 14,1 | 17,7 | 17,7 | 17,7 | 17,7 | 17,7 | 831 |
| moyen | 0 | 5,2 | 10,3 | 15,5 | 15,5 | 15,5 | 15,5 | 15,5 | 15,5 | 743 |
| mauvais | 0 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 12,4 | 606 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H016. VB.18a : Arbre isolé ou alignement d'essence indigène

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.18a |
| EUNIS 2012 | G5.1 |
| EUNIS 2022 (HabRef) | V6-3 Alignements d'arbres plantés |
| CORINE Biotopes (HabRef) | 84.1 Alignements d'arbres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | arbre (houppier projeté) |
| Grille d'état | EA1 (arbres) |

**Définition**

Arbre isolé, alignement ou groupe d'arbres d'essences indigènes, hors boisement, en milieu urbain. Surface : houppier projeté.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.05aM, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 474 de l'extraction) |
| Valeur, stade jeune | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.05aJ, « – Junge Ausprägung », 11 sur 24 |
| Valeur, stade moyen | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.05aM, « – Mittlere Ausprägung », 15 sur 24 |
| Valeur, stade âgé | 0,75 m²HE/m² | 0,675 à 0,825 | code 41.05aA, « – Alte Ausprägung », 18 sur 24 |

Correspondance retenue : Arbres isolés, alignements et groupes d'essences autochtones ; stade jeune, moyen ou âgé selon la classe de diamètre (convention C-H5).

**Grille d'état EA1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Essence indigène (ou au moins 70 % d'essences indigènes dans un groupe) | non |
| B | Couvert continu, trouées sur moins de 10 % et aucune de plus de 5 m (critère réputé satisfait pour un arbre isolé) | non |
| C | Arbre mûr (ou plus de 50 % d'arbres mûrs dans un groupe) | non |
| D | Pas d'atteinte humaine à la santé de l'arbre et pas de taille régulière : plus de 75 % du houppier naturel conservé | non |
| E | Microhabitats présents : bois mort, cavités, lierre, écorce décollée | non |
| F | Plus de 20 % du houppier au-dessus d'une végétation (et non d'un sol revêtu) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible bon |
| Création, état moyen visé | 27 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible mauvais |
| Amélioration, mauvais vers moyen | 16 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 16 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 99, « Individual trees - Urban tree » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 99, « Individual trees - Urban tree » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2 | 3,9 | 7,8 | 17,6 | 27,3 | 37,1 | 56,6 | 62,5 | 2 094 |
| moyen | 0 | 2 | 4,1 | 8,1 | 18,2 | 28,4 | 38,5 | 54,7 | 54,7 | 1 969 |
| mauvais | 0 | 4,4 | 8,8 | 17,5 | 39,4 | 43,8 | 43,8 | 43,8 | 43,8 | 1 947 |

#### Fiche H017. VB.18b : Arbre isolé ou alignement d'essence non indigène

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.18b |
| EUNIS 2012 | G5.1 |
| EUNIS 2022 (HabRef) | V6-3 Alignements d'arbres plantés |
| CORINE Biotopes (HabRef) | 84.1 Alignements d'arbres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | arbre (houppier projeté) |
| Grille d'état | EA1 (arbres) |

**Définition**

Arbre isolé, alignement ou groupe d'arbres d'essences non indigènes, hors boisement, en milieu urbain. Surface : houppier projeté.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.05bM, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 11 sur 24 (ligne 478 de l'extraction) |
| Valeur, stade jeune | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 41.05bJ, « – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken », 8 sur 24 |
| Valeur, stade moyen | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.05bM, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », 11 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.05bA, « – Alte Ausprägung/– Mit Überhältern alter Ausprägung », 14 sur 24 |

Correspondance retenue : Arbres isolés, alignements et groupes d'essences non autochtones ; stade selon la classe de diamètre (convention C-H5).

**Grille d'état EA1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Essence indigène (ou au moins 70 % d'essences indigènes dans un groupe) | non |
| B | Couvert continu, trouées sur moins de 10 % et aucune de plus de 5 m (critère réputé satisfait pour un arbre isolé) | non |
| C | Arbre mûr (ou plus de 50 % d'arbres mûrs dans un groupe) | non |
| D | Pas d'atteinte humaine à la santé de l'arbre et pas de taille régulière : plus de 75 % du houppier naturel conservé | non |
| E | Microhabitats présents : bois mort, cavités, lierre, écorce décollée | non |
| F | Plus de 20 % du houppier au-dessus d'une végétation (et non d'un sol revêtu) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible bon |
| Création, état moyen visé | 27 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 76, « Individual trees - Urban tree », condition cible mauvais |
| Amélioration, mauvais vers moyen | 16 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 16 ans | onglet G-5, ligne 77, « Individual trees - Urban tree », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 99, « Individual trees - Urban tree » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 99, « Individual trees - Urban tree » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,9 | 5,7 | 12,9 | 20,1 | 27,2 | 41,5 | 45,8 | 1 535 |
| moyen | 0 | 1,5 | 3 | 5,9 | 13,4 | 20,8 | 28,2 | 40,1 | 40,1 | 1 444 |
| mauvais | 0 | 3,2 | 6,4 | 12,8 | 28,9 | 32,1 | 32,1 | 32,1 | 32,1 | 1 428 |

#### Fiche H018. VB.19 : Noue, jardin de pluie, bassin paysager alimenté en eau de pluie

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.19 |
| EUNIS 2012 | J5.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 89.2 Lagunes industrielles et canaux d'eau douce, 89.23 Lagunes industrielles et bassins ornementaux |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Ouvrage végétalisé de gestion des eaux pluviales à ciel ouvert : noue, jardin de pluie, bassin paysager, alimenté par le ruissellement et généralement temporairement en eau.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 23.05.01a.01, « – Naturnahe Ausbildung/ohne oder mit extensiver Unterhaltung », Biotoptypenwert 13 sur 24 (ligne 194 de l'extraction) |

Correspondance retenue : Fossé à fonctionnement naturel, sans entretien ou à entretien extensif : seul type BKompV d'ouvrage linéaire en eau végétalisé (convention C-H4).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 74, « Urban - Rain garden », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 74, « Urban - Rain garden », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 74, « Urban - Rain garden », condition cible mauvais |
| Amélioration, mauvais vers moyen | 1 ans | onglet G-5, ligne 75, « Urban - Rain garden », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 1 ans | onglet G-5, ligne 75, « Urban - Rain garden », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 1 ans | onglet G-5, ligne 75, « Urban - Rain garden », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 97, « Urban - Rain garden » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 97, « Urban - Rain garden » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 10,8 | 21,7 | 43,3 | 54,2 | 54,2 | 54,2 | 54,2 | 54,2 | 2 546 |
| moyen | 0 | 15,8 | 31,6 | 47,4 | 47,4 | 47,4 | 47,4 | 47,4 | 47,4 | 2 275 |
| mauvais | 0 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 1 858 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H019. VB.20 : Mare créée ou plan d'eau à berges naturelles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.20 |
| EUNIS 2012 | C1.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.13 Eaux eutrophes, 22.4 Végétations aquatiques, 22.41 Végétations flottant librement, 22.411 Couvertures de Lemnacées, 22.412 Radeaux d'Hydrocharis, 22.413 Radeaux de Stratiotes, 22.414 Colonies d'Utriculaires, 22.415 Couvertures de Salvinia, 22.416 Groupements à Aldrovanda, 22.42 Végétations enracinées immergées, et 10 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Mare ou petit plan d'eau créé, à berges en pente douce et sans revêtement étanche visible, alimenté par la nappe, le ruissellement ou la pluie.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (43 taxons ; les 40 plus cités) : Callitriche sp., Hottonia palustris, Chlorophyta sp., Bacillariophyta sp., Myriophyllum spicatum, Ceratophyllum submersum, Lemna minor, Salvinia natans, Spirodela polyrhiza, Stratiotes aloides, Wolffia arrhiza, Cladocera sp., Chrysophyta sp., Euglenophyta sp., Rotatoria sp., Pyrrophyta sp., Copepoda sp., Ceratophyllum demersum, Lemna trisulca, Nuphar lutea, Nymphaea alba, Nymphoides peltata, Persicaria amphibia, Trapa natans, Myriophyllum verticillatum, Najas marina, Najas minor, Potamogeton sp., Cyanobacteriophyta sp., Ranunculus aquatilis, Ranunculus baudotii, Ranunculus hederaceus, Ranunculus ololeucos, Ranunculus omiophyllus, Ranunculus peltatus, Ranunculus trichophyllus, Ranunculus tripartitus, Ranunculus lenormandi, Ranunculus confervoides, Ranunculus rionii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 24.04c, « Naturnahe eutrophe Gewässer, inkl. sich selbst überlassene Abbaugewässer (Teilabschnitte können getrennt betrachtet werden) », Biotoptypenwert 15 sur 24 (ligne 232 de l'extraction) |

Correspondance retenue : Plan d'eau eutrophe proche de l'état naturel.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 47, « Lakes - Ponds (non-priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 48, « Lakes - Ponds (non-priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 60, « Lakes - Ponds (non-priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 60, « Lakes - Ponds (non-priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 12,5 | 25 | 50 | 62,5 | 62,5 | 62,5 | 62,5 | 62,5 | 2 938 |
| moyen | 0 | 18,2 | 36,5 | 54,7 | 54,7 | 54,7 | 54,7 | 54,7 | 54,7 | 2 625 |
| mauvais | 0 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 144 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H020. VB.21 : Bassin, fontaine ou plan d'eau à eau traitée

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.21 |
| EUNIS 2012 | J5.5, J5.1, J5.2, J5.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 89.1 Lagunes industrielles et canaux salins, 89.12 Salines, 89.13 Autres lagunes industrielles et canaux salins, 89.2 Lagunes industrielles et canaux d'eau douce, 89.21 Canaux navigables, 89.22 Fossés et petits canaux |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Bassin d'agrément, fontaine, miroir d'eau ou plan d'eau dont l'eau est traitée, recyclée ou chlorée, ou dont les berges sont maçonnées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2083 m²HE/m² | 0,1875 à 0,2292 | code 24.07.05, « Zier- und Löschteich », Biotoptypenwert 5 sur 24 (ligne 242 de l'extraction) |

Correspondance retenue : Bassin d'agrément et réserve incendie.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 60, « Lakes - Ornamental lake or pond », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 61, « Lakes - Ornamental lake or pond », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 54, « Lakes - Ornamental lake or pond » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 54, « Lakes - Ornamental lake or pond » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 20,83 |
| État moyen | 18,23 |
| Mauvais état | 14,58 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,2 | 8,3 | 16,7 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 979 |
| moyen | 0 | 6,1 | 12,2 | 18,2 | 18,2 | 18,2 | 18,2 | 18,2 | 18,2 | 875 |
| mauvais | 0 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 714 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H021. VB.22 : Potager, jardin partagé, jardin familial

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.22 |
| EUNIS 2012 | I1.2 |
| EUNIS 2022 (HabRef) | V1-2 Cultures mixtes des jardins maraîchers et horticulture |
| CORINE Biotopes (HabRef) | 82.12 Cultures et maraichage |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Potager, jardin partagé ou jardin familial cultivé, avec ses allées, abris et bordures.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |

Correspondance retenue : Jardins familiaux et terres de jardinage riches en structures.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 1 ans | onglet G-4, ligne 59, « Urban - Allotments », condition cible bon |
| Création, état moyen visé | 1 ans | onglet G-4, ligne 59, « Urban - Allotments », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 59, « Urban - Allotments », condition cible mauvais |
| Amélioration, mauvais vers moyen | 1 ans | onglet G-5, ligne 60, « Urban - Allotments », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 1 ans | onglet G-5, ligne 60, « Urban - Allotments », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 1 ans | onglet G-5, ligne 60, « Urban - Allotments », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 83, « Urban - Allotments » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 83, « Urban - Allotments » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 2 246 |
| moyen | 0 | 40,1 | 40,1 | 40,1 | 40,1 | 40,1 | 40,1 | 40,1 | 40,1 | 1 965 |
| mauvais | 0 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 1 572 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H022. VB.23 : Jardinière, bac et plantation hors sol au niveau du sol

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.23 |
| EUNIS 2012 | J1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86 Villes, villages et sites industriels, 86.1 Villes, 86.2 Villages, 86.3 Sites industriels en activité |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | hors-sol (toiture ou bac) |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Plantations en bacs, jardinières ou caissons posés sur un sol revêtu, sans continuité avec le sol en place.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Antirrhinum majus, Asphodelus fistulosus, Bromus madritensis, Diplotaxis tenuifolia, Erysimum cheiri, Hyoscyamus albus, Lactuca serriola, Mercurialis annua, Micromeria juliana, Parietaria judaica, Sedum album, Verbascum undulatum, Capparis spinosa ssp. spinosa, Sonchus oleraceus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2639 m²HE/m² | 0,1319 à 0,3958 | onglet G-1, ligne 69, « Urban - Ground level planters », distinctivité 2 sur 8, multipliée par le rapport C-H3 |

Correspondance retenue : Aucun type BKompV : valeur transposée de la métrique anglaise (convention C-H3).

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 70, « Urban - Ground level planters », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 93, « Urban - Ground level planters » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 93, « Urban - Ground level planters » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 26,39 |
| État moyen | 23,09 |
| Mauvais état | 18,47 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 26,4 | 1 293 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H023. VB.24 : Bassin de rétention sec ou en eau, non paysager

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.24 |
| EUNIS 2012 | J5.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 89.2 Lagunes industrielles et canaux d'eau douce, 89.23 Lagunes industrielles et bassins ornementaux |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Bassin de rétention ou d'infiltration des eaux pluviales sans aménagement paysager, sec ou en eau, à berges talutées ou maçonnées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2083 m²HE/m² | 0,1875 à 0,2292 | code 24.07.08, « Offene Wasserrückhaltebecken », Biotoptypenwert 5 sur 24 (ligne 245 de l'extraction) |

Correspondance retenue : Bassin de rétention ouvert.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 77, « Urban - Sustainable drainage system », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 78, « Urban - Sustainable drainage system », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 100, « Urban - Sustainable drainage system » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 100, « Urban - Sustainable drainage system » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 20,83 |
| État moyen | 18,23 |
| Mauvais état | 14,58 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,8 | 5,6 | 11,2 | 14 | 14 | 14 | 14 | 14 | 656 |
| moyen | 0 | 4,1 | 8,1 | 12,2 | 12,2 | 12,2 | 12,2 | 12,2 | 12,2 | 586 |
| mauvais | 0 | 9,8 | 9,8 | 9,8 | 9,8 | 9,8 | 9,8 | 9,8 | 9,8 | 479 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H024. VB.25 : Voie ferrée, ballast

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.25 |
| EUNIS 2012 | J4.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 86.43 Voies de chemins de fer, gares de triage et autres espaces ouverts |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Plate-forme ferroviaire en service ou non, ballast et abords immédiats.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,0417 m²HE/m² | 0,0375 à 0,0458 | code 52.04.01, « Gleiskörper », Biotoptypenwert 1 sur 24 (ligne 768 de l'extraction) |

Correspondance retenue : Plate-forme ferroviaire.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 87, « Urban - Built linear features » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 87, « Urban - Built linear features » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 4,17 |
| État moyen | 3,65 |
| Mauvais état | 2,92 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H025. VB.26 : Prairie urbaine extensive, fauche tardive

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | VB.26 |
| EUNIS 2012 | E2.2 |
| EUNIS 2022 (HabRef) | R2-2 Prairies de fauche de basse et moyenne altitudes |
| CORINE Biotopes (HabRef) | 38.2 Prairies de fauche de basse altitude, 38.21 Prairies de fauche atlantiques, 38.22 Prairies de fauche des plaines médio-européennes, 38.23 Prairies de fauche submontagnardes médio-européennes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Prairie gérée par fauche tardive en milieu urbain ou périurbain, semée ou spontanée, à flore moyennement riche, sans fertilisation.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (113 taxons ; les 40 plus cités) : Arrhenatherum elatius, Trisetum flavescens, Alopecurus pratensis, Knautia arvensis, Pastinaca sativa, Trifolium dubium, Crepis biennis, Pimpinella major, Campanula patula, Dactylis glomerata, Geranium pratense, Leucanthemum vulgare, Sanguisorba officinalis, Festuca pratensis, Poa pratensis, Trifolium repens, Alchemilla xanthochlora, Bromus erectus, Festuca rubra, Daucus carota, Alopecurus rendlei, Alopecurus utriculatus, Geranium sylvaticum, Pimpinella saxifraga, Potentilla erecta, Ranunculus bulbosus, Anthriscus sylvestris, Heracleum sphondylium, Alopecurus sp., Deschampsia cespitosa, Filipendula ulmaria, Anthoxanthum odoratum, Holcus lanatus, Malva moschata, Sanguisorba minor, Arrhenatherum elatius ssp. bulbosum, Equisetum arvense, Galium album, Picris hieracioides, Medicago sativa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 34.07b.01, « Mäßig artenreiche, frische Mähwiese », Biotoptypenwert 15 sur 24 (ligne 341 de l'extraction) |

Correspondance retenue : Prairie de fauche fraîche moyennement riche en espèces : une prairie semée en ville n'atteint pas le type riche en espèces 34.07a.01, réservé à E2.2.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| Création, mauvais état visé | 2 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,2 | 12,5 | 25 | 56,2 | 62,5 | 62,5 | 62,5 | 62,5 | 2 781 |
| moyen | 0 | 10,9 | 21,9 | 43,8 | 54,7 | 54,7 | 54,7 | 54,7 | 54,7 | 2 570 |
| mauvais | 0 | 21,9 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 122 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.2 Eaux de surface continentales (EUNIS C)

#### Fiche H026. C1.1 : Lacs, étangs et mares oligotrophes permanents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.1 |
| EUNIS 2012 | C1.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.11 Eaux oligotrophes pauvres en calcaire, 22.15 Eaux oligo-mésotrophes riches en calcaire, 22.4 Végétations aquatiques, 22.42 Végétations enracinées immergées, 22.421 Groupements de grands Potamots, 22.422 Groupements de petits Potamots, 22.43 Végétations enracinées flottantes, 22.433 Groupements oligotrophes de Potamots, 22.44 Tapis immergés de Characées, 22.441 Tapis de Chara, et 2 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Plans d'eau pauvres en nutriments (azote, phosphore), le plus souvent acides (pH 4 à 6), y compris les eaux calcaires oligotrophes non polluées où se développent des characées. Les herbiers de Callitriche, de potamots et d'isoètes y sont souvent clairsemés. Les eaux tourbeuses dystrophes relèvent de C1.4.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (25 taxons ; les 40 plus cités) : Potamogeton sp., Sparganium minimum, Callitriche sp., Chara sp., Nitella sp., Utricularia bremii, Utricularia intermedia, Utricularia minor, Utricularia ochroleuca, Sphagnum sp., Scorpidium scorpioides, Apium inundatum, Luronium natans, Potamogeton alpinus, Potamogeton gramineus, Potamogeton oblongus, Potamogeton polygonifolius, Ranunculus ololeucos, Ranunculus omiophyllus, Ranunculus tripartitus, Sparganium sp., Lamprothamnium sp., Nitellopsis sp., Lychnothamnus sp., Tolypella sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 24.02a, « Natürliche oligotrophe Gewässer », Biotoptypenwert 22 sur 24 (ligne 223 de l'extraction) |

Correspondance retenue : Eaux stagnantes oligotrophes naturelles.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 42, « Lakes - Low alkalinity lakes », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 43, « Lakes - Low alkalinity lakes », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 56, « Lakes - Low alkalinity lakes » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 56, « Lakes - Low alkalinity lakes » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1 | 2 | 4 | 9,1 | 14,1 | 19,2 | 29,2 | 30,3 | 1 044 |
| moyen | 0 | 2,6 | 5,3 | 10,6 | 23,8 | 26,5 | 26,5 | 26,5 | 26,5 | 1 178 |
| mauvais | 0 | 4,2 | 8,5 | 16,9 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 995 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H027. C1.2 : Lacs, étangs et mares mésotrophes permanents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.2 |
| EUNIS 2012 | C1.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.12 Eaux mésotrophes, 22.4 Végétations aquatiques, 22.41 Végétations flottant librement, 22.411 Couvertures de Lemnacées, 22.412 Radeaux d'Hydrocharis, 22.413 Radeaux de Stratiotes, 22.414 Colonies d'Utriculaires, 22.415 Couvertures de Salvinia, 22.416 Groupements à Aldrovanda, 22.42 Végétations enracinées immergées, et 13 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Lacs et mares aux eaux assez riches en nutriments et en bases dissoutes (pH souvent 6 à 7). Beaucoup de lacs et d'étangs de plaine non pollués sont naturellement mésotrophes et portent des herbiers denses, qui disparaissent quand l'eau se pollue.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (78 taxons ; les 40 plus cités) : Nymphaea alba, Nymphaea sp., Polygonum amphibium, Hydrocharis morsus-ranae, Azolla sp., Lemna sp., Riccia sp., Spirodela sp., Wolffia sp., Ricciocarpus sp., Zannichellia palustris, Potamogeton sp., Nuphar lutea, Nymphoides peltata, Potamogeton natans, Trapa natans, Nuphar sp., Ceratophyllum sp., Salvinia natans, Nymphaea candida, Nymphaea pygmaea, Nymphaea tetragona, Scorpidium scorpioides, Sparganium minimum, Utricularia intermedia, Utricularia minor, Utricularia ochroleuca, Sphagnum sp., Utricularia bremii, Ceratophyllum submersum, Elodea canadensis, Myriophyllum spicatum, Najas marina, Elodea nuttallii, Callitriche palustris, Batrachium sp., Ranunculus sp., Nymphoides sp., Nymphoides indica, Nuphar pumila.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 24.03b, « Sonstige natürliche mesotrophe Gewässer », Biotoptypenwert 19 sur 24 (ligne 227 de l'extraction) |

Correspondance retenue : Autres eaux mésotrophes naturelles.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 44, « Lakes - Moderate alkalinity lakes », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 45, « Lakes - Moderate alkalinity lakes », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 58, « Lakes - Moderate alkalinity lakes » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 58, « Lakes - Moderate alkalinity lakes » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,5 | 7,8 | 12,2 | 16,5 | 25,3 | 26,1 | 901 |
| moyen | 0 | 2,3 | 4,6 | 9,1 | 20,6 | 22,9 | 22,9 | 22,9 | 22,9 | 1 017 |
| mauvais | 0 | 3,7 | 7,3 | 14,6 | 18,3 | 18,3 | 18,3 | 18,3 | 18,3 | 860 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H028. C1.3 : Lacs, étangs et mares eutrophes permanents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.3 |
| EUNIS 2012 | C1.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.13 Eaux eutrophes, 22.4 Végétations aquatiques, 22.41 Végétations flottant librement, 22.411 Couvertures de Lemnacées, 22.412 Radeaux d'Hydrocharis, 22.413 Radeaux de Stratiotes, 22.414 Colonies d'Utriculaires, 22.415 Couvertures de Salvinia, 22.416 Groupements à Aldrovanda, 22.42 Végétations enracinées immergées, et 10 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Lacs et mares aux eaux grises ou vert-bleu plus ou moins troubles, très riches en nutriments et en bases (pH le plus souvent supérieur à 7). Une eutrophie modérée permet des herbiers denses, qui disparaissent si la charge en nutriments augmente encore.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (43 taxons ; les 40 plus cités) : Callitriche sp., Hottonia palustris, Chlorophyta sp., Bacillariophyta sp., Myriophyllum spicatum, Ceratophyllum submersum, Lemna minor, Salvinia natans, Spirodela polyrhiza, Stratiotes aloides, Wolffia arrhiza, Cladocera sp., Chrysophyta sp., Euglenophyta sp., Rotatoria sp., Pyrrophyta sp., Copepoda sp., Ceratophyllum demersum, Lemna trisulca, Nuphar lutea, Nymphaea alba, Nymphoides peltata, Persicaria amphibia, Trapa natans, Myriophyllum verticillatum, Najas marina, Najas minor, Potamogeton sp., Cyanobacteriophyta sp., Ranunculus aquatilis, Ranunculus baudotii, Ranunculus hederaceus, Ranunculus ololeucos, Ranunculus omiophyllus, Ranunculus peltatus, Ranunculus trichophyllus, Ranunculus tripartitus, Ranunculus lenormandi, Ranunculus confervoides, Ranunculus rionii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 24.04b, « Sonstige natürliche eutrophe Gewässer », Biotoptypenwert 16 sur 24 (ligne 231 de l'extraction) |

Correspondance retenue : Autres eaux eutrophes naturelles.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,3 | 13,9 | 21,3 | 22 | 759 |
| moyen | 0 | 1,9 | 3,9 | 7,7 | 17,3 | 19,3 | 19,3 | 19,3 | 19,3 | 857 |
| mauvais | 0 | 3,1 | 6,2 | 12,3 | 15,4 | 15,4 | 15,4 | 15,4 | 15,4 | 724 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H029. C1.4 : Lacs, étangs et mares permanents dystrophes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.4 |
| EUNIS 2012 | C1.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.14 Eaux dystrophes, 22.4 Végétations aquatiques, 22.42 Végétations enracinées immergées, 22.421 Groupements de grands Potamots, 22.422 Groupements de petits Potamots, 22.43 Végétations enracinées flottantes, 22.431 Tapis flottant de végétaux à grandes feuilles, 22.4311 Tapis de Nénuphars, 22.4312 Tapis de chataîgnes d'eau, 22.4313 Tapis de Nymphoides, et 11 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Lacs et mares aux eaux acides riches en humus, souvent teintées de brun (pH souvent 3 à 5).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (20 taxons ; les 40 plus cités) : Sparganium minimum, Utricularia sp., Chara sp., Nitella sp., Nitellopsis sp., Tolypella sp., Lychnothamnus sp., Lamprothamnium sp., Carex flava, Carex rostrata, Eriophorum vaginatum, Parnassia palustris, Scirpus hudsonianus, Eriophorum angustifolium, Potamogeton sp., Campylium stellatum, Scorpidium scorpioides, Sparganium natans, Sphagnum sp., Nymphaea sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 24.01a, « Natürliche dystrophe Gewässer », Biotoptypenwert 20 sur 24 (ligne 220 de l'extraction) |

Correspondance retenue : Eaux dystrophes naturelles.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 45, « Lakes - Peat lakes », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 46, « Lakes - Peat lakes », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 59, « Lakes - Peat lakes » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 59, « Lakes - Peat lakes » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,7 | 8,2 | 12,8 | 17,4 | 26,6 | 27,5 | 949 |
| moyen | 0 | 2,4 | 4,8 | 9,6 | 21,7 | 24,1 | 24,1 | 24,1 | 24,1 | 1 071 |
| mauvais | 0 | 3,8 | 7,7 | 15,4 | 19,2 | 19,2 | 19,2 | 19,2 | 19,2 | 905 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H030. C1.5 : Lacs, étangs et mares continentaux salés et saumâtres permanents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.5 |
| EUNIS 2012 | C1.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 23.1 Eaux saumâtres ou salées sans végétation, 23.11 Eau libre sans tapis de Charophytes, 23.12 Tapis algual de Charophyte, 23.2 Eaux saumâtres ou salées végétalisées, 23.21 Formations immergées des eaux saumâtres ou salées, 23.211 Groupements à Ruppia |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Lacs, étangs et mares saumâtres, salés ou hypersalés éloignés du littoral, avec leur plancton et leur faune pélagique.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (18 taxons ; les 40 plus cités) : Potamogeton pectinatus, Callitriche sp., Lemna sp., Wolffia sp., Potamogeton crispus, Ruppia maritima, Najas sp., Zannichellia sp., Ranunculus baudotii, Ranunculus rionii, Ranunculus sp., Zostera noltii, Najas minor, Ranunculus trichophyllus, Utricularia neglecta, Najas marina, Zannichellia pedicellata, Chara sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 24.06.01, « Salzhaltiges, perennierendes, stehendes Gewässer (Binnenlandsalzstellen) », Biotoptypenwert 21 sur 24 (ligne 235 de l'extraction) |

Correspondance retenue : Eau stagnante salée pérenne de l'intérieur.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 41, « Lakes - High alkalinity lakes », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 42, « Lakes - High alkalinity lakes », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 55, « Lakes - High alkalinity lakes » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1 | 1,9 | 3,9 | 8,7 | 13,5 | 18,3 | 27,9 | 28,9 | 996 |
| moyen | 0 | 2,5 | 5,1 | 10,1 | 22,7 | 25,3 | 25,3 | 25,3 | 25,3 | 1 124 |
| mauvais | 0 | 4 | 8,1 | 16,2 | 20,2 | 20,2 | 20,2 | 20,2 | 20,2 | 950 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H031. C1.6 : Lacs, étangs et mares temporaires

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C1.6 |
| EUNIS 2012 | C1.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.4 Végétations aquatiques, 22.43 Végétations enracinées flottantes, 22.432 Communautés flottantes des eaux peu profondes, 22.433 Groupements oligotrophes de Potamots, 22.5 Masses d'eau temporaires |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Plans d'eau douce, ou parties de plans d'eau, qui s'assèchent périodiquement, avec leurs communautés animales et algales. Les végétations de la phase sèche relèvent de C3.5 à C3.7.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (4 taxons ; les 40 plus cités) : Ceratophyllum demersum, Najas marina, Ranunculus trichophyllus, Najas minor.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 24.09a, « Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) », Biotoptypenwert 19 sur 24 (ligne 256 de l'extraction) |

Correspondance retenue : Eaux stagnantes temporaires naturelles.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 10,6 | 21,2 | 42,4 | 53 | 53 | 53 | 53 | 53 | 2 493 |
| moyen | 0 | 15,5 | 30,9 | 46,4 | 46,4 | 46,4 | 46,4 | 46,4 | 46,4 | 2 228 |
| mauvais | 0 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 1 819 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H032. C2.1 : Sources, ruisseaux de sources

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.1 |
| EUNIS 2012 | C2.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 24.1 Lits des rivières, 24.11 Ruisselets, 24.4 Végétation immergée des rivières, 24.41 Végétation des rivières oligotrophes acidiphiles, 24.42 Végétation des rivières oligotrophes riches en calcaire, 24.43 Végétation des rivières mésotrophes, 24.44 Végétation des rivières eutrophes, 54.1 Sources, 54.11 Sources d'eaux douces pauvres en bases, 54.12 Sources d'eaux dures, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Sources et résurgences, avec les communautés animales et végétales liées à leur microclimat et à leur régime hydrique particuliers. Les sources noyées dans une végétation de bas-marais relèvent de D2.2 ou D4.1.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (56 taxons ; les 40 plus cités) : Bryum pseudotriquetrum, Conocephalum conicum, Fontinalis antipyretica, Ranunculus trichophyllus, Ranunculus fluitans, Eucladium verticillatum, Cratoneuron commutatum, Arabis soyeri, Cochlearia pyrenaica, Saxifraga aizoides, Viola biflora, Palustriella commutata, Callitriche hamulata, Littorella uniflora, Montia fontana, Myriophyllum alterniflorum, Potamogeton filiformis, Ranunculus confervoides, Scirpus fluitans, Juncus bulbosus, Potamogeton polygonifolius, Ranunculus aquatilis var. diffusus, Callitriche obtusangula, Nuphar lutea, Potamogeton crispus, Potamogeton nodosus, Potamogeton pectinatus, Ranunculus circinatus, Sagittaria sagittifolia, Zannichellia palustris f. fluviatilis, Potamogeton lucens, Sparganium emersum, Nymphaea lotus, Berula erecta, Callitriche stagnalis, Callitriche truncata, Groenlandia densa, Myriophyllum spicatum, Nymphaea alba, Potamogeton natans.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 22.02, « Grundquellen (Limnokrenen) », Biotoptypenwert 22 sur 24 (ligne 179 de l'extraction) |

Correspondance retenue : Sources limnocrènes ; aucune ligne surfacique anglaise pour les cours d'eau (module rivières distinct) : délai et difficulté de la mare prioritaire (convention C-H4).

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 12,3 | 24,6 | 49,1 | 61,4 | 61,4 | 61,4 | 61,4 | 61,4 | 2 887 |
| moyen | 0 | 17,9 | 35,8 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 2 580 |
| mauvais | 0 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 2 107 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H033. C2.2 : Cours d'eau permanents à écoulement rapide

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.2 |
| EUNIS 2012 | C2.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 24.1 Lits des rivières, 24.12 Zone à Truites, 24.13 Zone à Ombres, 24.4 Végétation immergée des rivières, 24.41 Végétation des rivières oligotrophes acidiphiles, 24.42 Végétation des rivières oligotrophes riches en calcaire, 24.43 Végétation des rivières mésotrophes, 24.44 Végétation des rivières eutrophes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Cours d'eau permanents à courant rapide et turbulent : ruisseaux, torrents, cascades, rapides, sur fond de roches, de pierres ou de graviers. Les îlots et bancs exondés relèvent de C3.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (48 taxons ; les 40 plus cités) : Ranunculus fluitans, Fontinalis antipyretica, Ranunculus trichophyllus, Diptera sp., Ephemeroptera sp., Plecoptera sp., Trichoptera sp., Bryophyta sp., Rhodophyta sp., Chlorophyta sp., Bacillariophyta sp., Turbellaria sp., Cyanophycaea sp., Chara hispida, Potamogeton coloratus, Callitriche obtusangula, Nuphar lutea, Potamogeton crispus, Potamogeton lucens, Potamogeton nodosus, Ranunculus circinatus, Sagittaria sagittifolia, Sparganium emersum, Zannichellia palustris f. fluviatilis, Potamogeton pectinatus, Berula erecta, Callitriche stagnalis, Callitriche truncata, Groenlandia densa, Nymphaea alba, Potamogeton natans, Potamogeton perfoliatus, Ranunculus aquatilis, Ranunculus penicillatus, Mentha aquatica f. submersa, Myriophyllum spicatum, Ranunculus peltatus, Sium erectum, Callitriche hamulata, Juncus bulbosus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |

Correspondance retenue : Cours d'eau naturels ; délai et difficulté par la convention C-H4.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 12,3 | 24,6 | 49,1 | 61,4 | 61,4 | 61,4 | 61,4 | 61,4 | 2 887 |
| moyen | 0 | 17,9 | 35,8 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 2 580 |
| mauvais | 0 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 2 107 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H034. C2.3 : Cours d'eau permanents à débit régulier

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.3 |
| EUNIS 2012 | C2.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 24.1 Lits des rivières, 24.14 Zone à Barbeaux, 24.15 Zone à Brèmes, 24.4 Végétation immergée des rivières, 24.43 Végétation des rivières mésotrophes, 24.44 Végétation des rivières eutrophes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Cours d'eau permanents à courant lent ou laminaire, sur fond de sable ou de vase. Les îlots et bancs exondés relèvent de C3.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (26 taxons ; les 40 plus cités) : Ranunculus fluitans, Fontinalis antipyretica, Callitriche obtusangula, Nuphar lutea, Potamogeton crispus, Potamogeton lucens, Potamogeton nodosus, Potamogeton pectinatus, Ranunculus circinatus, Sagittaria sagittifolia, Sparganium emersum, Zannichellia palustris f. fluviatilis, Berula erecta, Callitriche stagnalis, Callitriche truncata, Groenlandia densa, Myriophyllum spicatum, Nymphaea alba, Potamogeton perfoliatus, Ranunculus aquatilis, Ranunculus peltatus, Ranunculus penicillatus, Ranunculus trichophyllus, Sium erectum, Mentha aquatica f. submersa, Potamogeton natans.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |

Correspondance retenue : Cours d'eau naturels ; délai et difficulté par la convention C-H4.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 12,3 | 24,6 | 49,1 | 61,4 | 61,4 | 61,4 | 61,4 | 61,4 | 2 887 |
| moyen | 0 | 17,9 | 35,8 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 2 580 |
| mauvais | 0 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 2 107 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H035. C2.4 : Fleuves et rivières tidaux en amont de l'estuaire

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.4 |
| EUNIS 2012 | C2.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 13.1 Fleuves et rivières soumis à marées, 13.11 Eau saumâtre des cours d'eau soumis à marées, 13.12 Eau douce des cours d'eau soumis à marées, 24.4 Végétation immergée des rivières, 24.43 Végétation des rivières mésotrophes, 24.44 Végétation des rivières eutrophes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Parties des cours d'eau soumises à la marée, en amont de l'estuaire.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (26 taxons ; les 40 plus cités) : Ranunculus fluitans, Callitriche obtusangula, Nuphar lutea, Potamogeton crispus, Potamogeton lucens, Potamogeton nodosus, Potamogeton pectinatus, Ranunculus circinatus, Sagittaria sagittifolia, Sparganium emersum, Zannichellia palustris f. fluviatilis, Fontinalis antipyretica, Berula erecta, Callitriche stagnalis, Callitriche truncata, Groenlandia densa, Myriophyllum spicatum, Nymphaea alba, Potamogeton natans, Potamogeton perfoliatus, Ranunculus aquatilis, Ranunculus peltatus, Ranunculus penicillatus, Ranunculus trichophyllus, Sium erectum, Mentha aquatica f. submersa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 23.01, « Natürliche und naturnahe Fließgewässer », Biotoptypenwert 22 sur 24 (ligne 184 de l'extraction) |

Correspondance retenue : Cours d'eau naturels ; délai et difficulté par la convention C-H4.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 12,3 | 24,6 | 49,1 | 61,4 | 61,4 | 61,4 | 61,4 | 61,4 | 2 887 |
| moyen | 0 | 17,9 | 35,8 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 53,7 | 2 580 |
| mauvais | 0 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 2 107 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H036. C2.5 : Eaux courantes temporaires

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.5 |
| EUNIS 2012 | C2.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 24.1 Lits des rivières, 24.16 Cours d'eau intermittents |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Cours d'eau qui cessent de couler une partie de l'année, laissant un lit sec ou des vasques. La phase sèche relève de C3.5 à C3.7.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 23.09, « Natürliche und naturnahe temporäre Fließgewässer », Biotoptypenwert 20 sur 24 (ligne 217 de l'extraction) |

Correspondance retenue : Cours d'eau temporaires naturels.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 11,2 | 22,3 | 44,7 | 55,8 | 55,8 | 55,8 | 55,8 | 55,8 | 2 624 |
| moyen | 0 | 16,3 | 32,6 | 48,9 | 48,9 | 48,9 | 48,9 | 48,9 | 48,9 | 2 345 |
| mauvais | 0 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 915 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H037. C2.6 : Films d'eau sur les marges rocheuses d'un cours d'eau

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C2.6 |
| EUNIS 2012 | C2.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Eau courante qui ne suit pas un lit mais suinte sur les rochers.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 23.07.01, « Wasserfall », Biotoptypenwert 21 sur 24 (ligne 209 de l'extraction) |

Correspondance retenue : Cascade ; délai et difficulté par la convention C-H4.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 46, « Lakes - Ponds (priority habitat) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 47, « Lakes - Ponds (priority habitat) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 61, « Lakes - Ponds (priority habitat) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 11,7 | 23,5 | 46,9 | 58,6 | 58,6 | 58,6 | 58,6 | 58,6 | 2 755 |
| moyen | 0 | 17,1 | 34,2 | 51,3 | 51,3 | 51,3 | 51,3 | 51,3 | 51,3 | 2 462 |
| mauvais | 0 | 41 | 41 | 41 | 41 | 41 | 41 | 41 | 41 | 2 011 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H038. C3.1 : Formations à hélophytes riches en espèces

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.1 |
| EUNIS 2012 | C3.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.4 Bordures à Calamagrostis des eaux courantes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Végétations de bordure des lacs, rivières et ruisseaux, de composition mélangée.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (15 taxons ; les 40 plus cités) : Apium nodiflorum, Apium repens, Catabrosa aquatica, Glyceria declinata, Glyceria fluitans, Glyceria plicata, Leersia oryzoides, Nasturtium officinale, Sium erectum, Sparganium microcarpum, Sparganium neglectum, Veronica beccabunga, Nasturtium microphyllum, Veronica anagallis-aquatica, Glyceria nemoralis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |

Correspondance retenue : Autre roselière.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| Création, mauvais état visé | 3 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 12 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,7 | 7,4 | 14,9 | 33,5 | 44,7 | 44,7 | 44,7 | 44,7 | 1 943 |
| moyen | 0 | 5,6 | 11,2 | 22,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 798 |
| mauvais | 0 | 10,4 | 20,8 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 501 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H039. C3.2 : Roselières et formations de bordure à grands hélophytes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.2 |
| EUNIS 2012 | C3.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.1 Roselières, 53.11 Phragmitaies, 53.111 Phragmitaies inondées, 53.113 Phagmitaies géantes, 53.12 Scirpaies lacustres, 53.13 Typhaies, 53.14 Roselières basses, 53.141 Communautés de Sagittaires, 53.142 Communautés à Rubanier négligé, 53.143 Communautés à Rubanier rameux, et 24 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Ceintures de grands hélophytes au bord des plans d'eau et des cours d'eau, pauvres en espèces et souvent dominées par une seule : laîches, marisque, prêle des eaux, glycérie aquatique, roseau, sagittaire, scirpes, rubaniers, massettes. Les roselières terrestres sans eau libre relèvent de D5.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (64 taxons ; les 40 plus cités) : Phragmites australis, Equisetum fluviatile, Hippuris vulgaris, Sagittaria sagittifolia, Acorus calamus, Cladium mariscus, Calamagrostis canescens, Carex elata, Leersia sp., Calamagrostis sp., Glyceria sp., Glyceria maxima, Typha angustifolia, Typha latifolia, Typha sp., Phragmites sp., Rorippa amphibia, Oenanthe aquatica, Sparganium sp., Eleocharis palustris, Sparganium neglectum, Potentilla anserina, Tripolium pannonicum, Bolboschoenus maritimus ssp. compactus, Puccinellia limosa, Cirsium brachycephalum, Carex acutiformis, Carex paniculata, Mentha aquatica, Phalaris arundinacea, Sparganium emersum, Caltha membranacea, Sagittaria natans, Juncus gerardi, Juncus maritimus, Schoenoplectus tabernaemontani, Scirpus litoralis, Scirpus maritimus, Scirpus pungens, Scirpus tabernaemontani.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 38.02.01, « Schilf-Wasserröhricht », Biotoptypenwert 19 sur 24 (ligne 390 de l'extraction) |

Correspondance retenue : Roselière aquatique à roseau.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| Création, mauvais état visé | 3 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 12 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,4 | 8,8 | 17,7 | 39,8 | 53 | 53 | 53 | 53 | 2 307 |
| moyen | 0 | 6,6 | 13,3 | 26,5 | 46,4 | 46,4 | 46,4 | 46,4 | 46,4 | 2 135 |
| mauvais | 0 | 12,4 | 24,8 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 37,1 | 1 782 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H040. C3.3 : Formations riveraines à grandes cannes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.3 |
| EUNIS 2012 | C3.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.6 Formations riveraines de Cannes, 53.61 Communautés avec les Cannes de Ravenne, 53.62 Peuplements de Cannes de Provence |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Ceintures méditerranéennes de grandes cannes (canne de Provence, canne de Ravenne) le long des cours d'eau et des plans d'eau permanents ou temporaires.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (9 taxons ; les 40 plus cités) : Arundo donax, Saccharum ravennae, Erianthus ravennae, Imperata cylindrica, Saccharum spontaneum, Hemarthria altissima, Arundo plinii, Saccharum aegyptiacum, Saccharum strictum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |

Correspondance retenue : Autre roselière.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| Création, mauvais état visé | 3 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 12 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,7 | 7,4 | 14,9 | 33,5 | 44,7 | 44,7 | 44,7 | 44,7 | 1 943 |
| moyen | 0 | 5,6 | 11,2 | 22,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 798 |
| mauvais | 0 | 10,4 | 20,8 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 501 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H041. C3.4 : Végétations amphibies lentes, pauvres en espèces

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.4 |
| EUNIS 2012 | C3.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 16 Dunes côtières et plages de sable, 16.3 Lettes dunaires humides (= Pannes humides, = Dépressions humides intradunales), 16.32 Gazons pionniers des lettes ou pannes humides, 22.3 Communautés amphibies, 22.31 Communautés amphibies pérennes septentrionales, 22.311 Gazons de Littorelles, étangs à Lobélies, gazons d'Isoètes, 22.3111 Gazons de Littorelles, 22.3112 Etangs à Lobélies, 22.3113 Gazons d'Isoètes euro-sibériens, 22.3114 Communautés flottantes de Sparganium, et 19 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Végétations amphibies pauvres en espèces et à croissance lente : gazons d'isoètes des rives oligotrophes, cressonnières des ruisseaux, gazons méditerranéens de petits scirpes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (113 taxons ; les 40 plus cités) : Littorella uniflora, Pilularia globulifera, Lobelia dortmanna, Cyperus flavescens, Elatine hungarica, Isoetes sp., Eleocharis acicularis, Samolus valerandi, Elatine sp., Cyperus fuscus, Cyperus michelianus, Juncus bufonius, Sparganium angustifolium, Ranunculus reptans, Deschampsia setacea, Eleocharis multicaulis, Juncus bulbosus, Ranunculus flammula, Scirpus fluitans, Hippuris vulgaris, Isoetes azorica, Lythrum hyssopifolia, Marsilea quadrifolia, Elatine triandra, Scirpus sp., Pilularia sp., Blackstonia perfoliata, Damasonium bourgaei, Elatine macropoda, Laurentia gasparrinii, Laurentia tenella, Morisia monanthos, Myosurus minimus, Nananthea perpusilla, Elatine gussonei, Radiola linoides, Elatine pedunculata, Echinochloa crus-galli, Filaginella uliginosa, Gnaphalium uliginosum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 24.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 18 sur 24 (ligne 254 de l'extraction) |

Correspondance retenue : Milieux exondés temporairement au bord des eaux stagnantes, forme naturelle.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 10,1 | 20,1 | 40,2 | 50,2 | 50,2 | 50,2 | 50,2 | 50,2 | 2 362 |
| moyen | 0 | 14,7 | 29,3 | 44 | 44 | 44 | 44 | 44 | 44 | 2 110 |
| mauvais | 0 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 1 724 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H042. C3.5 : Berges périodiquement inondées à végétation pionnière

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.5 |
| EUNIS 2012 | C3.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.3 Communautés amphibies, 22.32 Gazons amphibies annuels septentrionaux, 22.321 Communautés à Eleocharis, 22.322 Gazons de plantes pionnières des lettes dunaires, 22.323 Communautés naines à Juncus bufonius, 22.3231 Gazons à Juncus bufonius, 22.3232 Gazons à petits Souchets, 22.3233 Communautés d'herbes naines des substrats humides, 22.33 Groupements à Bidens tripartitus, 24.2 Bancs de graviers des cours d'eau, et 7 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | EM1 (mares et plans d'eau) |

**Définition**

Rives et fonds exondés vaseux, sableux ou graveleux des lacs et des rivières, à couvert modéré de plantes annuelles (bidents, souchets, renouées) développées pendant l'exondation, et de vivaces tolérant une immersion temporaire.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (77 taxons ; les 40 plus cités) : Juncus bufonius, Calamagrostis pseudophragmites, Bidens sp., Cyperus flavescens, Cyperus fuscus, Erucastrum nasturtiifolium, Salix elaeagnos, Epilobium dodonaei, Chenopodium sp., Polygonum sp., Salix purpurea, Agrostis gigantea, Hieracium piloselloides, Myricaria germanica, Blackstonia perfoliata, Centaurium pulchellum, Samolus valerandi, Rorippa sp., Xanthium sp., Poa trivialis, Caltha palustris ssp. laeta, Thlaspietea rotundifolii, Carex bohemica, Coleanthus subtilis, Elatine hexandra, Elatine hydropiper, Juncus tenageia, Limosella aquatica, Lindernia procumbens, Peplis portula, Scirpus supinus, Eleocharis ovata, Eleocharis carniolica, Aethionema saxatile, Buphthalmum salicifolium, Chondrilla chondrilloides, Conyza canadensis, Erigeron acer, Euphorbia cyparissias, Gypsophila repens.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 24.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 18 sur 24 (ligne 254 de l'extraction) |

Correspondance retenue : Milieux exondés temporairement au bord des eaux stagnantes, forme naturelle.

**Grille d'état EM1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Eau claire, sans signe évident de pollution | non |
| B | Habitat semi-naturel sur au moins 10 m tout autour de la mare | non |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface | non |
| D | Pas de raccordement artificiel à d'autres plans d'eau (fossés agricoles, canalisations) | non |
| E | Niveau d'eau libre de fluctuer naturellement, sans barrage, pompe ni canalisation | non |
| F | Absence d'espèces végétales et animales exotiques envahissantes | non |
| G | Pas d'empoissonnement artificiel | non |
| H | Plantes émergées, immergées ou flottantes (lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur | non |
| I | Surface en eau ombragée à 50 % au plus par les arbres et fourrés voisins | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 49, « Lakes - Temporary lakes ponds and pools (H3170) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 50, « Lakes - Temporary lakes ponds and pools (H3170) », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 63, « Lakes - Temporary lakes ponds and pools (H3170) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 10,1 | 20,1 | 40,2 | 50,2 | 50,2 | 50,2 | 50,2 | 50,2 | 2 362 |
| moyen | 0 | 14,7 | 29,3 | 44 | 44 | 44 | 44 | 44 | 44 | 2 110 |
| mauvais | 0 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 1 724 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H043. C3.6 : Berges nues ou clairsemées à sédiments meubles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.6 |
| EUNIS 2012 | C3.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 22.2 Galets ou vasières non végétalisés, 24.2 Bancs de graviers des cours d'eau, 24.21 Bancs de graviers sans végétation, 24.3 Bancs de sable des rivières, 24.31 Bancs de sable des rivières sans végétation, 24.32 Bancs de sable riverains pourvus de végétation, 24.5 Dépôts d'alluvions fluviatiles limoneuses, 24.51 Dépôts nus d'alluvions fluviatiles limoneuses |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Bancs de sable, de graviers et de vase dans ou au bord des rivières, graviers des torrents, fonds vaseux de rivières et de lacs asséchés, y compris salés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Bidens sp., Polygonum sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 23.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 20 sur 24 (ligne 215 de l'extraction) |

Correspondance retenue : Milieux exondés temporairement au bord des eaux courantes, forme naturelle.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 16,7 | 33,3 | 66,7 | 83,3 | 83,3 | 83,3 | 83,3 | 83,3 | 3 917 |
| moyen | 0 | 24,3 | 48,6 | 72,9 | 72,9 | 72,9 | 72,9 | 72,9 | 72,9 | 3 500 |
| mauvais | 0 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 858 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H044. C3.7 : Berges nues ou clairsemées à sédiments non mobiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.7 |
| EUNIS 2012 | C3.7 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | eau |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Rochers, dalles et blocs exondés périodiquement au bord des rivières et des lacs et dans la zone de marnage des retenues.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 23.08a.01, « – Natürliche oder naturnahe Ausprägung », Biotoptypenwert 20 sur 24 (ligne 215 de l'extraction) |

Correspondance retenue : Milieux exondés temporairement au bord des eaux courantes, forme naturelle.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 16,7 | 33,3 | 66,7 | 83,3 | 83,3 | 83,3 | 83,3 | 83,3 | 3 917 |
| moyen | 0 | 24,3 | 48,6 | 72,9 | 72,9 | 72,9 | 72,9 | 72,9 | 72,9 | 3 500 |
| mauvais | 0 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 858 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H045. C3.8 : Habitats continentaux dépendant de la bruine

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | C3.8 |
| EUNIS 2012 | C3.8 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Abords de vasques sous les cascades, aspergés en permanence par les embruns d'eau douce.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 22.03, « Sturzquellen (Rheokrenen) (inkl. Kalktuff-Sturzquelle) », Biotoptypenwert 22 sur 24 (ligne 180 de l'extraction) |

Correspondance retenue : Sources rhéocrènes.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,9 | 3,8 | 8,5 | 13,2 | 18 | 27,4 | 30,3 | 1 013 |
| moyen | 0 | 1,3 | 2,6 | 5,3 | 11,9 | 18,5 | 25,1 | 26,5 | 26,5 | 1 046 |
| mauvais | 0 | 2,1 | 4,2 | 8,5 | 19,1 | 21,2 | 21,2 | 21,2 | 21,2 | 942 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.3 Tourbières hautes et bas-marais (EUNIS D)

#### Fiche H046. D1.1 : Tourbières hautes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D1.1 |
| EUNIS 2012 | D1.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.93 Bois marécageux de Bouleaux et de piment royal, 51 Tourbières hautes, 51.1 Tourbières hautes à peu près naturelles, 51.11 Buttes, bourrelets et pelouses tourbeuses, 51.111 Buttes de Sphaignes colorées (bulten), 51.1111 Buttes de Sphagnum magellanicum, 51.1112 Buttes de Sphagnum fuscum, 51.1113 Couronnes de buttes à Sphagnum rubellum, 51.1114 Buttes de Sphagnum rubellum, et 20 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Tourbières bombées très pauvres en nutriments et très acides, alimentées seulement par la pluie, dont la tourbe est faite surtout de sphaignes. Leur surface associe buttes, gouilles et végétations de sphaignes, de linaigrette engainante, de canneberge, d'andromède et de rossolis. Elles abritent une faune spécialisée (libellules, papillons, araignées) et des espèces rares aux populations fragmentées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (86 taxons ; les 40 plus cités) : Eriophorum vaginatum, Eriophorum sp., Sphagnum rubellum, Sphagnum magellanicum, Sphagnum papillosum, Sphagnum fuscum, Erica tetralix, Sphagnum balticum, Vaccinium oxycoccos, Scirpus cespitosus, Ledum palustre, Sphagnum recurvum, Sphagnum tenellum, Andromeda polifolia, Drosera rotundifolia, Betula nana, Rubus chamaemorus, Chamaedaphne calyculata, Sphagnum angustifolium, Empetrum hermaphroditum, Sphagnum cuspidatum, Carex pauciflora, Eriophorum angustifolium, Sphagnum capillifolium var. rubellum, Calluna vulgaris, Myrica gale, Sphagnum sp., Sphagnum capillifolium, Sphagnum capillifolium var. capillifolium, Carex paupercula, Rhynchospora alba, Scheuchzeria palustris, Molinia caerulea, Sphagnum pulchrum, Vaccinium uliginosum, Vaccinium sp., Sphagnum fallax, Vaccinium microcarpum, Sphagnum warnstorfii, Erica sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 1 m²HE/m² | 0,9 à 1 | code 36.01, « Hochmoore (weitgehend intakt) », Biotoptypenwert 24 sur 24 (ligne 374 de l'extraction) |

Correspondance retenue : Tourbières hautes intactes.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 85, « Wetland - Lowland raised bog », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 86, « Wetland - Lowland raised bog », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 106, « Wetland - Lowland raised bog » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 106, « Wetland - Lowland raised bog » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 100 |
| État moyen | 87,5 |
| Mauvais état | 70 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 50 m²HE, 15 à 30 cm 60 m²HE, 30 à 80 cm 70 m²HE, 80 cm et plus 90 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,2 | 2,8 | 4,4 | 5,9 | 9,1 | 10 | 335 |
| moyen | 0 | 0,3 | 0,6 | 1,2 | 2,6 | 4,1 | 5,5 | 8,5 | 8,8 | 302 |
| mauvais | 0 | 0,5 | 0,9 | 1,9 | 4,2 | 6,5 | 7 | 7 | 7 | 294 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H047. D1.2 : Tourbières de couverture

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D1.2 |
| EUNIS 2012 | D1.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 52 Tourbières de couverture |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Tourbières ombrotrophes formées sur terrain plat ou en pente faible sous climat océanique très pluvieux, à surface de buttes et de gouilles dominées par les sphaignes, la narthécie, la molinie, la linaigrette et la callune.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (65 taxons ; les 40 plus cités) : Eriophorum vaginatum, Scirpus cespitosus, Calluna vulgaris, Sphagnum rubellum, Sphagnum magellanicum, Sphagnum papillosum, Drosera rotundifolia, Erica tetralix, Sphagnum fuscum, Racomitrium lanuginosum, Andromeda polifolia, Sphagnum tenellum, Narthecium ossifragum, Rhynchospora alba, Eriophorum angustifolium, Carex limosa, Vaccinium oxycoccos, Vaccinium uliginosum, Rubus chamaemorus, Sphagnum compactum, Sphagnum auriculatum, Carex panicea, Molinia caerulea, Schoenus nigricans, Zygogonium sp., Sphagnum cuspidatum, Drosera anglica, Scheuchzeria palustris, Cladonia sylvatica, Betula nana, Empetrum sp., Deschampsia flexuosa, Empetrum nigrum, Campylopus atrovirens, Myrica gale, Pinguicula lusitanica, Polygala serpyllifolia, Potentilla erecta, Pleurozia purpurea, Sphagnum nemoreum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 1 m²HE/m² | 0,9 à 1 | code 36.01, « Hochmoore (weitgehend intakt) », Biotoptypenwert 24 sur 24 (ligne 374 de l'extraction) |

Correspondance retenue : Tourbières hautes intactes.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible moyen |
| Création, mauvais état visé | 32 ans | onglet G-4, ligne 82, « Wetland - Blanket bog », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 83, « Wetland - Blanket bog », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 103, « Wetland - Blanket bog » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 103, « Wetland - Blanket bog » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 100 |
| État moyen | 87,5 |
| Mauvais état | 70 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 50 m²HE, 15 à 30 cm 60 m²HE, 30 à 80 cm 70 m²HE, 80 cm et plus 90 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,2 | 2,8 | 4,4 | 5,9 | 9,1 | 10 | 335 |
| moyen | 0 | 0,3 | 0,5 | 1,1 | 2,5 | 3,8 | 5,2 | 7,9 | 8,8 | 293 |
| mauvais | 0 | 0,2 | 0,4 | 0,9 | 2 | 3,1 | 4,2 | 6,3 | 7 | 234 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H048. D2.1 : Tourbières de vallée

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D2.1 |
| EUNIS 2012 | D2.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Tourbières topogènes alimentées par les eaux de ruissellement du bassin versant, le plus souvent en complexes de bas-marais acides, de tourbières de transition et de gouilles.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 1 m²HE/m² | 0,9 à 1 | code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |

Correspondance retenue : Bas-marais et marécages intacts.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 86, « Wetland - Oceanic valley mire[1] (D2.1) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 87, « Wetland - Oceanic valley mire[1] (D2.1) », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 107, « Wetland - Oceanic valley mire[1] (D2.1) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 107, « Wetland - Oceanic valley mire[1] (D2.1) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 100 |
| État moyen | 87,5 |
| Mauvais état | 70 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 50 m²HE, 15 à 30 cm 60 m²HE, 30 à 80 cm 70 m²HE, 80 cm et plus 90 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,2 | 2,8 | 4,4 | 5,9 | 9,1 | 10 | 335 |
| moyen | 0 | 0,3 | 0,6 | 1,2 | 2,6 | 4,1 | 5,5 | 8,5 | 8,8 | 302 |
| mauvais | 0 | 0,5 | 0,9 | 1,9 | 4,2 | 6,5 | 7 | 7 | 7 | 294 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H049. D2.2 : Bas-marais oligotrophes et tourbières des sources

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D2.2 |
| EUNIS 2012 | D2.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.93 Bois marécageux de Bouleaux et de piment royal, 54.1 Sources, 54.11 Sources d'eaux douces pauvres en bases, 54.111 Sources d'eaux douces à Bryophytes, 54.112 Sources à Cardamines, 54.4 Bas-marais acides, 54.41 Ceintures lacustres à Eriophorum scheuchzeri, 54.42 Tourbières basses à Carex nigra, C. canescens et C. echinata, 54.421 Bas-marais alpins à Carex fusca, et 15 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Tourbières, suintements et sources végétalisées à eau modérément acide, où la nappe affleure en permanence. Végétation dominée par de petites laîches (laîche blanchâtre, laîche étoilée, laîche noire, linaigrette à feuilles étroites), des mousses brunes ou des sphaignes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (214 taxons ; les 40 plus cités) : Carex echinata, Carex nigra, Eriophorum angustifolium, Carex canescens, Scirpus cespitosus, Eriophorum vaginatum, Carex rostrata, Sphagnum papillosum, Drosera rotundifolia, Agrostis canina, Carex sp., Sphagnum compactum, Andromeda polifolia, Carex pauciflora, Molinia caerulea, Drepanocladus exannulatus, Narthecium ossifragum, Sphagnum magellanicum, Trichophorum cespitosum, Calliergon sarmentosum, Eriophorum scheuchzeri, Juncus filiformis, Viola palustris, Philonotis fontana, Juncus acutiflorus, Carex magellanica, Myrica gale, Nardus stricta, Calliergon stramineum, Sphagnum cuspidatum, Sphagnum recurvum, Carex intricata, Parnassia palustris, Sphagnum lindbergii, Sphagnum sp., Sphagnum balticum, Sphagnum tenellum, Menyanthes trifoliata, Vaccinium oxycoccos, Rubus chamaemorus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 1 m²HE/m² | 0,9 à 1 | code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |

Correspondance retenue : Bas-marais et marécages intacts.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 18 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 100 |
| État moyen | 87,5 |
| Mauvais état | 70 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 50 m²HE, 15 à 30 cm 60 m²HE, 30 à 80 cm 70 m²HE, 80 cm et plus 90 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,1 | 2,2 | 4,4 | 9,9 | 15,4 | 20,9 | 31,9 | 33 | 1 138 |
| moyen | 0 | 1,4 | 2,9 | 5,8 | 13 | 20,2 | 27,4 | 28,9 | 28,9 | 1 141 |
| mauvais | 0 | 2,3 | 4,6 | 9,2 | 20,8 | 23,1 | 23,1 | 23,1 | 23,1 | 1 028 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H050. D2.3 : Tourbières de transition et tremblantes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D2.3 |
| EUNIS 2012 | D2.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 54.5 Tourbières de transition, 54.51 Pelouses à Carex lasiocarpa, 54.511 Pelouses de Carex lasiocarpa et Mousses brunes, 54.512 Pelouses à Carex lasiocarpa et Sphaignes, 54.52 Tourbières tremblantes à Carex diandra, 54.53 Tourbières tremblantes à Carex rostrata, 54.531 Tourbières tremblantes acidiclines à Carex rostrata, 54.532 Tourbières tremblantes basiclines à Carex rostrata, 54.5321 Tourbières tremblantes basiclines à Carex rostrata et Sphaignes, 54.5322 Tourbières tremblantes basiclines à Carex rostrata et Mousses brunes, et 15 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Zones humides incomplètement atterries, à végétation turfigène sur eau acide : radeaux flottants et tremblants à trèfle d'eau, comaret, laîche à long rhizome, laîche des bourbiers, rhynchospore blanc.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (149 taxons ; les 40 plus cités) : Carex rostrata, Carex limosa, Menyanthes trifoliata, Carex lasiocarpa, Eriophorum angustifolium, Potentilla palustris, Sphagnum recurvum, Sphagnum subsecundum, Drosera rotundifolia, Equisetum fluviatile, Scorpidium scorpioides, Rhynchospora alba, Drepanocladus revolvens, Vaccinium oxycoccos, Carex chordorrhiza, Scheuchzeria palustris, Campylium stellatum, Sphagnum riparium, Eriophorum gracile, Sphagnum contortum, Sphagnum squarrosum, Carex diandra, Drepanocladus exannulatus, Sphagnum auriculatum, Comarum palustre, Hydrocotyle vulgaris, Carex nigra, Sphagnum flexuosum, Liparis loeselii, Pedicularis palustris, Molinia caerulea, Paludella squarrosa, Calliergon giganteum, Sphagnum dusenii, Sphagnum teres, Sphagnum warnstorfii, Cicuta virosa, Sphagnum cuspidatum, Eriophorum russeolum, Sphagnum lindbergii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9583 m²HE/m² | 0,8625 à 1 | code 36.02, « Übergangsmoore und Zwischenmoore (weitgehend intakt) », Biotoptypenwert 23 sur 24 (ligne 375 de l'extraction) |

Correspondance retenue : Tourbières de transition intactes.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 89, « Wetland - Transition mires and quaking bogs (H7140) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 90, « Wetland - Transition mires and quaking bogs (H7140) », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 110, « Wetland - Transition mires and quaking bogs (H7140) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 110, « Wetland - Transition mires and quaking bogs (H7140) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 95,83 |
| État moyen | 83,85 |
| Mauvais état | 67,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 47,91 m²HE, 15 à 30 cm 57,5 m²HE, 30 à 80 cm 67,08 m²HE, 80 cm et plus 86,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,2 | 2,7 | 4,2 | 5,7 | 8,7 | 9,6 | 321 |
| moyen | 0 | 0,3 | 0,6 | 1,1 | 2,5 | 3,9 | 5,3 | 8,1 | 8,4 | 289 |
| mauvais | 0 | 0,4 | 0,9 | 1,8 | 4 | 6,3 | 6,7 | 6,7 | 6,7 | 282 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H051. D4.1 : Bas-marais riches en bases

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D4.1 |
| EUNIS 2012 | D4.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.93 Bois marécageux de Bouleaux et de piment royal, 51 Tourbières hautes, 51.1 Tourbières hautes à peu près naturelles, 51.12 Tourbières basses (Schlenken), 51.122 Chenaux superficiels, cuvettes peu profondes, 54.1 Sources, 54.12 Sources d'eaux dures, 54.122 Sources calcaires, 54.2 Bas-marais alcalins (tourbières basses alcalines), et 19 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Zones humides et sources à alimentation riche en bases, souvent calcaire, saturées en eau une partie de l'année ou en permanence. Végétation de petites ou grandes graminoïdes (laîches, choin, molinie) ou de hautes herbes, souvent avec un tapis de mousses brunes 

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (207 taxons ; les 40 plus cités) : Carex panicea, Eriophorum latifolium, Pinguicula vulgaris, Carex hostiana, Parnassia palustris, Carex flava, Carex davalliana, Carex dioica, Carex nigra, Carex lepidocarpa, Schoenus nigricans, Molinia caerulea, Eleocharis quinqueflora, Primula farinosa, Schoenus ferrugineus, Campylium stellatum, Carex demissa, Saxifraga aizoides, Tofieldia calyculata, Juncus articulatus, Equisetum palustre, Eriophorum angustifolium, Epipactis palustris, Equisetum variegatum, Potentilla erecta, Scirpus cespitosus, Tofieldia pusilla, Carex pulicaris, Blysmus compressus, Paludella squarrosa, Carex rostrata, Cratoneuron commutatum, Juncus subnodulosus, Carex sp., Drepanocladus revolvens, Drepanocladus intermedius, Bartsia alpina, Carex flacca, Carex rariflora, Carex capillaris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 1 m²HE/m² | 0,9 à 1 | code 35.01a, « – Weitgehend intakt », Biotoptypenwert 24 sur 24 (ligne 352 de l'extraction) |

Correspondance retenue : Bas-marais et marécages intacts.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 18 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 100 |
| État moyen | 87,5 |
| Mauvais état | 70 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 50 m²HE, 15 à 30 cm 60 m²HE, 30 à 80 cm 70 m²HE, 80 cm et plus 90 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,1 | 2,2 | 4,4 | 9,9 | 15,4 | 20,9 | 31,9 | 33 | 1 138 |
| moyen | 0 | 1,4 | 2,9 | 5,8 | 13 | 20,2 | 27,4 | 28,9 | 28,9 | 1 141 |
| mauvais | 0 | 2,3 | 4,6 | 9,2 | 20,8 | 23,1 | 23,1 | 23,1 | 23,1 | 1 028 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H052. D4.2 : Communautés riveraines des sources calcaires de montagne

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D4.2 |
| EUNIS 2012 | D4.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 54.3 Gazons riverains arctico-alpins, 54.31 Gazons riverains arctico-alpins à élyne fausse Laîche, 54.32 Gazons riverains arctico-alpins à Carex maritima, 54.33 Gazons riverains arctico-alpins à Typha |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Communautés pionnières rares des substrats calcaires détrempés d'eau froide, en bordure des sources et des torrents glaciaires des étages alpin et subalpin ou sur les sables des rivières froides, à laîche bicolore, kobrésie, jonc arctique, petites massettes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (48 taxons ; les 40 plus cités) : Carex atrofusca, Juncus arcticus, Juncus castaneus, Equisetum variegatum, Carex dioica, Juncus triglumis, Tofieldia pusilla, Carex microglochin, Kobresia simpliciuscula, Juncus alpinoarticulatus, Typha minima, Typha shuttleworthii, Carex bicolor, Carex maritima, Campylium stellatum, Carex capillaris, Carex vaginata, Saxifraga aizoides, Thalictrum alpinum, Juncus biglumis, Carex panicea, Eriophorum scheuchzeri, Eriophorum angustifolium, Carex sp., Juncus alpinus, Carex incurva, Carex juncifolia, Drepanocladus revolvens, Bistorta vivipara, Polygonum viviparum, Salix reticulata, Carex bigelowii, Carex parallela, Blindia acuta, Carex demissa, Equisetum hyemale, Bryum sp., Calliergon sp., Philonotis sp., Drepanocladus intermedius.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 22.01.02, « Kalkreiche Sicker- und Sumpfquellen (Helokrenen) (inkl. Kalktuff-Sicker- und -Sumpfquelle) », Biotoptypenwert 20 sur 24 (ligne 178 de l'extraction) |

Correspondance retenue : Sources de suintement calcaires.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 18 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,7 | 8,2 | 12,8 | 17,4 | 26,6 | 27,5 | 949 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H053. D5.1 : Roselières normalement sans eau libre

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D5.1 |
| EUNIS 2012 | D5.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.1 Roselières, 53.11 Phragmitaies, 53.112 Phragmitaies sèches, 53.113 Phagmitaies géantes, 53.12 Scirpaies lacustres, 53.13 Typhaies |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Peuplements atterris de grands hélophytes (roseau, scirpes, massettes, prêles), pauvres en espèces et souvent dominés par une seule, sur sol gorgé d'eau.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (12 taxons ; les 40 plus cités) : Typha angustifolia, Phragmites australis, Phragmites sp., Typha latifolia, Typha domingensis, Typha laxmannii, Typha elephantina, Poaceae sp., Scirpus sp., Typha sp., Schoenoplectus sp., Scirpus lacustris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 38.02.02, « Schilf-Landröhricht », Biotoptypenwert 15 sur 24 (ligne 391 de l'extraction) |

Correspondance retenue : Roselière terrestre à roseau.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| Création, mauvais état visé | 3 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 12 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 31,25 m²HE, 15 à 30 cm 37,5 m²HE, 30 à 80 cm 43,75 m²HE, 80 cm et plus 56,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,5 | 7 | 14 | 31,4 | 41,9 | 41,9 | 41,9 | 41,9 | 1 822 |
| moyen | 0 | 5,2 | 10,5 | 20,9 | 36,6 | 36,6 | 36,6 | 36,6 | 36,6 | 1 685 |
| mauvais | 0 | 9,8 | 19,5 | 29,3 | 29,3 | 29,3 | 29,3 | 29,3 | 29,3 | 1 407 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H054. D5.2 : Formations à grandes cypéracées sans eau libre

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D5.2 |
| EUNIS 2012 | D5.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.2 Communautés à grandes Laîches, 53.21 Peuplements de grandes Laîches (Magnocariçaies), 53.211 Cariçaies à laîche distique, 53.212 Cariçaies à laîche aiguë et communautés s'y rapportant, 53.2121 Cariçaies à laîche aiguë, 53.2122 Cariçaies à laîche des marais, 53.213 Cariçaies à Carex riparia, 53.214 Cariçaies à Carex rostrata et à Carex vesicaria, 53.2141 Cariçaies à Carex rostrata, 53.2142 Cariçaies à Carex vesicaria, et 12 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Peuplements atterris de grandes laîches, de marisque ou de souchets, pauvres en espèces, sur sol gorgé d'eau.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (38 taxons ; les 40 plus cités) : Carex acutiformis, Carex lasiocarpa, Carex paniculata, Carex elata, Carex rostrata, Carex vesicaria, Carex acuta, Carex otrubae, Carex vulpina, Cyperus papyrus, Carex appropinquata, Carex sp., Cyperus sp., Carex riparia, Carex buekii, Cladium mariscus, Eriophorum latifolium, Molinia caerulea, Schoenus nigricans, Schoenus ferrugineus, Carex buxbaumii, Carex pseudocyperus, Carex paradoxa, Carex diandra, Carex hispida, Carex aquatilis, Carex curvata, Carex melanostachya, Carex nutans, Kosteletzkya pentacarpos, Carex cespitosa, Carex acuta ssp. broteriana, Carex disticha, Carex lyngbyei, Cladium sp., Cyperus longus, Cyperus papyrus ssp. siculus, Carex oenensis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 37.02, « Nährstoffreiches Großseggenried », Biotoptypenwert 16 sur 24 (ligne 386 de l'extraction) |

Correspondance retenue : Magnocariçaie eutrophe.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 84, « Wetland - Fens (upland and lowland) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 18 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 12 ans | onglet G-5, ligne 85, « Wetland - Fens (upland and lowland) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 105, « Wetland - Fens (upland and lowland) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,3 | 13,9 | 21,3 | 22 | 759 |
| moyen | 0 | 1 | 1,9 | 3,9 | 8,7 | 13,5 | 18,3 | 19,3 | 19,3 | 760 |
| mauvais | 0 | 1,5 | 3,1 | 6,2 | 13,9 | 15,4 | 15,4 | 15,4 | 15,4 | 685 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H055. D5.3 : Zones marécageuses à grands joncs

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D5.3 |
| EUNIS 2012 | D5.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 53.5 Jonchaies hautes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Peuplements de grands joncs envahissant des marais surpâturés ou piétinés, ou des bas-marais et tourbières eutrophisés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Juncus sp., Juncus effusus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 35.02.06.03, « Brachgefallenes, artenarmes Feuchtgrünland », Biotoptypenwert 12 sur 24 (ligne 371 de l'extraction) |

Correspondance retenue : Prairie humide pauvre en espèces en déprise (jonchaies).

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,6 | 1,1 | 2,2 | 5 | 7,7 | 10,4 | 15,9 | 16,5 | 569 |
| moyen | 0 | 0,7 | 1,4 | 2,9 | 6,5 | 10,1 | 13,7 | 14,4 | 14,4 | 570 |
| mauvais | 0 | 1,2 | 2,3 | 4,6 | 10,4 | 11,6 | 11,6 | 11,6 | 11,6 | 514 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H056. D6.1 : Marais salés continentaux

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D6.1 |
| EUNIS 2012 | D6.1 |
| EUNIS 2022 (HabRef) | R6-3 Marais salés intérieurs tempérés |
| CORINE Biotopes (HabRef) | 15.1 Gazons pionniers salés, 15.11 Gazons à Salicorne et Suaeda, 15.112 Gazons continentaux à salicorne, 15.1121 Suintements continentaux à salicorne, 15.1122 Gazons continentaux secs à salicorne, 15.4 Prés salés continentaux, 15.41 Prés salés continentaux avec Puccinellia distans, 15.42 Prés salés continentaux à jonc et Elymus |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Prés salés et peuplements de salicornes des bassins salés de l'intérieur des terres, communautés rares et très menacées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (36 taxons ; les 40 plus cités) : Salicornia sp., Suaeda sp., Salsola soda, Juncus gerardi, Glaux maritima, Triglochin maritima, Salicornia europaea, Suaeda maritima, Microcnemum coralloides, Salicornia prostrata, Salsola sp., Chenopodiaceae sp., Hordeum geniculatum, Puccinellia distans, Puccinellia limosa, Camphorosma annua, Plantago tenuiflora, Elymus repens, Melilotus dentata, Suaeda maritima ssp. salsa, Suaeda pannonica, Suaeda maritima ssp. prostrata, Salicornia simonkaiana, Parnassia palustris, Pinguicula vulgaris, Primula farinosa, Scirpus pumilus, Centaurium littorale ssp. uliginosum, Plantago maritima ssp. salsa, Microcnemum sp., Microcnemum coralloides ssp. coralloides, Bassia hirsuta, Limonium gmelinii, Carex distans, Carex divisa, Halimione pedunculata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 35.03, « Salzgrünland des Binnenlandes », Biotoptypenwert 22 sur 24 (ligne 372 de l'extraction) |

Correspondance retenue : Prés salés de l'intérieur.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 6 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 14 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2 | 4 | 8,1 | 18,2 | 28,2 | 30,3 | 30,3 | 30,3 | 1 271 |
| moyen | 0 | 3,8 | 7,6 | 15,1 | 26,5 | 26,5 | 26,5 | 26,5 | 26,5 | 1 218 |
| mauvais | 0 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 1 038 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H057. D6.2 : Nappes d'hélophytes saumâtres pauvres en espèces

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | D6.2 |
| EUNIS 2012 | D6.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Peuplements atterris de grands hélophytes tolérants au sel, roseau notamment.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (5 taxons ; les 40 plus cités) : Cyperus laevigatus, Phragmites australis, Aeluropus littoralis, Juncus gerardi, Puccinellia fasciculata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 38.07, « Sonstiges Röhricht », Biotoptypenwert 16 sur 24 (ligne 396 de l'extraction) |

Correspondance retenue : Autre roselière.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible moyen |
| Création, mauvais état visé | 3 ans | onglet G-4, ligne 88, « Wetland - Reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 12 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 89, « Wetland - Reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 109, « Wetland - Reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3,7 | 7,4 | 14,9 | 33,5 | 44,7 | 44,7 | 44,7 | 44,7 | 1 943 |
| moyen | 0 | 5,6 | 11,2 | 22,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 798 |
| mauvais | 0 | 10,4 | 20,8 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 501 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.4 Prairies, pelouses et formations de hautes herbes (EUNIS E)

#### Fiche H058. E1.1 : Végétations ouvertes des substrats sableux et rocheux

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.1 |
| EUNIS 2012 | E1.1 |
| EUNIS 2022 (HabRef) | R1-1 Pannonian and Pontic sandy steppe, R1-2 Végétations dominées par des cryptogames et des annuelles sur les affleurements de roches siliceuses, R1-3 Végétations dominées par des cryptogames et des annuelles sur les affleurements de roches calcaires et ultramafiques, R1-4 Perennial rocky grassland of the Italian Peninsula, R1-5 Continental dry rocky steppic grassland and dwarf scrub on chalk outcrops, R1-6 Perennial rocky grassland of Central and South-Eastern Europe, R1-7 Heavy-metal dry grassland of the Balkans, R1-8 Pelouses calcicoles rocailleuses vivaces d'Europe subatlantique-subméditerranéenne, et 1 autres |
| CORINE Biotopes (HabRef) | 34.1 Pelouses pionnières médio-européennes, 34.11 Pelouses médio-européennes sur débris rocheux, 34.111 Pelouses à orpins, 34.112 Formations à Joubarbes, 34.1121 Communautés à Sempervivum tectorum, 34.113 Formations herbeuses sur débris rocheux, 34.114 Communautés thérophytiques médio-européennes sur débris rocheux, 34.12 Pelouses des sables calcaires |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Végétation ouverte et thermophile des sables et des débris rocheux, formée surtout d'annuelles et de plantes grasses, sur sols calcaires ou siliceux.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (44 taxons ; les 40 plus cités) : Melica ciliata, Poa bulbosa, Sedum acre, Poa badensis, Poa angustifolia, Poa compressa, Asplenium ruta-muraria, Colchicum hungaricum, Sedum neglectum ssp. sopianae, Ceterach javorkaenum, Erophila verna, Sedum album, Sedum sexangulare, Jovibarba globifera ssp. glabrescens, Androsace septentrionalis, Arenaria serpyllifolia, Astragalus arenarius, Bromus tectorum, Cerastium semidecandrum, Colchicum arenarium, Cynodon dactylon, Dianthus arenarius, Dianthus deltoides, Helichrysum arenarium, Koeleria glauca, Koeleria macrantha, Onosma arenaria, Petrorhagia prolifera, Phleum arenarium, Silene conica, Silene otites, Vicia lathyroides, Festuca polesica, Festuca duvalii, Festuca psammophila, Gypsophila fastigiata ssp. arenaria, Jurinea cyanoides, Stipa borysthenica ssp. germanica, Silene chlorantha, Jovibarba sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |

Correspondance retenue : Pelouses sableuses annuelles.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H059. E1.2 : Pelouses calcaires vivaces et steppes riches en bases

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.2 |
| EUNIS 2012 | E1.2 |
| EUNIS 2022 (HabRef) | R1-A Pelouses calcicoles vivaces semi-sèches (steppes prairiales), R1-B Prairies sèches continentales (vraies steppes) |
| CORINE Biotopes (HabRef) | 34.3 Pelouses pérennes denses et steppes médio-européennes, 34.31 Pelouses steppiques sub-continentales, 34.312 Pelouses steppiques de l'Europe centrale, 34.3121 Pelouses steppiques xérophiles de l'Europe centrale, 34.3122 Pelouses steppiques mésophiles de l'Europe centrale, 34.3123 Pelouses steppiques à brachypode penné de l'Europe centrale, 34.314 Pelouses arides des Alpes occidentales internes, 34.32 Pelouses calcaires sub-atlantiques semi-arides, 34.321 Pelouses calcicoles semi-sèches nord-occidentales, 34.322 Pelouses semi-sèches médio-européennes à Bromus erectus, et 42 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses vivaces, souvent pauvres en nutriments et riches en espèces, des sols calcaires et basiques (pelouses des Festuco-Brometea).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (578 taxons ; les 40 plus cités) : Bromus erectus, Carex humilis, Festuca pallens, Stipa capillata, Festuca rupicola, Brachypodium pinnatum, Festuca vaginata, Helianthemum canum, Fumana procumbens, Sesleria albicans, Stipa pulcherrima, Teucrium montanum, Melica ciliata, Helianthemum nummularium, Festuca valesiaca, Poa bulbosa, Potentilla arenaria, Euphorbia seguierana, Koeleria macrantha, Festuca trachyphylla, Helichrysum arenarium, Astragalus exscapus, Stipa joannis, Thymus praecox, Carex flacca, Sempervivum marmoreum, Seseli osseum, Cynodon dactylon, Thymus glabrescens, Armeria elongata, Artemisia campestris, Astragalus austriacus, Astragalus onobrychis, Dichanthium ischaemum, Galium verum, Alyssum montanum ssp. gmelinii, Alyssum tortuosum, Festuca wagneri, Artemisia alba, Briza media.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.02a, « Halbtrockenrasen, beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 318 de l'extraction) |

Correspondance retenue : Pelouses mi-sèches pâturées ou fauchées.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,9 | 5,8 | 13 | 20,2 | 27,4 | 28,9 | 28,9 | 1 141 |
| moyen | 0 | 2,5 | 5,1 | 10,1 | 22,7 | 25,3 | 25,3 | 25,3 | 25,3 | 1 124 |
| mauvais | 0 | 4 | 8,1 | 16,2 | 20,2 | 20,2 | 20,2 | 20,2 | 20,2 | 950 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H060. E1.3 : Pelouses xériques méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.3 |
| EUNIS 2012 | E1.3 |
| EUNIS 2022 (HabRef) | R1-D Pelouses sèches méditerranéennes fortement pâturées, R1-E Pelouses sèches vivaces hautes méditerranéennes, R1-F Pelouses sèches méditerranéennes riches en annuelles |
| CORINE Biotopes (HabRef) | 34.5 Pelouses méditerranéennes xériques, 34.51 Pelouses xériques de la Méditerranée occidentale, 34.511 Pelouses du Brachypodietum retusi, 34.512 Steppe de la Crau, 34.513 Communautés méditerranéennes annuelles sur sols superficiels, 34.5131 Communautés annuelles calciphiles de l'ouest méditerranéen, 34.514 Arènes dolomitiques des Causses |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses xérophiles méso- et thermoméditerranéennes, le plus souvent ouvertes, à graminées courtes et riches en annuelles, sur substrats basiques souvent calcaires.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (183 taxons ; les 40 plus cités) : Stipa capensis, Brachypodium distachyon, Brachypodium retusum, Bromus fasciculatus, Dactylis hispanica, Lagurus ovatus, Aster sorrentinii, Alyssum serpyllifolium, Armeria girardii, Armeria juncea, Aster alpinus, Corynephorus canescens, Helianthemum pilosum, Helichrysum stoechas, Phleum arenarium, Sedum ochroleucum, Silene otites, Alkanna tinctoria, Festuca christianii-bernardii, Arenaria aggregata, Allium chamaemoly, Anagallis monelli, Andryala ragusina, Asteriscus aquaticus, Astragalus sesameus, Bellis annua, Campanula erinus, Catananche lutea, Convolvulus lineatus, Daucus aureus, Daucus lopadusanus, Desmazeria marina, Desmazeria sicula, Echium parviflorum, Erophila verna, Evax pygmaea, Filago cossyrensis, Hainardia cylindrica, Hedysarum spinosissimum, Koeleria splendens.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.01, « Trockenrasen auf karbonatischem oder silikatischem Untergrund », Biotoptypenwert 21 sur 24 (ligne 316 de l'extraction) |

Correspondance retenue : Pelouses sèches.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,9 | 5,8 | 13 | 20,2 | 27,4 | 28,9 | 28,9 | 1 141 |
| moyen | 0 | 2,5 | 5,1 | 10,1 | 22,7 | 25,3 | 25,3 | 25,3 | 25,3 | 1 124 |
| mauvais | 0 | 4 | 8,1 | 16,2 | 20,2 | 20,2 | 20,2 | 20,2 | 20,2 | 950 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H061. E1.4 : Steppes méditerranéennes à grandes graminées et armoises

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.4 |
| EUNIS 2012 | E1.4 |
| EUNIS 2022 (HabRef) | R1-E Pelouses sèches vivaces hautes méditerranéennes |
| CORINE Biotopes (HabRef) | 34.6 Steppes méditerranéennes à Graminées, 34.63 Steppes à Stipa, Ampelodesmos, Andropogon, fétuque, 34.632 Steppes méditerranéennes à Stipa, 34.634 Steppes à Andropogon |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Formations méditerranéennes dominées par de grandes graminées, entre lesquelles poussent des annuelles ou des chaméphytes, sur sols siliceux ou basiques.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (27 taxons ; les 40 plus cités) : Chrysopogon gryllus, Dichanthium ischaemum, Hyparrhenia hirta, Andropogon distachyos, Lygeum spartum, Heteropogon contortus, Dichanthium insculptum, Stipa tenacissima, Artemisia sp., Stipa gigantea, Ampelodesmos mauritanica, Stipa offneri, Piptatherum sp., Stipa sp., Oryzopsis sp., Stipa lagascae, Helictotrichon filifolium, Festuca capillifolia, Festuca scariosa, Helictotrichon sarracenorum, Arrhenatherum album, Arundo sp., Imperata sp., Hemarthria sp., Saccharum sp., Andropogon ischaemum, Bothriochloa ischaemum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 34.03.01a, « Steppenrasen, beweidet oder gemäht », Biotoptypenwert 22 sur 24 (ligne 321 de l'extraction) |

Correspondance retenue : Pelouses steppiques pâturées ou fauchées.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,5 | 3 | 6,1 | 13,6 | 21,2 | 28,7 | 30,3 | 30,3 | 1 195 |
| moyen | 0 | 2,6 | 5,3 | 10,6 | 23,8 | 26,5 | 26,5 | 26,5 | 26,5 | 1 178 |
| mauvais | 0 | 4,2 | 8,5 | 16,9 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 995 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H062. E1.5 : Pelouses méditerranéo-montagnardes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.5 |
| EUNIS 2012 | E1.5 |
| EUNIS 2022 (HabRef) | R1-G Iberian oromediterranean siliceous dry grassland, R1-H Pelouses sèches basiphiles ibériques oroméditerranéennes, R1-J Pelouses sèches siliceuses oroméditerranéennes cyrno-sardes, R1-K Balkan and Anatolian oromediterranean dry grassland, R1-L Madeiran oromediterranean siliceous dry grassland |
| CORINE Biotopes (HabRef) | 34.7 Pelouses méditerranéo-montagnardes, 34.71 Steppes méditerranéo-montagnardes, 34.711 Steppes méditerranéo-montagnardes à Stipa, 34.7111 Steppes à Stipa des Causses, 34.7112 Steppes à Stipa de haute-Provence, 34.712 Pelouses méditerranéo-montagnardes à Sesleria, 34.713 Steppes méditerranéo-montagnardes à Festuca-Koeleria, 34.7131 Pelouses rases des Causses à Festuca, 34.7132 Pelouses rases des Causses à Carex-Anthyllis, 34.7133 Steppes méditerranéo-montagnardes franco-ibériennes, et 3 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses vivaces ouvertes riches en chaméphytes de l'étage des chênaies thermophiles, maintenues par un pâturage et une fauche extensifs.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (160 taxons ; les 40 plus cités) : Bromus erectus, Carex humilis, Artemisia alba, Chrysopogon gryllus, Festuca valesiaca, Sesleria juncifolia, Festuca auquieri, Koeleria vallesiana, Ononis striata, Stipa pennata, Genista holopetala, Melica ciliata, Koeleria splendens, Sesleria sp., Cleistogenes serotina, Stipa bromoides, Sesleria albicans var. elegantissima, Helianthemum canum, Plantago argentea, Gentiana clusii, Brachypodium pinnatum, Hypochoeris maculata, Scorzonera villosa, Festuca rupicola, Alyssum montanum, Helichrysum italicum, Armeria dalmatica, Crepis chondrilloides, Edraianthus tenuifolius, Satureja subspicata, Helianthemum oelandicum ssp. italicum, Chamaecytisus spinescens, Cirsum acarna, Inula candida, Scutellaria orientalis var. pinnatifida, Asphodelus microcarpus, Achillea nobilis, Medicago prostrata, Cladonia endiviaefolia, Allium ochroleucum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.01, « Trockenrasen auf karbonatischem oder silikatischem Untergrund », Biotoptypenwert 21 sur 24 (ligne 316 de l'extraction) |

Correspondance retenue : Pelouses sèches.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 25 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,2 | 2,3 | 4,6 | 10,4 | 16,2 | 21,9 | 28,9 | 28,9 | 1 068 |
| moyen | 0 | 1,7 | 3,4 | 6,7 | 15,2 | 23,6 | 25,3 | 25,3 | 25,3 | 1 061 |
| mauvais | 0 | 2 | 4 | 8,1 | 18,2 | 20,2 | 20,2 | 20,2 | 20,2 | 899 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H063. E1.6 : Pelouses à annuelles subnitrophiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.6 |
| EUNIS 2012 | E1.6 |
| EUNIS 2022 (HabRef) | V3-2 Pelouses à annuelles subnitrophiles méditerranéennes |
| CORINE Biotopes (HabRef) | 34.8 Pelouses méditerranéennes subnitrophiles, 34.81 Groupements méditerranéens subnitrophiles de graminées |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Pelouses d'annuelles (bromes, égilopes, avoines, vulpies, crucifères, légumineuses) des sols légèrement enrichis en nitrates, pionnières des sols nus, des bords de route et des espaces interstitiels des cultures.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (65 taxons ; les 40 plus cités) : Aegilops sp., Vulpia sp., Bromus sp., Avena sp., Andryala arenaria, Capsella rubella, Hirschfeldia incana, Papaver argemone, Sisymbrium contortum, Brassica barrelieri, Alyssum granatense, Euphorbia matritensis, Rhynchosinapis hispida, Lotus edulis, Matthiola lunata, Volutaria lippii, Euphorbia dracunculoides, Leontodon salzmannii, Amberboa lippii, Astragalus longidentatus, Brassica cossoniana, Lasiopogon muscoides, Lycocarpus fugax, Matthiola parviflora, Notoceras bicorne, Carrichtera annua, Aegilops geniculata, Aegilops neglecta, Aegilops triuncialis, Aegilops ventricosa, Astragalus scorpioides, Avena barbata, Bromus alopecuros, Bromus fasciculatus, Bromus hordeaceus, Bromus intermedius, Bromus madritensis, Bromus rubens, Bromus tectorum, Coronilla scorpioides.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 39.06.02, « Trocken-warme Ruderalstandorte auf bindigem Boden », Biotoptypenwert 14 sur 24 (ligne 412 de l'extraction) |

Correspondance retenue : Stations rudérales sèches et chaudes sur sol limoneux.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 58,33 |
| État moyen | 51,04 |
| Mauvais état | 40,83 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 29,17 m²HE, 15 à 30 cm 35 m²HE, 30 à 80 cm 40,83 m²HE, 80 cm et plus 52,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| moyen | 0 | 17 | 34 | 51 | 51 | 51 | 51 | 51 | 51 | 2 450 |
| mauvais | 0 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 2 001 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H064. E1.7 : Pelouses sèches acides et neutres fermées non méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.7 |
| EUNIS 2012 | E1.7 |
| EUNIS 2022 (HabRef) | R1-M Pelouses planitiaires à montagnardes, sèches à mésiques, généralement dominées par Nardus stricta, R4-2 Boreal and arctic acidophilous alpine grassland |
| CORINE Biotopes (HabRef) | 35.1 Pelouses atlantiques à Nard raide et groupements apparentés, 35.11 Gazons à Nard raide, 35.12 Pelouses à Agrostis-Festuca, 35.13 Pelouses à canche flexueuse, 35.14 Pelouses intraforestières à Calamagrostis epigejos, 35.15 Pelouses à laîche des sables |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses vivaces fermées, sèches à mésophiles, des sols acides des régions atlantiques et subatlantiques, à nard, fétuques, agrostide capillaire, danthonie, flouve, canche flexueuse, arnica, potentille tormentille.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (94 taxons ; les 40 plus cités) : Anthoxanthum odoratum, Agrostis capillaris, Nardus stricta, Festuca sp., Festuca rubra, Polygonum viviparum, Agrostis sp., Deschampsia flexuosa, Galium saxatile, Potentilla erecta, Nardus sp., Danthonia decumbens, Polygala vulgaris, Bistorta vivipara, Galium sp., Galium boreale, Gentianella campestris, Carex bigelowii, Carex arenaria, Hierochloe odorata, Campanula rotundifolia, Calamagrostis epigejos, Festuca ovina, Sieglingia decumbens, Viola canina var. ericetorum, Calluna vulgaris, Calluna sp., Avenula pratensis, Botrychium lanceolatum, Botrychium lunaria, Carex brunnescens, Cerastium alpinum, Gentiana nivalis, Gentianella amarella, Gentianella tenella, Poa glauca, Botrychium boreale, Erigeron borealis, Primula scandinavica, Primula striata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.04.03.01a, « – Beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 326 de l'extraction) |

Correspondance retenue : Pelouses sableuses vivaces fermées, pâturées ou fauchées.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,6 | 8,1 | 12,6 | 17,1 | 26,2 | 28,9 | 967 |
| moyen | 0 | 1,3 | 2,5 | 5,1 | 11,4 | 17,7 | 24 | 25,3 | 25,3 | 998 |
| mauvais | 0 | 2 | 4 | 8,1 | 18,2 | 20,2 | 20,2 | 20,2 | 20,2 | 899 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H065. E1.8 : Pelouses fermées sèches acides et neutres méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.8 |
| EUNIS 2012 | E1.8 |
| EUNIS 2022 (HabRef) | R1-G Iberian oromediterranean siliceous dry grassland, R1-K Balkan and Anatolian oromediterranean dry grassland, R1-M Pelouses planitiaires à montagnardes, sèches à mésiques, généralement dominées par Nardus stricta, R1-N Pelouses sèches ouvertes acides et neutres supraméditerranéennes ibériques, R1-R Pelouses sèches ouvertes, acides et neutres, méditerranéennes à atlantiques |
| CORINE Biotopes (HabRef) | 35.3 Pelouses siliceuses méditerranéennes, 35.7 Pelouses méditerranéo-montagnardes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses vivaces des sols acides de l'étage supraméditerranéen, et pelouses siliceuses méditerranéennes riches en annuelles sur sols superficiels.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (131 taxons ; les 40 plus cités) : Nardus stricta, Linaria pelisseriana, Plantago bellardii, Silene gallica, Tuberaria guttata, Quercus pyrenaica, Briza maxima, Galium divaricatum, Vulpia myuros, Trifolium cherleri, Vulpia bromoides, Geum heterocarpum, Paeonia coriacea, Festuca elegans, Trifolium ochroleucon, Aira caryophyllea, Aira cupaniana, Airopsis tenella, Anthoxanthum aristatum, Corynephorus divaricatus, Crassula tillaea, Filago gallica, Jasione montana, Lathyrus angulatus, Linaria arvensis, Linum gallicum, Lupinus angustifolius, Molineria minuta, Ornithopus pinnatus, Ornithopus sativus, Paronychia cymosa, Paronychia echinulata, Radiola linoides, Sedum andegavense, Sedum caespitosum, Silene portensis, Teesdalia coronopifolia, Tolpis barbata, Trifolium arvense, Trifolium purpureum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.04.03.01a, « – Beweidet oder gemäht », Biotoptypenwert 21 sur 24 (ligne 326 de l'extraction) |

Correspondance retenue : Pelouses sableuses vivaces fermées, pâturées ou fauchées.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,6 | 8,1 | 12,6 | 17,1 | 26,2 | 28,9 | 967 |
| moyen | 0 | 1,3 | 2,5 | 5,1 | 11,4 | 17,7 | 24 | 25,3 | 25,3 | 998 |
| mauvais | 0 | 2 | 4 | 8,1 | 18,2 | 20,2 | 20,2 | 20,2 | 20,2 | 899 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H066. E1.9 : Pelouses ouvertes sèches acides et neutres non méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.9 |
| EUNIS 2012 | E1.9 |
| EUNIS 2022 (HabRef) | R1-P Pelouses sableuses intérieures océaniques à subcontinentales sur sols acides et neutres, R1-Q Pelouses siliceuses des congères de sables et des dunes continentales |
| CORINE Biotopes (HabRef) | 35.2 Pelouses siliceuses ouvertes médio-européennes, 35.21 Prairies siliceuses à annuelles naines, 35.22 Pelouses siliceuses ouvertes pérennes, 35.23 Pelouses à Corynephorus, 64.1 Dunes fluvio-glaciaires, 64.11 Pelouses pionnières des dunes continentales, 64.12 Pelouses siliceuses des dunes intérieures, 64.4 Dunes fluviatiles |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses ouvertes, souvent riches en annuelles, des sols bruts non calcaires, notamment des dunes continentales et des sables fixés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (129 taxons ; les 40 plus cités) : Corynephorus canescens, Festuca vaginata, Carex arenaria, Astragalus onobrychis, Carex liparocarpos, Teesdalia nudicaulis, Spergula morisonii, Koeleria glauca, Anacamptis pyramidalis, Astragalus exscapus, Chrysopogon gryllus, Colchicum arenarium, Festuca rupicola, Muscari comosum, Ophrys sphegodes, Potentilla cinerea, Silene parviflora, Thymus glabrescens, Agropyron cristatum ssp. pectinatum, Iris variegata, Lotus sp., Festuca pseudovina, Achillea ochroleuca, Astragalus asper, Festuca wagneri, Iris humilis ssp. arenaria, Onosma arenaria ssp. pseudoarenaria, Linum austriacum, Salvia nemorosa, Alyssum sp., Dianthus giganteiformis ssp. pontederae, Muscari botryoides, Psatirella ammophyla, Aira caryophyllea, Aira praecox, Filago arvensis, Filago gallica, Filago lutescens, Filago pyramidata, Micropyrum tenellum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |

Correspondance retenue : Pelouses sableuses annuelles.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H067. E1.A : Pelouses sèches ouvertes acides et neutres méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.A |
| EUNIS 2012 | E1.A |
| EUNIS 2022 (HabRef) | R1-R Pelouses sèches ouvertes, acides et neutres, méditerranéennes à atlantiques |
| CORINE Biotopes (HabRef) | 35.4 Communautés annuelles méditerranéennes des sables profonds, 64.6 Dunes continentales méditerranéennes, 64.61 Dunes riveraines du Rhône, 64.611 Prairies dunaires du Rhône, 64.6111 Végétation de cannes sur dunes du Rhône, 64.6112 Autres pelouses des dunes du Rhône, 64.612 Fourrés dunaires du Rhône, 64.613 Bois de Genévriers des dunes du Rhône |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Terrains sableux ouverts à annuelles printanières de la région méditerranéenne, et pelouses vivaces ouvertes des sols siliceux squelettiques de l'étage supraméditerranéen.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (39 taxons ; les 40 plus cités) : Armeria alliacea, Corynephorus canescens, Festuca costei, Festuca indigesta, Scleranthus perennis, Teucrium aureum, Leucanthemopsis pulverulenta, Armeria caballeroi, Dianthus laricifolius, Festuca summilusitana, Hieracium castellanum, Koeleria caudata ssp. crassipes, Plantago radicata, Thymus serpylloides ssp. gadorensis, Jasione crispa ssp. sessiliflora, Dianthus merinoi, Erodium laciniatum, Leucojum trichophyllum, Loeflingia hispanica, Malcolmia lacera, Malcolmia ramosissima, Maresia nana, Ononis variegata, Vulpia membranacea, Evax asterisciflora, Anthyllis hamosa, Arenaria emarginata, Erodium cicutarium ssp. bipinnatum, Evax lusitanica, Linaria donyana, Linaria pedunculata, Loeflingia spartea, Loeflingia tavaresiana, Ononis cossoniana, Ononis subspicata, Coronilla repanda, Loeflingia baetica, Hymenostemma pseudanthemis, Ononis baetica.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 34.04.01a, « Annuelle Sandtrockenrasen und Silbergrasfluren », Biotoptypenwert 20 sur 24 (ligne 324 de l'extraction) |

Correspondance retenue : Pelouses sableuses annuelles.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 18, « Grassland - Lowland dry acid grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 19, « Grassland - Lowland dry acid grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 19, « Grassland - Lowland dry acid grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H068. E1.B : Pelouses des sols métallifères

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.B |
| EUNIS 2012 | E1.B |
| EUNIS 2022 (HabRef) | R1-S Pelouses des sols métallifères d'Europe occidentale et centrale |
| CORINE Biotopes (HabRef) | 34.2 Pelouses métallifères de basse altitude, 34.22 Pelouses calaminaires, 34.223 Pelouses à Armeria halleri de l'Eifel, 34.23 Pelouses métallifères d'Europe centrale, 36.4 Pelouses calcicoles alpines et subalpines, 36.44 Communautés alpines métallifères |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Pelouses rases et sèches, souvent riches en lichens et mousses, des sols riches en métaux lourds (zinc, plomb), à espèces et écotypes adaptés (Violetalia calaminariae).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (26 taxons ; les 40 plus cités) : Thlaspi caerulescens, Armeria maritima, Armeria halleri, Silene vulgaris ssp. humilis, Viola guestphalica, Viola calaminaria, Viola lutea, Minuartia verna var. hercynica, Thlaspi alpestre ssp. calaminare, Armeria arenaria, Dianthus sylvestris, Galium anisophyllon, Poa alpina, Viola dubyana, Agrostis capillaris, Agrostis tenuis, Festuca ovina, Festuca rubra, Minuartia verna, Armeria hornburgensis, Armeria bottendorfensis, Silene maritima, Cardaminopsis halleri, Festuca aquisgranensis, Festuca valesiaca, Festuca ophioliticola ssp. calaminaria.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 34.05.01, « Natürlicher und halbnatürlicher Schwermetallrasen », Biotoptypenwert 21 sur 24 (ligne 329 de l'extraction) |

Correspondance retenue : Pelouses métallicoles naturelles.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible moyen |
| Création, mauvais état visé | 2 ans | onglet G-4, ligne 50, « Sparsely vegetated land - Calaminarian grasslands », condition cible mauvais |
| Amélioration, mauvais vers moyen | 3 ans | onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 8 ans | onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 5 ans | onglet G-5, ligne 51, « Sparsely vegetated land - Calaminarian grasslands », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 72, « Sparsely vegetated land - Calaminarian grasslands » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 72, « Sparsely vegetated land - Calaminarian grasslands » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 87,5 |
| État moyen | 76,56 |
| Mauvais état | 61,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 43,75 m²HE, 15 à 30 cm 52,5 m²HE, 30 à 80 cm 61,25 m²HE, 80 cm et plus 78,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,5 | 7,9 | 8,8 | 8,8 | 8,8 | 8,8 | 389 |
| moyen | 0 | 1,5 | 3,1 | 6,1 | 7,7 | 7,7 | 7,7 | 7,7 | 7,7 | 360 |
| mauvais | 0 | 3,1 | 6,1 | 6,1 | 6,1 | 6,1 | 6,1 | 6,1 | 6,1 | 297 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H069. E1.C : Habitats méditerranéens secs à herbacées inappétentes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.C |
| EUNIS 2012 | E1.C |
| EUNIS 2022 (HabRef) | V3-3 Habitats méditerranéens secs à végétation herbacée non-vernale inappétente |
| CORINE Biotopes (HabRef) | 32.9 Champs d'Asphodèles, de Phlomis, de Chardons, de Ferula |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Terres sèches à moins de 10 % d'arbustes, dominées par des plantes non appétentes (asphodèles, chardons, férules, phlomis), issues le plus souvent du surpâturage des garrigues.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (10 taxons ; les 40 plus cités) : Phlomis sp., Ferula sp., Asphodelus sp., Carlina sp., Carthamus sp., Onopordum sp., Centaurea sp., Urginea sp., Galactites sp., Notobasis sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 39.07, « Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) », Biotoptypenwert 10 sur 24 (ligne 414 de l'extraction) |

Correspondance retenue : Peuplements monospécifiques pauvres en espèces.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| Création, mauvais état visé | 2 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,2 | 8,3 | 16,7 | 37,5 | 41,7 | 41,7 | 41,7 | 41,7 | 1 854 |
| moyen | 0 | 7,3 | 14,6 | 29,2 | 36,5 | 36,5 | 36,5 | 36,5 | 36,5 | 1 714 |
| mauvais | 0 | 14,6 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 415 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H070. E1.D : Pelouses xériques non exploitées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.D |
| EUNIS 2012 | E1.D |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses xériques qui ne sont actuellement ni fauchées ni pâturées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 34.02b, « Halbtrockenrasen, brachgefallen bzw. ungenutzt », Biotoptypenwert 17 sur 24 (ligne 319 de l'extraction) |

Correspondance retenue : Pelouses mi-sèches en déprise.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 17, « Grassland - Lowland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 18, « Grassland - Lowland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 18, « Grassland - Lowland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,2 | 2,3 | 4,7 | 10,5 | 16,4 | 22,2 | 23,4 | 23,4 | 923 |
| moyen | 0 | 2 | 4,1 | 8,2 | 18,4 | 20,5 | 20,5 | 20,5 | 20,5 | 910 |
| mauvais | 0 | 3,3 | 6,5 | 13,1 | 16,4 | 16,4 | 16,4 | 16,4 | 16,4 | 769 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H071. E1.E : Pelouses xériques piétinées à annuelles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E1.E |
| EUNIS 2012 | E1.E |
| EUNIS 2022 (HabRef) | V3-4 Pelouses xériques piétinées à espèces annuelles |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP1 (prairies de faible valeur) |

**Définition**

Végétations basses d'annuelles des lieux secs, chauds et piétinés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (13 taxons ; les 40 plus cités) : Coronopus squamatus, Cynodon dactylon, Herniaria glabra, Herniaria hirsuta, Juncus tenuis, Lepidium ruderale, Lolium perenne, Plantago lanceolata, Plantago major, Poa annua, Polygonum arenastrum, Eragrostis minor, Matricaria discoidea.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |

Correspondance retenue : Gazon piétiné.

**Grille d'état EP1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Fourrés sur moins de 20 % de la surface de la prairie | non |
| D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface | non |
| E | Sol nu entre 1 % et 10 % de la surface | non |
| F | Fougère aigle sur moins de 20 % de la surface | non |
| G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 7 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| Création, état moyen visé | 4 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 33,33 |
| État moyen | 29,16 |
| Mauvais état | 23,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 16,66 m²HE, 15 à 30 cm 20 m²HE, 30 à 80 cm 23,33 m²HE, 80 cm et plus 30 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,8 | 9,5 | 19 | 33,3 | 33,3 | 33,3 | 33,3 | 33,3 | 1 533 |
| moyen | 0 | 7,3 | 14,6 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 385 |
| mauvais | 0 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 1 143 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H072. E2.1 : Pâturages permanents mésotrophes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.1 |
| EUNIS 2012 | E2.1 |
| EUNIS 2022 (HabRef) | R2-1 Pâturages permanents mésiques planitiaires et montagnards, R2-2 Prairies de fauche de basse et moyenne altitudes, R2-3 Prairies de fauche de montagne |
| CORINE Biotopes (HabRef) | 38.1 Pâtures mésophiles, 38.11 Pâturages continus, 38.111 Pâturages à Ray-grass, 38.112 Pâturages à Cynosurus-Centaurea, 38.12 Pâturages interrompus par des fossés, 38.13 Pâturages abandonnés |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pâtures mésotrophes régulièrement pâturées et fertilisées, sur sols bien drainés, à ray-grass, crételle, pâturins, fétuques, trèfle rampant, pâquerette, renoncules.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (22 taxons ; les 40 plus cités) : Cynosurus cristatus, Lolium perenne, Festuca nigrescens, Bellis perennis, Cardamine pratensis, Deschampsia cespitosa, Leontodon autumnalis, Ranunculus acris, Trifolium repens, Festuca sp., Poa sp., Ranunculus repens, Centaurea nigra, Centaurea sp., Cynosurus sp., Astrantia major, Coronilla varia, Gentiana cruciata, Geranium sylvaticum, Listera ovata, Platanthera bifolia, Trifolium medium.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 34.07b.02, « Mäßig artenreiche, frische (Mäh-)Weide », Biotoptypenwert 13 sur 24 (ligne 342 de l'extraction) |

Correspondance retenue : Pâture fraîche moyennement riche en espèces.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| Création, mauvais état visé | 2 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 27,08 m²HE, 15 à 30 cm 32,5 m²HE, 30 à 80 cm 37,92 m²HE, 80 cm et plus 48,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5,4 | 10,8 | 21,7 | 48,8 | 54,2 | 54,2 | 54,2 | 54,2 | 2 411 |
| moyen | 0 | 9,5 | 19 | 37,9 | 47,4 | 47,4 | 47,4 | 47,4 | 47,4 | 2 228 |
| mauvais | 0 | 19 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 1 839 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H073. E2.2 : Prairies de fauche de basse et moyenne altitude

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.2 |
| EUNIS 2012 | E2.2 |
| EUNIS 2022 (HabRef) | R2-2 Prairies de fauche de basse et moyenne altitudes |
| CORINE Biotopes (HabRef) | 38.2 Prairies de fauche de basse altitude, 38.21 Prairies de fauche atlantiques, 38.22 Prairies de fauche des plaines médio-européennes, 38.23 Prairies de fauche submontagnardes médio-européennes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Prairies de fauche mésotrophes de basse et moyenne altitude, fertilisées et bien drainées, à fromental, avoine dorée, cerfeuil sauvage, berce, carotte, knautie, marguerite, géranium des prés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (113 taxons ; les 40 plus cités) : Arrhenatherum elatius, Trisetum flavescens, Alopecurus pratensis, Knautia arvensis, Pastinaca sativa, Trifolium dubium, Crepis biennis, Pimpinella major, Campanula patula, Dactylis glomerata, Geranium pratense, Leucanthemum vulgare, Sanguisorba officinalis, Festuca pratensis, Poa pratensis, Trifolium repens, Alchemilla xanthochlora, Bromus erectus, Festuca rubra, Daucus carota, Alopecurus rendlei, Alopecurus utriculatus, Geranium sylvaticum, Pimpinella saxifraga, Potentilla erecta, Ranunculus bulbosus, Anthriscus sylvestris, Heracleum sphondylium, Alopecurus sp., Deschampsia cespitosa, Filipendula ulmaria, Anthoxanthum odoratum, Holcus lanatus, Malva moschata, Sanguisorba minor, Arrhenatherum elatius ssp. bulbosum, Equisetum arvense, Galium album, Picris hieracioides, Medicago sativa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 34.07a.01, « Artenreiche, frische Mähwiese », Biotoptypenwert 20 sur 24 (ligne 337 de l'extraction) |

Correspondance retenue : Prairie de fauche fraîche riche en espèces.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 19, « Grassland - Lowland meadows », condition cible mauvais |
| Amélioration, mauvais vers moyen | 8 ans | onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 8 ans | onglet G-5, ligne 20, « Grassland - Lowland meadows », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 20, « Grassland - Lowland meadows » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 20, « Grassland - Lowland meadows » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,8 | 3,7 | 7,3 | 16,5 | 25,7 | 27,5 | 27,5 | 27,5 | 1 155 |
| moyen | 0 | 2,4 | 4,8 | 9,6 | 21,7 | 24,1 | 24,1 | 24,1 | 24,1 | 1 071 |
| mauvais | 0 | 3,8 | 7,7 | 15,4 | 19,2 | 19,2 | 19,2 | 19,2 | 19,2 | 905 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H074. E2.3 : Prairies de fauche montagnardes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.3 |
| EUNIS 2012 | E2.3 |
| EUNIS 2022 (HabRef) | R2-3 Prairies de fauche de montagne |
| CORINE Biotopes (HabRef) | 38.3 Prairies de fauche de montagne |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Prairies de fauche mésotrophes à eutrophes, souvent riches en espèces, des étages montagnard et subalpin.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (31 taxons ; les 40 plus cités) : Trisetum flavescens, Cynosurus cristatus, Armeria rumelica, Rhinanthus rumelicus, Festuca pratensis, Knautia dinarica, Anthoxanthum odoratum, Campanula glomerata, Carum carvi, Crocus albiflorus, Lilium bulbiferum, Malva moschata, Muscari botryoides, Narcissus poeticus, Pimpinella major, Primula elatior, Salvia pratensis, Thlaspi caerulescens, Valeriana repens, Chaerophyllum hirsutum, Alchemilla sp., Crepis sp., Geranium sp., Silene sp., Viola sp., Trollius europaeus, Phyteuma sp., Astrantia major, Heracleum sphondylium, Polygonum bistorta, Centaurea nemoralis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 34.07a.01, « Artenreiche, frische Mähwiese », Biotoptypenwert 20 sur 24 (ligne 337 de l'extraction) |

Correspondance retenue : Prairie de fauche fraîche riche en espèces.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 27, « Grassland - Upland hay meadows » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 27, « Grassland - Upland hay meadows » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,7 | 5,5 | 12,4 | 19,2 | 26,1 | 27,5 | 27,5 | 1 086 |
| moyen | 0 | 1,6 | 3,2 | 6,4 | 14,4 | 22,5 | 24,1 | 24,1 | 24,1 | 1 011 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H075. E2.6 : Prairies améliorées, terrains de sport et pelouses ornementales

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.6 |
| EUNIS 2012 | E2.6 |
| EUNIS 2022 (HabRef) | V3-1 Prairies améliorées, réensemencées et fortement fertilisées, y compris les terrains de sport et les gazons |
| CORINE Biotopes (HabRef) | 81 Prairies améliorées, 81.1 Prairies sèches améliorées, 81.2 Prairies humides améliorées, 85.1 Grands parcs, 85.12 Pelouses de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP1 (prairies de faible valeur) |

**Définition**

Prairies permanentes fortement fertilisées ou réensemencées, parfois désherbées sélectivement, à flore et faune très appauvries, utilisées pour le pâturage, la protection des sols, l'agrément ou les loisirs, terrains de sport compris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 34.08a.01, « Intensiv genutztes, frisches Dauergrünland », Biotoptypenwert 8 sur 24 (ligne 345 de l'extraction) |

Correspondance retenue : Prairie permanente intensive.

**Grille d'état EP1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Fourrés sur moins de 20 % de la surface de la prairie | non |
| D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface | non |
| E | Sol nu entre 1 % et 10 % de la surface | non |
| F | Fougère aigle sur moins de 20 % de la surface | non |
| G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 7 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| Création, état moyen visé | 4 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 33,33 |
| État moyen | 29,16 |
| Mauvais état | 23,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 16,66 m²HE, 15 à 30 cm 20 m²HE, 30 à 80 cm 23,33 m²HE, 80 cm et plus 30 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,8 | 9,5 | 19 | 33,3 | 33,3 | 33,3 | 33,3 | 33,3 | 1 533 |
| moyen | 0 | 7,3 | 14,6 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 385 |
| mauvais | 0 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 1 143 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H076. E2.7 : Prairies mésiques non gérées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.7 |
| EUNIS 2012 | E2.7 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Prairies mésiques qui ne sont actuellement ni fauchées ni pâturées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 34.07b.03, « Mäßig artenreiche, frische Grünlandbrache », Biotoptypenwert 11 sur 24 (ligne 343 de l'extraction) |

Correspondance retenue : Prairie fraîche en déprise moyennement riche en espèces.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible moyen |
| Création, mauvais état visé | 2 ans | onglet G-4, ligne 22, « Grassland - Other neutral grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 23, « Grassland - Other neutral grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 23, « Grassland - Other neutral grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 22,91 m²HE, 15 à 30 cm 27,5 m²HE, 30 à 80 cm 32,08 m²HE, 80 cm et plus 41,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,6 | 9,2 | 18,3 | 41,2 | 45,8 | 45,8 | 45,8 | 45,8 | 2 039 |
| moyen | 0 | 8 | 16 | 32,1 | 40,1 | 40,1 | 40,1 | 40,1 | 40,1 | 1 885 |
| mauvais | 0 | 16 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 1 556 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H077. E2.8 : Pelouses mésophiles piétinées à annuelles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E2.8 |
| EUNIS 2012 | E2.8 |
| EUNIS 2022 (HabRef) | V3-5 Pelouses mésophiles piétinées à espèces annuelles |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP1 (prairies de faible valeur) |

**Définition**

Végétations basses d'annuelles des lieux mésophiles piétinés, à sagines, spergulaire rouge, jonc des crapauds, pâturin couché.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (6 taxons ; les 40 plus cités) : Juncus bufonius, Poa supina, Sagina apetala, Sagina procumbens, Spergularia rubra, Veronica serpyllifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 34.09, « Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) », Biotoptypenwert 8 sur 24 (ligne 349 de l'extraction) |

Correspondance retenue : Gazon piétiné.

**Grille d'état EP1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Fourrés sur moins de 20 % de la surface de la prairie | non |
| D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface | non |
| E | Sol nu entre 1 % et 10 % de la surface | non |
| F | Fougère aigle sur moins de 20 % de la surface | non |
| G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 7 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible bon |
| Création, état moyen visé | 4 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 20, « Grassland - Modified grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 21, « Grassland - Modified grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 21, « Grassland - Modified grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 33,33 |
| État moyen | 29,16 |
| Mauvais état | 23,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 16,66 m²HE, 15 à 30 cm 20 m²HE, 30 à 80 cm 23,33 m²HE, 80 cm et plus 30 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,8 | 9,5 | 19 | 33,3 | 33,3 | 33,3 | 33,3 | 33,3 | 1 533 |
| moyen | 0 | 7,3 | 14,6 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 385 |
| mauvais | 0 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 1 143 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H078. E3.1 : Prairies humides hautes méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E3.1 |
| EUNIS 2012 | E3.1 |
| EUNIS 2022 (HabRef) | R3-1 Prairies intérieures humides hautes méditerranéennes |
| CORINE Biotopes (HabRef) | 22.3 Communautés amphibies, 22.34 Groupements amphibies méridionaux, 22.344 Prairies à Serapias, 37.4 Prairies humides méditerranéennes à grandes herbes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Prairies humides méditerranéennes de hautes graminées et de joncs, à scirpe-jonc, agrostide stolonifère, molinie, choin noirâtre, orchidées des prairies humides.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (49 taxons ; les 40 plus cités) : Oenanthe lachenalii, Briza minor, Lolium multiflorum, Rumex conglomeratus, Agrostis reuteri, Agrostis stolonifera, Asteriscus aquaticus, Calamagrostis epigejos, Cirsium monspessulanum, Cirsium pyrenaicum, Cyperus longus, Dorycnium rectum, Erica terminalis, Eupatorium cannabinum, Euphorbia pubescens, Holoschoenus vulgaris, Hypericum tetrapterum, Hypericum tomentosum, Inula viscosa, Juncus maritimus, Lysimachia ephemerum, Molinia caerulea, Orchis laxiflora, Pulicaria dysenterica, Sanguisorba officinalis, Schoenus nigricans, Senecio doria, Serratula tinctoria, Silaum silaus, Succisa pratensis, Trifolium resupinatum, Sonchus maritimus ssp. aquatilis, Galium debile, Melica cupanii, Dactylorhiza elata, Genista tinctoria, Juncus acutus, Oenanthe pimpinelloides, Scirpus holoschoenus, Tetragonolobus maritimus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 35.02.03a.01, « – Bewirtschaftet », Biotoptypenwert 20 sur 24 (ligne 362 de l'extraction) |

Correspondance retenue : Autre prairie humide extensive exploitée.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,7 | 8,2 | 12,8 | 17,4 | 26,6 | 27,5 | 949 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H079. E3.2 : Prairies humides rases méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E3.2 |
| EUNIS 2012 | E3.2 |
| EUNIS 2022 (HabRef) | R3-2 Prairies humides basses méditerranéennes de basse altitude, R3-3 Prairies humides basses méditerranéennes de montagne |
| CORINE Biotopes (HabRef) | 37.5 Prairies humides méditerranéennes rases |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Prairies très rases des sols compacts imperméables ou des marnes, humides une grande partie de l'année et desséchées en été, de la région méditerranéenne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (7 taxons ; les 40 plus cités) : Centaurium pulchellum, Deschampsia media, Lotus tenuis, Prunella hyssopifolia, Trifolium lappaceum, Plantago maritima ssp. serpentina, Centaurea timbali.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 35.02.03a.01, « – Bewirtschaftet », Biotoptypenwert 20 sur 24 (ligne 362 de l'extraction) |

Correspondance retenue : Autre prairie humide extensive exploitée.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,8 | 3,7 | 8,2 | 12,8 | 17,4 | 26,6 | 27,5 | 949 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H080. E3.4 : Prairies eutrophes et mésotrophes humides

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E3.4 |
| EUNIS 2012 | E3.4 |
| EUNIS 2022 (HabRef) | R3-5 Prairies de fauche eutrophes à mésotrophes humides ou mouilleuses, R3-6 Pâtures mésotrophes à eutrophes humides ou mouilleuses |
| CORINE Biotopes (HabRef) | 37.2 Prairies humides eutrophes, 37.21 Prairies humides atlantiques et subatlantiques, 37.211 Prairies humides à cirse des maraîchers, 37.212 Prairies humides à Trolle et Cirse des ruisseaux, 37.213 Prairies à Canche cespiteuse, 37.214 Prairies à Séneçon aquatique, 37.215 Prairies à Renouée bistorte, 37.216 Prairies à Jonc filiforme, 37.217 Prairies à Jonc diffus, 37.218 Prairies à Jonc subnoduleux, et 7 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Prairies humides et prairies inondables eutrophes ou mésotrophes, dominées par des graminées, des joncs ou le scirpe des bois.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (164 taxons ; les 40 plus cités) : Deschampsia cespitosa, Polygonum bistorta, Angelica sylvestris, Juncus inflexus, Juncus effusus, Scirpus sylvaticus, Trollius europaeus, Molinia caerulea, Cirsium palustre, Filipendula ulmaria, Holcus lanatus, Alopecurus pratensis, Festuca pratensis, Cirsium rivulare, Caltha palustris, Ranunculus acris, Juncus filiformis, Equisetum palustre, Cirsium oleraceum, Rumex acetosa, Lychnis flos-cuculi, Myosotis palustris, Agrostis stolonifera, Alopecurus geniculatus, Carex nigra, Juncus balticus, Juncus subnodulosus, Dactylorhiza fuchsii, Lotus uliginosus, Mentha aquatica, Cirsium helenioides, Bromus racemosus, Crepis paludosa, Fritillaria meleagris, Geum rivale, Gratiola officinalis, Oenanthe silaifolia, Senecio aquaticus, Telekia speciosa, Agropyron repens.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 35.02.05.01, « – Extensiv bewirtschaftet », Biotoptypenwert 18 sur 24 (ligne 365 de l'extraction) |

Correspondance retenue : Prairie inondable extensive.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 16, « Grassland - Floodplain wetland mosaic and CFGM », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 4 ans | onglet G-5, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 17, « Grassland - Floodplain wetland mosaic and CFGM » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,2 | 2,5 | 5 | 11,1 | 17,3 | 23,5 | 24,8 | 24,8 | 978 |
| moyen | 0 | 2,2 | 4,3 | 8,7 | 19,5 | 21,7 | 21,7 | 21,7 | 21,7 | 964 |
| mauvais | 0 | 3,5 | 6,9 | 13,9 | 17,3 | 17,3 | 17,3 | 17,3 | 17,3 | 814 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H081. E3.5 : Prairies oligotrophes humides

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E3.5 |
| EUNIS 2012 | E3.5 |
| EUNIS 2022 (HabRef) | R3-7 Prairies oligotrophes humides ou mouilleuses tempérées et boréales |
| CORINE Biotopes (HabRef) | 37.3 Prairies humides oligotrophes, 37.31 Prairies à Molinie et communautés associées, 37.311 Prairies à Molinie sur calcaires, 37.312 Prairies à Molinie acidiphiles, 37.32 Prairies à Jonc rude et pelouses humides à Nard |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Prairies des sols humides pauvres en nutriments, souvent tourbeux : prairies acides à molinie et prairies humides basses à jonc rude, nard et scirpe cespiteux.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (70 taxons ; les 40 plus cités) : Galium boreale, Molinia caerulea, Nardus stricta, Betonica officinalis, Carex pallescens, Carex tomentosa, Deschampsia cespitosa, Dianthus superbus, Gentiana pneumonanthe, Parnassia palustris, Potentilla erecta, Selinum carvifolia, Serratula tinctoria, Silaum silaus, Succisa pratensis, Tetragonolobus maritimus, Cirsium dissectum, Inula salicina, Ophioglossum vulgatum, Stachys officinalis, Cirsium tuberosum, Juncus squarrosus, Scirpus cespitosus, Allium angulosum, Allium suaveolens, Carex panicea, Dactylorhiza maculata, Festuca rubra, Gentiana asclepiadea, Gladiolus palustris, Iris sibirica, Laserpitium prutenicum, Lathyrus pannonicus, Festuca arundinacea, Trollius europaeus, Molinia arundinacea, Molinia caerulea ssp. arundinacea, Achillea millefolium, Bartsia alpina, Carex acuta.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9583 m²HE/m² | 0,8625 à 1 | code 35.02.01a, « – Bewirtschaftet », Biotoptypenwert 23 sur 24 (ligne 356 de l'extraction) |

Correspondance retenue : Prairie à molinie exploitée.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 87, « Wetland - Purple moor grass and rush pastures », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 88, « Wetland - Purple moor grass and rush pastures », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 108, « Wetland - Purple moor grass and rush pastures » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 95,83 |
| État moyen | 83,85 |
| Mauvais état | 67,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 47,91 m²HE, 15 à 30 cm 57,5 m²HE, 30 à 80 cm 67,08 m²HE, 80 cm et plus 86,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,1 | 2,1 | 4,2 | 9,5 | 14,8 | 20 | 30,6 | 31,6 | 1 091 |
| moyen | 0 | 1,4 | 2,8 | 5,5 | 12,5 | 19,4 | 26,3 | 27,7 | 27,7 | 1 093 |
| mauvais | 0 | 2,2 | 4,4 | 8,9 | 19,9 | 22,1 | 22,1 | 22,1 | 22,1 | 985 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H082. E4.1 : Combes à neige avec végétation

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E4.1 |
| EUNIS 2012 | E4.1 |
| EUNIS 2022 (HabRef) | R4-1 Combes à neige avec végétation |
| CORINE Biotopes (HabRef) | 36.1 Communautés des combes à neige, 36.11 Communautés des combes à neige acidiphiles, 36.111 Communautés acidiphiles des combes à neige alpines, 36.1111 Communautés acidiphiles des combes à neige alpines à mousses, 36.1113 Communautés acidiphiles de combes à neige alpines à Carex-Gnaphalium, 36.12 Communautés de combes à neige sur substrats calcaires, 36.121 Communautés des combes à neige sur calcaires à Arabis-Gnaphalium |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Zones végétalisées où la neige persiste tard dans la saison, dominées par des mousses, des hépatiques, des lichens, des graminoïdes et de petites herbes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (108 taxons ; les 40 plus cités) : Oxyria digyna, Salix herbacea, Saxifraga oppositifolia, Ranunculus nivalis, Arabis caerulea, Ranunculus alpestris, Cerastium cerastoides, Carex lachenalii, Ranunculus pygmaeus, Poa arctica, Ranunculus sulphureus, Ranunculus glacialis, Carex atrata, Saxifraga androsacea, Polytrichum juniperinum, Polytrichum sexangulare, Anthelia juratzkana, Pohlia commutata, Kiaeria falcata, Dicranum falcatum, Omalotheca supina, Gnaphalium supinum, Hutchinsia alpina, Cerastium arcticum, Juncus biglumis, Saxifraga rivularis, Saxifraga tenuis, Bistorta vivipara, Poa alpina, Polygonum viviparum, Viola biflora, Minuartia biflora, Saussurea alpina, Trisetum spicatum, Lidia biflora, Potentilla hyparctica, Cerastium sp., Draba crassifolia, Luzula confusa, Luzula arctica.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 64.01, « Kalkschneeboden », Biotoptypenwert 17 sur 24 (ligne 843 de l'extraction) |

Correspondance retenue : Combe à neige calcaire.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,8 | 1,6 | 3,3 | 7,4 | 11,5 | 15,5 | 20,5 | 20,5 | 757 |
| mauvais | 0 | 1,1 | 2,2 | 4,4 | 9,8 | 15,3 | 16,4 | 16,4 | 16,4 | 687 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H083. E4.2 : Sommets et crêtes à mousses et lichens

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E4.2 |
| EUNIS 2012 | E4.2 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Sommets, crêtes et pentes exposés des montagnes, dominés par les mousses et les lichens.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (3 taxons ; les 40 plus cités) : Carex bigelowii, Racomitrium lanuginosum, Racomitrium sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 68.01, « Alpine „Windheide“ (z. B. mit Gamsheide) », Biotoptypenwert 19 sur 24 (ligne 863 de l'extraction) |

Correspondance retenue : Lande alpine ventée.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,6 | 3,3 | 7,3 | 11,4 | 15,5 | 23,7 | 26,1 | 875 |
| moyen | 0 | 0,9 | 1,8 | 3,7 | 8,2 | 12,8 | 17,4 | 22,9 | 22,9 | 846 |
| mauvais | 0 | 1,2 | 2,4 | 4,9 | 11 | 17,1 | 18,3 | 18,3 | 18,3 | 768 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H084. E4.3 : Pelouses alpines et subalpines acidiphiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E4.3 |
| EUNIS 2012 | E4.3 |
| EUNIS 2022 (HabRef) | R4-2 Boreal and arctic acidophilous alpine grassland, R4-3 Pelouses alpines acidiphiles tempérées |
| CORINE Biotopes (HabRef) | 36.3 Pelouses acidiphiles alpines et subalpines, 36.31 Gazons à Nard raide et groupements apparentés, 36.311 Nardaies mésophiles pyrénéo-alpines, 36.312 Nardaies pyrénéo-alpines hygrophiles, 36.313 Pelouses pyrénéo-alpines hygrophiles à Vulpins, 36.314 Pelouses pyrénéennes fermées à Festuca eskia, 36.315 Pelouses pyrénéennes à Poa violacea, 36.316 Nardaies sommitales hercyniennes, 36.3161 Nardaies sommitales des Hautes-Chaumes, 36.3162 Gazons sommitaux de la Forêt noire à Nard raide, et 17 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses alpines et subalpines des roches cristallines, des substrats pauvres en calcaire ou des sols décalcifiés, à jonc trifide, arméries, gentianes, benoîte des montagnes, phytéume hémisphérique.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (244 taxons ; les 40 plus cités) : Nardus stricta, Juncus trifidus, Festuca airoides, Festuca supina, Carex curvula, Bellardiochloa violacea, Agrostis rupestris, Oreochloa disticha, Poa violacea, Hieracium alpinum, Festuca indigesta, Sesleria comosa, Poa media, Festuca eskia, Potentilla aurea ssp. chrysocraspeda, Alopecurus gerardii, Festuca paniculata, Minuartia recurva, Festuca valida, Avenula versicolor, Festuca riloensis, Festuca varia, Festuca nigrescens, Carex ericetorum, Carex sempervirens, Potentilla aurea, Gentiana punctata, Ranunculus pyrenaeus, Trifolium alpinum, Luzula spicata, Pulsatilla alpina, Senecio carpathicus, Lychnis alpina, Verbascum longifolium, Genista depressa, Poa ursina, Plantago holosteum, Anthoxanthum odoratum, Potentilla ternata, Festuca halleri.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 66.09, « Krummseggenrasen », Biotoptypenwert 19 sur 24 (ligne 858 de l'extraction) |

Correspondance retenue : Pelouse à laîche courbée.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 24, « Grassland - Upland acid grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 25, « Grassland - Upland acid grassland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 25, « Grassland - Upland acid grassland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 25, « Grassland - Upland acid grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5,3 | 10,6 | 21,1 | 47,5 | 73,9 | 79,2 | 79,2 | 79,2 | 3 325 |
| moyen | 0 | 6,9 | 13,9 | 27,7 | 62,3 | 69,3 | 69,3 | 69,3 | 69,3 | 3 083 |
| mauvais | 0 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 2 716 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H085. E4.4 : Pelouses alpines et subalpines calcicoles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E4.4 |
| EUNIS 2012 | E4.4 |
| EUNIS 2022 (HabRef) | R4-4 Pelouses calcicoles arctico-alpines, R4-5 Pelouses calcaires alpines et subalpines des Balkans et des Apennins |
| CORINE Biotopes (HabRef) | 36.4 Pelouses calcicoles alpines et subalpines, 36.41 Pelouses à laîche ferrugineuse et communautés apparentées, 36.411 Pelouses mésophiles à laîche sempervirente, 36.4111 Pelouses à laîche sempervirente des Alpes, 36.4112 Pelouses pyrénéennes à laîche sempervirente, 36.412 Pelouses à laîche ferrugineuse septentrionales, 36.414 Pelouses à fétuque violette et communautés apparentées, 36.4141 Pelouses alpines à fétuque violette, 36.4142 Pelouses pyrénéennes à fétuque noircissante, 36.416 Pelouses sommitales du Jura, et 10 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pelouses alpines et subalpines des sols riches en bases des hautes montagnes, à dryade, gentianes, alchémilles, anthyllide, aster des Alpes, hélianthèmes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (274 taxons ; les 40 plus cités) : Carex sempervirens, Elyna myosuroides, Kobresia myosuroides, Sesleria albicans, Carex kitaibeliana, Dryas octopetala, Sesleria korabensis, Sesleria tenuifolia, Carex firma, Ranunculus thora, Helictotrichon montanum, Festuca sp., Sesleria sp., Festuca amethystina, Festuca versicolor, Trifolium thalii, Carex ferruginea, Leontopodium alpinum, Phyteuma orbiculare, Carex laevis, Oxytropis pyrenaica, Sesleria rigida, Festuca saxatilis, Sesleria bielzii, Sesleria rigida ssp. haynaldiana, Festuca penzesii, Bartsia alpina, Draba aizoides, Scabiosa cinerea, Astrantia major, Horminum pyrenaicum, Oxytropis sp., Carex humilis, Helianthemum alpestre, Helianthemum nummularium ssp. grandiflorum, Sesleria klasterskyi, Acinos alpinus, Daphne oleoides, Iberis sempervirens, Minuartia verna.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 66.02, « Polsterseggenrasen », Biotoptypenwert 17 sur 24 (ligne 851 de l'extraction) |

Correspondance retenue : Pelouse à laîche ferme.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 25 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 25, « Grassland - Upland calcareous grassland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 26, « Grassland - Upland calcareous grassland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 26, « Grassland - Upland calcareous grassland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,9 | 3,7 | 8,4 | 13,1 | 17,8 | 23,4 | 23,4 | 865 |
| moyen | 0 | 1,4 | 2,7 | 5,5 | 12,3 | 19,1 | 20,5 | 20,5 | 20,5 | 859 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H086. E4.5 : Prairies alpines et subalpines fertilisées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E4.5 |
| EUNIS 2012 | E4.5 |
| EUNIS 2022 (HabRef) | V3-6 Prairies alpines et subalpines fertilisées |
| CORINE Biotopes (HabRef) | 36.5 Prairies alpines et subalpines fertilisées, 36.51 Prairies subalpines à Trisetum flavescens, 36.52 Pâturages à Liondent hispide |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Pâtures enrichies des étages subalpin et alpin inférieur. Les prairies de fauche enrichies relèvent de E2.3.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (18 taxons ; les 40 plus cités) : Trisetum flavescens, Alchemilla sp., Agrostis capillaris, Anthoxanthum odoratum, Astrantia elatior, Festuca fallax, Nardus stricta, Pancicia serbica, Rhinanthus rumelicus, Leucanthemum vulgare, Agrostis alpina, Cerastium fontanum, Crepis aurea, Leontodon hispidus, Phleum alpinum, Poa alpina, Trifolium badium, Trifolium thalii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 66.06, « Alpenfettweide », Biotoptypenwert 14 sur 24 (ligne 855 de l'extraction) |

Correspondance retenue : Pâturage gras alpin.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 26, « Grassland - Upland hay meadows », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 27, « Grassland - Upland hay meadows », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 27, « Grassland - Upland hay meadows » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 27, « Grassland - Upland hay meadows » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 58,33 |
| État moyen | 51,04 |
| Mauvais état | 40,83 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 29,17 m²HE, 15 à 30 cm 35 m²HE, 30 à 80 cm 40,83 m²HE, 80 cm et plus 52,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1 | 1,9 | 3,8 | 8,7 | 13,5 | 18,3 | 19,2 | 19,2 | 760 |
| moyen | 0 | 1,1 | 2,2 | 4,5 | 10,1 | 15,7 | 16,8 | 16,8 | 16,8 | 707 |
| mauvais | 0 | 1,3 | 2,7 | 5,4 | 12,1 | 13,5 | 13,5 | 13,5 | 13,5 | 600 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H087. E5.1 : Végétations herbacées anthropiques

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E5.1 |
| EUNIS 2012 | E5.1 |
| EUNIS 2022 (HabRef) | V3-7 Végétations herbacées annuelles anthropiques, V3-8 Végétations herbacées vivaces anthropiques sèches, V3-9 Végétations herbacées vivaces anthropiques mésiques |
| CORINE Biotopes (HabRef) | 87 Terrains en friche et terrains vagues, 87.2 Zones rudérales |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Peuplements d'herbacées qui se développent sur des terrains urbains ou agricoles abandonnés, des terrains remis en état, les réseaux de transport ou les sites de dépôt de déchets.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Urtica dioica, Epilobium sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 39.06.03, « Frische bis nasse Ruderalstandorte », Biotoptypenwert 12 sur 24 (ligne 413 de l'extraction) |

Correspondance retenue : Stations rudérales fraîches à humides.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 10 | 20 | 40 | 50 | 50 | 50 | 50 | 50 | 2 350 |
| moyen | 0 | 14,6 | 29,2 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 100 |
| mauvais | 0 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 1 715 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H088. E5.2 : Ourlets forestiers thermophiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E5.2 |
| EUNIS 2012 | E5.2 |
| EUNIS 2022 (HabRef) | R5-1 Ourlets forestiers thermophiles des sols riches en bases, R5-2 Ourlets forestiers des sols acides pauvres en éléments nutritifs, R5-3 Macaronesian thermophilous forest fringe |
| CORINE Biotopes (HabRef) | 34.4 Lisières (ou ourlets) forestières thermophiles, 34.41 Lisières xéro-thermophiles, 34.42 Lisières mésophiles |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Ourlets herbacés et arbustifs thermophiles et résistants à la sécheresse, formant une ceinture entre les pelouses et le manteau forestier, côté ensoleillé, sur sols pauvres.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (33 taxons ; les 40 plus cités) : Origanum vulgare, Agrimonia eupatoria, Brachypodium sylvaticum, Campanula baumgartenii, Digitalis grandiflora, Lathyrus latifolius, Teucrium scorodonia, Trifolium medium, Trifolium ochroleucon, Valeriana wallrothii, Melampyrum sp., Vicia sp., Peucedanum cervaria, Anemone sylvestris, Anthericum ramosum, Clematis recta, Dictamnus albus, Geranium sanguineum, Lathyrus pannonicus, Melampyrum cristatum, Polygonatum odoratum, Rosa pimpinellifolia, Tanacetum corymbosum, Trifolium rubens, Veronica teucrium, Vincetoxicum hirundinaria, Fragaria viridis, Coronilla coronata, Bupleurum sp., Campanula sp., Inula sp., Peucedanum sp., Laserpitium latifolium.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 39.01.01, « Wald- und Gehölzsäume oligo- bis eutropher, trockener bis nasser Standorte », Biotoptypenwert 16 sur 24 (ligne 399 de l'extraction) |

Correspondance retenue : Lisières forestières oligo- à eutrophes.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 54, « Sparsely vegetated land - Tall forbs », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 55, « Sparsely vegetated land - Tall forbs », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 80, « Sparsely vegetated land - Tall forbs » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 80, « Sparsely vegetated land - Tall forbs » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 13,3 | 26,7 | 53,3 | 66,7 | 66,7 | 66,7 | 66,7 | 66,7 | 3 133 |
| moyen | 0 | 19,4 | 38,9 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 800 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H089. E5.3 : Formations à fougère aigle

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E5.3 |
| EUNIS 2012 | E5.3 |
| EUNIS 2022 (HabRef) | R5-4 Végétations à Pteridium aquilinum |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.86 Landes à Fougères, 31.861 Landes subatlantiques à Fougères, 31.863 Landes supra-méditerranéennes à Fougères |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP1 (prairies de faible valeur) |

**Définition**

Formations étendues et souvent fermées dominées par la fougère aigle.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Pteridium aquilinum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 39.07, « Artenarme Dominanzbestände von Poly-Kormonbildnern (z. B. von Adlerfarn oder Landreitgras) », Biotoptypenwert 10 sur 24 (ligne 414 de l'extraction) |

Correspondance retenue : Peuplements monospécifiques (fougère aigle).

**Grille d'état EP1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de faible valeur : au moins 6 à 8 espèces de plantes vasculaires par m², dont au moins 2 dicotylédones non nitrophiles (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant et cerfeuil sauvage exclus) | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Fourrés sur moins de 20 % de la surface de la prairie | non |
| D | Dégradations physiques (piétinement, engins, stockage, érosion) sur moins de 5 % de la surface | non |
| E | Sol nu entre 1 % et 10 % de la surface | non |
| F | Fougère aigle sur moins de 20 % de la surface | non |
| G | Absence d'espèces végétales exotiques envahissantes (liste de l'Union au titre du règlement (UE) n° 1143/2014 et liste nationale, à la place de l'annexe 9 du Wildlife and Countryside Act) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 15, « Grassland - Bracken », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 16, « Grassland - Bracken » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 16, « Grassland - Bracken » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 41,7 | 41,7 | 41,7 | 41,7 | 41,7 | 41,7 | 41,7 | 41,7 | 2 042 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H090. E5.4 : Lisières et prairies humides à grandes herbacées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E5.4 |
| EUNIS 2012 | E5.4 |
| EUNIS 2022 (HabRef) | R5-5 Lisières et prairies humides ou mouilleuses de basse altitude à grandes herbacées et à fougères |
| CORINE Biotopes (HabRef) | 24.5 Dépôts d'alluvions fluviatiles limoneuses, 24.53 Groupements méditerranéens des limons riverains, 37.1 Communautés à Reine des prés et communautés associées, 37.7 Lisières humides à grandes herbes, 37.71 Voiles des cours d'eau, 37.711 Communautés fluviales à Angelica archangelica, 37.712 Communautés fluviales à Angelica heterocarpa, 37.713 Ourlets à Althaea officinalis, 37.714 Communautés riveraines à Pétasites, 37.715 Ourlets riverains mixtes, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Végétations de hautes herbes et de fougères, souvent dominantes le long des cours d'eau, dans les prairies humides et à l'ombre des lisières forestières (mégaphorbiaies).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (40 taxons ; les 40 plus cités) : Filipendula ulmaria, Aegopodium podagraria, Chaerophyllum hirsutum, Achillea ptarmica, Dactylorhiza fuchsii, Galium uliginosum, Geum rivale, Lysimachia vulgaris, Trollius europaeus, Valeriana sambucifolia, Crepis paludosa, Geranium palustre, Alliaria petiolata, Carduus crispus, Geum urbanum, Glechoma hederacea, Lamium album, Silene dioica, Viola alba, Viola odorata, Galium aparine, Lapsana communis, Geranium robertianum, Angelica heterocarpa, Lythrum salicaria, Iris sibirica, Althaea officinalis, Angelica sylvestris, Caltha palustris, Epilobium hirsutum, Mentha longifolia, Urtica dioica, Petasites sp., Agrostis semiverticillata, Cyperus fuscus, Paspalum paspalodes, Paspalum vaginatum, Polypogon viridis, Catabrosa aquatica, Angelica archangelica ssp. litoralis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 39.04a.01, « – Naturnahe Ausprägung », Biotoptypenwert 17 sur 24 (ligne 407 de l'extraction) |

Correspondance retenue : Ourlets riverains herbacés naturels.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,6 | 3,1 | 7 | 10,9 | 14,8 | 22,6 | 23,4 | 806 |
| moyen | 0 | 1 | 2 | 4,1 | 9,2 | 14,3 | 19,4 | 20,5 | 20,5 | 808 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H091. E5.5 : Formations subalpines humides à grandes herbacées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E5.5 |
| EUNIS 2012 | E5.5 |
| EUNIS 2022 (HabRef) | R5-6 Lisières et prairies humides ou mouilleuses montagnardes à subalpines à grandes herbacées et à fougères |
| CORINE Biotopes (HabRef) | 37.8 Mégaphorbiaies alpines et subalpines, 37.81 Mégaphorbiaies des montagnes hercyniennes, du Jura et des Alpes, 37.82 Prairies subalpines à Calamagrostis arundinacea, 37.83 Mégaphorbiaies pyrénéo-ibériques, 37.85 Mégaphorbiaies corses à Cymbalaria, 37.86 Mégaphorbiaies corses à Doronicum, 37.88 Communautés alpines à Patience alpine |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EP2 (prairies de valeur moyenne à très haute) |

**Définition**

Mégaphorbiaies luxuriantes des sols profonds et humides des étages montagnard à alpin, surtout subalpin, à laitue des Alpes, cirses, géranium des bois, aconits, adénostyles, vérâtre, trolle.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (103 taxons ; les 40 plus cités) : Geum coccineum, Athyrium distentifolium, Adenostyles alliariae, Cicerbita alpina, Veratrum album, Cirsium appendiculatum, Peucedanum ostruthium, Valeriana pyrenaica, Athyrium alpestre, Dryopteris filix-mas, Chaerophyllum hirsutum, Aconitum sp., Trollius europaeus, Aconitum napellus, Aconitum nevadense, Cirsium spinosissimum, Geranium sylvaticum, Cirsium flavispina, Ranunculus platanifolius, Angelica sylvestris, Calamagrostis arundinacea, Calamagrostis villosa, Deschampsia cespitosa, Petasites albus, Alchemilla sp., Adenostyles alliariae ssp. hybrida, Adenostyles alliariae ssp. pyrenaica, Athyrium filix-femina, Dryopteris dilatata, Alchemilla plicatula, Pinguicula vulgaris, Petasites sp., Archangelica officinalis, Aconitum callibotryon, Delphinium oxysepalum, Aconitum firmum, Aconitum vulparia, Centaurea rhapontica, Leuzea rhapontica, Pedicularis foliosa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 67.01, « Hochstauden- und Hochgrasflur der hochmontanen bis alpinen Stufe », Biotoptypenwert 16 sur 24 (ligne 860 de l'extraction) |

Correspondance retenue : Mégaphorbiaie subalpine.

**Grille d'état EP2 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Prairie de valeur moyenne à très haute : exemple représentatif de son type, avec une forte proportion d'espèces indicatrices caractéristiques | oui |
| B | Hauteur de végétation variée : au moins 20 % sous 7 cm et au moins 20 % au-dessus | non |
| C | Sol nu entre 1 % et 5 % de la surface | non |
| D | Fougère aigle sur moins de 20 % et fourrés (ronce comprise) sur moins de 5 % de la surface | non |
| E | Espèces indicatrices d'un état dégradé et dégradations physiques cumulées sur moins de 5 % de la surface | non |
| F | Au moins 10 espèces de plantes vasculaires par m², dont des dicotylédones caractéristiques du type | oui |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 23, « Grassland - Tall herb communities (H6430) », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 30 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 24, « Grassland - Tall herb communities (H6430) », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 24, « Grassland - Tall herb communities (H6430) » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,3 | 13,9 | 21,3 | 22 | 759 |
| moyen | 0 | 1 | 1,9 | 3,9 | 8,7 | 13,5 | 18,3 | 19,3 | 19,3 | 760 |
| mauvais | 0 | 1,5 | 3,1 | 6,2 | 13,9 | 15,4 | 15,4 | 15,4 | 15,4 | 685 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H092. E6.1 : Steppes salées intérieures méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E6.1 |
| EUNIS 2012 | E6.1 |
| EUNIS 2022 (HabRef) | R6-1 Steppes salées intérieures méditerranéennes |
| CORINE Biotopes (HabRef) | 15.1 Gazons pionniers salés, 15.12 Groupements halonitrophiles à Frankenia, 15.8 Steppes salées méditerranéennes, 15.81 Steppes à Lavande de mer, 15.811 Steppes à Lavande de mer ibériques, 15.8114 Steppes à Lavande de mer catalano-provençales |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EZ1 (zones humides) |

**Définition**

Terres salées végétalisées des régions côtières méditerranéennes et des bords de bassins salés, souvent dominées par les statices ou le sparte, à sols temporairement imprégnés d'eau salée et très secs en été.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (27 taxons ; les 40 plus cités) : Limonium sp., Polypogon maritimus, Goniolimon sp., Lygeum spartum, Camphorosma monspeliaca, Centaurium pulchellum, Centaurium tenuiflorum, Elymus flaccidifolius, Halimione portulacoides, Inula crithmoides, Plantago crassifolia, Polypogon monspeliensis, Psilurus incurvus, Elymus elongatus ssp. ponticus, Puccinellia festuciformis ssp. convoluta, Petrosimonia sp., Parapholis marginata, Cressa cretica, Frankenia pulverulenta, Hordeum marinum, Parapholis strigosa, Salsola soda, Sphenopus divaricatus, Vella annua, Parapholis incurva, Suaeda splendens, Spergularia sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 35.03, « Salzgrünland des Binnenlandes », Biotoptypenwert 22 sur 24 (ligne 372 de l'extraction) |

Correspondance retenue : Prés salés de l'intérieur.

**Grille d'état EZ1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Nappe à la surface ou proche de la surface toute l'année, sans drainage artificiel | oui |
| B | Zone humide représentative de son type, espèces indicatrices régulièrement présentes | non |
| C | Eaux d'alimentation de bonne qualité, claires, sans signe de pollution | non |
| D | Fourrés et arbres épars sur moins de 10 % | non |
| E | Sol nu sur moins de 5 % | non |
| F | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % du sol | non |
| G | Litière continue empêchant la régénération sur 25 % au plus de la surface | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible bon |
| Création, état moyen visé | 7 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 115, « Coastal saltmarsh - Saltmarshes and saline reedbeds », condition cible mauvais |
| Amélioration, mauvais vers moyen | 6 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 14 ans | onglet G-5, ligne 116, « Coastal saltmarsh - Saltmarshes and saline reedbeds », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 4, « Coastal saltmarsh - Saltmarshes and saline reedbeds » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2 | 4 | 8,1 | 18,2 | 28,2 | 30,3 | 30,3 | 30,3 | 1 271 |
| moyen | 0 | 3,8 | 7,6 | 15,1 | 26,5 | 26,5 | 26,5 | 26,5 | 26,5 | 1 218 |
| mauvais | 0 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 21,2 | 1 038 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H093. E7.1 : Parcs boisés atlantiques

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E7.1 |
| EUNIS 2012 | E7.1 |
| EUNIS 2022 (HabRef) | R7-1 Pâturages et prairies boisés tempérés |
| CORINE Biotopes (HabRef) | 84.5 Parcs boisés |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Grandes étendues de prairies parsemées d'arbres plantés à larges espacements, des régions atlantiques, souvent closes et pâturées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |

Correspondance retenue : Forêt pâturée à usage traditionnel.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,1 | 2,6 | 4 | 5,4 | 8,3 | 9,2 | 307 |
| moyen | 0 | 0,3 | 0,5 | 1 | 2,3 | 3,5 | 4,8 | 7,3 | 8 | 269 |
| mauvais | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 6,4 | 6,4 | 6,4 | 6,4 | 286 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H094. E7.2 : Parcs boisés subcontinentaux

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E7.2 |
| EUNIS 2012 | E7.2 |
| EUNIS 2022 (HabRef) | R7-2 Pâturages et prairies boisés hémiboréaux et boréaux |
| CORINE Biotopes (HabRef) | 84.5 Parcs boisés |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Prairies parsemées d'arbres plantés à larges espacements, à l'est de la zone atlantique.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |

Correspondance retenue : Forêt pâturée à usage traditionnel.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,1 | 2,6 | 4 | 5,4 | 8,3 | 9,2 | 307 |
| moyen | 0 | 0,3 | 0,5 | 1 | 2,3 | 3,5 | 4,8 | 7,3 | 8 | 269 |
| mauvais | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 6,4 | 6,4 | 6,4 | 6,4 | 286 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H095. E7.3 : Dehesa

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | E7.3 |
| EUNIS 2012 | E7.3 |
| EUNIS 2022 (HabRef) | R7-3 Pâturages et prairies boisés méditerranéens |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Paysage du sud-ouest de la péninsule Ibérique où cultures, pâtures et maquis sont ombragés par un couvert plus ou moins ouvert de chênes indigènes (chêne-liège, chêne vert, chêne tauzin).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (7 taxons ; les 40 plus cités) : Aquila adalberti, Grus grus, Lynx pardinus, Quercus rotundifolia, Quercus suber, Quercus faginea, Quercus pyrenaica.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 42.04.01, « – Hudewald mit traditioneller Weidenutzung », Biotoptypenwert 22 sur 24 (ligne 513 de l'extraction) |

Correspondance retenue : Forêt pâturée à usage traditionnel.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 102, « Woodland and forest - Wood-pasture and parkland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 103, « Woodland and forest - Wood-pasture and parkland », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 123, « Woodland and forest - Wood-pasture and parkland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,6 | 1,1 | 2,6 | 4 | 5,4 | 8,3 | 9,2 | 307 |
| moyen | 0 | 0,3 | 0,5 | 1 | 2,3 | 3,5 | 4,8 | 7,3 | 8 | 269 |
| mauvais | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 6,4 | 6,4 | 6,4 | 6,4 | 286 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.5 Landes, fourrés et toundras (EUNIS F)

#### Fiche H096. F2.1 : Fourrés subarctiques et alpins à saules nains

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F2.1 |
| EUNIS 2012 | F2.1 |
| EUNIS 2022 (HabRef) | S2-1 Fourrés à Salix nains subarctiques et alpins |
| CORINE Biotopes (HabRef) | 36.1 Communautés des combes à neige, 36.11 Communautés des combes à neige acidiphiles, 36.111 Communautés acidiphiles des combes à neige alpines, 36.1112 Communautés acidiphiles des combes à neige alpines à Saule nain, 36.12 Communautés de combes à neige sur substrats calcaires, 36.122 Communautés des combes à neige sur calcaires, à Saules en espaliers |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés de saules nains, rarement plus hauts que 1,5 m, des combes à neige des montagnes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (68 taxons ; les 40 plus cités) : Salix reticulata, Salix polaris, Salix retusa, Polygonum viviparum, Salix kitaibeliana, Salix herbacea, Dryas octopetala, Poa alpina, Selaginella selaginoides, Silene acaulis, Thalictrum alpinum, Tofieldia pusilla, Viola biflora, Veronica alpina, Bistorta vivipara, Salix sp., Aster alpinus, Carex firma, Carex sempervirens, Pinguicula alpina, Equisetum variegatum, Antennaria alpina, Festuca vivipara, Bartsia alpina, Carex parviflora, Gentiana bavarica, Gnaphalium hoppeanum, Omalotheca hoppeana, Plantago montana, Ranunculus alpestris, Saxifraga androsacea, Saxifraga oppositifolia, Sesleria varia, Veronica aphylla, Anemone narcissiflora, Achillea schurii, Homogyne discolor, Saxifraga sempervivum, Sesleria rigida var. haynaldiana, Plantago atrata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 69.07, « Knieweidengebüsch », Biotoptypenwert 16 sur 24 (ligne 872 de l'extraction) |

Correspondance retenue : Fourré de saules nains.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,4 | 2,8 | 6,2 | 9,6 | 13,1 | 19,9 | 22 | 737 |
| moyen | 0 | 0,8 | 1,5 | 3,1 | 6,9 | 10,8 | 14,6 | 19,3 | 19,3 | 712 |
| mauvais | 0 | 1 | 2,1 | 4,1 | 9,2 | 14,4 | 15,4 | 15,4 | 15,4 | 647 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H097. F2.2 : Landes et fourrés sempervirents alpins et subalpins

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F2.2 |
| EUNIS 2012 | F2.2 |
| EUNIS 2022 (HabRef) | S2-2 Landes à éricoïdes alpines et subalpines, S2-3 Fourrés à Juniperus alpins et subalpins |
| CORINE Biotopes (HabRef) | 31.4 Landes alpines et boréales, 31.41 Landes naines à Azalée et à Vaccinium, 31.411 Landes à Loiseleuria, 31.412 Landes alpines à Vaccinium, 31.42 Landes à Rhododendron, 31.43 Fourrés à Genévriers nains, 31.431 Fourrés à Juniperus communis subsp. nana, 31.432 Fourrés à Juniperus sabina, 31.433 Fourrés à Juniperus communis subsp. hemisphaerica, 31.44 Landes à Empetrum et Vaccinium, et 4 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Formations naines ou prostrées des étages alpin et subalpin, dominées par des éricacées, la dryade, des genévriers nains ou des genêts.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (102 taxons ; les 40 plus cités) : Dryas octopetala, Dryas sp., Vaccinium sp., Empetrum hermaphroditum, Vaccinium vitis-idaea, Vaccinium myrtillus, Juniperus nana, Vaccinium uliginosum, Arctostaphylos alpinus, Loiseleuria procumbens, Arctostaphylos uva-ursi, Bruckenthalia sp., Bruckenthalia spiculifolia, Juniperus sabina, Rhododendron myrtifolium, Calluna vulgaris, Betula nana, Erica herbacea, Cetraria islandica, Vaccinium gaultherioides, Vaccinium uliginosum ssp. microphyllum, Rhododendron ferrugineum, Daphne striata, Globularia cordifolia, Racomitrium lanuginosum, Campanula serrata, Campanula abietina, Potentilla aurea ssp. chrysocraspeda, Empetrum nigrum, Salix sp., Clematis alpina, Daphne mezereum, Rhododendron hirsutum, Rhodothamnus chamaecistus, Rhododendron intermedium, Phyllodoce caerulea, Erica carnea, Globularia nudicaulis, Polygala chamaebuxus, Sesleria albicans.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 69.05, « Alpenrosengebüsch », Biotoptypenwert 17 sur 24 (ligne 870 de l'extraction) |

Correspondance retenue : Fourré à rhododendron.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,8 | 1,6 | 3,3 | 7,4 | 11,5 | 15,5 | 20,5 | 20,5 | 757 |
| mauvais | 0 | 1,1 | 2,2 | 4,4 | 9,8 | 15,3 | 16,4 | 16,4 | 16,4 | 687 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H098. F2.3 : Fourrés subalpins caducifoliés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F2.3 |
| EUNIS 2012 | F2.3 |
| EUNIS 2022 (HabRef) | S2-5 Fourrés caducifoliés subalpins et subarctiques |
| CORINE Biotopes (HabRef) | 31.6 Fourrés subalpins et communautés de hautes herbes (mégaphorbiaies), 31.61 Broussailles d'Aulnes verts, 31.611 Fourrés d'Aulnes verts des Alpes, 31.612 Broussailles corses d'Alnus viridis subsp. suaveolens, 31.62 Fourrés de Saules, 31.621 Fourrés de Saules pyrénéo-alpiens, 31.6211 Brousses à Saules bas des Alpes, 31.6212 Brousses alpiennes à Saules prostrés, 31.6213 Brousses alpiennes de Saules élevés, 31.6214 Broussailles de Saules pyrénéens, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés subalpins d'aulnes, de bouleaux, de saules et de rosacées (amélanchier, sorbiers, ronces), de moins de 5 m, souvent accompagnés de hautes herbes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (65 taxons ; les 40 plus cités) : Salix sp., Alnus viridis, Betula carpatica, Padus petraea, Sorbus aucuparia ssp. glabrata, Prunus padus ssp. borealis, Lonicera nigra, Sorbus sp., Salix waldsteiniana, Rubus sp., Alnus viridis ssp. viridis, Salix silesiaca, Amelanchier sp., Betula sp., Potentilla sp., Vaccinium sp., Betula pubescens, Cirsium waldsteinii, Pulmonaria filarszkyana, Rumex arifolius ssp. carpaticus, Geum coccineum, Ligusticum mutellina, Rumex alpinus, Veratrum album, Sorbus chamaemespilus, Sorbus mougeotii, Sorbus ambigua, Sorbus austriaca, Salix appendiculata, Salix elaeagnos, Salix purpurea, Salix lapponum, Rubus idaeus, Rubus saxatilis, Prunus sp., Alnus sp., Acer pseudoplatanus, Sorbus aucuparia, Alnus viridis ssp. suaveolens, Rhamnus alpinus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 69.02, « Grünerlengebüsche », Biotoptypenwert 15 sur 24 (ligne 867 de l'extraction) |

Correspondance retenue : Aulnaie verte.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 31,25 m²HE, 15 à 30 cm 37,5 m²HE, 30 à 80 cm 43,75 m²HE, 80 cm et plus 56,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 9 | 12,2 | 18,7 | 20,6 | 691 |
| moyen | 0 | 0,7 | 1,4 | 2,9 | 6,5 | 10,1 | 13,7 | 18 | 18 | 668 |
| mauvais | 0 | 1 | 1,9 | 3,9 | 8,7 | 13,5 | 14,4 | 14,4 | 14,4 | 606 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H099. F2.4 : Fourrés de conifères proches de la limite des arbres

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F2.4 |
| EUNIS 2012 | F2.4 |
| EUNIS 2022 (HabRef) | S2-6 Fourrés à Pinus mugo subalpins, S2-7 Krummholz avec des conifères autres que Pinus mugo |
| CORINE Biotopes (HabRef) | 31.5 Fourré bas de Pins mugo, 31.51 Fourrés bas de Pins mugo des Alpes internes, 31.53 Fourrés bas de Pins mugo des Alpes sud-occidentales |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés de conifères nains ou tordus proches de la limite des arbres, à couvert souvent incomplet (pin couché notamment).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (38 taxons ; les 40 plus cités) : Pinus mugo, Vaccinium myrtillus, Homogyne alpina, Arctostaphylos uva-ursi, Erica herbacea, Rhododendron hirsutum, Salix silesiaca, Rosa pendulina, Sorbus aucuparia, Arctostaphylos alpinus, Rhododendron ferrugineum, Rhodothamnus chamaecistus, Trientalis europaea, Polygonatum verticillatum, Rubus idaeus, Rubus saxatilis, Veratrum album, Sorbus aucuparia ssp. glabrata, Campanula abietina, Campanula patula ssp. abietina, Ribes petraeum var. carpaticum, Soldanella hungarica ssp. major, Empetrum hermaphroditum, Lonicera alpigena, Lonicera caerulea, Sorbus chamaemespilus, Vaccinium vitis-idaea, Calamagrostis varia, Carex firma, Daphne striata, Juniperus nana, Adenostyles alliariae, Calamagrostis villosa, Luzula sylvatica, Pinus cembra, Ribes petraeum, Soldanella carpatica, Rhododendron myrtifolium.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 69.04, « Latschengebüsch », Biotoptypenwert 15 sur 24 (ligne 869 de l'extraction) |

Correspondance retenue : Fourré de pin couché.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible moyen |
| Création, mauvais état visé | 15 ans | onglet G-4, ligne 35, « Heathland and shrub - Mountain heaths and willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 36, « Heathland and shrub - Mountain heaths and willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 31,25 m²HE, 15 à 30 cm 37,5 m²HE, 30 à 80 cm 43,75 m²HE, 80 cm et plus 56,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 9 | 12,2 | 18,7 | 20,6 | 691 |
| moyen | 0 | 0,7 | 1,4 | 2,9 | 6,5 | 10,1 | 13,7 | 18 | 18 | 668 |
| mauvais | 0 | 1 | 1,9 | 3,9 | 8,7 | 13,5 | 14,4 | 14,4 | 14,4 | 606 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H100. F3.1 : Fourrés tempérés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F3.1 |
| EUNIS 2012 | F3.1 |
| EUNIS 2022 (HabRef) | S3-2 Fourrés à Rubus tempérés, S3-4 Balkan-Anatolian submontane genistoid scrub, S3-5 Fourrés épineux tempérés et subméditerranéens, S3-6 Low steppic scrub, S3-7 Fourrés à Corylus avellana, S3-8 Fourrés des clairières des forêts tempérées |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.81 Fourrés médio-européens sur sol fertile, 31.811 Fruticées à Prunus spinosa et halliers à Rubus fruticosus, 31.8111 Fruticées subatlantiques Prunus spinosa et Rubus fruticosus, 31.8112 Fruticées atlantiques Prunus spinosa et Rubus fruticosus, 31.812 Fruticées à Prunelliers et Troènes, 31.8121 Fruticées atlantiques et médio-européennes à Prunelliers et Troènes, 31.81211 Fruticées médio-européennes à Prunelliers et Troènes, 31.81212 Fruticées atlantiques à Crataegus et Hedera, 31.812121 Fruticées atlantiques calciclines, et 26 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés de recolonisation ou de dégradation, surtout caducifoliés, d'affinités atlantiques à subcontinentales : buis, noisetier, genêt à balais, genévrier, prunellier, ronces, ajonc d'Europe.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (77 taxons ; les 40 plus cités) : Corylus avellana, Prunus spinosa, Rubus sp., Juniperus communis, Cytisus scoparius, Carpinus betulus, Crataegus sp., Rubus fruticosus, Ulex europaeus, Pteridium aquilinum, Rosa sp., Cornus mas, Ligustrum vulgare, Viburnum lantana, Rhamnus catharticus, Lonicera periclymenum, Viburnum opulus, Acer monspessulanum, Amelanchier ovalis, Clematis vitalba, Cornus sanguinea, Cotoneaster integerrimus, Prunus mahaleb, Sorbus aria, Rhamnus alpinus, Frangula alnus, Sorbus aucuparia, Juniperus sp., Buxus sempervirens, Rubus bifrons, Rubus elegantispinosus, Sambucus nigra, Rubus armeniacus, Acer campestre, Geranium robertianum, Malus sylvestris, Pyrus pyraster, Ulmus minor, Euonymus europaeus, Cotoneaster nebrodensis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 41.01.04.02, « Sonstiges Gebüsch frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 434 de l'extraction) |

Correspondance retenue : Autre fourré des stations fraîches.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 27,08 m²HE, 15 à 30 cm 32,5 m²HE, 30 à 80 cm 37,92 m²HE, 80 cm et plus 48,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5,4 | 10,8 | 21,7 | 48,8 | 54,2 | 54,2 | 54,2 | 54,2 | 2 411 |
| moyen | 0 | 9,5 | 19 | 37,9 | 47,4 | 47,4 | 47,4 | 47,4 | 47,4 | 2 228 |
| mauvais | 0 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 1 858 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H101. F3.2 : Fourrés caducifoliés subméditerranéens

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F3.2 |
| EUNIS 2012 | F3.2 |
| EUNIS 2022 (HabRef) | S3-2 Fourrés à Rubus tempérés, S3-4 Balkan-Anatolian submontane genistoid scrub, S3-5 Fourrés épineux tempérés et subméditerranéens, S3-6 Low steppic scrub, S3-7 Fourrés à Corylus avellana, S3-8 Fourrés des clairières des forêts tempérées |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.842 Landes à Cytisus purgans, 31.8421 Landes à Cytisus purgans des Cévennes, 31.8422 Landes à Cytisus purgans pyrénéennes, 31.89 Fourrés caducifoliés sub-méditerranéens sud-occidentaux, 31.891 Fourrés caducifoliés sub-méditerranéens franco-ibériques, 31.8A Fourrés tyrrhéniens subméditerranéens caducifoliés, 31.8A1 Fourrés cyrno-sardes subméditerranéens caducifoliés |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés de recolonisation ou de dégradation, surtout caducifoliés, des étages subméditerranéen et supraméditerranéen.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (214 taxons ; les 40 plus cités) : Cotinus coggygria, Crataegus monogyna, Prunus spinosa, Carpinus orientalis, Cytisus purgans, Syringa vulgaris, Paliurus spina-christi, Fraxinus ornus, Prunus fruticosa, Cornus mas, Cytisus scoparius, Cornus sanguinea, Prunus mahaleb, Rubus ulmifolius, Cytisus striatus, Prunus tenella, Amygdalus nana, Ligustrum vulgare, Rhus coriaria, Rosa canina, Rosa sempervirens, Cytisus multiflorus, Rosa pimpinellifolia, Colutea arborescens, Coronilla emerus, Pyrus amygdaliformis, Achillea clypeolata, Salvia ringens, Genista florida, Caragana frutex, Acer monspessulanum, Genista cinerea ssp. cinerascens, Genista florida ssp. florida, Genista florida ssp. polygaliphylla, Euphorbia cyparissias, Teucrium chamaedrys, Jasminum fruticans, Pistacia terebinthus, Cercis siliquastrum, Clematis vitalba.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H102. F4.1 : Landes humides

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F4.1 |
| EUNIS 2012 | F4.1 |
| EUNIS 2022 (HabRef) | S4-1 Landes humides |
| CORINE Biotopes (HabRef) | 31.1 Landes humides, 31.11 Landes humides atlantiques septentrionales, 31.12 Landes humides atlantiques méridionales, 31.13 Landes humides à Molinia caerulea, 31.2 Landes sèches, 31.23 Landes atlantiques à Erica et Ulex, 31.235 Landes anglo-armoricaines occidentales à Ajoncs, 31.2352 Landes anglo-armoricaines à Ulex gallii et Erica ciliaris, 31.2353 Landes anglo-armoricaines à Ulex gallii et Calluna |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Landes humides à éricacées des zones atlantiques et subatlantiques, sur sols tourbeux ou semi-tourbeux engorgés une partie de l'année.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (12 taxons ; les 40 plus cités) : Erica tetralix, Calluna vulgaris, Molinia caerulea, Erica ciliaris, Erica scoparia, Genista anglica, Ulex gallii, Ulex minor, Sphagnum compactum, Sphagnum molle, Sphagnum tenellum, Scirpus cespitosus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,9167 m²HE/m² | 0,825 à 1 | code 40.02.01, « – Weitgehend intakt », Biotoptypenwert 22 sur 24 (ligne 418 de l'extraction) |

Correspondance retenue : Lande tourbeuse intacte.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 91,67 |
| État moyen | 80,21 |
| Mauvais état | 64,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 45,84 m²HE, 15 à 30 cm 55 m²HE, 30 à 80 cm 64,17 m²HE, 80 cm et plus 82,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,9 | 3,8 | 8,5 | 13,2 | 18 | 27,4 | 30,3 | 1 013 |
| moyen | 0 | 1,3 | 2,6 | 5,3 | 11,9 | 18,5 | 25,1 | 26,5 | 26,5 | 1 046 |
| mauvais | 0 | 2,1 | 4,2 | 8,5 | 19,1 | 21,2 | 21,2 | 21,2 | 21,2 | 942 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H103. F4.2 : Landes sèches

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F4.2 |
| EUNIS 2012 | F4.2 |
| EUNIS 2022 (HabRef) | S4-2 Landes sèches |
| CORINE Biotopes (HabRef) | 31.2 Landes sèches, 31.21 Landes submontagnardes à Vaccinium, 31.213 Landes hercyniennes à Vaccinium, 31.214 Landes submontagnardes alpiennes à Vaccinium, 31.215 Landes sub-montagnardes pyrénéo-cantabriques à Vaccinium, 31.22 Landes sub-atlantiques à Genêt et Callune, 31.223 Landes campino-flandriennes à Callune et Genêt, 31.224 Landes campino-flandriennes à Erica cinerea, 31.226 Landes montagnardes à Calluna et Genista, 31.227 Landes à Empetrum nigrum, et 24 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Landes des sols siliceux et podzoliques rarement ou jamais engorgés, sous climat atlantique ou subatlantique humide, des plaines et basses montagnes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (118 taxons ; les 40 plus cités) : Calluna vulgaris, Erica cinerea, Erica aragonensis, Calluna sp., Genista sp., Erica umbellata, Vaccinium myrtillus, Vaccinium vitis-idaea, Vaccinium sp., Genista pilosa, Halimium alyssoides, Genista anglica, Erica vagans, Ulex europaeus, Arctostaphylos uva-ursi, Empetrum nigrum, Ulex gallii, Ulex minor, Genista sagittalis, Nardus stricta, Vaccinium uliginosum, Empetrum sp., Chamaespartium tridentatum, Cistus salvifolius, Chamaespartium sagittale, Halimium umbellatum, Hylocomium splendens, Empetrum hermaphroditum, Juniperus communis, Daboecia cantabrica, Genista tinctoria, Polygala chamaebuxus, Genista micrantha, Ulex sp., Erica arborea, Cistus sp., Erica sp., Erica mackaiana, Daboecia sp., Agrostis capillaris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 40.03.01, « – Weitgehend intakt », Biotoptypenwert 19 sur 24 (ligne 421 de l'extraction) |

Correspondance retenue : Lande à callune intacte.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,6 | 3,3 | 7,3 | 11,4 | 15,5 | 23,7 | 26,1 | 875 |
| moyen | 0 | 1,1 | 2,3 | 4,6 | 10,3 | 16 | 21,7 | 22,9 | 22,9 | 903 |
| mauvais | 0 | 1,8 | 3,7 | 7,3 | 16,5 | 18,3 | 18,3 | 18,3 | 18,3 | 814 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H104. F5.1 : Matorrals arborescents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F5.1 |
| EUNIS 2012 | F5.1 |
| EUNIS 2022 (HabRef) | S5-1 Maquis méditerranéens et matorrals arborescents |
| CORINE Biotopes (HabRef) | 32.1 Matorral arborescent, 32.11 Matorral à Chênes sempervirents, 32.111 Matorral de Quercus suber, 32.112 Matorral acidiphile de Quercus ilex, 32.113 Matorral calciphile à Quercus ilex, Q. coccifera, 32.12 Matorral à Oliviers et Lentisques, 32.121 Matorral arborescent à Olivier sauvage, 32.122 Matorral arborescent à Caroubier, 32.123 Matorral arborescent à Lentisque, 32.124 Matorral arborescent à Myrte, et 17 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Végétation sempervirente sclérophylle ou laurifoliée à couvert arborescent plus ou moins dense et à strate arbustive épaisse, issue le plus souvent de la dégradation ou de la reconstitution des forêts sempervirentes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (52 taxons ; les 40 plus cités) : Quercus ilex, Quercus rotundifolia, Juniperus oxycedrus, Juniperus phoenicea, Juniperus excelsa, Juniperus foetidissima, Quercus coccifera, Quercus suber, Juniperus communis, Juniperus thurifera, Juniperus drupacea, Juniperus lycia, Myrtus communis, Pistacia lentiscus, Olea europaea var. sylvestris, Ceratonia siliqua, Pistacia atlantica, Olea europaea ssp. cerasiformis, Ziziphus lotus, Quercus calliprinos, Quercus pyrenaica, Quercus faginea, Pinus pinea, Pinus salzmannii, Pinus sylvestris, Pinus pallasiana, Pinus halepensis, Phillyrea latifolia, Juniperus oxycedrus ssp. transtagana, Juniperus transtagana, Juniperus macrocarpa, Juniperus oxycedrus ssp. macrocarpa, Acer sempervirens, Zelkova abelicea, Pinus pinaster ssp. pinaster, Cupressus sp., Asparagus albus, Asparagus stipularis, Lycium intricatum, Periploca laevigata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H105. F5.2 : Maquis

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F5.2 |
| EUNIS 2012 | F5.2 |
| EUNIS 2022 (HabRef) | S5-1 Maquis méditerranéens et matorrals arborescents |
| CORINE Biotopes (HabRef) | 32.3 Maquis silicicoles méso-méditerranéens, 32.31 Maquis hauts, 32.311 Maquis hauts de Méditerranée occidentale, 32.32 Maquis bas à Ericacées, 32.33 Maquis hauts à Cistus, 32.334 Maquis tyrrhénéens hauts à Cistus, 32.34 Maquis bas à Cistes (Cistus sp. pl.), 32.341 Maquis à Cistus monspeliensis, 32.342 Maquis à Cistus salviifolius, 32.343 Maquis à Cistus populifolius, et 8 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Végétation arbustive sempervirente sclérophylle à couvert plus ou moins fermé, dominée par des espèces qui ne deviennent pas de grands arbres : arbousier, bruyères arborescentes, genévrier oxycèdre, filaires dans le haut maquis, cistes, bruyères, genêts et lavandes dans le maquis bas.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (52 taxons ; les 40 plus cités) : Erica arborea, Cistus ladanifer, Cistus sp., Genista sp., Erica scoparia, Juniperus oxycedrus, Erica sp., Arbutus unedo, Cytisus sp., Cistus albidus, Cistus psilosepalus, Quercus ilex, Lavandula stoechas, Cistus populifolius, Calicotome spinosa, Adenocarpus sp., Teline sp., Lavandula stoechas ssp. stoechas, Arbutus sp., Lavandula sp., Phillyrea sp., Cistus incanus, Cistus incanus ssp. corsicus, Cistus incanus ssp. creticus, Fraxinus ornus, Phillyrea angustifolia, Rhamnus alaternus, Viburnum tinus, Phillyrea media, Pistacia lentiscus, Quercus sp., Lavandula stoechas ssp. luisieri, Lavandula stoechas ssp. sampaiana, Cistus salvifolius, Erica cinerea, Calluna vulgaris, Erica lusitanica, Arbutus andrachne, Myrtus communis, Phillyrea latifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H106. F5.3 : Pseudo-maquis

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F5.3 |
| EUNIS 2012 | F5.3 |
| EUNIS 2022 (HabRef) | S5-2 Pseudo-maquis subméditerranéens |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés mêlant arbustes sclérophylles sempervirents et caducifoliés, à la périphérie de l'aire des maquis, issus de la dégradation des chênaies thermophiles.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (30 taxons ; les 40 plus cités) : Prunus lusitanica, Quercus coccifera, Quercus pubescens, Quercus ilex, Buxus sempervirens, Juniperus oxycedrus, Ostrya carpinifolia, Pistacia terebinthus, Carpinus orientalis, Quercus trojana, Paliurus spina-christi, Pyrus spinosa, Berberis cretica, Pistacia palaestina, Quercus calliprinos, Amelanchier ovalis, Ilex aquifolium, Crataegus monogyna, Laurus nobilis, Ligustrum vulgare, Phillyrea media, Pyracantha coccinea, Rosa sempervirens, Rubus ulmifolius, Juniperus excelsa, Crataegus pycnoloba, Pistacia atlantica, Jasminum fruticans, Prunus spinosa, Rosa sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H107. F5.4 : Fourrés à genêt d'Espagne

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F5.4 |
| EUNIS 2012 | F5.4 |
| EUNIS 2022 (HabRef) | S5-3 Fourrés à Spartium junceum |
| CORINE Biotopes (HabRef) | 32.A Champs de Spartium junceum |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés de genêt d'Espagne des régions méditerranéennes et subméditerranéennes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Spartium junceum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes, genêts compris.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 29, « Heathland and shrub - Gorse scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 30, « Heathland and shrub - Gorse scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 30, « Heathland and shrub - Gorse scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 30, « Heathland and shrub - Gorse scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H108. F5.5 : Fourrés thermoméditerranéens

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F5.5 |
| EUNIS 2012 | F5.5 |
| EUNIS 2022 (HabRef) | S5-4 Fourrés arides thermoméditerranéens |
| CORINE Biotopes (HabRef) | 32.2 Formations arbustives thermo-méditerranéennes, 32.21 Fruticées, fourrés et landes-garrigues thermo-méditerranéennes, 32.211 Fruticées à Oliviers et Lentisques, 32.212 Landes-garrigues thermo-méditerranéennes, 32.2121 Landes-garrigues occidentales à Erica multiflora, 32.214 Fruticée à Lentisques, 32.215 Fruticée à Calicotome, 32.216 Fourrés à Lauriers, 32.217 Garrigues côtières à Helichrysum, 32.218 Fourrés à Myrtes, et 14 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Formations arbustives de l'étage thermoméditerranéen, à lentisque, myrte, filaires, euphorbe arborescente, calicotome.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (225 taxons ; les 40 plus cités) : Quercus coccifera, Pistacia lentiscus, Ulex parviflorus ssp. willkommii, Genista umbellata ssp. equisetiformis, Halimium halimifolium, Phlomis purpurea ssp. purpurea, Thymus capitatus, Calicotome villosa, Chamaerops humilis, Cistus bourgaeanus, Halimium commutatum, Cistus libanotis, Stauracanthus genistoides ssp. genistoides, Phillyrea angustifolia, Phillyrea sp., Ulex baeticus, Rhamnus lycioides, Genista hirsuta, Stauracanthus boivinii, Erica manipuliflora, Euphorbia dendroides, Lycium intricatum, Chronanthus biflorus, Asparagus albus, Genista spartioides ssp. retamoides, Phlomis purpurea ssp. almeriensis, Erica scoparia, Calluna vulgaris, Ptilostemon hispanicus, Asparagus sp., Ulex australis, Salvia candelabrum, Teucrium polium, Erica umbellata, Myrtus communis, Ulex argenteus ssp. erinaceus, Frankenia webbii, Periploca sp., Calicotome infesta ssp. intermedia, Periploca laevigata ssp. angustifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H109. F6.1 : Garrigues occidentales

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F6.1 |
| EUNIS 2012 | F6.1 |
| EUNIS 2022 (HabRef) | S6-1 Garrigues basiphiles occidentales, S6-2 Garrigues acidiphiles occidentales |
| CORINE Biotopes (HabRef) | 32.4 Garrigues calcicoles de l'étage méso-méditerranéen occidental, 32.41 Garrigues à chênes kermès, 32.42 Garrigues à romarin, 32.43 Garrigues à cistes, 32.431 Garrigues à Cistus albidus, 32.433 Garrigues à C. monspeliensis, C. salviifolius, C. incanus, 32.44 Garrigues à euphorbes, 32.441 Garrigues à euphorbe épineuse, 32.45 Garrigues à genévrier oxycèdre, 32.46 Garrigues à lavande, et 21 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Formations arbustives souvent basses, surtout sur sols calcaires, de l'étage mésoméditerranéen occidental (garrigues).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (43 taxons ; les 40 plus cités) : Bupleurum fruticosum, Lavandula angustifolia, Lavandula latifolia, Calicotome spinosa, Juniperus oxycedrus, Cistus albidus, Cistus clusii, Pistacia lentiscus, Quercus coccifera, Lithodora fruticosa, Lavandula sp., Rosmarinus sp., Rosmarinus officinalis, Ononis fruticosa, Globularia alypum, Fumana ericoides, Fumana laevipes, Fumana thymifolia, Helianthemum lavandulifolium, Helianthemum marifolium, Helianthemum nummularium, Helianthemum oelandicum, Helianthemum pilosum, Helianthemum sp., Helianthemum asperum, Helianthemum cinereum, Fumana sp., Helianthemum caput-felis, Ulex parviflorus, Genista corsica, Genista hispanica, Genista scorpius, Genista lucida, Thymelaea tinctoria, Thymelaea pubescens, Thymelaea sp., Thymelaea nitida, Dictamnus albus, Dictamnus hispanicus, Anthyllis cytisoides.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 41.01.05.03, « Trockenes Zwerg- und Weichselkirschen-Gebüsch », Biotoptypenwert 18 sur 24 (ligne 438 de l'extraction) |

Correspondance retenue : Fourré nain des stations sèches : aucun type BKompV de garrigue.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 1,1 | 2,2 | 4,3 | 9,7 | 15,2 | 20,6 | 21,7 | 21,7 | 855 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H110. F6.6 : Garrigues supraméditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F6.6 |
| EUNIS 2012 | F6.6 |
| EUNIS 2022 (HabRef) | S6-1 Garrigues basiphiles occidentales, S6-2 Garrigues acidiphiles occidentales, S6-3 Eastern garrigue |
| CORINE Biotopes (HabRef) | 32.6 Garrigues supra-méditerranéennes, 32.61 Garrigues à Lavande vraie, 32.62 Garrigues à Genista cinerea, 32.63 Garrigues montagnardes à Thyms, 32.64 Broussailles supra-méditerranéennes à Buis |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Formations arbustives basses d'affinité méditerranéenne de l'étage supraméditerranéen, issues de la dégradation des chênaies thermophiles ou sempervirentes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (32 taxons ; les 40 plus cités) : Buxus sempervirens, Salvia sp., Teucrium sp., Thymus sp., Lavandula sp., Satureja montana, Genista cinerea ssp. cinerea, Euphorbia sp., Helichrysum sp., Aphyllanthes monspeliensis, Artemisia alba, Astragalus purpureus, Lavandula angustifolia, Lavandula vera, Onobrychis supina, Catananche caerulea, Thymus vulgaris, Coronilla minima, Genista pilosa, Genista scorpius, Dorycnium pentaphyllum ssp. pentaphyllum, Genista cinerea ssp. speciosa, Brachypodium sp., Satureja sp., Sideritis sp., Stipa sp., Genista pseudopilosa, Juniperus oxycedrus, Phillyrea latifolia, Quercus coccifera, Genista nissana, Quercus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 41.01.05.03, « Trockenes Zwerg- und Weichselkirschen-Gebüsch », Biotoptypenwert 18 sur 24 (ligne 438 de l'extraction) |

Correspondance retenue : Fourré nain des stations sèches : aucun type BKompV de garrigue.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 33, « Heathland and shrub - Lowland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 34, « Heathland and shrub - Lowland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 34, « Heathland and shrub - Lowland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 1,1 | 2,2 | 4,3 | 9,7 | 15,2 | 20,6 | 21,7 | 21,7 | 855 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H111. F6.8 : Fourrés xérohalophiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F6.8 |
| EUNIS 2012 | F6.8 |
| EUNIS 2022 (HabRef) | S6-6 Fourrés halonitrophiles méditerranéens, S6-7 Aralo-Caspian semi-desert |
| CORINE Biotopes (HabRef) | 15.7 Fourrés halophiles semi-désertiques, 15.72 Fourrés halonitrophiles méditerranéens |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Formations arbustives halophiles des sols secs des régions méditerranéennes peu arrosées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (35 taxons ; les 40 plus cités) : Suaeda pruinosa, Zygophyllum fontanesii, Atriplex glauca, Atriplex halimus, Capparis ovata, Salsola verticillata, Chenoleoides tomentosa, Anagyris foetida, Artemisia arborescens, Artemisia herba-alba, Camphorosma monspeliaca, Piptatherum miliaceum, Salsola vermiculata, Anabasis articulata, Lycium intricatum, Ruta chelepensis, Salsola genistoides, Smyrnium apifolium, Peganum harmala, Haloxylon articulatum, Salsola longifolia, Salsola oppositifolia, Herniaria fontanesii ssp. empedocleana, Limonium opulentum, Reaumuria vermiculata, Arthrocnemum perenne, Frankenia laevis, Polycarpaea nivea, Suaeda vermiculata, Limonium sp., Zygophyllum sp., Suaeda fruticosa var. brevifolia, Arthrocnemum glaucum, Suaeda vera, Limonium papillatum var. callibotryum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.05.04a, « Sonstiges Gebüsch trocken-warmer Standorte (inkl. Besenginster-Gebüsch) », Biotoptypenwert 16 sur 24 (ligne 439 de l'extraction) |

Correspondance retenue : Autre fourré des stations sèches et chaudes.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 10 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible bon |
| Création, état moyen visé | 5 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 34, « Heathland and shrub - Mixed scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 5 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 10 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 3 ans | onglet G-5, ligne 35, « Heathland and shrub - Mixed scrub », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 35, « Heathland and shrub - Mixed scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 60 | 66,7 | 66,7 | 66,7 | 66,7 | 2 967 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H112. F7.1 : Landes épineuses ouest-méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F7.1 |
| EUNIS 2012 | F7.1 |
| EUNIS 2022 (HabRef) | S7-1 Landes épineuses de Méditerranée occidentale |
| CORINE Biotopes (HabRef) | 33 Phryganes, 33.1 Phryganes ouest méditerranéennes des sommets de falaises, 33.11 Phryganes de la Provence calcaire, 33.12 Phryganes de la Provence cristalline, 33.13 Phryganes du Cap Corse, 33.14 Phryganes du détroit de Bonifacio |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Landes épineuses, surtout des falaises littorales, de la Méditerranée occidentale.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (27 taxons ; les 40 plus cités) : Astragalus massiliensis, Anthyllis hermanniae, Plantago subulata, Thymelaea hirsuta, Armeria ruscinonensis, Helichrysum italicum, Anthyllis fulgurans, Anthyllis hermanniae ssp. hystrix, Astragalus balearicus, Centaurea balearica, Launaea cervicornis, Teucrium subspinosum, Artemisia arborescens, Asteriscus maritimus, Teucrium polium, Plantago coronopus ssp. humulis, Anthyllis barba-jovis, Euphorbia pithyusa, Limonium minutum, Polycarpon polycarpoides, Crithmum maritimum, Thymelaea tartonraira, Cistus albidus, Juniperus oxycedrus, Pistacia lentiscus, Cistus salvifolius, Phillyrea angustifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |

Correspondance retenue : Lande de montagne.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,4 | 6,7 | 15,1 | 23,4 | 31,8 | 48,6 | 50,2 | 1 734 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,8 | 30,8 | 41,8 | 44 | 44 | 1 737 |
| mauvais | 0 | 3,5 | 7 | 14,1 | 31,7 | 35,2 | 35,2 | 35,2 | 35,2 | 1 565 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H113. F7.2 : Landes épineuses centro-méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F7.2 |
| EUNIS 2012 | F7.2 |
| EUNIS 2022 (HabRef) | S7-1 Landes épineuses de Méditerranée occidentale |
| CORINE Biotopes (HabRef) | 33 Phryganes, 33.9 Phryganes cyrno-sardes à Genista |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Landes épineuses, surtout littorales, de la Méditerranée centrale.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (14 taxons ; les 40 plus cités) : Helichrysum saxatile ssp. errerae, Matthiola pulchella, Genista acanthoclada ssp. sardoa, Astragalus massiliensis, Erodium corsicum, Evax rotundata, Limonium acutifolium, Nananthea perpusilla, Centaurea horrida, Armeria pungens, Hypericum aegyptiacum, Genista corsica, Genista morisii, Sarcopoterium spinosum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |

Correspondance retenue : Lande de montagne.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,4 | 6,7 | 15,1 | 23,4 | 31,8 | 48,6 | 50,2 | 1 734 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,8 | 30,8 | 41,8 | 44 | 44 | 1 737 |
| mauvais | 0 | 3,5 | 7 | 14,1 | 31,7 | 35,2 | 35,2 | 35,2 | 35,2 | 1 565 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H114. F7.4 : Landes-hérisson

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F7.4 |
| EUNIS 2012 | F7.4 |
| EUNIS 2022 (HabRef) | S7-3 Landes-hérissons des montagnes méditerranéennes occidentales, S7-4 Landes-hérisson des montagnes de la Méditerranée centrale, S7-5 Landes-hérisson des montagnes de la Méditerranée orientale, S7-6 Canarian mountain hedgehog-heath |
| CORINE Biotopes (HabRef) | 31.7 Landes épineuses (= Landes hérisson), 31.74 Landes épineuses franco-ibériques, 31.741 Landes épineuses à Erinacea, 31.745 Landes en coussinets de Genista, 31.7451 Landes en coussinets pyrénéo-cantabriennes, 31.7456 Landes en coussinets à Genista lobelii et G. pulchella, 31.75 Landes épineuses cyrno-sardes, 31.751 Landes épineuses à Astragalus gennargenteus, 31.752 Landes épineuses cyrno-sardes à Euphorbia, 31.753 Landes en coussinets cyrno-sardes à Thymus, et 4 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Landes en coussinets, souvent épineux, des hautes montagnes sèches méditerranéennes, primaires ou issues du pâturage.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (198 taxons ; les 40 plus cités) : Erinacea anthyllis, Astragalus sp., Erinacea sp., Astragalus angustifolius, Echinospartum sp., Genista sp., Vella spinosa, Daphne oleoides, Astragalus sempervirens ssp. nevadensis, Astragalus granatensis ssp. granatensis, Juniperus hemisphaerica, Astragalus creticus ssp. rumelicus, Berberis cretica, Ptilotrichum spinosum, Bupleurum spinosum, Arctostaphylos uva-ursi ssp. crassifolia, Acantholimon androsaceum, Juniperus nana, Genista baetica, Genista pumila, Echinospartum ibericum ssp. pulviniformis, Genista scorpius, Astragalus boissieri, Teucrium subspinosum, Berberis aetnensis, Prunus prostrata, Andryala agardhii, Pterocephalus spathulatus, Vella sp., Acantholimon sp., Echium wildpretii, Echinospartum boissieri, Echinospartum horridum, Ononis fruticosa, Pinus sylvestris, Buxus sempervirens, Genista acanthoclada, Astragalus parnassi ssp. cylleneus, Aster alpinus, Paronychia kapela.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 40.05, « Bergheiden („Hochheiden“) », Biotoptypenwert 18 sur 24 (ligne 424 de l'extraction) |

Correspondance retenue : Lande de montagne.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 39, « Heathland and shrub - Upland heathland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 40, « Heathland and shrub - Upland heathland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 40, « Heathland and shrub - Upland heathland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,4 | 6,7 | 15,1 | 23,4 | 31,8 | 48,6 | 50,2 | 1 734 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,8 | 30,8 | 41,8 | 44 | 44 | 1 737 |
| mauvais | 0 | 3,5 | 7 | 14,1 | 31,7 | 35,2 | 35,2 | 35,2 | 35,2 | 1 565 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H115. F9.1 : Fourrés ripicoles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F9.1 |
| EUNIS 2012 | F9.1 |
| EUNIS 2022 (HabRef) | S9-1 Fourrés ripicoles tempérés |
| CORINE Biotopes (HabRef) | 24.2 Bancs de graviers des cours d'eau, 24.22 Bancs de graviers végétalisés, 24.223 Broussailles de Saules et de Myricaire germanique, 24.224 Fourrés et bois des bancs de graviers, 44.1 Formations riveraines de Saules, 44.11 Saussaies pré-alpines, 44.111 Saussaies à Myricaria, 44.112 Saussaies à Argousier, 44.12 Saussaies de plaine, collinéennes et méditerranéo-montagnardes, 44.121 Saussaies à Osier et Salix triandra, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Fourrés riverains de saules à larges feuilles, d'aulnes, de saules à feuilles étroites de moins de 5 m, d'argousier ou de tamarin d'Allemagne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (56 taxons ; les 40 plus cités) : Salix triandra, Hippophae rhamnoides, Myricaria germanica, Salix sp., Salix viminalis, Salix purpurea ssp. lambertiana, Salix purpurea, Salix pedicellata, Salix daphnoides, Salix elaeagnos, Salix cinerea, Salix nigricans, Salix elaeagnos ssp. angustifolia, Salix acutifolia, Salix daphnoides ssp. acutifolia, Salix australior, Salix myrsinifolia, Salix pentandra, Salix phylicifolia, Salix alba, Alnus sp., Salix purpurea ssp. gracilis, Salix triandra ssp. discolor, Elaeagnus angustifolia, Salix rosmarinifolia, Elaeagnus oxycarpa, Elaeagnus turkmanica, Salix caspica, Salix cheilophila, Salix euapiculata, Salix flavida, Salix songarica, Salix wilhelmsiana, Salix blakii, Salix microstacha, Salix glauca, Salix amplexicaulis, Frangula alnus, Myrica gale, Salix aurita.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.02, « (Weiden-)Gebüsch in Auen », Biotoptypenwert 16 sur 24 (ligne 428 de l'extraction) |

Correspondance retenue : Fourré de saules alluvial.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3 | 6 | 11,9 | 26,8 | 41,7 | 44,7 | 44,7 | 44,7 | 1 876 |
| moyen | 0 | 3,9 | 7,8 | 15,6 | 35,2 | 39,1 | 39,1 | 39,1 | 39,1 | 1 739 |
| mauvais | 0 | 6,3 | 12,5 | 25 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 470 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H116. F9.2 : Saussaies marécageuses et fourrés de bas-marais

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F9.2 |
| EUNIS 2012 | F9.2 |
| EUNIS 2022 (HabRef) | S9-2 Fourrés des bas-marais à Salix |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.92 Saussaies marécageuses, 44.921 Saussaies marécageuses à Saule cendré, 44.922 Saussaies à sphaigne, 44.923 Saussaies marécageuses à Saule laurier, 44.924 Saussaies naines marécageuses |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Bois bas et fourrés de saules arbustifs colonisant les bas-marais, les plaines inondables marécageuses et les bords d'étangs, avec bourdaine, nerprun, aulne ou bouleau pubescent.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (38 taxons ; les 40 plus cités) : Salix cinerea, Salix aurita, Alnus glutinosa, Betula pubescens, Frangula alnus, Salix atrocinerea, Salix pentandra, Betula humilis, Rhamnus catharticus, Menyanthes trifoliata, Phragmites australis, Salix repens, Salix rosmarinifolia, Betula nana, Salix sp., Carex pseudocyperus, Equisetum fluviatile, Glyceria maxima, Calamagrostis canescens, Deschampsia cespitosa, Filipendula ulmaria, Galium palustre, Lysimachia vulgaris, Myosotis palustris, Spiraea salicifolia, Euonymus nanus, Ribes nigrum, Poa trivialis, Betula carpatica, Carex elata, Scirpus sylvaticus, Carex caespitosa, Salix glauca, Salix lapponum, Salix nigricans, Salix phylicifolia, Carex aquatilis, Salix myrsinifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.03.01, « Moor-Gebüsch (z. B. mit Weiden, Gagel) », Biotoptypenwert 16 sur 24 (ligne 430 de l'extraction) |

Correspondance retenue : Fourré de tourbière.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3 | 6 | 11,9 | 26,8 | 41,7 | 44,7 | 44,7 | 44,7 | 1 876 |
| moyen | 0 | 3,9 | 7,8 | 15,6 | 35,2 | 39,1 | 39,1 | 39,1 | 39,1 | 1 739 |
| mauvais | 0 | 6,3 | 12,5 | 25 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 470 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H117. F9.3 : Galeries et fourrés riverains méridionaux

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | F9.3 |
| EUNIS 2012 | F9.3 |
| EUNIS 2022 (HabRef) | S9-3 Fourrés riverains méditerranéens |
| CORINE Biotopes (HabRef) | 44.8 Galeries et fourrés riverains méridionaux, 44.81 Galeries de Laurier-roses, de Gattiliers et de Tamaris, 44.811 Galeries de Laurier-rose, 44.812 Fourrés de Gattiliers, 44.813 Fourrés de Tamaris, 44.8131 Fourrés de Tamaris ouest-méditerranéens |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EL1 (landes) |

**Définition**

Galeries et fourrés de tamaris, de laurier-rose et de gattilier des cours d'eau permanents ou temporaires de l'étage thermoméditerranéen.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (54 taxons ; les 40 plus cités) : Tamarix smyrnensis, Tamarix canariensis, Tamarix gallica, Tamarix sp., Tamarix tetrandra, Vitex agnus-castus, Tamarix africana, Tamarix ramosissima, Nerium oleander, Tamarix boveana, Tamarix dalmatica, Tamarix hampeana, Arundo donax, Dittrichia viscosa, Saccharum ravennae, Tamarix parviflora, Brachypodium phoenicoides, Equisetum ramosissimum, Piptatherum miliaceum, Scirpus holoschoenus, Rubia longifolia, Asparagus acutifolius, Rubia peregrina, Rubia angustifolia, Securinega sp., Amorpha fruticosa, Reynoutria japonica, Arthrocnemum fruticosum, Arthrocnemum glaucum, Halimione portulacoides, Inula crithmoides, Limonium sinuatum, Atriplex hastata, Limonium angustibracteanum, Limonium cossonianum, Limonium eugeniae, Limonium lactibracteatum, Suaeda brevifolia, Atriplex halimus, Tamarix octandra.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.01.02, « (Weiden-)Gebüsch in Auen », Biotoptypenwert 16 sur 24 (ligne 428 de l'extraction) |

Correspondance retenue : Fourré de saules alluvial.

**Grille d'état EL1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Lande représentative de son type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes | oui |
| B | Au moins deux espèces d'arbrisseaux fréquentes, recouvrement des arbrisseaux de 25 à 75 % en plaine | oui |
| C | Toutes les classes d'âge de la callune présentes, dont au moins 10 % de stade pionnier en plaine | non |
| D | Sol nu non ombragé entre 1 % et 10 % | non |
| E | Absence d'espèces végétales exotiques envahissantes | non |
| F | Aucune trace de perturbation des zones sensibles, brûlages dirigés compris | non |
| G | Au plus 33 % des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne | non |
| H | Arbres et fourrés épars (ajoncs exclus) sur moins de 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne | non |
| I | Ajoncs sur moins de 50 %, ajonc d'Europe sur moins de 25 % | non |
| J | Fougère aigle sur moins de 5 % | non |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 15 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 32, « Heathland and shrub - Willow scrub », condition cible mauvais |
| Amélioration, mauvais vers moyen | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 15 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 7 ans | onglet G-5, ligne 33, « Heathland and shrub - Willow scrub », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 33, « Heathland and shrub - Willow scrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 3 | 6 | 11,9 | 26,8 | 41,7 | 44,7 | 44,7 | 44,7 | 1 876 |
| moyen | 0 | 3,9 | 7,8 | 15,6 | 35,2 | 39,1 | 39,1 | 39,1 | 39,1 | 1 739 |
| mauvais | 0 | 6,3 | 12,5 | 25 | 31,3 | 31,3 | 31,3 | 31,3 | 31,3 | 1 470 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H118. FA.1 : Haies d'espèces non indigènes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FA.1 |
| EUNIS 2012 | FA.1 |
| EUNIS 2022 (HabRef) | V4-1 Haies d'espèces non indigènes |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | linéaire (longueur x largeur) |
| Grille d'état | EH1 (haies) |

**Définition**

Haies plantées d'espèces non indigènes dans la région, exotiques ou européennes hors de leur aire naturelle.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Ligustrum ovalifolium.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.04M, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 11 sur 24 (ligne 469 de l'extraction) |
| Valeur, stade jeune | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 41.04J, « – Junge Ausprägung/– Ohne Überhälter sowie Schnitthecken », 8 sur 24 |
| Valeur, stade moyen | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.04M, « – Mittlere Ausprägung/– Mit Überhältern mittlerer Ausprägung », 11 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.04A, « – Alte Ausprägung/– Mit Überhältern alter Ausprägung », 14 sur 24 |

Correspondance retenue : Plantations et haies d'essences non autochtones, stade moyen (convention C-H5).

**Grille d'état EH1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A1 | Hauteur moyenne de la haie supérieure à 1,5 m | non |
| A2 | Largeur moyenne de la haie supérieure à 1,5 m | non |
| B1 | Espace entre le sol et la base du feuillage inférieur à 0,5 m sur plus de 90 % de la longueur | non |
| B2 | Trouées sur moins de 10 % de la longueur et aucune trouée de plus de 5 m | non |
| C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace sur au moins un côté et plus de 90 % de la longueur | non |
| C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de la bande non perturbée | non |
| D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes | non |
| D2 | Plus de 90 % de la haie et de sa bande exempts de dégradations d'origine humaine | non |
| E1 | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m | non |
| E2 | Au moins 95 % des arbres de la haie en bonne santé | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, mauvais état visé | 1 ans | onglet G-6, ligne 15, « Non-native and ornamental hedgerow », condition mauvais |
| Difficulté de création | 1 | onglet G-6, ligne 15, difficulté Low ; onglet G-3, table Difficulty |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| mauvais | 0 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 1 572 |

#### Fiche H119. FA.2 : Haies d'espèces indigènes fortement gérées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FA.2 |
| EUNIS 2012 | FA.2 |
| EUNIS 2022 (HabRef) | V4-2 Haies d'espèces indigènes fortement gérées |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | linéaire (longueur x largeur) |
| Grille d'état | EH1 (haies) |

**Définition**

Haies d'espèces indigènes plantées en haie et taillées régulièrement.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », Biotoptypenwert 12 sur 24 (ligne 464 de l'extraction) |
| Valeur, stade jeune | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| Valeur, stade moyen | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| Valeur, stade âgé | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |

Correspondance retenue : Haie autochtone taillée, sans arbres de haut jet.

**Grille d'état EH1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A1 | Hauteur moyenne de la haie supérieure à 1,5 m | non |
| A2 | Largeur moyenne de la haie supérieure à 1,5 m | non |
| B1 | Espace entre le sol et la base du feuillage inférieur à 0,5 m sur plus de 90 % de la longueur | non |
| B2 | Trouées sur moins de 10 % de la longueur et aucune trouée de plus de 5 m | non |
| C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace sur au moins un côté et plus de 90 % de la longueur | non |
| C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de la bande non perturbée | non |
| D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes | non |
| D2 | Plus de 90 % de la haie et de sa bande exempts de dégradations d'origine humaine | non |
| E1 | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m | non |
| E2 | Au moins 95 % des arbres de la haie en bonne santé | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-6, ligne 12, « Native hedgerow », condition bon |
| Création, état moyen visé | 5 ans | onglet G-6, ligne 12, « Native hedgerow », condition moyen |
| Création, mauvais état visé | 1 ans | onglet G-6, ligne 12, « Native hedgerow », condition mauvais |
| Difficulté de création | 1 | onglet G-6, ligne 12, difficulté Low ; onglet G-3, table Difficulty |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,2 | 8,3 | 16,7 | 37,5 | 50 | 50 | 50 | 50 | 2 175 |
| moyen | 0 | 8,8 | 17,5 | 35 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 056 |
| mauvais | 0 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 1 715 |

#### Fiche H120. FA.3 : Haies d'espèces indigènes riches en espèces

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FA.3 |
| EUNIS 2012 | FA.3 |
| EUNIS 2022 (HabRef) | V4-3 Haies d'espèces indigènes riches en espèces |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | linéaire (longueur x largeur) |
| Grille d'état | EH1 (haies) |

**Définition**

Haies composées surtout d'espèces indigènes, avec en moyenne au moins cinq espèces ligneuses indigènes par 25 m, ronce et grimpantes non comptées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (3 taxons ; les 40 plus cités) : Clematis vitalba, Rubus fruticosus, Hedera helix.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », Biotoptypenwert 16 sur 24 (ligne 465 de l'extraction) |
| Valeur, stade jeune | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| Valeur, stade moyen | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| Valeur, stade âgé | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |

Correspondance retenue : Haie autochtone avec arbres de haut jet de stade moyen (convention C-H5).

**Grille d'état EH1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A1 | Hauteur moyenne de la haie supérieure à 1,5 m | non |
| A2 | Largeur moyenne de la haie supérieure à 1,5 m | non |
| B1 | Espace entre le sol et la base du feuillage inférieur à 0,5 m sur plus de 90 % de la longueur | non |
| B2 | Trouées sur moins de 10 % de la longueur et aucune trouée de plus de 5 m | non |
| C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace sur au moins un côté et plus de 90 % de la longueur | non |
| C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de la bande non perturbée | non |
| D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes | non |
| D2 | Plus de 90 % de la haie et de sa bande exempts de dégradations d'origine humaine | non |
| E1 | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m | non |
| E2 | Au moins 95 % des arbres de la haie en bonne santé | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-6, ligne 7, « Species-rich native hedgerow », condition bon |
| Création, état moyen visé | 5 ans | onglet G-6, ligne 7, « Species-rich native hedgerow », condition moyen |
| Création, mauvais état visé | 1 ans | onglet G-6, ligne 7, « Species-rich native hedgerow », condition mauvais |
| Difficulté de création | 1 | onglet G-6, ligne 7, difficulté Low ; onglet G-3, table Difficulty |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 66,67 |
| État moyen | 58,34 |
| Mauvais état | 46,67 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 5,6 | 11,1 | 22,2 | 50 | 66,7 | 66,7 | 66,7 | 66,7 | 2 900 |
| moyen | 0 | 11,7 | 23,3 | 46,7 | 58,3 | 58,3 | 58,3 | 58,3 | 58,3 | 2 742 |
| mauvais | 0 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 46,7 | 2 287 |

#### Fiche H121. FA.4 : Haies d'espèces indigènes pauvres en espèces

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FA.4 |
| EUNIS 2012 | FA.4 |
| EUNIS 2022 (HabRef) | V4-4 Haies d'espèces indigènes pauvres en espèces |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | linéaire (longueur x largeur) |
| Grille d'état | EH1 (haies) |

**Définition**

Haies composées surtout d'espèces indigènes, non taillées régulièrement, avec en moyenne moins de cinq espèces ligneuses par 25 m.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (3 taxons ; les 40 plus cités) : Hedera helix, Rubus fruticosus, Clematis vitalba.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », Biotoptypenwert 12 sur 24 (ligne 464 de l'extraction) |
| Valeur, stade jeune | 0,5 m²HE/m² | 0,45 à 0,55 | code 41.03.03J, « – Junge Ausprägung (ohne Überhälter) sowie Schnitthecken », 12 sur 24 |
| Valeur, stade moyen | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 41.03.03M, « – Mit Überhältern mittlerer Ausprägung », 16 sur 24 |
| Valeur, stade âgé | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 41.03.03A, « – Mit Überhältern alter Ausprägung », 19 sur 24 |

Correspondance retenue : Haie autochtone jeune, sans arbres de haut jet.

**Grille d'état EH1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A1 | Hauteur moyenne de la haie supérieure à 1,5 m | non |
| A2 | Largeur moyenne de la haie supérieure à 1,5 m | non |
| B1 | Espace entre le sol et la base du feuillage inférieur à 0,5 m sur plus de 90 % de la longueur | non |
| B2 | Trouées sur moins de 10 % de la longueur et aucune trouée de plus de 5 m | non |
| C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace sur au moins un côté et plus de 90 % de la longueur | non |
| C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de la bande non perturbée | non |
| D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes | non |
| D2 | Plus de 90 % de la haie et de sa bande exempts de dégradations d'origine humaine | non |
| E1 | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m | non |
| E2 | Au moins 95 % des arbres de la haie en bonne santé | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 12 ans | onglet G-6, ligne 12, « Native hedgerow », condition bon |
| Création, état moyen visé | 5 ans | onglet G-6, ligne 12, « Native hedgerow », condition moyen |
| Création, mauvais état visé | 1 ans | onglet G-6, ligne 12, « Native hedgerow », condition mauvais |
| Difficulté de création | 1 | onglet G-6, ligne 12, difficulté Low ; onglet G-3, table Difficulty |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,2 | 8,3 | 16,7 | 37,5 | 50 | 50 | 50 | 50 | 2 175 |
| moyen | 0 | 8,8 | 17,5 | 35 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 056 |
| mauvais | 0 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 35 | 1 715 |

#### Fiche H122. FB.1 : Plantations d'arbustes pour la récolte de la plante entière

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FB.1 |
| EUNIS 2012 | FB.1 |
| EUNIS 2022 (HabRef) | V5-1 Plantations d'arbustes pour la récolte de la plante entière |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Plantations d'arbustes récoltés entiers, pépinières d'arbustes comprises.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,25 m²HE/m² | 0,225 à 0,275 | code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |

Correspondance retenue : Plantations ligneuses.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 12,5 m²HE, 15 à 30 cm 15 m²HE, 30 à 80 cm 17,5 m²HE, 80 cm et plus 22,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 1 225 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H123. FB.2 : Plantations d'arbustes pour la récolte de feuilles et de branches

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FB.2 |
| EUNIS 2012 | FB.2 |
| EUNIS 2022 (HabRef) | V5-2 Plantations d'arbustes pour la récolte de feuilles et de branches |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Plantations d'arbustes récoltés pour leurs feuilles ou leurs rameaux, oseraies comprises.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (3 taxons ; les 40 plus cités) : Salix viminalis, Camellia sinensis, Salix rubra.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,25 m²HE/m² | 0,225 à 0,275 | code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |

Correspondance retenue : Plantations ligneuses.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 12,5 m²HE, 15 à 30 cm 15 m²HE, 30 à 80 cm 17,5 m²HE, 80 cm et plus 22,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 1 225 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H124. FB.3 : Plantations d'arbustes ornementaux ou fruitiers

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FB.3 |
| EUNIS 2012 | FB.3 |
| EUNIS 2022 (HabRef) | V5-3 Plantations d'arbustes à des fins ornementales ou pour les fruits, autres que les vignobles |
| CORINE Biotopes (HabRef) | 83.2 Vergers à arbustes, 83.22 Vergers de basses tiges |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Plantations d'arbres nains, d'arbustes, d'espaliers ou de grimpantes ligneuses autres que la vigne, cultivés pour leurs fruits ou leurs fleurs (groseilliers, framboisiers).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Ribes sp., Rubus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,25 m²HE/m² | 0,225 à 0,275 | code 41.07, « Gehölzplantagen und Hopfenkulturen », Biotoptypenwert 6 sur 24 (ligne 499 de l'extraction) |

Correspondance retenue : Plantations ligneuses.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 72, « Urban - Introduced shrub », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 95, « Urban - Introduced shrub » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 95, « Urban - Introduced shrub » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 25 |
| État moyen | 21,88 |
| Mauvais état | 17,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 12,5 m²HE, 15 à 30 cm 15 m²HE, 30 à 80 cm 17,5 m²HE, 80 cm et plus 22,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 1 225 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H125. FB.4 : Vignobles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | FB.4 |
| EUNIS 2012 | FB.4 |
| EUNIS 2022 (HabRef) | V5-4 Vignobles |
| CORINE Biotopes (HabRef) | 83.2 Vergers à arbustes, 83.21 Vignobles, 83.211 Vignobles traditionnels, 83.212 Vignobles intensifs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Vignobles.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Vitis vinifera.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 41.08.02, « Rebkulturen in ebener bis schwach geneigter Lage », Biotoptypenwert 9 sur 24 (ligne 502 de l'extraction) |

Correspondance retenue : Vigne en terrain plat ou faiblement incliné.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 37,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 18,75 m²HE, 15 à 30 cm 22,5 m²HE, 30 à 80 cm 26,25 m²HE, 80 cm et plus 33,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 37,5 | 1 838 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.6 Boisements, forêts et autres habitats boisés (EUNIS G)

#### Fiche H126. G1.1 : Forêts riveraines à aulnes, peupliers ou saules

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.1 |
| EUNIS 2012 | G1.1 |
| EUNIS 2022 (HabRef) | T1-1 Forêts riveraines tempérées de Salix et Populus |
| CORINE Biotopes (HabRef) | 44.1 Formations riveraines de Saules, 44.13 Forêts galeries de Saules blancs, 44.14 Galeries méditerranéennes de grands Saules, 44.141 Galeries méditerranéennes de Saules blancs, 44.1412 Galeries de Salix alba méditerranéennes, 44.142 Bois riverains de Saules à feuilles d'Olivier et de Saules cendrés, 44.2 Galeries d'Aulnes blancs, 44.21 Galeries montagnardes d'Aulnes blancs, 44.22 Galeries sub-montagnardes d'Aulnes blancs, 44.5 Galeries méridionales d'Aulnes et de Bouleaux, et 5 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts riveraines à une ou quelques essences dominantes, aulnes, bouleaux, peupliers ou saules, dont les saulaies arborescentes à saules à feuilles étroites.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (108 taxons ; les 40 plus cités) : Alnus incana, Salix alba, Salix fragilis, Populus nigra, Alnus glutinosa, Fraxinus angustifolia, Salix atrocinerea, Populus alba, Frangula alnus, Salix x rubens, Lycopus europaeus, Galium broterianum, Populus tremula, Salix cinerea, Rubus sp., Matteuccia struthiopteris, Paris quadrifolia, Betula pendula, Pinus sylvestris, Filipendula ulmaria, Lysimachia vulgaris, Betula celtiberica, Carex acuta ssp. broteriana, Betula sp., Salix sp., Osmunda regalis, Salix neotricha, Alnus cordata, Thelypteris palustris, Amorpha fruticosa, Fraxinus pennsylvanica, Lycopus exaltatus, Polygonum hydropiper, Rubus caesius, Tamus communis, Anemone nemorosa, Betula pubescens, Equisetum pratense, Geranium sylvaticum, Melandrium rubrum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 565 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.04.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 43.04.02.01A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Forêt alluviale à bois tendre à dynamique naturelle, stade moyen (convention C-H5).

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H127. G1.2 : Forêts riveraines mixtes des plaines inondables

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.2 |
| EUNIS 2012 | G1.2 |
| EUNIS 2022 (HabRef) | T1-2 Forêts à Alnus glutinosa-Alnus incana sur sols riverains et minéraux, T1-3 Forêts riveraines à bois durs tempérées |
| CORINE Biotopes (HabRef) | 44.3 Forêt de Frênes et d'Aulnes des fleuves médio-européens, 44.31 Forêts de Frênes et d'Aulnes des ruisselets et des sources (rivulaires), 44.311 Forêts de Frênes et d'Aulnes à Laîches, 44.312 Forêts de Frênes et d'Aulnes fontinales, 44.313 Forêts de Frênes et d'Aulnes à Cirse des maraîchers, 44.314 Forêts de Frênes et d'Aulnes des bords de sources à groseillers, 44.315 Forêts de Frênes et d'Aulnes à grande Prêle, 44.32 Bois de Frênes et d'Aulnes des rivières à débit rapide, 44.33 Bois de Frênes et d'Aulnes des rivières à eaux lentes, 44.331 Bois de Frênes et d'Aulnes des rivières médio-européennes à eaux lentes à cerisiers à grappes, et 7 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts riveraines mêlées, parfois très structurées et riches en espèces, des plaines inondables et des galeries le long des rivières, à érables, frênes, ormes, chênes, peupliers et saules.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (204 taxons ; les 40 plus cités) : Alnus glutinosa, Fraxinus excelsior, Quercus robur, Fraxinus angustifolia, Ulmus minor, Carex remota, Carpinus betulus, Acer campestre, Rubus caesius, Ulmus laevis, Frangula alnus, Populus alba, Alnus incana, Picea abies, Ulmus glabra, Prunus padus, Cornus sanguinea, Carex acutiformis, Ribes rubrum, Urtica dioica, Corylus avellana, Salix alba, Crataegus monogyna, Filipendula ulmaria, Carex brizoides, Humulus lupulus, Cirsium oleraceum, Equisetum telmateia, Sambucus nigra, Hedera helix, Impatiens noli-tangere, Tilia cordata, Acer pseudoplatanus, Stellaria nemorum, Aegopodium podagraria, Periploca graeca, Calystegia sepium, Symphytum officinale, Ulmus sp., Tamus communis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 573 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.04.03.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.03.01M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9167 m²HE/m² | 0,825 à 1 | code 43.04.03.01A, « – Alte Ausprägung », 22 sur 24 |

Correspondance retenue : Forêt alluviale à bois dur à dynamique naturelle, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H128. G1.3 : Forêts riveraines méditerranéennes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.3 |
| EUNIS 2012 | G1.3 |
| EUNIS 2022 (HabRef) | T1-4 Forêts riveraines méditerranéennes et macaronésiennes |
| CORINE Biotopes (HabRef) | 44.6 Forêts méditerranéennes de Peupliers, d'Ormes et de Frênes, 44.61 Forêts de Peupliers riveraines et méditerranéennes, 44.612 Galeries de Peupliers provenço-languedociennes, 44.613 Galeries de Peupliers cyrno-sardes, 44.62 Forêts d'Ormes riveraines et méditerranéennes, 44.63 Bois de Frênes riverains et méditerranéens, 44.634 Galeries de Frênes et d'Aulnes tyrrhéniennes, 44.64 Galeries de Charmes Houblon |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts alluviales et galeries méditerranéennes, à frênes, platanes, peupliers, saules, ormes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (122 taxons ; les 40 plus cités) : Populus alba, Populus nigra, Fraxinus angustifolia, Alnus glutinosa, Platanus orientalis, Cornus sanguinea, Ulmus minor, Brachypodium sylvaticum, Salix alba, Salix sp., Populus canescens, Rubus caesius, Crataegus monogyna, Periploca graeca, Quercus robur, Acer campestre, Arum italicum, Viburnum opulus, Vitex agnus-castus, Carex pendula, Celtis australis, Humulus lupulus, Vitis vinifera ssp. sylvestris, Clematis vitalba, Hedera helix, Pyracantha coccinea, Salix fragilis, Ulmus laevis, Frangula alnus, Fraxinus ornus, Rubus ulmifolius, Ranunculus ficaria, Fraxinus excelsior, Quercus pubescens, Saponaria officinalis, Bidens tripartita, Lycopus europaeus, Scutellaria galericulata, Juglans regia, Ligustrum vulgare.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 565 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.04.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.04.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 43.04.02.01A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Forêt alluviale à bois tendre, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H129. G1.4 : Forêts marécageuses de feuillus hors tourbe acide

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.4 |
| EUNIS 2012 | G1.4 |
| EUNIS 2022 (HabRef) | T1-5 Forêts marécageuses de feuillus ne se trouvant pas sur tourbe acide |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.91 Bois marécageux d'Aulnes, 44.911 Bois d'Aulnes marécageux méso-eutrophes, 44.9111 Bois d'Aulnes marécageux atlantiques à grandes touffes de laîches, 44.9112 Bois d'Aulnes marécageux à laîche allongée, 44.912 Bois d'Aulnes marécageux oligotrophes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts marécageuses de feuillus hors tourbe acide : aulnaies, peupleraies et chênaies marécageuses.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (66 taxons ; les 40 plus cités) : Alnus glutinosa, Carex elongata, Calamagrostis canescens, Thelypteris palustris, Betula pubescens, Dryopteris cristata, Frangula alnus, Ribes nigrum, Carex laevigata, Osmunda regalis, Salix cinerea, Alnus sp., Salix sp., Calla palustris, Ligularia sibirica, Dryopteris carthusiana, Athyrium filix-femina, Sphagnum sp., Carex acutiformis, Alnus incana, Filipendula ulmaria, Lysimachia thyrsiflora, Fraxinus angustifolia, Rubus hirtus, Alnus barbata, Smilax excelsa, Oenanthe crocata, Scutellaria minor, Salix aurita, Salix pentandra, Populus sp., Quercus sp., Populus tremula, Carex caespitosa, Blechnum spicant, Equisetum sylvaticum, Oreopteris limbosperma, Quercus robur, Caltha palustris, Festuca gigantea.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.02.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 543 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.02.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.02.02.01M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 43.02.02.01A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Aulnaie marécageuse à régime hydrique intact, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H130. G1.5 : Forêts marécageuses de feuillus sur tourbe acide

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.5 |
| EUNIS 2012 | G1.5 |
| EUNIS 2022 (HabRef) | T1-6 Forêts marécageuses de feuillus sur tourbe acide |
| CORINE Biotopes (HabRef) | 44.9 Bois marécageux d'Aulne, de Saule et de Myrte des marais, 44.91 Bois marécageux d'Aulnes, 44.A Forêts marécageuses de Bouleaux et de Conifères, 44.A1 Bois de Bouleaux à Sphaignes, 44.A11 Forêts de Bouleaux à Sphaignes et Linaigrettes, 44.A12 Bois de Bouleaux à Sphaignes et à Laîches, 44.A13 Bois de Bouleaux à Sphaignes méso-acidiphiles |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Boisements de feuillus sur tourbe acide humide, dominés par le bouleau pubescent ou plus rarement l'aulne glutineux, à sphaignes abondantes au sol.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (35 taxons ; les 40 plus cités) : Betula pubescens, Betula carpatica, Alnus glutinosa, Molinia caerulea, Eriophorum vaginatum, Picea abies, Vaccinium oxycoccos, Deschampsia flexuosa, Luzula sylvatica, Oxalis acetosella, Salix cinerea, Lysimachia vulgaris, Salix sp., Sphagnum sp., Sphagnum magellanicum, Empetrum nigrum, Trientalis europaea, Vaccinium sp., Sphagnum fallax, Calamagrostis canescens, Calamagrostis purpurea, Carex nigra, Carex rostrata, Juncus acutiflorus, Narthecium ossifragum, Pinus sylvestris, Scirpus cespitosus, Vaccinium uliginosum, Carex sp., Empetrum sp., Juncus sp., Cornus suecica, Rubus chamaemorus, Agrostis canina, Carex echinata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.02.01.01M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 535 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.02.01.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.02.01.01M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 1 m²HE/m² | 0,9 à 1 | code 43.02.01.01A, « – Alte Ausprägung », 24 sur 24 |

Correspondance retenue : Boulaie marécageuse à régime hydrique intact, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H131. G1.6 : Hêtraies

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.6 |
| EUNIS 2012 | G1.6 |
| EUNIS 2022 (HabRef) | T1-7 Hêtraies sur sols non acides, T1-8 Hêtraies sur sols acides |
| CORINE Biotopes (HabRef) | 41.1 Hêtraies, 41.11 Hêtraies acidiphiles médio-européennes à Luzule blanchâtre du Luzulo-Fagenion, 41.111 Hêtraies collinéennes à Luzule, 41.112 Hêtraies montagnardes à Luzule, 41.1122 Hêtraies montagnardes semi-naturelles à Luzule françaises, 41.12 Hêtraies atlantiques acidiphiles, 41.121 Hêtraies acidiphiles de la mer du Nord, 41.122 Hêtraies acidiphiles sub-atlantiques, 41.123 Hêtraies acidiphiles armoricaines, 41.124 Hêtraies acidiphiles pyrénéo-cantabriques, et 28 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts dominées par le hêtre. Les forêts mixtes hêtre-sapin ou hêtre-sapin-épicéa de montagne relèvent de G4.6.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (317 taxons ; les 40 plus cités) : Fagus sylvatica, Fagus moesiaca, Abies alba, Picea abies, Fagus orientalis, Carpinus betulus, Galium odoratum, Acer pseudoplatanus, Fraxinus ornus, Melica uniflora, Quercus petraea, Luzula luzuloides, Taxus baccata, Fraxinus excelsior, Galium rotundifolium, Tilia tomentosa, Dentaria glandulosa, Pulmonaria rubra, Symphytum cordatum, Cardamine bulbifera, Mercurialis perennis, Dentaria bulbifera, Deschampsia flexuosa, Ostrya carpinifolia, Oxalis acetosella, Ruscus hypoglossum, Tilia cordata, Festuca drymeja, Ulmus glabra, Lathyrus venetus, Cardamine glanduligera, Calamagrostis arundinacea, Buxus sempervirens, Neottia nidus-avis, Acer heldreichii, Dentaria enneaphyllos, Potentilla micrantha, Aremonia agrimonoides, Corylus colurna, Helleborus odorus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |

Correspondance retenue : Hêtraie des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 8,9 | 12,1 | 18,5 | 20,5 | 685 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H132. G1.7 : Forêts caducifoliées thermophiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.7 |
| EUNIS 2012 | G1.7 |
| EUNIS 2022 (HabRef) | T1-9 Forêts caducifoliées thermophiles tempérées et subméditerranéennes |
| CORINE Biotopes (HabRef) | 41.6 Forêts de Chêne tauzin, 41.65 Forêts françaises de Quercus pyrenaica, 41.7 Chênaies thermophiles et supra-méditerranéennes, 41.71 Chênaies blanches occidentales et communautés apparentées, 41.711 Bois occidentaux de Quercus pubescens, 41.712 Bois sub-méditerranéens de Quercus petraea-Q. robur, 41.713 Bois de Quercus palensis, 41.714 Bois de Chênes blancs eu-méditerranéens, 41.72 Chênaies pubescentes cyrno-sardes, 41.73 Chênaies pubescentes orientales, et 10 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts et bois des climats subméditerranéens et de l'étage supraméditerranéen, dominés par des chênes caducifoliés ou semi-caducifoliés thermophiles (chêne pubescent notamment), le châtaignier, le charme-houblon.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (318 taxons ; les 40 plus cités) : Carpinus orientalis, Quercus cerris, Quercus pubescens, Quercus petraea, Fraxinus ornus, Ostrya carpinifolia, Quercus frainetto, Quercus pyrenaica, Acer campestre, Acer tataricum, Carpinus betulus, Cornus mas, Lychnis coronaria, Crataegus monogyna, Buglossoides purpurocaerulea, Lithospermum purpurocaeruleum, Castanea sativa, Tilia tomentosa, Ligustrum vulgare, Cotinus coggygria, Quercus faginea, Quercus virgiliana, Quercus polycarpa, Quercus robur, Lathyrus niger, Vincetoxicum hirundinaria, Sorbus torminalis, Mercurialis ovata, Acer monspessulanum, Quercus pedunculiflora, Fraxinus excelsior, Quercus dalechampii, Cynanchum vincetoxicum, Quercus macrolepis, Quercus pubescens ssp. pubescens, Piptatherum virescens, Paeonia peregrina, Sorbus aria, Chrysanthemum corymbosum, Quercus ilex.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H133. G1.8 : Boisements acidophiles à chênes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.8 |
| EUNIS 2012 | G1.8 |
| EUNIS 2022 (HabRef) | T1-B Chênaies acidiphiles |
| CORINE Biotopes (HabRef) | 41.5 Chênaies acidiphiles, 41.51 Bois de Chênes pédonculés et de Bouleaux, 41.52 Chênaies acidiphiles atlantiques à Hêtres, 41.521 Forêts de Chênes sessiles du nord-ouest, 41.522 Forêts armoricaine de Chênes sessiles, 41.523 Forêts sur dune, 41.53 Forêts de Chênes sessiles britanniques et irlandaises, 41.54 Chênaies aquitano-ligériennes sur podzols, 41.55 Chênaies aquitano-ligériennes sur sols lessivés ou acides, 41.56 Chênaies acidiphiles ibéro-atlantiques, et 6 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts de chêne pédonculé ou de chêne sessile sur sols acides, à canche flexueuse, myrtille, fougère aigle, chèvrefeuille, houlque molle.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (141 taxons ; les 40 plus cités) : Quercus petraea, Quercus robur, Deschampsia flexuosa, Luzula luzuloides, Castanea sativa, Fagus sylvatica, Genista tinctoria, Vaccinium myrtillus, Pinus sylvestris, Hieracium sabaudum, Hypericum pulchrum, Ilex aquifolium, Sorbus torminalis, Pteridium aquilinum, Veronica officinalis, Melampyrum pratense, Hieracium umbellatum, Teucrium scorodonia, Betula pendula, Carpinus betulus, Lembotropis nigricans, Molinia caerulea, Quercus pyrenaica, Frangula alnus, Sorbus aucuparia, Prunus avium, Tilia cordata, Calluna vulgaris, Populus tremula, Convallaria majalis, Ruscus aculeatus, Betula celtiberica, Lathyrus montanus, Cytisus nigricans, Saxifraga spathularis, Arbutus unedo, Lathyrus linifolius, Acer campestre, Acer pseudoplatanus, Euphorbia amygdaloides.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.03M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 603 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.07.03J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.03M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 43.07.03A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Chênaie des stations fraîches à humides, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 0,8 | 1,5 | 3 | 6,8 | 10,5 | 14,3 | 21,8 | 24,1 | 806 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H134. G1.9 : Boisements non riverains à bouleaux, trembles ou sorbiers

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.9 |
| EUNIS 2012 | G1.9 |
| EUNIS 2022 (HabRef) | T1-C Forêts de montagne à Betula et Populus tremula sur sols minéraux des zones tempérées et boréales, T1-D Forêts à Betula et Populus tremula sur sols minéraux des montagnes d'Europe méridionale |
| CORINE Biotopes (HabRef) | 41.B Bois de Bouleaux, 41.B1 Bois de bouleaux de plaine et colline, 41.B11 Bois de Bouleaux humides, 41.B111 Bois de Bouleaux humides septentrionaux, 41.B112 Bois de Bouleaux humides aquitano-ligériens, 41.B12 Bois de Bouleaux secs acidiphiles médio-européens, 41.B16 Bois de Bouleaux de dunes, 41.B3 Bois de Bouleaux montagnards et subalpins, 41.B31 Bois de Bouleaux en limite forestière dans les Alpes, 41.B32 Massifs forestiers de Bouleaux, et 8 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts et bois dominés par les bouleaux, le tremble ou le sorbier des oiseleurs, hors forêts marécageuses, tourbeuses et riveraines.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (143 taxons ; les 40 plus cités) : Betula pendula, Betula pubescens ssp. czerepanovii, Populus tremula, Betula pubescens, Deschampsia flexuosa, Vaccinium myrtillus, Betula celtiberica, Salix sp., Empetrum hermaphroditum, Sorbus aucuparia, Juniperus communis, Vaccinium uliginosum, Solidago virgaurea, Vaccinium vitis-idaea, Hylocomium splendens, Agrostis capillaris, Anthoxanthum odoratum, Geranium sylvaticum, Gymnocarpium dryopteris, Rubus saxatilis, Trientalis europaea, Betula nana, Corylus avellana, Betula sp., Athyrium filix-femina, Campanula rotundifolia, Carex vaginata, Festuca rubra, Filipendula ulmaria, Hierochloe odorata, Poa nemoralis, Cornus suecica, Galium verum, Oxalis acetosella, Juncus trifidus, Kobresia myosuroides, Betula carpatica, Aconitum lycoctonum, Calamagrostis purpurea, Dryopteris expansa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 42.03.02, « Vorwald frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 510 de l'extraction) |

Correspondance retenue : Pré-bois des stations fraîches.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible bon |
| Création, état moyen visé | 25 ans | onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 98, « Woodland and forest - Upland birchwoods », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 99, « Woodland and forest - Upland birchwoods », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 119, « Woodland and forest - Upland birchwoods » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 119, « Woodland and forest - Upland birchwoods » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 27,08 m²HE, 15 à 30 cm 32,5 m²HE, 30 à 80 cm 37,92 m²HE, 80 cm et plus 48,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,1 | 2,3 | 4,5 | 10,2 | 15,9 | 21,5 | 32,9 | 36,3 | 1 216 |
| moyen | 0 | 1,3 | 2,5 | 5,1 | 11,4 | 17,8 | 24,1 | 31,8 | 31,8 | 1 175 |
| mauvais | 0 | 2,5 | 5,1 | 10,2 | 22,9 | 25,4 | 25,4 | 25,4 | 25,4 | 1 131 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H135. G1.A : Boisements mésotrophes et eutrophes à chênes, charmes, frênes, érables

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.A |
| EUNIS 2012 | G1.A |
| EUNIS 2022 (HabRef) | T1-E Forêts mésiques de feuillus à Carpinus et Quercus |
| CORINE Biotopes (HabRef) | 41.2 Chênaies-charmaies, 41.21 Chênaies atlantiques mixtes à Jacinthes des bois, 41.22 Frênaies-chênaies et chênaies-charmaies aquitaniennes, 41.23 Frênaies-chênaies sub-atlantiques à primevère, 41.231 Frênaies-chênaies à Arum, 41.232 Frênaies-chênaies à Corydale, 41.233 Frênaies-chênaies à Ail, 41.24 Chênaies-charmaies à Stellaire sub-atlantiques, 41.241 Chênaies-charmaies du Nord-Ouest, 41.242 Chênaies-charmaies de Lorraine sur marnes, et 32 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois, le plus souvent mélangés, des sols riches à moyennement riches : érables, charme, frênes, chênes, tilleuls, ormes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (317 taxons ; les 40 plus cités) : Carpinus betulus, Quercus robur, Fraxinus excelsior, Quercus petraea, Fagus sylvatica, Ulmus glabra, Acer pseudoplatanus, Tilia cordata, Tilia platyphyllos, Acer platanoides, Corylus avellana, Quercus cerris, Acer campestre, Mercurialis perennis, Sorbus torminalis, Prunus avium, Stellaria holostea, Asplenium scolopendrium, Ulmus minor, Fraxinus ornus, Tilia sp., Galium odoratum, Anemone nemorosa, Tilia tomentosa, Quercus dalechampii, Euonymus europaeus, Lunaria rediviva, Fagus moesiaca, Cornus mas, Acer tataricum, Carpinus orientalis, Ranunculus ficaria, Picea abies, Acer sp., Asarum europaeum, Crataegus monogyna, Lamium galeobdolon, Pyrus pyraster, Deschampsia flexuosa, Luzula luzuloides.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.02M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 599 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.07.02J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.02M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 43.07.02A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Chênaie-charmaie, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 0,8 | 1,5 | 3 | 6,8 | 10,5 | 14,3 | 21,8 | 24,1 | 806 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H136. G1.B : Aulnaies non riveraines

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.B |
| EUNIS 2012 | G1.B |
| EUNIS 2022 (HabRef) | T1-G Aulnaies à Alnus cordata |
| CORINE Biotopes (HabRef) | 41.C Aulnaies, 41.C1 Bois d' Alnus cordata, 41.C2 Bois d'Alnus glutinosa |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Aulnaies non riveraines et non marécageuses.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (17 taxons ; les 40 plus cités) : Alnus incana, Alnus glutinosa, Urtica dioica, Anthriscus sylvestris, Mnium cuspidatum, Alnus cordata, Cardamine amara, Chaerophyllum temulentum, Equisetum telmateia, Lamium maculatum, Veronica hederifolia, Corylus avellana, Myosotis sparsiflora, Alnus sp., Betula pendula, Picea abies, Populus tremula.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 552 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.03.01J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.03.01M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.03.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Forêt marécageuse intacte, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,6 | 3,1 | 6,3 | 14,1 | 22 | 29,8 | 45,5 | 50,2 | 1 683 |
| moyen | 0 | 2,9 | 5,9 | 11,7 | 26,4 | 41 | 44 | 44 | 44 | 1 847 |
| mauvais | 0 | 7 | 14,1 | 28,1 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 1 653 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H137. G1.C : Plantations forestières très artificielles de feuillus caducifoliés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.C |
| EUNIS 2012 | G1.C |
| EUNIS 2022 (HabRef) | T1-H Plantations de feuillus caducifoliés non indigènes, T1-K Plantations de feuillus caducifoliés indigènes |
| CORINE Biotopes (HabRef) | 83.3 Plantations, 83.32 Plantations d'arbres feuillus, 83.321 Plantations de Peupliers, 83.3211 Plantations de Peupliers avec une strate herbacée élevée (Mégaphorbiaies), 83.3212 Autres plantations de Peupliers, 83.323 Plantations de Chênes exotiques, 83.324 Plantations de Robiniers, 83.325 Autres plantations d'arbres feuillus |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations de feuillus caducifoliés pour la production de bois, d'espèces exotiques, d'espèces indigènes hors de leur aire ou en peuplements nettement artificiels, souvent monospécifiques (peupleraies notamment).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (12 taxons ; les 40 plus cités) : Populus sp., Quercus sp., Robinia sp., Populus balsamifera, Populus candicans, Populus nigra, Populus trichocarpa, Populus x canadensis, Populus nigra var. italica, Populus deltoides, Robinia pseudacacia, Quercus rubra.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 43.10M, « – Mittlere Ausprägung », Biotoptypenwert 12 sur 24 (ligne 644 de l'extraction) |
| Valeur, stade jeune | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| Valeur, stade moyen | 0,5 m²HE/m² | 0,45 à 0,55 | code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.10A, « – Alte Ausprägung », 14 sur 24 |

Correspondance retenue : Plantation de feuillus d'essences introduites, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,6 | 3,1 | 6,2 | 14,1 | 21,9 | 29,7 | 45,3 | 50 | 1 675 |
| moyen | 0 | 2,9 | 5,8 | 11,7 | 26,2 | 40,8 | 43,8 | 43,8 | 43,8 | 1 838 |
| mauvais | 0 | 7 | 14 | 28 | 35 | 35 | 35 | 35 | 35 | 1 645 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H138. G1.D : Vergers d'arbres fruitiers et à noix

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G1.D |
| EUNIS 2012 | G1.D |
| EUNIS 2022 (HabRef) | V6-1 Vergers d'arbres fruitiers caducifoliés et d'arbres à noix |
| CORINE Biotopes (HabRef) | 83.1 Vergers de hautes tiges, 83.12 Châtaigneraies, 83.13 Vergers à Noyers, 83.14 Vergers à Amandiers, 83.15 Vergers, 83.151 Vergers septentrionaux, 83.152 Vergers méridionaux, 83.18 Autres vergers à hautes tiges |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EV1 (vergers) |

**Définition**

Peuplements d'arbres cultivés pour leurs fruits ou leurs fleurs, formant un couvert permanent à maturité. Les vergers anciens et extensifs abritent une flore et une faune riches.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (3 taxons ; les 40 plus cités) : Juglans sp., Castanea sp., Rosaceae sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 41.06.01.MA, « – Mit mittlerem bis altem Baumbestand », Biotoptypenwert 19 sur 24 (ligne 495 de l'extraction) |

Correspondance retenue : Verger de haute tige sur prairie, arbres moyens à âgés ; un verger intensif est saisi en FB.3.

**Grille d'état EV1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Présence d'arbres anciens ou vétérans | oui |
| B | Bois mort dans ou sur les arbres, ou au sol, pour au moins 20 % des arbres mûrs | oui |
| C | Moins de 5 % des arbres fruitiers étouffés par les fourrés, fourrés sur moins de 10 % du sol | non |
| D | Taille de formation ou de restauration qui prolonge la vie des arbres | non |
| E | Au moins 95 % des arbres exempts de dégâts d'origine humaine ou animale (abroutissement, écorçage, liens non ajustés) | non |
| F | Prairie non surpâturée, piétinement sous le houppier de 10 % des arbres au plus | non |
| G | Prairie d'une richesse en espèces équivalente à une prairie de valeur moyenne ou plus | non |
| H | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 10 % du sol | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 15, « Grassland - Traditional orchards » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 15, « Grassland - Traditional orchards » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,6 | 5,3 | 10,6 | 23,8 | 36,9 | 50,1 | 76,5 | 79,2 | 2 731 |
| moyen | 0 | 3,5 | 6,9 | 13,9 | 31,2 | 48,5 | 65,8 | 69,3 | 69,3 | 2 736 |
| mauvais | 0 | 11,1 | 22,2 | 44,3 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 2 605 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H139. G2.1 : Forêts méditerranéennes de chênes sempervirents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.1 |
| EUNIS 2012 | G2.1 |
| EUNIS 2022 (HabRef) | T2-1 Forêts méditerranéennes à Chênes sempervirents |
| CORINE Biotopes (HabRef) | 45.2 Forêts de Chênes lièges (suberaies), 45.21 Forêts thyrrhéniennes de Chênes lièges, 45.211 Forêts provençales de Chênes lièges, 45.212 Forêts corses de Chênes lièges, 45.216 Suberaies catalano-pyrénéennes, 45.24 Forêts aquitaniennes de Chênes lièges, 45.3 Forêts de Chênes verts méso- et supra méditerranéennes, 45.31 Forêts de Chêne verts, 45.311 Forêts de Chênes verts ibériques nord-occidentales, 45.312 Forêts de Chênes verts de la plaine catalo-provençale, et 8 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois dominés par des chênes sempervirents arborescents : chêne vert, chêne-liège, chêne kermès.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (124 taxons ; les 40 plus cités) : Quercus ilex, Quercus rotundifolia, Quercus suber, Smilax aspera, Quercus coccifera, Arbutus unedo, Rubia peregrina, Viburnum tinus, Phillyrea angustifolia, Pistacia lentiscus, Phillyrea media, Rosa sempervirens, Clematis flammula, Lonicera implexa, Ruscus aculeatus, Rhamnus alaternus, Cyclamen repandum, Phillyrea latifolia, Lonicera etrusca, Pistacia terebinthus, Luzula forsteri, Myrtus communis, Chamaerops humilis, Erica arborea, Crataegus monogyna, Quercus faginea, Quercus alnifolia, Juniperus oxycedrus, Quercus calliprinos, Hedera helix, Laurus nobilis, Daphne gnidium, Fraxinus ornus, Quercus pubescens, Tamus communis, Quercus pyrenaica, Ostrya carpinifolia, Asplenium onopteris, Daphne laureola, Olea europaea.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen : aucun type BKompV méditerranéen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H140. G2.2 : Forêts sclérophylles continentales

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.2 |
| EUNIS 2012 | G2.2 |
| EUNIS 2022 (HabRef) | T2-2 Forêts laurophylles continentales |
| CORINE Biotopes (HabRef) | 45.5 Forêts de Chênes et Lauriers |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts sempervirentes laurifoliées ou mixtes des zones tempérées chaudes humides et des enclaves humides de la région méditerranéenne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (5 taxons ; les 40 plus cités) : Laurus nobilis, Laurus sp., Laurocerasus officinalis, Prunus laurocerasus, Buxus hyrcanica.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H141. G2.4 : Boisements à caroubier et olivier

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.4 |
| EUNIS 2012 | G2.4 |
| EUNIS 2022 (HabRef) | T2-4 Forêts à Ceratonia siliqua et Olea europea |
| CORINE Biotopes (HabRef) | 45.1 Forêts d'Oliviers et de Caroubiers, 45.11 Bois d'Oliviers sauvages (oléastres), 45.12 Bois de Caroubiers |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois thermoméditerranéens dominés par l'olivier sauvage, le caroubier, le lentisque ou le myrte, à couvert assez haut et fermé.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (8 taxons ; les 40 plus cités) : Pistacia lentiscus, Ceratonia siliqua, Olea europaea ssp. cerasiformis, Pistacia atlantica, Olea europaea var. sylvestris, Olea europae var. sylvestris, Myrtus communis, Olea europaea.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 92, « Woodland and forest - Lowland mixed deciduous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 93, « Woodland and forest - Lowland mixed deciduous woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 113, « Woodland and forest - Lowland mixed deciduous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H142. G2.6 : Bois de houx

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.6 |
| EUNIS 2012 | G2.6 |
| EUNIS 2022 (HabRef) | T2-7 Forêts à Ilex aquifolium |
| CORINE Biotopes (HabRef) | 45.8 Bois de Houx |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois dominés par le houx arborescent, notamment en Corse et en faciès des hêtraies et chênaies acidiphiles.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Ilex aquifolium, Ilex sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |

Correspondance retenue : Hêtraie des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 8,9 | 12,1 | 18,5 | 20,5 | 685 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H143. G2.8 : Plantations forestières de feuillus sempervirents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.8 |
| EUNIS 2012 | G2.8 |
| EUNIS 2022 (HabRef) | T2-9 Plantations forestières très artificielles de feuillus sempervirents, T2-A Plantations de feuillus sempervirents non indigènes |
| CORINE Biotopes (HabRef) | 83.3 Plantations, 83.32 Plantations d'arbres feuillus, 83.322 Plantations d'Eucalyptus, 83.323 Plantations de Chênes exotiques, 83.325 Autres plantations d'arbres feuillus |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations de feuillus sempervirents pour la production de bois, exotiques ou hors de leur aire, souvent monospécifiques (eucalyptus notamment).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (19 taxons ; les 40 plus cités) : Eucalyptus sp., Eucalyptus globulus, Eucalyptus nitens, Eucalyptus pauciflora, Eucalyptus viminalis, Eucalyptus cornuta, Eucalyptus regnans, Eucalyptus delegatensis, Eucalyptus maidenii, Eucalyptus radiata, Eucalyptus grandis, Eucalyptus bicostata, Eucalyptus brockwayi, Eucalyptus cladocalyx, Eucalyptus fastigata, Eucalyptus camaldulensis, Eucalyptus astringens, Eucalyptus gomphocephala, Quercus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 43.10M, « – Mittlere Ausprägung », Biotoptypenwert 12 sur 24 (ligne 644 de l'extraction) |
| Valeur, stade jeune | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| Valeur, stade moyen | 0,5 m²HE/m² | 0,45 à 0,55 | code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.10A, « – Alte Ausprägung », 14 sur 24 |

Correspondance retenue : Plantation de feuillus d'essences introduites, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,6 | 3,1 | 6,2 | 14,1 | 21,9 | 29,7 | 45,3 | 50 | 1 675 |
| moyen | 0 | 2,9 | 5,8 | 11,7 | 26,2 | 40,8 | 43,8 | 43,8 | 43,8 | 1 838 |
| mauvais | 0 | 7 | 14 | 28 | 35 | 35 | 35 | 35 | 35 | 1 645 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H144. G2.9 : Vergers et bosquets sempervirents (oliveraies)

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G2.9 |
| EUNIS 2012 | G2.9 |
| EUNIS 2022 (HabRef) | V6-2 Vergers et bosquets sempervirents |
| CORINE Biotopes (HabRef) | 83.1 Vergers de hautes tiges, 83.11 Oliveraies, 83.111 Oliveraies traditionnelles, 83.112 Oliveraies intensives, 83.16 Vergers à agrumes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EV1 (vergers) |

**Définition**

Vergers et bosquets sempervirents, surtout oliveraies et agrumes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (2 taxons ; les 40 plus cités) : Phoenix dactylifera, Olea europaea var. europaea.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 41.06.01.MA, « – Mit mittlerem bis altem Baumbestand », Biotoptypenwert 19 sur 24 (ligne 495 de l'extraction) |

Correspondance retenue : Verger traditionnel, arbres moyens à âgés.

**Grille d'état EV1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Présence d'arbres anciens ou vétérans | oui |
| B | Bois mort dans ou sur les arbres, ou au sol, pour au moins 20 % des arbres mûrs | oui |
| C | Moins de 5 % des arbres fruitiers étouffés par les fourrés, fourrés sur moins de 10 % du sol | non |
| D | Taille de formation ou de restauration qui prolonge la vie des arbres | non |
| E | Au moins 95 % des arbres exempts de dégâts d'origine humaine ou animale (abroutissement, écorçage, liens non ajustés) | non |
| F | Prairie non surpâturée, piétinement sous le houppier de 10 % des arbres au plus | non |
| G | Prairie d'une richesse en espèces équivalente à une prairie de valeur moyenne ou plus | non |
| H | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 10 % du sol | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 30 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 14, « Grassland - Traditional orchards », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 25 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 15, « Grassland - Traditional orchards », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 15, « Grassland - Traditional orchards » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 15, « Grassland - Traditional orchards » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,6 | 5,3 | 10,6 | 23,8 | 36,9 | 50,1 | 76,5 | 79,2 | 2 731 |
| moyen | 0 | 3,5 | 6,9 | 13,9 | 31,2 | 48,5 | 65,8 | 69,3 | 69,3 | 2 736 |
| mauvais | 0 | 11,1 | 22,2 | 44,3 | 55,4 | 55,4 | 55,4 | 55,4 | 55,4 | 2 605 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H145. G3.1 : Boisements à épicéas et sapins

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.1 |
| EUNIS 2012 | G3.1 |
| EUNIS 2022 (HabRef) | T3-1 Forêts tempérées à Picea et Abies, T3-2 Sapinières montagnardes tempérées, T3-3 Sapinières montagnardes méditerranéennes |
| CORINE Biotopes (HabRef) | 42.1 Sapinières, 42.11 Sapinières neutrophiles, 42.111 Sapinières neutrophiles intra-alpines, 42.1111 Sapinières à Oxalis, 42.1112 Sapinières à hautes herbes, 42.1113 Sapinières à Trochiscanthes, 42.112 Sapinières neutrophiles de la zone du Hêtre, 42.113 Sapinières intra-pyrénéennes, 42.12 Sapinières calciphiles, 42.121 Sapinières calcicoles intra-alpines, et 34 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois dominés par les sapins ou les épicéas.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (173 taxons ; les 40 plus cités) : Picea abies, Abies alba, Fagus sylvatica, Vaccinium myrtillus, Calamagrostis villosa, Homogyne alpina, Oxalis acetosella, Pinus nigra, Pinus sylvestris, Abies pinsapo, Soldanella hungarica ssp. major, Abies borisii-regis, Bazzania trilobata, Calamagrostis varia, Listera cordata, Abies cephalonica, Calamagrostis arundinacea, Abies nebrodensis, Abies nordmanniana, Hylocomium splendens, Abies sp., Sorbus aucuparia, Cicerbita alpina, Festuca flavescens, Rhododendron ferrugineum, Vaccinium vitis-idaea, Campanula abietina, Luzula sylvatica, Valeriana montana, Stellaria nemorum, Goodyera repens, Hieracium rotundatum, Abies bornmuelleriana, Sphagnum girgensohnii, Sphagnum palustre, Bazzania sp., Abies equi-trojani, Adenostyles alliariae, Geranium sylvaticum, Peucedanum ostruthium.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 44.03.03M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 692 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 44.03.03J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 44.03.03M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 44.03.03A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Sapinière-pessière montagnarde, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H146. G3.2 : Boisements alpins à mélèze et pin cembro

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.2 |
| EUNIS 2012 | G3.2 |
| EUNIS 2022 (HabRef) | T3-4 Forêts subalpines tempérées à Larix, Pinus cembra et Pinus uncinata |
| CORINE Biotopes (HabRef) | 42.3 Forêts de Mélèzes et d'Arolles, 42.33 Forêts occidentales de Mélèzes, de Pins de montagne et d'Arolles, 42.331 Forêts occidentales de Mélèzes et de Mélèzes et de Pins de montagne, 42.3311 Forêts occidentales de Mélèzes et de Mélèzes et de Pins de montagne sur landes, 42.3312 Forêts occidentales de Mélèzes et de Mélèzes et de Pins de montagne sur prairies, 42.3313 Forêts occidentales de Mélèzes et de Mélèzes et de Pins de montagne sur hautes herbes, 42.332 Forêts occidentales d'Arolles, 42.3321 Forêts occidentales d'Arolles sur silice, 42.3322 Forêts occidentales d'Arolles à Genévriers nains, 42.3323 Forêts occidentales calcicoles d'Arolles, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts subalpines dominées par le mélèze ou le pin cembro, en peuplements purs ou mélangés.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (26 taxons ; les 40 plus cités) : Pinus cembra, Larix decidua, Picea abies, Pinus mugo, Pinus uncinata, Larix sp., Campanula abietina, Soldanella hungarica ssp. major, Calamagrostis villosa, Luzula albida, Vaccinium myrtillus, Rhododendron ferrugineum, Larix decidua ssp. polonica, Erica herbacea, Polygala chamaebuxus, Rhododendron hirsutum, Moneses uniflora, Saxifraga cuneifolia, Aquilegia transsilvanica, Hieracium rotundatum, Ranunculus carpaticus, Tricetum fuscum, Juniperus nana, Rhododendron myrtifolium, Bruckenthalia spiculifolia, Melampyrum saxosum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 70.03M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 884 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 70.03J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 70.03M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 70.03A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Mélézein-cembraie subalpin, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,8 | 1,5 | 3,1 | 7 | 10,8 | 14,7 | 22,4 | 24,8 | 829 |
| moyen | 0 | 0,7 | 1,4 | 2,7 | 6,1 | 9,5 | 12,9 | 19,6 | 21,7 | 725 |
| mauvais | 0 | 1,7 | 3,5 | 6,9 | 15,6 | 17,3 | 17,3 | 17,3 | 17,3 | 771 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H147. G3.3 : Pinèdes à pin à crochets

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.3 |
| EUNIS 2012 | G3.3 |
| EUNIS 2022 (HabRef) | T3-4 Forêts subalpines tempérées à Larix, Pinus cembra et Pinus uncinata |
| CORINE Biotopes (HabRef) | 42.4 Forêts de Pins de montagne, 42.41 Forêts de Pins de montagne à Rhododendron ferrugineux, 42.411 Forêts de Pins de montagne à Rhododendron des Alpes externes, 42.412 Forêts de Pins de montagne à Rhododendron du Jura, 42.413 Forêts pyrénéennes de Pins de montagne à Rhododendron, 42.42 Forêts de Pins de montagne xéroclines, 42.421 Forêts de Pins de montagne des Alpes internes, 42.4211 Forêts de Pins de montagne à laîche humble, 42.4212 Forêts de Pins de montagne à Erica herbacea, 42.4213 Forêts de Pins de montagne à Silène rupestre, et 14 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts surtout subalpines dominées par le pin à crochets, ouvertes, à strate arbustive très développée.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (54 taxons ; les 40 plus cités) : Pinus uncinata, Juniperus nana, Rhododendron ferrugineum, Vaccinium myrtillus, Arctostaphylos uva-ursi, Juniperus hemisphaerica, Deschampsia flexuosa, Homogyne alpina, Cotoneaster integerrimus, Calluna vulgaris, Vaccinium uliginosum, Dryas octopetala, Festuca gautieri, Sesleria caerulea, Valeriana montana, Hepatica nobilis, Cladonia rangiferina, Astrantia minor, Bartsia alpina, Empetrum hermaphroditum, Selaginella spinosa, Vaccinium vitis-idaea, Lycopodium selago, Arctostaphylos alpinus, Daphne striata, Erica herbacea, Polygala chamaebuxus, Rhododendron hirsutum, Lycopodium annotinum, Amelanchier vulgaris, Polygala calcarea, Helectotrichon sedenense, Avena montana, Hippocrepis comosa, Primula suaveolens, Teucrium pyrenaicum, Rhamnus alpinus, Polystichum spinulosum, Dryopteris linneana, Oxalis acetosella.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Pinède sèche des rochers, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 93, « Woodland and forest - Native pine woodlands », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 94, « Woodland and forest - Native pine woodlands », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 114, « Woodland and forest - Native pine woodlands » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 8,9 | 12,1 | 18,5 | 20,5 | 685 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H148. G3.4 : Pinèdes à pin sylvestre

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.4 |
| EUNIS 2012 | G3.4 |
| EUNIS 2022 (HabRef) | T3-5 Pinèdes continentales tempérées à Pinus sylvestris, T3-6 Pinèdes montagnardes tempérées et subméditerranéennes à Pinus sylvestris et Pinus nigra, T3-68 Pinus sylvestris forest on chalk in the steppe zone, T3-7 Pinèdes montagnardes méditerranéennes à Pinus sylvestris et Pinus nigra |
| CORINE Biotopes (HabRef) | 42.5 Forêts de Pins sylvestres, 42.52 Forêts de Pins sylvestres médio-européennes, 42.521 Forêts subcontinentales de Pins sylvestres, 42.5212 Forêts de Pins sylvestres des plaines occidentales, 42.522 Forêts hercyniennes de Pins sylvestres, 42.5223 Forêts de Pins sylvestres des Vosges, 42.5224 Pinèdes de pin sylvestre des grès de Luxembourg, 42.523 Forêts steppiques de Pins sylvestres planitiaires, 42.53 Forêts steppiques intra-alpines à Ononis, 42.54 Forêts de Pins sylvestre à Erica herbacea, et 13 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts de pin sylvestre des zones némorale et méditerranéenne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (196 taxons ; les 40 plus cités) : Pinus sylvestris, Erica herbacea, Vaccinium myrtillus, Calluna vulgaris, Deschampsia flexuosa, Molinia caerulea, Picea abies, Pinus sylvestris var. scotica, Betula pendula, Juniperus communis, Goodyera repens, Polygala chamaebuxus, Sorbus aria, Galium lucidum, Juniperus sabina, Arctostaphylos uva-ursi, Epipactis atrorubens, Pinus sylvestris var. iberica, Amelanchier ovalis, Carex alba, Carex humilis, Erica carnea, Buxus sempervirens, Sorbus aucuparia, Pinus sylvestris ssp. sylvestris, Fagus sylvatica, Moneses uniflora, Luzula luzuloides, Vaccinium vitis-idaea, Polytrichum commune, Corylus avellana, Melica nutans, Quercus petraea, Quercus robur, Berberis vulgaris, Melampyrum pratense, Melampyrum sylvaticum, Calamagrostis varia, Pyrola chlorantha, Festuca ovina.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 44.02.03M, « – Mittlere Ausprägung », Biotoptypenwert 19 sur 24 (ligne 675 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.02.03J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7917 m²HE/m² | 0,7125 à 0,8708 | code 44.02.03M, « – Mittlere Ausprägung », 19 sur 24 |
| Valeur, stade âgé | 0,9167 m²HE/m² | 0,825 à 1 | code 44.02.03A, « – Alte Ausprägung », 22 sur 24 |

Correspondance retenue : Pinède sèche sur sable, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 79,17 |
| État moyen | 69,27 |
| Mauvais état | 55,42 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 39,59 m²HE, 15 à 30 cm 47,5 m²HE, 30 à 80 cm 55,42 m²HE, 80 cm et plus 71,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,3 | 6,6 | 14,9 | 23,2 | 31,5 | 48,1 | 53 | 1 777 |
| moyen | 0 | 1,5 | 2,9 | 5,8 | 13,1 | 20,3 | 27,6 | 42,1 | 46,4 | 1 555 |
| mauvais | 0 | 3,7 | 7,4 | 14,9 | 33,4 | 37,1 | 37,1 | 37,1 | 37,1 | 1 652 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H149. G3.5 : Pinèdes à pin noir

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.5 |
| EUNIS 2012 | G3.5 |
| EUNIS 2022 (HabRef) | T3-6 Pinèdes montagnardes tempérées et subméditerranéennes à Pinus sylvestris et Pinus nigra, T3-7 Pinèdes montagnardes méditerranéennes à Pinus sylvestris et Pinus nigra |
| CORINE Biotopes (HabRef) | 42.6 Forêts de Pins noirs, 42.63 Forêts de Pins de Salzmann, 42.631 Forêts de Pins de Salzmann des Causses, 42.632 Forêts pré-pyrénéennes de Pins de Salzmann, 42.64 Forêts corses de Pins laricio, 42.641 Forêts denses montagnardes de Pin laricio, 42.642 Forêts ouvertes montagnardes de Pins laricio, 42.643 Forêts de Pins laricio supra-méditerranéennes, 42.67 Reboisement en Pins noirs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts dominées par des pins du groupe du pin noir (pin de Salzmann compris).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (105 taxons ; les 40 plus cités) : Pinus nigra, Pinus nigra ssp. nigra, Pinus pallasiana, Pinus nigra ssp. pallasiana, Pinus sylvestris, Pinus laricio, Pinus salzmannii, Erica carnea, Cyclamen purpurascens, Erica herbacea, Buxus sempervirens, Juniperus oxycedrus, Pinus salzmannii var. pyrenaica, Rosmarinus officinalis, Amelanchier ovalis, Abies alba, Ostrya carpinifolia, Quercus dalechampii, Pinus dalmatica, Carex humilis, Galium lucidum, Polygala chamaebuxus, Epipactis atrorubens, Pinus salzmannii var. hispanica, Pinus banatica, Pinus nigra var. banatica, Juniperus communis, Lonicera etrusca, Quercus ilex, Quercus pubescens, Cornus sanguinea, Pinus nigra ssp. dalmatica, Epipactis troodi, Euphorbia cassia, Jurinea cypria, Pinus pallasiana var. caramanica, Platanthera holmboei, Thlaspi cyprium, Sitta whiteheadi, Pinus nigra ssp. salzmannii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Pinède sèche des rochers, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,5 | 3 | 5,9 | 13,3 | 20,8 | 28,2 | 43 | 47,5 | 1 590 |
| moyen | 0 | 1,3 | 2,6 | 5,2 | 11,7 | 18,2 | 24,7 | 37,6 | 41,5 | 1 391 |
| mauvais | 0 | 3,3 | 6,6 | 13,3 | 29,9 | 33,2 | 33,2 | 33,2 | 33,2 | 1 478 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H150. G3.7 : Pinèdes méditerranéennes hors pin noir

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.7 |
| EUNIS 2012 | G3.7 |
| EUNIS 2022 (HabRef) | T3-A Pinèdes méditerranéennes planitiaires à submontagnardes |
| CORINE Biotopes (HabRef) | 42.8 Bois de Pins méditerranéens, 42.81 Forêts de Pins maritimes, 42.811 Forêts de Pins et de Chênes verts des Charentes, 42.812 Forêts de Pins et de Chênes lièges aquitaniennes, 42.813 Plantations de Pins maritimes des Landes, 42.82 Forêts de Pins mésogéens, 42.822 Pinèdes de Pin mésogéen des Corbières, 42.823 Forêts de Pins mésogéens franco-italiennes, 42.824 Forêts corses de Pins mésogéens, 42.83 Forêts de Pins parasols, et 7 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts de pins thermophiles méditerranéens et thermo-atlantiques (pin d'Alep, pin maritime, pin pignon), souvent stades de succession des chênaies sempervirentes, plantations anciennes dans leur aire comprises.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (63 taxons ; les 40 plus cités) : Pinus pinea, Pinus pinaster, Pinus halepensis, Pinus pinaster ssp. atlantica, Cytisus scoparius, Arbutus unedo, Cistus salvifolius, Erica scoparia, Rubia peregrina, Quercus suber, Cistus laurifolius, Calicotome spinosa, Erica arborea, Hedera helix, Quercus robur, Ruscus aculeatus, Quercus ilex, Pinus brutia, Juniperus oxycedrus, Quercus pyrenaica, Quercus rotundifolia, Quercus faginea, Corynephorus canescens, Crataegus monogyna, Juniperus communis, Juniperus thurifera, Lavandula latifolia, Salvia officinalis, Cistus albidus, Cistus monspeliensis, Ulex australis, Erica cinerea, Frangula alnus, Ilex aquifolium, Pteridium aquilinum, Calluna vulgaris, Genista corsica, Lavandula stoechas, Pistacia lentiscus, Rosmarinus officinalis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Pinède sèche des rochers, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 95, « Woodland and forest - Other Scot's pine woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 15 ans | onglet G-5, ligne 96, « Woodland and forest - Other Scot's pine woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 116, « Woodland and forest - Other Scot's pine woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,5 | 3 | 5,9 | 13,3 | 20,8 | 28,2 | 43 | 47,5 | 1 590 |
| moyen | 0 | 1,3 | 2,6 | 5,2 | 11,7 | 18,2 | 24,7 | 37,6 | 41,5 | 1 391 |
| mauvais | 0 | 3,3 | 6,6 | 13,3 | 29,9 | 33,2 | 33,2 | 33,2 | 33,2 | 1 478 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H151. G3.9 : Bois de cupressacées ou de taxacées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.9 |
| EUNIS 2012 | G3.9 |
| EUNIS 2022 (HabRef) | T3-C Forêts à Taxus baccata, T3-D Forêts de Cupressaceae méditérranéennes |
| CORINE Biotopes (HabRef) | 42.A Forêts dominées par les Cyprès, les Genévriers et les Ifs, 42.A2 Forêts de Juniperus thurifera, 42.A27 Bois pyrénéens de Genévriers thurifères, 42.A28 Bois sud-alpiens de Genévriers thurifères, 42.A29 Bois de Genévriers thurifères de l'Isère, 42.A2A Bois de Génevriers thurifères corses, 42.A7 Forêts d'Ifs, 42.A72 Forêts d'Ifs corses, 42.A76 Forêts d'Ifs provençales, 42.A9 Bois de Genévriers oxycèdres, et 1 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois dominés par le cyprès, les genévriers arborescents ou l'if.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (66 taxons ; les 40 plus cités) : Juniperus thurifera, Taxus baccata, Juniperus excelsa, Cedrus libani, Ilex aquifolium, Cupressus sempervirens, Tetraclinis articulata, Juniperus sabina, Juniperus oxycedrus, Cedrus brevifolia, Juniperus phoenicea, Cupressus sp., Juniperus sp., Pinus laricio, Juniperus nana, Viburnum lantana, Berberis vulgaris ssp. cantabrica, Rhamnus alpinus, Fraxinus excelsior, Picea abies, Pinus pallasiana, Cedrus atlantica, Rhamnus lycioides, Acer platanoides, Alliaria officinalis, Populus tremula, Ulmus montana, Acer sempervirens, Campanula michauxioides, Ebenus boissieri, Paeonia turcica, Pentapera bocquetii, Oryzopsis holciformis, Juniperus foetidissima, Mercurialis perennis, Sorbus aria, Buxus sempervirens, Juniperus brevifolia, Juniperus polycarpos, Juniperus seravshanica.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 667 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.02.01J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 44.02.01M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 44.02.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Pinède sèche des rochers, stade moyen : aucun type BKompV d'ifs ou de genévriers arborescents.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 91, « Woodland and forest - Lowland beech and yew woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 92, « Woodland and forest - Lowland beech and yew woodland », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |
| Difficulté d'amélioration | 0,33 | onglet G-3, ligne 112, « Woodland and forest - Lowland beech and yew woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,7 | 1,5 | 2,9 | 6,6 | 10,2 | 13,9 | 21,2 | 23,4 | 783 |
| moyen | 0 | 0,6 | 1,3 | 2,6 | 5,8 | 8,9 | 12,1 | 18,5 | 20,5 | 685 |
| mauvais | 0 | 1,6 | 3,3 | 6,5 | 14,7 | 16,4 | 16,4 | 16,4 | 16,4 | 728 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H152. G3.E : Forêts de conifères des tourbières

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.E |
| EUNIS 2012 | G3.E |
| EUNIS 2022 (HabRef) | T3-J Forêts tourbeuses à Pinus et Larix, T3-K Pessières tourbeuses |
| CORINE Biotopes (HabRef) | 44.A Forêts marécageuses de Bouleaux et de Conifères, 44.A2 Bois tourbeux de Pins sylvestres, 44.A3 Bois tourbeux de Pins de montagne, 44.A4 Bois d'Epicéas à Sphaignes, 44.A41 Pessières à Sphaignes montagnardes, 44.A42 Tourbières boisées à Epicéas |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Bois de pins ou d'épicéas, parfois mêlés de bouleau pubescent, colonisant les tourbières et les bas-marais.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (47 taxons ; les 40 plus cités) : Pinus sylvestris, Picea abies, Betula pubescens, Eriophorum vaginatum, Vaccinium uliginosum, Vaccinium myrtillus, Sorbus aucuparia, Sphagnum sp., Vaccinium oxycoccos, Ledum palustre, Vaccinium vitis-idaea, Frangula alnus, Andromeda polifolia, Betula carpatica, Sphagnum girgensohnii, Calamagrostis villosa, Listera cordata, Maianthemum bifolium, Deschampsia flexuosa, Agrostis canina, Molinia caerulea, Salix caprea, Salix cinerea, Salix pentandra, Carex sp., Betula nana, Pinus mugo, Pinus uncinata, Pinus rotundata, Myrica gale, Calluna vulgaris, Eriophorum latifolium, Picea sp., Pinus sp., Betula pendula, Carex pauciflora, Chamaedaphne calyculata, Salix sp., Moneses uniflora, Oxalis acetosella.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 44.01.02M, « – Mittlere Ausprägung », Biotoptypenwert 20 sur 24 (ligne 654 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.01.02J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 44.01.02M, « – Mittlere Ausprägung », 20 sur 24 |
| Valeur, stade âgé | 0,9583 m²HE/m² | 0,8625 à 1 | code 44.01.02A, « – Alte Ausprägung », 23 sur 24 |

Correspondance retenue : Pinède tourbeuse, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,5 | 7 | 15,7 | 24,4 | 33,1 | 50,6 | 55,8 | 1 870 |
| moyen | 0 | 3,3 | 6,5 | 13 | 29,3 | 45,6 | 48,9 | 48,9 | 48,9 | 2 052 |
| mauvais | 0 | 7,8 | 15,6 | 31,3 | 39,1 | 39,1 | 39,1 | 39,1 | 39,1 | 1 837 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H153. G3.F : Plantations très artificielles de conifères

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G3.F |
| EUNIS 2012 | G3.F |
| EUNIS 2022 (HabRef) | T3-M Plantations de conifères non indigènes, T3-N Plantation de conifères indigènes |
| CORINE Biotopes (HabRef) | 83.3 Plantations, 83.31 Plantations de conifères, 83.311 Plantations de conifères indigènes, 83.3111 Plantations de Sapins, d'Epicéas et de Mélèzes européens, 83.3112 Plantations de Pins européens, 83.3113 Plantations de Cyprès et de Genévriers européens, 83.312 Plantations de conifères exotiques, 83.3121 Plantations d'Epicéas, de Sapins exotiques, de Sapin de Douglas et de Cèdres, 83.3122 Plantations de Pins exotiques, 83.3123 Autres plantations de conifères exotiques |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations de conifères exotiques, ou européens hors de leur aire, ou indigènes en peuplements nettement artificiels, souvent monospécifiques (douglas notamment).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (9 taxons ; les 40 plus cités) : Abies sp., Cedrus sp., Larix sp., Picea sp., Pinus sp., Pseudotsuga sp., Cupressus sp., Juniperus sp., Taxus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 44.05M, « – Mittlere Ausprägung », Biotoptypenwert 10 sur 24 (ligne 712 de l'extraction) |
| Valeur, stade jeune | 0,25 m²HE/m² | 0,225 à 0,275 | code 44.05J, « – Junge Ausprägung », 6 sur 24 |
| Valeur, stade moyen | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 44.05M, « – Mittlere Ausprägung », 10 sur 24 |
| Valeur, stade âgé | 0,5 m²HE/m² | 0,45 à 0,55 | code 44.05A, « – Alte Ausprägung », 12 sur 24 |

Correspondance retenue : Plantation de résineux d'essences introduites, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 25 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,3 | 2,6 | 5,2 | 11,7 | 18,2 | 24,7 | 37,8 | 41,7 | 1 396 |
| moyen | 0 | 1,2 | 2,4 | 4,9 | 10,9 | 17 | 23,1 | 35,2 | 36,5 | 1 258 |
| mauvais | 0 | 5,8 | 11,7 | 23,3 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 371 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H154. G4.1 : Forêts mixtes marécageuses

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.1 |
| EUNIS 2012 | G4.1 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts marécageuses de feuillus associées à des conifères des tourbières.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (6 taxons ; les 40 plus cités) : Betula pubescens, Alnus sp., Picea sp., Pinus sp., Populus sp., Quercus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.03.01M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 552 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.03.01J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.03.01M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.03.01A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Forêt marécageuse intacte, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 101, « Woodland and forest - Wet woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 102, « Woodland and forest - Wet woodland », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 122, « Woodland and forest - Wet woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,6 | 3,1 | 6,3 | 14,1 | 22 | 29,8 | 45,5 | 50,2 | 1 683 |
| moyen | 0 | 2,9 | 5,9 | 11,7 | 26,4 | 41 | 44 | 44 | 44 | 1 847 |
| mauvais | 0 | 7 | 14,1 | 28,1 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 1 653 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H155. G4.6 : Forêts mixtes à sapin, épicéa et hêtre

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.6 |
| EUNIS 2012 | G4.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 43.1 Hêtraies mixtes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts où le hêtre partage la canopée avec le sapin ou l'épicéa, caractéristiques de l'étage montagnard.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (6 taxons ; les 40 plus cités) : Fagus sylvatica, Abies sp., Fagus sp., Picea sp., Pinus sp., Fagus orientalis.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.07.06M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 615 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.07.06J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.07.06M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.07.06A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Hêtraie-sapinière montagnarde, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,3 | 4,7 | 9,4 | 21,1 | 32,8 | 44,5 | 68 | 75 | 2 512 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 41,6 | 63,4 | 65,6 | 2 264 |
| mauvais | 0 | 10,5 | 21 | 42 | 52,5 | 52,5 | 52,5 | 52,5 | 52,5 | 2 468 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H156. G4.8 : Forêts mixtes non riveraines de feuillus et de conifères

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.8 |
| EUNIS 2012 | G4.8 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts mixtes non riveraines, sans pins notables, associant hêtre, bouleaux, tremble ou sorbier à des sapins ou épicéas.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (8 taxons ; les 40 plus cités) : Corylus avellana, Populus tremula, Abies sp., Betula sp., Fagus sp., Picea sp., Sorbus aucuparia, Pinus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |

Correspondance retenue : Hêtraie mêlée des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,2 | 4,4 | 8,9 | 19,9 | 31 | 42,1 | 64,2 | 70,8 | 2 373 |
| moyen | 0 | 2,1 | 4,1 | 8,3 | 18,6 | 28,9 | 39,3 | 59,9 | 62 | 2 138 |
| mauvais | 0 | 9,9 | 19,8 | 39,7 | 49,6 | 49,6 | 49,6 | 49,6 | 49,6 | 2 330 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H157. G4.9 : Forêts caducifoliées mixtes avec cupressacées ou taxacées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.9 |
| EUNIS 2012 | G4.9 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts mixtes non riveraines, sans pins notables, associant les essences des boisements mésotrophes (chênes, charme, frênes, érables, tilleuls) à des cupressacées ou à l'if.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (9 taxons ; les 40 plus cités) : Cupressaceae sp., Taxaceae sp., Acer sp., Carpinus sp., Pinus sp., Quercus sp., Tilia sp., Fraxinus sp., Ulmus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », Biotoptypenwert 17 sur 24 (ligne 607 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.07.04J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 43.07.04M, « – Mittlere Ausprägung », 17 sur 24 |
| Valeur, stade âgé | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 43.07.04A, « – Alte Ausprägung », 20 sur 24 |

Correspondance retenue : Hêtraie mêlée des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 70,83 |
| État moyen | 61,98 |
| Mauvais état | 49,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 35,41 m²HE, 15 à 30 cm 42,5 m²HE, 30 à 80 cm 49,58 m²HE, 80 cm et plus 63,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,2 | 4,4 | 8,9 | 19,9 | 31 | 42,1 | 64,2 | 70,8 | 2 373 |
| moyen | 0 | 2,1 | 4,1 | 8,3 | 18,6 | 28,9 | 39,3 | 59,9 | 62 | 2 138 |
| mauvais | 0 | 9,9 | 19,8 | 39,7 | 49,6 | 49,6 | 49,6 | 49,6 | 49,6 | 2 330 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H158. G4.B : Forêts mixtes méditerranéennes de pins et de chênes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.B |
| EUNIS 2012 | G4.B |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts mêlant pins thermophiles méditerranéens et chênes caducifoliés thermophiles ou autres essences méridionales.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (4 taxons ; les 40 plus cités) : Castanea sativa, Carpinus orientalis, Quercus sp., Ostrya carpinifolia.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,3 | 4,7 | 9,4 | 21,1 | 32,8 | 44,5 | 68 | 75 | 2 512 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 41,6 | 63,4 | 65,6 | 2 264 |
| mauvais | 0 | 10,5 | 21 | 42 | 52,5 | 52,5 | 52,5 | 52,5 | 52,5 | 2 468 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H159. G4.C : Boisements mixtes à pin sylvestre et chênes thermophiles

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.C |
| EUNIS 2012 | G4.C |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 43.7 Chênaies mixtes thermophiles et supra-méditerranéennes |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts subméditerranéennes et supraméditerranéennes où les chênes caducifoliés thermophiles partagent la canopée avec le pin sylvestre, le pin noir ou d'autres pins thermophiles.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (7 taxons ; les 40 plus cités) : Ostrya carpinifolia, Pinus salzmannii, Pinus sylvestris, Carpinus sp., Pinus pallasiana, Pinus nigra, Quercus sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,3 | 4,7 | 9,4 | 21,1 | 32,8 | 44,5 | 68 | 75 | 2 512 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 41,6 | 63,4 | 65,6 | 2 264 |
| mauvais | 0 | 10,5 | 21 | 42 | 52,5 | 52,5 | 52,5 | 52,5 | 52,5 | 2 468 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H160. G4.D : Forêts mixtes de pin noir et de chênes sempervirents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.D |
| EUNIS 2012 | G4.D |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts mêlant chênes sempervirents et pin noir.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Pinus nigra.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,3 | 4,7 | 9,4 | 21,1 | 32,8 | 44,5 | 68 | 75 | 2 512 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 41,6 | 63,4 | 65,6 | 2 264 |
| mauvais | 0 | 10,5 | 21 | 42 | 52,5 | 52,5 | 52,5 | 52,5 | 52,5 | 2 468 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H161. G4.E : Forêts mixtes de pins méditerranéens et de chênes sempervirents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.E |
| EUNIS 2012 | G4.E |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Forêts mêlant chênes sempervirents et pins méditerranéens autres que le pin noir.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Pinus nigra.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », Biotoptypenwert 18 sur 24 (ligne 636 de l'extraction) |
| Valeur, stade jeune | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 43.08.05J, « – Junge Ausprägung », 15 sur 24 |
| Valeur, stade moyen | 0,75 m²HE/m² | 0,675 à 0,825 | code 43.08.05M, « – Mittlere Ausprägung », 18 sur 24 |
| Valeur, stade âgé | 0,875 m²HE/m² | 0,7875 à 0,9625 | code 43.08.05A, « – Alte Ausprägung », 21 sur 24 |

Correspondance retenue : Chênaie sèche, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,3 | 4,7 | 9,4 | 21,1 | 32,8 | 44,5 | 68 | 75 | 2 512 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 41,6 | 63,4 | 65,6 | 2 264 |
| mauvais | 0 | 10,5 | 21 | 42 | 52,5 | 52,5 | 52,5 | 52,5 | 52,5 | 2 468 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H162. G4.F : Plantations forestières mixtes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G4.F |
| EUNIS 2012 | G4.F |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations mixtes de conifères et de feuillus dont au moins une essence est exotique ou hors de son aire, ou plantations indigènes en peuplements nettement artificiels.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 44.04M, « – Mittlere Ausprägung », Biotoptypenwert 11 sur 24 (ligne 708 de l'extraction) |
| Valeur, stade jeune | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 44.04J, « – Junge Ausprägung », 9 sur 24 |
| Valeur, stade moyen | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 44.04M, « – Mittlere Ausprägung », 11 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.04A, « – Alte Ausprägung », 14 sur 24 |

Correspondance retenue : Plantation mixte d'essences indigènes, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 22,91 m²HE, 15 à 30 cm 27,5 m²HE, 30 à 80 cm 32,08 m²HE, 80 cm et plus 41,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,9 | 5,7 | 12,9 | 20,1 | 27,2 | 41,5 | 45,8 | 1 535 |
| moyen | 0 | 1,3 | 2,7 | 5,3 | 12 | 18,7 | 25,4 | 38,8 | 40,1 | 1 383 |
| mauvais | 0 | 6,4 | 12,8 | 25,7 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 1 508 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H163. G5.1 : Alignements d'arbres hors milieu urbain

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.1 |
| EUNIS 2012 | G5.1 |
| EUNIS 2022 (HabRef) | V6-3 Alignements d'arbres plantés |
| CORINE Biotopes (HabRef) | 84.1 Alignements d'arbres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | arbre (houppier projeté) |
| Grille d'état | EA1 (arbres) |

**Définition**

Lignes plus ou moins continues d'arbres pouvant dépasser 5 m de haut, au milieu de prairies, de cultures ou le long des routes, servant d'abri ou d'ombrage.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.05aM, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 474 de l'extraction) |
| Valeur, stade jeune | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 41.05aJ, « – Junge Ausprägung », 11 sur 24 |
| Valeur, stade moyen | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.05aM, « – Mittlere Ausprägung », 15 sur 24 |
| Valeur, stade âgé | 0,75 m²HE/m² | 0,675 à 0,825 | code 41.05aA, « – Alte Ausprägung », 18 sur 24 |

Correspondance retenue : Arbres isolés et alignements d'essences autochtones, stade moyen ; en ville, saisir VB.18a ou VB.18b.

**Grille d'état EA1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Essence indigène (ou au moins 70 % d'essences indigènes dans un groupe) | non |
| B | Couvert continu, trouées sur moins de 10 % et aucune de plus de 5 m (critère réputé satisfait pour un arbre isolé) | non |
| C | Arbre mûr (ou plus de 50 % d'arbres mûrs dans un groupe) | non |
| D | Pas d'atteinte humaine à la santé de l'arbre et pas de taille régulière : plus de 75 % du houppier naturel conservé | non |
| E | Microhabitats présents : bois mort, cavités, lierre, écorce décollée | non |
| F | Plus de 20 % du houppier au-dessus d'une végétation (et non d'un sol revêtu) | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible bon |
| Création, état moyen visé | 27 ans | onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 135, « Individual trees - Rural tree », condition cible mauvais |
| Amélioration, mauvais vers moyen | 16 ans | onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 16 ans | onglet G-5, ligne 136, « Individual trees - Rural tree », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 134, « Individual trees - Rural tree » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 134, « Individual trees - Rural tree » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2 | 3,9 | 7,8 | 17,6 | 27,3 | 37,1 | 56,6 | 62,5 | 2 094 |
| moyen | 0 | 2 | 4,1 | 8,1 | 18,2 | 28,4 | 38,5 | 54,7 | 54,7 | 1 969 |
| mauvais | 0 | 4,4 | 8,8 | 17,5 | 39,4 | 43,8 | 43,8 | 43,8 | 43,8 | 1 947 |

#### Fiche H164. G5.2 : Petits bois anthropiques de feuillus caducifoliés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.2 |
| EUNIS 2012 | G5.2 |
| EUNIS 2022 (HabRef) | V6-4 Petits bois plantés de feuillus caducifoliés |
| CORINE Biotopes (HabRef) | 84.3 Petits bois, bosquets, 85.11 Parcelles boisées de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations et petits bois de feuillus caducifoliés de moins d'environ 0,5 ha, gérés intensivement.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.02.02M, « – Mittlere Ausprägung », Biotoptypenwert 14 sur 24 (ligne 448 de l'extraction) |
| Valeur, stade jeune | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 41.02.02J, « – Junge Ausprägung », 13 sur 24 |
| Valeur, stade moyen | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.02.02M, « – Mittlere Ausprägung », 14 sur 24 |
| Valeur, stade âgé | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 41.02.02A, « – Alte Ausprägung », 17 sur 24 |

Correspondance retenue : Bosquet des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 58,33 |
| État moyen | 51,04 |
| Mauvais état | 40,83 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 29,17 m²HE, 15 à 30 cm 35 m²HE, 30 à 80 cm 40,83 m²HE, 80 cm et plus 52,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,8 | 3,6 | 7,3 | 16,4 | 25,5 | 34,6 | 52,9 | 58,3 | 1 954 |
| moyen | 0 | 3,4 | 6,8 | 13,6 | 30,6 | 47,6 | 51 | 51 | 51 | 2 144 |
| mauvais | 0 | 8,2 | 16,3 | 32,7 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 1 919 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H165. G5.3 : Petits bois anthropiques de feuillus sempervirents

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.3 |
| EUNIS 2012 | G5.3 |
| EUNIS 2022 (HabRef) | V6-5 Petits bois plantés de feuillus sempervirents |
| CORINE Biotopes (HabRef) | 84.3 Petits bois, bosquets, 85.11 Parcelles boisées de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations et petits bois de feuillus sempervirents de moins d'environ 0,5 ha, gérés intensivement.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.02.03M, « – Mittlere Ausprägung », Biotoptypenwert 15 sur 24 (ligne 452 de l'extraction) |
| Valeur, stade jeune | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.02.03J, « – Junge Ausprägung », 14 sur 24 |
| Valeur, stade moyen | 0,625 m²HE/m² | 0,5625 à 0,6875 | code 41.02.03M, « – Mittlere Ausprägung », 15 sur 24 |
| Valeur, stade âgé | 0,75 m²HE/m² | 0,675 à 0,825 | code 41.02.03A, « – Alte Ausprägung », 18 sur 24 |

Correspondance retenue : Bosquet des stations sèches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 62,5 |
| État moyen | 54,69 |
| Mauvais état | 43,75 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 31,25 m²HE, 15 à 30 cm 37,5 m²HE, 30 à 80 cm 43,75 m²HE, 80 cm et plus 56,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2 | 3,9 | 7,8 | 17,6 | 27,3 | 37,1 | 56,6 | 62,5 | 2 094 |
| moyen | 0 | 3,6 | 7,3 | 14,6 | 32,8 | 51 | 54,7 | 54,7 | 54,7 | 2 297 |
| mauvais | 0 | 8,8 | 17,5 | 35 | 43,8 | 43,8 | 43,8 | 43,8 | 43,8 | 2 056 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H166. G5.4 : Petits bois anthropiques de conifères

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.4 |
| EUNIS 2012 | G5.4 |
| EUNIS 2022 (HabRef) | V6-6 Petits bois plantés de conifères |
| CORINE Biotopes (HabRef) | 84.3 Petits bois, bosquets, 85.11 Parcelles boisées de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations et petits bois de conifères de moins d'environ 0,5 ha, gérés intensivement.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 44.04M, « – Mittlere Ausprägung », Biotoptypenwert 11 sur 24 (ligne 708 de l'extraction) |
| Valeur, stade jeune | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 44.04J, « – Junge Ausprägung », 9 sur 24 |
| Valeur, stade moyen | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 44.04M, « – Mittlere Ausprägung », 11 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 44.04A, « – Alte Ausprägung », 14 sur 24 |

Correspondance retenue : Plantation de résineux indigènes, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 94, « Woodland and forest - Other coniferous woodland », condition cible mauvais |
| Amélioration, mauvais vers moyen | 25 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 32 ans | onglet G-5, ligne 95, « Woodland and forest - Other coniferous woodland », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 115, « Woodland and forest - Other coniferous woodland » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 22,91 m²HE, 15 à 30 cm 27,5 m²HE, 30 à 80 cm 32,08 m²HE, 80 cm et plus 41,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,4 | 2,9 | 5,7 | 12,9 | 20,1 | 27,2 | 41,5 | 45,8 | 1 535 |
| moyen | 0 | 1,3 | 2,7 | 5,3 | 12 | 18,7 | 25,4 | 38,8 | 40,1 | 1 383 |
| mauvais | 0 | 6,4 | 12,8 | 25,7 | 32,1 | 32,1 | 32,1 | 32,1 | 32,1 | 1 508 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H167. G5.5 : Petits bois anthropiques mixtes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.5 |
| EUNIS 2012 | G5.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 84.3 Petits bois, bosquets, 85.11 Parcelles boisées de parcs |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Plantations et petits bois mixtes de moins d'environ 0,5 ha, à 25 à 75 % de conifères.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.02.02M, « – Mittlere Ausprägung », Biotoptypenwert 14 sur 24 (ligne 448 de l'extraction) |
| Valeur, stade jeune | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 41.02.02J, « – Junge Ausprägung », 13 sur 24 |
| Valeur, stade moyen | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 41.02.02M, « – Mittlere Ausprägung », 14 sur 24 |
| Valeur, stade âgé | 0,7083 m²HE/m² | 0,6375 à 0,7792 | code 41.02.02A, « – Alte Ausprägung », 17 sur 24 |

Correspondance retenue : Bosquet des stations fraîches, stade moyen.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible bon |
| Création, état moyen visé | 30 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 97, « Woodland and forest - Other woodland; mixed », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 98, « Woodland and forest - Other woodland; mixed », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 118, « Woodland and forest - Other woodland; mixed » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 58,33 |
| État moyen | 51,04 |
| Mauvais état | 40,83 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 29,17 m²HE, 15 à 30 cm 35 m²HE, 30 à 80 cm 40,83 m²HE, 80 cm et plus 52,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,8 | 3,6 | 7,3 | 16,4 | 25,5 | 34,6 | 52,9 | 58,3 | 1 954 |
| moyen | 0 | 1,7 | 3,4 | 6,8 | 15,3 | 23,8 | 32,3 | 49,3 | 51 | 1 761 |
| mauvais | 0 | 8,2 | 16,3 | 32,7 | 40,8 | 40,8 | 40,8 | 40,8 | 40,8 | 1 919 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H168. G5.6 : Stades initiaux et régénérations des forêts

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.6 |
| EUNIS 2012 | G5.6 |
| EUNIS 2022 (HabRef) | T4-1 Stades initiaux et régénérations des forêts naturelles et semi-naturelles |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.8D Recrûs forestiers caducifoliés, 31.8F Fourrés mixtes, 31.8G Prébois de résineux, 51.1 Tourbières hautes à peu près naturelles, 51.16 Pré-bois tourbeux |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Premiers stades de reconstitution ou de colonisation forestière, formés surtout de jeunes arbres d'essences de futaie de moins de 5 m, jeunes plantations indigènes comprises.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (5 taxons ; les 40 plus cités) : Betula carpatica, Betula pubescens, Picea abies, Pinus rotundata, Pinus sylvestris var. turfosa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 42.03.02, « Vorwald frischer Standorte », Biotoptypenwert 13 sur 24 (ligne 510 de l'extraction) |

Correspondance retenue : Pré-bois des stations fraîches.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 27,08 m²HE, 15 à 30 cm 32,5 m²HE, 30 à 80 cm 37,92 m²HE, 80 cm et plus 48,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,4 | 6,8 | 15,2 | 23,7 | 32,2 | 49,1 | 54,2 | 1 815 |
| moyen | 0 | 3,2 | 6,3 | 12,6 | 28,4 | 44,2 | 47,4 | 47,4 | 47,4 | 1 991 |
| mauvais | 0 | 7,6 | 15,2 | 30,3 | 37,9 | 37,9 | 37,9 | 37,9 | 37,9 | 1 782 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H169. G5.7 : Taillis et stades initiaux des plantations

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.7 |
| EUNIS 2012 | G5.7 |
| EUNIS 2022 (HabRef) | T4-2 Taillis et stades initiaux des plantations |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.8E Taillis |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Taillis simples, jeunes plantations de moins de 5 m, cultures d'arbres nains ou d'arbustes récoltés entiers (taillis à courte rotation, sapins de Noël, pépinières).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Salix sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 43.10J, « – Junge Ausprägung », Biotoptypenwert 9 sur 24 (ligne 643 de l'extraction) |
| Valeur, stade jeune | 0,375 m²HE/m² | 0,3375 à 0,4125 | code 43.10J, « – Junge Ausprägung », 9 sur 24 |
| Valeur, stade moyen | 0,5 m²HE/m² | 0,45 à 0,55 | code 43.10M, « – Mittlere Ausprägung », 12 sur 24 |
| Valeur, stade âgé | 0,5833 m²HE/m² | 0,525 à 0,6417 | code 43.10A, « – Alte Ausprägung », 14 sur 24 |

Correspondance retenue : Plantation de feuillus, stade jeune.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible bon |
| Création, état moyen visé | 15 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 96, « Woodland and forest - Other woodland; broadleaved », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 97, « Woodland and forest - Other woodland; broadleaved », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 117, « Woodland and forest - Other woodland; broadleaved » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 37,5 |
| État moyen | 32,81 |
| Mauvais état | 26,25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 18,75 m²HE, 15 à 30 cm 22,5 m²HE, 30 à 80 cm 26,25 m²HE, 80 cm et plus 33,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,2 | 2,3 | 4,7 | 10,5 | 16,4 | 22,3 | 34 | 37,5 | 1 256 |
| moyen | 0 | 2,2 | 4,4 | 8,8 | 19,7 | 30,6 | 32,8 | 32,8 | 32,8 | 1 378 |
| mauvais | 0 | 5,2 | 10,5 | 21 | 26,2 | 26,2 | 26,2 | 26,2 | 26,2 | 1 234 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H170. G5.8 : Coupes forestières récentes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | G5.8 |
| EUNIS 2012 | G5.8 |
| EUNIS 2022 (HabRef) | T4-3 Coupes forestières récentes |
| CORINE Biotopes (HabRef) | 31.8 Fourrés, 31.87 Clairières forestières, 31.871 Clairières herbacées forestières, 31.8711 Clairières à Epilobes et Digitales, 31.8712 Clairières à Bardane et Belladonne, 31.872 Clairières à couvert arbustif |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Terrains récemment déboisés par coupe rase ou incendie, avec leur végétation de recolonisation tant qu'elle n'est pas dominée par un couvert arboré.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (18 taxons ; les 40 plus cités) : Sambucus nigra, Sambucus racemosa, Sorbus aucuparia, Rubus sp., Salix caprea, Calamagrostis epigejos, Digitalis grandiflora, Digitalis purpurea, Senecio sylvaticus, Epilobium angustifolium, Carex pilulifera, Arctium nemorosum, Atropa bella-donna, Bromus ramosus, Digitalis lutea, Fragaria vesca, Hypericum hirsutum, Stachys alpina.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 39.02, « Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) », Biotoptypenwert 10 sur 24 (ligne 401 de l'extraction) |

Correspondance retenue : Coupes et végétation des clairières.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 90, « Woodland and forest - Felled », condition cible bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 111, « Woodland and forest - Felled » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 111, « Woodland and forest - Felled » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,4 | 0,9 | 1,7 | 3,9 | 6 | 8,2 | 12,5 | 13,8 | 461 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.7 Habitats continentaux sans végétation ou à végétation clairsemée (EUNIS H)

#### Fiche H171. H2.3 : Éboulis siliceux des montagnes tempérées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H2.3 |
| EUNIS 2012 | H2.3 |
| EUNIS 2022 (HabRef) | U2-2 Éboulis siliceux des hautes montagnes tempérées |
| CORINE Biotopes (HabRef) | 61.1 Eboulis siliceux alpins et nordiques, 61.11 Eboulis siliceux alpins, 61.111 Eboulis à Oxyria digyna, 61.1111 Eboulis à Oxyria digyna des Alpes, 61.1112 Eboulis du sud-ouest des Alpes à Oxyria digyna, 61.1113 Eboulis pyrénéens à Oxyria, 61.112 Eboulis à Androsace alpina, 61.113 Eboulis à Luzule alpine, 61.114 Eboulis siliceux et froids de blocailles, 61.12 Eboulis siliceux des montagnes nordiques |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Éboulis siliceux d'altitude et des stations fraîches des montagnes tempérées.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (58 taxons ; les 40 plus cités) : Oxyria digyna, Luzula alpinopilosa, Cryptogramma crispa, Androsace alpina, Luzula spadicea, Festuca picta, Geum reptans, Saxifraga adscendens, Saxifraga bryoides, Androsace wulfeniana, Viola valderia, Thlaspi limosellifolium, Festuca picturata, Festuca violacea ssp. picta, Armeria alpina, Bellardiochloa violacea, Pedicularis verticillata, Satureja alpina, Luzula spicata, Poa cenisia ssp. contracta, Acetosella vulgaris, Epilobium collinum, Galeopsis segetum, Petasites albus, Senecio viscosus, Tussilago farfara, Anarrhinum bellidifolium, Dalanum ladanum, Pleuropteropyrum undulatum, Poa cenisia, Polygonum alpinum, Saxifraga oppositifolia, Senecio rupestris, Vaccinium sp., Androsace hedraeantha, Lerchenfeldia flexuosa, Athyrium distentifolium, Cystopteris fragilis, Dryopteris disjuncta, Gymnocarpium dryopteris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |

Correspondance retenue : Éboulis naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H172. H2.4 : Éboulis calcaires des montagnes tempérées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H2.4 |
| EUNIS 2012 | H2.4 |
| EUNIS 2022 (HabRef) | U2-6 Éboulis et moraines riches en bases des hautes montagnes des zones tempérées |
| CORINE Biotopes (HabRef) | 61.2 Eboulis calcaires alpiens, 61.21 Eboulis alpiens sur calcschistes, 61.22 Eboulis alpiens à Tabouret à feuilles rondes, 61.23 Eboulis calcaires fins, 61.231 Eboulis à Petasites, 61.232 Eboulis à Liondent des montagnes, 61.2321 Eboulis à Liondent des montagnes des Alpes centrales, 61.2322 Eboulis à Berardia |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Éboulis calcaires et calcschisteux d'altitude et des stations fraîches des montagnes tempérées, instables, à végétation clairsemée.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (21 taxons ; les 40 plus cités) : Arabis alpina, Linaria alpina, Papaver rhaeticum, Thlaspi rotundifolium, Viola cenisia, Papaver sendtneri, Sideritis scardica, Morina persica, Gypsophila repens, Petasites paradoxus, Valeriana montana, Cystopteris montana, Hutchinsia alpina, Sedum atratum, Cerastium latifolium, Cerastium tatrae, Campanula cenisia, Draba hoppeana, Herniaria alpina, Saxifraga biflora, Trisetum spicatum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |

Correspondance retenue : Éboulis naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H173. H2.5 : Éboulis siliceux des expositions chaudes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H2.5 |
| EUNIS 2012 | H2.5 |
| EUNIS 2022 (HabRef) | U2-3 Éboulis siliceux planitiaires à montagnards des zones tempérées, U2-4 Éboulis siliceux méditerranéens |
| CORINE Biotopes (HabRef) | 61.3 Eboulis ouest-méditerranéens et éboulis thermophiles, 61.33 Eboulis pyrénéo-alpiens siliceux thermophiles |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Éboulis siliceux des expositions chaudes des montagnes, des collines et des plaines méditerranéennes, et localement des stations chaudes de moyenne Europe.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (32 taxons ; les 40 plus cités) : Crepis oporinoides, Holcus caespitosus, Rumex suffruticosus, Galeopsis pyrenaica, Senecio leucophyllus, Taraxacum pyrenaicum, Xatardia scabra, Armeria alpina, Erigeron frigidus, Papaver suaveolens, Ranunculus glacialis, Saxifraga oppositifolia, Linaria glacialis, Rhynchosinapis cheiranthos ssp. nevadensis, Ranunculus parnassifolius, Viola crassiuscula, Linaria alpina, Conopodium bunioides, Digitalis purpurea var. carpetana, Reseda gredensis, Santolina oblongifolia, Senecio pyrenaicus ssp. carpetanus, Linaria saxatilis, Digitalis purpurea var. nevadensis, Eryngium glaciale, Senecio tournefortii var. granatensis, Solidago virgaurea ssp. alpestris, Cirsium gregarium, Linaria aeruginea var. nevadensis, Trisetum hispidum, Achnatherum calamagrostis, Melica ciliata.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |

Correspondance retenue : Éboulis naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H174. H2.6 : Éboulis calcaires des expositions chaudes

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H2.6 |
| EUNIS 2012 | H2.6 |
| EUNIS 2022 (HabRef) | U2-7 Éboulis riches en bases planitiaires à montagnards des zones tempérées, U2-8 Éboulis riches en bases de la Méditerranée occidentale, U2-9 Eastern Mediterranean base-rich scree, U2-A Crimean base-rich screes |
| CORINE Biotopes (HabRef) | 61.3 Eboulis ouest-méditerranéens et éboulis thermophiles, 61.31 Eboulis thermophiles péri-alpins, 61.311 Eboulis à Stipa calamagrostis, 61.312 Eboulis calcaires sub-montagnards, 61.3121 Eboulis à Galeopsis angustifolia, 61.3122 Eboulis à Rumex scutatus, 61.3123 Eboulis calcaires à Fougères, 61.313 Eboulis à Leontodon hyoseroides, 61.32 Eboulis provençaux, 61.34 Eboulis calcaires pyrénéens, et 7 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Éboulis calcaires et calcschisteux des expositions chaudes des montagnes, des collines et des plaines méditerranéennes, et localement des stations chaudes de moyenne Europe.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (87 taxons ; les 40 plus cités) : Achnatherum calamagrostis, Corydalis ochroleuca, Vincetoxicum hirundinaria, Galeopsis angustifolia, Linaria supina, Rumex scutatus, Hieracium bifidum, Geranium robertianum, Peltaria alliacea, Teucrium chamaedrys, Dianthus petraeus, Drypis spinosa ssp. jacquiniana, Malcolmia serbica, Galium corrudifolium, Anthericum ramosum, Brachypodium pinnatum, Campanula rapunculoides, Galium album, Knautia dipsacifolia, Origanum vulgare, Calamagrostis varia, Knautia sylvatica, Aethionema saxatile, Mercurialis annua, Theligonum cynocrambe, Thlaspi perfoliatum, Centranthus calcitrapa, Drypis spinosa, Geranium robertianum ssp. purpureum, Ranunculus brevifolius, Senecio thapsoides, Cardamine carnosa, Drypis spinosa ssp. linnaena, Parietaria officinalis, Galium album ssp. album, Lamium garganicum ssp. laevigatum, Leontodon hyoseroides, Sisymbrium supinum, Viola hispida, Galium timeroyi ssp. fleurotii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.03a.01, « Natürliche Block- und Schutthalden », Biotoptypenwert 20 sur 24 (ligne 269 de l'extraction) |

Correspondance retenue : Éboulis naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H175. H3.1 : Falaises continentales siliceuses

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H3.1 |
| EUNIS 2012 | H3.1 |
| EUNIS 2022 (HabRef) | U3-1 Boreal and arctic siliceous inland cliff, U3-2 Falaises continentales siliceuses des hautes montagnes des zones tempérées, U3-3 Falaises continentales siliceuses planitiaires à montagnardes des zones tempérées, U3-4 Falaises continentales siliceuses méditerranéennes |
| CORINE Biotopes (HabRef) | 62.2 Végétation des falaises continentales siliceuses, 62.21 Falaises siliceuses des montagnes médio-européennes, 62.211 Falaises siliceuses pyrénéo-alpiennes, 62.212 Falaises siliceuses hercyniennes, 62.213 Falaises de serpentines hercyniennes, 62.23 Falaises siliceuses des Alpes sud-occidentales, 62.24 Falaises des montagnes cyrno-sardes, 62.26 Falaises siliceuses catalano-languedociennes, 62.28 Falaises siliceuses provenço-ibériques, 62.4 Falaises continentales dénudées, et 3 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Falaises continentales sèches non calcaires, colonisées par des associations végétales spécialisées en montagne et en région méditerranéenne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (83 taxons ; les 40 plus cités) : Hieracium pallidum ssp. graniticum, Murbeckiella boryi ssp. boryi, Murbeckiella boryi ssp. herminii, Saxifraga willkommiana, Spergula viscosa ssp. pourretii, Cheilanthes hispanica, Cheilanthes tinaei, Saxifraga pedemontana, Aquilegia bernardii, Armeria leucocephala, Asplenium viride, Draba loiseleurii, Festuca sardoa, Leucanthemum corsicum, Phyteuma serratum, Potentilla crassinervia, Scabiosa corsica, Silene requienii, Amelanchier ovalis ssp. rhamnoides, Helechryssum frigidum, Erigeron paolii, Draba dubia, Saxifraga pedemontana ssp. cervicornis, Sedum brevifolium, Centranthus nevadensis, Saxifraga nevadensis, Asplenium adiantum-nigrum, Asplenium billotii, Asplenium foreziense, Asplenium septentrionale, Biscutella laevigata, Saxifraga sponhemica, Cornicularia sp., Ramalina sp., Rhizocarpon sp., Rhizoplaca sp., Umbilicaria sp., Dianthus sylvestris ssp. siculus, Asplenium sp., Cheilanthes sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |

Correspondance retenue : Rochers naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H176. H3.2 : Falaises continentales basiques

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H3.2 |
| EUNIS 2012 | H3.2 |
| EUNIS 2022 (HabRef) | U3-5 Boreal and arctic base-rich inland cliff, U3-6 Falaises continentales riches en bases des hautes montagnes des zones tempérées, U3-7 Falaises continentales riches en bases, planitiaires à montagnardes des zones tempérées, U3-8 Falaises continentales méditerranéennes riches en bases, U3-9 Boreal ultramafic inland cliff, U3-A Falaises continentales ultramafiques tempérées, U3-B Falaises continentales ultramafiques méditerranéennes |
| CORINE Biotopes (HabRef) | 62.1 Végétation des falaises continentales calcaires, 62.11 Falaises calcaires eu-méditerranéennes occidentales et oro-ibériques, 62.111 Falaises calcaires eu-méditerranéennes occidentales, 62.1111 Falaises calcaires ibéro-méditerranéennes, 62.1115 Falaises méditerranéennes à Fougères, 62.12 Falaises calcaires des Pyrénées centrales, 62.13 Falaises calcaires des Alpes ligures et des Apennins, 62.15 Falaises calcaires alpiennes et sub-méditerranéennes, 62.151 Falaises calcaires ensoleillées des Alpes, 62.152 Falaises calcaires médio-européennes à Fougères, et 4 autres |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Falaises continentales sèches calcaires, colonisées par des associations végétales spécialisées en montagne et en région méditerranéenne.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (241 taxons ; les 40 plus cités) : Teucrium flavum, Asplenium trichomanes, Campanula pyramidalis, Sesleria juncifolia, Asplenium viride, Sesleria rigida, Amaracus tournefortii, Inula candida, Potentilla caulescens, Inula heterolepis, Silene fruticosa, Euphorbia wulfenii, Micromeria thymifolia, Saxifraga aretioides, Asperula hirta, Satureja parnassica, Asplenium ruta-muraria, Cystopteris fragilis, Carex brachystachys, Cheiranthus cheiri, Centaurea kartschiana, Moehringia tommasinii, Ceterach officinarum, Campanula lanata, Campanula orphanidea, Morina persica, Petkovia orphanidea, Saxifraga stribrnyi, Scabiosa rhodopensis, Seseli rhodopeum, Sideritis scardica, Trachelium jacquinii ssp. rumelianum, Trachelium rumelianum, Haberlea rhodopensis, Putoria calabrica, Kernera saxatilis, Convolvulus boissieri, Pinus heldreichii, Aster alpinus var. dolomiticus, Brassica jordanoffii.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |

Correspondance retenue : Rochers naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H177. H3.4 : Falaises continentales humides

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H3.4 |
| EUNIS 2012 | H3.4 |
| EUNIS 2022 (HabRef) | U3-D Falaises continentales humides |
| CORINE Biotopes (HabRef) | 62.5 Falaises continentales humides, 62.51 Falaises continentales humides méditerranéennes, 62.52 Falaises continentales humides septentrionales |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Rochers très humides, ruisselants, verticaux ou en surplomb, des collines, des montagnes et des plaines méditerranéennes.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (18 taxons ; les 40 plus cités) : Adiantum capillus-veneris, Eucladium verticillatum, Cratoneuron commutatum, Blackstonia perfoliata, Borago pygmaea, Carex distans, Dittrichia viscosa, Ficus carica, Hypericum hircinum, Samolus valerandi, Pinguicula hirtiflora, Pinguicula grandiflora ssp. coenocantabrica, Alchemilla glabra, Aurinia saxatilis, Phegopteris connectilis, Saxifraga paniculata, Viola palustris, Dianthus nitidus.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |

Correspondance retenue : Rochers naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H178. H3.5 : Pavements rocheux, dont pavements calcaires

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H3.5 |
| EUNIS 2012 | H3.5 |
| EUNIS 2022 (HabRef) | U3-E Pavements calcaires |
| CORINE Biotopes (HabRef) | 62.3 Dalles rocheuses |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Surfaces rocheuses plus ou moins planes mises à nu par l'érosion, nues ou colonisées par des mousses, des algues ou des lichens, lapiaz compris, avec des plantes vasculaires dans les fissures.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |

Correspondance retenue : Rochers naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible bon |
| Création, état moyen visé | 32 ans | onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible moyen |
| Création, mauvais état visé | 32 ans | onglet G-4, ligne 56, « Sparsely vegetated land - Limestone pavement », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 57, « Sparsely vegetated land - Limestone pavement », amélioration moyen vers bon |
| Difficulté de création | 0,1 | onglet G-3, ligne 76, « Sparsely vegetated land - Limestone pavement » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 76, « Sparsely vegetated land - Limestone pavement » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,3 | 0,5 | 1 | 2,3 | 3,6 | 4,9 | 7,6 | 8,3 | 279 |
| moyen | 0 | 0,2 | 0,5 | 0,9 | 2,1 | 3,2 | 4,3 | 6,6 | 7,3 | 244 |
| mauvais | 0 | 0,2 | 0,4 | 0,7 | 1,6 | 2,6 | 3,5 | 5,3 | 5,8 | 195 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H179. H3.6 : Affleurements et rochers érodés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H3.6 |
| EUNIS 2012 | H3.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 36.2 Communautés des affleurements et rochers désagrégés alpins |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Rochers et affleurements siliceux colonisés par des communautés pionnières de joubarbes et d'orpins, avec lichens et mousses, aux étages montagnard et alpin.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (24 taxons ; les 40 plus cités) : Scleranthus polycarpos, Thymus praecox ssp. polytrichus, Viola tricolor ssp. saxatilis, Crassulaceae sp., Veronica fruticans, Silene rupestris, Polytrichum piliferum, Racomitrium canescens, Erophila verna, Jovibarba sp., Sempervivum sp., Sedum sp., Saxifraga aspera, Sedum album, Sedum annuum, Sedum montanum, Sedum sexangulare, Sempervivum wulfenii, Sedum anglicum ssp. pyrenaicum, Sempervivum arachnoideum ssp. tomentosum, Sempervivum montanum ssp. stiriacum, Sempervivum arachnoideum ssp. arachnoideum, Jovibarba arenaria, Sempervivum montanum ssp. montanum.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,8333 m²HE/m² | 0,75 à 0,9167 | code 32.01a, « Natürliche Felsen », Biotoptypenwert 20 sur 24 (ligne 264 de l'extraction) |

Correspondance retenue : Rochers naturels.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible bon |
| Création, état moyen visé | 20 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible moyen |
| Création, mauvais état visé | 10 ans | onglet G-4, ligne 55, « Sparsely vegetated land - Inland rock outcrop and scree habitats », condition cible mauvais |
| Amélioration, mauvais vers moyen | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 32 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 20 ans | onglet G-5, ligne 56, « Sparsely vegetated land - Inland rock outcrop and scree habitats », amélioration moyen vers bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 75, « Sparsely vegetated land - Inland rock outcrop and scree habitats » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 83,33 |
| État moyen | 72,91 |
| Mauvais état | 58,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 41,66 m²HE, 15 à 30 cm 50 m²HE, 30 à 80 cm 58,33 m²HE, 80 cm et plus 75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,9 | 1,7 | 3,4 | 7,7 | 12 | 16,3 | 24,9 | 27,5 | 921 |
| moyen | 0 | 1,2 | 2,4 | 4,8 | 10,8 | 16,8 | 22,9 | 24,1 | 24,1 | 950 |
| mauvais | 0 | 1,9 | 3,8 | 7,7 | 17,3 | 19,2 | 19,2 | 19,2 | 19,2 | 857 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H180. H5.2 : Moraines glaciaires peu végétalisées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H5.2 |
| EUNIS 2012 | H5.2 |
| EUNIS 2022 (HabRef) | U5-3 Moraines glaciaires avec peu ou pas de végétation |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Moraines glaciaires libérées de leur glace et pas encore revégétalisées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5 m²HE/m² | 0,45 à 0,55 | code 63.04, « Silikatschutthalde der subalpinen bis alpinen Stufe », Biotoptypenwert 12 sur 24 (ligne 841 de l'extraction) |

Correspondance retenue : Éboulis siliceux subalpins à alpins.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 50 |
| État moyen | 43,75 |
| Mauvais état | 35 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 25 m²HE, 15 à 30 cm 30 m²HE, 30 à 80 cm 35 m²HE, 80 cm et plus 45 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 1,7 | 3,4 | 6,7 | 15,1 | 23,4 | 31,8 | 33,5 | 33,5 | 1 323 |
| moyen | 0 | 2,9 | 5,9 | 11,7 | 26,4 | 29,3 | 29,3 | 29,3 | 29,3 | 1 304 |
| mauvais | 0 | 4,7 | 9,4 | 18,8 | 23,5 | 23,5 | 23,5 | 23,5 | 23,5 | 1 102 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H181. H5.3 : Substrats minéraux nus ou clairsemés d'origine naturelle

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H5.3 |
| EUNIS 2012 | H5.3 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | 61 Eboulis, 64 Dunes sableuses continentales, 64.5 Dunes d'origine lacustre |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Accumulations de sable, de blocs, de pierres, de galets ou de graviers d'origine naturelle, nues, couvertes de lichens ou de mousses ou colonisées par des herbes et arbustes épars (dunes continentales, moraines, chaos de blocs). Un sol nu de chantier relève de VB.10.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (6 taxons ; les 40 plus cités) : Equisetum boreale, Leymus arenarius, Armeria maritima, Festuca cryophila, Silene maritima, Silene uniflora.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,75 m²HE/m² | 0,675 à 0,825 | code 32.09, « Vegetationslose bzw. -arme Sandfläche », Biotoptypenwert 18 sur 24 (ligne 274 de l'extraction) |

Correspondance retenue : Surface sableuse sans ou presque sans végétation ; un sol nu de chantier est saisi en VB.10.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 20 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible bon |
| Création, état moyen visé | 10 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible moyen |
| Création, mauvais état visé | 5 ans | onglet G-4, ligne 58, « Sparsely vegetated land - Other inland rock and scree », condition cible mauvais |
| Amélioration, mauvais vers moyen | 10 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 20 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 10 ans | onglet G-5, ligne 59, « Sparsely vegetated land - Other inland rock and scree », amélioration moyen vers bon |
| Difficulté de création | 0,67 | onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 78, « Sparsely vegetated land - Other inland rock and scree » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 75 |
| État moyen | 65,62 |
| Mauvais état | 52,5 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 37,5 m²HE, 15 à 30 cm 45 m²HE, 30 à 80 cm 52,5 m²HE, 80 cm et plus 67,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,67 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 2,5 | 5 | 10,1 | 22,6 | 35,2 | 47,7 | 50,2 | 50,2 | 1 985 |
| moyen | 0 | 4,4 | 8,8 | 17,6 | 39,6 | 44 | 44 | 44 | 44 | 1 957 |
| mauvais | 0 | 7 | 14,1 | 28,1 | 35,2 | 35,2 | 35,2 | 35,2 | 35,2 | 1 653 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H182. H5.4 : Substrats organiques secs peu végétalisés

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H5.4 |
| EUNIS 2012 | H5.4 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Humus brut non végétalisé, non issu d'un incendie.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2083 m²HE/m² | 0,1875 à 0,2292 | code 36.04.04, « Torfhalden », Biotoptypenwert 5 sur 24 (ligne 383 de l'extraction) |

Correspondance retenue : Dépôts de tourbe.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 20,83 |
| État moyen | 18,23 |
| Mauvais état | 14,58 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 10,42 m²HE, 15 à 30 cm 12,5 m²HE, 30 à 80 cm 14,58 m²HE, 80 cm et plus 18,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 4,2 | 8,3 | 16,7 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 979 |
| moyen | 0 | 6,1 | 12,2 | 18,2 | 18,2 | 18,2 | 18,2 | 18,2 | 18,2 | 875 |
| mauvais | 0 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 14,6 | 714 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H183. H5.5 : Zones incendiées peu végétalisées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H5.5 |
| EUNIS 2012 | H5.5 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EB1 (boisements) |

**Définition**

Sol brûlé encore dépourvu de plantes vasculaires. Les bois récemment brûlés relèvent de G5.8.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 39.02, « Kahlschläge und Fluren der Lichtungen (mit überwiegend krautiger Vegetation) », Biotoptypenwert 10 sur 24 (ligne 401 de l'extraction) |

Correspondance retenue : Coupes et végétation des clairières.

**Grille d'état EB1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| age peuplement | Répartition des âges des arbres, chaque indicateur est noté de 1 à 3 selon les seuils de la fiche | non |
| degats herbivores | Dégâts d'herbivores sauvages ou domestiques | non |
| especes envahissantes | Espèces végétales envahissantes | non |
| nombre essences indigenes | Nombre d'essences d'arbres indigènes | non |
| couvert indigene | Couvert des arbres et arbustes indigènes | non |
| espaces ouverts | Espaces ouverts dans le boisement | non |
| regeneration | Régénération du boisement | non |
| sante arbres | Santé des arbres | non |
| flore sol | Végétation et flore du sol | non |
| structure verticale | Structure verticale | non |
| arbres veterans | Arbres vétérans | non |
| bois mort | Quantité de bois mort | non |
| perturbations | Perturbations du boisement | non |
| seuil bon | Score total minimal du bon état | non |
| seuil moyen | Score total minimal de l'état moyen | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 32 ans | onglet G-4, ligne 90, « Woodland and forest - Felled », condition cible bon |
| Difficulté de création | 0,33 | onglet G-3, ligne 111, « Woodland and forest - Felled » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 111, « Woodland and forest - Felled » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 0,33 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 0,4 | 0,9 | 1,7 | 3,9 | 6 | 8,2 | 12,5 | 13,8 | 461 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H184. H5.6 : Zones piétinées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | H5.6 |
| EUNIS 2012 | H5.6 |
| EUNIS 2022 (HabRef) | aucune correspondance |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Sol nu résultant du piétinement par l'homme ou les animaux.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4167 m²HE/m² | 0,375 à 0,4583 | code 52.02.06, « Unbefestigter Weg », Biotoptypenwert 10 sur 24 (ligne 759 de l'extraction) |

Correspondance retenue : Chemin non stabilisé.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Difficulté de création | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 84, « Urban - Artificial unvegetated, unsealed surface » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 41,67 |
| État moyen | 36,46 |
| Mauvais état | 29,17 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 20,84 m²HE, 15 à 30 cm 25 m²HE, 30 à 80 cm 29,17 m²HE, 80 cm et plus 37,5 m²HE.

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

### 4.8 Habitats agricoles, horticoles et domestiques régulièrement cultivés (EUNIS I)

#### Fiche H185. I1.1 : Monocultures intensives

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I1.1 |
| EUNIS 2012 | I1.1 |
| EUNIS 2022 (HabRef) | V1-1 Monocultures intensives |
| CORINE Biotopes (HabRef) | 82.11 Grandes cultures |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Céréales et autres cultures sur de grandes surfaces continues de paysages d'openfield.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,25 m²HE/m² | 0,225 à 0,275 | code 33.04a.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) », Biotoptypenwert 6 sur 24 (ligne 305 de l'extraction) |

Correspondance retenue : Culture sur sol limoneux ou argileux à flore adventice appauvrie.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 8, « Cropland - Cereal crops », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 9, « Cropland - Cereal crops » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 9, « Cropland - Cereal crops » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 12,5 m²HE, 15 à 30 cm 15 m²HE, 30 à 80 cm 17,5 m²HE, 80 cm et plus 22,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 1 225 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H186. I1.2 : Cultures maraîchères et horticulture

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I1.2 |
| EUNIS 2012 | I1.2 |
| EUNIS 2022 (HabRef) | V1-2 Cultures mixtes des jardins maraîchers et horticulture |
| CORINE Biotopes (HabRef) | 82.12 Cultures et maraichage |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Cultures intensives de légumes, de fleurs ou de petits fruits, souvent en bandes alternées, jardins ouvriers et maraîchage compris.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,25 m²HE/m² | 0,225 à 0,275 | code 33.04a.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Lehm- oder Tonboden) », Biotoptypenwert 6 sur 24 (ligne 305 de l'extraction) |

Correspondance retenue : Culture sur sol limoneux ou argileux à flore adventice appauvrie.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 10, « Cropland - Horticulture », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 11, « Cropland - Horticulture » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 25 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 12,5 m²HE, 15 à 30 cm 15 m²HE, 30 à 80 cm 17,5 m²HE, 80 cm et plus 22,5 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 1 225 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H187. I1.3 : Terres arables à monocultures extensives

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I1.3 |
| EUNIS 2012 | I1.3 |
| EUNIS 2022 (HabRef) | V1-3 Terres arables à monocultures extensives |
| CORINE Biotopes (HabRef) | 82.3 Culture extensive |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Cultures, surtout céréalières, conduites de façon traditionnelle et extensive, abritant une flore messicole riche et menacée (nielle, bleuet, miroir de Vénus, adonis, pieds-d'alouette, coquelicots).

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (9 taxons ; les 40 plus cités) : Agrostemma githago, Calendula arvensis, Centaurea cyanus, Chrysanthemum segetum, Legousia speculum-veneris, Adonis sp., Consolida sp., Nigella sp., Papaver sp..

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,6667 m²HE/m² | 0,6 à 0,7333 | code 33.04a.02, « – Acker mit artenreicher Segetalvegetaion (Lehm- oder Tonboden) », Biotoptypenwert 16 sur 24 (ligne 304 de l'extraction) |

Correspondance retenue : Culture sur sol limoneux ou argileux à flore adventice riche.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 4, « Cropland - Arable field margins cultivated annually », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 5, « Cropland - Arable field margins cultivated annually » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 5, « Cropland - Arable field margins cultivated annually » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 66,67 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 33,34 m²HE, 15 à 30 cm 40 m²HE, 30 à 80 cm 46,67 m²HE, 80 cm et plus 60 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 66,7 | 66,7 | 66,7 | 66,7 | 66,7 | 66,7 | 66,7 | 66,7 | 3 267 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H188. I1.4 : Cultures inondées ou inondables

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I1.4 |
| EUNIS 2012 | I1.4 |
| EUNIS 2022 (HabRef) | V1-4 Cultures inondées ou inondables, y compris les rizières |
| CORINE Biotopes (HabRef) | 82.41 Rizières |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | aucune (f = 1) |

**Définition**

Champs inondés ou inondables cultivés en riz, qui peuvent servir d'habitat de substitution à des oiseaux d'eau quand ils sont peu traités.

**Espèces caractéristiques**

Espèces que HabRef donne comme caractéristiques, diagnostiques, dominantes ou indicatrices du type et de ses subdivisions (1 taxons ; les 40 plus cités) : Oryza sativa.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,2083 m²HE/m² | 0,1875 à 0,2292 | code 33.05.03, « – Acker mit stark verarmter oder fehlender Segetalvegetation (Torf- oder Anmoorboden) », Biotoptypenwert 5 sur 24 (ligne 313 de l'extraction) |

Correspondance retenue : Culture sur sol tourbeux à flore adventice appauvrie.

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 12, « Cropland - Non-cereal crops », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Difficulté de création | 1 | onglet G-3, ligne 13, « Cropland - Non-cereal crops » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 13, « Cropland - Non-cereal crops » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Sans grille (f = 1) | 20,83 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 10,42 m²HE, 15 à 30 cm 12,5 m²HE, 30 à 80 cm 14,58 m²HE, 80 cm et plus 18,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 20,8 | 1 021 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H189. I1.5 : Friches, jachères et terres arables récemment abandonnées

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I1.5 |
| EUNIS 2012 | I1.5 |
| EUNIS 2022 (HabRef) | V1-5 Friches, jachères ou terres arables récemment abandonnées |
| CORINE Biotopes (HabRef) | 87 Terrains en friche et terrains vagues, 87.1 Terrains en friche |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | ER1 (milieux peu végétalisés) |

**Définition**

Champs abandonnés ou en repos et autres espaces interstitiels sur sol remanié, colonisés par des plantes pionnières, introduites ou nitrophiles.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,3333 m²HE/m² | 0,3 à 0,3667 | code 33.04a.04, « – Ackerbrache (Lehm- oder Tonboden) », Biotoptypenwert 8 sur 24 (ligne 306 de l'extraction) |

Correspondance retenue : Jachère sur sol limoneux ou argileux.

**Grille d'état ER1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Milieu représentatif de son type, espèces indicatrices régulièrement présentes | non |
| B | Fougère aigle, fourrés et arbres sur moins de 25 % | non |
| C | Absence d'espèces exotiques envahissantes et espèces d'un état dégradé sur moins de 5 % de la surface végétalisée | non |
| D | Recouvrement végétal entre 5 % et 50 % | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, bon état visé | 5 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible bon |
| Création, état moyen visé | 3 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible moyen |
| Création, mauvais état visé | 1 ans | onglet G-4, ligne 53, « Sparsely vegetated land - Ruderal/Ephemeral », condition cible mauvais |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 54, « Sparsely vegetated land - Ruderal/Ephemeral », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |
| Difficulté d'amélioration | 0,67 | onglet G-3, ligne 79, « Sparsely vegetated land - Ruderal/Ephemeral » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 33,33 |
| État moyen | 29,16 |
| Mauvais état | 23,33 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 16,66 m²HE, 15 à 30 cm 20 m²HE, 30 à 80 cm 23,33 m²HE, 80 cm et plus 30 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| bon | 0 | 6,7 | 13,3 | 26,7 | 33,3 | 33,3 | 33,3 | 33,3 | 33,3 | 1 567 |
| moyen | 0 | 9,7 | 19,4 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 29,2 | 1 400 |
| mauvais | 0 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 23,3 | 1 143 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H190. I2.1 : Grands jardins ornementaux et parcs

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I2.1 |
| EUNIS 2012 | I2.1 |
| EUNIS 2022 (HabRef) | V2-1 Grands jardins ornementaux |
| CORINE Biotopes (HabRef) | 85.1 Grands parcs, 85.14 Parterre de fleurs, avec arbres et avec bosquets en parc |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Grands jardins et parcs d'agrément, à végétation souvent introduite ou horticole mais pouvant compter de nombreuses espèces indigènes et une faune variée quand l'entretien est extensif.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,5417 m²HE/m² | 0,4875 à 0,5958 | code 51.06a.03, « Intensiv gepflegte Parkanlage mit altem Baumbestand », Biotoptypenwert 13 sur 24 (ligne 725 de l'extraction) |

Correspondance retenue : Parc entretenu intensivement avec arbres anciens.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 54,17 |
| État moyen | 47,4 |
| Mauvais état | 37,92 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 27,08 m²HE, 15 à 30 cm 32,5 m²HE, 30 à 80 cm 37,92 m²HE, 80 cm et plus 48,75 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 54,2 | 54,2 | 54,2 | 54,2 | 54,2 | 54,2 | 54,2 | 54,2 | 2 654 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).

#### Fiche H191. I2.3 : Zones de jardins abandonnées récemment

**Identification**

| Élément | Valeur |
|---|---|
| Code OpenNAT | I2.3 |
| EUNIS 2012 | I2.3 |
| EUNIS 2022 (HabRef) | V2-3 Jardins abandonnés récemment |
| CORINE Biotopes (HabRef) | aucune correspondance |
| Habitats d'intérêt communautaire (HabRef) | aucun |
| Position de saisie | au sol |
| Grille d'état | EU1 (milieux urbains) |

**Définition**

Massifs et potagers de jardins abandonnés, rapidement colonisés par des plantes spontanées.

**Valeur intrinsèque (module H, équation H1)**

| Paramètre | Valeur | Plage | Source |
|---|---|---|---|
| Valeur intrinsèque | 0,4583 m²HE/m² | 0,4125 à 0,5042 | code 51.08a.01, « Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich », Biotoptypenwert 11 sur 24 (ligne 733 de l'extraction) |

Correspondance retenue : Jardins riches en structures.

**Grille d'état EU1 (module H, équations H2 et H3)**

| Critère | Libellé | Essentiel |
|---|---|---|
| A | Structure de végétation variée : aucune strate ni aucun type de végétation ne dépasse 80 % de la surface | non |
| B | Espèces favorables à la faune, notamment des plantes à fleurs nectarifères étalées sur l'année | non |
| C | Espèces exotiques envahissantes sur moins de 5 % de la surface végétalisée (absence totale exigée pour le bon état) | oui |
| D | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares) | non |
| E1 | Plantes majoritairement indigènes, les espèces exotiques présentes ne nuisant pas à l'habitat | non |
| E2 | Végétation composée d'espèces de milieux humides ou riverains | non |
| F | Au moins 50 % de plantes à fleurs, 70 % de la toiture en sol et végétation, eau comprise | non |
| G | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de fleurs sauvages et d'orpins, tas de sable, pierres ou bois pour le bon état | non |

**Délais et difficultés (module T, équations T3 et T4)**

| Paramètre | Valeur | Source |
|---|---|---|
| Création, type sans état | 1 ans | onglet G-4, ligne 81, « Urban - Vegetated garden », habitat sans évaluation d'état (colonne Condition Assessment N/A) |
| Amélioration, mauvais vers moyen | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers moyen |
| Amélioration, mauvais vers bon | 5 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration mauvais vers bon |
| Amélioration, moyen vers bon | 2 ans | onglet G-5, ligne 82, « Urban - Vegetated garden », amélioration moyen vers bon |
| Difficulté de création | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |
| Difficulté d'amélioration | 1 | onglet G-3, ligne 102, « Urban - Vegetated garden » |

**Valeurs de référence pour 100 m² (équations H4 et H5)**

| État | V, m²HE |
|---|---|
| Bon état | 45,83 |
| État moyen | 40,1 |
| Mauvais état | 32,08 |

Posé sur dalle (convention C-S2), en bon état, 100 m² valent : moins de 15 cm de substrat 22,91 m²HE, 15 à 30 cm 27,5 m²HE, 30 à 80 cm 32,08 m²HE, 80 cm et plus 41,25 m²HE.

**Trajectoire de 100 m² créés (équation T3)**

Difficulté de création D = 1 ; valeurs annuelles en m²HE et valeur intégrée sur 50 ans en m²HE·an.

| État visé | An 1 | An 2 | An 3 | An 5 | An 10 | An 15 | An 20 | An 30 | An 50 | Intégrée |
|---|---|---|---|---|---|---|---|---|---|---|
| sans état | 0 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 45,8 | 2 246 |

**Contribution à Bnat**

Bnat ne dépend pas du type d'habitat mais de la nature de surface et du support : en pleine terre, 100 m² apportent 100 points-m² au numérateur de l'équation A3 ; sur dalle ou en toiture, 100 m² apportent 100 x c, où c est le coefficient de la classe d'épaisseur (`sols.csv`).
