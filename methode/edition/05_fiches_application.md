## Partie 5. Fiches d'application

Les fiches d'application précisent comment appliquer la méthode dans des configurations particulières, comme les fiches FA_ de la méthode Th-BCE. Elles ne créent aucun coefficient : elles disent comment saisir une situation avec les types, les positions, les statuts et les conventions existants. Une règle d'application qui demande une valeur renvoie à une convention numérotée.

### 5.1 Périmètre et nature de l'opération

#### Fiche F01. Réhabilitation

Une réhabilitation sans emprise nouvelle se calcule comme une opération neuve : état initial relevé, état projet saisi. Le bâti existant est une unité VB.1 conservée à l'état projet (valeur nulle, sans effet sur Cnat). La cour, le jardin ou la toiture modifiés sont des unités créées ou améliorées. Une toiture existante végétalisée lors de la réhabilitation est une unité hors-sol créée.

Le module G ne porte que sur les matériaux de la réhabilitation, tels que l'ACV du projet les donne. Quand l'opération n'est pas soumise à la RE2020, les émissions par phase se saisissent depuis l'ACV réalisée volontairement ; à défaut, Inat n'est pas calculé et le RSNat le dit (fiche F23).

Exemple : cas 4 de la partie 8.

#### Fiche F02. Extension et surélévation

Le périmètre est la parcelle entière, existant compris. Les unités non touchées par l'extension sont conservées ; l'emprise nouvelle détruit les unités qu'elle recouvre. Une surélévation ne change rien au sol ; elle peut porter une toiture végétalisée créée. Le seuil de Bnat se lit sur l'emprise totale du bâti après extension (fiche A02).

#### Fiche F03. Opérations d'ensemble, lots et zones d'aménagement concerté

Une opération d'aménagement se calcule à deux niveaux :
- l'aménageur calcule l'opération d'ensemble : parcelle = périmètre de l'opération, unités des espaces publics détaillées, lots représentés par une unité « lot » au type d'habitat que le cahier des charges de cession leur impose (ou VB.1 pour la part constructible si rien n'est imposé) ;
- chaque constructeur calcule son lot : parcelle = lot, état initial = état du lot à sa cession.

Les deux calculs ne s'additionnent pas : celui de l'aménageur porte la transformation du site, celui du lot porte ce que le constructeur ajoute ou retire. Le RSNat du lot cite l'empreinte du RSNat de l'opération d'ensemble.

#### Fiche F04. Changement d'usage de terres agricoles

