# Méthode OpenNAT Crédits, version 1

Méthode conventionnelle de quantification, de suivi, de vérification et d'émission de crédits de gain de nature, fondée sur la méthode de calcul OpenNAT 1.

Éditeur : NORMATYS. Vérification : IRICE et tout organisme qualifié selon ISO/IEC 17029 agréé par le registre. Émission : l'opérateur du registre des crédits OpenNAT. Moteur de calcul libre : le moteur OpenNAT.
Version 1, 24 octobre 2026. Projet soumis à la validation du Biodiversity Standard Council : la méthode, ses conventions et ses valeurs ne sont pas opposables tant que le conseil ne les a pas validées. Aucun crédit ne peut être émis avant cette validation.
Texte sous licence CC BY 4.0. Moteur sous licence AGPL-3.0-or-later.

## 1. Objet, domaine d'application, exclusions

### 1.1 Objet

La méthode OpenNAT Crédits dit comment un gain de nature, mesuré par la méthode OpenNAT 1 sur un site réel, devient des crédits : ce qui est mesuré, par rapport à quoi, avec quelle prudence, à quels moments, par qui, pendant combien de temps, avec quelle garantie, et ce que l'acheteur d'un crédit peut en dire. Elle ne modifie aucun calcul d'OpenNAT 1 : elle les appelle sur des états supplémentaires (le scénario de référence, la variante d'obligations, les états relevés) et compare leurs résultats.

Un crédit OpenNAT est un engagement du porteur de projet à produire et à maintenir un gain de nature mesuré, vérifié et inscrit au registre. Il est acquis par un acheteur pour son propre usage puis retiré. Dans la présente version, il ne se revend pas (convention C-X15).

### 1.2 Domaine d'application

Projets situés en France métropolitaine, dans le domaine d'application d'OpenNAT 1 (zones biogéographiques atlantique, continentale, méditerranéenne et alpine), qui créent ou améliorent des habitats :

- restauration ou renaturation d'un site sans construction ;
- désimperméabilisation et renaturation d'espaces bâtis ou revêtus ;
- opération de construction ou d'aménagement dont le gain sur le site dépasse ses obligations (chapitre 6).

### 1.3 Exclusions de la version 1

- Les crédits de perte évitée : un projet qui se contente de protéger un habitat menacé ne reçoit aucun crédit, faute de méthode partagée pour établir la menace (convention C-X5).
- La biodiversité grise : Inat mesure une consommation de nature ailleurs, il ne crée aucun gain et ne se crédite jamais.
- Les exclusions d'OpenNAT 1 : milieux littoraux et marins, outre-mer, complexes d'habitats, grottes, glaciers et reliefs volcaniques actifs.
- Les parcelles d'un site France Crédits Biodiversité pendant la durée de son agrément : leurs gains sont vendus en unités de compensation, de restauration et de renaturation, et ne peuvent pas l'être une seconde fois (convention C-X16).
- Les sites dégradés volontairement dans les dix ans qui précèdent le dépôt du projet, sauf si l'état antérieur documenté sert d'état initial (convention C-X6).

La méthode ne remplace ni la séquence éviter, réduire, compenser, ni l'agrément d'un site France Crédits Biodiversité. Un crédit OpenNAT ne vaut pas mesure compensatoire au sens du code de l'environnement.

## 2. Termes, définitions, symboles et unités

### 2.1 Termes

Projet : ensemble des opérations de création, d'amélioration et de gestion d'habitats sur un site défini par ses parcelles cadastrales et sa géométrie, porté par un porteur de projet pendant la période de crédit.

Période de crédit : 50 ans à compter du premier mois des travaux, comme la période de référence N d'OpenNAT 1 (conventions C-K3 et C-X2).

Scénario de référence : évolution la plus probable du site en l'absence du projet, sur la période de crédit, sous le même climat (chapitre 6).

Variante d'obligations : état du site qui satisfait exactement les obligations réglementaires, contractuelles et de certification du projet, et rien de plus (chapitre 6).

