# Cahier des charges : OpenNat, méthode de calcul Vi-BCN v1 et utilitaire de calcul

**Pour :** Claude Code (session Fable 5.1)
**De :** Claude, pour Cédric Plantaz, président de NORMAXIS
**Date :** 16 octobre 2026
**Règle d'or :** aucune valeur sans source. Chaque coefficient du moteur porte sa référence bibliographique (auteur, année, tableau ou page, URL) ou, à défaut, une convention Vi-BCN numérotée et justifiée par écrit. Chaque lot s'arrête à sa livraison et attend le go écrit de Cédric. Rien n'est publié (dépôt public, site, annonce) sans ce go.

---

## 0. Objet et esprit

OpenNat est à la biodiversité ce qu'OpenBCE est à l'énergie : une **méthode de calcul conventionnelle, publique et opposable**, et un **moteur open source** qui l'exécute. La méthode s'appelle **Vi-BCN**. Elle est éditée par IRICE, soumise à la validation du **Biodiversity Standard Council**, et sert de base aux exigences de la certification **Effinature**.

Ce que la méthode calcule :

| Indicateur | Équivalent RE2020 | Définition | Unité |
|---|---|---|---|
| **Cnat** | Cep | Consommation de nature sur site : perte de valeur écologique entre l'état initial et l'état projet, intégrée sur la période de référence | m²HE·an, et m²HE moyen |
| **Inat** | Ic construction | Biodiversité grise : impact des matériaux et du chantier sur les écosystèmes, sur tout le cycle de vie | m²HE·an |
| **Snat** | Ic bâtiment | Solde de nature : −(Cnat + Inat). Positif si le projet restaure plus qu'il ne consomme | m²HE·an |
| **Bnat** | Bbio | Besoin de nature lié à la conception (plan masse, emprise, pleine terre, continuités), indépendamment des aménagements paysagers | points, sans unité |

**Unité de base : le m² d'habitat équivalent (m²HE).** Un m²HE est un m² d'écosystème de référence en pleine intégrité. Un m² d'habitat réel vaut entre 0 et 1 m²HE (au-delà de 1 seulement si un multiplicateur de contexte le justifie). Le temps est pris en compte en intégrant les valeurs annuelles sur une **période de référence de 50 ans**, comme l'ACV de la RE2020, ce qui rend le site et les matériaux additionnables dans la même unité (m²HE·an).

**Pourquoi le calcul n'est pas instantané :** comme la Th-BCE, Vi-BCN enchaîne des calculs intermédiaires. Il y a un prétraitement des surfaces, puis sept modules calculés dans un ordre imposé, une simulation annuelle sur 50 ans de chaque habitat, et une analyse d'incertitude par tirages aléatoires. Chaque étape produit des sorties intermédiaires conservées et consultables.

**Cible utilisateur :** l'écologue et le chargé QEB. L'utilitaire est **simple** : saisir, lancer, suivre les étapes, lire les résultats, éditer la fiche standardisée. Ce n'est pas une plateforme SaaS.

---

## 1. Références à lire avant de commencer