Une culture se saisit avec son type EUNIS I1 (sans grille d'état : f = 1). Une prairie permanente se saisit avec son type E2 et sa grille. Une prairie temporaire en rotation est une culture (I1.1 ou I1.3). Une jachère de plus de cinq ans se relève comme une prairie ou une friche selon sa végétation. Le diagnostic se fait sur la végétation constatée, pas sur la déclaration à la politique agricole commune.

#### Fiche F05. Opérations phasées

Une opération réalisée en plusieurs tranches se calcule par variante unique avec un chantier par tranche : chaque unité porte l'année de début de son chantier. Les fiches A26 à A28 s'appliquent unité par unité avec son propre calendrier. Une unité conservée jusqu'à une tranche ultérieure, puis détruite, est une unité conservée dont la valeur s'annule l'année de destruction (saisie comme un renouvellement sans recréation).

#### Fiche F06. Démolition et dépollution préalables

La démolition et la dépollution font partie de l'opération quand elles sont réalisées pour elle : l'état initial est l'état avant démolition. Les terres excavées et évacuées n'entrent pas dans Inat (le transport et le traitement des terres relèvent du contributeur chantier de l'ACV, lu dans le RSEE). Un sol pollué laissé en place sous une couverture se saisit avec la position et l'épaisseur de la couverture.

### 5.2 Sols et supports

#### Fiche F07. Friches urbaines et industrielles

Une friche se relève avec soin : sa valeur peut être élevée (VB.8 vaut 0,5 m²HE par m² en bon état), et le critère D de la grille urbaine (mosaïque d'au moins quatre communautés pionnières) distingue une friche riche d'un terrain vague. Le relevé se fait en période favorable (convention C-R1) et l'écologue décrit la mosaïque. Une friche sur dalle ou sur remblai étanche se saisit en position sol sur dalle avec l'épaisseur de substrat constatée.

#### Fiche F08. Sols reconstitués et apports de terre

Une terre végétale ou un sol reconstitué sur un sol en place perméable est en pleine terre si les cinq critères de la pleine terre du Cerema sont remplis : sans revêtement, végétalisé, au moins deux horizons et plus de 30 cm, sans interface imperméable, matériaux terreux majoritaires. Sinon, l'unité est sur dalle et l'épaisseur saisie est celle du sol reconstitué. Un sol reconstitué sur une dalle de parking souterrain n'est jamais en pleine terre, quelle que soit son épaisseur (convention C-S2).

#### Fiche F09. Protection des habitats pendant le chantier

Une unité conservée est protégée (fiche A27) si le plan d'installation de chantier prévoit : une clôture fixe autour de l'unité, et sous le houppier des arbres jusqu'à l'aplomb de la couronne ; l'interdiction de stocker, de circuler et de déposer des terres dans l'emprise protégée ; le contrôle de ces mesures par le maître d'œuvre. À défaut, l'unité perd 25 % de sa valeur pendant le chantier (convention C-T4). L'attestation à l'achèvement vérifie l'état des unités conservées : une unité dégradée pendant le chantier est saisie avec son état constaté.

### 5.3 Éléments végétaux particuliers

#### Fiche F10. Arbres existants

Un arbre conservé est une unité arbre conservée ; un arbre abattu est une unité de l'état initial absente de l'état projet. Un arbre transplanté est une unité créée de stade jeune, quel que soit son âge, parce que la reprise n'est pas acquise. Le houppier se relève sur photographie aérienne ou au sol ; à défaut, la surface par défaut de la classe de diamètre s'applique (fiche A14).

#### Fiche F11. Haies

Une haie créée se saisit avec le type visé (FA.3 si au moins cinq espèces indigènes par 25 m sont plantées). Le renforcement d'une haie existante (regarnissage, plantation d'arbres de haut jet) est une amélioration. Un déplacement de haie est une destruction suivie d'une création.

#### Fiche F12. Matériaux biosourcés autres que le bois, réemploi

La paille, le chanvre, la ouate de cellulose, le liège et les autres matériaux biosourcés ne sont pas couverts par le module G en v1 : leur occupation des sols n'a pas d'inventaire sourcé. Leur climat est compté par l'indicateur 101 du RSEE. Les matériaux de réemploi n'ont pas d'occupation des sols et leur climat est celui que la RE2020 leur attribue.

#### Fiche F13. Toitures végétalisées et toitures biosolaires

Une toiture qui associe panneaux photovoltaïques et végétation compte pour sa seule surface végétalisée, mesurée en projection hors emprise des panneaux et de leurs allées techniques. Une toiture végétalisée dont la réfection de l'étanchéité est prévue pendant la période de référence porte ce renouvellement (fiche A30). Une toiture biodiverse se justifie par le critère G de la grille urbaine.

#### Fiche F14. Façades végétalisées

Une façade compte pour sa surface végétalisée à maturité, plafonnée à 10 m de hauteur imputable (convention C-B1). Une façade enracinée au sol dont les plantes ne sont pas encore installées est une unité créée (délai de la ligne anglaise « ground based green wall »). Les murs végétalisés hors sol exigent un arrosage : leur pérennité se justifie par un contrat d'entretien.

#### Fiche F15. Mares, noues et zones humides créées

Une mare se saisit en VB.20 si ses berges sont naturelles et son alimentation pluviale, phréatique ou par ruissellement ; en VB.21 si son eau est traitée ou ses berges maçonnées. Une noue végétalisée qui infiltre en surface se saisit en VB.19 ; la surface de toiture ou de voirie qu'elle reçoit entre dans le bonus d'infiltration de Bnat (fiche A24). Une zone humide créée par décaissement se saisit avec le type de zone humide visé (D5, E3) et sa grille EZ1 : le critère A (nappe proche de la surface toute l'année) doit être justifié par une étude hydrologique.

Le bilan hydrique (fiche A49) demande, pour une mare, sa profondeur, la nature de son fond et les surfaces raccordées ; pour une noue ou un jardin de pluie, les surfaces raccordées. Une zone humide créée alimentée par la nappe se déclare comme telle et n'a pas de bilan ; alimentée par la seule pluie, elle relève du groupe des milieux humides alimentés par la pluie (fiche A47) et sa valeur suit son stress hydrique.

### 5.4 Nuisances et clôtures

#### Fiche F16. Éclairage extérieur

L'éclairage se saisit avec les données de la note d'éclairage du projet : implantation des points lumineux, distance de chaque unité au plus proche, température de couleur, horaires d'extinction et de rallumage, part de temps allumé sous détection de présence (fiches A51 à A53). Les raccourcis L1 et L2 ne servent qu'à défaut de note. Un éclairage décoratif de façade allumé toute la nuit se saisit avec sa température de couleur et sa distance à chaque unité située à moins de 50 m ; au-delà, il est sans effet. Voir aussi la fiche F26.

#### Fiche F17. Clôtures et passages à faune

Une tache est close si une clôture continue l'entoure, bâtiments compris. Une clôture est perméable si elle offre un passage de 15 x 15 cm au moins tous les 20 m (convention C-C3), ou si elle est une haie sans grillage. Un muret plein de plus de 20 cm de haut est une clôture étanche (convention C-C3).

### 5.5 Articulation avec les autres démarches

#### Fiche F18. Espèces protégées et séquence éviter, réduire, compenser

OpenNAT ne remplace ni l'inventaire des espèces protégées, ni la demande de dérogation, ni l'étude d'impact. Quand une espèce protégée est présente, son habitat se saisit avec son type et son état comme tout autre ; la méthode ne lui applique aucun coefficient propre. Le RSNat mentionne les procédures en cours. Les mesures d'évitement se traduisent par des unités conservées et protégées ; les mesures de réduction, par des facteurs de nuisances et des clôtures perméables ; les mesures de compensation sur le site, par des unités créées ou améliorées.

#### Fiche F19. Mesures compensatoires hors du site

La v1 ne calcule que le site. Une mesure de compensation hors site n'entre pas dans Cnat ; elle peut faire l'objet d'un calcul OpenNAT distinct sur la parcelle où elle est mise en œuvre, dont le RSNat est cité par celui de l'opération. Les deux résultats ne s'additionnent pas dans la v1.

#### Fiche F20. Stationnements et voiries perméables

Une aire de stationnement en dalles alvéolées engazonnées se saisit en VB.4 ; en enrobé drainant ou en pavés à joints sablés, en VB.3 ; en enrobé ou en béton, en VB.2. Les arbres d'alignement d'un parking sont des unités arbres ; leurs fosses de plantation ne sont pas de la pleine terre si elles sont isolées sous le revêtement.

#### Fiche F21. Espaces partagés entre plusieurs bâtiments

Une opération de plusieurs bâtiments sur une même parcelle se calcule en une seule fois : Bnat, Cnat et Inat portent sur l'opération entière. Les indicateurs par bâtiment ne sont pas définis en v1 ; le RSNat donne Inat par bâtiment à titre indicatif.

#### Fiche F22. Diagnostic de l'état initial

L'état initial se relève par un écologue, sur le terrain, en période favorable (convention C-R1), avant toute intervention sur le site. Un état initial dégradé volontairement dans les deux ans précédant le dépôt (convention C-R5) (débroussaillage, labour, décapage) se saisit avec l'état antérieur documenté (photographies aériennes, inventaires antérieurs), pour ne pas récompenser une destruction préalable.

#### Fiche F23. Opérations sans étude RE2020

Les aménagements, les bâtiments non soumis à la RE2020 et les opérations sans RSEE saisissent les données du chapitre 4 directement. Sans ACV, Inat n'est pas calculé : le RSNat porte Cnat, Bnat et la conformité du site, et mentionne l'absence d'Inat.

#### Fiche F24. Plan local d'urbanisme et autres règles d'urbanisme

Quand le PLU impose un coefficient de biotope par surface ou une part de pleine terre, l'attestation au permis compare le projet à ces minimums et ne conclut pas à la conformité s'ils ne sont pas respectés (convention C-P1). Les coefficients de pondération du PLU peuvent différer de ceux de Bnat : l'attestation affiche Bnat / 100 et rappelle que le respect du PLU s'apprécie avec les coefficients du PLU, calculés par le pétitionnaire dans son dossier de permis. OpenNAT ne se substitue à aucune pièce du permis de construire.

#### Fiche F25. Certification Effinature

Les seuils de Bnat et de pleine terre de la v1 reprennent ceux du critère SOL 01.2.5 du référentiel Effinature 8.1 (convention C-E6). Un projet engagé dans la certification Effinature fournit son RSNat comme pièce ; l'organisme certificateur applique le référentiel et ses propres modes de preuve. OpenNAT ne délivre ni certificat ni label.

### 5.6 Données des modules dynamiques

#### Fiche F26. Note d'éclairage et horaires

L'heure d'extinction se saisit en heure légale, telle que le règlement de la copropriété, le contrat d'exploitation ou l'arrêté municipal la fixe. Pour un éclairage d'activité économique, c'est l'heure de fin d'activité plus une heure (arrêté du 27 décembre 2018, article 2) ; pour un parc de stationnement, plus deux heures. Un éclairage dont la plage varie selon les jours se saisit avec sa plage la plus longue. Une détection de présence se saisit avec la part de temps allumé mesurée sur une installation comparable ou, à défaut, déclarée par le fabricant ; sans justification, la part est 1. La distance se mesure du pied du luminaire au bord le plus proche de l'unité. Un luminaire équipé d'un pare-lumière qui empêche toute lumière directe sur l'unité est réputé à plus de 50 m.

#### Fiche F27. Calendrier du chantier

L'année et le mois de début du chantier sont ceux de la déclaration d'ouverture du chantier prévue ; à l'achèvement, ceux de la déclaration réelle. Le mois de destruction est celui des défrichements, abattages, dessouchages, comblements de mares et démolitions de bâtis abritant des gîtes ; quand ces travaux sont faits avant l'ouverture du chantier, c'est leur mois réel. Un calendrier écologique prescrit par un arrêté de dérogation espèces protégées s'applique et se déclare tel qu'il est prescrit. Un projet qui avance les plantations par une installation provisoire (pépinière sur site, placage de gazon en motte) les déclare au mois réel ; la convention C-K2 ne s'applique qu'à défaut.

#### Fiche F28. Plan de gestion écologique

Le plan de gestion écologique se déclare par sa durée, comptée depuis la livraison, et se justifie par une pièce qui engage le gestionnaire : clause du règlement de copropriété ou du cahier des charges de cession, contrat d'entretien, obligation réelle environnementale, convention avec une collectivité. Il décrit au moins la fauche ou le pâturage des milieux herbacés (dates, fréquence, exportation des produits), la taille des haies hors période de nidification et le maintien des bois morts. Une tonte régulière n'est pas un plan de gestion écologique : les unités ainsi tondues se déclarent en gestion courante. Un abandon prévu (réserve foncière, délaissé) se déclare comme tel (fiche A55). Un plan de gestion prescrit par la certification Effinature se déclare avec la durée de l'engagement pris.

#### Fiche F29. Raccordement des eaux pluviales aux milieux humides

Une surface imperméable raccordée à une mare, une noue ou un jardin de pluie se déclare par sa surface en projection horizontale. Une surface perméable (talus, prairie) dont le ruissellement est dirigé vers le milieu humide se déclare séparément : seul un dixième de la pluie qui y tombe est compté (convention C-W11). Le raccordement doit figurer au plan des réseaux et au dossier loi sur l'eau quand il existe. Une surverse vers le réseau ne change pas la surface raccordée. Une mare dont le fond est rendu étanche par une géomembrane ou un béton se déclare à fond étanche ; un fond d'argile compactée, à fond argileux ; un fond non traité, naturel.

#### Fiche F30. Sol, substrat et arrosage

La texture du sol se déclare d'après l'étude géotechnique ou une analyse de terre, selon la classification de la FAO-56 (tableau 19) ; un sol reconstitué (fiche F08) se déclare avec la texture et l'épaisseur de la terre apportée. La profondeur de sol est celle que les racines peuvent atteindre : jusqu'à la roche, à la dalle, à une couche compactée ou à la nappe permanente. Un substrat de toiture ou de dalle se déclare avec son épaisseur ; la réserve volumique déclarée par le fabricant remplace la valeur de 0,20 quand une fiche technique la justifie. Une unité arrosée par un système automatique se déclare arrosée ; un arrosage manuel d'appoint ne se déclare pas. Le volume d'arrosage calculé est un indicateur complémentaire : il ne réduit ni n'augmente Cnat.

