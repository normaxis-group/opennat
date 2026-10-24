# Conventions de la méthode OpenNAT Crédits, version 1

Les conventions de la famille X (crédits) complètent les 70 conventions d'OpenNAT 1 et suivent les mêmes règles : chacune est numérotée, citée dans le texte de la méthode, classée dans l'une des trois catégories du registre des lectures (source muette, convention de transposition, valeur de secours) et soumise au Biodiversity Standard Council. Toutes sont « proposées, en attente de validation ». Les valeurs numériques entreront dans `donnees/credits.csv` au lot 2, avec leur plage d'incertitude, comme les autres valeurs de méthode : aucune n'est écrite dans le moteur.

Sources lues pour cette famille (texte téléchargé et lu le 24/10/2026, sauf mention) :

| Abréviation | Document |
|---|---|
| VNF | Verra, SD VISta Nature Framework v1.0 (SDVM002), 29 octobre 2024 |
| VRT | Verra, AFOLU Non-Permanence Risk Tool v4.2, 3 mai 2024 |
| VMR | Verra, VCS Methodology Requirements v5.0, 16 décembre 2025 |
| VRI | Verra, Registration and Issuance Process v5.0, 16 décembre 2025 |
| VCS | Verra, VCS Standard v5.0, 16 décembre 2025, et v4.7 pour les règles d'inversion détaillées |
| PVN | Plan Vivo, PV Nature Project Requirements v1.1, et Validation and Verification Requirements |
| GSP | Gold Standard, GHG Emissions Reduction and Sequestration Product Requirements v3.1, 24 avril 2025 |
| GSA | Gold Standard, Afforestation/Reforestation Activity Requirements v1.2.1, avril 2020 |
| BCA | Biodiversity Credit Alliance et Forum économique mondial, High-level Principles to Guide the Biodiversity Credit Market, v7, mai 2025 |
| BNG | Statutory Biodiversity Metric, User Guide (Defra, Natural England), version servie en octobre 2026 ; page gov.uk « Biodiversity net gain » |
| A2024 | Arrêté du 21 novembre 2024 définissant les conditions d'agrément d'un site naturel de compensation, de restauration et de renaturation (JORF n° 277 du 23/11/2024) |
| ORE | Ministère de la Transition écologique, page « Obligation réelle environnementale », mise à jour du 13/02/2026 |

## Unité et durée

