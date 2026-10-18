# Livraison du lot 1 : méthode OpenNAT v1 et tables de données

**Date :** 18 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne. Commits du lot : tables de données, texte de la méthode.
**État :** lot livré dans sa version noyau, rien n'est publié. Arrêt et attente du go écrit avant la suite.

## Ce qui est fait

| Livrable (cahier des charges, § 4) | Fichier | État |
|---|---|---|
| Texte de la méthode, structure de l'annexe Th-BCE, 12 chapitres | `methode/OpenNAT_v1.md` ; version Word au papier NORMATYS pour le Biodiversity Standard Council : `livraison/Méthode de calcul OpenNAT v1.docx` (19 pages) et son PDF | fait |
| Tables de coefficients, une ligne par valeur, source, référence précise, URL, type, justification, plage d'incertitude | `donnees/*.csv` : 1 398 valeurs dans 9 tables, plus la nomenclature (191 types) et l'index des conventions | fait |
| Conventions numérotées et justifiées | `methode/conventions.md` (42 conventions, familles H, S, E, C, N, T, G, I, B, P) et `donnees/conventions.csv` | fait |
| Bibliographie | `methode/bibliographie.md` | fait |
| Exemple de calcul complet déroulé à la main | annexe C du texte, vérifié par `outils/verifier_exemple.py` | fait |

Outils livrés avec les tables : `outils/construire_habitats.py` (lit la BKompV et le tableur anglais, aucune valeur saisie), `outils/construire_sols.py` (médiane des grilles relevées), `outils/controle_donnees.py` (refuse toute ligne sans source, sans référence ou hors de sa plage, et écrit `donnees/rapport_couverture.md`), `outils/methode_docx.py` (version Word au gabarit).

## Recette du lot 1

- [x] Le texte de méthode contient les douze chapitres du § 4.1.
- [x] Chaque équation est numérotée (1, 2, S1 à S4, H1 à H5, C1 à C3, N1, E1, T1 à T7, G1 à G6, A1 à A4, I1, I2) et ses unités sont données ; le contrôle dimensionnel automatique viendra avec le moteur (exigence E12).
- [x] Chaque ligne de `donnees/` a une source ou une convention : contrôle automatique sans défaut.
- [x] Le rapport de couverture indique la part de valeurs sourcées : 96 % de valeurs primaires ou transposées d'une source primaire, 1 % secondaires, 4 % conventions. Le chiffre est flatteur : 1 216 lignes viennent de la seule table des habitats. Les conventions sont peu nombreuses en lignes mais portent les modules les moins documentés (connectivité, nuisances, eau, temps).
- [x] L'exemple de calcul complet est déroulé à la main (annexe C).

## Ce que le calcul de l'exemple montre

Sur une résidence de 1 400 m² de S_ref bâtie sur une friche de 2 000 m², Cnat vaut 672 m²HE·an, alors que Inat vaut 141 843 m²HE·an : 60 % par le climat, 39 % par le bois d'origine non justifiée. La biodiversité grise pèse 200 fois la perte du site, et dix fois la valeur intégrée du site entier sur 50 ans. Avec le climat dans Inat (décision du 18/10, point P19), Snat devient presque un indicateur des matériaux. La méthode juge donc le site et les matériaux séparément, comme la RE2020 sépare le Cep et l'Ic construction : seuils sur Bnat et Cnat, pas de seuil sur Snat.

## Écarts par rapport au cahier des charges et à l'audit