| Référence | Où | Ce qu'elle fixe |
|---|---|---|
| Ce cahier des charges | ce fichier | Périmètre, lots, exigences, recette |
| Dépôt et documentation d'OpenBCE | à demander à Cédric (dépôt du groupe) | **Architecture à reproduire** : langage, structure du moteur, format pivot, tests, journal des calculs, sorties RSEE. OpenNat doit en être le jumeau technique |
| Méthode Th-BCE 2020 (annexe à l'arrêté du 4 août 2021) | legifrance.gouv.fr, rt-re-batiment.developpement-durable.gouv.fr | **Structure documentaire à reproduire** : conventions, données d'entrée, algorithmes par module, sorties, seuils, coefficients de modulation |
| Format RSEE (XSD) | rt-re-batiment.developpement-durable.gouv.fr | Modèle du récapitulatif standardisé RSNat |
| Carbone 4, « La biodiversité grise dans le bâtiment » (avec Altarea, Nexity, Darwin Data) | carbone4.com | Approche de la biodiversité grise, ordres de grandeur de contrôle |
| Statutory Biodiversity Metric (Royaume-Uni, 2024) : guide utilisateur, outil de calcul, annexes techniques d'état | gov.uk (Defra, Natural England) | Architecture surface × distinctivité × état × importance stratégique, multiplicateurs temporels (3,5 %/an) et de difficulté, règles de calcul des haies, arbres urbains |
| Bundeskompensationsverordnung 2020, Anlage 1 (Biotopwertliste) et méthodes des Länder (Hessen, Bayern, NRW) | gesetze-im-internet.de, sites des Länder | Valeurs de biotopes réglementaires (0 à 24 points), y compris milieux urbains |
| GLOBIO 4 (Schipper et al. 2020, Global Change Biology) et Alkemade et al. 2009 | revues, globio.info | Valeurs MSA par usage des sols et relations pression-réponse (fragmentation, infrastructures, azote, climat) |
| Global Biodiversity Score (CDC Biodiversité) | documentation technique publique | Calcul en MSA·km², intensités par matière première |
| LC-IMPACT (Verones et al. 2020), Chaudhary et al. 2015, ReCiPe 2016 (RIVM), EF 3.1 (JRC, indicateur LANCA) | sites officiels, revues | Facteurs de caractérisation occupation et transformation des sols |
| EN 15804+A2 et base INIES | base-inies.fr | Indicateur « utilisation des sols » des FDES, structure des quantités par lot |
| Nomenclature de l'artificialisation (décret ZAN et ses révisions) | legifrance.gouv.fr | Définition des surfaces artificialisées, imperméabilisées, végétalisées |
| Coefficient de biotope (Berlin BAF, PLU français), Urban Greening Factor (London Plan G5) | sites officiels | Points de comparaison et d'étalonnage |
| Typologies d'habitats : EUNIS, CORINE Biotopes, HabRef (INPN) | inpn.mnhn.fr, eea.europa.eu | Nomenclature des habitats saisis |
| Référentiel Effinature v8.1 | à demander à Cédric | Niveaux de certification auxquels les seuils Vi-BCN doivent se raccorder |

Si une référence n'est pas accessible depuis ton environnement, demande-la à Cédric en fichier. Ne la reconstitue jamais de mémoire. Une valeur lue dans une source secondaire est signalée comme telle et remplacée par la source primaire dès que possible.

**Ne pas réutiliser** le prototype en ligne « OpenNat » publié le 16 octobre 2026 : ses coefficients sont des valeurs de travail sans source, et son modèle est trop simple. Il est hors périmètre.

---

## 2. Ce qu'on fait et ce qu'on ne fait pas

**On fait :**
- la **méthode Vi-BCN v1**, document complet sur le modèle de l'annexe Th-BCE, avec ses tables de données sourcées ;
- le **moteur de calcul** open source qui exécute la méthode, module par module, avec sorties intermédiaires ;
- le **format d'entrée** (fichier projet) et le **récapitulatif standardisé RSNat**, avec leurs schémas ;
- un **utilitaire simple** : saisie, lancement du calcul, suivi des étapes, résultats, édition de la fiche standardisée ;
- un **banc de validation** public : cas tests de référence, résultats attendus, tests de non-régression ;
- la **documentation** de contribution open source.

**On ne fait pas, dans cette phase :**
- de comptes utilisateurs, de base de projets en ligne, de facturation ;
- d'import de maquette BIM ou de géométrie SIG : la saisie est tabulaire. **Mais** le format d'entrée prévoit dès maintenant les champs d'identifiant géométrique, pour un import futur sans refonte ;
- de seuils Effinature définitifs : les seuils sont **proposés** et marqués « en attente de validation du Biodiversity Standard Council » ;
- de publication du dépôt, de nom de domaine ou d'annonce : **décision de Cédric** ;
- de lien avec le CSTB ou ses outils.

---

## 3. Lot 0 : audit et état de l'art, sans rien coder

Livrable : `audit.md`, puis arrêt et attente du go.

1. **OpenBCE.** Lis le dépôt OpenBCE. Décris en vingt lignes maximum : langage, structure des modules, format pivot, gestion des données de référence, journal des calculs, tests, génération du RSEE, licence. Liste ce qui est **réutilisable tel quel** dans OpenNat.
2. **Inventaire des sources.** Pour chaque référence du § 1 et toute autre source pertinente trouvée, une fiche : objet, valeurs disponibles, licence de réutilisation, limites. Tu cherches large : publications scientifiques, méthodes réglementaires européennes, documentation des bases de données, rapports d'organismes publics.
3. **Couverture des besoins en valeurs.** Pour chaque table de données listée au § 5.3, indique la source pressentie et le taux de couverture (valeurs trouvées / valeurs nécessaires). Liste explicitement les **trous** qui imposeront une convention Vi-BCN.
4. **Choix de nomenclature d'habitats.** Proposition argumentée (EUNIS niveau 3 recommandé, avec correspondance CORINE et une extension pour les milieux urbains et bâtis).
5. **Points de méthode à trancher**, présentés **un par un**, chacun avec ta recommandation : par exemple, l'échelle de valeur (MSA ou points de biotopes rapportés à 1), le taux d'actualisation, la période de référence, le traitement du bois certifié.

**Arrêt.** Tu attends le go écrit de Cédric sur l'audit avant le lot 1.

---

## 4. Lot 1 : méthode Vi-BCN v1 (document)

Livrables :
- `methode/Vi-BCN_v1.md` : le texte de la méthode, rédigé en français, structuré comme l'annexe Th-BCE ;
- `donnees/` : toutes les tables de coefficients en CSV, une ligne par valeur, avec les colonnes `valeur`, `unite`, `source`, `reference_precise` (tableau, page), `url`, `type` (source primaire, source secondaire, convention) et `justification` pour les conventions ;
- `methode/conventions.md` : la liste numérotée des conventions Vi-BCN (C1, C2…), chacune justifiée ;
- `methode/bibliographie.md`.

### 4.1 Structure imposée du texte de méthode

1. Objet, domaine d'application (bâtiments neufs, réhabilitations lourdes, aménagements), exclusions
2. Termes, définitions, symboles et unités
3. Principes : unité m²HE, période de référence, intégration temporelle, frontières du système (parcelle, hors-sol, amont des matériaux)
4. Données d'entrée : liste exhaustive, unités, valeurs par défaut, règles de saisie
5. Conventions de contexte : zones biogéographiques (atlantique, continentale, méditerranéenne, alpine), situation vis-à-vis de la trame verte et bleue, typologie d'opération
6. Algorithme général : ordre des étapes et des modules, schéma des flux de données
7. Un chapitre **par module** (§ 4.2), chacun avec : objet, entrées, paramètres conventionnels, algorithme pas à pas avec équations numérotées, sorties intermédiaires, cas limites
8. Agrégation et calcul des indicateurs
9. Analyse d'incertitude
10. Seuils proposés et coefficients de modulation (Mnat)
11. Récapitulatif standardisé RSNat
12. Annexes : tables de coefficients, correspondances de nomenclatures, exemples de calcul complets

### 4.2 Les étapes et modules de calcul

L'ordre est imposé. Chaque étape lit les sorties des précédentes.

**Étape E1 : contexte et conventions.** Détermination de la zone biogéographique, des multiplicateurs de situation (réservoir de biodiversité, corridor, hors trame), de la typologie et des coefficients de modulation.

**Étape E2 : prétraitement des surfaces.**
- Découpage du site en unités d'habitat, à l'état initial et à l'état projet.
- Contrôle de fermeture : la somme des surfaces au sol égale la surface de la parcelle (tolérance à fixer).
- Classement de chaque unité : au sol en pleine terre, au sol sur dalle, hors-sol (toiture, façade).
- Correspondance de chaque habitat avec la nomenclature de référence.

**Module S, sol.**
- Surfaces imperméabilisées, perméables, en pleine terre, sur dalle (avec épaisseur de substrat).
- Coefficient de fonctionnalité du sol par unité, selon la nature et l'épaisseur.
- Sorties : taux de pleine terre, surface imperméabilisée nette créée, coefficient de sol par unité.

**Module H, habitats.**
- Valeur intrinsèque de chaque habitat (distinctivité, rapportée à l'échelle 0 à 1).
- **État écologique calculé** à partir d'une grille de critères observables par habitat (comme les fiches d'état anglaises), et non d'un choix direct « bon / moyen / dégradé ».
- Valeur de l'unité = surface × valeur intrinsèque × état × coefficient de sol × multiplicateur de situation.

**Module C, connectivité.**
- Regroupement des unités végétalisées contiguës en taches (selon la contiguïté déclarée).
- Effet de taille des taches, fondé sur une relation aire-espèces sourcée.
- Connexion aux réservoirs et corridors (distance, nature des obstacles).
- Effet des clôtures et des voiries internes.
- Sortie : coefficient de connectivité par tache.

**Module N, nuisances.**
- Lumière artificielle : par zone, éclairement, température de couleur, durée et horaires d'extinction. Relation pression-réponse sourcée.
- Bruit : niveau sonore par zone.
- Collisions avec les vitrages : surfaces vitrées exposées, traitement anti-collision.
- Sortie : coefficient de nuisance par unité d'habitat.

**Module E, eau.**
- Part des eaux pluviales infiltrées ou gérées à ciel ouvert, milieux humides créés ou détruits.
- Sortie : coefficient hydrique et valeur des milieux humides.

**Module T, temps (simulation annuelle).**
C'est l'équivalent du calcul pas à pas de la Th-BCE.
- Pour **chaque unité d'habitat**, simulation **année par année sur 50 ans** :
  - phase chantier (durée saisie) : destruction temporaire, valeur nulle ou réduite ;
  - habitats conservés : valeur constante, diminuée si les mesures de protection en chantier sont absentes ;
  - habitats créés ou restaurés : **courbe de maturation** jusqu'à la valeur cible en un délai propre à chaque habitat (délais sourcés), avec un multiplicateur de difficulté (risque d'échec) ;
  - remplacements et renouvellements prévus (par exemple une toiture végétalisée refaite).
