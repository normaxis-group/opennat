# OpenNAT, méthode de calcul du gain des sites France Crédits Biodiversité

Volet de la méthode OpenNAT Crédits, version 1, 24 octobre 2026. Éditeur : NORMATYS. Projet soumis à la validation du Biodiversity Standard Council. Texte sous licence CC BY 4.0.

## 1. Objet

Les sites naturels de compensation, de restauration et de renaturation, appelés depuis mai 2026 « sites France Crédits Biodiversité », sont agréés par le préfet de région pour 30 ans au moins (article L.163-1 A du code de l'environnement, décrets n° 2024-1052 et n° 2024-1053 du 21 novembre 2024, arrêté du 21 novembre 2024). Leurs unités de compensation, de restauration et de renaturation sont les seules à valoir mesure compensatoire. Le dossier d'agrément doit décrire l'état initial du site, les opérations prévues, le gain écologique attendu et son calendrier, le plan de gestion et le suivi. Les textes ne prescrivent aucune méthode de calcul du gain.

Ce volet propose OpenNAT comme cette méthode. Il dit comment OpenNAT produit les pièces chiffrées du dossier d'agrément et du suivi, et ce qu'il n'apporte pas. Il ne crée aucun crédit OpenNAT : les unités d'un site agréé restent régies par son agrément, et ses parcelles sont fermées aux crédits OpenNAT pendant l'agrément (convention C-X16).

## 2. Ce que les textes demandent et ce qu'OpenNAT fournit

| Exigence du dossier ou du suivi | Ce qu'OpenNAT fournit | Partie d'OpenNAT |
|---|---|---|
| État initial du site, réactualisé tous les quatre ans tant que l'agrément n'est pas délivré (arrêté du 21/11/2024, article 4) | unités d'habitat, types, scores d'état relevés selon des protocoles écrits, valeur de chaque unité en m²HE, avec ses pièces | OpenNAT 1, chapitres 4 et 7 ; partie 6 de l'édition complète |
| Gain écologique attendu des opérations | gain intégré sur la durée de l'agrément au-dessus du scénario de référence, unité par unité et pour le site | OpenNAT Crédits, chapitres 6 et 7 |
| Calendrier du gain | trajectoire annuelle de chaque unité : maturation, stress hydrique sous la TRACC, gestion | OpenNAT 1, modules T et W |
| Prudence de l'estimation | centiles 5, 10, 50 et 90 du gain par 1 000 tirages | OpenNAT 1, chapitre 9 ; OpenNAT Crédits, C-X9 |
| Plan de gestion | traduction du plan en facteurs de gestion, effet chiffré de son arrêt ou de sa prolongation | OpenNAT 1, convention C-M3 |
| Suivi, à une fréquence cohérente avec le temps de réponse des milieux (arrêté du 21/11/2024) | calendrier de relevés et règles de saisie des états relevés | OpenNAT Crédits, chapitre 8 |
| Rapport annuel au comité de suivi | recalcul avec les états relevés, écart à la trajectoire prévue | OpenNAT Crédits, formules (X5) et (X6) |
| Définition et nombre des unités vendues | gain en m²HE·an de chaque unité définie par l'opérateur (par exemple un hectare de site) | section 3 ci-dessous |

## 3. Unités du site et m²HE·an

L'opérateur du site définit ses unités : à La Tuile et aux Pradeaux, agréés le 15 octobre 2026, une unité est un hectare de site. OpenNAT ne change pas cette définition. Il calcule, pour chaque unité, le gain qu'elle porte en m²HE·an au 10e centile, au-dessus du scénario de référence, sur la durée de l'agrément :

g_unité = 10e centile, tirage par tirage, de [ I_proj(0..D) - I_ref(0..D) ] restreint aux unités d'habitat de l'unité de vente, avec D la durée de l'agrément en années.

Ce chiffre sert à trois choses :

- comparer des unités de sites différents, ou de parties différentes d'un même site, sur une même échelle ;
- justifier un prix différencié par unité devant les acheteurs ;
- aider le maître d'ouvrage et le service instructeur à apprécier si les unités achetées suffisent à compenser une perte calculée, elle aussi, par OpenNAT (Cnat de l'opération qui compense).

## 4. Ce qu'OpenNAT n'apporte pas

- L'équivalence écologique entre la perte et le gain (mêmes espèces, mêmes fonctions) : OpenNAT mesure une valeur d'habitat agrégée, il ne dit pas si une prairie restaurée compense la perte d'un habitat d'espèce protégée. Le service instructeur l'apprécie.
- La proximité fonctionnelle : OpenNAT ne la calcule pas ; il situe le site dans la trame verte et bleue, ce qui l'éclaire.
- L'avis du conseil scientifique régional du patrimoine naturel ou du Conseil national de la protection de la nature.
- La décision d'agrément, qui appartient au préfet de région.

## 5. Mode d'emploi pour un opérateur de site

- Décrire l'état initial dans un fichier projet OpenNAT, avec les relevés de la partie 6 de l'édition complète.
- Saisir l'état visé, les opérations, le calendrier des travaux et le plan de gestion sur la durée de l'agrément.
- Saisir le scénario de référence selon le chapitre 6 d'OpenNAT Crédits.
- Lancer le calcul : trajectoires, gain par unité de vente, centiles, rapport du moteur, RSNat.
- Joindre au dossier d'agrément le rapport du moteur et le RSNat, avec la mention de la version de la méthode et l'empreinte de contrôle.
- Chaque année, relever le site, recalculer avec les états relevés et joindre l'écart à la trajectoire au rapport annuel.

L'opérateur peut demander au registre des crédits OpenNAT d'inscrire ses unités et son registre des ventes, avec ancrage des empreintes sur la chaîne de blocs. Cette inscription est un service de publicité : elle ne transforme pas les unités en crédits OpenNAT, ne permet pas leur revente et reste soumise à l'avis juridique demandé au lot 0.

## 6. Présentation aux services de l'État

Après la validation par le Biodiversity Standard Council, et sur décision de NORMATYS, ce volet est présenté aux DREAL et aux opérateurs de sites agréés ou candidats. Il n'a de valeur pour un dossier d'agrément que si le service instructeur l'accepte, dossier par dossier.
