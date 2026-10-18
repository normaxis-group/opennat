# Livraison du lot 0 : audit et état de l'art

**Date :** 17 octobre 2026
**Livrable :** `audit.md` (6 chapitres, 7 fiches de sources, environ 66 000 mots), les 5 fichiers de fiches de sources A à E dans `audit/fiches/` (101 fiches, repris de l'audit VIBCN), les fiches et le script d'assemblage dans `lot0/`, les fichiers sources dans `sources/` (environ 900 Mo, copies de travail non redistribuées).
**État :** lot terminé, rien n'a été codé, rien n'est publié. Arrêt et attente du go écrit avant le lot 1.
**Fusion :** à la demande de Cédric (17 octobre 2026), 3 éléments de l'audit parallèle de lot 0 « VIBCN » ont été intégrés à l'audit : la définition de Bnat calquée sur le coefficient de biotope par surface et la règle de construction de `sols.csv` (P12), la liste des 26 types urbains et hors-sol VB.1 à VB.26 (audit § 4.3) et les fiches de sources A à E (audit § 2.9 et `audit/fiches/`). Les passages modifiés portent la mention « (fusion VIBCN) » ; pour tout le reste, l'audit VINAT prévaut, y compris sur les 2 divergences relevées (licence du GBS, lecture de Carbone 4).

## Ce qui est fait

| Point du cahier des charges (§ 3) | État | Où |
|---|---|---|
| 1. OpenBCE lu, décrit en 20 lignes, liste du réutilisable | fait, dépôt public cloné et lu en entier (commit du 11/10/2026) | audit § 1.1, § 1.2 ; écarts imposés § 1.3 ; structure Th-BCE lue sur le PDF consolidé § 1.4 |
| 2. Inventaire des sources, une fiche par source | fait : 16 références du cahier des charges et une centaine de sources complémentaires, en 7 fiches, chaque valeur lue et localisée ; complété par 101 fiches de sources A à E en annexe | audit § 2.1 à 2.7 ; références non lues § 2.8 ; fiches A à E § 2.9 et `audit/fiches/` |
| 3. Couverture des 10 tables de données, trous listés | fait, avec taux estimés et trous nommés | audit § 3 |
| 4. Choix de nomenclature | fait : EUNIS 2012 niveau 3, liste de 26 types urbains et hors-sol VB.1 à VB.26, correspondances (EUNIS 2022, CORINE Biotopes, ZAN, sources de valeurs) | audit § 4, liste § 4.3 |
| 5. Points de méthode à trancher, un par un, avec recommandation | fait : 19 points, chacun avec sources, recommandation et valeur par défaut | audit § 5 |

Recette propre au lot 0 (le cahier des charges n'en fixe pas pour ce lot ; celle-ci est la mienne) :
- [x] Aucune valeur citée sans document, endroit précis et URL ; les valeurs non lues à la source sont marquées « NON VÉRIFIÉ » (48 mentions dans l'audit).
- [x] Les valeurs lues dans des sources secondaires sont signalées (Hesse via Lexaris, corroborée par un bilan officiel ; Drakare 2006 via 2 articles ; règlement (UE) 2024/1991 via un miroir et la note officielle wallonne).
- [x] Les licences de réutilisation de chaque source sont lues et reportées ; 3 sources exclues pour cause de licence (GBS, CBSh du CSTB, webservice INIES).
- [x] Aucun cadratin ni demi-cadratin dans les livrables, fiches A à E comprises (contrôle automatique) ; nombres en chiffres.
- [x] Le prototype en ligne du 16 octobre 2026 n'a pas été ouvert.
- [x] Aucune publication, aucun dépôt créé en ligne.

## Écarts par rapport au cahier des charges

1. Le dépôt OpenBCE était à demander à Cédric ; il est public (github.com/normaxis-group/openbce), il a été cloné et lu directement.
2. Le cahier des charges date l'étude Carbone 4 avec Altarea et Nexity de 2022 ou 2023 ; la publication est du 6 octobre 2026 (PDF daté du 7 octobre dans ses métadonnées). Le PDF, derrière un formulaire, a été fourni par Cédric le 17 octobre et lu en entier : la méthode est IMPACT World+ (PDF.m².yr) sur la plateforme Darwin, pas une méthode d'occupation des sols ; l'usage des sols n'y fait que 11 % de la biodiversité grise, ce qui ouvre le point P19 sur le périmètre des pressions du module G.
3. Le cahier des charges cite les « annexes techniques d'état » de la métrique anglaise ; le Technical Annex 1 est un classeur Excel (lu) et il n'existe pas de Technical Annex 2 propre à la métrique statutaire (Natural England annonce sa publication) : l'annexe 2 du Biodiversity Metric 4.0 (mars 2023) a été lue à la place, et ses tables sont identiques à celles du tableur statutaire pour les valeurs vérifiées.
4. Le cahier des charges cite un arrêté du 29 avril 2022 fixant les seuils de la nomenclature ZAN ; aucun arrêté de ce type n'a été trouvé : le décret 2022-763 renvoyait à un arrêté à venir, le Conseil d'État a annulé ce renvoi le 4 octobre 2023 et le décret 2023-1096 a inscrit les seuils dans l'annexe (50 m² bâti, 2 500 m² autres surfaces, 5 m linéaires, 25 % de couvert arboré).
5. Le lot 3 demande un utilitaire « sur le modèle de celui d'OpenBCE » ; OpenBCE n'a pas d'interface graphique (ligne de commande, API HTTP, serveur MCP) : point P17.
6. Le cahier des charges exige des données chargées depuis des CSV sourcés ; OpenBCE code ses tableaux en constantes Python : écart justifié au § 1.3 (A1), à conserver.
7. Legifrance, EUR-Lex et iso.org bloquent les accès automatisés depuis cet environnement ; les textes ont été lus sur codes.droit.org (données DILA), AIDA Ineris, le Conseil d'État, les portails ministériels, un miroir EUR-Lex et la note officielle wallonne, chaque cas étant indiqué dans les fiches.
8. Les serveurs de l'INPN sont hors service à la suite d'une attaque informatique ; HabRef v7 (07/08/2025) a été récupéré sur la page temporaire de PatriNat, sans licence lisible.

## Conventions ajoutées

Aucune convention Vi-BCN n'est écrite au lot 0 : c'est l'objet du lot 1. L'audit en annonce la liste minimale, issue des trous du § 3 et des points du § 5 : correspondance EUNIS vers codes allemands et UK ; rééchelonnage BKompV vers Hesse ; facteur d'état (P7) ; multiplicateurs de situation (P10) ; haies et arbres (P11) ; coefficients de sol de `sols.csv` par médiane des grilles publiées, seule convention de Bnat (P12) ; seuils et Mnat (P13) ; zone par département (P15) ; relation aire-espèces sous 1 ha ; perméabilité des clôtures ; voiries internes ; seuils de nuisances en coefficients ; relation infiltration et biodiversité ; délais des habitats méditerranéens ; inventaire d'occupation des sols par matériau (P8) ; temps de régénération ; plages d'incertitude par défaut (P18) ; tolérance de fermeture des surfaces.

## Questions ouvertes

1. P1 : qui édite la méthode et détient les droits du moteur (IRICE selon le cahier des charges ; recommandation NORMATYS). Attend une réponse.
2. P16 : version du référentiel Effinature de raccordement (v8.1 citée ; d'autres notes citent HOR v25.05 et une V9.1) et le fichier correspondant, nécessaire au lot 1.
3. Si un schéma XSD officiel du RSEE existe dans les archives des études RE2020 d'ARKEMEP, le joindre : il servira de modèle au XSD du RSNat.

Pour les 17 autres points du § 5, la recommandation est retenue par défaut si le go ne dit rien d'autre ; le point P12 (Bnat en coefficient de biotope par surface, repris de VIBCN) remplace la formule à 3 poids de la première version et mérite une relecture ; le point P19 (périmètre des pressions du module G : usage des sols et climat dans Inat, pollution en indicateur complémentaire) mérite un regard particulier parce qu'il élargit ce que le cahier des charges écrit du module G.

## Ce que le go déclenche

Lot 1 : rédaction de `methode/Vi-BCN_v1.md` sur la structure du § 4.1 du cahier des charges, construction de `donnees/` (une ligne par valeur, source, référence précise, URL, type, justification, incertitude), `methode/conventions.md`, `methode/bibliographie.md`, exemple de calcul complet déroulé à la main ; puis arrêt et attente du go.