- Actualisation, si le lot 0 la retient (taux de référence de la métrique anglaise : 3,5 %/an, à confirmer ou écarter par convention).
- Sorties : trajectoire annuelle de chaque unité et du site, valeur intégrée en m²HE·an, **dette de maturité**.

**Module G, biodiversité grise.**
- Quantités par matériau, structurées par lot comme dans la RE2020 (lots 1 à 13), reprises de l'ACV du projet.
- Pour chaque matériau : occupation et transformation des sols par unité de matériau (m²·an par kg ou par m³), puis conversion en m²HE·an par facteur de caractérisation sourcé.
- Phases du cycle de vie : production (A1-A3), transport (A4), chantier (A5), remplacements (B4), fin de vie (C).
- Traitement du bois selon l'origine et la certification de gestion forestière.
- Sorties : impact par matériau, par lot et par phase.

**Étape E3 : agrégation.**
- Cnat = Σ sur 50 ans (valeur initiale maintenue − valeur projet de l'année).
- Inat = Σ des impacts du module G.
- Snat = −(Cnat + Inat).
- Ratios : Cnat par m² de parcelle, Inat par m² de surface de plancher.
- Bnat : score de conception calculé sur les seules données de plan masse (emprise, pleine terre, continuités).
- Indicateurs complémentaires : coefficient de biotope recalculé, taux de pleine terre, part d'espèces indigènes, part de surfaces éclairées.

**Étape E4 : incertitude.**
- Chaque coefficient porte une plage d'incertitude (dans les tables de données).
- Simulation Monte-Carlo (au moins 1000 tirages, paramétrable) sur l'ensemble de la chaîne.
- Sorties : valeur centrale, intervalle à 90 %, et les cinq paramètres qui pèsent le plus dans le résultat.

**Étape E5 : vérification de conformité.** Comparaison des indicateurs aux seuils proposés, modulés par les coefficients Mnat (typologie, zone, taille de parcelle). Niveau Effinature atteint.

### 4.3 Exigences sur le texte

- Chaque équation est numérotée, avec ses symboles définis et ses unités vérifiées.
- Chaque coefficient renvoie à sa ligne dans `donnees/`.
- Un **exemple de calcul complet**, déroulé à la main étape par étape, en annexe.
- Chaque convention est signalée dans le texte par son numéro (C1, C2…).

**Arrêt.** Livraison du texte et des tables, puis attente du go de Cédric. C'est cette version qui part devant le Biodiversity Standard Council.

---

## 5. Lot 2 : moteur de calcul

Livrable : le moteur, dans la même architecture qu'OpenBCE (même langage, même découpage, mêmes conventions de code, sauf écart justifié dans l'audit).

