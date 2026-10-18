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

### 5.4 Nuisances et clôtures

#### Fiche F16. Éclairage extérieur

La classe d'éclairage se justifie par la note d'éclairage du projet : implantation des points lumineux, température de couleur, orientation du flux, horaires d'extinction. Un éclairage piloté par détection de présence, éteint hors présence, est de classe L1. Un éclairage décoratif de façade allumé toute la nuit est de classe L2 pour les unités situées à moins de 50 m.

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