État relevé : état d'une unité d'habitat constaté sur le terrain lors d'un relevé de suivi selon les protocoles de la partie 6 de l'édition complète d'OpenNAT 1.

Gain créditable : gain intégré du projet au-delà du scénario de référence et de la variante d'obligations, retenu au 10e centile des tirages (chapitre 7).

Lot de crédits : crédits émis pour un même projet à une même vérification.

Unité prévisionnelle : gain futur estimé à la validation, inscrit au registre sans pouvoir être cédé ni retiré.

Réserve : crédits retenus à chaque émission, non cessibles, qui couvrent les pertes de tous les projets du registre.

Inversion : diminution du gain créditable cumulé constatée à une vérification.

Retrait : usage définitif d'un crédit par son détenteur, public et irréversible.

### 2.2 Symboles

| Symbole | Désignation | Unité |
|---|---|---|
| t | Année de la vérification, comptée depuis le premier mois des travaux | an |
| t_prec | Année de la vérification précédente | an |
| I_proj,obs(0..t) | Valeur du site intégrée de l'année 1 à t, avec les états relevés jusqu'à t | m²HE·an |
| I_proj,prev(0..N) | Valeur du site intégrée sur la période de crédit, avec les états projetés | m²HE·an |
| I_ref(0..t) | Valeur intégrée du scénario de référence de l'année 1 à t | m²HE·an |
| I_obl(0..t) | Valeur intégrée de la variante d'obligations de l'année 1 à t | m²HE·an |
| I_seuil(0..t) | max(I_ref(0..t), I_obl(0..t)), tirage par tirage | m²HE·an |
| ΔI_j(t) | I_proj,obs(0..t) - I_seuil(0..t) pour le tirage j | m²HE·an |
| G(t) | Gain créditable cumulé : 10e centile des ΔI_j(t) | m²HE·an |
| U | Taille du crédit : 1 000 | m²HE·an |
| r | Taux de réserve du projet | sans unité, 0,20 à 0,40 |
| C_emis(t) | Crédits émis au porteur, cumulés, jusqu'à t | crédits |
| C_res(t) | Crédits versés à la réserve, cumulés, jusqu'à t | crédits |
| E(t) | Crédits émis au porteur à la vérification t | crédits |
| P | Plafond d'émission du projet | crédits |

### 2.3 Unités et arrondis

Les gains sont en m²HE·an, les crédits en nombre de crédits. Les crédits émis au porteur sont des nombres entiers ; les crédits de la réserve et les retraits se comptent au centième. Les résultats intermédiaires sont conservés sans arrondi.

## 3. Principes

**Constat avant émission.** Un crédit n'est émis que pour un gain réalisé à la date de la vérification et constaté par relevé. Le gain encore attendu reste en unités prévisionnelles.

**Comparaison au scénario de référence et aux obligations.** Le gain se mesure par rapport à ce que le site serait devenu sans le projet et à ce que le porteur était de toute façon tenu de faire. Seul l'excédent est créditable.

**Prudence.** Le gain retenu est le 10e centile des tirages de l'analyse d'incertitude d'OpenNAT 1, calculé sur la différence tirage par tirage, et non la valeur centrale.

**Durée.** Le gain doit être maintenu pendant toute la période de crédit de 50 ans, garanti par une obligation réelle environnementale et par un plan de gestion financé.

**Garantie mutualisée.** Une part de chaque émission alimente une réserve commune qui couvre les pertes.

**Unicité.** Un gain n'est crédité qu'une fois, sur un seul registre, au profit d'un seul usage.

**Publicité.** Les pièces du projet, les relevés, les rapports, les émissions, les cessions et les retraits sont publics, hors données personnelles et secrets d'affaires listés au dossier.

**Usage honnête.** Un crédit retiré permet de déclarer une contribution chiffrée à la restauration d'un site identifié, jamais une neutralité, une compensation ou un impact positif global.

**Séparation des rôles.** NORMATYS écrit la méthode, le vérificateur vérifie, le registre émet. Aucun d'eux ne détient de crédits ni n'est rémunéré selon le prix ou le volume des crédits.