### 5.1 Exigences

- **Un module de code par module de méthode** (E1, E2, S, H, C, N, E, T, G, E3, E4, E5). Chaque fonction de calcul cite dans son en-tête le numéro d'équation de la méthode qu'elle implémente.
- **Aucune valeur numérique en dur dans le code.** Toutes les valeurs viennent de `donnees/`, chargées et validées au démarrage. Une donnée sans source fait échouer le chargement.
- **Journal des calculs** : chaque étape écrit ses sorties intermédiaires (tables, trajectoires annuelles) dans un dossier de résultats. On peut relire n'importe quel résultat intermédiaire.
- **Exécution par étapes** avec progression visible, interruption et reprise possibles. Le calcul complet, Monte-Carlo compris, peut prendre plusieurs minutes : c'est accepté.
- **Variantes** : un même projet peut porter plusieurs variantes, calculées et comparées.
- **Déterminisme** : à graine aléatoire identique, résultat identique au bit près.
- **Utilisation en ligne de commande** : `opennat calcul projet.json` produit le dossier de résultats et le RSNat.

### 5.2 Format d'entrée et RSNat

- `schemas/projet.schema.json` : le fichier projet (contexte, unités d'habitat initial et projet avec critères d'état, contiguïtés, nuisances, eau, matériaux par lot, variantes). Champs d'identifiant géométrique prévus, facultatifs.
- `schemas/rsnat.schema.json` (et sa version XSD, comme le RSEE) : données d'entrée, résultats par module, indicateurs, incertitude, version de la méthode et des données, empreinte de contrôle (hash) du calcul.