### C-X1
Catégorie : valeur de secours.
Un crédit vaut 1 000 m²HE·an. Aucune source ne fixe d'unité en m²HE·an. La taille est choisie pour qu'un crédit représente un gain tangible à l'échelle d'une opération (20 m² d'écosystème de référence pendant 50 ans), que les projets d'un hectare comptent leurs crédits par dizaines ou par centaines et non par centaines de milliers, et que les frais par crédit restent lisibles. Les retraits se comptent au centième. La taille est confirmée ou corrigée au lot 2 sur les cas du banc.

### C-X2
Catégorie : convention de transposition.
La période de crédit dure 50 ans à compter du premier mois des travaux, comme la période de référence d'OpenNAT 1 (C-T1, C-K3). Elle est garantie par une obligation réelle environnementale d'une durée au moins égale à la durée restante. Sources : PVN fixe une période de crédit de 10 à 50 ans et une analyse des risques de maintien sur au moins 50 ans (§3.10.1, §3.15) ; GSA, 30 à 50 ans pour le boisement (§3.1.9) ; VCS, longévité d'au moins 40 ans pour les projets à risque de non-permanence (§3.2.12) ; BNG, 30 ans de maintien ; A2024, agrément d'au moins 30 ans ; ORE, durée pouvant aller jusqu'à 99 ans. Les 50 ans sont le haut de la pratique et l'horizon déjà calculé par OpenNAT.

## Éligibilité

### C-X3
Catégorie : convention de transposition.
Pas de surface minimale. A2024 n'en fixe pas pour les sites agréés ; les frais fixes de validation et de vérification écartent d'eux-mêmes les projets trop petits pour être viables.

### C-X4
Catégorie : convention de transposition.
Le scénario de référence est l'évolution la plus probable du site sans le projet, calculée par le moteur comme une variante, sous le même climat et avec les mêmes tirages ; en cas d'usage incertain, l'hypothèse qui donne la valeur la plus forte est retenue. Il est arrêté à la validation et réexaminé tous les dix ans. Sources : PVN définit la référence comme l'usage le plus probable en l'absence du projet et la réévalue au moins tous les dix ans (§3.1.1, §3.1.2) ; VNF recalcule la référence à chaque vérification par des témoins appariés ou des taux de changement (§7.5) ; BCA, principe 6, demande des références prudentes exposées aux mêmes pressions ; BNG garde l'état initial statique. OpenNAT retient une référence modélisée et non des sites témoins, faute de réseau de témoins en France, et la rend prudente par la règle de l'hypothèse la plus favorable à la nature et par la succession de C-M2.

### C-X5
Catégorie : source muette.
Pas de crédit de perte évitée en version 1. Le scénario de référence ne prévoit jamais la destruction du site. Les crédits de perte évitée exigent une mesure de la menace (taux de conversion régional, pression foncière) qu'aucune source française ne fournit sous une forme partagée ; VNF ne les admet qu'avec des taux de changement mesurés.

### C-X6
Catégorie : convention de transposition.
Date de coupure de dix ans : un site dégradé dans les dix ans qui précèdent le dépôt est décrit par son état antérieur documenté. PVN exclut les zones dégradées volontairement dans les dix ans (§1.1.3) ; BCA, principe 5, interdit de dégrader pour créer de l'additionnalité ; BNG reprend l'habitat d'avant la dégradation ; OpenNAT 1 applique déjà la règle sur deux ans au permis (C-R5). La durée de PVN est retenue parce qu'un crédit, à la différence d'une attestation au permis, rémunère le gain.

### C-X7
Catégorie : convention de transposition.
Additionnalité financière par plan de financement ou par barrières, et démonstration renforcée en cas d'autres financements. Sources : VNF §5.9.1 et §5.9.2 ; PVN §3.7.1 à §3.7.5 ; BCA, principe 5. L'additionnalité réglementaire ne se déclare pas : elle se calcule par la variante d'obligations (C-X8).

### C-X8
Catégorie : source muette.
Chaque obligation se traduit, unité par unité, par la plus petite configuration conforme du plan masse du projet, en gardant ses types d'habitat ; une obligation exprimée en niveau de gain s'ajoute au scénario de référence. Le gain créditable se mesure au-dessus du plus grand des deux, tirage par tirage. Aucune source ne traite la soustraction d'obligations d'urbanisme d'un gain de biodiversité ; VNF et PVN exigent seulement que les activités créditées ne soient pas imposées par la loi. La règle fait entrer les objectifs de certification dans les obligations pour qu'un même gain ne soit pas à la fois exigé par une certification et vendu en crédits.

## Calcul

### C-X9
Catégorie : convention de transposition.
Le gain retenu est le 10e centile de la différence calculée tirage par tirage entre l'état projet et le seuil. VMR §2.4 exprime l'incertitude par l'intervalle de confiance à 90 % et impose une décote quand sa demi-largeur dépasse 10 % de la moyenne ; VNF recommande la borne prudente de l'intervalle à 90 % pour les valeurs de référence. Le 10e centile est la borne basse d'un intervalle unilatéral à 90 % : il applique la même exigence de confiance que Verra, sans formule de décote, directement sur les tirages que le moteur produit déjà (C-I2). Le calcul tirage par tirage fait disparaître l'incertitude commune aux trois états (valeurs d'habitat, facteurs de contexte), qui ne porte pas sur la différence.

### C-X19
Catégorie : source muette.
Dans les calculs de crédits (état projet prévu, variante d'obligations, états relevés), la difficulté de création ou d'amélioration de la convention C-T7 est neutralisée : D vaut 1. Dans OpenNAT 1, la difficulté multiplie la valeur cible d'un milieu créé pour exprimer son risque d'échec : c'est une espérance, adaptée à une attestation au permis. Pour les crédits, le risque d'échec est déjà porté par le constat avant émission (aucun crédit sans état relevé) et par la réserve (C-X11). Appliquer aussi la difficulté le compterait deux fois et rendrait inéligible toute restauration difficile, même réussie : sur l'exemple d'une culture restaurée en prairie de fauche (difficulté 0,33), le gain prévu devient négatif. Convention ajoutée au lot 2, après le premier calcul du moteur, retenue par Cédric PLANTAZ le 24/10/2026 ; soumise au conseil (décision DC10).

### C-X10
Catégorie : source muette.
Pour une opération de construction, Inat n'est pas déduit du gain créditable et il est publié avec chaque lot. Déduire Inat priverait de crédit toute opération : sur l'exemple de l'annexe C d'OpenNAT 1, Inat (141 843 m²HE·an) vaut plus de dix fois la valeur de tout le site intégrée sur 50 ans (I_0 = 13 277,1 m²HE·an), si bien qu'aucun gain sur la parcelle ne pourrait l'équilibrer. Ne pas le publier laisserait l'acheteur ignorer ce que l'opération consomme ailleurs. Le choix est soumis au conseil (décision DC3).

## Suivi et vérification

### C-X11
Catégorie : convention de transposition.
Réserve commune de 20 %, plus 5 points par facteur de risque élevé, plafonnée à 40 %, projet inéligible au-delà ; les inversions sont couvertes par la réserve et jamais reprises chez l'acheteur ; une inversion évitable oblige le porteur à reconstituer la réserve et bloque ses émissions. Sources : VNF, 20 % des crédits émis en réserve (§5.10.3) et annulation dans la réserve sans reprise des crédits émis (§5.10.4) ; PVN, 20 % pour les projets de restauration (§3.10.3) ; GSP, 20 % pour la séquestration (§11.1.1) ; VRT, note de risque par facteurs, plancher de 12 et échec au-delà de 60 (§2.5) ; VRI §5.3 et VCS v4.7 §3.2.22 à §3.2.27 pour la procédure d'inversion (signalement sous 30 jours, mise en attente, annulation, remplacement et blocage en cas d'inversion évitable). Le plancher suit les standards de biodiversité (20 %), la modulation suit la logique de Verra, et le plafond est plus bas que celui de Verra (40 au lieu de 60) parce que la réserve d'OpenNAT est commune et récente.

### C-X12
Catégorie : convention de transposition.
Relevés aux années 1, 3, 5, 10, 15, 20, 30, 40 et 50 depuis la fin des travaux de restauration ; revalidation tous les dix ans. Sources : BNG, calendriers locaux des plans de gestion et de suivi (par exemple années 1, 3, 5, 10, 15, 20, 25, 30, ou 2, 5, 10, 15, 20, 25, 30), source secondaire concordante ; VNF §5.2.5, PVN et BCA (principe 10), vérification au moins tous les cinq ans ; PVN, réévaluation de la référence et de l'additionnalité au moins tous les dix ans ; A2024, fréquence de suivi cohérente avec le temps de réponse des milieux. Le calendrier est serré au début, quand la maturation se joue et que les échecs se produisent, et suit la courbe de C-M1 ; il dépasse le minimum de cinq ans des standards jusqu'à l'année 20, puis l'espace à dix ans, quand les milieux sont mûrs. Une inversion de cette pratique est à surveiller : un écart de dix ans entre deux relevés laisse une perte non vue plus longtemps qu'en standard de marché, ce que compense la règle du score le plus faible (C-X14).

### C-X13
Catégorie : valeur de secours.
L'écologue qui relève le site est inscrit sur la liste du registre, n'a ni conçu ni réalisé le projet et n'a aucun lien d'intérêt avec le porteur. Règle d'indépendance usuelle des vérifications par tiers (BCA, principe 10), étendue à celui qui produit les données.

### C-X14
Catégorie : valeur de secours.
Entre deux relevés, chaque unité garde le plus faible des deux scores relevés ; une unité non relevée prend un score nul depuis le relevé précédent. Aucune source ne dit comment interpoler un état entre deux relevés. La règle du plus faible empêche de créditer une amélioration avant de l'avoir vue et fait porter au porteur le risque d'une dégradation intermédiaire non observée.

## Cession, retrait, versions

### C-X15
Catégorie : convention de transposition.
Un crédit se cède une fois, du porteur à l'acheteur, puis se retire ; il ne se revend pas en version 1. Transposition du régime des unités de compensation, de restauration et de renaturation (article D.163-1 du code de l'environnement : prestation de services, pas de revente), retenue par Cédric PLANTAZ le 24/10/2026 (décision D11 du lot 0) pour rester hors du régime des crypto-actifs et des instruments financiers tant que l'avis juridique n'est pas rendu.

### C-X16
Catégorie : convention de transposition.
Un gain n'est crédité qu'une fois : une parcelle ne porte qu'un projet actif ; les parcelles d'un site agréé sont exclues pendant l'agrément ; un gain crédité sur un autre registre est exclu. VNF §5.9.3 et PVN §3.7.5 interdisent le double comptage avec un autre programme.

### C-X17
Catégorie : convention de transposition.
Formule de contribution type, liste d'allégations interdites, publication des retraits par l'auteur d'une allégation et suspension du compte en cas d'abus. Sources : VNF interdit l'usage des crédits nature pour compenser des impacts attribuables (encadré 1), exige la publication des achats et retraits par l'utilisateur qui fait une allégation (§9.2.1), propose une formulation de contribution (§9.2.2) et prévoit l'arrêt du compte (§9.2.3) ; BCA, principes 2 et 4, distingue contribution et compensation ; directive (UE) 2024/825, applicable depuis le 27/09/2026, interdit les allégations génériques et les allégations de neutralité fondées sur la compensation.

### C-X18
Catégorie : convention de transposition.
Versions figées à la validation pour toute la période de crédit, sauf correction d'erreur par le conseil ou passage volontaire à la version en vigueur lors d'une revalidation ; aucune nouvelle version ne remet en cause des crédits émis. Pratique des programmes de Verra et de Plan Vivo pour les méthodologies, transposée à OpenNAT.