1. Nom : la méthode et le moteur s'appellent OpenNAT (décision du 18/10/2026). L'audit garde son nom de travail, Vi-BCN.
2. Format des tables : une ligne par valeur, 13 colonnes communes à toutes les tables. Le cahier des charges en prévoyait 7. Les colonnes ajoutées sont `cle`, `parametre`, `incertitude_min`, `incertitude_max`, `licence` et `convention`.
3. Données d'entrée calquées sur la RE2020 (demande de Cédric du 18/10) : le chapitre 4 reprend du RSEE la parcelle, l'emprise, la durée du chantier, la S_ref et les 36 indicateurs d'ACV par phase. Seuls 6 RSEE d'ARKEMEP sur 228 portent la branche RSEnv qui contient ces données. L'ordre des codes 101 à 136 est déduit de la liste de l'annexe II, puis contrôlé sur un RSEE réel (les totaux d'énergie se retrouvent) : aucun texte publié ne le donne.
4. Attestation au permis de construire et fichier XML (demande de Cédric du 18/10) : chapitre 11 et convention C-P1. Le schéma XSD du RSNat sera écrit avec le moteur (lot 2).
5. Seuils raccordés à Effinature 8.1 (critère SOL 01.2.5) par transposition du CBSh à Bnat. Les coefficients de Bnat ne sont pas ceux du CBSh, exclus pour leur licence : l'écart sera mesuré au banc.
6. Grilles de coefficient de biotope : six retenues (Berlin, Londres, Strasbourg, Grand Annecy, Paris, Lille) et relues à la source. Montreuil et le SDAGE Seine-Normandie, cités par l'audit, ne sont pas retenus faute de relecture.
7. Inventaire d'occupation des sols des matériaux : seuls le bois et les granulats sont couverts, et les usines sont négligées (convention C-G7). C'est le principal écart connu.
8. Table d'aide de la zone biogéographique par département : elle demande un croisement de couches cartographiques, prévu avec le moteur.
9. Les sources téléchargées pendant le lot 0 (900 Mo) n'étaient pas sur ce poste. Les sources utiles au lot 1 ont été retéléchargées et relues dans `sources/`, hors dépôt.

## Sources secondaires restantes

Matthews 2016 (exposant aire-espèces, dépôt universitaire refusé), Azam 2018 et Rowse 2018 (éclairage), Reijnen 1997 (bruit), quatre dossiers de carrières, mémento FCBA. Elles sont marquées « secondaire » dans les tables, à remplacer par la lecture de la source primaire.

## Volume de la méthode

Cédric demande que la méthode atteigne au moins le volume de l'annexe III de la RE2020 (1 854 pages dans sa version consolidée du 21/07/2026). La version noyau livrée ici fait 19 pages. Le volume de l'annexe III vient de sa structure : des fiches algorithmes par composant, des données conventionnelles imprimées en entier et des fiches d'application. Une édition complète d'OpenNAT construite sur le même plan atteindrait 1 400 à 1 500 pages de contenu réel :

| Partie | Contenu | Pages estimées |
|---|---|---|
| Généralités | chapitres 1 à 6 actuels, développés | 30 |
| Données conventionnelles | les 1 398 valeurs imprimées avec leur source, la nomenclature | 160 |
| Fiches algorithmes au format Th-BCE (variables avec nom, description, unité, plage, valeur conventionnelle, puis équations) | une fiche par étape, module et sous-module, soit environ 35 fiches | 280 |
| Fiches habitats | une fiche par type (191) : reconnaissance, correspondances EUNIS, CORINE et HabRef, valeur et stades, délais, difficulté, grille d'état, espèces indicatrices tirées de HabRef | 550 |
| Fiches d'application | réhabilitation, opérations d'ensemble et lots, phasage, toitures, façades, sols reconstitués, mares, arbres, haies, friches, sols pollués, espèces protégées, variantes | 100 |
| Protocoles de relevé des grilles d'état, listes d'espèces exotiques envahissantes | 11 grilles | 120 |
| Dictionnaire du RSNat et schéma XSD | chaque élément du fichier | 80 |
| Cas de validation déroulés | les 8 cas du lot 4 | 120 |

Une grande partie se génère depuis `donnees/` et HabRef, comme les tableaux de l'annexe III. Au-delà de ce plan, ajouter des pages reviendrait à faire du remplissage, ce qui desservirait la méthode devant le Biodiversity Standard Council.

## Questions ouvertes

Posées une par une à Cédric, dans cet ordre :
1. Édition complète : la produire maintenant (lot 1 bis, avant le moteur) ou après le moteur ? Recommandation : maintenant, parce que les fiches algorithmes au format Th-BCE servent aussi de spécification au moteur, comme les specs écrites avant chaque lot d'OpenBCE.
2. Licence de la convention NORMATYS-IRICE : la licence exclusive prévue doit laisser publier la méthode sous CC BY 4.0 et le moteur sous AGPL.
3. Relecture par un écologue (IRICE) de la nomenclature et des 191 correspondances BKompV, une par une.

## Ce que le go déclenche

Selon la réponse à la question 1 : le lot 1 bis (édition complète sur le plan ci-dessus), ou le lot 2 (moteur : un module de code par module de méthode, chargeur des tables, journal des calculs, Monte-Carlo, RSNat et son XSD, ligne de commande).