### 5.3 Tables de données attendues dans `donnees/`

| Table | Contenu |
|---|---|
| `habitats.csv` | Nomenclature, valeur intrinsèque, zone biogéographique, délai de maturité, difficulté de création |
| `etat_criteres.csv` | Grilles de critères d'état par grand type d'habitat et règle de calcul du score |
| `sols.csv` | Coefficients de fonctionnalité par nature de sol et épaisseur de substrat |
| `connectivite.csv` | Paramètres aire-espèces, distances, effets des obstacles |
| `nuisances.csv` | Relations pression-réponse : lumière, bruit, vitrages |
| `eau.csv` | Coefficients hydriques |
| `contexte.csv` | Multiplicateurs de situation et zones biogéographiques |
| `materiaux.csv` | Occupation des sols par matériau, facteurs de caractérisation, plages d'incertitude |
| `seuils.csv` | Seuils proposés et coefficients Mnat |
| `conventions.csv` | Index des conventions Vi-BCN |

---

## 6. Lot 3 : utilitaire de calcul

Un utilitaire **simple et sobre**, sur le modèle de celui d'OpenBCE.

1. **Saisie** par onglets qui suivent la méthode : projet et contexte, état initial, état projet, sol, connectivité, nuisances, eau, matériaux par lot, variantes. Contrôles de saisie en direct (fermeture des surfaces, champs obligatoires, unités).
2. **Import et export** du fichier projet JSON. Import des quantités de matériaux depuis un fichier tableur au format documenté.
3. **Lancement du calcul** avec suivi des étapes (E1 à E5) et de leur avancement. Le calcul tourne sans bloquer l'interface.
4. **Résultats** :
   - indicateurs et niveau atteint ;
   - détail par module et par poste ;
   - trajectoire du site sur 50 ans (courbe) ;
   - biodiversité grise par lot et par matériau ;
   - incertitude et paramètres les plus influents ;
   - comparaison des variantes.
5. **Édition de la fiche standardisée** : le RSNat (JSON et XML) et une fiche de synthèse imprimable en PDF, à l'en-tête de la méthode Vi-BCN, avec version de méthode, version des données et empreinte de contrôle.
6. **Consultation des résultats intermédiaires** de chaque étape.

Pas de compte utilisateur : les projets sont des fichiers.

---

## 7. Lot 4 : banc de validation et documentation

- **Au moins 8 cas tests** couvrant les situations types :
  1. friche urbaine imperméabilisée devenue résidence avec jardin (gain attendu) ;
  2. prairie naturelle en périphérie, construite en logements (forte perte) ;
  3. bureaux sur dalle avec toiture végétalisée ;
  4. réhabilitation sans emprise nouvelle ;
  5. projet en réservoir de biodiversité ;
  6. projet avec mare et haies créées (effet de maturation) ;
  7. bâtiment bois face au même bâtiment béton (module G) ;
  8. site méditerranéen face au même site en zone continentale.
