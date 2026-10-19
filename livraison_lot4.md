# Livraison du lot 4 : banc de validation et documentation

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne.
**Versions :** méthode OpenNAT 1 (révision du 19/10/2026), données 1.2.1, moteur 0.2.0.
**État :** lot livré, rien n'est publié. Dernier lot du cahier des charges ; arrêt et attente du go écrit.

## Ce qui est fait

| Exigence du cahier des charges (§ 7) | Réalisation |
|---|---|
| Au moins huit cas tests couvrant les situations types | Les huit situations du § 7 (cas 1 à 6, 7a à 7c, 8a à 8c) et l'exemple de l'annexe C, plus 60 cas complémentaires et dynamiques : 73 cas (`banc/README.md`) |
| Pour chaque cas : fichier d'entrée, calcul de référence indépendant, résultats attendus, tolérance | Fichier projet (`banc/cas/`) ; carnet de référence `outils/carnet_reference.py`, sans aucun code partagé avec le moteur, déroulé dans la partie 8 de l'édition ; résultats attendus `banc/attendus.json` (indicateurs, valeur et trajectoire de chaque unité) ; tolérance de 0,1 % ou 0,05 en absolu ; résultat attendu qualitatif de chaque situation vérifié par un test |
| Tests unitaires par module | 24 cas élémentaires des fiches (`tests/test_modules.py`), chargeur des tables, recherche des constantes dans le code |
| Tests de non-régression | `banc/regression.py` fige 38 930 grandeurs : toutes les sorties numériques de toutes les étapes des 73 cas et une analyse d'incertitude de 200 tirages à deux variantes ; tolérance 10⁻⁶ ; l'empreinte des tables y est liée au journal des versions |
| Tests de propriétés | 20 tests (`tests/test_proprietes.py`) : pleine terre, état initial et état projet, durée du chantier, réservoir, éclairage, plan de gestion, épaisseur de substrat, mois de destruction, protection d'un arbre conservé, linéarité des GES et des matériaux, bois justifié, identités des indicateurs, ordre et noms des unités, découpage d'une unité, écart nul entre variantes identiques sur chaque tirage, plan de gestion vérifié sur chaque tirage |
| Contrôle d'ordre de grandeur du module G face à l'étude Carbone 4, avec explication des écarts | Note « Contrôle d'ordre de grandeur du module G face à l'étude Carbone 4 » (4 pages) et `python -m banc.carbone4` ; section ajoutée à la partie 8 de la méthode |
| Guide utilisateur | « OpenNAT, guide utilisateur » (6 pages) |
| Guide du contributeur (proposer une valeur avec sa source) | « OpenNAT, guide du contributeur » (5 pages) : format des lignes, types de valeur, licences, tables à la main ou construites, marche à suivre en sept étapes, modèle de proposition |
| Journal des versions de la méthode et des données | « OpenNAT, journal des versions » (`JOURNAL_DES_VERSIONS.md`) : six révisions de la méthode, six versions des données avec leur empreinte, deux versions du moteur |
| E12 : unités cohérentes, contrôle dimensionnel automatique | `opennat/dimensions.py` : 81 unités traduites en dimensions (longueur, masse, temps, température, habitat équivalent), 45 équations des fiches vérifiées à partir des unités inscrites dans les tables, unités du RSNat ; appelé par `python -m opennat controle` et par les tests |

Les quatre documents sont dans `livraison/` en Word et en PDF, au papier NORMATYS (Calibri 10, langue française, pagination « Page X sur Y »), rendus par LibreOffice et regardés page par page.

## Recette du lot 4 (§ 9)

- [x] Les huit cas tests passent : les 13 fichiers des huit situations et de l'annexe C retrouvent le carnet de référence à 0,1 %, ainsi que les 60 autres cas.
- [x] Les tests de propriétés passent : 20 sur 20, chacun avec un effet réel sur l'exemple (de 9 à 3 442 m²HE·an).
- [x] L'écart avec l'ordre de grandeur Carbone 4 est expliqué : au périmètre commun (climat et usage des sols, phases A1-A3, par m² de plancher), OpenNAT 54 m²HE·an contre 44 PDF.m².yr, rapport 1,0 à 1,5 ; la pollution (moitié du résultat de Carbone 4) n'est pas dans Inat (P19) ; le bois est pénalisé plusieurs fois plus fort (C-G4, C-G5, C-G7).
- [x] Les guides utilisateur et contributeur sont rédigés.

## Ce que le contrôle dimensionnel a trouvé

Une incohérence, corrigée : le facteur de caractérisation du climat était étiqueté « m²HE par kg CO2 éq. et par an ». Avec cette unité, Inat_clim = CF × S_ref × GES × durée sortirait en m²HE et non en m²HE·an. L'unité juste est « m²HE par kg CO2 éq. », perdus chaque année tant que le réchauffement persiste. La valeur ne change pas, aucun résultat non plus (instantané de non-régression identique hors empreinte) ; l'étiquette est corrigée dans la table (données 1.2.1), le texte de la méthode, la fiche A33, les conventions et le RSNat.

## Tests

`python -m pytest` : 142 tests, tous passent (8 min 30 s), dont 73 cas du banc, la non-régression, 20 tests de propriétés et le contrôle dimensionnel.

## Écarts et points ouverts

1. Le contrôle Carbone 4 repose sur des hypothèses OpenNAT déclarées (émissions A1-A3, granulats, bois), Carbone 4 ne publiant ni son empreinte carbone ni ses métrés ; les deux métriques sont rapprochées à 1 pour 1 faute de conversion publiée.
2. Les seuils d'Inat et de Snat ne devraient pas être fixés avant le traitement de la pollution (P19).
3. Le bois reste le premier point à soumettre au Biodiversity Standard Council (C-G4, C-G5, C-G7).
4. La gouvernance des contributions décrite dans le guide (décision de l'éditeur, conventions et seuils au Biodiversity Standard Council) est une proposition à confirmer.

## Ce que le go déclenche

Le cahier des charges s'arrête au lot 4. La suite est à décider : soumission de la méthode au Biodiversity Standard Council, licence entre NORMATYS et IRICE, recalibrage du bois, traitement de la pollution, relecture par un écologue, puis publication du dépôt.