## 4. Éligibilité des projets

### 4.1 Conditions

Un projet est éligible si, à sa validation :

- il entre dans le domaine d'application (1.2) et dans aucune exclusion (1.3) ;
- le porteur a la maîtrise foncière du site pour toute la période de crédit, ou s'engage à la produire avant la première émission (chapitre 10) ;
- le gain prévu au 10e centile, I_proj,prev(0..N) - I_seuil(0..N), est positif ;
- l'additionnalité réglementaire et financière est démontrée (4.2) ;
- la note de risque de l'annexe A ne dépasse pas 40 points (convention C-X11) ;
- aucune parcelle du site ne porte un autre projet actif au registre, ni une unité de compensation, de restauration ou de renaturation d'un site agréé, ni un crédit d'un autre registre pour le même gain (convention C-X16).

Il n'y a pas de surface minimale (convention C-X3) : les frais fixes de validation et de vérification limitent d'eux-mêmes les projets trop petits.

### 4.2 Additionnalité

Additionnalité réglementaire : aucune part du gain créditable ne répond à une obligation. Toutes les obligations entrent dans la variante d'obligations (6.2), ce qui retire leur effet du gain par le calcul et non par une déclaration.

Additionnalité financière : le porteur démontre, par l'un des deux moyens suivants, que le projet ne se ferait pas, ou pas à la même échelle, sans le revenu des crédits (convention C-X7) :

- plan de financement montrant que les recettes du projet hors crédits ne couvrent pas le coût de la restauration et de la gestion sur 50 ans ;
- barrières documentées (absence de financement public ou privé disponible, absence de débouché économique du site restauré).

Quand le projet reçoit d'autres financements (subvention, mécénat, crédits carbone sur la même surface), le porteur démontre que le revenu des crédits OpenNAT étend la portée, l'échelle, la vitesse ou la durée du projet. La démonstration est publique et vérifiée sur pièces à la validation, puis à chaque revalidation décennale.

Date de coupure : un site débroussaillé, labouré, décapé, drainé ou revêtu dans les dix ans qui précèdent le dépôt est décrit, à l'état initial et dans le scénario de référence, par son état antérieur documenté (convention C-X6).

## 5. Unité, lot et numéro de série

Un crédit OpenNAT vaut U = 1 000 m²HE·an de gain créditable (convention C-X1). Ordre de grandeur : 20 m² d'écosystème de référence en pleine intégrité pendant 50 ans.

Chaque lot porte : l'identifiant du projet, le numéro de vérification, la période couverte (de t_prec à t), le millésime (année de t), la version de la méthode OpenNAT Crédits, la version de la méthode OpenNAT et la version des données, le type de milieu dominant du gain, la zone biogéographique, la commune, le nombre de crédits émis au porteur, le nombre versé à la réserve et une plage de numéros de série.

Numéro de série : ONC-[identifiant du projet]-[millésime]-[numéro de vérification]-[rang du crédit dans le lot, sur six chiffres].

## 6. Scénario de référence et variante d'obligations

### 6.1 Scénario de référence

Le scénario de référence décrit l'évolution la plus probable du site sans le projet. Il se saisit comme une variante du fichier projet OpenNAT, calculée par les mêmes modules que l'état projet, sous le même climat, avec les mêmes tirages. Il part de l'état initial (OpenNAT 1, chapitre 4) et lui applique les règles suivantes, dans cet ordre (convention C-X4) :

| Situation de l'unité à l'état initial | Évolution dans le scénario de référence |
|---|---|
| Usage agricole, forestier ou urbain en cours, documenté sur les trois dernières années (déclaration PAC, bail, plan de gestion, entretien facturé) | l'usage et la gestion se poursuivent sur toute la période (règle de l'état initial de la convention C-M3) |
| Milieu herbacé sans usage ni entretien depuis au moins deux ans | succession de la convention C-M2 : variante abandonnée de la BKompV, puis friche arbustive après quinze ans |
| Milieu ligneux sans gestion | maintien de son type ; vieillissement par les stades d'âge de la BKompV quand le type les distingue |
| Milieu minéral, revêtu ou bâti | maintien |
| Obligation déjà prescrite sur le site sans le projet (gestion imposée, restauration ordonnée, servitude) | appliquée comme si elle était exécutée |
| Usage incertain entre deux lignes du tableau | la ligne qui donne la valeur intégrée la plus forte |