- Pour chaque cas : fichier d'entrée, **calcul de référence fait à la main** (tableur ou carnet) indépendamment du moteur, résultats attendus, tolérance. Le moteur doit retrouver le calcul de référence.
- Tests unitaires par module, tests de non-régression, tests de propriétés (par exemple : ajouter de la pleine terre ne peut pas dégrader Cnat, toutes choses égales par ailleurs).
- Contrôle d'ordre de grandeur du module G par rapport à l'étude Carbone 4, avec explication des écarts.
- Documentation : guide utilisateur, guide du contributeur (comment proposer une nouvelle valeur avec sa source), journal des versions de la méthode et des données.

---

## 8. Tableau de conformité

| N° | Exigence | Lot | Comment on le vérifie |
|---|---|---|---|
| E1 | Chaque coefficient a une source primaire ou une convention numérotée justifiée | 1, 2 | Le chargeur de données refuse toute ligne sans source ; rapport de couverture |
| E2 | Aucune valeur numérique de méthode en dur dans le code | 2 | Revue de code et recherche automatique de constantes |
| E3 | Chaque fonction de calcul cite son équation | 2 | Revue de code |
| E4 | Le texte de méthode suit la structure du § 4.1 | 1 | Revue du sommaire |
| E5 | Les sept modules et les étapes E1 à E5 sont calculés dans l'ordre imposé | 2 | Journal des calculs |
| E6 | Simulation annuelle sur 50 ans par unité d'habitat | 2 | Trajectoires présentes dans les sorties |
| E7 | Monte-Carlo paramétrable, déterministe à graine fixe | 2 | Deux exécutions identiques |
| E8 | Sorties intermédiaires conservées et consultables | 2, 3 | Ouverture dans l'utilitaire |
| E9 | RSNat conforme à ses schémas JSON et XSD | 2 | Validation automatique |
| E10 | Les cas tests retrouvent le calcul de référence à la tolérance fixée | 4 | Banc de validation |
| E11 | Seuils marqués « en attente de validation du Biodiversity Standard Council » | 1, 3 | Texte, fiche, utilitaire |
| E12 | Unités cohérentes dans toute la chaîne (m²HE, m²HE·an) | 1, 2 | Contrôle dimensionnel automatique |
| E13 | Architecture alignée sur OpenBCE, écarts justifiés | 2 | Audit et revue |
| E14 | Aucune publication sans go écrit de Cédric | tous | Rapport de livraison |

---

## 9. Recette

**Méthode (lot 1)**
- [ ] Le texte de méthode contient les douze chapitres du § 4.1.
- [ ] Chaque équation est numérotée et ses unités sont vérifiées.
- [ ] Chaque ligne de `donnees/` a une source ou une convention.
- [ ] Le rapport de couverture indique la part de valeurs sourcées et de conventions.
- [ ] L'exemple de calcul complet est déroulé à la main.

**Moteur (lot 2)**
- [ ] `opennat calcul` produit le dossier de résultats et le RSNat pour chaque cas test.
- [ ] Une ligne de données sans source fait échouer le chargement avec un message clair.
- [ ] Les trajectoires annuelles sur 50 ans sont présentes pour chaque unité.
- [ ] Deux exécutions à graine identique donnent un résultat identique.
- [ ] Le RSNat est valide selon ses schémas.

**Utilitaire (lot 3)**
- [ ] Un projet se saisit entièrement sans toucher au JSON.
- [ ] Une erreur de fermeture des surfaces est signalée avant le calcul.
- [ ] L'avancement des étapes s'affiche pendant le calcul.
- [ ] Les résultats intermédiaires de chaque étape sont consultables.
- [ ] La fiche PDF et le RSNat s'éditent et portent version et empreinte.
- [ ] Deux variantes se comparent côte à côte.

**Validation (lot 4)**
- [ ] Les huit cas tests passent.
- [ ] Les tests de propriétés passent.
- [ ] L'écart avec l'ordre de grandeur Carbone 4 est expliqué.
- [ ] Les guides utilisateur et contributeur sont rédigés.

---

## 10. Livraison

À la fin de **chaque lot** :
1. un rapport `livraison_lotN.md` : ce qui est fait, l'état de la recette cochée, les écarts, les conventions ajoutées, les questions ouvertes ;
2. **arrêt et attente du go écrit de Cédric** avant le lot suivant.

Les questions à Cédric sont posées **une par une**, avec ta recommandation, jamais en liste.