Le scénario de référence ne prévoit jamais la destruction du site : la méthode ne crédite pas la perte évitée (1.3). Il est arrêté à la validation, et réexaminé à chaque revalidation décennale (9.4) ; une réévaluation ne s'applique qu'aux vérifications suivantes.

### 6.2 Variante d'obligations

La variante d'obligations est l'état projet réduit à ce que le porteur est tenu de faire. Elle se saisit comme une variante du fichier projet, et le porteur liste chaque obligation avec sa source :

- règles d'urbanisme : coefficient de biotope, pleine terre, espaces verts, plantations imposés par le PLU ou le permis ;
- autorisations environnementales et mesures d'évitement, de réduction ou de compensation prescrites ;
- obligations contractuelles : cahier des charges de cession, bail environnemental, convention de financement qui impose des aménagements ;
- objectifs de certification : quand le projet est candidat à une certification qui exige un niveau de gain (par exemple le niveau 2 d'OpenNAT dans une certification Effinature), la part du gain que ce niveau exige.

Chaque obligation exprimée en surface d'habitat ou en coefficient se traduit, unité par unité, par la plus petite configuration conforme du plan masse du projet, en gardant les types d'habitat du projet. Une obligation exprimée en niveau de gain se traduit par I_obl(0..N) = I_ref(0..N) + gain exigé. Le vérificateur contrôle la traduction de chaque obligation (convention C-X8).

Pour un projet sans aucune obligation, la variante d'obligations est le scénario de référence.

## 7. Calcul du gain créditable et des émissions

### 7.1 Gain à la validation

Dans tous les calculs du présent chapitre, la difficulté de création ou d'amélioration d'OpenNAT 1 (convention C-T7) est neutralisée : le risque d'échec qu'elle exprime est porté par le constat avant émission et par la réserve (convention C-X19).

À la validation, le moteur calcule pour chaque tirage j de 1 à n (n au moins 1 000, mêmes valeurs tirées pour les trois états) :

(X1) ΔI_prev,j = I_proj,prev(0..N) - max(I_ref(0..N), I_obl(0..N))

(X2) G_prev = 10e centile des ΔI_prev,j

(X3) Unités prévisionnelles : UP = G_prev x (1 - r) / U, au centième

(X4) Plafond d'émission : P = partie entière de UP

### 7.2 Gain à une vérification

À la vérification de l'année t, le moteur recalcule l'état projet en remplaçant, pour chaque unité et chaque année jusqu'à t, l'état prévu par l'état relevé (chapitre 8). Au-delà de t, il garde la prévision. Pour chaque tirage j :

(X5) ΔI_j(t) = I_proj,obs(0..t) - max(I_ref(0..t), I_obl(0..t))

(X6) G(t) = 10e centile des ΔI_j(t) (convention C-X9)

### 7.3 Émissions

(X7) C_emis(t) = min( P , partie entière de [max(G(t), 0) x (1 - r) / U] )

(X8) E(t) = C_emis(t) - C_emis(t_prec), si E(t) est positif ; sinon E(t) = 0 et le chapitre 11 s'applique

(X9) Réserve : C_res(t) = max(G(t), 0) x r / U, au centième, plafonné à P x r / (1 - r) ; versement à la vérification t : C_res(t) - C_res(t_prec) quand il est positif

Les formules (X7) à (X9) travaillent sur des cumuls : le reste d'arrondi d'une vérification est repris à la suivante, et aucun crédit n'est émis deux fois pour la même année.

Le gain des années postérieures à t n'est jamais crédité à la vérification t, même s'il est très probable.

### 7.4 Cas des opérations de construction

Pour une opération de construction ou d'aménagement, le gain créditable porte sur le site seul. La biodiversité grise de l'opération (Inat) n'est pas déduite ; elle est publiée avec chaque lot, avec Snat, pour que l'acheteur sache ce que l'opération consomme ailleurs (convention C-X10, soumise au conseil, décision DC3).

## 8. Suivi et relevés

### 8.1 Calendrier

Le porteur fait relever le site aux années 1, 3, 5, 10, 15, 20, 30, 40 et 50 comptées depuis la fin des travaux de restauration (convention C-X12). Il peut faire relever le site à toute autre date, à ses frais. Un relevé n'est retenu pour une vérification que s'il a moins de douze mois.

### 8.2 Contenu d'un relevé

Un relevé couvre toutes les unités d'habitat de l'état projet et comprend :

- les surfaces réalisées, mesurées sur plan ou par géomètre, à 5 % près ;
- la grille d'état de chaque unité, selon les protocoles de la partie 6 de l'édition complète d'OpenNAT 1, avec les pièces exigées pour chaque réponse « oui » ;
- l'inventaire des arbres plantés et leur survie, l'état des haies par tronçons de 100 m au plus ;
- la gestion réalisée depuis le relevé précédent, avec ses pièces (factures, registre de fauche, rapports) ;
- les espèces exotiques envahissantes observées ;
- des photographies géolocalisées et datées, depuis des points fixes repérés au premier relevé.

Le relevé est fait par un écologue inscrit sur la liste du registre, qui n'a ni conçu ni réalisé le projet et n'a aucun lien d'intérêt avec le porteur (convention C-X13).

### 8.3 Règles de saisie

- Une unité non relevée prend un score d'état nul (toutes ses réponses valent « non », règle de la partie 6) pour toutes les années depuis le relevé précédent.
- Entre deux relevés, chaque unité garde, pour chaque année, le plus faible des deux scores relevés (convention C-X14).
- Une unité disparue ou détruite prend la valeur du type constaté à la date du relevé, et la valeur nulle depuis le relevé précédent si la date de destruction n'est pas connue.
- La maturation des unités créées continue de suivre la courbe de la convention C-M1, avec le délai de maturité de l'état prévu, qui court depuis la plantation : l'état relevé fixe la valeur visée, il ne remet pas l'horloge à zéro. Sans cette règle, un meilleur état relevé, dont le délai de maturité est plus long dans OpenNAT 1, ferait baisser la valeur des premières années.

## 9. Validation et vérification

### 9.1 Vérificateur

Le vérificateur est IRICE ou tout organisme agréé par le registre, qualifié selon ISO/IEC 17029. Il est rémunéré au forfait, quel que soit le nombre de crédits émis. Il ne vérifie pas un projet qu'une entité liée a conçu, monté ou réalisé, sauf si le lien est traité dans son analyse de risques d'impartialité et que son comité d'impartialité l'a accepté.

### 9.2 Validation

Avant les travaux, ou au plus tard dans les douze mois qui suivent leur début, le vérificateur valide le projet :

- éligibilité (chapitre 4) et additionnalité ;
- fichier projet OpenNAT : état initial, état projet, scénario de référence, variante d'obligations, avec le contrôle de chaque obligation ;
- visite du site pour l'état initial ;
- calcul du moteur : (X1) à (X4), rapport du moteur, RSNat-C prévisionnel ;
- note de risque (annexe A) et taux de réserve ;
- plan de gestion, maîtrise foncière, financement (chapitre 10).

Le rapport de validation conclut favorablement ou non, liste les écarts et les conditions. Le registre enregistre le projet sur un rapport favorable.

### 9.3 Vérification

À chaque relevé du calendrier, le vérificateur :

- contrôle le relevé : qualification et indépendance de l'écologue, période, pièces, cohérence avec le relevé précédent ;
- visite le site, au moins une fois sur deux vérifications et obligatoirement aux années 5, 20 et 50 ;
- recalcule avec le moteur, à la même version de méthode et de données que la validation : (X5) à (X9) ;
- constate une éventuelle inversion (chapitre 11) ;
- signe le rapport de vérification et le RSNat-C constaté.

### 9.4 Revalidation décennale

Tous les dix ans, la vérification comprend une revalidation : scénario de référence, obligations nouvelles, additionnalité, note de risque, plan de gestion et garantie financière (convention C-X12). Le plafond P peut être relevé ou abaissé pour la suite à cette occasion, jamais en dessous des crédits déjà émis.

### 9.5 Projet sans vérification

Si une vérification du calendrier n'est pas faite dans les douze mois qui suivent son échéance, le registre suspend toute émission au profit du projet et met en attente un nombre de crédits de la réserve égal à 10 % des crédits déjà émis au projet. Après cinq ans de retard, le projet est réputé abandonné : l'inversion est réputée totale et évitable (chapitre 11).

## 10. Durée, maîtrise foncière et financement de la gestion

Avant la première émission, le porteur produit au registre :

- une obligation réelle environnementale, au sens de l'article L.132-3 du code de l'environnement, d'une durée au moins égale à la durée restante de la période de crédit, conclue avec une collectivité, un établissement public ou une personne morale de droit privé agissant pour la protection de l'environnement, ou un acte de même effet accepté par le registre (convention C-X2) ;
- le plan de gestion écologique sur la période de crédit, cohérent avec la gestion déclarée dans le fichier projet ;
- la preuve du financement de la gestion sur toute la période : provision affectée, garantie bancaire ou contrat avec un gestionnaire, pour au moins le coût actualisé du plan de gestion et des relevés.

Une cession du site pendant la période de crédit transmet l'obligation réelle environnementale au nouveau propriétaire ; le porteur informe le registre dans les trente jours.

## 11. Réserve de garantie et inversions

### 11.1 Taux de réserve

Le taux de réserve r du projet vaut 20 % plus 5 points par facteur de risque élevé de l'annexe A, dans la limite de 40 %. Un projet dont la note dépasse 40 points n'est pas éligible (convention C-X11). Le taux est fixé à la validation et réexaminé à chaque revalidation décennale.

La réserve est commune à tous les projets du registre. Ses crédits ne sont ni cessibles ni retirables. Ils ne reviennent jamais au porteur.

### 11.2 Signalement

Le porteur signale au registre, dans les trente jours, tout événement susceptible de réduire le gain : incendie, inondation, sécheresse exceptionnelle, destruction, abandon de la gestion, changement de propriétaire ou d'usage. Le registre met alors en attente un nombre de crédits de la réserve égal à la perte estimée.

### 11.3 Constat d'une inversion

Il y a inversion quand, à une vérification, partie entière de [G(t) x (1 - r) / U] est inférieure à C_emis(t_prec). L'inversion vaut la différence, en crédits.

- **Inversion inévitable** (événement naturel ou fait d'un tiers, gestion conforme au plan) : le registre annule dans la réserve autant de crédits que l'inversion. Le porteur présente un plan de reprise. Aucune nouvelle émission n'a lieu au profit du projet tant que le gain cumulé n'a pas retrouvé son niveau d'avant l'inversion.
- **Inversion évitable** (gestion non conforme, changement d'usage, destruction par le porteur, abandon) : le registre annule dans la réserve autant de crédits que l'inversion, puis le porteur remplace ces crédits dans la réserve, par des crédits OpenNAT d'autres projets ou par rachat au registre, dans un délai d'un an. Jusqu'au remplacement, aucun crédit n'est émis au profit d'aucun projet du même porteur.

Les crédits déjà cédés ou retirés ne sont jamais annulés chez l'acheteur : c'est la réserve qui porte le risque (convention C-X11).

## 12. Cession, retrait et allégations

### 12.1 Cession

Un crédit émis peut être cédé une fois, du porteur à un acheteur identifié par le registre. La cession s'inscrit au registre, avec son prix si les parties l'acceptent. Un crédit acquis ne se revend pas : il se retire (convention C-X15). Les unités prévisionnelles ne se cèdent pas. Un contrat d'achat à terme peut porter sur des crédits futurs, hors registre, à condition d'être réglé par la livraison des crédits eux-mêmes, sans règlement en espèces de la différence, sans compensation de positions et sans cession du contrat.

### 12.2 Retrait

Le retrait est demandé par le détenteur et porte : le nombre de crédits (au centième), le lot, le bénéficiaire (le détenteur ou l'entité au nom de laquelle il retire), l'usage déclaré, la période à laquelle l'usage se rapporte, et la date. Le registre publie le retrait et délivre une attestation de retrait, signée et vérifiable, qui porte ces informations, l'identification du site et de ses lots, et la mention d'usage du 12.3.

### 12.3 Allégations

Le détenteur qui retire des crédits peut déclarer :

« [Bénéficiaire] a contribué à la restauration de [nombre] crédits OpenNAT, soit [nombre x 1 000] m²HE·an de gain de nature vérifié, sur le site [nom], à [commune], pour la période [période]. Registre des crédits OpenNAT, retrait n° [numéro]. »

Il ne peut pas déclarer, à partir de crédits OpenNAT : qu'il est neutre, positif ou « nature positive » en biodiversité ; qu'il compense ses impacts, ceux d'un produit ou ceux d'une activité ; qu'un produit ou un service a un effet favorable sur la biodiversité ; ni que ses crédits valent mesure compensatoire au sens du code de l'environnement. Ces règles appliquent la directive (UE) 2024/825 et la reprennent pour la biodiversité (convention C-X17).

Le détenteur qui fait une allégation publique publie la référence de ses retraits. En cas d'allégation contraire au présent chapitre, le registre peut suspendre son compte et publier la suspension.

## 13. Gouvernance des versions

Un projet est validé, vérifié et crédité selon la version de la méthode OpenNAT Crédits, de la méthode OpenNAT et des données en vigueur à sa validation. Ces versions sont figées pour toute la période de crédit, sauf :

- correction d'une erreur reconnue par le Biodiversity Standard Council, qui s'applique aux vérifications suivantes de tous les projets concernés ;
- choix du porteur, à une revalidation décennale, de passer à la version en vigueur, entièrement et pour la suite.

Une nouvelle version ne remet jamais en cause les crédits déjà émis (convention C-X18).

## 14. Récapitulatif standardisé RSNat-C

Un RSNat-C se produit à la validation (prévisionnel) et à chaque vérification (constaté). Il étend le RSNat d'OpenNAT 1 et porte en plus :

- identifiants du projet, de la vérification, du vérificateur et de l'écologue ;
- versions de la méthode OpenNAT Crédits, de la méthode OpenNAT, des données et du moteur ; graine ;
- état initial, état projet, scénario de référence, variante d'obligations, liste des obligations et leur traduction ;
- états relevés par unité et par relevé, avec les références des pièces ;
- I_proj,obs, I_proj,prev, I_ref, I_obl, en valeur centrale et en centiles 5, 10, 50 et 90 ;
- G(t), UP, P, r, C_emis, C_res, E(t), inversion éventuelle ;
- Inat et Snat de l'opération quand c'est une opération de construction ;
- empreintes SHA-256 des entrées, des tables, des sorties et des pièces ;
- signature électronique du vérificateur.

Le schéma XSD et le schéma JSON du RSNat-C sont livrés avec le moteur.

## Annexe A. Grille de risque

Chaque facteur est noté faible, moyen ou élevé ; seul un facteur élevé ajoute 5 points de réserve, les niveaux faible et moyen sont relevés pour suivre leur évolution aux revalidations. Un facteur rédhibitoire rend le projet inéligible. Note du projet : 20 plus la somme des points (convention C-X11).

| Facteur | Faible | Moyen | Élevé | Rédhibitoire |
|---|---|---|---|---|
| Maîtrise foncière | propriété du porteur ou ORE signée | bail emphytéotique couvrant la période | bail plus court, renouvellement prévu | aucune maîtrise sur la période |
| Financement de la gestion | provision ou garantie couvrant 100 % | 75 à 100 % | 50 à 75 % | moins de 50 % |
| Gestionnaire | gestionnaire professionnel sous contrat de 10 ans et plus | contrat de 3 à 10 ans | gestion par le porteur sans référence | aucun gestionnaire désigné |
| Sécheresse | facteur hydrique moyen de l'état projet au moins 0,9 à +2,7 °C | 0,8 à 0,9 | 0,7 à 0,8 | moins de 0,7 |
| Incendie | hors massif exposé | massif exposé, débroussaillement prévu | massif exposé, sans débroussaillement prévu | |
| Inondation et érosion | hors zone inondable | zone d'aléa faible | zone d'aléa moyen | zone d'aléa fort, milieu non adapté |
| Pression foncière | zone naturelle ou agricole du PLU | zone à urbaniser à long terme | zone urbaine ou à urbaniser | projet d'aménagement connu sur le site |
| Espèces exotiques envahissantes | absentes | présentes hors site à moins de 500 m | présentes sur le site, plan de lutte | présentes sur le site, sans plan de lutte |
| Fréquentation | site fermé ou fréquentation encadrée | fréquentation libre faible | fréquentation libre forte | |

Le facteur hydrique est la moyenne, sur les unités végétalisées de l'état projet, du facteur k_W calculé par le module W d'OpenNAT 1 pour le niveau de réchauffement de +2,7 °C.

## Annexe B. Exemple de calcul

Valeurs fictives destinées à montrer l'enchaînement des formules ; le lot 2 recalcule trois exemples par le moteur (culture restaurée en prairie, friche urbaine, parking désimperméabilisé).

Site : un hectare de culture, restauré en prairie de fauche avec une haie. Pas d'obligation. Risque : maîtrise foncière par bail emphytéotique (moyen), financement à 100 % (faible), gestionnaire sous contrat de cinq ans (moyen), facteur hydrique 0,85 (moyen) : aucun facteur élevé, r = 20 %.

Validation : I_proj,prev(0..50) - I_ref(0..50) a pour valeur centrale 150 000 m²HE·an et pour 10e centile 120 000. UP = 120 000 x 0,8 / 1 000 = 96,00 ; P = 96 crédits.

Vérification de l'année 5 : G(5) = 9 300 m²HE·an. C_emis(5) = partie entière de 9 300 x 0,8 / 1 000 = 7 ; E(5) = 7 crédits. C_res(5) = 9 300 x 0,2 / 1 000 = 1,86 crédit versé à la réserve.

Vérification de l'année 10 : G(10) = 24 600. C_emis(10) = partie entière de 19,68 = 19 ; E(10) = 12. C_res(10) = 4,92 ; versement de 3,06.

Vérification de l'année 15, après une sécheresse qui a dégradé la prairie : G(15) = 22 000. Partie entière de 22 000 x 0,8 / 1 000 = 17, inférieure à C_emis(10) = 19 : inversion de 2 crédits, inévitable, annulés dans la réserve. Aucune émission au projet tant que G n'a pas retrouvé 24 600.

## Annexe C. Pièces du dossier de projet

- Formulaire de dépôt : porteur, site, parcelles, géométrie, calendrier.
- Fichier projet OpenNAT avec ses quatre variantes : état initial, état projet, scénario de référence, variante d'obligations.
- Diagnostic écologique de l'état initial, avec relevés selon la partie 6 de l'édition complète d'OpenNAT 1.
- Pièces de l'usage actuel du site sur trois ans et de son état sur dix ans (photographies aériennes datées, déclarations PAC, factures).
- Liste des obligations et leurs sources.
- Démonstration de l'additionnalité financière.
- Plan de gestion sur 50 ans, devis de restauration et de gestion, plan de financement.
- Maîtrise foncière : titre de propriété, bail, projet d'obligation réelle environnementale.
- Auto-évaluation de la grille de risque de l'annexe A.
- Déclaration sur l'honneur : absence de double comptage, absence de dégradation volontaire, liens d'intérêts.
