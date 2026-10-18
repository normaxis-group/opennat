# OpenNat, méthode Vi-BCN : audit et état de l'art (lot 0)

**Pour :** Cédric Plantaz, président de NORMAXIS
**De :** Claude (session Fable 5.1)
**Date :** 17 octobre 2026
**Objet :** livrable du lot 0 du cahier des charges du 16 octobre 2026 : lecture d'OpenBCE, inventaire des sources, couverture des tables de données, choix de nomenclature, points de méthode à trancher. Rien n'a été codé. Le lot s'arrête à ce document et attend le go écrit.

**Fusion.** À la demande de Cédric (17 octobre 2026), ce document intègre 3 éléments repris de l'audit parallèle de lot 0 « VIBCN » (autre session, même cahier des charges) : la définition de Bnat, calquée sur le coefficient de biotope par surface existant (point P12), la liste des 26 types urbains et hors-sol VB.1 à VB.26 (§ 4.3) et les 101 fiches de sources A à E (§ 2.9, dossier `audit/fiches/`). Pour tout le reste, le présent audit prévaut. Les passages modifiés portent la mention « (fusion VIBCN) ».

**Règle appliquée.** Aucune valeur de ce document ne vient de mémoire. Chaque valeur citée a été lue dans un fichier ou une page récupérés le 17 octobre 2026, avec son document, son endroit (tableau, page, cellule, ligne) et son URL. Quand une valeur n'a pas pu être lue à la source, elle est marquée « NON VÉRIFIÉ ». Les valeurs lues dans une source secondaire sont signalées comme telles. Les fichiers sources téléchargés (environ 900 Mo : guides, tableurs, textes, articles) sont conservés avec le projet (§ 6) pour le lot 1.

**Ce que dit l'audit, en 12 lignes.**

1. OpenBCE est entièrement lu : Python 3.11 et numpy, AGPL-3.0, un module par fiche, registre des lectures, banc, API et serveur MCP. Son arborescence, ses conventions de code, son registre des lectures et ses points d'entrée se reprennent tels quels. 6 écarts sont imposés par le cahier des charges et justifiés au § 1.3, dont 2 qui ne sont pas des détails : OpenBCE code ses tableaux en constantes alors qu'OpenNat doit les charger depuis des CSV sourcés, et OpenBCE n'a pas d'interface graphique alors que le lot 3 en demande une « sur le modèle d'OpenBCE ».
2. Les 16 références du cahier des charges et une centaine de sources complémentaires sont inventoriées en 7 fiches (§ 2), avec pour chacune l'accès, la licence, les valeurs disponibles (lues et localisées) et les limites de transposition. 101 fiches de sources complémentaires (A à E, § 2.9, dossier `audit/fiches/`) les complètent en annexe.
3. 3 familles de sources portent la méthode : la métrique statutaire anglaise (architecture surface × distinctivité × état × situation, délais et difficultés par habitat, fiches d'état ; OGL v3), les listes allemandes de valeurs de biotopes (BKompV 0 à 24, 668 types, libres de droits ; Hesse 3 à 80 avec toitures et façades) et les facteurs d'usage des sols de l'ACV (GLOBIO, LC-IMPACT v2 pour la France, ReCiPe 2016, EF 3.1 ; licences libres).
4. 3 sources sont exclues pour cause de licence : le Global Biodiversity Score (CC BY-NC, facteurs sous licence payante), la grille CBSh du CSTB (usage non commercial interdit) et le webservice INIES (interdiction expresse de tout scoring sur les déclarations).
5. Couverture (§ 3) : les valeurs intrinsèques, délais de maturité et difficultés de création des habitats sont sourçables à environ 70 % ; les seuils de nuisances (lumière, bruit, vitrages) existent mais aucune relation continue dose-réponse n'a été trouvée ; aucune valeur MSA n'existe pour les milieux urbains fins ; la relation aire-espèces n'est pas calibrée sous 1 ha ; la perméabilité des clôtures n'a aucune valeur publiée.
6. Le trou le plus grave est dans le module G : aucune source ouverte ne donne l'occupation des sols par kg ou m³ de matériau (les FDES ne publient que le SQP, indicateur de services du sol et non de biodiversité). Les facteurs de caractérisation existent (France, licence libre), pas l'inventaire. Une convention est proposée (P8).
7. Carbone 4 a publié « La biodiversité grise dans le bâtiment » le 6 octobre 2026 (et non en 2022) ; le PDF, fourni par Cédric, est lu en entier : méthode IMPACT World+ sur la plateforme Darwin, fiches INIES complétées par des proxys ecoinvent dimensionnés sur le carbone déclaré, bâtiment type de 50 logements à 272 000 PDF.m².yr en A1-A3, soit environ 91 par m² de plancher ; l'usage des sols n'y pèse que 11 %, la pollution 51 % et le climat 38 %. C'est un contrôle d'ordre de grandeur, pas une source de coefficients (rien n'y est imprimé par matériau), et c'est ce qui conduit au point P19 sur le périmètre du module G.
8. Nomenclature (§ 4) : EUNIS 2012 niveau 3 (EEA, CC BY 4.0), niveau 4 toléré, avec une liste de 26 types urbains et hors-sol à code propre (VB.1 à VB.26, § 4.3), chacun relié à son parent EUNIS 2022 et 2012, à CORINE Biotopes, à la nomenclature ZAN et aux sources de valeurs lues (de 1 à 8 par type, au moins 2 pour 24 types), CORINE Biotopes en code secondaire, EUNIS 2022 en colonne de migration.
9. 19 points de méthode sont présentés un par un avec recommandation et valeur par défaut (§ 5). 2 attendent une réponse de Cédric : qui édite la méthode (P1) et quelle version d'Effinature sert de raccordement (P16).
10. Recommandations structurantes : valeur intrinsèque sur l'échelle BKompV ramenée à 1 (P2) ; période de 50 ans avec sortie à 30 ans (P3) ; pas d'actualisation, le délai étant déjà compté en m²HE·an par la simulation annuelle (P4) ; module G en MSA avec inventaire par convention et surcharge par l'ACV du projet (P8) ; quantités de matériaux lues dans la branche RSEnv du RSEE du projet, jamais dans INIES (P9) ; composante climat ajoutée à Inat et pollution en indicateur complémentaire (P19) ; Bnat défini comme un coefficient de biotope par surface, 100 × Σ (S_i × c_i) / S_parcelle, dont les coefficients de sol sont les médianes des grilles publiées et non des poids inventés (P12).
11. 2 contraintes d'accès à inscrire dans le dépôt : Legifrance, EUR-Lex et iso.org bloquent les accès automatisés (textes lus sur des copies officielles ou des miroirs référencés) ; les serveurs de l'INPN sont hors service pour une durée indéterminée (HabRef v7 récupéré sur la page temporaire de PatriNat, licence non lue).
12. Le prototype en ligne « OpenNat » du 16 octobre 2026 n'a pas été ouvert, conformément au cahier des charges.

## 1. OpenBCE, le jumeau technique à reproduire

Dépôt lu le 17/10/2026 : https://github.com/normaxis-group/openbce (clone du commit 66b6550 du 11/10/2026 ; version 0.1.0 publiée le 09/10/2026 d'après CITATION.cff).

### 1.1 Description en 20 lignes

1. Auteur Cédric PLANTAZ, droits ARKEMEP, licence AGPL-3.0-or-later, en-tête SPDX dans chaque fichier, fichier de citation CITATION.cff et index llms.txt pour les assistants.
2. Langage : Python 3.11 ou plus, dépendance unique numpy ; pytest et openpyxl en développement seulement ; API HTTP et serveur MCP sur la bibliothèque standard ; Dockerfile python:3.12-slim.
3. Volume : environ 11 300 lignes de Python, tout en français (noms, commentaires, documentation).
4. Structure : `openbce/` 42 modules, un par fiche ou famille de fiches de l'annexe III, les numéros d'équation et de tableau en commentaire à côté de la ligne qui les applique ; `banc/` 34 scripts de comparaison aux sorties de référence ; `outils/` 2 convertisseurs de données publiées ; `tests/` 37 fichiers pytest ; `specs/` spécifications de lecture écrites avant chaque lot de code ; `docs/` 6 documents, `openapi.yaml` et `schemas/resume.schema.json`.
5. Format pivot : le RSEE, c'est à dire le XML réglementaire de l'annexe VI, lu en arbre de noeuds (`openbce/rsee.py`, classe `Noeud`, collections aplaties) ; la sortie est un RSEE recalculé dont seul le bloc `Sortie_Projet` est remplacé (`openbce/sortie_rsee.py`).
6. Schémas : aucun XSD officiel du RSEE n'est publié, la structure lue est celle des RSEE rencontrés ; seul le résumé JSON de l'API est validé par un schéma (`resume.schema.json`).
7. Données de référence : les tableaux de la méthode sont des constantes Python dans les modules, avec le numéro de tableau en commentaire (tableau 78 dans `eclairage.py`, tableau 337 dans `bilans.py`, coefficients f_CO2 et DE dans `carbone.py`) ; les scénarios conventionnels sont convertis en JSON (`openbce/tables/scenarios_officiels.json`, 2 Mo, clé `source` qui nomme le tableur officiel) ; la météo est téléchargée à la source et reste hors dépôt (droit de redistribution à confirmer, `.gitignore`).
8. Sources : `docs/sources.md` liste chaque texte, annexe et donnée avec son lien ; portail du ministère sous Licence Ouverte etalab-2.0.
9. Lectures du texte : `docs/lectures.md`, registre en 3 catégories (muet, déduit, contre la lettre), chaque lecture écrite aussi dans le module concerné avec la mesure chiffrée qui l'a décidée ; les hypothèses écartées restent dans le code comme options d'étude inactives par défaut.
10. Règle de `CONTRIBUTING.md` : aucun coefficient de calage ; une hypothèse à tester devient une option d'étude inactive ; des tests sans données réelles.
11. Journal des calculs : il n'y en a pas ; les résultats vivent en mémoire dans un dictionnaire `calcul` (séries mensuelles par groupe) assemblé par `banc/sortie_rsee.py`, et les mesures du banc sont écrites dans des fichiers `brut/*.txt` hors dépôt.
12. Progression : le serveur MCP envoie une notification toutes les 15 s si le client fournit un `progressToken` ; pas d'interruption ni de reprise.
13. Déterminisme : calcul synchrone et déterministe, sans aucun tirage aléatoire ; de 30 s à 40 min par projet.
14. Tests : pytest sur des RSEE fabriqués dans le test (`tests/test_socle.py`), jamais de données de clients dans le dépôt (`*.xml` ignorés).
15. Banc de validation : 223 RSEE de 54 opérations réelles non publiées, comparés poste par poste aux sorties du logiciel évalué qui les a produits ; résultats dans `docs/validation.md` (Cep : écart absolu médian 1,5 % sur 50 opérations au 09/10/2026).
16. Interfaces : ligne de commande (`python -m banc.cep_total <rsee.xml>`), API HTTP (`POST /calcul`, réponse RSEE recalculé, en-tête de résumé), serveur MCP stdio (outils `version`, `lire_rsee`, `calculer`, `comparer`, `variante`).
17. Il n'existe aucune interface graphique : l'« utilitaire » d'OpenBCE, c'est la ligne de commande, l'API et le serveur MCP.
18. Génération du RSEE : noms de champs repris des RSEE lus, champs non calculés absents (aucune valeur inventée), validation par un schéma « à faire ».
19. Documentation : README avec avertissement de non-opposabilité, `docs/methode.md` (correspondance fiche par module), `docs/validation.md` (réserves, protocole, résultats, écarts connus, détail par brique), `docs/ia.md`.
20. Couverture : énergie (Bbio, Cep, DH, Ic énergie) ; l'ACV des composants (base INIES) n'est pas traitée.

### 1.2 Réutilisable tel quel dans OpenNat

- L'arborescence : `opennat/` (moteur), `banc/`, `outils/`, `tests/`, `specs/`, `docs/`, `pyproject.toml`, `Dockerfile`, `CITATION.cff`, `llms.txt`, `CONTRIBUTING.md`, `.gitignore`.
- Les conventions de code : Python 3.11 et numpy, tout en français, un module par module de méthode, en-tête SPDX, numéro d'équation en commentaire à côté de la ligne qui l'applique, docstring de module qui résume la fiche suivie.
- `docs/lectures.md` : c'est, à la lettre, le modèle de `methode/conventions.md` (catégories, mesure qui décide, options d'étude inactives). Les 3 catégories d'OpenBCE deviennent : « source muette », « convention de transposition », « valeur de secours ».
- `docs/sources.md` : modèle de `methode/bibliographie.md` (tableau texte, objet, lien, licence).
- La clé `source` du JSON des scénarios : le principe est généralisé aux CSV de `donnees/` (une colonne `source` obligatoire par ligne).
- `docs/validation.md` : structure du rapport de validation (réserves, protocole, résultats, écarts connus, détail par brique).
- `openbce/api.py` et `openbce/serveur_mcp.py` : squelettes de l'API HTTP et du serveur MCP, à reprendre avec les outils renommés (`version`, `lire_projet`, `calculer`, `comparer`, `variante`).
- `docs/schemas/resume.schema.json` : modèle du résumé JSON d'un calcul.
- `tests/` : fabrication des entrées dans le test, aucune donnée réelle ; `banc/` : scripts de comparaison à des références hors dépôt.
- L'avertissement de non-opposabilité du README, à adapter : « méthode en attente de validation du Biodiversity Standards Council ».

Repris pour un autre usage : `openbce/rsee.py` (lecteur XML en arbre de noeuds) sert à lire la branche RSEnv du RSEE du projet, qui porte les quantités de composants par lot (point P9) ; OpenBCE ne lit pas encore cette branche. Non repris : `sortie_rsee.py`, puisque le pivot d'OpenNat est un fichier JSON et que le RSNat a son propre schéma ; les modules physiques, sans équivalent.

### 1.3 Écarts imposés par le cahier des charges (à justifier au titre de E13)

| N° | Point | OpenBCE | OpenNat (cahier des charges) | Justification de l'écart |
|---|---|---|---|---|
| A1 | Données de référence | Constantes dans les modules, numéro de tableau en commentaire | `donnees/*.csv`, une ligne par valeur avec `source`, `reference_precise`, `url`, `type`, `justification` ; chargeur qui refuse toute ligne sans source (E1, E2) | Th-BCE a une source unique et opposable ; Vi-BCN assemble des dizaines de sources de rangs différents, la traçabilité par ligne est la condition de l'opposabilité |
| A2 | Format pivot | RSEE XML réglementaire | `projet.json` validé par `schemas/projet.schema.json` ; RSNat en sortie, JSON et XML avec XSD | Aucun format réglementaire n'existe pour la biodiversité ; le XML n'est utile qu'en sortie, par analogie avec le RSEE |
| A3 | Journal des calculs | Aucun ; résultats en mémoire | Dossier de résultats par étape, sorties intermédiaires relisibles, interruption et reprise (E5, E8) | Exigé pour la relecture par l'écologue et pour la simulation sur 50 ans par unité |
| A4 | Aléatoire | Aucun | Monte-Carlo paramétrable, déterministe à graine fixe (E7) : `numpy.random.Generator` avec graine écrite dans le projet et dans le RSNat | Nouveau besoin (étape E4) |
| A5 | Utilitaire | Pas d'interface graphique : ligne de commande, API, MCP | Lot 3 : saisie par onglets, suivi, résultats, fiche PDF | Le « modèle d'OpenBCE » n'existe pas pour ce lot ; voir le point à trancher P9 |
| A6 | Droits | ARKEMEP | À fixer : voir le point à trancher P1 | |

### 1.4 La méthode Th-BCE 2020, structure documentaire à reproduire

Lu le 17/10/2026 sur la version consolidée de l'annexe III (PDF de 1 854 pages, modifié le 21/07/2026), https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/annexeiii_arrete_4_aout_2021_complet_compresse.pdf, pages 15 et 16 :

- Le texte distingue des fiches d'application (préfixe FA_, qui précisent comment appliquer la méthode dans certaines configurations) et des fiches algorithmes (les éléments codés dans le coeur de calcul, préfixe C_ pour un composant, S1_, S2_, S3_ pour les assemblages).
- Une fiche algorithme a 3 parties : Introduction (objet de la fiche) ; Nomenclature (liste des variables avec, dans l'ordre : nom, description, unité, plage d'évolution et, le cas échéant, valeur conventionnelle) ; Description mathématique (équations numérotées qui emploient les variables de la nomenclature).
- La nomenclature distingue 5 types de variables : entrées (venant d'autres fiches), paramètres (intrinsèques, propres au composant, ou d'intégration, propres à la mise en oeuvre dans le projet), variables internes, constantes, sorties (qui font le lien avec les autres objets du coeur de calcul).
- Règle d'arrondi (1.3.1) : résultats intermédiaires et finaux fournis avec 1 chiffre après la virgule.
- Les données conventionnelles (chapitre 2) sont séparées des fiches : scénarios d'occupation et d'usage horaires, à la semaine, avec vacances.
- Le sommaire du texte : 1 Généralités, 2 Données conventionnelles, puis les fiches par chapitre physique (3 météo et environnement extérieur, 4 scénarios et environnement intérieur, 5 bâti, 6 ventilation, 7 éclairage, 8 chauffage et refroidissement, 9 ECS, 10 déplacements et parkings, 11 pertes récupérables, 12 photovoltaïque, 13 sorties et bilans, 15 scénarios, 16 Titre V).

Transposition pour Vi-BCN : chaque module (S, H, C, N, E, T, G) et chaque étape (E1 à E5) est écrit comme une fiche algorithme avec ces 3 parties et ces 5 types de variables ; les tables de `donnees/` jouent le rôle du chapitre 2 ; les conventions numérotées jouent le rôle des fiches d'application.

Pour le RSEE : OpenBCE confirme (`docs/rsee.md`) qu'aucun XSD n'est publié par le ministère ; la vérification directe sur le portail est reprise au § 2.5.

## 2. Inventaire des sources

7 fiches, une par famille de sources. Chaque fiche a été établie le 17/10/2026 par lecture des documents eux-mêmes (PDF, tableurs, XML, pages), jamais de mémoire ; les fiches indiquent pour chaque document s'il a été lu intégralement, partiellement ou s'il n'a pas été accessible. Les valeurs sont reproduites telles qu'écrites dans la source (point ou virgule décimale, notation E). Les tirets typographiques des titres originaux sont rendus par des traits d'union.

| Fiche | Famille | Références du cahier des charges couvertes | Ce qu'elle apporte à Vi-BCN |
|---|---|---|---|
| 2.1 | Statutory Biodiversity Metric (Angleterre) | Statutory Biodiversity Metric 2024 | architecture du calcul, échelles de distinctivité et d'état, multiplicateurs temporels et de difficulté, délais par habitat, fiches d'état, arbres, haies, habitats urbains |
| 2.2 | Biotopwertverfahren allemands | BKompV 2020, Hesse, Bavière, NRW | valeurs de biotopes 0 à 24 (Bund), 3 à 80 (Hesse), 0 à 15 (Bavière), 0 à 10 (NRW), plus de 190 valeurs urbaines et périurbaines, règles temporelles |
| 2.3 | MSA, GLOBIO, GBS | GLOBIO 4, Alkemade 2009, GBS | définition et agrégation de la MSA, valeurs par usage des sols, relations pression-réponse (fragmentation, routes, azote, climat), coefficients du code GLOBIO 4, limites du GBS |
| 2.4 | ACV et occupation des sols | LC-IMPACT, Chaudhary 2015, ReCiPe 2016, EF 3.1, EN 15804 et INIES, Carbone 4 | facteurs de caractérisation occupation et transformation (France), temps de régénération, lots RE2020, licence INIES, études de biodiversité grise |
| 2.5 | Cadre français et nomenclatures | nomenclature ZAN, trame verte et bleue, BAF Berlin et CBS, UGF Londres, EUNIS, CORINE Biotopes, HabRef, zones biogéographiques, XSD du RSEE | textes exacts et seuils, coefficients de biotope lus dans 4 règlements, facteurs UGF, versions et licences des typologies, couche des régions biogéographiques |
| 2.6 | Écologie quantitative des modules | (recherche large demandée par le cahier des charges) | aire-espèces, surfaces minimales, routes et clôtures, lumière (dont arrêté du 27/12/2018), bruit, vitrages, sols et substrats, mares, maturation et échec des créations |
| 2.7 | Méthodes françaises et textes récents | (recherche large) | dimensionnement ERC (CGDD 2021), guide ARB îdF 2026, BiodiverCity, règlement (UE) 2024/1991, ISO TC 331, coefficients de biotope en France, code de l'urbanisme |

La fiche 2.8 liste les références du cahier des charges qui n'ont pas pu être lues et ce qui doit être demandé en fichier. La section 2.9 présente les 101 fiches de sources A à E reprises de l'audit VIBCN et livrées en annexe dans `audit/fiches/`.

### 2.1 Statutory Biodiversity Metric (Angleterre)

Date de consultation : 17/10/2026. Toutes les valeurs ci-dessous ont été lues dans les fichiers téléchargés depuis gov.uk / publications.naturalengland.org.uk (PDF et tableurs ouverts et parcourus intégralement) ou sur les pages lues. Aucune valeur de mémoire. Copies locales de travail : user_guide_june2026.pdf, ssm_user_guide_july2025.pdf, statutory_metric_1.0.4.xlsx, condition_assessments_july2025.xlsx, ssm_1.2.3.xlsm, bm4_technical_annex2.pdf, marshall2024.pdf (dossier de travail de la session, à verser dans `sources/` au lot 1).

#### Objet

Le Statutory Biodiversity Metric est la métrique officielle publiée par le Secretary of State (Defra) pour mesurer la « valeur de biodiversité » des habitats dans le cadre du Biodiversity Net Gain (BNG) obligatoire en Angleterre. Base légale : Environment Act 2021, Schedule 14, qui insère un Schedule 7A dans le Town and Country Planning Act 1990 ; para. 2(1) : l'objectif de gain est atteint si la valeur de biodiversité post-aménagement dépasse la valeur pré-aménagement d'au moins le « relevant percentage » ; para. 2(3) : « The relevant percentage is 10% » ; para. 4(1)-(2) : la métrique est un document produit et publié par le Secretary of State ; para. 9(3) : les améliorations doivent être maintenues au moins 30 ans après achèvement (source : legislation.gov.uk, Schedule 14).

Calendrier (page gov.uk « Understanding biodiversity net gain », mise à jour affichée 14 July 2026) : BNG obligatoire « from 12 February 2024 » ; NSIP « from 2 November 2026 » ; pour les petits sites la page lue mentionne seulement « From 6 August 2026, small ('minor') developments ... can consider options 1 and 2 at the same time ». Date d'entrée en vigueur pour les petits sites : NON VÉRIFIÉ (non trouvée sur la page lue).

Filiation : le guide (p. 6, Acknowledgements) indique que la métrique statutaire « builds on a series of previous versions of the biodiversity metric » (Natural England, Environment Agency, Forestry Commission) et sur le cadre de Treweek et Butcher (2009, 2010). Le tableur statutaire v1.0.0 date du 29 novembre 2023 (onglet « Version History »).

3 modules, 3 types d'unités non fongibles : area habitat units (ha), hedgerow units (km), watercourse units (km) (guide p. 10 et Table 1 p. 11-13).

#### Accès et licence (consulté le 17/10/2026)

Page pivot gov.uk : « Statutory biodiversity metric tools and guides », https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides. Publiée le 29 November 2023, dernière mise à jour 2 June 2026. Pied de page : « All content is available under the Open Government Licence v3.0, except where otherwise stated », avec mention « © Crown copyright ». Historique des versions : https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides/statutory-biodiversity-metric-tools-and-guides-version-history

| Document | URL | Format / taille | Version lue |
|---|---|---|---|
| Statutory biodiversity metric: user guide | https://assets.publishing.service.gov.uk/media/6a1d98e9c7335e2ca6daadd5/The_Statutory_Biodiversity_Metric_-_User_Guide_-_June_2026.pdf | PDF, 2,18 Mo, 89 pages | « First published: February 2024, Last updated: June 2026 » (p. 1) |
| Calculation tool (macro enabled) | https://assets.publishing.service.gov.uk/media/6867e61881dd8f70f5de3b63/The_Statutory_Metric_Macro_Enabled_1.0.4.xlsm | XLSM, 4,12 Mo | 1.0.4 |
| Calculation tool (macro disabled) | https://assets.publishing.service.gov.uk/media/6867e62810d550c668de3b4e/The_Statutory_Metric_Macro_Disabled_1.0.4.xlsx | XLSX, 4,05 Mo | 1.0.4, « 3rd July 2025 » (onglet Version History) |
| Small sites metric: user guide | https://assets.publishing.service.gov.uk/media/686677acdd1a7e01559e6d45/The_Small_Sites_Metric__Statutory_Biodiversity_Metric__-_User_Guide_July_2025.pdf | PDF, 1,04 Mo, 63 pages | July 2025 |
| Small sites metric: calculation tool | https://assets.publishing.service.gov.uk/media/6863f5ba08bf2f5376121aee/The_Small_Sites_Metric_1.2.3.xlsm | XLSM, 877 Ko | 1.2.3, « 3rd July 2025 » |
| Condition assessments (= Technical Annex 1) | https://assets.publishing.service.gov.uk/media/689c5f19d2a1b0d5d1bb1254/Statutory_Biodiversity_Metric_Condition_Assessments_-_July_2025.xlsx | XLSX, 379 Ko | Onglet INSTRUCTIONS : « Technical Annex 1: Condition Assessment Sheets and Methodology, Version Number: July 2025 (v1.0.2) » |
| Transferring data from 4.0 to the statutory tool | https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides/transferring-data-from-40-to-the-statutory-biodiversity-metric-calculation-tool | HTML | non lu |

Observations :
- L'édition « July 2025 » du guide (https://assets.publishing.service.gov.uk/media/689c5ee17b2e384441636196/The_Statutory_Biodiversity_Metric_-_User_Guide_-_July_2025.pdf) renvoie un fichier identique (même md5) à l'édition June 2026 : gov.uk sert la version courante. Les numéros de page sont ceux de l'édition June 2026.
- Le « Technical Annex 1 » n'existe pas comme PDF séparé : c'est le classeur Excel des fiches d'état. L'onglet interne « 27.VERSION HISTORY » indique « Version 1.0.2, 3rd July 2025 » alors que la page gov.uk d'historique liste une « Version 1.0.3 » avec les mêmes changements.
- Il n'existe PAS de « Technical Annex 2 » propre à la métrique statutaire. La page Natural England « The Biodiversity Metric Supporting Documents (JP039) », https://publications.naturalengland.org.uk/publication/6049804846366720, indique : « A detailed technical annex for the statutory metric will be published shortly. » La source méthodologique disponible est « The Biodiversity Metric 4.0, User Guide - Technical Annex 2 - Technical Information », Natural England Joint Publication JP039, March 2023, ISBN 978-1-7393362-3-3, 79 pages : https://publications.naturalengland.org.uk/file/5749350878412800. Ses tables de données (p. 69-79) sont identiques aux onglets G-1 à G-8 du tableur statutaire pour les valeurs vérifiées.

Licences :
- Guide utilisateur (p. 2) : « © Crown copyright 2026. This information is licensed under the Open Government Licence v3.0. » Même mention dans le guide SSM (p. 2).
- Restriction explicite (guide p. 6) : « The UK Habitat Classification System is used under licence from UKHab Ltd. No onward licence implied or provided and, where applicable, the same shall be out of scope of the OGL v3.0 ». La page de licence UKHab (https://ukhab.org/licensing/) a répondu 403 : conditions UKHab NON VÉRIFIÉES.
- Technical Annex 2 du BM 4.0 (p. 2) : OGL v3.0, « © Natural England and other parties 2023 », photos réservées à un usage non commercial.
- Tableur de calcul : aucune mention de licence à l'intérieur du classeur 1.0.4 ; seul le bandeau de la page gov.uk s'applique. Téléchargeable sans compte.
- Texte OGL v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) : liberté de copier, publier, distribuer, adapter, exploiter commercialement ; obligation d'attribution (« Contains public sector information licensed under the Open Government Licence v3.0 ») ; exemptions : données personnelles, logos, droits de tiers, autres droits de PI.

#### Architecture du calcul (formules)

Formules lues dans le Technical Annex 2 BM 4.0, section 7 « Metric equations and functions », p. 65-67, et confirmées dans les formules du tableur 1.0.4 (onglet A-1, cellule Q11 ; onglet A-2, cellule Y11).

Notation : A aire (ha) ; L longueur (km) ; QD distinctiveness ; QC condition ; QSS strategic significance ; RD difficulté ; RT temporel ; ROS risque spatial (hors site) ; RRE empiétement de la zone riveraine ; RWE empiétement du cours d'eau ; t0 état initial ; t1 état post-intervention.

- État initial (area) : Baseline AHBU = (A_t0 × QD_t0 × QC_t0) × QSS_t0 (TA2 p. 65, Eq. 1 ; tableur A-1 Q11 = H11 × J11 × L11 × O11).
- Création : Creation AHBU = [A_t1 × QD_t1 × QC_t1] × [RD × RT] × [QSS_t1] (TA2 p. 65, Eq. 2 ; tableur A-2 Y11 = G11 × I11 × K11 × N11 × T11 × X11).
- Amélioration : Enhancement AHBU = {[(A_t1 × QD_t1 × QC_t1) - (A_t0 × QD_t0 × QC_t0)] × (RD × RT) + (A_t0 × QD_t0 × QC_t0)} × QSS_t1 (TA2 p. 65, Eq. 3) : seuls les gains incrémentaux subissent les multiplicateurs de risque.
- Habitats retenus : comptés dans l'état post-intervention à leur valeur initiale (guide p. 33).
- Variation sur site : (Enhancement + Creation + Retained)_t1 - Baseline_t0 (Eq. 4) ; hors site : même différence × ROS (Eq. 5) ; total = somme (Eq. 6).
- Haies : mêmes équations avec L (km) (TA2 p. 66).
- Cours d'eau : Baseline WBU = (L × QD × QC × QSS) × RRE × RWE ; création = [L × QD × QC × QSS] × [RD × RT] × [RRE × RWE] (TA2 p. 67).
- Règle 2 (guide p. 15, Table 2) : les 3 types d'unités ne peuvent être ni sommés ni convertis ; le 10 % s'applique à chaque type. Règle 3 : l'usage du tableur officiel est obligatoire. Règle 4 : dérogation possible dans des « exceptional ecological circumstances » (guide p. 19-21).
- Multiplicateur temporel : actualisation à 3,5 % par an, « the value recommended in the Treasury Green Book » (TA2 p. 52, § 5.3.2) ; multiplicateur = 0,965^t (onglet G-4 : 96,5 % à 1 an, 93,1225 % à 2 ans, 70,028 % à 10 ans, 34,342 % à 30 ans). Au-delà : catégorie « 30+ » = 0,3197967361 (G-4 cellule C36), qui correspond arithmétiquement à 0,965^32. La métrique suppose un « saut » de qualité à l'issue du délai, sans progression incrémentale (TA2 p. 52, § 5.3.3). Fonctions « habitat created in advance » et « delay in starting » : guide p. 36-37 ; tableur A-2 colonnes P, Q, S.

#### Valeurs disponibles

Distinctiveness (guide p. 27, Table 5 ; tableur G-1 V3:W7) : Very high 8 ; High 6 ; Medium 4 ; Low 2 ; Very low (haies) 1 ; Very low (surfacique) 0. Critères d'affectation (TA2 p. 25, Technical Table 3-1) : rareté en Angleterre (Priority Habitat Inventory 2019), part protégée en SSSI, statut Priority Habitat (NERC Act s. 41), Liste rouge européenne des habitats. Very high = habitats prioritaires menacés ou « Critically Endangered » ; Medium = semi-naturels non prioritaires ; Low = « Agricultural and urban land of lower biodiversity value » ; Very low = « hard standing or sealed surface ».

Condition (guide p. 28, Table 6 ; tableur G-1 Z3:AA9) : Good 3 ; Fairly Good 2,5 ; Moderate 2 ; Fairly Poor 1,5 ; Poor 1 ; Condition Assessment N/A 1 ; N/A - Other 0. Les catégories « fairly » ne peuvent s'écarter que d'un cran du résultat d'une fiche standard (guide p. 28 et p. 88).

Strategic significance (guide p. 30 Table 7 et p. 32 Table 8 ; tableur G-3 L3:N6) : High (formally identified in local strategy) 1,15 ; Medium 1,10 (interdit là où une Local Nature Recovery Strategy est publiée) ; Low 1. Là où une LNRS est publiée, l'état initial est toujours Low (guide p. 29).

Difficulté de création / d'amélioration (tableur G-3 P3:Q6 ; TA2 p. 56-57) : Low 1 ; Medium 0,67 ; High 0,33 ; Very High 0,1. Exemples (G-3, colonnes B à E ; TA2 p. 69-70) : Modified grassland Low/Low (1 / 1) ; Lowland calcareous grassland High/High (0,33 / 0,33) ; Lowland meadows High/Medium (0,33 / 0,67) ; Lowland heathland High/Medium ; Other woodland broadleaved Low/Low ; Lowland mixed deciduous woodland High/High ; Wood-pasture and parkland Very High/High (0,1 / 0,33) ; Blanket bog Very High/High ; Ponds non-priority Low/Medium ; Biodiverse green roof Medium/Medium (0,67 / 0,67) ; Green walls Medium/Medium ; Bioswale et SuDS Medium (création) ; Developed land sealed surface Low/Low ; Urban tree Low/Low. Méthode : jugement d'experts avec référence à Entec (2011), Entec et Amec (2013), Amec (2016) (TA2 p. 56, § 6.1.4).

Multiplicateur temporel (tableur G-4 A4:C37 ; TA2 p. 52-53, Technical Table 5-1) : 0 an : 1,000 ; 1 : 0,965 ; 2 : 0,931 ; 3 : 0,899 ; 4 : 0,867 ; 5 : 0,837 ; 6 : 0,808 ; 7 : 0,779 ; 8 : 0,752 ; 9 : 0,726 ; 10 : 0,700 ; 11 : 0,676 ; 12 : 0,652 ; 13 : 0,629 ; 14 : 0,607 ; 15 : 0,586 ; 16 : 0,566 ; 17 : 0,546 ; 18 : 0,527 ; 19 : 0,508 ; 20 : 0,490 ; 21 : 0,473 ; 22 : 0,457 ; 23 : 0,441 ; 24 : 0,425 ; 25 : 0,410 ; 26 : 0,396 ; 27 : 0,382 ; 28 : 0,369 ; 29 : 0,356 ; 30 : 0,343 ; 30+ : 0,320.

Temps vers la condition cible, création (années) : tableur G-4, colonnes F à M ; valeurs identiques dans TA2 p. 73-74. Colonnes : Good / Fairly Good / Moderate / Fairly Poor / Poor.

| Habitat (libellé du tableur) | G | FG | M | FP | P | Ligne G-4 |
|---|---|---|---|---|---|---|
| Grassland - Modified grassland | 7 | 5 | 4 | 2 | 1 | 20 |
| Grassland - Other neutral grassland | 10 | 7 | 5 | 3 | 2 | 22 |
| Grassland - Lowland calcareous grassland | 20 | 15 | 10 | 8 | 5 | 17 |
| Grassland - Lowland meadows | 15 | 12 | 10 | 8 | 5 | 19 |
| Grassland - Traditional orchards | 30 | 25 | 20 | 10 | 5 | 14 |
| Heathland and shrub - Mixed scrub | 10 | 7 | 5 | 3 | 1 | 34 |
| Heathland and shrub - Lowland heathland | 30+ | 25 | 20 | 15 | 10 | 33 |
| Lakes - Ponds (non-priority habitat) | 5 | 4 | 3 | 2 | 1 | 47 |
| Wetland - Reedbeds | 12 | 10 | 7 | 5 | 3 | 88 |
| Wetland - Blanket bog | 30+ | 30+ | 30+ | 30+ | 30+ | 82 |
| Woodland and forest - Other woodland; broadleaved | 30+ | 25 | 15 | 7 | 5 | 96 |
| Woodland and forest - Lowland mixed deciduous woodland | 30+ | 30+ | 30+ | 25 | 10 | 92 |
| Woodland and forest - Wet woodland | 30+ | 30 | 15 | 10 | 5 | 101 |
| Individual trees - Urban tree | 30+ | 30+ | 27 | 19 | 10 | 76 |
| Individual trees - Rural tree | 30+ | 30+ | 27 | 19 | 10 | 135 |
| Urban - Biodiverse green roof | 10 | 8 | 5 | 3 | 1 | 71 |
| Urban - Intensive green roof | 5 | 4 | 3 | 2 | 1 | 63 |
| Urban - Facade-bound green wall | 5 | 4 | 3 | 2 | 1 | 68 |
| Urban - Ground based green wall | 5 | 4 | 3 | 2 | 1 | 69 |
| Urban - Open mosaic habitats on previously developed land | 10 | 7 | 4 | 2 | 0 | 73 |
| Urban - Cemeteries and churchyards | 20 | 17 | 15 | 12 | 10 | 65 |
| Urban - Allotments | 1 | 1 | 1 | 1 | 1 | 59 |
| Urban - Rain garden / SuDS / Vacant or derelict land / Bare ground | 5 | 4 | 3 | 2 | 1 | 74, 77, 79, 80 |
| Urban - Bioswale | 3 | 2 | 1 | 1 | 1 | 62 |
| Urban - Vegetated garden, Introduced shrub, Other green roof, Ground level planters | condition « Condition Assessment N/A » uniquement : 1 an | | | | | 81, 72, 67, 70 |
| Urban - Developed land; sealed surface, Unvegetated garden, Built linear features, Artificial unvegetated unsealed surface | « N/A - Other » uniquement : 0 | | | | | 66, 78, 64, 61 |

Amélioration (matrice condition de départ vers condition cible) : tableur G-5 ; par exemple Modified grassland Poor vers Good 15 ans, Moderate vers Good 10 ans (ligne 21) ; Other neutral grassland Poor vers Good 15, Moderate vers Good 10 (ligne 23) ; Lowland calcareous grassland Poor vers Good 20 (ligne 18).

Arbres isolés (guide p. 61-65 ; tableur G-3 W3:Z7) : Small (DBH > 7,5 cm et ≤ 30 cm) 0,0041 ha ; Medium (> 30 et ≤ 60 cm) 0,0163 ha ; Large (> 60 et ≤ 90 cm) 0,0366 ha ; Very large (> 90 cm) 0,0765 ha (guide p. 62, Table 15). Le guide précise : « Tree helper values are a representation of canopy biomass, and are based on the root protection area formula, derived from BS 5837:2012 » ; dans le tableur le rayon vaut 12 fois le diamètre et la surface est π × rayon². Distinctiveness Urban tree et Rural tree : Medium, 4 (G-1 lignes 80-81). Fiche d'état « 9A.INDIVIDUAL TREES » : 6 critères (espèce indigène, continuité de houppier, maturité, santé, niches écologiques, plus de 20 % du houppier surplombant de la végétation) ; Good = 5 ou 6, Moderate = 3 ou 4, Poor = 2 ou moins. Arbres nouvellement plantés : classe Small (guide p. 64) ; la croissance naturelle n'est pas comptée. Site résidentiel sans plan paysager : ratio par défaut 70:30 entre « Developed land; sealed surface » et « Vegetated garden » (guide p. 59). Lots privés : création uniquement comme « vegetated garden » ou « unvegetated garden » (guide p. 59-60).

Habitats urbains : distinctiveness et condition (tableur G-1 colonnes K et L ; onglet 22A.URBAN du Technical Annex 1) :

| Habitat | Distinctiveness (score) | Condition admise | Code UKHab |
|---|---|---|---|
| Developed land; sealed surface | V.Low (0) | N/A - Other = 0 ; donc 0 unité | u1b |
| Artificial unvegetated, unsealed surface | V.Low (0) | N/A - Other = 0 | u1c |
| Built linear features | V.Low (0) | N/A - Other = 0 | u1e |
| Unvegetated garden | V.Low (0) | N/A - Other = 0 | 829 |
| Vegetated garden | Low (2) | Condition Assessment N/A = 1 | 828 |
| Introduced shrub | Low (2) | Condition Assessment N/A = 1 | 847 |
| Other green roof | Low (2) | Condition Assessment N/A = 1 | 89 |
| Intensive green roof | Low (2) | Good 3 à Poor 1 | 88 |
| Biodiverse green roof | Medium (4) | Good 3 à Poor 1 | 87 |
| Facade-bound green wall | Low (2) | Good 3 à Poor 1 | 843 |
| Ground based green wall | Low (2) | Good 3 à Poor 1 | 842 |
| Ground level planters | Low (2) | Condition Assessment N/A = 1 | 845 |
| Rain garden, Bioswale, Sustainable drainage system, Allotments, Vacant or derelict land, Bare ground | Low (2) | Good 3 à Poor 1 | 850, 849, 848, 616, 82, 510 |
| Cemeteries and churchyards | Medium (4) | Good 3 à Poor 1 | 90 |
| Open mosaic habitats on previously developed land | High (6) | Good 3 à Poor 1 | 80 |

Fiche 22A.URBAN : 3 critères de base (A structure variée, aucune composante > 80 % ; B espèces bénéfiques ; C espèces exotiques envahissantes < 5 %, absence totale exigée pour Good) ; critère D pour les OMHPDL (au moins 4 communautés pionnières) ; E1 et E2 pour bioswale et SuDS ; F pour toiture intensive (minimum 50 % de fleurs sauvages, 70 % de la surface en substrat et végétation) ; G pour toiture biodiverse (substrat 80 à 150 mm, au moins 50 % à 150 mm). Habitats à 3 critères : Good = 3/3 avec absence totale d'EEE ; Moderate = 2/3 ; Poor = 0 ou 1. Murs végétalisés : seule la surface végétalisée (projetée) est comptée et n'entre pas dans la surface du site (guide p. 60). Toitures végétalisées de maisons individuelles : uniquement « other green roof » (guide p. 60).

Module haies (guide p. 26 et p. 69 ; tableur G-6 ; fiche 8A.HEDGEROW) : unité km sur l'axe ; haies doubles comptées 2 fois ; pas de soustraction de l'emprise de la haie des habitats surfaciques (guide p. 26). Distinctiveness (G-6, colonnes C-D) : Species-rich native hedgerow with trees associated with bank or ditch V.High 8 ; Species-rich native hedgerow with trees, Species-rich native hedgerow associated with bank or ditch, Native hedgerow with trees associated with bank or ditch : High 6 ; Species-rich native hedgerow, Native hedgerow associated with bank or ditch, Native hedgerow with trees, Ecologically valuable line of trees : Medium 4 ; Native hedgerow, Line of trees : Low 2 ; Non-native and ornamental hedgerow : V.Low 1. Condition : Good 3, Moderate 2, Poor 1. Années vers condition cible en création (G-6 colonnes E, G, I : Poor / Moderate / Good) : Native hedgerow 1 / 5 / 12 ; Native hedgerow with trees 1 / 10 / 20 ; Line of trees 5 / 20 / 30+ ; Non-native hedgerow 1 / impossible / impossible. Fiche 8A : 10 attributs en 5 groupes fonctionnels (hauteur et largeur > 1,5 m ; trous à la base ; bande non perturbée > 1 m et végétation nitrophile < 20 % ; EEE < 10 % et dommages < 10 % ; classes d'âge des arbres) ; Good = au plus 2 échecs et au plus 1 par groupe ; Moderate = au plus 4 échecs ; sinon Poor ; dérivée du Hedgerow Survey Handbook (Defra 2007).

Module cours d'eau (guide p. 41-55 ; tableur G-7) : unité km ; distinctiveness : Priority habitat V.High 8 ; Other rivers and streams High 6 ; Canals Medium 4 ; Ditches Medium 4 ; Culvert Low 2. Condition : River Condition Assessment par assesseur qualifié ; survey d'au moins 20 % de la longueur. Zone riveraine : 10 m depuis le haut de berge pour rivières et canaux, 5 m pour fossés (Table 12 p. 46). Empiétement dans le cours d'eau (Table 14 p. 51) : none 1,0 ; minor 0,8 ; major 0,5 ; culvert 0,68. Empiétement riverain (G-7 AD4:AE14) : Major/Major 0,75 ; Major/Moderate 0,8 ; Major/Minor 0,84 ; Major/None 0,87 ; Moderate/Moderate 0,85 ; Moderate/Minor 0,9 ; Moderate/None 0,92 ; Minor/Minor 0,95 ; Minor/None 0,98 ; None/None 1. Création, années vers condition cible (G-7 N3:O7) : Good 10, Fairly Good 8, Moderate 5, Fairly Poor 2, Poor 1. Risque spatial cours d'eau : même bassin 1,0 ; bassin opérationnel 0,75 ; au-delà 0,5 (Table 9 p. 39).

Risque spatial hors site, modules surfacique et haies (guide p. 39, Table 9 ; G-3 S3:T10) : Within 1,0 ; Neighbouring 0,75 ; Outside 0,5.

Fiches d'état, exemples prairies (Technical Annex 1) :
- Onglet « 5A.GRASSLAND LOW » (Modified grassland) : 7 critères A à G ; A essentiel (6 à 8 espèces vasculaires par m² dont au moins 2 dicotylédones) ; B structure de hauteur (au moins 20 % < 7 cm et 20 % > 7 cm) ; C ligneux < 20 % ; D dégâts physiques < 5 % ; E sol nu entre 1 % et 10 % ; F fougère aigle < 20 % ; G absence d'EEE. Good (3) = 6 ou 7 critères dont A ; Moderate (2) = 4 ou 5 dont A ; Poor (1) = 3 ou moins, ou 4 à 6 sans A.
- Onglet « 6A.GRASSLAND MED HIGH & V.HIGH » (dont Other neutral grassland) : critères A (bon exemple du type), B structure, C sol nu 1 à 5 %, D fougère < 20 % et ligneux < 5 %, E espèces de dégradation et dommages < 5 % (échec automatique si EEE), F pour les non acides : 10 espèces vasculaires ou plus par m². Prairies non acides (6 critères) : 5 ou 6 avec A et F = Good ; 3 à 5 avec A = Moderate ; sinon Poor.
- Fiche bois « 24A.WOODLAND » : 13 indicateurs notés 1 à 3, total sur 39 ; Good > 32, Moderate 26 à 32, Poor < 26.
- Règles générales (onglet INSTRUCTIONS) : pass/fail par critère ; en cas de limite de survey, critère présumé réussi à l'état initial et échoué en suivi ; catégories « fairly » limitées à un cran.

Trading rules (guide p. 16, Table 3) : Very high perdue : priorité au même type d'habitat, option « bespoke compensation » ; High : même type obligatoire ; Medium : même grand type en bande medium ou toute bande supérieure ; Low : même bande ou supérieure ; Very low : sans objet. Les règles ne s'appliquent que jusqu'au no net loss (guide p. 17). Habitats irremplaçables : exclus du calcul, compensation sur mesure obligatoire (guide p. 22-24). Cible par défaut du tableur : 10 % (guide p. 78, Table D).

Small Sites Metric (guide SSM p. 10) : 1 à 9 logements sur un site de 1 ha au plus, ou site < 0,5 ha ; commercial : surface de plancher créée < 1 000 m² ou site < 1 ha ; exclu si habitats prioritaires, sites protégés ou espèces protégées ; distinctiveness limitée à very low, low, medium ; condition affectée automatiquement à l'état initial ; unités en m² et m (p. 18) ; 2 multiplicateurs de risque seulement (difficulté et temporel) (p. 26). Tableur SSM 1.2.3, onglet « 10. Condition and Temporal » : condition initiale par défaut « Moderate » ; création Modified grassland Moderate 4 ans / Good 7 ; Other neutral grassland 5 / 10 ; Urban/rural tree 27 / 30+ ; Biodiverse green roof 5 / 10 ; green walls 3 / 5. Onglet « 11. Lists » : surfaces d'arbres en m² : Small 40,69 ; Medium 162,78 ; Large 366,25 ; Very Large 764,15.

#### Limites pour une transposition en France

1. Classification d'habitats : liste calée sur UKHab (niveaux 4 et 5), EUNIS pour l'intertidal, typologies DCE pour les lacs et Annexe I pour quelques habitats (guide p. 12 ; G-1 colonne C). UKHab est sous licence propre, hors OGL (guide p. 6) ; conditions non lues (403). Une transposition suppose une table de correspondance vers EUNIS / HIC / typologie française, qui n'existe pas dans les documents lus.
2. Bandes de distinctiveness : construites sur la rareté en Angleterre, la part en SSSI et le statut NERC Act s. 41 (TA2 p. 23-25). Les scores ne sont pas transférables tels quels ; seule la grille 8/6/4/2/0 et la logique des seuils le sont.
3. Strategic significance : dépend des Local Nature Recovery Strategies (guide p. 29-32). Équivalent à définir (SRADDET, trames vertes et bleues, PLU).
4. Condition : fiches dérivées du Common Standards Monitoring et du Farm Environment Plan (TA2 p. 50) ; listes d'espèces anglaises. Le RCA exige un assesseur certifié britannique.
5. Multiplicateur temporel : taux de 3,5 % issu du Treasury Green Book (TA2 p. 52) ; choix économique et non écologique, explicitement reconnu (« economic technique », § 5.3.1). Les délais vers condition cible sont « largely expert-driven » (TA2 p. 52, § 5.2.4), sans publication des données sous-jacentes.
6. Difficulté : jugements d'experts fondés sur des rapports Entec/Amec 2011-2016 non publiés sur la page (TA2 p. 56).
7. Cadre juridique : les 10 %, les 30 ans, les crédits statutaires relèvent du Schedule 7A TCPA 1990 ; sans équivalent direct dans la séquence ERC française.
8. Milieu urbain : valeur nulle de tout sol imperméabilisé, « vegetated garden » et « introduced shrub » figés en condition N/A (= 1), « other green roof » figé à 1 : conventions structurantes pour un projet de construction, contestées par Marshall et al. (2024). Le ratio 70:30 par défaut (guide p. 59) est une convention anglaise.
9. Habitats méditerranéens quasi absents : seul « Temporary lakes ponds and pools (H3170) » apparaît (guide p. 67 ; G-1 ligne 49).

Critiques scientifiques publiées (lues) :
- Marshall C. A. M. et al. (2024), « England's statutory biodiversity metric enhances plant, but not bird nor butterfly, biodiversity », Journal of Applied Ecology 61(8), 1918-1931, DOI 10.1111/1365-2664.14697, CC BY 4.0 (PDF lu intégralement). Résultats : les unités de l'état initial corrèlent avec la plupart des variables « plantes » mais avec aucune variable « oiseaux » ni « papillons » sur 24 sites ; 1 unité supplémentaire associée à + 1 % de richesse spécifique végétale ; un gain de 10 % « is likely to translate into small gains for plant biodiversity, and negligible gains for birds and butterflies ». Critiques de conception : (a) linéarité de l'échelle 8/6/4/2 alors que les relations écologiques sont log-linéaires ; proposition d'une relation de puissance 16/8/4/2 et 4/2/1 pour la condition ; (b) distinctiveness mélangeant rareté et menace ; (c) critères de condition hérités d'une perspective agricole ; (d) condition « N/A » (= 1) pour les cultures et les habitats urbains à faible distinctiveness jugée injustifiée ; (e) seuil de 10 % « appears to be arbitrary » ; (f) aucune donnée urbaine, aquatique ou linéaire, multiplicateurs non testés.
- zu Ermgassen S. O. S. E. et al. (2021), « Exploring the ecological outcomes of mandatory biodiversity net gain using evidence from early-adopter jurisdictions in England », Conservation Letters 14(6), e12820, DOI 10.1111/conl.12820, CC BY 4.0 (résumé et métadonnées lus ; article intégral non accessible). Sur les dossiers BNG de 6 collectivités (janvier 2020 à février 2021), réduction proposée de 34 % de la surface d'habitats non urbains, compensée par des promesses de condition plus élevée sur des surfaces plus petites ; environ 95 % des unités générées sur site ou en bordure, dans un « governance gap ».
- Rampling E. E. et al. (2024), Conservation Biology 38(2), e14198, DOI 10.1111/cobi.14198, CC BY 4.0 (notice lue) : environ 27 % des unités dans des lacunes de gouvernance ; environ 21 % des dossiers avec une erreur de calcul récurrente.
- Hawkins I. et al. (2022), In Practice (CIEEM) 118, 16-20, sans DOI : aucune relation cohérente entre scores et présence d'espèces prioritaires sur 110 habitats (bulletin professionnel).
- Critique spécifique de l'actualisation à 3,5 % dans un article évalué par les pairs : NON VÉRIFIÉ.

#### Ce qui manque

- Technical Annex 2 de la métrique statutaire : non publié ; la méthode repose sur l'annexe BM 4.0 de mars 2023.
- Données sources des délais vers condition cible et des difficultés (rapports Entec 2011, Entec et Amec 2013, Amec 2016) : non publiées sur les pages consultées.
- Conditions de licence UKHab : page inaccessible (403).
- Mention de licence à l'intérieur du tableur : absente.
- Fiches d'état non lues en détail : lacs, intertidal, zones humides, landes, vergers, mares, fossés, RCA.
- Matrice complète d'amélioration (G-5) : extraite partiellement.
- Article intégral de zu Ermgassen et al. 2021 : non accessible.

#### Sources consultées (2.1)

1. https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides : lue intégralement.
2. https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides/statutory-biodiversity-metric-tools-and-guides-version-history : lue intégralement.
3. https://assets.publishing.service.gov.uk/media/6a1d98e9c7335e2ca6daadd5/The_Statutory_Biodiversity_Metric_-_User_Guide_-_June_2026.pdf : lue intégralement (89 pages).
4. https://assets.publishing.service.gov.uk/media/689c5ee17b2e384441636196/The_Statutory_Biodiversity_Metric_-_User_Guide_-_July_2025.pdf : identique à la source 3.
5. https://assets.publishing.service.gov.uk/media/6867e62810d550c668de3b4e/The_Statutory_Metric_Macro_Disabled_1.0.4.xlsx : onglets G-1, G-3, G-4, G-6, G-7, G-8, Version History, formules A-1 et A-2 lus intégralement ; G-5 partiellement.
6. https://assets.publishing.service.gov.uk/media/689c5f19d2a1b0d5d1bb1254/Statutory_Biodiversity_Metric_Condition_Assessments_-_July_2025.xlsx : onglets INSTRUCTIONS, HABITAT DEFINITIONS (partiel), 5A, 6A, 8A, 9A, 22A, 24A, 27 lus.
7. https://assets.publishing.service.gov.uk/media/686677acdd1a7e01559e6d45/The_Small_Sites_Metric__Statutory_Biodiversity_Metric__-_User_Guide_July_2025.pdf : lue partiellement.
8. https://assets.publishing.service.gov.uk/media/6863f5ba08bf2f5376121aee/The_Small_Sites_Metric_1.2.3.xlsm : onglets 9, 10, 11, 12 et 1 lus partiellement.
9. https://publications.naturalengland.org.uk/publication/6049804846366720 : lue intégralement.
10. https://publications.naturalengland.org.uk/file/5749350878412800 (BM 4.0 Technical Annex 2, JP039, mars 2023) : lue partiellement (p. 1-3, 23-26, 50-57, 65-67, 69-74).
11. https://publications.naturalengland.org.uk/file/4542050687778816 (Habitat Guide SSM HMMP, JP058, avril 2024) : lue partiellement.
12. https://www.legislation.gov.uk/ukpga/2021/30/schedule/14 : lue partiellement (paragraphes 2, 4 et 9 du Schedule 7A).
13. https://www.gov.uk/guidance/understanding-biodiversity-net-gain : lue partiellement.
14. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ : lue intégralement.
15. https://ukhab.org/licensing/ : non accessible (403).
16. https://eprints.glos.ac.uk/15391/ et PDF Marshall et al. 2024 : lus intégralement.
17. https://api.crossref.org/works/10.1111/1365-2664.14697 ; https://api.crossref.org/works/10.1111/conl.12820 ; https://api.crossref.org/works/10.1111/cobi.14198 : lues.
18. https://doaj.org/article/181442d7277a44f0af15647b4b6e87ca (zu Ermgassen et al. 2021, résumé) : lue ; https://doi.org/10.1111/conl.12820 : non accessible.
19. https://cieem.net/wp-content/uploads/2021/03/Exploring-the-ecological-outcomes-of-mandatory-Biodiversity-Net-Gain-using-evidence-from-early-adopter-jurisdictions-in-England.pdf : lue intégralement.
20. https://ora.ox.ac.uk/objects/uuid:01b99121-202f-4f7a-a8e2-2e0f3859c359 (Rampling et al.) et https://ora.ox.ac.uk/objects/uuid:d0f359e9-f9f5-4a61-ba1d-f6ba5a8943fb (Hawkins et al. 2022) : notices lues.
21. https://www.repository.cam.ac.uk/items/756d33c3-da61-4e1d-8d92-54bfcf4aa210 : notice lue.

### 2.2 Méthodes allemandes de valeur de biotopes (Biotopwertverfahren)

Date de consultation de toutes les sources : 17/10/2026.
Règle appliquée : aucune valeur de mémoire. Chaque nombre ci-dessous a été lu dans un document récupéré (HTML brut, XLSX ou PDF téléchargé et converti en texte, ou page rasterisée et lue visuellement). Lorsqu'une source primaire n'a pas pu être lue, la mention "NON VÉRIFIÉ : page non accessible" est portée.

#### 1. Objet

Documenter, à partir des textes et listes officiels, 4 méthodes allemandes d'évaluation des biotopes par points utilisées pour dimensionner la compensation écologique (Eingriffsregelung, § 13 à § 17 BNatSchG) :

1. Bundeskompensationsverordnung (BKompV, Bund, 2020), Anlage 2 "Liste der Biotoptypen und -werte".
2. Kompensationsverordnung de Hesse (KV, 2018), Anlage 3 "Wertliste nach Nutzungstypen".
3. Bayerische Kompensationsverordnung (BayKompV, 2013) et Biotopwertliste bavaroise (StMUV / LfU, 2014).
4. Nordrhein-Westfalen, "Numerische Bewertung von Biotoptypen für die Eingriffsregelung in NRW" (LANUK, Arbeitsblatt 61, 2026 ; historique LANUV 2008).

Pour chacune : échelle, structure de la liste, formule de calcul, valeurs de biotopes urbains et périurbains, règles temporelles (durée de développement, timelag) et de risque, statut juridique, licence, format de diffusion.

#### 2. Accès et licence

##### 2.1 Tableau d'accès

| Méthode | Document | URL exacte | Statut de lecture le 17/10/2026 |
|---|---|---|---|
| BKompV | Texte intégral (toutes les Anlagen) | https://www.gesetze-im-internet.de/bkompv/BJNR108800020.html | Lu intégralement (HTML brut, 690 Ko) |
| BKompV | Table des matières | https://www.gesetze-im-internet.de/bkompv/index.html | Lue intégralement |
| BKompV | § 5 (Grundbewertung Biotope) | https://www.gesetze-im-internet.de/bkompv/__5.html | Lu intégralement |
| BKompV | § 7, § 8, § 9, § 12, § 13, § 14, § 17, § 18 | https://www.gesetze-im-internet.de/bkompv/__7.html (et __8, __9, __12, __13, __14, __17, __18) | Lus intégralement |
| BKompV | Anlage 1 (weitere Schutzgüter) | https://www.gesetze-im-internet.de/bkompv/anlage_1.html | Lue intégralement |
| BKompV | Anlage 2 (Biotopwertliste) | https://www.gesetze-im-internet.de/bkompv/anlage_2.html | Lue intégralement : 889 lignes de tableau extraites, 668 lignes porteuses d'une valeur |
| BKompV | Anlage 3 (Erheblichkeit) | https://www.gesetze-im-internet.de/bkompv/anlage_3.html | Lue intégralement |
| BKompV | Anlage 5 (Abschnitt B : Entwicklungszeiten, Timelag-Aufschlag) | https://www.gesetze-im-internet.de/bkompv/anlage_5.html | Lue intégralement |
| BKompV | Anlage 6 (Maßnahmen) | https://www.gesetze-im-internet.de/bkompv/anlage_6.html | Lue intégralement (30 262 caractères) |
| BKompV | Export XML (zip) | https://www.gesetze-im-internet.de/bkompv/xml.zip | Téléchargé (538 681 octets), non exploité |
| BKompV | Handreichung zum Vollzug der BKompV (BfN / BMU, 11/2021) | https://epflicht.ulb.uni-bonn.de/download/pdf/692898 | Téléchargée (103 pages), lue partiellement (recherche par mots-clés) |
| Hesse KV 2018 | Texte intégral avec Anlagen 1 à 4 (source secondaire, éditeur privé Lexaris) | https://www.lexaris.de/book/version/documentflat/head/1329058 | Lu intégralement |
| Hesse KV 2018 | Source officielle hessenrecht | https://www.rv.hessenrecht.hessen.de/bshe/document/jlr-KompVHE2018rahmen | NON VÉRIFIÉ : page non accessible (curl : "Connection reset by peer" ; WebFetch : ROBOTS_DISALLOWED) |
| Hesse KV 2018 | Page thématique du ministère | https://umwelt.hessen.de/naturschutz/eingriffsregelung-und-kompensation | NON VÉRIFIÉ : page non accessible (CLIENT_ERROR) |
| Hesse KV 2018 | "Einführung in die Kompensationsverordnung 2018" (umweltministerium.hessen.de) | https://umweltministerium.hessen.de/sites/umwelt.hessen.de/files/2021-08/einfuehrung_in_die_kompensationsverordnung_2018.pdf | NON VÉRIFIÉ : HTTP 404 |
| Hesse KV 2018 | Bilan réel appliquant la KV 2018 (RP Gießen, autorité du Land, Stand 31.10.2025) | https://rp-giessen.hessen.de/sites/rp-giessen.hessen.de/files/2026-07/u19.1_03.1_kv-bilanz_anlage_3.1.pdf | Lu via WebFetch (contrôle croisé de valeurs) |
| Hesse KV 2005 (abrogée) | Archive umwelt-online | https://umwelt-online.de/recht/natursch/laender/he/kv.htm | Lue intégralement (sert uniquement de comparaison historique) |
| Hesse KV 2018 | Extrait umwelt-online (démo) | https://umwelt-online.de/recht/natursch/laender/he/kv18.htm | Lue partiellement (en-tête et § 1 seulement ; le reste est réservé aux abonnés) |
| Bavière | BayKompV, page d'accueil et table des matières | https://www.gesetze-bayern.de/Content/Document/BayKompV | Lue intégralement |
| Bavière | BayKompV § 4, § 7, § 8, § 9, § 24 | https://www.gesetze-bayern.de/Content/Document/BayKompV-4 (et -7, -8, -9, -24) | Lus intégralement |
| Bavière | BayKompV Anlage 3.1 | https://www.gesetze-bayern.de/Content/Document/BayKompV-ANL_5 | Lue intégralement |
| Bavière | BayKompV Anlage 3.2 | https://www.gesetze-bayern.de/Content/Document/BayKompV-ANL_6 | Lue intégralement |
| Bavière | Vollzugshinweise (Bekanntmachung StMUV 14.10.2015, Stand 09.01.2025) | https://www.gesetze-bayern.de/Content/Document/BayVwV319722/true | Lue intégralement (texte de la Bekanntmachung ; les Anlagen sont des PDF séparés) |
| Bavière | Biotopwertliste (PDF, Stand 28.02.2014, red. Änd. 31.03.2014), 24 pages | https://www.stmuv.bayern.de/themen/naturschutz/eingriffe/doc/biotopwertliste.pdf | Lue intégralement (texte extrait + pages 8, 9, 11 rasterisées et lues) |
| Bavière | Page LfU Kompensationsverordnung | https://www.lfu.bayern.de/natur/kompensationsverordnung/index.htm | Lue via WebFetch |
| NRW | LANUK-Arbeitsblatt 61 (PDF, 52 pages, Stand März 2026, Veröffentlichung Juli 2026) | https://www.lanuk.nrw.de/fileadmin/lanuvpubl/4_arbeitsblaetter/Arbeitsblatt_61.pdf | Lu intégralement (texte extrait, page 27 rasterisée) |
| NRW | Biotoptypenliste en tableur (XLSX) | https://www.lanuk.nrw.de/fileadmin/lanuv/natur/uploads/Biotoptypenliste_Numerische_Bewertung_Eingriffsregelung_aktuell_01.xlsx | Téléchargé et lu (1 399 lignes, 3 feuilles ; métadonnées : créé 27.08.2007, modifié 01.10.2025 par "Jung, Robert") |
| NRW | Page LANUK "Numerische Bewertung von Biotoptypen" | https://www.lanuk.nrw.de/themen/natur/eingriffsregelung/numerische-bewertung-von-biotopraeumen | Téléchargée (liens de téléchargement extraits) |
| NRW | Version LANUV septembre 2008 (copie hébergée par la préfecture du Territoire de Belfort) | https://www.territoire-de-belfort.gouv.fr/index.php/contenu/telechargement/24544/177227/file/Num_Bew_Biotyp_NRW_Sept2008.pdf | NON VÉRIFIÉ : page non accessible (curl erreur 92 HTTP/2 ENHANCE_YOUR_CALM) |
| NRW | Version juin 2021 (copie Kreis Soest) | https://kreis-soest.de/fileadmin/citko_buerger/Dateien/Numerische_Bewertung_von_Biotoptypen_fuer_die_Eingriffsregelung_Stand_Juni_2021.pdf | NON VÉRIFIÉ : HTTP 404 |
| NRW | Version ULB Münster (epflicht) | https://epflicht.ulb.uni-muenster.de/download/pdf/131330 | NON VÉRIFIÉ : page anti-robot, contenu non délivré |
| Licence | § 5 UrhG | https://www.gesetze-im-internet.de/urhg/__5.html | Lu intégralement |
| Licence | Hinweise gesetze-im-internet.de | https://www.gesetze-im-internet.de/hinweise.html | Lues (section 6 "Download und Weiterverwertung der Normen", section 7 "Verlinkung") |

##### 2.2 Statut juridique de chaque méthode (tel que lu)

- BKompV : Rechtsverordnung du Bund. En-tête lu sur gesetze-im-internet : "Ausfertigungsdatum: 14.05.2020", "Bundeskompensationsverordnung vom 14. Mai 2020 (BGBl. I S. 1088), die durch Artikel 4 des Gesetzes vom 22. Dezember 2025 (BGBl. 2025 I Nr. 351) geändert worden ist", "Textnachweis ab: 3.6.2020". Base légale : § 15 Absatz 8 BNatSchG (Eingangsformel). Champ : "soweit die Vorschriften des Dritten Kapitels des Bundesnaturschutzgesetzes ... ausschließlich durch die Bundesverwaltung ausgeführt werden" (§ 1 Abs. 1). Mention en tête du texte : "Abweichendes Landesrecht: Bayern - Abweichung durch § 1 Abs. 1 Satz 1 u. 3 der Bayerischen Kompensationsverordnung (BayKompV) v. 7.8.2013".
- Hesse KV : Rechtsverordnung du Land. Intitulé lu : "Verordnung über die Durchführung von Kompensationsmaßnahmen, das Führen von Ökokonten, deren Handelbarkeit und die Festsetzung von Ersatzzahlungen (Kompensationsverordnung - KV) Vom 26. Oktober 2018", "Gesamtausgabe in der Gültigkeit vom 10.11.2018 bis 31.12.2026", "letzte berücksichtigte Änderung: Berichtigung vom 1.2.2019 (GVBl. S. 19)". Base : § 34 HAGBNatSchG et § 17 Abs. 11 BNatSchG. § 10 : "Diese Verordnung tritt am Tag nach der Verkündung in Kraft. Sie tritt mit Ablauf des 31. Dezember 2026 außer Kraft." La référence GVBl. de publication (p. 652, GVBl. Nr. 24 du 09.11.2018) n'a été lue que sur l'extrait umwelt-online kv18.htm, pas sur le site officiel : à confirmer sur hessenrecht.
- BayKompV : Rechtsverordnung du Land. En-tête lu : "Verordnung über die Kompensation von Eingriffen in Natur und Landschaft (Bayerische Kompensationsverordnung - BayKompV) Vom 7. August 2013 (GVBl. S. 517) BayRS 791-1-4-U", "die durch § 2 des Gesetzes vom 23. Juni 2021 (GVBl. S. 352) geändert worden ist", "Text gilt ab: 03.06.2020". § 24 : "Diese Verordnung tritt am 1. September 2014 in Kraft."
- Biotopwertliste bavaroise : Verwaltungsvorschrift (Bekanntmachung). Lu : "Bekanntmachung des Bayerischen Staatsministeriums für Umwelt und Verbraucherschutz vom 14. Oktober 2015, Az. 62-U8680.11-2014/1-3 (AllMBl. S. 443)", "zuletzt durch Bekanntmachung vom 12. Dezember 2024 (BayMBl. 2025 Nr. 4) geändert", point 1 : la liste "liefert die Grundlage zur Umsetzung des in der BayKompV festgelegten Biotopwertverfahrens (Stand: 28. Februar 2014; redaktionelle Änderungen 31. März 2014)". Le PDF lui-même indique "Die Biotopwertliste ist die maßgebliche Grundlage für die Anwendung des Biotopwertverfahrens nach der BayKompV" (p. 3).
- NRW : document technique d'un Landesamt (guide), pas un règlement. Lu dans l'Impressum : "Herausgeber Landesamt für Natur, Umwelt und Klima Nordrhein-Westfalen (LANUK NRW)", "Stand März 2026", "Veröffentlichung Juli 2026", "ISSN 3052-8569 (Online), LANUK-Arbeitsblätter". Le texte (p. 4) rappelle que 4 méthodes ont été utilisées en NRW (Adam/Nohl/Valentin 1986 ; ARGE Eingriff/Ausgleich 1994 ; Ludwig/Meinig 1991 ; Froelich & Sporbeck et al. 2002) et que le document harmonise leurs listes.

##### 2.3 Licence de réutilisation

- § 5 UrhG, texte lu intégralement : "(1) Gesetze, Verordnungen, amtliche Erlasse und Bekanntmachungen sowie Entscheidungen und amtlich verfaßte Leitsätze zu Entscheidungen genießen keinen urheberrechtlichen Schutz. (2) Das gleiche gilt für andere amtliche Werke, die im amtlichen Interesse zur allgemeinen Kenntnisnahme veröffentlicht worden sind, mit der Einschränkung, daß die Bestimmungen über Änderungsverbot und Quellenangabe in § 62 Abs. 1 bis 3 und § 63 Abs. 1 und 2 entsprechend anzuwenden sind."
- Conséquence lue dans le texte même : la BKompV, la KV Hesse et la BayKompV, y compris leurs Anlagen (listes de valeurs), sont des "Verordnungen" au sens de § 5 Abs. 1 UrhG ; la Biotopwertliste bavaroise est publiée par "Bekanntmachung" (AllMBl. S. 443), ce qui relève également de § 5 Abs. 1 ("amtliche ... Bekanntmachungen"). L'appréciation juridique définitive de l'applicabilité de § 5 Abs. 1 ou Abs. 2 à chaque document n'est pas une donnée lue : c'est une qualification à faire valider.
- gesetze-im-internet.de, Hinweise section 6 (lu) : les textes sont fournis en HTML, PDF, EPUB et XML ; "Das XML-Format ... ist insbes. für die Nutzer geeignet, die die hier zur Verfügung gestellten Gesetze und Rechtsverordnungen über automatisierte Verfahren weiterverarbeiten möchten", DTD publique www.gesetze-im-internet.de/dtd/1.01/gii-norm.dtd ; section 7 : "Eine Verlinkung auf Inhalte von Gesetze im Internet (sog. Deep Links) ist ausdrücklich erlaubt." L'Impressum de gesetze-im-internet.de ne contient aucune clause de licence (lu).
- gesetze-bayern.de : l'Impressum ne contient aucune clause de droits d'auteur ni de réutilisation (lu).
- NRW Arbeitsblatt 61, Impressum (lu, p. 52) : "Nachdruck - auch auszugsweise - ist nur unter Quellenangaben und Überlassung von Belegexemplaren nach vorheriger Zustimmung des Herausgebers gestattet. Die Verwendung für Werbezwecke ist grundsätzlich untersagt." Ce document n'est donc pas placé sous licence libre par son éditeur ; sa nature d'oeuvre officielle au sens de § 5 Abs. 2 UrhG n'est pas affirmée dans le document. Aucune mention de licence sur le tableur XLSX (métadonnées lues).
- Biotopwertliste bavaroise (PDF) : métadonnées lues "Author: Dr. Ingo Hetzel (Bosch & Partner)", "CreationDate: 13.05.2014" ; aucune mention de licence dans le PDF ni sur la page LfU (lue via WebFetch : "aucune mention").
- Lexaris (Hesse) : site privé ; les conditions de réutilisation du site n'ont pas été lues. Le texte reproduit est celui d'une Verordnung (§ 5 Abs. 1 UrhG) mais la mise en forme Lexaris n'est pas la publication officielle.

##### 2.4 Disponibilité en tableur ou en PDF seulement

- BKompV Anlage 2 : HTML (tableau), PDF, EPUB et XML (zip téléchargé, 538 681 octets). Pas de tableur officiel, mais le XML est structuré et destiné au retraitement automatisé (Hinweise, section 6).
- Hesse Anlage 3 : HTML sur Lexaris (tableau), PDF officiel non accessible depuis cet environnement. L'Anlage 4 n° 4 de la KV prévoit : "Die Ausgleichsberechnung ist nach den von der obersten Naturschutzbehörde vorgeschriebenen Vordrucken vorzunehmen" ; ces Vordrucke (formulaires) n'ont pas été trouvés en accès direct.
- Bavière : PDF uniquement (24 pages, tableau sur les pages 15 à 24). La page LfU lue ne mentionne aucune version Excel ou CSV ; seule une "Arbeitshilfe zur Biotopwertliste - Verbale Kurzbeschreibungen (07/2014)" et une "Übersicht über die neuen Biotoptypen-Zuordnungen" sont citées.
- NRW : PDF (Arbeitsblatt 61) et tableur XLSX officiel (3 feuilles "Tabelle1" à "Tabelle3", 1 399 lignes dans la feuille 1).

#### 3. Structure de chaque méthode

##### 3.1 BKompV (Bund, 2020)

- Échelle : Biotoptypenwert de 0 à 24 (lu : minimum 0 pour 9 lignes, maximum 24 pour 7 lignes sur 668 lignes valorisées de l'Anlage 2 ; valeur 24 pour p. ex. 43.08.04A "Buchenbuschwald (auf Ostseedünen), alte Ausprägung").
- Colonnes de l'Anlage 2 (lues) : "Code", "Biotoptyp", "Biotop-typenwert". 3 colonnes seulement ; aucune colonne "Wiederherstellbarkeit", "Entwicklungsdauer" ou "Regenerationsfähigkeit". Les stades d'âge sont exprimés par des sous-lignes avec suffixe J / M / A ("Junge / Mittlere / Alte Ausprägung") sur le code, p. ex. 41.05aJ = 11, 41.05aM = 15, 41.05aA = 18. Aucune légende des lettres J, M, A ni des suffixes a, b, c n'est présente dans l'Anlage 2 (vérifié).
- Codes : numériques hiérarchiques à 2 à 6 niveaux (p. ex. 02.01.04.01.01.03), avec suffixes alphabétiques (a, b, c, n) et J/M/A/MA. 889 lignes de tableau, dont des lignes de titre sans valeur.
- § 5 Abs. 1 (lu) : affectation de chaque biotope à un Biotoptyp (Spalte 2) puis à son Biotoptypenwert (Spalte 3) ; "Im Einzelfall kann der Biotoptypenwert nach Anlage 2 Spalte 3 um bis zu drei Wertpunkte erhöht werden, wenn das Biotop überdurchschnittlich gut ausgeprägt ist, oder um bis zu drei Wertpunkte verringert werden, wenn das Biotop unterdurchschnittlich gut ausgeprägt ist", sur 3 critères : "die Flächengröße", "die abiotische und die biotische Ausstattung", "die Lage zu anderen Biotopen". La somme donne le "Biotopwert".
- § 5 Abs. 2 (lu), classes de signification : 0 à 4 "sehr gering" ; 5 à 9 "gering" ; 10 à 15 "mittel" ; 16 à 18 "hoch" ; 19 à 21 "sehr hoch" ; 22 à 24 "hervorragend".
- § 5 Abs. 3 et 4 (lus) : intensité des effets classée "gering / mittel / hoch" ; pour les effets indirects, facteur de 0,1 à 1 (0,1 à 0,3 = gering ; 0,4 à 0,6 = mittel ; 0,7 à 1 = hoch). Anlage 3 (lue) : matrice signification (1 à 6) x intensité (I à III) donnant "-", "eB" (erhebliche Beeinträchtigung) ou "eBS" (besonderer Schwere) ; p. ex. ligne "2 gering" : "- / - / eB" ; ligne "4 hoch" : "eB / eB / eBS" ; ligne "6 hervorragend" : "eBS / eBS / eBS".
- Formule du besoin de compensation, § 7 Abs. 1 (lu) : pour une emprise, "die Differenz zwischen den Biotopwerten des vorhandenen Zustands und des nach dem Eingriff zu erwartenden Zustands zu bilden und mit der voraussichtlich beeinträchtigten Fläche in Quadratmetern zu multiplizieren" ; pour les effets indirects : Biotopwert x surface x facteur (§ 5 Abs. 4). La somme des produits = "biotopwertbezogener Kompensationsbedarf".
- Formule du gain, § 8 Abs. 2 (lu) : "Differenz zwischen den Biotopwerten des zu erreichenden Zustands (Zielbiotop) und des vorhandenen Zustands (Ausgangsbiotop) multipliziert mit der aufgewerteten Fläche in Quadratmetern".
- Bonus désimperméabilisation, § 8 Abs. 3 (lu) : "zusätzlich 30 Wertpunkte je Quadratmeter aufgewerteter Fläche" lorsque la revalorisation est liée à une Entsiegelung. Anlage 6 Abschnitt B (lu) : "Mindestgröße 100 m2", enlèvement complet du revêtement et de la fondation.
- Plafond, § 8 Abs. 4 (lu) : sur les surfaces agricoles à forte part de biotopes de valeur (16 ou plus), revalorisation possible de 3 à 6 points ; "Eine höhere Wertpunktzahl als 24 Punkte kann jedoch nicht erreicht werden."
- Ersatzzahlung, § 14 (lu) : fondée sur les coûts moyens des mesures et les Bodenrichtwerte (§ 196 BauGB) ; barèmes forfaitaires pour le Landschaftsbild (p. ex. mâts : 100 à 800 euros par mètre de hauteur selon la Wertstufe 2 à 6 ; bâtiments : 0,01 à 0,08 euro par m3). Il n'existe pas dans la BKompV de prix en euros par Wertpunkt de biotope (vérifié dans § 13 et § 14).
- Anlage 1 (lue) : les autres Schutzgüter (Tiere, Pflanzen, Boden, Wasser, Klima/Luft, Landschaftsbild) sont évalués sur 6 Wertstufen (1 "sehr gering" à 6 "hervorragend"), de façon verbale-argumentative, pas en points par m2.

##### 3.2 Hesse, KV 2018, Anlage 3

- Échelle : "WP je qm" (Wertpunkte je Quadratmeter) de 3 à 80 (lu : 305 lignes de types codés, 243 porteuses d'une valeur ; minimum 3, p. ex. 10.510, 10.520, 10.710, 05.120 ; maximum 80 pour 08.100 "Hochmoore", 08.300, 08.400).
- Colonnes (lues) : "Typ-Nr.", "Restriktionen", "Überschirmung", "Standard-Nutzungstyp", "Lebensraumtyp i. S. der Anlage 1 der Richtlinie 92/43/EWG", "Gesetzlich geschütztes Biotop (§ 30 BNatSchG und § 13 HAGBNatSchG)", "WP je qm".
- Codes : numériques à 5 chiffres "xx.yyy" (p. ex. 10.720). Restrictions (lues) : "B" = type à utiliser pour l'état existant ; "(B)" = utilisable pour les mesures seulement sous conditions ; "E" = planifiable uniquement comme mesure de compensation ; "°" = "Überschirmung" : les points de la surface surplombée (houppier) s'ajoutent à ceux du type sous-jacent.
- Règle de surface des houppiers pour les plantations (lue, en tête du groupe 04) : "unter 16 cm" de circonférence à 1 m = 1 qm ; "ab 16 cm bis unter 20 cm" = 3 qm ; "ab 20 cm" = 5 qm.
- Formule : la KV ne l'écrit pas sous forme d'équation, mais Anlage 2 n° 1.2 (lu) impose de ventiler les surfaces par Nutzungstyp "entsprechend der Wertliste (Anlage 3)" et d'inscrire les parts de surface dans l'Ausgleichsberechnung ; Anlage 2 n° 3 (lu) : "Die Ersatzzahlung wird durch Vervielfachung der Summe der nach Nr. 1 und gegebenenfalls nach Nr. 2 errechneten WP mit dem Betrag der durchschnittlichen Aufwendungen für Ersatzmaßnahmen nach § 6 berechnet." Le contrôle sur un bilan officiel du RP Gießen (lu via WebFetch, Stand 31.10.2025) confirme la règle Biotopwertpunkte = Fläche (m2) x WP/qm, formules "Sp. 3 x Sp. 4" dans le formulaire ; exemples : 10.510, 3 WP x 6 584 m2 = 19 752 ; 02.510, 30 WP x 5 605 m2 = 168 150.
- État de référence pour la planification (lu, Anlage 2 n° 1.2) : "Bei der Ausgleichsplanung ist der Zustand zu bewerten, der bei plangemäßer Pflege drei Vegetationsperioden nach Herstellung der Kompensationsmaßnahme zu erwarten ist."
- Zusatzbewertung (lu, Anlage 2 n° 2) : uniquement si la Grundbewertung est "offenbar falsch oder erheblich unvollständig" ; 8 Beurteilungsgrößen (Landschaftsbild, Vernetzung/Zerschneidung, Klimawirkungen, geschützte Arten/biologische Vielfalt, Bodenfunktion, sonstige Randwirkungen, besondere örtliche Situation, invasive Pflanzenarten). N° 2.3 : "kleinste Einheit sind 0,5 WP je qm" ; schéma à 3 niveaux "Gering (1 WP je qm), mittel (2 WP je qm), hoch (3 WP je qm)" ; "Je Beurteilungsgröße können maximal 3 WP je qm Zuschlag oder Abschlag vergeben werden. Insgesamt können bis zu 10 WP je qm Zuschlag oder Abschlag vergeben werden." Sols : "je angefangene 10 EMZ über beziehungsweise unter der ... Grenze ein Zuschlag von 3 WP je qm" ; "Eingriffe in Archivböden oder Bodendenkmäler werden immer mit einem Aufschlag von 3 WP je qm bewertet". Invasives : "je 10% Deckungsgrad um einen Abschlag in Höhe von 1 WP je qm" ; élimination durable créditée "mit bis zu 10 WP je qm Zuschlag". Doublement possible de la Zusatzbewertung pour les mesures bénéficiant à un Naturschutzgebiet, Nationalpark ou site Natura 2000.
- Ersatzzahlung, § 6 (lu) : "0,40 Euro je Wertpunkt, zuzüglich eines regionalen Bodenwertanteils" ; Bodenwertanteil = "10 Prozent des durchschnittlichen Kaufwerts landwirtschaftlicher Grundstücke in Euro pro Quadratmeter" du Landkreis.
- Mesures (lu, § 2 Abs. 5) : achèvement "spätestens drei Jahre nach Eingriffsbeginn" ; à défaut, Ersatzzahlung complémentaire.

##### 3.3 Bavière, BayKompV 2013 et Biotopwertliste 2014

- Échelle : Wertpunkte de 0 à 15 (lu, Biotopwertliste p. 6 : "Der Grundwert der Biotop- und Nutzungstypen in Wertpunkten von 0 und 15 gem. Anlage 3.1 BayKompV ergibt sich ... aus der Addition dieser drei Einzelbewertungen ohne Gewichtung"). Classes (lu, p. 6) : "hoch" 11 à 15 ; "mittel" 6 à 10 ; "gering" 1 à 5 ; "keine naturschutzfachliche Bedeutung" 0.
- Construction du Grundwert (lu, p. 6 à 9) : 3 critères notés chacun de 0 à 5 et additionnés sans pondération : Seltenheit/Gefährdung (G), Wiederherstellbarkeit/Ersetzbarkeit (W), Natürlichkeit (N). Exemple lu : F15 "Nicht oder gering veränderte Fließgewässer" = 4 + 5 + 5 = 14.
- Colonnes de la liste (lues, en-tête des pages 15 à 24) : colonnes 1 à 3 = hiérarchie du Biotop-/Nutzungstyp (Obergruppe, Typ, Untertyp) ; colonne 4 = classe (hoch/mittel/gering/keine) ; colonne 5 = "Grundwert" avec marquage "*" (W = 4) ou "**" (W = 5) ; colonne 6 = "+ 1 WP" (Zusatzbewertung) ; colonne 7 = "Typ nach BK oder FFH-LRT" ("x" toujours, "(x)" possible) ; colonne 8 = codes Biotopkartierung / FFH.
- Codes : une lettre d'Obergruppe plus jusqu'à 3 chiffres (lu, p. 4 : "z. B. S112"), combinés le cas échéant au code BK ou LRT (p. ex. "S112-SU3160").
- Majoration de 1 point (lu, chap. 1.3.2) : pour les types marqués "(x)" et "+", "um einen Wertpunkt erhöht, sofern es sich bei dem Biotop- und Nutzungstyp tatsächlich um ein gesetzlich geschütztes Biotop, einen FFH-Lebensraumtyp oder ein Biotop gem. Biotopkartierung Bayern handelt". Pas d'autre marge d'appréciation en points sur le Grundwert ; la valorisation d'une richesse spécifique exceptionnelle est "verbal-argumentativ" (§ 4 Abs. 3 Satz 1 Nr. 2 BayKompV, lu).
- Formule du besoin, Anlage 3.1 (lue) : "Kompensationsbedarf ... in Wertpunkten (Spalte 4) = Quadratmeter beeinträchtigte Fläche durch den Eingriff x Wertpunkte (Spalte 2) x Beeinträchtigungsfaktor (Spalte 3)". Beeinträchtigungsfaktor (lu) : "hoch" = 1 ; "mittel" = 0,7 ; "gering" = 0,4 ; "nicht erheblich" = 0 ; pour la classe 0 ("keine naturschutzfachliche Bedeutung") : "kein Kompensationsbedarf erforderlich".
- Formule du gain, Anlage 3.2 (lue) : "Kompensationsumfang in Wertpunkten (Kompensationsfläche m2 x Spalte 3)" avec Spalte 3 = "Prognosezustand nach 25 Jahren Entwicklungszeit" (Spalte 2) moins "Ausgangzustand" (Spalte 1). "Wertpunkte werden nur für die Aufwertung der Fläche vergeben".
- Restriction d'usage de la section urbaine (lu, p. 23) : "mit Ausnahme von P1, P43, V23, V33 und V5 sind alle nachfolgenden Typen nur bei der Ermittlung des Kompensationsbedarfs auf der Eingriffsseite zu verwenden und können nicht als Zielbiotope herangezogen werden".

##### 3.4 NRW, LANUK-Arbeitsblatt 61 (2026)

- Échelle : 0 à 10 (lu, chap. 2.1 : "Die numerische Bewertung der Biotoptypen erfolgt auf einer Skala von 0-10" ; contrôle sur le XLSX : 151 valeurs numériques, minimum 0, maximum 10). Une valeur décimale existe : "Solarmodul (überschirmte Fläche)" = 1,5.
- Critères (lus, chap. 2.1 et Anhang 3.1) : Natürlichkeit, Gefährdung/Seltenheit, Ersetzbarkeit/Wiederherstellbarkeit, Vollkommenheit ; "Gleichgewichtung" ; "Der Gesamtwert des Biotoptyps ergibt sich durch arithmetische Mittelwertbildung (gerundet) der vier Kriterien." Exemples de Tabelle 2 (lus) : "Acker, intensiv, Wildkrautarten weitgehend fehlend" : 2 / 1 / 2 / 1 = 2 ; "Artenreiche Mähwiese, mittel bis schlecht ausgeprägt" : 5 / 3 / 5 / 6 = 5 ; "Quelle, Bach, Fluss, bedingt naturfern" : 5 / 8 / 4 / 4 = 5. Les termes "Grundwert" et "Gesamtkorrekturfaktor" n'apparaissent pas dans l'Arbeitsblatt 61 (recherche plein texte : aucune occurrence de "Korrekturfaktor" ; "Grundwert" n'apparaît pas non plus). Le document parle de "Gesamtwert" / "Gesamtbiotopwert" et de "Wertvorschlag".
- Colonnes de la Tabelle 1 (lues) : "Code", "Biotoptyp (mit Codierung)", "Biotopwert", "§ 30 BNatSchG / § 42 LNatSchG NRW", "nicht ausgleichbar / Sonderstandort", "Potenzieller Lebensraumtyp (FFH-LRT, N-LRT)", "Lebensräume planungsrelevanter Arten".
- Codes : codes du Biotoptypenschlüssel LANUV (lettres, p. ex. HN, BD5, EA3) complétés de Zusatzcodes après virgule (p. ex. "...,ta3-5", "...,xd3,mq1", "...,me1/me2").
- Marge d'appréciation (lue, chap. 2.2) : "Von dem Bewertungsvorschlag der Biotoptypen kann je nach naturräumlicher Ausstattung, Bedeutung, Seltenheit und Naturnähe in Ausnahmefällen mit textlicher Begründung um bis zu zwei Wertstufen nach unten oder oben bis zum Minimal- bzw. Maximalwert des jeweiligen Biotoptyps abgewichen werden" ; plus des "Aufschlag um 1 Wertpunkt" ciblés (Acker et Ackerbrachen pour la flore de Liste rouge ; Säume ; Gärten "parkartig, strukturreich" ; Brachen avec RL-Pflanzenarten n > 2) et "Abschlag um 1 Wertpunkt, aber nicht kleiner als den Minimalbiotopwert 3" pour les jeunes peuplements forestiers isolés.
- Formule du bilan : l'Arbeitsblatt 61 ne contient pas d'équation explicite "surface x valeur" (vérifié) ; il fournit les valeurs et les Prognosewerte, le bilan surface x valeur étant celui des procédures cadres (ARGE 1994 et suivantes, citées p. 4).

#### 4. Valeurs disponibles

Toutes les valeurs ci-dessous ont été lues dans le document indiqué. "Ligne" = numéro de ligne (à partir de 1, en-tête compris) du tableau extrait de l'Anlage 2 (HTML brut, fichier anlage_2_rows.txt), "p." = page du PDF.

##### 4.1 BKompV, Anlage 2 (échelle 0 à 24), document : Anlage 2 (zu § 5 Absatz 1), BGBl. I 2020, 1100 à 1122, URL https://www.gesetze-im-internet.de/bkompv/anlage_2.html

| Code | Biotoptyp (verbatim) | Valeur | Ligne du tableau |
|---|---|---|---|
| 52.01.01a | Versiegelter oder sonstiger gepflasterter Verkehrs- und Betriebsweg (z. B. Straße, Start-, Landebahn) | 0 | 747 |
| 52.03.01 | Versiegelter Platz oder sonstiger gepflasterter Platz | 0 | 763 |
| 52.02.01a | Versiegelter oder sonstiger gepflasterter Weg | 0 | 756 |
| 52.01.03 | Teilbefestigter Verkehrsweg (z. B. Rasengitter, Spurplatten) | 2 | 748 |
| 52.03.02 | Teilbefestigter Platz (z. B. Rasengitter) | 3 | 764 |
| 52.02.04a | Geschotterter Weg oder Weg mit wassergebundener Decke | 4 | 758 |
| 52.03.03a | Platz mit geschottertem Belag oder wassergebundener Decke (z. B. Aschensportplatz) | 4 | 765 |
| 52.01.07a | Verkehrsweg mit Natursteinpflaster | 6 | 750 |
| 52.04.01 | Gleiskörper | 1 | 768 |
| 32.11.09a | Bauflächen und Baustelleneinrichtungsflächen | 3 | 289 |
| 53.01.03a | Altes Villengebiet mit altem Baumbestand | 13 | 777 |
| 53.01.03b | Lockeres Einzelhausgebiet | 5 | 778 |
| 53.01.03c | Verdichtetes Einzel- und Reihenhausgebiet | 4 | 779 |
| 53.01.05a | Wohnnutzung in Hochhaus- und Großformbauten | 4 | 781 |
| 53.01.14a | Industrie- und Gewerbefläche inkl. typischen Freiräumen | 2 | 786 |
| 53.01.15a.02 | Moderne Innenstadt | 3 | 789 |
| 53.01.16a.02 | Sonstige Blockbebauung | 4 | 792 |
| 53.01.17a.02 | Sonstiges Dorfgebiet inkl. Neubaugebiete | 4 | 796 |
| 53.01.07a.02 | Sonstige Einzelgebäude, Moderne Bauweise | 2 | 785 |
| 53.01.19a | Tierproduktionsanlage und Gewächshäuser | 0 | 800 |
| 53.02.02 | Betonmauer | 0 | 806 |
| 53.02.03a | Unverfugte Natursteinmauer bzw. Trockenmauer | 17 | 807 |
| 53.02.06a | Gabionen | 2 | 810 |
| 34.09 | Tritt- und Parkrasen (vgl. Siedlungsbiotope 51 bis 53) | 8 | 349 |
| 51.11a.01 | Sportrasenplatz | 7 | 740 |
| 34.08a.01 | Intensiv genutztes, frisches Dauergrünland | 8 | 345 |
| 34.08a.02 | Extensiv genutztes, frisches Dauergrünland | 11 | 346 |
| 34.08.02 | Frisches Ansaatgrünland | 7 | 347 |
| 34.08.03 | Artenarme, frische Grünlandbrache | 9 | 348 |
| 34.07b.01 | Mäßig artenreiche, frische Mähwiese | 15 | 341 |
| 34.07a.01 | Artenreiche, frische Mähwiese | 20 | 337 |
| 34.07a.03 | Artenreiche, frische Grünlandbrache | 16 | 339 |
| 41.06.01.J / 41.06.01.MA | Streuobstbestand auf Grünland, mit jungem Baumbestand / mit mittlerem bis altem Baumbestand | 12 / 19 | 494 à 495 |
| 41.03.03J / M / A | Sonstige Hecken, junge Ausprägung (ohne Überhälter) sowie Schnitthecken / mit Überhältern mittlerer / alter Ausprägung | 12 / 16 / 19 | 464 à 466 |
| 41.04J / M / A | Gehölzanpflanzungen und Hecken aus überwiegend nicht autochthonen Arten | 8 / 11 / 14 | 468 à 470 |
| 41.02.02J / M / A | Feldgehölz frischer Standorte | 13 / 14 / 17 | 447 à 449 |
| 41.05aJ / M / A | Einzelbäume, Baumreihen und Baumgruppen aus überwiegend autochtonen Arten | 11 / 15 / 18 | 473 à 475 |
| 41.05bJ / M / A | idem, nicht autochthone Arten | 8 / 11 / 14 | 477 à 479 |
| 41.05.04J / M / A | Allee | 11 / 16 / 19 | 485 à 487 |
| 43.07.04J / M / A | Buchen(misch)wälder frischer, basenarmer Standorte | 14 / 17 / 20 | 606 à 608 |
| 43.07.02J / M / A | Eichen-Hainbuchenwald staunasser bis frischer Standorte | 15 / 20 / 23 | 598 à 600 |
| 24.04a | Natürliches eutrophes Altwasser und eutrophe Tümpel | 19 | 230 |
| 24.09a | Natürliche und naturnahe temporäre stehende Gewässer (ohne Salztümpel) | 19 | 256 |
| 24.07.05 | Zier- und Löschteich | 5 | 242 |
| 24.07.13a | Sonstige stehende Gewässer (naturfern) | 5 | 252 |
| 39.06.01 / 02 / 03 | Trocken-warme Ruderalstandorte auf Sand-, Kies- und Schotterböden / auf bindigem Boden / Frische bis nasse Ruderalstandorte | 16 / 14 / 12 | 411 à 413 |
| 51.01 | Kleine vegetationsfreie Freiflächen | 5 | 716 |
| 51.02 | Kleine unbefestigte Freiflächen mit Spontanvegetation | 11 | 717 |
| 51.04a.01 / .02 | Brachflächen (ehemalige Baukomplexe, Industrie- und Verkehrsanlagen) mit / ohne wesentliche Anteile struktur-/artenreicher Ausprägung | 12 / 7 | 719 à 720 |
| 51.06a.01 | Historische Garten- und Parkanlage | 19 | 722 |
| 51.06a.02.01 / .02 | Extensiv gepflegte Parkanlage mit / ohne alten Baumbestand | 16 / 13 | 723 à 724 |
| 51.06a.03 / .04 | Intensiv gepflegte Parkanlage mit / ohne alten Baumbestand | 13 / 10 | 725 à 726 |
| 51.07a.01 / .02 | Sonstige Grünanlage mit / ohne alten Baumbestand | 13 / 9 | 730 à 731 |
| 51.08a.01 / .02 | Kleingartenanlagen, Grabeland, Gärten und private Grünflächen, strukturreich / strukturarm | 11 / 7 | 733 à 734 |
| 51.09a.01 / .02 | Friedhof mit / ohne alten Baumbestand | 14 / 9 | 736 à 737 |
| 52.01.08a.01 | Bankette, Mittelstreifen | 3 | 752 |
| 52.01.08a.02 / 52.01.08n.03 | Funktionsgrün an Verkehrswegen, artenarm oder junge Gehölze / artenreich oder Gehölze mittlerer bis alter Ausprägung | 7 / 11 | 753 à 754 |
| 33.04a.03 / 33.04a.02 | Acker mit stark verarmter oder fehlender Segetalvegetation / mit artenreicher Segetalvegetation (Lehm- oder Tonboden) | 6 / 16 | 304 à 305 |

Absences vérifiées dans l'Anlage 2 BKompV : aucun type "Dachbegrünung", "begrüntes Dach", "Fassadenbegrünung", "begrünte Fassade" (recherche plein texte sur le HTML brut : 0 occurrence). Les toitures et façades sont donc incluses dans les types de bâti (53.01.x) sans distinction.

##### 4.2 Hesse, KV 2018, Anlage 3 (échelle 3 à 80 WP je qm), document : KV vom 26. Oktober 2018, Anlage 3 "Wertliste nach Nutzungstypen", URL https://www.lexaris.de/book/version/documentflat/head/1329058 (source secondaire ; source officielle hessenrecht non accessible)

| Typ-Nr. | Restriction | Standard-Nutzungstyp (verbatim, abrégé) | WP je qm |
|---|---|---|---|
| 10.510 | | Sehr stark oder völlig versiegelte Flächen (Ortbeton, Asphalt), Müll-Deponie in Betrieb oder nicht abgedeckt, unbegrünte Keller, Fundamente etc. | 3 |
| 10.520 | | Nahezu versiegelte Flächen, Pflaster | 3 |
| 10.530 | | Schotter-, Kies- u. Sandflächen, -wege, -plätze oder andere wasserdurchlässige Flächenbefestigung sowie versiegelte Flächen, deren Wasserabfluss gezielt versickert wird inkl. Gleisanlagen im Schotterbett | 6 |
| 10.540 | | Befestigte und begrünte Flächen Rasenpflaster, Rasengittersteine o.ä. | 7 |
| 10.630 | | Wege mit hydraulisch gebundener Tragdeckschicht HGTD-Wege, auch Neuanlage | 5 |
| 10.690 | | Neuanlage Schotterrasenwege Steinerde mit Einsaat | 9 |
| 10.710 | | Dachfläche nicht begrünt | 3 |
| 10.715 | | Dachfläche nicht begrünt, mit zulässiger Regenwasserversickerung | 6 |
| 10.720 | | Dachfläche extensiv begrünt; begrünte Fundamente ohne Pflege, Sukzession | 19 |
| 10.730 | | Dachfläche intensiv begrünt mit dauernder Pflege, Ziergartencharakter | 13 |
| 10.741 | B, ° | Mauern und Hauswände mit Fassadenbegrünung, begrünte Pergolen | 19 |
| 10.743 | ° | Neuanlage von Fassaden- oder Pergola-Begrünung | 13 |
| 10.230 | | Rohböden | 23 |
| 10.430 | | Schotterhalde, Abraumhalde, Abbruchmaterial von Gebäuden, naturfern und/oder vegetationsfrei | 14 |
| 11.191 | | Acker, intensiv genutzt | 16 |
| 11.193 | B | Ackerbrachen mehr als ein Jahr nicht bewirtschaftet | 29 |
| 11.221 | | Gärtnerisch gepflegte Anlagen im besiedelten Bereich, arten- und strukturarme Hausgärten, kleine öffentliche Grünanlagen, innerstädtisches Straßenbegleitgrün etc., strukturarme Grünanlagen, Baumbestand nahezu fehlend | 14 |
| 11.222 | B | Arten- und strukturreiche Hausgärten auch im Außenbereich | 25 |
| 11.223 | | Neuanlage strukturreicher Hausgärten | 20 |
| 11.224 | | Intensivrasen z.B. in Sportanlagen | 10 |
| 11.225 | (B) | Extensivrasen, Wiesen im besiedelten Bereich, z.B. Rasenflächen alter Stadtparks | 23 |
| 11.231 | B | Park- und Waldfriedhöfe, Waldsiedlungen, Parks, Villensiedlungen mit Großbaumbestand nicht versiegelte Flächen | 38 |
| 11.232 | | Friedhofsneuanlagen, neu angelegte Grabfelder ohne nennenswerten Baumbestand | 16 |
| 06.350 | | Intensiv genutzte Wirtschaftswiesen und Mähweiden, inkl. Neuanlage ... artenarm | 21 |
| 06.360 | | Einsaat aus Futterpflanzen | 16 |
| 06.370 | | Naturnahe Grünlandanlage Einsaat aus gebietseigener Herkunft | 25 |
| 06.340 | (B) | Frischwiesen mäßiger Nutzungsintensität ... mäßig artenreich | 35 |
| 06.310 | (B) | Extensiv genutzte Flachland-Mähwiesen ... artenreich (LRT 6510) | 55 |
| 06.380 | B | Wiesenbrachen und ruderale Wiesen | 39 |
| 09.123 | B | Artenarme oder nitrophytische Ruderalvegetation | 25 |
| 09.124 | B | Arten- oder blütenreiche Ruderalvegetation | 41 |
| 09.160 | | Straßenränder mit Entwässerungsmulde, Mittelstreifen, intensiv gepflegt | 13 |
| 03.111 | B | Streuobstbestand mäßig intensiv bewirtschaftet | 38 |
| 03.130 | (B) | Streuobstbestand extensiv bewirtschaftet (mit LRT 6510 o.a.) | 50 |
| 03.121 | | Flächige Ersatz- oder Nachpflanzung hochstämmiger Obstbäume | 31 |
| 02.200 | (B) | Gebüsche, Hecken, Säume heimischer Arten auf frischen Standorten | 39 |
| 02.400 | | Neuanpflanzung von Hecken/Gebüschen (heimisch, standortgerecht, nur Außenbereich), Neuanlage von Feldgehölzen ... mindestens dreireihig, mindestens 5 m breit | 27 |
| 02.500 | | Standortfremde Hecken-/Gebüsche (... sowie Neuanlage im Innenbereich) | 20 |
| 04.110 | ° | Einzelbaum einheimisch, standortgerecht, Obstbaum | 34 |
| 04.120 | (B), ° | Einzelbaum nicht heimisch, nicht standortgerecht, Exot als Planung nur im besiedelten Bereich | 23 |
| 04.210 | ° | Baumgruppe / Baumreihe einheimisch, standortgerecht, Obstbäume ab 3 Bäumen | 34 |
| 04.600 | B | Feldgehölz (Baumhecke), großflächig Deckungsgrad der Bäume > 50 % | 50 |
| 01.115 / 01.116 | (B) | Bodensaurer Buchenwald / Mesophiler Buchenwald (Fremdbaumanteil 11 à 30 % oder Alter) | 41 / 45 |
| 01.111 / 01.112 | B | Bodensaurer / Mesophiler Buchenwald, naturschutzfachlich besonders wertvoll (max. 10 % Fremdbaumanteil, Alter mind. 120 Jahre) | 58 / 64 |
| 01.118 | | Buchenaufforstungen vor Kronenschluss | 33 |
| 01.181 | B | Naturferne Laubholzforste nach Kronenschluss | 33 |
| 05.333 | B | Ausdauernde Kleingewässer, eutroph (LRT 3150) | 49 |
| 05.334 | B | sonstige ausdauernde Kleingewässer | 50 |
| 05.343 | | Neuanlage von sonstigen Kleingewässern z.B. im besiedelten Bereich, In Parks | 29 |
| 05.352 | | Kleinspeicher, Teiche, Grubengewässer ... z.B. Fischteiche, Löschwasserteich | 25 |
| 05.354 | | Periodische/ temporäre Becken soweit nicht versiegelt, z.B. Regenrückhaltebecken o. ä. | 21 |

Contrôle croisé (bilan officiel RP Gießen, Stand 31.10.2025, lu via WebFetch) : 10.510 = 3 ; 10.530 = 6 ; 11.191 = 16 ; 11.224 = 10 ; 06.350 = 21 ; 04.110 = 34 ; 09.123 = 25 ; 02.510 = 30 (ce code 02.510 n'a pas été retrouvé dans l'Anlage 3 telle que lue sur Lexaris : à vérifier). Ces valeurs concordent avec la lecture Lexaris, ce qui corrobore la fiabilité de cette source secondaire pour les codes testés. Un second bilan (uvp-verbund.de, non daté) utilise 04.110 = 31, valeur qui correspond à la KV 2005 (lue sur umwelt-online : 04.110 = 31) : ce document applique donc l'ancienne version.

##### 4.3 Bavière, Biotopwertliste (échelle 0 à 15), document : "Biotopwertliste zur Anwendung der Bayerischen Kompensationsverordnung (BayKompV), Stand 28.02.2014 (mit redaktionellen Änderungen vom 31.03.14)", URL https://www.stmuv.bayern.de/themen/naturschutz/eingriffe/doc/biotopwertliste.pdf

| Code | Biotop-/Nutzungstyp (verbatim, abrégé) | Classe | Grundwert | Page |
|---|---|---|---|---|
| V11 | Verkehrsflächen des Straßen- und Flugverkehrs, versiegelt | keine | 0 | 23 |
| V12 | idem, befestigt (wasserdurchlässige Pflasterdecke, geschottert, wassergebundene Decke; Bankette, Mittelstreifen) | gering | 1 | 23 |
| V21 / V22 / V23 | Gleisanlagen versiegelt / geschottert / begrünt (Grüne Gleise) | keine / gering / gering | 0 / 1 / 4 | 23 |
| V31 / V32 | Rad-/Fußwege und Wirtschaftswege versiegelt / befestigt | keine / gering | 0 / 1 | 23 |
| V331 / V332 | unbefestigt, nicht bewachsen / bewachsen (Grünwege) | gering | 2 / 3 | 23 |
| V51 / V52 | Grünflächen und Gehölzbestände entlang von Verkehrsflächen, junger bis mittlerer Ausprägung / alter Ausprägung | gering / mittel | 3 / 7* | 23 |
| X4 | Gebäude der Siedlungs-, Industrie- und Gewerbegebiete | keine | 0 | 23 |
| X11 | Dorf-, Kleinsiedlungs- und Wohngebiete (inkl. typischer Freiräume) | gering | 2 | 23 |
| X12 | Misch- und Kerngebiete (inkl. typischer Freiräume) | gering | 1 | 23 |
| X2 | Industrie- und Gewerbegebiete (inkl. typische Freiräume) | gering | 1 | 23 |
| P5 | Sonstige versiegelte Freiflächen | keine | 0 | 23 |
| P411 / P412 | Sonderflächen der Land- und Energiewirtschaft, versiegelt / teilversiegelt | keine / gering | 0 / 1 | 23 |
| P11 | Park- und Grünanlagen (inkl. Friedhöfe) ohne Baumbestand oder mit Baumbestand junger bis mittlerer Ausprägung | gering | 5 | 23 |
| P12 | idem, mit Baumbestand alter Ausprägung | mittel | 10** | 23 |
| P21 / P22 | Privatgärten und Kleingartenanlagen, strukturarm / strukturreich | gering / mittel | 5 / 7 (+) | 23 |
| P31 | Sport-/Spiel-/Erholungsanlagen mit hohem Versiegelungsgrad | keine | 0 | 23 |
| P32 | idem, mit geringem Versiegelungsgrad (z.B. Naturrasensportplatz, Spielplatz) | gering | 2 | 23 |
| P431 / P432 / P433 | Ruderalflächen im Siedlungsbereich, vegetationsarm / artenarme Ruderal- und Staudenfluren / artenreiche | gering / gering / mittel | 2 / 4 / 8 (+) | 23 |
| A11 | Intensiv bewirtschaftete Äcker ohne oder mit stark verarmter Segetalvegetation | gering | 2 | 16 |
| A2 | Ackerbrachen | gering | 5 | 16 |
| G11 | Intensivgrünland (genutzt) | gering | 3 | 16 |
| G12 | Intensivgrünland, brachgefallen | gering | 5 | 16 |
| G211 | Mäßig extensiv genutztes, artenarmes Grünland | mittel | 6 | 16 |
| G212 | Mäßig extensiv genutztes, artenreiches Grünland | mittel | 8 (+) | 16 |
| G214 | Artenreiches Extensivgrünland | hoch | 12* | 16 |
| K11 | Artenarme Säume und Staudenfluren (hypertroph, Neophyten) | gering | 4 | 17 |
| K121 / K122 | Mäßig artenreiche Säume und Staudenfluren trocken-warmer / frischer Standorte | mittel | 8 (+) / 6 (+) | 17 |
| K131 | Artenreiche Säume und Staudenfluren trocken-warmer Standorte | hoch | 11 | 17 |
| B112 | Mesophiles Gebüsche / Hecken (Schlehe, Weißdorn, Hasel) | mittel | 10 | 19 |
| B116 | Gebüsche / Hecken stickstoffreicher, ruderaler Standorte | mittel | 7 | 19 |
| B12 | Gebüsche / Hecken mit überwiegend gebietsfremden Arten | gering | 5 | 19 |
| B141 / B142 | Schnitthecken, einheimische / fremdländische Arten | gering | 5 / 3 | 19 |
| B211 / B212 / B213 | Feldgehölze mit überwiegend einheimischen Arten, junge / mittlere / alte Ausprägung | mittel / mittel / hoch | 6 / 10* / 12** | 19 |
| B311 / B312 / B313 | Einzelbäume / Baumreihen / Baumgruppen einheimisch, junge / mittlere / alte Ausprägung | gering / mittel / hoch | 5 / 9* / 12** (+) | 19 |
| B321 / B322 / B323 | idem, gebietsfremde Arten | gering / mittel / hoch | 4 / 8* / 11** (+) | 19 |
| B411 / B412 | Streuobstbestände im Komplex mit Äckern, junge / mittlere bis alte Ausbildung | gering / mittel | 5 / 8* (+) | 19 |
| B431 / B432 | Streuobstbestände im Komplex mit intensiv bis extensiv genutztem Grünland, junge / mittlere bis alte Ausbildung | mittel | 8 (+) / 10* (+) | 20 |
| B441 | Streuobstbestände im Komplex mit artenreichem Extensivgrünland | hoch | 12* | 20 |
| L241 / L242 / L243 | Buchenwälder basenreicher Standorte, junge / mittlere / alte Ausprägung | mittel / hoch / hoch | 8 / 12* / 14** | 21 |
| S131 / S132 / S133 | Eutrophe Stillgewässer, bedingt naturfern / bedingt naturnah / natürlich oder naturnah | mittel / mittel / hoch | 6 / 9 (+) / 13* | 16 |
| S22 | Sonstige naturfremde bis künstliche Stillgewässer | gering | 3 | 16 |
| S21 | Abbaugewässer | gering | 1 | 16 |

Légende lue : "*" = W = 4 (Prognosewert : abattement possible de 1 à 2 WP) ; "**" = W = 5 (abattement possible de 1 à 3 WP) ; "(+)" = majoration de 1 WP si le biotope est effectivement protégé, cartographié BK ou LRT FFH.

Absences vérifiées : aucun type "Dachbegrünung" ni "Fassadenbegrünung" dans la liste bavaroise (recherche plein texte "dach", "fassade", "gründach" : 0 occurrence pertinente ; seule "begrünt" apparaît pour V23 Grüne Gleise et O652). Les toitures relèvent donc de X4 "Gebäude" = 0.

##### 4.4 NRW, Arbeitsblatt 61 (échelle 0 à 10), document : LANUK-Arbeitsblatt 61, Stand März 2026, URL https://www.lanuk.nrw.de/fileadmin/lanuvpubl/4_arbeitsblaetter/Arbeitsblatt_61.pdf ; valeurs recoupées dans le XLSX officiel (modifié 01.10.2025)

| Code | Biotoptyp (verbatim, abrégé) | Biotopwert | Page PDF |
|---|---|---|---|
| HN | Gebäude, Mauerwerk, Ruinen | 0 | 27 |
| ...,mi1 | Dachbegrünung (Dachbegrünung oder übererdete Anlage mit einem von Gehölzen ... überdeckten Flächenanteil von mehr als 30 % (Bodenauftrag über 30 cm)) | 1 | 27 |
| ...,me1/me2 | versiegelte Plätze und Verkehrswege (Pflaster- und Plattenbeläge, Asphalt- und Betonflächen) | 0 | 28 |
| ...,me3/mf1/mf6/mf7 | teilversiegelte Plätze und Verkehrswege (wassergebundene Decke, Schotterwege u. -flächen, etc.) | 1 | 28 |
| ...,me4/me6/me7/mf8,stb3 | unbefestigte Plätze und Verkehrswege, auf nährstoffreichen Böden | 3 | 28 |
| ...,sty1 | Solarmodul (überschirmte Fläche) | 1,5 | 28 |
| ..., mr3 | Straßenbegleitgrün auf Bankette, Mittelstreifen | 1 | 27 |
| HC0 | Rain, Straßenrand, straßenbegleitend | 2 | 27 |
| BA4/BD3 | Verkehrsgehölz, Gehölzstreifen, straßenbegleitend | 4 | 27 |
| HW ..., neo6 / neo7 | Siedlungs-, Industrie- und Verkehrsbrachen mit Neo-, Nitrophytenanteil > 50 % / < 50 % (Gehölzanteil < 50 %) | 3 / 4 | 27 |
| ...,ka4 | Zier- und Nutzgarten ohne bzw. mit überwiegend nicht heimischen Baum- und Straucharten | 2 | 26 |
| ...,ka6 | Zier- und Nutzgarten mit überwiegend einheimischen Baum- und Straucharten | 4 | 26 |
| ...,mc1 | Rasenfläche, intensiv genutzt (z.B. Trittrasen) | 2 | 26 |
| ...,mc2 | Rasen- und Wiesenfläche, extensiv genutzt | 4 | 26 |
| ...,xd4,ob1 | Grünanlage, Friedhof < 2 ha, strukturarm, Baumbestand nahezu fehlend | 3 | 26 |
| ...,xd3 | Grünanlage, Friedhof ≤ 2 ha, strukturreich mit Baumbestand | 5 | 26 |
| ...xd4 | Park, Friedhof > 2 ha, strukturarm ohne alten Baumbestand | 4 | 26 |
| ...,xd3,mq1 | Park, Friedhof > 2 ha, strukturreich mit altem Baumbestand | 6 | 27 |
| ..., acs / aci / acme / ace | Acker sehr intensiv ohne Wildkräuter / intensiv / mäßig extensiv / extensiv auf nährstoffarmen Böden | 1 / 2 / 4 / 5 | 25 |
| HB1, ed | Einsaatbrache (mit Nutzpflanzen z. B. Phacelia) | 3 | 25 |
| ..., stb3 / sta3 | Ackerbrache auf nährstoffreichen Böden / auf nährstoffarmen Sand- und flachgründigen Kalkböden | 4 / 5 | 25 |
| EA3, EB1 | Feldgras, Neueinsaat ; Fettweide, Neueinsaat | 2 | 23 |
| EA, EB, xd2 | Fettwiese / -(mäh)weide, artenarm | 3 | 23 |
| ..., xd5 | Fettwiese / -(mäh)weide, mäßig artenreich | 4 | 23 |
| ...,veg1 / veg2 / veg3 | Artenreiche Fettwiese, Magerwiese/-weide, Feucht-/Nasswiese : mittel bis schlecht / gut / hervorragend ausgeprägt | 5 / 6 / 7 | 23 |
| EE0a, xd2 | Fettgrünlandbrache, artenarm | 3 | 23 |
| ...,neo5 / neo4 / neo2 / neo1 | Säume, Hochstauden- und Annuellenfluren mit Anteil Störzeiger > 75 % / > 50 à 75 % / > 25 à 50 % / ≤ 25 % | 3 / 4 / 5 / 6 | 24 |
| ...,ta14 / ta15a / ta15b | Streuobstwiese/-weide mit Baumbestand < 10 Jahre / 10 bis 30 Jahre / > 30 Jahre | 5 / 6 / 7 | 26 |
| BD5 (lrg0 / lrg70 / lrg100) | Schnitthecke (jährlicher Formschnitt) selon part d'essences typiques < 50 % / > 50 à 70 % / > 70 % | 2 / 3 / 4 | 20 |
| ..., kb (tc) ; kb1(tc) (lrg0) | Hecke einreihig / mehrreihig, kein regelmäßiger Formschnitt, essences typiques < 50 % | 3 (+1 Überhälter) / 4 (+1) | 20 |
| ..., kb (tc) ; kb1(tc) (lrg100) | idem, essences typiques > 70 % | 5 (+1) / 6 (+1) | 21 |
| Einzelbäume lrt30, ta3-5 / ta1-2 / ta-11 / ta11a/tb2 | Baumgruppen, Baumreihen, Einzelbäume, Alleen, Kopfbäume, part d'essences typiques < 70 % : Jungwuchs bis Stangenholz (BHD bis 13 cm) / geringes bis mittleres Baumholz (14 à 49 cm) / starkes bis sehr starkes (≥ 50 ; ≥ 80 cm) / mächtiges Baumholz, Uraltbaum (> 100 cm) | 3 / 4 / 5 / 6 | 22 |
| Einzelbäume lrt70 | idem, part d'essences typiques > 70 % | 6 / 7 / 8 / 9 | 22 |
| Wald lrt30, ta3-5 (m/g/h) | Wald mit lebensraumtypischen Baumarten-Anteilen 0 < 30 %, Jungwuchs bis Stangenholz, Strukturen mittel bis schlecht / gut / hervorragend | 3 / 4 / 5 | 13 |
| Wald lrt30, ta1-2 et ta-11a | idem, geringes bis mittleres Baumholz, et starkes bis mächtiges Baumholz | 4 / 5 / 6 (les 2 classes) | 13 |
| Wald lrt100, ta3-5 / ta1-2 / ta-11a (m/g/h) | Laubwald mit lebensraumtypischen Baumarten-Anteilen > 90 % (lrt100) | 6 / 7 / 8 ; 7 / 8 / 9 ; 8 / 9 / 10 | XLSX lignes 150 à 170 |
| Stillgewässer FD/FF/FG..., wf5 / wf4 / wf4a / wf3 / wf | stehende Kleingewässer, Teiche, Abgrabungsgewässer etc. : naturfremd / naturfern / bedingt naturfern / bedingt naturnah / naturnah | 1 / 2 / 4 / 6 / 7 | 10 |
| Seen, Weiher, Altwasser (FA, FB, FC...), wf4 / wf4a / wf3 / wf | naturfern / bedingt naturfern / bedingt naturnah / naturnah | 2 / 5 / 8 / 10 | 9 à 10 |

Règle de surface des arbres isolés (lue, p. 22) : "Kopf-/Einzelbaum: Berechnung des Flächenbezugs über m2 des Kronentraufbereichs".

#### 5. Règles temporelles et de risque trouvées

##### 5.1 BKompV

- Durée d'entretien, § 12 Abs. 1 (lu) : "Der Unterhaltungszeitraum richtet sich nach der für die Erreichung des Kompensationsziels erforderlichen Dauer; er überschreitet in der Regel die Dauer von 25 Jahren nicht."
- Timelag, Anlage 5 Abschnitt B "Berücksichtigung von Entwicklungszeiten" (lu intégralement) : "Sofern die Entwicklungszeit bis zur Erreichung des Zielzustandes der geplanten Ausgleichs- und Ersatzmaßnahme 30 Jahre überschreitet, ist eine Vergrößerung der Maßnahmenfläche um 25 Prozent erforderlich, um die verzögerte Funktionserfüllung zu berücksichtigen (Timelag-Aufschlag)." ; "Sofern Biotoptypen oder Zielzustände anderer Funktionen mit einem Alter von mehr als 100 Jahren erheblich beeinträchtigt werden, sind neben den langfristig wirksamen Maßnahmen mit einer Entwicklungszeit von mehr als 100 Jahren kurz- bis mittelfristig wirksame Maßnahmen mit einer Entwicklungszeit von weniger als 30 Jahren vorzusehen. Die beiden Maßnahmenanteile sollen jeweils 50 Prozent ... betragen." ; "Bei Entwicklungszeiten von weniger als 30 Jahren ist kein Timelag-Aufschlag erforderlich." Donc 3 classes de durée : moins de 30 ans (pas de majoration), 30 à 100 ans (majoration de surface de 25 %), plus de 100 ans (majoration de 25 % plus partage 50 / 50 avec des mesures à effet en moins de 30 ans). Tableau d'exemples lu (Zielbiotop / Ausgangsbiotop / Entwicklungszeit) : hêtraie ancienne à partir d'un Buchen-Mischbestand "< 30 Jahre" ; à partir d'un Fichtenforst "30 bis 100 Jahre" ; à partir d'un Acker "> 100 Jahre" ; Niedermoor à partir d'un Feuchtgrünland intensif "30 bis 100 Jahre" ; Hochmoor à partir d'un stade dégradé "> 100 Jahre" ; Halbtrockenrasen, Großseggenried, naturnahes Fließgewässer, extensiver Acker : "< 30 Jahre".
- Portée de cette règle : § 9 Abs. 3 et 4 (lus) la rattachent aux "weiteren Schutzgüter" et aux atteintes "besonderer Schwere" ; § 8 (biotopes, cas général) ne renvoie pas à l'Anlage 5 B. La Handreichung BfN/BMU 2021 (lue par mots-clés, lignes 3802 à 3812 du texte extrait) évoque néanmoins des "Timelag-Aufschläge ... nach Anlage 5 B BKompV" dans la fixation des mesures. L'articulation exacte entre le bilan de points (§ 7, § 8) et le Timelag-Aufschlag relève d'une lecture juridique à confirmer.
- Anlage 2 BKompV : les stades J / M / A intègrent implicitement l'âge dans la valeur (p. ex. hêtraie 14 / 17 / 20), ce qui réduit automatiquement le gain crédité à une plantation jeune ; la Handreichung (lue via WebFetch, p. 14) indique des classes d'âge forestières jeune < 30 ans, moyen 30 à 80 ans, âgé > 80 ans.
- Anlage 6 (lue) : durées minimales par type de mesure, p. ex. "Mindestdauer 10 Jahre" (Äcker extensifs, Säume, mesures forestières), "Vorher mind. 5 Jahre lang Acker" (création de prairie), "Höchstdauer der Belassung ohne Umbruch: 3 Jahre" (jachères), "Mindestdauer 3 Jahre" (habitats pour espèces cibles). Aucune colonne de risque ni coefficient de risque d'échec dans la BKompV (vérifié : "Risiko" 0 occurrence dans l'Anlage 6).
- Effets temporaires : § 5 Abs. 3 classe les effets selon "Stärke, Dauer und Reichweite" ; pas de formule de prorata temporel explicite.

##### 5.2 Hesse

- État planifié évalué "drei Vegetationsperioden nach Herstellung" (Anlage 2 n° 1.2, lu) : pas de projection à 25 ou 30 ans ; les types "Neuanlage" (p. ex. 02.400 = 27 contre 02.200 = 39 ; 10.743 = 13 contre 10.741 = 19 ; 11.223 = 20 contre 11.222 = 25 ; 05.343 = 29 contre 05.334 = 50 ; 01.118 = 33 contre 01.116 = 45) portent l'effet de la durée de développement dans la valeur elle-même.
- Aucun "Timelag-Aufschlag" ni coefficient de risque dans la KV 2018 (recherche plein texte : "Entwicklungszeit" 0 occurrence ; "Risiko" 0 occurrence). Pas de prorata pour durée de développement.
- Interventions temporaires (Anlage 2 n° 4.2, lu) : > 3 ans et < 50 ans : atteinte proratisée "wie die Dauer des Eingriffs zu 50 Jahren" ; "Bei Eingriffen unter drei Jahren Dauer ist nach Nr. 1 und 2 zu verfahren" ; intervention non achevable en 50 ans : état pendant l'intervention. Le document de 2005 (umwelt-online, lu) utilisait 100 ans au lieu de 50.
- Délai d'exécution : 3 ans après le début de l'intervention (§ 2 Abs. 5, lu) avec Ersatzzahlung complémentaire en cas de retard.
- Exigence de pérennité pour certains types E : "Nutzungssicherheit min. 30 Jahre" (06.950, 06.960, lus).

##### 5.3 Bavière

- Horizon de prognose fixé par règlement : Anlage 3.2 BayKompV (lue) : "Prognosezustand nach 25 Jahren Entwicklungszeit".
- Critère W (lu, tableau p. 9 rasterisé) : 5 classes de durée de développement : W = 5 "≥ 80 Jahre" ("äußerst bis sehr gering / nicht bis schwer (langfristig) wiederherstellbar") ; W = 4 "26 - 79 Jahre" ; W = 3 "10 - 25 Jahre" ; W = 2 "5 - 9 Jahre" ; W = 1 "< 5 Jahre" ; W = 0 "ohne naturschutzfachliche Bedeutung (versiegelte Flächen)". Sources citées sous le tableau : Riecken et al. 2006, LfU 2006, ARGE Eingriff-Ausgleich NRW 1994 / LANUV NRW 2008.
- Prognosewert (lu, chap. 1.4 et tableau p. 11 rasterisé) : abattement sur le Grundwert du Zielbiotop, applicable seulement si la durée jusqu'à la pleine fonctionnalité dépasse 25 ans : "26 - 49 Jahre : Abschlag = 1 WP (W = 4 et W = 5)" ; "50 - 79 Jahre : Abschlag = 2 WP (W = 4 et W = 5)" ; "≥ 80 Jahre : Abschlag = 3 WP (W = 5 seulement)". "Für Biotoptypen der Stufen 0 bis 3 ... sind ebenfalls keine Prognosewerte zu definieren, da diese immer nur eine kurze Entwicklungszeit von weniger als 25 Jahren ... aufweisen." La durée est fixée "gutachterlich" selon l'Ausgangsbiotop.
- Il s'agit donc d'un abattement de valeur (1 à 3 points sur 15), pas d'un "Risikozuschlag" de surface. Le mot "Zeitverzögerung" n'apparaît pas dans la Biotopwertliste (le document parle de "timelag" et de "Prognosewert"). Aucun coefficient de risque d'échec trouvé dans la BayKompV (§ 4, 7, 8) ni dans la Biotopwertliste.
- Les stades d'âge (junge / mittlere / alte Ausprägung) sont intégrés aux codes (p. ex. B311 / B312 / B313 = 5 / 9 / 12).

##### 5.4 NRW

- Horizon de prognose (lu, en-tête de Tabelle 1, p. 9) : "Im Rahmen der Kompensation ist für den zu entwickelnden Biotoptyp und seinen Prognosewert ein Zeitraum von 30 Jahren (eine Menschengeneration) zugrunde zu legen." Glossaire (p. 51) : "Prognosewert: Biotopwert, der nach 30 Jahren der Maßnahmenumsetzung mit hoher Wahrscheinlichkeit erreicht wird".
- Marquages de non-compensabilité (lus, p. 9) : colonne "nicht ausgleichbar / Sonderstandort" : "x" = non compensable au regard de la "zeitliche Wiederherstellbarkeit", "(x)" = au cas par cas ; "+" = "Biotoptypen mit langen Entwicklungszeiten (> 100 Jahre) und besonderen Standortfaktoren" ; "ist bei Inanspruchnahme dieser Biotoptypen eine funktional gleichartige Wiederherstellung nicht möglich, ergibt sich ein zusätzlicher Kompensationsbedarf" (à motiver, montant non chiffré).
- Forêts (lu, Anhang 3.3, p. 37) : pour une création de forêt, le Prognosewert à 30 ans est celui de la classe "Jungwuchs bis Stangenholz, Strukturen mittel bis schlecht ausgeprägt" (p. ex. 3 à 6 selon la part d'essences typiques) ; réévaluation possible "alle 30 Jahre" avec crédit des points supplémentaires à de nouveaux Eingriffe ou à un Ökokonto ; "Waldlebensraumtypen, die die maximale Wertstufe 10 erreicht haben, sind ... nicht mehr aufwertungsfähig".
- Pas de Gesamtkorrekturfaktor ni de coefficient de risque dans l'Arbeitsblatt 61 (vérifié). Historique lu dans Bruns 2007 (Tab. 7-22, p. 341) pour l'ancien document NRW ("NW 1") : "ein Mittelwert zwischen dem Wert eines neu angelegten Biotops und dem Wert eines Biotops nach 25 Jahren" ; cette règle n'est plus dans l'Arbeitsblatt 61.

##### 5.5 Synthèse comparative des règles temporelles (toutes lues)

| Méthode | Horizon de prognose | Mécanisme timelag | Classes de durée |
|---|---|---|---|
| BKompV | Aucun horizon fixe dans § 7 et § 8 ; Anlage 5 B | Majoration de surface de 25 % si > 30 ans ; partage 50/50 avec mesures < 30 ans si > 100 ans | < 30 ; 30 à 100 ; > 100 ans |
| Hesse | 3 périodes de végétation après réalisation | Aucun ; valeur réduite des types "Neuanlage" | Aucune |
| Bavière | 25 ans (Anlage 3.2) | Abattement de 1 à 3 WP sur le Grundwert du Zielbiotop | W : < 5 ; 5 à 9 ; 10 à 25 ; 26 à 79 ; ≥ 80 ans ; abattement : 26 à 49 ; 50 à 79 ; ≥ 80 ans |
| NRW | 30 ans | Prognosewert à 30 ans ; marquage "+" (> 100 ans) avec besoin complémentaire non chiffré | < 30 ; > 100 ans (marquage) |

#### 6. Limites pour une transposition en France

Les points suivants découlent directement des textes lus.

1. Échelles non convertibles entre elles : 0 à 24 (Bund), 3 à 80 (Hesse), 0 à 15 (Bavière), 0 à 10 (NRW). Les rapports entre types diffèrent : sol imperméabilisé / prairie intensive / hêtraie ancienne = 0 / 8 / 20 (Bund), 3 / 21 / 64 (Hesse, 01.112), 0 / 3 / 14 (Bavière, L243), 0 / 3 / 10 (NRW, lrt100 ta-11a h). Un facteur multiplicatif unique ne permet pas de passer de l'une à l'autre (minimum non nul en Hesse ; plafonds différents).
2. Typologies de biotopes propres à chaque Land, adossées à des clés de cartographie régionales (BKompV § 17 Abs. 4 renvoie aux "Kartieranleitungen der ... Länder" ; Bavière à la Biotopkartierung Bayern et au SNK+ ; NRW au Biotoptypenschlüssel LANUV). Il n'existe pas de table de correspondance avec EUNIS ou les typologies françaises dans les documents lus. Le BfN annonce des "Übersetzungsschlüssel" entre listes des Länder et liste fédérale (page BMUKN lue via WebFetch), mais la page https://www.bfn.de/eingriffsregelung n'a livré aucun document : NON VÉRIFIÉ.
3. Les valeurs sont calibrées sur la rareté et la menace en Allemagne (Liste rouge des biotopes de Riecken et al. 2006 citée par la Bavière p. 7 et par la Handreichung BKompV p. 14 ; "landesweite Ausprägung in Bayern") : la composante "Seltenheit/Gefährdung" n'est pas transposable sans recalibrage sur les listes rouges françaises.
4. Les types urbains sont traités de façon hétérogène : la BKompV et la Bavière n'ont aucun type de toiture ou de façade végétalisée (vérifié) ; la Hesse en a 4 (10.720 = 19, 10.730 = 13, 10.741 = 19, 10.743 = 13) ; NRW en a 1 (Dachbegrünung = 1 sur 10, sous condition d'un recouvrement ligneux > 30 % et d'un substrat > 30 cm). La Bavière interdit d'utiliser la plupart des types urbains comme Zielbiotope (p. 23).
5. Les objets ponctuels (arbres) sont traités par surface de houppier avec des conventions différentes : Hesse 1 / 3 / 5 m2 par arbre planté selon la circonférence (lu) ; NRW "m2 des Kronentraufbereichs" (lu) ; BKompV et Bavière : stades J/M/A sans règle de surface explicite dans les textes lus.
6. Les règles temporelles divergent (voir 5.5) et aucune des 4 méthodes ne contient de coefficient de risque d'échec de la mesure ; la seule pénalisation du risque est indirecte (valeur de prognose, abattement bavarois, majoration de surface fédérale).
7. Statut : 3 des 4 méthodes sont des règlements (donc libres de droits au titre de § 5 Abs. 1 UrhG, qualification à confirmer juridiquement) ; la liste NRW est un guide dont l'éditeur réserve la reproduction ("nur ... nach vorheriger Zustimmung des Herausgebers", p. 52). Pour une réutilisation commerciale dans un outil, la liste NRW et le PDF bavarois (auteur privé Bosch & Partner, publié par Bekanntmachung) demandent une analyse de licence distincte.
8. Le cadre juridique diffère : la compensation allemande est un bilan physique en points sur emprise et sur site de mesure, avec Ersatzzahlung monétaire subsidiaire (0,40 euro/WP plus Bodenwertanteil en Hesse ; barèmes du § 14 BKompV). Une "méthode de calcul de la biodiversité d'un projet de construction" en France (séquence ERC, L. 163-1 C. env.) n'a pas la même fonction : les points allemands sont des unités d'équivalence pour une obligation de compensation, pas un score de performance.

#### 7. Ce qui manque

- Hesse : texte officiel sur hessenrecht (inaccessible) et PDF officiel de l'Anlage 3 : la lecture repose sur Lexaris, corroborée par un bilan officiel du RP Gießen (8 codes vérifiés) ; la référence GVBl. 2018 S. 652 n'a été lue que sur l'extrait umwelt-online. Le code 02.510 (= 30 WP dans le bilan RP Gießen) n'a pas été retrouvé dans l'Anlage 3 lue : à vérifier. Les "Vordrucke" officiels d'Ausgleichsberechnung n'ont pas été trouvés.
- BKompV : la Kartieranleitung annoncée par § 17 Abs. 4 n'a pas été recherchée ; les clés de conversion BfN (Länder vers Bund) n'ont pas été obtenues ; la Handreichung BfN/BMU 2021 (103 pages) n'a été lue que par mots-clés ; le XML téléchargé n'a pas été exploité ; la modification de la BKompV par la loi du 22.12.2025 (BGBl. 2025 I Nr. 351) n'a pas été analysée dans son contenu (seule la mention de l'en-tête a été lue).
- Bavière : la "Arbeitshilfe zur Biotopwertliste - Verbale Kurzbeschreibungen (07/2014)" et l'"Übersicht über die neuen Biotoptypen-Zuordnungen" (LfU) n'ont pas été lues ; les Anlagen 2.1, 4.1, 4.2 et 5 de la BayKompV n'ont pas été lues ; aucune version tableur trouvée.
- NRW : les versions antérieures (LANUV septembre 2008, juin 2021) n'ont pas pu être lues (3 URL inaccessibles) ; la comparaison des valeurs 2008 / 2021 / 2026 n'est donc pas faite ; les Tabellen 5 (Grünland) et 8 (Wald) de l'Arbeitsblatt 61 n'ont pas été transcrites en détail ; seul le document 2026 a été lu, et la page LANUK ne précise pas le caractère contraignant.
- Références scientifiques : Bruns 2007 (thèse, 637 pages) n'a été lue que partiellement (résumé, section 7.3.7.4 et Tab. 7-22) ; Dietrich/Schweppe-Kraft/Haarnacke 2014 (BfN) lu via WebFetch seulement ; aucun article de revue à comité de lecture avec DOI traitant spécifiquement de la comparaison des Biotopwertverfahren entre Länder n'a été localisé (l'article MDPI 2018 trouvé porte sur la PIK, pas sur les Biotopwertverfahren ; l'ouvrage Springer 2018 a un DOI mais ses chapitres allemands n'ont pas été lus).

#### 8. Références scientifiques et rapports comparatifs (lus)

1. Bruns, Elke (2007) : "Bewertungs- und Bilanzierungsmethoden in der Eingriffsregelung. Analyse und Systematisierung von Verfahren und Vorgehensweisen des Bundes und der Länder". Dissertation, TU Berlin, Fakultät VI, soutenue le 30.11.2006, publiée le 29.05.2007, 637 pages. URN lue : urn:nbn:de:kobv:83-opus-15652 ; notice : https://depositonce.tu-berlin.de/items/2535e269-9c84-4328-a734-a241590d9120 ; PDF : https://api-depositonce.tu-berlin.de/server/api/core/bitstreams/5bac8870-5377-4297-b805-348420c5249f/content. Contenu lu : 42 Leitfäden analysés dont 27 en profondeur ; 3 familles ("verbal-argumentativ", "Biotopwertverfahren", "Erweiterter, biotopwertorientierter Bilanzierungsansatz") ; conclusion du résumé : "Nach wie vor besteht innerhalb dieser Grundtypen eine im Detail unnötig große Variationsbreite, die nicht unbedingt fachlich begründet ist. Vielmehr ist zu vermuten, dass die bestehenden Interpretationsspielräume auch dazu genutzt werden, um den Umfang der Verursacherpflichten politisch akzeptabel zu machen." Section 7.3.7.4 (p. 340 à 341) et Tab. 7-22 : inventaire Land par Land de la prise en compte du time lag (p. ex. Berlin : taux d'intérêt annuel de 1,13 % sur les coûts de restauration au-delà de 5 ans ; Hesse KV : "nicht vorgesehen" ; NRW : moyenne entre valeur initiale et valeur à 25 ans ; Baden-Württemberg : Planungswert à 25 ans ; Rheinland-Pfalz : aucun). Note 701 : renvoi à la critique des "Natural-Aufschläge" par Schweppe-Kraft 1998.
2. Dietrich, Katharina ; Schweppe-Kraft, Burkhard ; Haarnacke, Simone (2014) : "Methoden zur Bestimmung des Ausgleichs für Entwicklungszeiten bei Kompensationsmaßnahmen / Methods to calculate offsets to compensate for time lags in the recovery of ecosystems and biodiversity". Bundesamt für Naturschutz, 23.04.2014, environ 23 pages, pas de DOI. URL : https://www.bfn.de/sites/default/files/2021-06/Dietrich_Schweppe-Kraft_Haarnacke_2014_offsetting_time_lags.pdf (lu via WebFetch). Compare 3 approches (majoration à période fixe : NRW 30 ans, Hesse valeur à l'achèvement ; actualisation à 2 à 5 % ; fonds de compensation) ; conclut qu'aucune justification scientifique ne fonde le choix de la "bonne" période (p. 5) et que pour les durées très longues la compensation n'est pas réaliste (p. 21 à 22).
3. Darbi, Marianne ; Tausch, Christian (2010) : "Loss-Gain calculations in German Impact Mitigation Regulation", IOER Dresden, publié par Forest Trends, 31.03.2010, pas de DOI. URL : https://www.forest-trends.org/wp-content/uploads/imported/loss-gain-calculations-in-german-imr_md_100324-pdf.pdf (lu via WebFetch). Distingue Biotopwertverfahren, Kompensationsflächenfaktoren et approches par coûts ; "au moins 40 approches publiées" ; critique le passage d'échelles ordinales à des valeurs "quasi-cardinales" (p. 4) et la "Negligence of components of the natural balance" (p. 10).
4. Mazza, Leonardo ; Schiller, Julia (2014) : "The use of eco-accounts in Baden-Württemberg to implement the German Impact Mitigation Regulation: A tool to meet EU's No-Net-Loss requirement?", IEEP, 12.11.2014, projets Invaluable et OPERAs. URL : https://ieep.eu/wp-content/uploads/2022/12/Eco-Accounts_BW_case_study_final_221114.pdf (lu via WebFetch). Échelle BW de 0 à 64 Ökopunkte (p. 33) ; coexistence de modèles (60 % / 20 % / 20 % des communes, p. 33) ; absence de standard fédéral empêchant la compensation interrégionale (p. 32).
5. Wende, W. ; Tucker, G.-M. ; Quétier, F. ; Rayment, M. ; Darbi, M. (éd.) (2018) : "Biodiversity Offsets: European Perspectives on No Net Loss of Biodiversity and Ecosystem Services", Springer, 252 pages, DOI https://doi.org/10.1007/978-3-319-72581-9 (métadonnées lues sur fis.tu-dresden.de ; chapitres non lus).
6. Druckenbrod, C. ; Beckmann, V. (2018) : "Production-Integrated Compensation in Environmental Offsets - A Review of a German Offset Practice", Sustainability 10(11), 4161, DOI 10.3390/su10114161, licence CC BY (lu via WebFetch) : ne traite pas des Biotopwertverfahren ; cité pour le constat d'hétérogénéité entre Länder (section 6).

#### Sources consultées

| URL | Statut |
|---|---|
| https://www.gesetze-im-internet.de/bkompv/index.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/BJNR108800020.html | lue intégralement (HTML brut) |
| https://www.gesetze-im-internet.de/bkompv/__4.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__5.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__6.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__7.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__8.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__9.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__12.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__13.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__14.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__17.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/__18.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/anlage_1.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/anlage_2.html | lue intégralement (889 lignes extraites) |
| https://www.gesetze-im-internet.de/bkompv/anlage_3.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/anlage_5.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/anlage_6.html | lue intégralement |
| https://www.gesetze-im-internet.de/bkompv/xml.zip | téléchargée, non exploitée |
| https://www.gesetze-im-internet.de/urhg/__5.html | lue intégralement |
| https://www.gesetze-im-internet.de/hinweise.html | lue partiellement (sections 6 et 7) |
| https://www.gesetze-im-internet.de/impressum.html | lue via WebFetch |
| https://www.bundesumweltministerium.de/themen/naturschutz/gebietsschutz-und-vernetzung/bundeskompensationsverordnung | lue via WebFetch |
| https://www.bfn.de/eingriffsregelung | partiellement (navigation seule, aucun document livré) |
| https://epflicht.ulb.uni-bonn.de/download/pdf/692898 (Handreichung BKompV, BfN/BMU 2021) | téléchargée, lue partiellement |
| https://www.lexaris.de/book/version/documentflat/head/1329058 (KV Hesse 2018) | lue intégralement |
| https://www.rv.hessenrecht.hessen.de/bshe/document/jlr-KompVHE2018rahmen | non accessible |
| https://umwelt.hessen.de/naturschutz/eingriffsregelung-und-kompensation | non accessible |
| https://umweltministerium.hessen.de/sites/umwelt.hessen.de/files/2021-08/einfuehrung_in_die_kompensationsverordnung_2018.pdf | non accessible (404) |
| https://umwelt-online.de/recht/natursch/laender/he/kv.htm (KV 2005) | lue intégralement |
| https://umwelt-online.de/recht/natursch/laender/he/kv_in.htm | lue intégralement |
| https://umwelt-online.de/recht/natursch/laender/he/kv18.htm | lue partiellement (démo) |
| https://rp-giessen.hessen.de/sites/rp-giessen.hessen.de/files/2026-07/u19.1_03.1_kv-bilanz_anlage_3.1.pdf | lue via WebFetch |
| https://www.uvp-verbund.de/documents-ige-ng/igc_he/B0E0D331-8400-45F8-8AE0-20F7B8AFA019/UL19-3-1_AVb_KV-Berechnung_A3-Format.pdf | lue via WebFetch (version KV non identifiée) |
| https://www.gesetze-bayern.de/Content/Document/BayKompV | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-4 | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-7 | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-8 | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-9 | lue partiellement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-24 | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-ANL_5 (Anlage 3.1) | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayKompV-ANL_6 (Anlage 3.2) | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/BayVwV319722/true | lue intégralement |
| https://www.gesetze-bayern.de/Content/Document/Impressum | lue via WebFetch |
| https://www.stmuv.bayern.de/themen/naturschutz/eingriffe/doc/biotopwertliste.pdf | lue intégralement |
| https://www.lfu.bayern.de/natur/kompensationsverordnung/index.htm | lue via WebFetch |
| https://www.lanuk.nrw.de/fileadmin/lanuvpubl/4_arbeitsblaetter/Arbeitsblatt_61.pdf | lue intégralement |
| https://www.lanuk.nrw.de/fileadmin/lanuv/natur/uploads/Biotoptypenliste_Numerische_Bewertung_Eingriffsregelung_aktuell_01.xlsx | lue (feuille 1 extraite) |
| https://www.lanuk.nrw.de/themen/natur/eingriffsregelung/numerische-bewertung-von-biotopraeumen | lue partiellement (liens extraits) |
| https://www.territoire-de-belfort.gouv.fr/index.php/contenu/telechargement/24544/177227/file/Num_Bew_Biotyp_NRW_Sept2008.pdf | non accessible |
| https://kreis-soest.de/fileadmin/citko_buerger/Dateien/Numerische_Bewertung_von_Biotoptypen_fuer_die_Eingriffsregelung_Stand_Juni_2021.pdf | non accessible (404) |
| https://epflicht.ulb.uni-muenster.de/download/pdf/131330 | non accessible (anti-robot) |
| https://depositonce.tu-berlin.de/items/2535e269-9c84-4328-a734-a241590d9120 | lue (métadonnées) |
| https://api-depositonce.tu-berlin.de/server/api/core/bitstreams/5bac8870-5377-4297-b805-348420c5249f/content (Bruns 2007) | téléchargée, lue partiellement |
| https://www.bfn.de/sites/default/files/2021-06/Dietrich_Schweppe-Kraft_Haarnacke_2014_offsetting_time_lags.pdf | lue via WebFetch |
| https://www.forest-trends.org/wp-content/uploads/imported/loss-gain-calculations-in-german-imr_md_100324-pdf.pdf | lue via WebFetch |
| https://www.forest-trends.org/?p=4467 | lue via WebFetch |
| https://ieep.eu/wp-content/uploads/2022/12/Eco-Accounts_BW_case_study_final_221114.pdf | lue via WebFetch |
| https://fis.tu-dresden.de/portal/en/publications/biodiversity-offsets(1fea2a00-4e9d-4661-87b2-3d22e11092f6).html | lue via WebFetch (métadonnées) |
| https://www.mdpi.com/2071-1050/10/11/4161 | lue via WebFetch |

### 2.3 MSA, GLOBIO et Global Biodiversity Score (GBS)

Date de consultation de toutes les sources : 17/10/2026.
Règle appliquée : chaque valeur numérique ci-dessous a été lue dans un document effectivement récupéré (PDF, page HTML, fichier docx de matériel supplémentaire, dépôt Git cloné). Les éléments non lus sont signalés "NON VÉRIFIÉ".

#### 1. Objet

L'indicateur MSA (Mean Species Abundance) mesure l'abondance moyenne des espèces originelles d'un milieu par rapport à leur abondance dans un milieu non perturbé, entre 0 et 1 (ou 0 % et 100 %). Il est produit par le modèle GLOBIO du PBL (Pays-Bas) à partir de relations pression-réponse par usage des sols, fragmentation, infrastructures, dépôt d'azote, changement climatique et chasse. Le Global Biodiversity Score (GBS) de CDC Biodiversité réutilise ces relations pour produire des empreintes d'entreprise exprimées en MSA.km².

La fiche couvre : les 2 articles fondateurs (Alkemade 2009 pour GLOBIO3, Schipper 2020 pour GLOBIO 4), la documentation technique GLOBIO 3.5 et GLOBIO 4 (dont le code public), la documentation GBS (revue 2020, rapport sectoriel construction 2026, licence), 2 critiques publiées et la question des valeurs urbaines fines.

#### 2. Accès et licence

| Source | URL exacte | Accès | Licence (telle que lue) |
|---|---|---|---|
| Schipper et al. 2020, Global Change Biology 26:760-771, DOI 10.1111/gcb.14848 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7028079 | Libre (PMC) | "This is an open access article under the terms of the http://creativecommons.org/licenses/by/4.0/ License" (CC BY 4.0) |
| Schipper 2020, Supporting Information (GCB-26-760-s001.docx) | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7028079/supplementaryFiles | Libre (zip Europe PMC) | Même licence que l'article |
| Alkemade et al. 2009, Ecosystems 12:374-390, DOI 10.1007/s10021-009-9229-5 | https://unstats.un.org/unsd/envaccounting/seeaRev/meeting2013/EG13-BG-5.pdf (copie du PDF éditeur Springer) | Libre | "This article is distributed under the terms of the Creative Commons Attribution Noncommercial License" (CC BY-NC), mention "published with open access at Springerlink.com" |
| GLOBIO 3.5 technical model description (PBL n°2369, 2016) | https://www.pbl.nl/downloads/pbl-publication-2369pdf | Libre | "Parts of this publication may be reproduced, providing the source is stated" |
| GLOBIO 4, données de sortie (Schipper et al. 2020, rasters 10 arc-sec) | https://www.globio.info/globio-data-downloads | Libre | "Creative Commons License (CC-BY 4.0) and is free to use" |
| GLOBIOweb technical documentation (PBL, 19/02/2023, 48 p.) | https://www.globio.info/wp-content/uploads/2023/03/GlobioWeb_technical_documentation_20230219.pdf | Libre | Aucune mention de licence dans le PDF ; renvoie au code GitHub |
| Code GLOBIO 4 (GlobioModelPublic) | https://github.com/GLOBIO4/GlobioModelPublic (cloné le 17/10/2026, commit 21f868f du 17/07/2025) | Libre | Fichier LICENSE : "EUROPEAN UNION PUBLIC LICENCE v. 1.2" (EUPL-1.2) |
| GBS Review: Core concepts (CDC Biodiversité, mai 2020, 32 p.) | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/20200518_GBS-review_Core-concepts_final-version_no-track-changes.pdf | Libre | Aucune mention de licence dans le PDF |
| GBS Review: Terrestrial pressures on biodiversity (CDC Biodiversité, mars 2020, 43 p.) | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/Terrestrial-pressures-on-biodiversity.pdf | Libre | Aucune mention de licence dans le PDF |
| GBS Review: Wood logs CommoTool (juillet 2020, version corrigée) | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/Woodlogs-CommoTool.pdf | Libre | Aucune mention de licence dans le PDF |
| GBS Independent Review Report (Solinnen pour OFB, juin 2020, 62 p., réf. SOL 19-032) | https://oai-gem.ofb.fr/exl-php/document-affiche/ofb_recherche_oai/OUVRE_DOC/62001?fic=doc00085670.pdf (notice : https://www.documentation.eauetbiodiversite.fr/notice/00000000019660b568f0a929748d4112) | "Accès libre" (notice OFB) ; téléchargement nécessitant les cookies de session | Non précisée |
| MEB Outlook n°18, "GBS: Establishing an ecosystem of stakeholders", déc. 2021 (56 p.) | https://www.cdc-biodiversite.fr/download/global-biodiversity-score-establishing-an-ecosystem-of-stakeholders-to-measure-the-biodiversity-performance-of-human-activities/?wpdmdl=3531 | Libre | Seules les dépendances dérivées d'ENCORE sont indiquées "CC BY-SA 4.0" |
| MEB Report n°49, "GBS: Accounting for positive and negative impacts throughout the value chain", oct. 2023 (60 p.) | https://www.cdc-biodiversite.fr/wp-content/uploads/2024/01/DOSSIER-MEB-49-GBS-MD-WEB.pdf | Libre | Aucune mention de licence |
| Sectoral report "Construction and biodiversity", version 2.0, juin 2026 (69 p.) | https://www.cdc-biodiversite.fr/wp-content/uploads/2026/06/20260601_Sectoral-report_Construction.pdf | Libre | "Content licensed under the Creative Commons Attribution-Non Commercial 4.0 International (CC BY-NC 4.0) except for results derived from ENCORE" (CC BY-SA 4.0 pour ces derniers) ; "Contact us for commercial uses" |
| Changelog GBS | https://www.cdc-biodiversite.fr/simplified-changelog-gbs/ | Libre | Sans objet |
| Hub Notion "GBS Documentation" et page "MSA land use layer" | https://cdc-biodiversite.notion.site/GBS-Documentation-27f15ff341c480e8a12efcf55a4779cd ; https://cdc-biodiversite.notion.site/MSA-land-use-layer-12715ff341c480659666e0e70b83bbc1 | Libre (contenu lu via l'API publique Notion) | Section "Licence" de la page MSA layer : "The current version of the map is open for review" ; contact gbs@cdc-biodiversite.fr pour intégration |

Conditions d'accès à l'outil GBS lui-même (logiciel, bases de facteurs), lues dans MEB Outlook n°18 (déc. 2021), section 4.2 "Do I need a GBS licence to use the tool?" : "A licence is required for the use of the Global Biodiversity Score trademark, the GBS software and its data". "If a company only wants to conduct internal test through an assessment of its biodiversity footprint conducted by an external assessor, and no results of the assessment are made public, a licence is not mandatory for the company (but still is for the external assessor)". "The licence can also be purchased as a standalone (as of 2021, EUR 1500 excluded VAT per year)". "Consultants must join the B4B+ Club to access the licence extensions for commercial use". "Data providers and rating agencies require a specific licence". Confirmé par MEB Report n°49 (2023) : "Users of the GBS need a licence to use the Global Biodiversity Score trademarks, but also to use the software and the associated databases and documentation, and for consultants to sell services using the GBS". Le changelog mentionne un "package GBS-ecoinvent (sous licence)" à la version 1.3.1. Aucune mention de NDA n'a été lue. Conclusion : documentation méthodologique publique et gratuite ; logiciel, bases de facteurs d'impact et usage commercial sous licence payante.

Versions du GBS lues dans le changelog : 1.0.1 (13/11/2020) jusqu'à 1.6.1 (13/03/2026). La version 1.4.10 (15/05/2025) est celle utilisée par le rapport sectoriel construction 2026.

#### 3. Principe du calcul

##### 3.1 Définition de la MSA

Schipper et al. 2020, section 2.1.1 : "MSA values are retrieved by dividing the abundance of each species found in relation to a given pressure level by its abundance found in an undisturbed situation within the same study, truncating the values at 1, and then calculating the arithmetic mean over all species present in the reference situation". Les augmentations d'abondance sont tronquées "to avoid the indicator being inflated by opportunistic or generalist species".

Formulation du GBS (Core concepts, lignes 174-180, citant Schipper et al. 2016) : MSA = (1 / N_reference_species) x somme sur i de Min(A_observed(i) / A_intact(i), 100 %).

##### 3.2 Combinaison des pressions

Alkemade et al. 2009, équation (1), p. 380 : MSA_i = MSA_LU,i x MSA_N,i x MSA_I,i x MSA_F,i x MSA_CC,i (LU usage des sols, N dépôt d'azote, I infrastructures, F fragmentation, CC changement climatique), dans l'hypothèse "no interaction". Hypothèses associées (p. 380) : "N deposition does not affect MSA in croplands" ; "climate change and infrastructure were assumed to affect only natural and semi-natural areas, and effects of infrastructure were reduced in protected areas".

Schipper et al. 2020, équation (1) : MSA_s,i = produit de x = 1 à m de MSA_x,s,i (s groupe d'espèces, i cellule). 2 approches selon l'usage des sols (Table S1 du matériel supplémentaire) : "If the land use impact is expected to dominate over other impacts, the overall MSA value equals the MSA value of the land-use class". Table S1 lue intégralement : pour Urban, seul le changement climatique s'ajoute ("yes" pour Climate change, "no" pour Nitrogen deposition, Fragmentation, Road disturbance, Hunting) ; pour Cropland (intense et light) et Pasture intense : climat et routes "yes", azote, fragmentation et chasse "no" ; Pasture light : climat, fragmentation, routes "yes" ; Forestry : tout sauf chasse ; Secondary et Primary vegetation : toutes les pressions "yes".

Équation (2) de Schipper 2020 (contribution de chaque pression à la perte) : P_x,s,i = (1 - MSA_x,s,i) / somme_x(1 - MSA_x,s,i) x (1 - MSA_i).

GLOBIO 3.5 (PBL 2016, p. 10 à 11) formalise la priorité : "if LU = cropland OR LU = urban, MSA_i = MSA_LU,i".

##### 3.3 Agrégation spatiale

Alkemade 2009, équation (2) : MSA_r = somme_i(MSA_i x A_i) / somme_i(A_i), moyenne pondérée par la surface des cellules. Schipper 2020 : agrégation "calculated as mean value weighted by the area of the grid cells". GLOBIOweb (PBL 2023, Table 4.4) : "Mean MSA = (Sum of (MSA per cell x cell area)) / total land area" et "Mean MSA loss = 1 - Mean MSA".

GLOBIO 4 (GLOBIOweb 2023, section 4.4) calcule séparément une MSA plantes et une MSA oiseaux-mammifères, puis "Combined overall terrestrial MSA: the average of the MSA for plants and birds & mammals". Dans le code GLOBIO 4 (Globio_Config.glo), les facteurs de pondération INFRADIST_WeightFactor, INFRAG_WeightFactor, NDEP_WeightFactor et HUMANENC_WeightFactor valent tous 0.5 (poids du groupe taxonomique affecté dans la MSA globale).

##### 3.4 Unité MSA.km² et impacts statiques / dynamiques (GBS)

Core concepts (lignes 199-204) : "Through the spatial integration of MSA % over a surface area, impacts can be expressed in MSA.km². The latter is the product of MSA (in %) multiplied by the area to which it applies (expressed in km²)". Exemple lu : "for a surface area of 1 km² of intensely cultivated fields (MSA = 10 %), the value is 1x10% = 0.1 MSA.km²" ; "a change in MSA from 100% to 75% over a surface area of 1 km² corresponds to a loss of (100%-75%)*1 = 0.25 MSA.km²".

Impact statique (Terrestrial pressures, équation 1, ligne 330) : MSA_static_LU(n) = S_LU(n) x (100 % - MSA_LU). Impact dynamique (ligne 184) : MSA_dynamic_LU(n vers n+1) = S_RP,LU(n+1) x (MSA_RP(n) - MSA_LU), où RP est le "restricted perimeter" (surfaces dont l'usage a changé) et MSA_RP(n) la MSA moyenne initiale de ce périmètre. Relation de cohérence (ligne 301) : MSA_static(n+1) = MSA_static(n) + somme des MSA_dynamic_LU. Règle d'évaluation par défaut (lignes 198-199) : "biodiversity gains due to spatial pressures (land use, fragmentation and encroachment) are capped at 0".

Core concepts (lignes 314-322) : "'Dynamic footprint' is the footprint caused by changes, consumptions or restorations during the period assessed. 'Static footprint' or 'ecological opportunity cost' includes all the 'persistent' or 'long-lasting' effects which remain over time" ; "Static footprints should be accounted for separately and, unlike dynamic footprints, should not be summed up over time".

Unité complémentaire MSAppb (MEB n°49, 2023, section 3.1) : surface terrestre émergée 133 millions de km², surfaces d'eau douce 10,3 millions de km² ; "1 MSAppb = 0.133 MSA.km²" (terrestre) et "1 MSAppb = 0.010 MSA.km²" (aquatique).

#### 4. Valeurs disponibles

##### 4.1 MSA par usage des sols, GLOBIO3 (Alkemade et al. 2009, Table 4, p. 379)

| Classe GLC2000 / sous-catégorie | MSA_LU | SE |
|---|---|---|
| Snow and ice (primary vegetation) | 1.0 | <0.01 |
| Bare areas (primary vegetation) | 1.0 | <0.01 |
| Forests, primary vegetation | 1.0 | <0.01 |
| Lightly used natural forest | 0.7 | 0.07 |
| Secondary forests | 0.5 | 0.03 |
| Forest plantation | 0.2 | 0.04 |
| Scrublands and grasslands, primary vegetation | 1.0 | <0.01 |
| Livestock grazing | 0.7 | 0.05 |
| Man-made pastures | 0.1 | 0.07 |
| Agroforestry (mosaic cropland/forest) | 0.5 | 0.06 |
| Low-input agriculture | 0.3 | 0.12 |
| Intensive agriculture | 0.1 | 0.08 |
| Built-up areas (artificial surfaces, "Areas more than 80% built up") | 0.05 | note b : "Estimate based on expert opinion, representing densely populated cities" |

Texte p. 381 : "For urban areas no proper data were found and the value 0.05 was assigned by expert opinion". Document : Alkemade et al. 2009, URL https://unstats.un.org/unsd/envaccounting/seeaRev/meeting2013/EG13-BG-5.pdf.

##### 4.2 Fragmentation, infrastructures, azote, climat, GLOBIO3 (Alkemade et al. 2009)

Table 7, p. 382 ("The Relationship Between Area and Corresponding Fraction of Species Assumed to Meet Their Minimal Area Requirement") :

| Surface de la tache (km²) | MSA_F | SE |
|---|---|---|
| <1 | 0.3 | 0.15 |
| <10 | 0.6 | 0.19 |
| <100 | 0.7 | 0.19 |
| <1 000 | 0.9 | 0.20 |
| <10 000 | 0.95 | 0.20 |
| >10 000 | 1.0 | 0.20 |

Table 6, p. 382 (zones d'impact des routes, UNEP/RIVM 2004) : High impact MSA_I 0.4 (SE 0.22) ; Medium impact 0.8 (SE 0.13) ; Low impact 0.9 (SE 0.06) ; No impact 1.0 (SE 0.02). Les largeurs de bandes en km varient par biome (Figure 4, p. 382, graphique seulement : le texte ne donne pas les largeurs chiffrées par biome ; axe 0 à 16 km).

Table 5, p. 381 (dépôt d'azote, NE = dépassement de charge critique en g/m²) : Arctic alpine MSA_N = 1 - 0.15 ln(NE + 1) (R² 0.81, n 9) ; Boreal and temperate forests MSA_N = 1 - 0.22 ln(NE + 1) (R² 0.96, n 12) ; Grasslands MSA_N = 1 - 0.19 ln(NE + 1) (R² 0.85, n 21).

Table 8, p. 383 (pentes b de MSA_CC = 1 - b x GMTI, colonnes IMAGE et EUROMOVE ; valeurs marquées * utilisées dans GLOBIO3) : Ice 0.02* / 0.07 ; Tundra 0.17 / 0.05* ; Wooded tundra 0.24 / 0.07* ; Boreal forest 0.04* / 0.07 ; Cool conifer forest 0.17 / 0.08* ; Temp. mixed forest 0.04* / 0.12 ; Temp. deciduous forest 0.09* / 0.14 ; Warm mixed forest 0.05* / 0.17 ; Grassland and steppe 0.09* / 0.17 ; Hot desert 0.04* ; Scrubland 0.12* / 0.17 ; Savanna 0.09* ; Tropical woodland 0.03* ; Tropical forest 0.03*.

Table 9, p. 384 : MSA mondiale 0.70 en 2000 et 0.63 en 2050 (scénario de référence) ; Europe 0.45 en 2000 et 0.33 en 2050.

##### 4.3 MSA par usage des sols, GLOBIO 3.5 (PBL 2016, Table 2.2, p. 10)

| Classe GLOBIO 3.5 | MSA_LU |
|---|---|
| Forest - Natural | 1.0 |
| Forest - Plantation | 0.30 |
| Forest - Clear-cut harvesting | 0.50 (note a : moyenne sur la végétation secondaire) |
| Forest - Selective logging | 0.70 |
| Forest - Reduced impact logging | 0.85 |
| Burnt forest | 1.0 |
| Natural grassland | 1.0 |
| Pasture - moderately to intensively used | 0.60 |
| Pasture - man-made | 0.30 |
| Extensive cropland | 0.30 |
| Intensive cropland | 0.10 |
| Irrigated cropland | 0.05 |
| Woody biofuels | 0.30 |
| Bare area | 1.0 |
| Snow and ice | 1.0 |
| Urban area | 0.05 (note b : "Value for densely populated cities without significant green space; based on expert judgement") |

Sources de la table : "Alkemade et al. 2009; Alkemade et al. 2013; GLOBIO reference database". URL : https://www.pbl.nl/downloads/pbl-publication-2369pdf.

Autres valeurs GLOBIO 3.5 lues :
- Fragmentation, Table 6.1 (p. 19) : 0-1 km² MSA_F 0.35 ; 1-10 km² 0.45 ; 10-100 km² 0.65 ; 100-1 000 km² 0.90 ; 1 000-10 000 km² 0.98 ; >10 000 km² 1.00. Valeurs "corrected for the assumption that invertebrates and plants are not impacted by fragmentation".
- Infrastructures (section 5, p. 17 à 18) : zone d'impact de 1 km autour des infrastructures (routes GRIP types 1 à 5 et DCW) ; MSA oiseaux-mammifères 0.66 dans cette zone (Benítez-López et al. 2010), soit MSA_I globale "4/6 x 0.66 + 2/6 x 1 = 0.78" ; en aire protégée MSA_I = 0.90.
- Empiètement humain (section 7, p. 20) : zone de 10 km autour des zones urbaines et cultivées ; MSA oiseaux-mammifères 0.56, soit MSA_E = "2/6 x 0.56 + 4/6 x 1 = 0.85" ; MSA_E = 1 en aire protégée.
- Table 1.1 (p. 7) : la fragmentation (MSA_F) et les infrastructures (MSA_I) s'appliquent aux mammifères, oiseaux, amphibiens, reptiles, pas aux invertébrés ni aux plantes ; l'empiètement (MSA_E) aux mammifères et oiseaux seulement.

##### 4.4 GLOBIO 4 (Schipper et al. 2020 et code public)

Valeurs par classe d'usage des sols : l'article ne donne aucune valeur chiffrée dans le texte ; elles sont uniquement représentées graphiquement en Figure 2c (barres avec intervalles de confiance à 95 %), classes Cr.I, Cr.M, Pa.I, Pa.M, Pl, Se, Ur (cropland intense / minimal, pasture intense / minimal, plantation, secondary vegetation, urban), plantes en vert et vertébrés à sang chaud en rouge. Note de l'article : "Correction added on 31 December 2019 after first online publication: figure 2C has been updated". Le matériel supplémentaire (lu intégralement : Text S1, S2, Tables S1 à S5, Annex S1) ne contient pas de table de MSA_LU. Lecture graphique de la Figure 2c (image GCB-26-760-g002.jpg, approximative, à ne pas utiliser comme valeur de référence) : Ur plantes environ 0.3, Ur vertébrés environ 0.25 ; Se environ 0.55 (plantes) et 0.6 (vertébrés) ; Cr.I plantes environ 0.15, vertébrés environ 0.35.

Valeurs chiffrées GLOBIO 4 effectivement lues, dans la documentation GLOBIOweb (PBL, 19/02/2023, Table 3.1, p. 18), "MSA values for birds & mammals and plants per GLOBIO4 LULC type" :

| Code | Classe GLOBIO4 | Oiseaux et mammifères | Plantes | Origine indiquée |
|---|---|---|---|---|
| 1 | Urban-settlement | 0.264 | 0.361 | "Based on Schipper et al. 2020" |
| 10 | Cropland | 0.452 | 0.156 | Kok et al. 2022, agriculture globale |
| 11 | Cropland intensive use | 0.401 | 0.149 | Kok et al. 2022 |
| 12 | Cropland minimal use | 0.502 | 0.162 | Kok et al. 2022 |
| 13 | Mosaic cropland (>50 %) / natural vegetation | 0.671 | 0.493 | 60 % cropland + 40 % naturel (1.000) |
| 14 | Mosaic natural vegetation (>50 %) / cropland | 0.781 | 0.662 | 40 % cropland + 60 % naturel |
| 20 | Grazing | 0.452 | 0.156 | Kok et al. 2022 |
| 21 | Intensive pastures | 0.401 | 0.149 | Kok et al. 2022 |
| 22 | Extensive rangelands | 0.502 | 0.162 | Kok et al. 2022 |
| 30 | Forestry | 0.589 | 0.259 | "Based on Schipper et al. 2020" |
| 40 | Secondary vegetation | 0.621 | 0.568 | "Based on Schipper et al. 2020" |
| 50 à 220 | Couverts naturels | 1 | 1 | note (*) |

Aucun intervalle de confiance n'est donné dans cette table. Seuil d'intensité agricole (section 2.3, étape 6) : 100 kg N/ha (10 Mg/km²) d'engrais azoté.

Relations pression-réponse GLOBIO 4 (formes lues dans le code et coefficients lus dans Config/Globio_Config.glo du dépôt GitHub GLOBIO4/GlobioModelPublic, clone du 17/10/2026) :
- Fragmentation (GLOBIO_CalcInfraFragmentationMSA.py, ligne 334) : MSA = 1 / (1 + exp(-b0 - b1 x log10(surface de la tache en km²) - 2 x b1)), commentaire du code : "Original regression using ha so last term (2 * b1) is needed to convert the relationship to km2" ; coefficients INFRAG_WbVertRegressionCoefficients = -0.774 | 0.594 (b0, b1), poids 0.5 ; valeurs bornées entre 0 et 1. Schipper 2020 (Text S1) : taches de 10 000 ha ou plus prises comme référence, donc "fragmentation impacts are absent in patches of 10,000 ha or more" ; 39 valeurs MSA issues de 7 études.
- Routes (GLOBIO_CalcInfraDisturbanceMSA.py, ligne 252) : MSA = 1 / (1 + exp(-b0 - b1 x log10(distance en km) - 3 x b1)) ; INFRADIST_WbVertRegressionCoefficients = -1.772 | 1.391 ; INFRADIST_MaximumDistanceKM = 150 ; exclusion de la classe urbaine (INFRADIST_LandcoverExlCodes = 1). Schipper 2020 : routes GRIP types 1 à 3 seulement ; 204 valeurs MSA de 34 études ; aucune bande de distance tabulée (Figure 2e, courbe continue de 1 m à quelques km).
- Dépôt d'azote (GLOBIO_CalcNDepositionMSA.py, ligne 139) : MSA plantes = 1 / (1 + exp(-b0 - b1 x log10(dépôt en kg/ha/an))) ; NDEP_PlantRegressionCoefficients = 2.195 | -0.743 ; classes exclues 1, 10 à 13, 20 à 22 (urbain, cultures, pâturages). Schipper 2020 : 89 valeurs MSA de 37 études (base Midolo et al. 2019).
- Changement climatique (GLOBIO_CalcClimateChangeMSA.py, lignes 201 et 223) : MSA = 1 / (1 + exp(-b0 - b1 x GMTI)) ; CLIMCH_WbVertRegressionCoefficients = 3.213 | -0.362 ; CLIMCH_PlantRegressionCoefficients = 2.867 | -0.467 ; GMTI en °C depuis l'ère préindustrielle (1.116 °C pour 2015 et 1.259 °C pour 2020 dans GLOBIOweb Table 3.2).
- Chasse / empiètement (HUMANENC) : coefficients -0.223 | 0.876, distance maximale 150 km, tampon 1 km ; limitée aux biomes tropicaux.
Remarque : ces coefficients sont ceux du fichier de configuration public ; le script de fragmentation contient dans sa section de test des valeurs différentes ("0.38|0.13") et le script de perturbation routière "1.06|0.36", ce qui montre que les valeurs ont évolué entre versions. L'article Schipper 2020 lui-même ne publie pas ces coefficients.

Résultats agrégés Schipper 2020 (Table S2 lue) : MSA mondiale 0.56 en 2015 (plantes 0.53, vertébrés 0.60) ; Western Europe 0.56 (plantes 0.52, vertébrés 0.60). Table S4 (Western Europe, 2015) : pertes de MSA plantes CC -0.08, ND -0.03, LU -0.38, total -0.48 ; vertébrés CC -0.05, LU -0.23, F -0.05, RD -0.07, total -0.40.

##### 4.5 Valeurs utilisées par le GBS

Terrestrial pressures (Figure 2, p. 6) : le GBS 1.0 utilise GLOBIO 3.6 et "GLOBIO GBO4" (13 classes) : Natural forest 100 % ; Plantation forest 30 % (note 1 : GLOBIO GBO4 utilise 20 %, le GBS 30 % "in line with GLOBIO 3.6") ; Clear-cut forest 50 % ; Selectively logged forest 70 % ; Reduced impact logging 85 % ; Natural grassland 100 % ; Moderately and intensively used pasture 60 % ; Man-made pasture 30 % ; Rain-fed low input cropland 30 % ; Rain-fed high input cropland 10 % ; Irrigated cropland 5 % ; Woody biofuels 30 % ; Bare area 100 % ; Urban 5 % ("Also called Built-up areas. Areas more than 80% built up"). Ligne 143 : "For urban areas no proper data was found and the value of 5% was assigned by the PBL by expert opinion". Ligne 120 : "GLOBIO 4 model is out since early 2020 (Schipper et al. 2020). We have not yet been able to get access to the detailed projection data up to 2050 to update the GLOBIO3.6 data used in the GBS".

Fragmentation et empiètement (section 3) : relation de fragmentation reprise d'Alkemade 2009 (Figure 11) ; empiètement : "an MSA of 85% is applied within a 10-km zone around man-made areas for all types of biomes" ; répartition de la fragmentation entre usages anthropiques et infrastructures : 100 % / 0 %, 0 % / 100 % ou 50 % / 50 % selon présence (section 3.2.B) ; intensités exprimées en MSA.km²/km² d'usage anthropique, "data quality tier 2" ; "The refined Encroachment and Fragmentation biodiversity pressures evaluations are not implemented in the GBS for now".

Azote (section 4) : intensité globale "expressed in MSA.km² per tonne N-equivalent" calculée comme impacts globaux GLOBIO-IMAGE divisés par émissions mondiales EDGAR ; valeur numérique non publiée dans le document. Pas d'évaluation affinée dans GBS 1.0.

Changement climatique (section 5, Table 2 lue en image, p. 36) : MSA_loss par °C, Arets, Verwer et Alkemade 2014 : Boreal forest 0.0367 ; Cool coniferous forest 0.1127 ; Grassland and steppe 0.1201 ; Hot desert 0.0521 (a) ; Ice 0.0356 ; Mediterranean shrub 0.0521 (a) ; Savanna 0.0775 ; Scrubland 0.0661 ; Temperate deciduous forest 0.071 ; Temperate mixed forest 0.0487 ; Tropical forest 0.0521 (a) ; Tropical woodland 0.1075 ; Tundra 0.0426 ; Warm mixed forest 0.1457 ; Wooded tundra 0.0521 (a) ; Overall 0.0521 (SE 0.0047, N 239) ; (a) = "set equal to the overall MSA loss factor". Facteur d'impact dynamique (ligne 796) : "4.37.10-9 MSA.km2/kg CO2-eq" (IAGTP 4.76 x 10^-14 °C.an/kg CO2 sur 100 ans) ; variante 3.29 x 10^-9 si le facteur "Overall" est utilisé sans pondération par biome.

Facteurs par matière première publiés (Wood logs CommoTool, juillet 2020, Table 7, p. 24, composante changement climatique uniquement, MSA.km²/t) : Hardwood non-sustainable EU 9.41 x 10^-8 (21.5 kg CO2-eq/t) ; US, CA 9.45 x 10^-8 ; RoW 1.50 x 10^-7 ; Softwood EU, FI, SE 7.06 x 10^-8 (16.2 kg CO2-eq/t) ; US, CA 7.30 x 10^-8 ; RoW 6.97 x 10^-7. Les facteurs d'usage des sols par tonne de bois sont décrits (sections "COMPUTE THE LU DYNAMIC AND STATIC BIODIVERSITY IMPACT FACTORS IN MSA.KM²/T OF WOOD") mais leurs valeurs ne sont pas tabulées dans ce document.

Secteur construction (Sectoral report v2.0, juin 2026, calculs GBS 1.4.10, mai 2025, données EXIOBASE 3.8 de 2011, chiffre d'affaires mondial 7 500 000 MEUR) :
- Table 2 (Scope 1, MSA.km²) : terrestre statique 55 000 ; terrestre dynamique 1 100 ; aquatique statique 80.
- Table 3 (Scope 3 amont tier 1) : terrestre statique 940 000 ; dynamique 13 100 ; aquatique statique 21 400.
- Table 4 (intégré verticalement) : terrestre statique 3 100 000 ; dynamique 33 000 ; aquatique statique 120 000.
- Table 5 (intensités Scope 1, MSA.m²/kEUR hors écotoxicité / écotoxicité seule / MSAppb/bEUR) : terrestre statique 7 / 0.5 / 54 ; terrestre dynamique 0.14 / NA / 1.0 ; aquatique statique 0.01 / 0.07 / 1.0.
- Table 6 (Scope 3 amont tier 1) : terrestre statique 50 / 390 / 930 ; dynamique 2 / NA / 13 ; aquatique statique 3 / 5 / 270.
- Table 7 (intégré verticalement) : terrestre statique 410 / 1 210 / 3 100 ; dynamique 4 / NA / 33 ; aquatique statique 16 / 16 / 1 500.
- Seuil "compatible avec les limites planétaires" cité : 320 MSA.m²/kEUR, défini (glossaire, p. 54) comme 28 % MSA x surface émergée totale / chiffre d'affaires mondial.
- Avertissement du rapport (p. 23) : "The Construction sector shows low Scope 1 land use impact intensities because of the way GBS calculations are performed: they rely on financial data without accounting for infrastructures, which leads to an underestimation of results" ; "construction site areas are not included".
- Matériaux (section C.2, Figures 13 à 16) : 8 matériaux évalués (sable quartz, verre plat, acier d'armature, ciment Portland, lingot d'aluminium, cuivre, bois feuillu, bois résineux) à partir de facteurs GBStoolbox / GBSecoinvent, mais les impacts par kg ne sont donnés que sous forme de graphiques sans étiquettes de valeurs (Figure 14 : axe des impacts statiques terrestres par kg gradué de 0 à 0.00001 MSA.km², aluminium environ 0.0000095, cuivre environ 0.0000058, acier d'armature environ 0.0000023, verre environ 0.000002, ciment environ 0.0000003 ; Figure 15 : axe dynamique 0 à 5 x 10^-8 MSA.km²/kg, aluminium environ 4.9 x 10^-8, cuivre 1.5 x 10^-8, acier 1 x 10^-8, ciment 4 x 10^-9). Ces lectures graphiques sont approximatives ; aucune valeur chiffrée par kg de béton, ciment, acier ou bois n'est imprimée dans le rapport. Table 8 (consommations ADEME 2015 de matériaux pour bâtiments neufs) est une image non extraite.
- Fiche sectorielle construction 2022 (GBS 1.2.2, octobre 2021), lue via WebFetch : Scope 1 terrestre dynamique 0.59 MSA.m²/kEUR, statique 0.55 ; intégré verticalement dynamique 4.9, statique 210 MSA.m²/kEUR. Le rapport 2026 explique l'écart par l'ajout de la pression climat statique "from version 1.4.2".

CDC Biodiversité "MSA land use layer" (Notion, 2024) : 15 classes, résolution ESA-CCI 300 m, valeurs GLOBIO 3.5 reprises (Agroforestry 50 %, Natural forest 100 %, Productive plantations 30 %, RIL 85 %, Selective logging 70 %, Clear cut 50 %, Extensive croplands 30 %, Intensive croplands 10 %, Irrigated 5 %, Pasture man-made 30 %, Moderately used pastures 60 %, Natural grassland 100 %, Urban 5 %, Bare 100 %, Snow and ice 100 %). Avertissement lu : "this map is intended for regional analysis. Its use at very localized scales is limited by the resolution of the original ESA-CCI land cover map (approximately 300m)".

#### 5. Limites pour un calcul à l'échelle de la parcelle

1. Une seule valeur urbaine, d'origine experte : 0.05 dans GLOBIO3, GLOBIO 3.5 et le GBS ("no proper data were found", Alkemade 2009 p. 381 ; "densely populated cities without significant green space; based on expert judgement", PBL 2016 Table 2.2). GLOBIO 4 remplace cette valeur par des régressions PREDICTS (0.264 vertébrés, 0.361 plantes dans GLOBIOweb Table 3.1), soit un facteur 5 à 7 d'écart avec 0.05 ; les deux générations ne sont pas comparables.
2. Résolution et calibration : relations établies à l'échelle de cellules de 0.5° (GLOBIO3) ou 10 arc-secondes (environ 300 m, GLOBIO 4) ; CDC Biodiversité indique que sa couche MSA "is intended for regional analysis". Le GBS n'utilise pas de surfaces de chantier ("construction site areas are not included") et calcule le Scope 1 construction à partir de données financières.
3. Pas de pression intra-urbaine : Table S1 de Schipper 2020 : en classe Urban, seules les pertes climatiques s'ajoutent ; pas de perturbation routière, de fragmentation ni d'azote. Le code GLOBIO 4 exclut la classe 1 (urbain) des modules routes et azote.
4. Fragmentation uniquement pour les taches de végétation naturelle (oiseaux et mammifères), avec plancher implicite : les classes <1 km² (Alkemade 2009 : 0.3 ; GLOBIO 3.5 : 0.35) et la régression GLOBIO 4 ne sont pas conçues pour des taches de quelques centaines de m².
5. Groupes taxonomiques : GLOBIO 4 ne couvre que plantes et vertébrés à sang chaud (Schipper 2020, section 2.1.2) ; la fragmentation et les routes ne portent que sur les vertébrés.
6. Hétérogénéité et incertitude : intervalles de confiance à 95 % larges sur la Figure 2 de Schipper 2020 ; SE de 0.07 à 0.12 sur les classes agricoles d'Alkemade 2009 ; la revue indépendante (Solinnen 2020) rapporte l'avis de M. Huijbregts : "the MSA loss factors provided in the GBS-tool are not sufficiently scientific robust to use in practice with the exception of the MSA loss factors for land use" et la critique de C. Ionescu : "GLOBIO does not represent the actual state of biodiversity but a modelled version - potentially far from reality".
7. Critiques publiées avec DOI :
   - Marques et al. 2021, Int. J. Life Cycle Assessment, DOI 10.1007/s11367-020-01846-1 (CC BY) : "as those are species assemblage indicators, it is not possible to specifically relate the impact captured by these indicators to a list of affected species" ; "the selected indicators do not capture how environmental impacts affect species' physiology, dispersal, or their interactions with other organisms" ; "the LBII, MSA, and BHI indicators can currently only be measured for a limited number of realms and for a limited number of groups".
   - Hawkins et al. 2023, Conservation Biology, DOI 10.1111/cobi.14183 (résumé lu via la notice CIFOR-ICRAF) : "Top-down intactness metrics (e.g., Mean Species Abundance) can be valuable for generating high-level" estimations mais "do not provide sufficient precision or guidance for companies, regulators, or third-party assessors".
   - Durand et al. 2026, Conservation Biology 40(3), DOI 10.1111/cobi.70221 (manuscrit accepté lu sur ORA Oxford) : "at present, models are too generic to allow for context-specific assessments of biodiversity changes at a site level, making comparison of losses and gains challenging" ; cite "taxonomic biases and data gaps in the underlying datasets".
   - Kuipers, Melki, Morel et Schipper 2025 (ScienceDirect PII S266597272500073X, résumé lu sur globio.info) : "PDF leaves about half of the variance in MSA loss unexplained".
   - Faith, Ferrier et Williams 2008, Global Change Biology 14:207-217, DOI 10.1111/j.1365-2486.2007.01500.x : critique du BII (indice voisin), "only weakly linked to 'biodiversity' in its usual sense of 'variation'" ; cité par Alkemade 2009 dans ses références.

#### 6. Ce qui manque

- Aucune valeur MSA publiée pour des milieux urbains fins (toiture végétalisée, jardin, parc, friche, surface imperméabilisée) n'a été trouvée dans les sources lues : Alkemade 2009 (1 classe "built-up"), GLOBIO 3.5 (1 classe "Urban area"), GLOBIOweb 2023 (1 classe "Urban-settlement"), Schipper 2020 (1 classe "Ur"), GBS (1 classe "Urban", 5 %), couche MSA CDC 2024 (1 classe "Urban"). Les recherches ciblées (termes "green roof", "garden", "park", "brownfield", "sealed surface" associés à "mean species abundance") n'ont renvoyé que des études de biodiversité urbaine n'utilisant pas la MSA (par exemple Partridge et Clark 2022, DOI 10.3389/fevo.2022.779005, vérifiée : "The paper does not use or mention MSA"). Conclusion explicite : il n'existe pas, dans les sources primaires GLOBIO et GBS consultées, de MSA par type de surface urbaine fine ; une méthode parcellaire devra les construire (ou les dériver de PREDICTS, base utilisée par Schipper 2020, qui comporte une classe "Urban" à 3 niveaux d'intensité : "Minimal use", "Light use", "Intense use" d'après Text S1).
- Les coefficients des régressions GLOBIO 4 ne figurent pas dans l'article ni dans son matériel supplémentaire ; ils n'ont été obtenus que dans le fichier de configuration du code public (EUPL-1.2), sans intervalle de confiance.
- Les valeurs MSA_LU de GLOBIO 4 (Figure 2c) ne sont pas tabulées ; seules les valeurs de GLOBIOweb Table 3.1 (dérivées de Schipper 2020 et Kok et al. 2022) sont chiffrées, sans incertitude.
- Les largeurs des zones d'impact routier par biome (Alkemade 2009, Figure 4) ne sont données que graphiquement.
- GBS : les facteurs d'impact par kg de ciment, acier, verre, sable, aluminium, cuivre (Figures 14 à 16 du rapport construction 2026) ne sont pas publiés en chiffres ; les bases "GBS Impact Factors", GBStoolbox et GBSecoinvent sont sous licence. L'intensité azote globale (MSA.km²/t N-eq) n'est pas chiffrée dans la documentation publique. Aucune intensité par m² construit n'a été trouvée.
- NON VÉRIFIÉ : page non accessible pour https://www.mission-economie-biodiversite.com/en/publications (robots), https://www.sciencedirect.com/science/article/pii/S1470160X19302961 et https://doi.org/10.1016/j.ecolind.2019.04.022 (Marquardt et al. 2019 : seule la notice PBL a été lue, sans table de valeurs), https://hal.science/hal-04664805 et https://hal.inrae.fr/hal-04664805v1 (Durand et al. 2024, bloqué par anti-robot), https://conbio.onlinelibrary.wiley.com/doi/10.1111/cobi.14183 (Hawkins 2023, texte intégral non lu), https://www.researchgate.net/publication/389402099 (Kuipers 2025, non lu), https://link.springer.com/content/pdf/10.1007/s10021-009-9229-5.pdf (Springer renvoie une page HTML ; la copie unstats.un.org a servi), https://pmc.ncbi.nlm.nih.gov/articles/PMC7028079/pdf/GCB-26-760.pdf (reCAPTCHA ; la version HTML PMC et le zip Europe PMC ont servi).
- Kok et al. 2022 ("Exploring nature-positive pathways", PBL), source des valeurs agricoles de GLOBIOweb Table 3.1 : non récupéré.
- Arets, Verwer et Alkemade 2014 (source des pentes climatiques du GBS) : non récupéré, valeurs lues uniquement dans la Table 2 du document GBS.

#### Sources consultées

| Source | URL | Statut |
|---|---|---|
| Schipper et al. 2020, texte intégral (HTML PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7028079 | Lue intégralement (texte, équations, licence, Figure 2 en image) |
| Schipper et al. 2020, Supporting Information (docx, 792 lignes converties) | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7028079/supplementaryFiles | Lue intégralement |
| Schipper et al. 2020, PDF PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC7028079/pdf/GCB-26-760.pdf | Non accessible (reCAPTCHA) |
| Schipper et al. 2020, PDF Wiley | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.14848 | Non accessible (page HTML renvoyée) |
| README des données GLOBIO 4 | https://acc-dataportaal.pbl.nl/data/GLOBIO/Schipper_etal_2020/README.txt | Lue partiellement (résumé WebFetch) |
| Alkemade et al. 2009 (PDF éditeur, 17 pages, copie UNSD) | https://unstats.un.org/unsd/envaccounting/seeaRev/meeting2013/EG13-BG-5.pdf | Lue intégralement (tables 4 à 9, équations, licence) |
| Alkemade et al. 2009, Springer | https://link.springer.com/article/10.1007/s10021-009-9229-5 et /content/pdf/... | Partiellement (page HTML sans tables) ; PDF non accessible |
| Notice PBL Alkemade 2009 | https://www.pbl.nl/en/publications/globio-3-a-framework-to-investigate-options-for-reducing-global-terrestrial-biodiversity-loss | Lue (pas de PDF) |
| GLOBIO 3.5 technical model description (PBL 2369, 36 p.) | https://www.pbl.nl/downloads/pbl-publication-2369pdf | Lue intégralement |
| GLOBIOweb technical documentation (PBL, 48 p.) | https://www.globio.info/wp-content/uploads/2023/03/GlobioWeb_technical_documentation_20230219.pdf | Lue intégralement (chapitres 1 à 4 et annexes 1, 2, 5) |
| globio.info, pages What is GLOBIO, data downloads, GLOBIO 4, Global Biodiversity Score | https://www.globio.info/what-is-globio ; https://www.globio.info/globio-data-downloads ; https://www.globio.info/?p=1199 ; https://www.globio.info/global-biodiversity-score | Lues (résumés WebFetch et HTML brut pour la licence) |
| Code GLOBIO 4 (dépôt cloné) | https://github.com/GLOBIO4/GlobioModelPublic | Lue partiellement (LICENSE, Config/Globio_Config.glo, 5 scripts Calculations) |
| Wiki GLOBIO 4, pages Home et Terrestrial-module | https://github.com/GLOBIO4/GlobioModelPublic/wiki | Lues (résumés WebFetch) |
| models.pbl.nl, Terrestrial biodiversity | https://models.pbl.nl/image/Terrestrial_biodiversity/Description | Lue (résumé WebFetch) |
| GBS Review: Core concepts | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/20200518_GBS-review_Core-concepts_final-version_no-track-changes.pdf | Lue partiellement (sections 2.2 et 3.2.B, licence) |
| GBS Review: Terrestrial pressures on biodiversity | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/Terrestrial-pressures-on-biodiversity.pdf | Lue intégralement (texte converti et Table 2 en image) |
| GBS Review: Wood logs CommoTool | https://www.cdc-biodiversite.fr/wp-content/uploads/2023/01/Woodlogs-CommoTool.pdf | Lue partiellement (Table 7) |
| GBS Independent Review Report (Solinnen / OFB, 2020) | https://oai-gem.ofb.fr/exl-php/document-affiche/ofb_recherche_oai/OUVRE_DOC/62001?fic=doc00085670.pdf | Lue partiellement (sections 2.1 à 2.2, conclusions, grilles de commentaires) |
| Notice OFB du rapport Solinnen | https://www.documentation.eauetbiodiversite.fr/notice/00000000019660b568f0a929748d4112 | Lue |
| MEB Outlook n°18 (déc. 2021) | https://www.cdc-biodiversite.fr/download/global-biodiversity-score-establishing-an-ecosystem-of-stakeholders-to-measure-the-biodiversity-performance-of-human-activities/?wpdmdl=3531 | Lue partiellement (section 4.2 licence) |
| MEB Report n°49 (oct. 2023) | https://www.cdc-biodiversite.fr/wp-content/uploads/2024/01/DOSSIER-MEB-49-GBS-MD-WEB.pdf | Lue partiellement (sections 1.2 et 3.1) |
| Sectoral report Construction v2.0 (juin 2026) | https://www.cdc-biodiversite.fr/wp-content/uploads/2026/06/20260601_Sectoral-report_Construction.pdf | Lue partiellement (colophon, sections B.2, C.1, C.2, glossaire ; Figures 13 à 15 en image) |
| Executive summary Construction (juin 2026) | https://www.cdc-biodiversite.fr/wp-content/uploads/2026/06/20260601_Executive_summary_construction_sector_vf.pdf | Téléchargée, non lue en détail |
| Benchmark general appendix v2 (nov. 2025) | https://www.cdc-biodiversite.fr/wp-content/uploads/2025/11/Benchmark-general_appendix_v2.pdf | Lue partiellement (unités, seuil 72 % MSA) |
| Fiche benchmark Construction 2022 | https://www.cdc-biodiversite.fr/wp-content/uploads/2022/05/Fiche-benchmark-Secteur-Construction.pdf | Lue (résumé WebFetch) |
| Position papers MSA (CBD 2022, TNFD 2023) | https://www.cdc-biodiversite.fr/wp-content/uploads/2022/12/20221122_position-paper_MSA_CBD_v14.pdf ; https://www.cdc-biodiversite.fr/wp-content/uploads/2023/10/2023-08-31_Position-Paper-MSA-TNFD.pdf | Lues partiellement (annexe 4 du papier TNFD) |
| Pages CDC Biodiversité : GBS, documentation, revue critique, études sectorielles, études de cas, prises de position, construction, changelog | https://www.cdc-biodiversite.fr/le-global-biodiversity-score/ ; .../documentation-gbs/ ; .../documentation-global-biodiversity-score-revue-critique/ ; .../documentation-global-biodiversity-score-etudes-sectorielles/ ; .../documentation-global-biodiversity-score-etudes-de-cas/ ; .../documentation-global-biodiversity-score-prises-de-position/ ; .../documentation-global-biodiversity-score-etudes-sectorielles-construction/ ; .../simplified-changelog-gbs/ | Lues (résumés WebFetch) |
| Hub Notion GBS (hub, Library, FAQ, MSA land use layer) | https://cdc-biodiversite.notion.site/GBS-Documentation-27f15ff341c480e8a12efcf55a4779cd ; https://cdc-biodiversite.notion.site/MSA-land-use-layer-12715ff341c480659666e0e70b83bbc1 | Lues intégralement via l'API publique Notion (53 entrées de la bibliothèque, table complète de la couche MSA) |
| mission-economie-biodiversite.com | https://www.mission-economie-biodiversite.com/en/publications | Non accessible (robots / connexion réinitialisée) |
| Marques et al. 2021, IJLCA (PDF IIASA) | https://pure.iiasa.ac.at/16985/1/Marques2021_Article_AResearchPerspectiveTowardsAMo.pdf | Lue partiellement (section sur LBII/MSA/BHI, licence) |
| Durand et al. 2026, Conservation Biology (manuscrit accepté, ORA Oxford) | https://ora.ox.ac.uk/objects/uuid:e9da8351-1040-471f-9089-1646e2196314 (fichier spr76f5881) | Lue partiellement (notice et passages sur GLOBIO/MSA) |
| Hawkins et al. 2023 (notice CIFOR-ICRAF) | https://www.cifor-icraf.org/knowledge/publication/35500/ | Lue (résumé) ; texte Wiley non accessible |
| Kuipers et al. 2025 (notice globio.info) | https://www.globio.info/relationship_msa_pdf | Lue (résumé) ; ScienceDirect et ResearchGate non accessibles |
| Stimpson, Bull, Milner-Gulland 2025 (préprint EcoEvoRxiv, DOI 10.32942/X2GD37) | https://ecoevorxiv.org/repository/view/11181/ | Lue (résumé) |
| Faith, Ferrier, Williams 2008 (notice Australian Museum) | https://publications.australian.museum/2008-getting-biodiversity-intactness-indices-right-ensuring-that-biodiversity-reflects-diversity | Lue (résumé) |
| Marquardt et al. 2019 (notice PBL) et Marquardt et al. 2021 (edepot WUR) | https://pbl.nl/en/publications/consumption-based-biodiversity-footprints ; https://edepot.wur.nl/549490 | Lues (résumés) ; ScienceDirect non accessible |
| Plumptre et al. 2022, Frontiers (vérifiée : sans MSA) | https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2022.880353/pdf | Lue (résumé) |
| Partridge et Clark 2022, Frontiers (vérifiée : sans MSA) | https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.779005/full | Lue (résumé) |
| CE Delft 2011, Biodiversity and Land Use, annexes | https://ce.nl/wp-content/uploads/2021/03/8250_finalreport_AnnexesHCEV.pdf | Lue partiellement (annexe A, sans valeur urbaine fine) |
| Notice GLOBIO 3.5 (PBL) | https://www.pbl.nl/en/publications/globio-35-technical-model-description | Lue |

### 2.4 ACV et occupation des sols : LC-IMPACT, Chaudhary 2015, ReCiPe 2016, EF 3.1 (LANCA), EN 15804+A2 et INIES, Koellner 2013, Carbone 4

Date de consultation de toutes les sources : 17/10/2026. Règle appliquée : aucune valeur de mémoire ; chaque nombre ci-dessous a été lu dans une page ou un fichier récupéré (téléchargement direct du fichier source, puis lecture du PDF, du XLSX ou du XML). Les valeurs sont reproduites telles qu'écrites dans la source (point décimal, notation E).

Avertissement sur Carbone 4 : la publication « La biodiversité grise dans le bâtiment » n'est ni de 2022 ni de 2023 : la page officielle est datée du 6 octobre 2026 et le PDF (fourni par Cédric le 17/10/2026) est daté du 7 octobre 2026 dans ses métadonnées (voir Valeurs). Le programme de 2021 associant Altarea et Nexity est un autre dispositif (BIG, piloté par l'OID, sans Carbone 4).

#### Objet

Recenser, à la source, les référentiels de caractérisation « usage des sols » utilisables pour chiffrer l'impact biodiversité des matériaux de construction (occupation en m²·an et transformation en m²), leurs unités, licences, formats et valeurs, ainsi que les études chiffrant la biodiversité grise des bâtiments, en vue d'un module par lot de matériaux RE2020 (lots 1 à 13 du contributeur « composants »).

Sources auditées : LC-IMPACT (v1.3 et v2.0), Chaudhary et al. 2015, ReCiPe 2016, Environmental Footprint 3.1 (LANCA / SQP), EN 15804+A2 via la RE2020 et la base INIES, Koellner et al. 2013, Carbone 4 2026, et 6 autres études (Montilla Moreno et al. 2026, Christiansson et Roos 2023, One Click LCA / G-ON 2026, Scherer et al. 2023, Expedition Engineering 2023, Ramboll 2026).

#### Accès et licence (URL exactes, consultées le 17/10/2026)

| Source | URL | Format | Licence (texte lu) |
|---|---|---|---|
| LC-IMPACT, article cadre (Verones et al. 2020, J. Ind. Ecol. 24(6) 1201-1219, DOI 10.1111/jiec.13018) | https://lc-impact.eu/doc/Verones_etal_2020_LC-IMPACT.pdf (PDF 19 p.) ; https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13018 | PDF | « This is an open access article under the terms of the Creative Commons Attribution License » (p. 1) |
| LC-IMPACT v1.3, données | https://doi.org/10.5281/zenodo.6200606 (record « LC-IMPACT1.3 », 1 fichier LC-Impact-v-1-3.zip, 4,5 Go, publié le 18 août 2021) | ZIP | « Creative Commons Attribution 4.0 International » (page Zenodo). Fichier NON TÉLÉCHARGÉ (4,5 Go) : valeurs v1.3 non vérifiées |
| LC-IMPACT v2.0, données | https://zenodo.org/records/18670560 (DOI 10.5281/zenodo.18670560, version 2.0, publiée le 17 février 2026, 322,3 Mo ; fichier 6_CF_LAND_USE.zip 4,7 Mo ; fichier 14_CF_LAND_USE_MSA.zip 366,4 ko) ; pages https://lc-impact.eu/index_v2.html, https://lc-impact.eu/EQland_stress_v2.html, https://lc-impact.eu/EQLand_MSA_v2.html | ZIP contenant PDF (chapitre 6, 14 p.) + XLSX « EQ_LandUse_gloPDF_Country_Aggregated_2025-12-17.xlsx » (feuilles Country 59 455 lignes x 23 colonnes, Exio 11 285 lignes) | « Creative Commons Attribution 4.0 International » (page Zenodo). Les fichiers SI_ « are for research purposes only » |
| Chaudhary, Verones, de Baan, Hellweg 2015, ES&T 49(16) 9987-9995, DOI 10.1021/acs.est.5b02507 | https://pubs.acs.org/doi/10.1021/acs.est.5b02507 (NON ACCESSIBLE) ; métadonnées et résumé lus via https://api.crossref.org/works/10.1021/acs.est.5b02507 | HTML | ACS AuthorChoice (version of record, 2015-08-21). Supporting Information : NON VÉRIFIÉ |
| Scherer et al. 2023 (GLAM, base de LC-IMPACT v2), ES&T 57(48) 19612-19623, DOI 10.1021/acs.est.3c04191 | https://zenodo.org/records/10114493 (DOI 10.5281/zenodo.10114493, v1.0.0, 11 novembre 2023, 34,2 Mo : CF.csv 14,0 Mo, CF_country.csv 4,7 Mo, CF_global.csv 68,9 ko) ; https://research-collection.ethz.ch/handle/20.500.11850/643067 | CSV + TIF | « Creative Commons Attribution 4.0 International » (Zenodo) |
| ReCiPe 2016 v1.1, rapport RIVM 2016-0104 (Huijbregts et al.) | https://www.rivm.nl/sites/default/files/2018-11/Report%20ReCiPe_Update_20171002_0.pdf (PDF 201 p.) ; page https://www.rivm.nl/en/life-cycle-assessment-lca/downloads | PDF | « © RIVM 2017. Parts of this publication may be reproduced, provided acknowledgement is given to: National Institute for Public Health and the Environment, along with the title and year of publication. » (p. 2) |
| ReCiPe 2016 v1.1, facteurs (tableur) | https://www.rivm.nl/sites/default/files/2024-10/ReCiPe2016_CFs_v1.1_20180117.xlsx | XLSX, 21 feuilles dont « Land transformation » et « Land occupation » ; version 2017-05-01, mises à jour mars 2017, juillet 2017 (v1.1), janvier 2018 | Aucune mention de licence dans le fichier |
| EF 3.1 (JRC), paquet de référence | https://knowledge-for-policy.ec.europa.eu/sites/default/files/EF-v3.1_2.zip (197,33 Mo), page https://knowledge-for-policy.ec.europa.eu/european-platform-life-cycle-assessment-eplca/life-cycle-data-network-lcdn/reference-package_en (« Last Updated: 26 Nov 2025 / 22 Sep 2026 ») | ZIP au format ILCD ; fichier « Land use » = ILCD/lciamethods/b2ad6890-c78d-11e6-9d9d-cec0c932ce01.xml (36 423 facteurs, 213 localisations) ; Normalisation_Weighting_Factors_EF_3.1.xlsx | Texte lu dans le XML : « The data set can be used free of charge by anybody to perform LCA studies, to distribute it to third parties, to convert it to other formats, to develop own data sets etc. as long as the ILCD format is mantained. Please note e.g. that reference must be given to the 'Owner of data set'... » |
| De Laurentiis et al. 2019, « Soil quality index », J. Clean. Prod. 215, 63-74, DOI 10.1016/j.jclepro.2018.12.238 | Texte intégral lu via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6472660/fullTextXML | XML | « This is an open access article under the CC BY license » |
| RE2020, arrêté du 4 août 2021 | Texte consolidé lu via le docx de la notification TRIS 2020/0791/F : https://technical-regulation-information-system.ec.europa.eu/et/notification/23190/text/F/FR ; page Legifrance https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043936431 NON ACCESSIBLE (protection Cloudflare) ; page portail https://rt-re-batiment.developpement-durable.gouv.fr/textes-exigences-et-methode-a703.html | DOCX / HTML | Portail : « Sauf mention contraire, tous les contenus de ce site sont sous licence etalab-2.0 » |
| RE2020, annexe II consolidée (méthode) | https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/annexeii_arrete_4_aout_2021.pdf (PDF 101 p., créé le 16 juin 2026, intégrant les arrêtés du 6 avril 2022, du 22 décembre 2022 et du 19 mars 2026) | PDF | Licence etalab-2.0 (mention du portail) |
| INIES (programme et base) | https://www.inies.fr/ ; https://www.inies.fr/contenu-de-la-base/fdes-produits-de-construction/ ; https://www.inies.fr/le-webservice/demander-un-acces/ ; CGU webservice https://www.inies.fr/wp-content/uploads/2026/06/Conditions_Generales_Utilisation_Webservice-INIES_juillet_2026.pdf (8 p., « Version du 17/07/2026 ») ; bon de commande https://www.inies.fr/wp-content/uploads/2026/06/Bon-de-commande-INIES-2026-OK.pdf (3 p.) ; tarifs dépôt https://inies.fr/wp-content/uploads/2024/12/Reglement_programme_INIES_Annexe_A_Conditions_tarifaires_2024_12_FR.pdf ; chiffres clés https://inies.fr/wp-content/uploads/2025/02/chiffres-cles-INIES-2024.pdf ; doc API https://base-inies.fr/swagger/index.html et https://base-inies.fr/docs/ | HTML / PDF | Consultation : « Les données d'INIES sont consultables publiquement et gratuitement sur le site de consultation de la base INIES. » Données numérisées : accès payant au webservice (licence commerciale annuelle de 2 800 € HT). Détails plus bas |
| Koellner et al. 2013, Int J LCA 18:1188-1202, DOI 10.1007/s11367-013-0579-z | https://publications.polymtl.ca/4975/1/2013_Koellner_Unep-Setac_guideline_global_land_use.pdf (PDF 15 p.) | PDF | « Open Access This article is distributed under the terms of the Creative Commons Attribution License » |
| Carbone 4, « La biodiversité grise dans le bâtiment : comment estimer l'impact des matériaux de construction sur la nature ? » (position paper, 30 p.) | https://carbone4.com/fr/publications/la-biodiversite-grise-dans-le-batiment-comment-estimer-l-impact-des-materiaux-de-construction-sur-la-nature (page lue intégralement) ; PDF derrière un formulaire HubSpot, fourni par Cédric le 17/10/2026 et lu intégralement (copie dans `sources/acv/carbone4/`) | HTML + PDF | Aucune mention de licence ni de copyright, ni sur la page ni dans le PDF ; « Étude financée par Altarea et Nexity » |
| Montilla Moreno et al. 2026, Int J LCA 31, art. 118, DOI 10.1007/s11367-026-02688-z | https://link.springer.com/article/10.1007/s11367-026-02688-z ; licence confirmée via https://api.crossref.org/works/10.1007/s11367-026-02688-z | HTML | CC BY 4.0 |
| Christiansson et Roos 2023, Chalmers, rapport E2023:079 | https://odr.chalmers.se/items/31799976-4273-4235-9bd8-5e7148c17746/full ; PDF https://odr.chalmers.se/bitstreams/59a8a732-cf1b-4cc7-890a-8a94c53054b6/download (61 p.) | PDF | Aucune licence lue dans le PDF |
| One Click LCA / G-ON, étude de cas | https://oneclicklca.com/en/resources/case-studies/biodiversity-in-construction-lifecycle-assessment (publiée « Jul 16 2026 ») | HTML | Site commercial |
| Expedition Engineering 2023, « The Embodied Biodiversity Impacts of Construction Materials » | https://expedition.uk.com/wp-content/uploads/2023/11/231103_Embodied-Biodiversity_Report_Compressed.pdf (novembre 2023, « DRAFT 2.0 ») | PDF | Non lue |
| Ramboll 2026, « Beyond net zero: practical ways to measure nature impact » (17 février 2026) | https://www.ramboll.com/en-gb/insights/decarbonise-for-net-zero/beyond-net-zero-practical-ways-to-measure-nature-impact | HTML | Non lue |
| LPO / Club U2B, fiche « Du concept à la mise en oeuvre : la Biodiversité grise » (atelier du 18 novembre 2015, PDF créé le 9 mars 2016) | https://www.effinergie.org/web/images/attach/base_doc/2998/fichebiodiversitegrise.pdf (4 p.) | PDF | Aucune licence lue |

#### Principes (formules, unités, conversions)

Cadre UNEP-SETAC (Koellner et al. 2013, lu p. 1189-1197) :
- Impact de transformation : « TI = 0.5 × ΔQ × treg × A » (Eq. 1, p. 1189), treg = temps de régénération complète, trajectoire de régénération supposée linéaire. Facteur : « CFtrans = 0.5 × ΔQ × treg » (Eq. 2, p. 1190).
- Impact d'occupation : « OI = ΔQ × T × A » (Eq. 3, p. 1190), ΔQ supposé constant pendant l'occupation ; « CFocc = ΔQ » (Eq. 4). ΔQ = Qref - QLU ; valeur négative = bénéfice.
- Inventaire : « Land use inventory flow for land occupation and land transformation are measured in m2years and in m2, respectively. » (p. 1196, 3.2.1).
- Situation de référence (3.1.4, p. 1196) : option 1 végétation naturelle potentielle (PNV), option 2 couvert (quasi-)naturel du biome / de l'écorégion, option 3 mix actuel d'usages. Recommandation : couvert (quasi-)naturel prédominant des biomes et écorégions. Le choix de référence est « a value choice ».
- Temps de régénération (3.2.2, p. 1196-1197) : aucun tableau de valeurs ; indications lues : tourbières et forêts anciennes « up to 1,000 years for complete regeneration in the temperate zone » ; forêts tropicales « 100-300 years if species richness is taken as an indicator » ; le temps augmente vers les pôles et avec l'altitude ; il faut plus de temps pour régénérer une forêt si la transformation a abouti à un sol imperméabilisé qu'à une culture. Résultats « very sensitive to regeneration time » : analyse de sensibilité recommandée.
- Allocation des impacts de transformation (3.2.4, p. 1197) : « we suggest using 20 years as an allocation period », « the actual number of years is arbitrary in any case ».

ReCiPe 2016 (RIVM 2016-0104, chapitre 12 p. 89-94, SI S8 p. 189-192) :
- Midpoint : « occupation and time-integrated transformation », unité « m2·yr », facteur CFm en « m2 yr annual crop land », nom « agricultural land occupation potential (LOP) ».
- Srel = 1 - SLU/Sref (Eq. 2, p. 91) ; CFmocc,x = Srel,x / Srel,annual crops ; CFmrelax = CFmocc × 0.5 × trel (p. 91). Référence = PNV approchée par les habitats (semi-)naturels de la même écorégion ou du même biome (12.3.2, p. 92).
- Temps de récupération (p. 91, d'après Curran et al. 2014) : biomes forestiers « median of 73.5 years (range 46.7-138.8) », biomes ouverts « 7.5 years (range 4.7-14) » ; moyenne mondiale pondérée (40 % forêt, 60 % ouvert) « trel is calculated to be 33.9 years ». Restauration active : récupération accélérée « by approximately 80% » (12.3.4, p. 93).
- Endpoint : FM->E,LU = SDterr × Srel,annual crop avec « SDterr ... approximated to be 1.48·10-8 species/m2 » et « Srel,annual crop ... 0.60 » (p. 93) ; Table 12.2 (p. 94) : « 8.88E-09 » species/m2 annual crop eq.
- Périmètre : « The local impact of land use is covered only » ; « the impact of land transformation from one anthropogenic land use to another is not covered » (p. 89) ; reptiles et amphibiens « not included at all » (p. 93).

LC-IMPACT v1.3 (Verones et al. 2020 ; page https://lc-impact.eu/EQland_stress.html) :
- Approche Chaudhary et al. (2015), countryside SAR, « five taxa (mammals, birds, reptiles, amphibians, and vascular plants) and six land use types (annual crops, permanent crops, pastures, urban, extensive forestry and intensive forestry) », « 804 ecoregions ».
- Formule : S_lost = S_org - S_org × ((A_new + Σ h_g,i,j × A_i,j) / A_org)^z_j ; CF_occ,g,i,j = S_lost,g,j × a_i,j / A_i,j ; CF_trans = 0.5 × CF_occ × t_reg ; CF_weighted = CF_unweighted × VS_g,j avec « vulnerability score (0<VS<1) ». Unités : « species eq. lost/m2 » (occupation) et « species eq. lost · years/m2 » (transformation). « PDF/m2 for land occupation » multiplié par « m2·yr » donne « PDF·yr » (section 2.5, p. 6).
- Deux jeux : CF marginaux et CF moyens (Table 2, p. 5). Transformation : « total recovery times (up to 1,200 years, depending on ecosystem) » ou « 100 years » (Table 3). Valeurs numériques : aucune dans l'article ; z et VS par écorégion : NON VÉRIFIÉS.

LC-IMPACT v2.0 (chapitre 6 « Land use », Dorber, Kavak Gulbeyaz, Verones, PDF daté du 17 décembre 2025, 14 p., lu intégralement) :
- Base : Scherer et al. (2023). « Characterization factors for land occupation are expressed in PDF/m² and transformation characterization factors (CFs) are expressed in PDF·yr/m² » (p. 1). 5 usages (cropland, pasture, plantation, managed forest, urban land) x 3 intensités (minimal, light, intense) x 5 groupes taxonomiques (p. 2).
- Relation espèces-habitat (SHR, Kuipers et al. 2021) avec aire connectée équivalente (ECA) : « PDF_g,j,reg = RSL = 1 - H_g,j,1 / H_g,j,0 » (Eq. 1, p. 5) ; z spécifique au biome (Gerstner et al. pour les plantes, Storch et al. pour les vertébrés ; valeurs non reproduites dans le chapitre).
- Référence : « hypothetical biotic potential ... fully natural state » ; état actuel = usage des sols 2015 (HILDA+) (p. 2 et 6).
- CF moyen d'occupation : « CF = RSL × A_lu^-1 × a » (Eq. 6, p. 7) ; transformation : « CF_tra = CF_occ × 0.5 × t » (Eq. 7, p. 8), t d'après Curran et al. ; « For land transformation the time horizons is defined by t and varies per ecoregion and taxonomic group between 80 and 1186 years » (1.4.1, p. 13).
- Passage régional vers global : multiplication par le GEP (global extinction probability) (p. 8). Agrégation pays = moyenne pondérée par la surface des écorégions (Eq. 8).
- Flux « transformation, from / to » : logique ReCiPe 2016 adoptée : « CF_trans from,i = CF_occ,max × 0.5 × t_i » (Eq. 11-12), « to » = « from » x -1 ; occupation des types naturels fixée à 0 (p. 11-12).

EF 3.1 / LANCA / SQP :
- Métadonnées lues dans le XML EF 3.1 « Land use » : indicateur « Soil quality index » ; « CFs set was re-Calculated by JRC starting from LANCA® v 2.2 as baseline model. Out of 5 original indicator only 4 have been included in the aggregation » ; unité « dimensionless (pt) » ; « Environmental impacts on ecosystem services derived from land use » ; « Assignation of a soil quality score taking into account erosion potential, mechanical filtration, groundwater replenishment and biotic production » ; année de référence 2017.
- De Laurentiis et al. 2019 (texte intégral) : LANCA évalue 5 fonctions du sol (biotic production, groundwater recharge, erosion resistance, mechanical filtration, physiochemical filtration) ; re-scaling « CF'_i,j = CF_i,j / CF_i^95 × 100 [Pt/m2a] » (Eq. 6, 95e percentile) ; agrégation linéaire sur 4 indicateurs ; CF d'occupation mondiaux « ranged from -17 to 165 » et nationaux « from -47 and 318 ». Transformation : « assuming a regeneration time of 20 years for biotic land uses and of 85 years for artificial land use types (sealed land) » ; « CF_transf,to = CF_occ × 0.5 × T_reg [Pt/m2] ».
- Normalisation et pondération EF 3.1 : NF « Land use » = « 819498.1829230306 pt/person » ; WF « Land use » = 0.0794 (7,94 %).

EN 15804+A2 tel que repris par la RE2020 :
- Annexe II de l'arrêté du 4 août 2021, Tableau 12 « Liste des indicateurs environnementaux calculés sur la base de l'analyse du cycle de vie » (p. 100-101 du PDF consolidé) : « Indice potentiel de qualité des sols (SQP) | SQP | sans unité » et « Emissions de gaz à effet de serre - occupation des sols et transformation de l'occupation des sols | GES - luluc | kg éq. CO2 ». Aucune mention de « biodiversité » dans l'annexe II (0 occurrence).
- Le texte de la norme NF EN 15804+A2 et de son complément national : NON VÉRIFIÉ (norme payante, non consultée).

Unités et conversions (uniquement ce qui a été lu) :

| Unité | Définition lue | Conversion lue |
|---|---|---|
| m²a crop eq (ReCiPe midpoint) | « annual crop equivalents » : Srel,x / Srel,annual crops (p. 91) | vers species·yr : x 8.88E-09 species/(m²·annual crop eq) (Table 12.2 p. 94) ; le facteur vaut SDterr 1.48E-8 species/m² x Srel 0.60 (p. 93) |
| PDF (ReCiPe) | « Potentially Disappeared Fraction of Species (PDF) per annual crop equivalent » (p. 90) ; PDF local = Srel | PDF x SDterr = species/m² (p. 93) |
| PDF régional vs PDF global (LC-IMPACT v2) | régional = « reversible losses », global = « irreversible losses » (p. 3) | global = régional x GEP (p. 8) ; valeurs GEP dans 2_GEP.zip (non lu) |
| PDF·yr (LC-IMPACT) | CF en PDF/m² x m²·yr = PDF·yr (Verones 2020, p. 6) | vers species·yr : conversion signalée incomplète par Montilla Moreno et al. 2026 |
| PDF.m².yr (Carbone 4 via IMPACT World+, One Click LCA) | Carbone 4, note 5 : « métrique d'impact biodiversité quantifiant la fraction potentiellement disparue d'espèces végétales et animales sur une surface donnée (1m2) pendant une période d'un an » ; équivalence employée par Carbone 4 : 272 000 PDF.m².yr « correspondant à 12 500 m² de déforestation équivalente » (p. 15), soit, par calcul propre, 21,8 PDF.m².yr par m² déforesté, non explicitée dans le document | aucune conversion vers MSA ou species·yr lue |
| MSA-loss·km²·km⁻² (LC-IMPACT v2 chapitre 14, GLOBIO 4.3.1) | « area-integrated loss of mean species abundance (MSA) per km² of land use » ; « universal MSA impact relationships ... a loss in MSA due to a given pressure is the same everywhere » | aucune conversion MSA vers PDF lue ; les 2 métriques coexistent séparément dans LC-IMPACT v2 |
| Pt (EF 3.1, SQP) | « dimensionless (pt) » | normalisation EF : 819 498.18 pt/personne ; pondération 7,94 % ; aucune conversion vers PDF ou species.yr (indicateur de services écosystémiques du sol, pas de biodiversité) |

#### Valeurs disponibles

ReCiPe 2016 v1.1, Table 12.1 (p. 92), « Midpoint CFs for the impact of land transformation/occupation (CFmocc) and land relaxation (CFmrelax) on total species richness » :

| Type d'usage | CFmocc (annual crop eq) | CFmrelax (annual crop eq·yr) |
|---|---|---|
| Used forest | 0.30 | 5.1 |
| Pasture and meadow | 0.55 | 9.3 |
| Annual crops | 1.00 | 17.0 |
| Permanent crops | 0.70 | 11.9 |
| Mosaic agriculture | 0.33 | 5.6 |
| Artificial areas (note 1 : « urban areas, industrial areas, road and rail networks, dump sites ») | 0.73 | 12.4 |

Table S8.2 (p. 191), Srel moyennes mondiales (De Baan et al. 2013) : pasture and meadow 0.33 ; annual crops 0.60 ; permanent crops 0.42 ; mosaic agriculture 0.2 ; artificial areas 0.44.

Table S8.3 (p. 191), « Endpoint CFs ... on total species richness » : Used forest 2.66E-09 species/m² et 4.52E-08 species·yr/m² ; Pasture and meadow 4.88E-09 et 1.51E-07 ; Annual crops 8.88E-09 et 8.28E-08 ; Permanent crops 6.22E-09 et 1.05E-07 ; Mosaic agriculture 2.93E-09 et 4.97E-08 ; Artificial areas 6.48E-09 et 1.10E-07.

Table S8.4 (p. 192), « Midpoint CFs for transformation of natural land » (annual crop eq·yr ; CF = 1 annual crop eq x 0.5 x Trec, avec 73.5 ans forêt et 7.5 ans milieux ouverts) : from grassland, natural 3.75 ; from forest, primary 36.75 ; from forest, secondary 36.75 ; from shrub land, sclerophyllous 3.75 ; from wetland, inland 3.75 ; to shrub land, sclerophyllous -3.75.

Tableur, feuille « Land occupation » (correspondance flux ecoinvent vers classe ReCiPe) : « Occupation, mineral extraction site » vers artificial area 0.73 ; « industrial area » 0.73 ; « construction site » 0.73 ; « traffic area, road network » 0.73 ; « dump site » 0.73 ; « urban, discontinuously built » 0.73 ; « annual crop, greenhouse » 0.73 ; « forest, extensive » et « forest, intensive » vers managed forest 0.3 ; « shrub land, sclerophyllous » 0.3 ; « pasture, man made » 0.55 ; « permanent crop » 0.7 ; « annual crop » 1 ; « grassland, natural (non-use) », « river, artificial », « lake, artificial » 0. Pas de valeur nationale (France) : « Characterization factors were based on global scale data » (Table 1.1 p. 18).

Table S8.1 (p. 189-190) : pour « Artificial areas » seul vascular plants est renseigné (-0.70, c'est à dire un gain) ; trel par groupe (forest/open) : mammals 69.4/7.2 ; birds 68.6/6.3 ; insects 69.2/7.0 ; invertebrates 79.5/8.0 ; plants 73.5/7.3 ; trees 102.2/10.4.

LC-IMPACT v2.0, France (fichier EQ_LandUse_gloPDF_Country_Aggregated_2025-12-17.xlsx, feuille « Country », lignes LCIAMethod_location = « FRA », Species = « Aggregated », 242 lignes, 121 flux ; fichier 6_CF_LAND_USE.zip du record https://zenodo.org/records/18670560) :

Occupation, unité « Global PDF/m2 » :

| Flux (FLOW_name) | Average | Marginal |
|---|---|---|
| urban ; urban, continuously built ; industrial area ; mineral extraction site ; construction site ; dump site ; traffic area ; traffic area, road network ; artificial areas ; unspecified | 6.089e-14 | 7.745e-14 |
| urban, discontinuously built | 1.017e-14 | 1.659e-14 |
| urban, green areas | 5.798e-15 | 1.099e-14 |
| arable (toutes variantes, dont non-irrigated, intensive) ; permanent crops | 2.121e-14 | 3.577e-14 |
| pasture/meadow (dont intensive) | 1.583e-14 | 2.603e-14 |
| forest ; forest, intensive ; forest, used | 1.397e-14 | 2.233e-14 |
| forest, extensive | 6.894e-15 | 1.09e-14 |
| Plantation_forest_Intense ; Plantation_forest_Light | 4.804e-14 | 7.137e-14 |
| Plantation_forest_Minimal | 2.471e-14 | 3.8e-14 |
| forest, natural ; forest, primary ; forest, secondary ; grassland ; shrub land ; unspecified, natural | 0 | 0 |

Transformation, unité « Global PDF*y/m2 » :

| Flux | Scénario | Average | Marginal |
|---|---|---|---|
| transformation from reference state to urban / industrial area / mineral extraction site | long flow name | 7.506e-12 | 1.152e-11 |
| transformation from reference state to arable | long flow name | 4.32e-12 | 8.301e-12 |
| transformation from reference state to pasture/meadow | long flow name | 3.524e-12 | 6.449e-12 |
| transformation from reference state to forest, intensive | long flow name | 2.816e-12 | 5.126e-12 |
| transformation from reference state to Plantation_forest_Intense | long flow name | 7.499e-12 | 1.261e-11 |
| from forest, natural ; from grassland ; from shrub land ; from unspecified, natural | ReCiPe2016 logic | 4.99e-12 | 9.286e-12 |
| to grassland ; to forest, secondary | ReCiPe2016 logic | -4.99e-12 | -9.286e-12 |

Comparaison lue dans le même fichier, flux « urban », occupation, Average / Marginal (Global PDF/m2) : Belgium 4.349e-17 / 1.324e-16 ; Germany 5.807e-16 / 1.441e-15 ; Poland 2.624e-16 / 6.116e-16 ; Sweden 3.757e-16 / 4.812e-16 ; Finland 4.426e-17 / 5.659e-17 ; Italy 2.149e-14 / 5.224e-14 ; Spain 4.811e-14 / 8.271e-14 ; Turkey 1.981e-14 / 4.432e-14 ; Morocco 4.163e-15 / 1.017e-14 ; United States 5.744e-13 / 8.159e-13 ; China 2.14e-13 / 6.023e-12 ; Indonesia 7.872e-13 / 1.107e-12 ; Brazil 2.485e-12 / 3.94e-11. Ligne « GLO » : Average 6.1575e-15 (original_weighting_land_use), 3.2935e-15 (original_weighting_ecoregion_area), 2.0969e-14 (proxy_weighting_ecoregion_area) ; Marginal 1.4434e-14, 7.6589e-15, 1.0893e-13. Observation factuelle : la valeur France « urban » est environ 100 fois celle de l'Allemagne et environ 10 fois la moyenne mondiale (pondération usage des sols).

LC-IMPACT v2.0, chapitre 14 « Land use (MSA) » (Marques et Schipper, PBL ; fichier LC-IMPACT_EQ_land_use_GLOBIO.xlsx, feuille LCIAMethod_CF_LU_GLOBIO_ISO3, lignes FRA ; unité « MSAloss*km^2/km^2 ») : Cropland 0.613 (habitat loss) + 0.0132 (fragmentation) = 0.626 ; Pasture 0.572 + 0.0132 = 0.586 ; Plantation forest 0.462 ; Urban land 0.703 + 0.0132 = 0.716 ; Mines 0.929 + 0.559 (disturbance) = 1.49. Occupation seulement. Anomalie relevée dans la feuille EXIOBASE (FR) : la ligne totale « Urban land » vaut 0.0131510340179217 au lieu de 0.716 (incohérence du fichier, à signaler avant usage).

EF 3.1 « Land use » (fichier b2ad6890-c78d-11e6-9d9d-cec0c932ce01.xml ; occupation en Pt par m²·a, transformation en Pt par m²) :

| Flux | GLO occupation | FR occupation | GLO « to » (transformation) | FR « to » |
|---|---|---|---|---|
| urban | 139.88 | 250.49 | 5945 | 10646 |
| urban, continuously built | 165.22 | - | 7021.9 | - |
| urban, discontinuously built | 116.16 | - | 4937 | - |
| industrial area | 139.1 | 249.95 | 5911.8 | - |
| mineral extraction site | 110.79 | 204.88 | 4708.4 | 8707.3 |
| construction site | 110.79 | - | 4708.4 | - |
| traffic area, road network | 161.52 | - | 6864.8 | - |
| artificial areas | 139.27 | - | 5919.2 | - |
| arable | 50.191 | 87.631 | 501.91 | - |
| pasture/meadow | 54.923 | 105.45 | 549.23 | - |
| permanent crops | 50.191 | - | 501.91 | - |
| forest, intensive (= forest, used) | 33.964 | 77.936 | 339.64 | - |
| forest, extensive | 18.128 | 47.383 | 181.28 | - |
| forest, natural / primary | 11.459 | - | 114.59 | - |
| grassland | 35.641 | - | 356.41 | - |
| wetlands | -17.458 | - | -174.58 | - |
| unspecified | 69.262 | - | 2943.6 | - |

Flux « from X » = -« to X ». Cohérence vérifiée avec De Laurentiis 2019 : 139.88 x 0.5 x 85 = 5944.9 (urbain, 85 ans) ; 50.191 x 0.5 x 20 = 501.91 (arable, 20 ans).

EN 15804+A2, FDES et base INIES :
- Chiffres clés INIES au 31/12/2024 (PDF) : « 4560 FDES VÉRIFIÉES », « 1342 PEP VÉRIFIÉS », « 1691 DONNÉES ENVIRONNEMENTALES PAR DÉFAUT (DED) », « 105 DONNÉES CONVENTIONNELLES DE SERVICE (DES) » ; « les FDES doivent être conformes à la norme NF EN15804+A2 et au complément national NF EN15804+A2/CN ». Page d'accueil (17/10/2026) : 5 661 FDES, 1 888 PEP, 345 589 références commerciales.
- Structure d'une FDES (page INIES) : caractéristiques du produit, unité fonctionnelle et durée de vie, profil environnemental, informations santé et confort, identité du déclarant ; validité 5 ans ; vérification tierce partie obligatoire depuis le 1er juillet 2017 ; 4 types (individuelle, individuelle de gamme, collective, paramétrée). Les pages INIES lues ne citent ni « SQP » ni « occupation des sols » ; la présence effective du SQP dans chaque FDES n'a pas été vérifiée sur un exemplaire (aucune FDES téléchargée).
- Accès et licence : consultation « publiquement et gratuitement » ; webservice payant : CGU « Version du 17/07/2026 », 3 licences : commerciale, académique, découverte (2 mois). Bon de commande 2026 : frais de création de dossier 400,00 € HT ; part fixe commerciale 12 mois 2 800,00 € HT ; part variable 20,00 € HT « par Utilisateur Autorisé commercial » plafonnée à 600 utilisateurs ; option « Pack de données archivées » 2 800,00 € HT ; académique 500,00 € HT ; découverte 400,00 € HT. Usages exclusifs : ACV, bilans GES des organisations, MFA, information d'existence d'une déclaration. Interdiction expresse : « Toute utilisation du webservice, ainsi que des données qui en sont issues, pour la réalisation de classements, notations, scorings, étiquettes ou tout dispositif assimilé portant sur les Déclarations Environnementales est strictement interdite. » ; « toute extraction ou réutilisation ... interdites, sauf accord préalable et écrit du Propriétaire-gestionnaire » ; sous-licence interdite. Instruction des demandes en 2 sessions (dépôt avant le 15 mai, service en juillet ; avant le 15 novembre, service en janvier).
- Dépôt d'une FDES (annexe A, décembre 2024) : jeton F1 220 € HT (1 à 19 jetons) ou 190 € HT (20 et plus) ; jeton F2 1 100 € HT ; abonnement F3 3 200 € HT/an ; F4 1 000 € HT/an ; lien configurateur 2 000 € HT.
- Cadre réglementaire des FDES (page INIES) : décret n° 2021-1674 du 16 décembre 2021, arrêté du 14 décembre 2021, arrêté du 20 octobre 2022.

RE2020 : contributeur « composants », lots 1 à 13. Source : arrêté du 4 août 2021 (texte lu dans le docx TRIS) ; article 8 : « La méthode de calcul jointe aux annexes II à IV du présent arrêté, et prévue à l'article R. 172-6 du code de la construction et de l'habitation, est approuvée. » Annexe II consolidée, 2.3.2 (p. 23) : « Pour le calcul de la contribution composants, les produits et équipements doivent être affectés à un ou plusieurs lots et sous-lots. Voir Tableau 5 et Tableau 6 ». Tableau 5 « Description de la composition physique du bâtiment en lots et sous lots » (p. 23 à 30) :

| Lot | Intitulé (annexe II) | Sous-lots lus |
|---|---|---|
| 1 | VRD (Voirie et Réseaux Divers) | 1.1 Réseaux ; 1.2 Stockage ; 1.3 Aires |
| 2 | Fondations et infrastructure | 2.1 Fondations ; 2.2 Murs ; 2.3 Parcs |
| 3 | Superstructure - Maçonnerie | 3.1 à 3.8 (éléments horizontaux, porteurs, escaliers, isolants/rupteurs, maçonneries) |
| 4 | Couverture - Etanchéité - Charpente - Zinguerie | 4.1 Toitures ; 4.2 Toitures en pente ; 4.3 Éléments |
| 5 | Cloisonnement - Doublage - Plafonds suspendus - Menuiseries intérieures | 5.1 Cloisons ; 5.2 Doublages, isolants et membranes ; 5.3 Plafonds suspendus ; 5.4 Planchers surélevés ; 5.5 Menuiseries, métalleries, quincailleries |
| 6 | Façades et menuiseries extérieures | 6.1 Revêtement, isolation et doublage extérieur ; 6.2 Portes, fenêtres, fermetures, protections solaires ; 6.3 Habillages |
| 7 | Revêtements des sols, murs et plafonds - Chape - Peintures - Produits de décoration | 7.1 ; 7.2 ; 7.3 |
| 8 | CVC (Chauffage - Ventilation - Refroidissement - eau chaude sanitaire) | 8.1 Équipements de production ; 8.2 Cogénération ; 8.3 Émission ; 8.4 Traitement de l'air et désenfumage ; 8.5 Réseaux et conduits ; 8.6 Stockage ; 8.7 Fluides frigorigènes |
| 9 | Installations sanitaires | 9.1 Éléments sanitaires et robinetterie ; 9.2 Canalisations, réseaux et systèmes de traitement |
| 10 | Réseaux d'énergie (courant fort) | 10.1 à 10.6 |
| 11 | Réseaux de communication (courant faible) | 11.1 Réseaux ; 11.2 Systèmes de sécurité ; 11.3 Installations |
| 12 | Appareils élévateurs et autres équipements de transport intérieur | - |
| 13 | Équipement de production locale d'électricité | affecté « au prorata du taux d'autoconsommation » |

Tableau 6 « Description de la composition physique de la parcelle » (p. 33) : 1. Gestion de l'eau ; 2. Ouvrages de soutènement ; 3. Aménagement de la parcelle ; 4. Locaux hors volume chauffé du bâtiment à usage tertiaire.

Carbone 4, « La biodiversité grise dans le bâtiment : comment estimer l'impact des matériaux de construction sur la nature ? », position paper, 30 pages, PDF fourni par Cédric le 17/10/2026 et lu intégralement (couverture, sommaire, notes de bas de page, annexes, quatrième de couverture ; métadonnées du fichier : créé et modifié le 07/10/2026 ; page de présentation en ligne datée du 6 octobre 2026). Copie dans `sources/acv/carbone4/`. Aucune mention de licence ni de copyright dans le document ; « Étude financée par Altarea et Nexity » (p. 24) ; auteurs Gabrielle Guidetti (manager des pôles Bâtiment et Biodiversité) et Jeanne Callec (consultante) ; « contribution de Darwin » (plateforme SaaS fondée en 2024 à Paris, p. 25).
- Méthode (p. 14 et annexe 1, p. 26 à 28) : « modélisation réalisée avec la plateforme nature de Darwin » ; empreinte calculée « en suivant la méthode IMPACT World + », métrique PDF, résultats en PDF.m².yr (« la fraction d'espèces qui risquent de disparaître complètement d'un milieu donné, sur une surface spécifique (m²) pendant une durée d'un an », p. 14 et 27). Ni MSA, ni GLOBIO, ni ReCiPe, ni LC-IMPACT ne sont utilisés (GLOBIO et ReCiPe sont seulement cités p. 9 parmi les méthodes existantes). Pressions et métriques du calcul (tableau p. 28) : changement d'usage des sols (occupation ; conversion, « transformation irréversible d'un écosystème naturel vers un usage anthropique différent »), changement climatique (GES), pollution (écotoxicité, acidification, eutrophisation marine et eau douce, formation d'ozone photochimique), exploitation des ressources (consommation d'eau). Les espèces exotiques envahissantes ne sont pas quantifiées.
- Données (p. 14, 20, 26 et 27) : bâtiment type modélisé pour en déduire les métrés ; chaque élément associé à une fiche INIES (FDES ou DED) « dans le cadre de l'accord d'accès au webservice INIES » de la plateforme Darwin ; les pressions couvertes par la fiche (réchauffement climatique, acidification, eutrophisation) sont reprises « sans recalcul ni modification » ; les pressions absentes des fiches (« occupation et transformation des terres, écotoxicité ») viennent d'un « proxy Ecoinvent représentatif du produit », « dimensionné de sorte que son empreinte carbone soit cohérente avec la valeur déclarée dans la fiche FDES », facteur d'échelle appliqué dans le calcul du projet sans création de donnée produit stockée. Le document écrit (p. 20) : « les FDES ne couvrent qu'une partie des pressions nécessaires à une évaluation biodiversité : elles documentent le changement climatique, l'acidification ou l'eutrophisation, mais pas l'occupation et la transformation des terres ni l'écotoxicité ». Annexe 2 (p. 28) : les comparaisons « portent sur des familles de matériaux et non sur des déclarations environnementales individuelles. Elles ne constituent ni une notation, ni un classement, ni un étiquetage de FDES ou de PEP ».
- Bâtiment type (p. 26) : logements collectifs, 3 000 m², R+4 avec parking en infrastructure, 50 logements, structure béton, toiture terrasse, façade enduit et plaquette brique, fenêtres PVC et volets roulants aluminium, carrelage et revêtement PVC, ascenseur, pompe à chaleur air/eau collective ; phases A1-A3 seulement (production, de l'extraction au transport, note 4 p. 3), sans renouvellement des matériaux ; lots 1, 10 et 11 non modélisés ; « les éléments modélisés représentent environ 80 % de l'empreinte carbone liée aux matériaux de construction du bâtiment ».
- Résultats du bâtiment type (p. 4, 15, 16) : impact biodiversité grise « 272 000 PDF.m².yr, correspondant à 12 500 m² de déforestation équivalente, soit environ 10 fois l'emprise du projet » ; répartition par pression (graphique p. 15, valeurs imprimées) : pollution 51 %, changement climatique 38 %, changement d'usage des sols 11 %, exploitation des ressources non chiffrée (part résiduelle) ; « plus de 50 % du résultat global en PDF.m²yr est lié à la pollution (écotoxicité, acidification, eutrophisation, etc.), très largement due aux produits en béton » ; lot 3 (superstructure) « plus d'1/4 de l'impact global », lot 6 (façades et menuiseries extérieures) en deuxième position ; dallages et murs en béton « plus d'un quart de l'impact total » ; volets roulants en aluminium 10 %, ascenseur 5 %, fenêtres PVC 4 % du total ; « forte corrélation entre l'impact carbone et l'impact sur la biodiversité ».
- Résultats par lot (graphique p. 15 « Résultats détaillés par pression et par lot du bâtiment », en k PDF.m².yr, lecture graphique approximative, les valeurs ne sont pas imprimées) : lot 2 environ 33 ; lot 3 environ 71 ; lot 4 environ 10 ; lot 5 environ 15 ; lot 6 environ 51 ; lot 7 environ 31 ; lot 8 environ 30 ; lot 9 environ 9 ; lot 12 environ 14 ; lots 1, 10, 11 et 13 absents. Dans chaque lot, la pollution et le changement climatique dominent ; le changement d'usage des sols est de l'ordre de 2 à 8 k par lot.
- Variante biosourcée (p. 16 et 17) : façade ossature bois au lieu de béton, fenêtres bois, parquet massif au lieu du PVC : 314 k PDF.m².yr, soit « 15% plus élevé que le bâtiment classique en béton » ; répartition : pollution 38 %, changement climatique 35 %, changement d'usage des sols 27 %, exploitation des ressources 0 % ; la pression changement d'usage des sols « est environ 3 fois plus importante que dans la modélisation initiale » ; facteurs génériques « qui ne prennent pas en compte des spécificités locales ou de choix spécifiques d'approvisionnement (par exemple d'éventuels labels FSC ou PEFC) ».
- Impact in situ (p. 17 à 19) : emprise au sol du bâtiment 750 m² et espaces extérieurs 500 m² dont la moitié d'espaces verts ; pressions limitées au changement d'usage des sols (conversion et occupation) ; surface avant projet non artificialisée (« un espace naturel de type prairie ou forêt ») : « les impacts in-situ représentent environ 58 k PDF.m².yr, soit 18% de l'impact total du projet » (total 330 k sur 50 ans, graphique p. 18) ; près de 40 % de cet impact in situ est la conversion, 60 % l'occupation pendant 50 ans (« durée de vie de référence d'un bâtiment ») ; « l'importance des impacts in situ (conversion et occupation) sont probablement surestimés : on considère ici un écosystème initial intact » ; variante friche industrielle : transformation nulle, occupation inchangée, in situ 11 % de 305 k ; construire sur une surface déjà artificialisée réduit les impacts in situ jusqu'à 40 %, « soit 8% de l'impact total ».
- Limites écrites par les auteurs (p. 15 et 20) : « premier exercice d'empreinte, les incertitudes associées sont importantes » ; facteurs d'impact « non spécifiques et pour la plupart pris au niveau monde » ; « l'impact sur l'utilisation des sols est probablement sous-estimé du fait des hypothèses intrinsèques au modèle qui prennent par défaut des prairies comme écosystème de départ et pénalisent peu les changements d'usage des sols d'une prairie vers un terrain transformé par une activité humaine » ; l'outil « ne permet pas de calculer finement l'impact in situ » (p. 22).
- Annexe 2 (p. 28 et 29, graphiques en k PDF.m².yr, lecture approximative) : revêtements de sol : stratifié environ 37, parquet massif environ 26, contrecollé environ 21, carrelage environ 7, PVC environ 7, moquette environ 5 ; « l'impact global des produits en bois est 3 à 7 fois plus important que les alternatives non biosourcées », le changement d'usage des sols étant « responsable de la quasi-totalité de l'impact » des produits bois, durée de vie non prise en compte (parquet 50 ans, PVC 25 ans, moquette 10 ans) ; menuiseries : fenêtres bois-alu environ 13, alu environ 11,5, PVC environ 10,5, bois environ 10, « la différence entre les différents types de menuiserie est assez faible ».
- Contexte cité (p. 8 à 10, 23) : construction responsable d'environ 50 % de l'extraction mondiale de matières premières (UNEP 2024) ; minéraux de construction près de 90 % de la masse anthropique mondiale (Elhacham 2020) ; Expedition Engineering 2023 comme « publication de référence » qualitative ; WBCSD 2024 ; UKGBC « Embodied Ecological Impacts » ; One Click LCA et G-ON 2024 ; méthode ACT Biodiversité de l'ADEME publiée en juin 2026, module sectoriel construction prévu en 2027 (p. 10 et 23).
- Calculs propres à partir des valeurs lues (pas dans le document) : impact gris par m² de surface de plancher = 272 000 / 3 000 ≈ 91 PDF.m².yr par m² (A1-A3, environ 80 % des matériaux) ; impact in situ sur site naturel ≈ 58 000 PDF.m².yr pour 1 250 m² de parcelle sur 50 ans, soit ≈ 0,93 PDF par m² de parcelle et par an ; part de l'usage des sols dans l'impact gris ≈ 0,11 × 272 000 ≈ 30 000 PDF.m².yr, soit environ la moitié de l'impact in situ : un module G limité à l'occupation et à la transformation des sols ne capte, dans ce modèle, qu'environ 11 % de la biodiversité grise, la pollution (51 %) et le climat (38 %) faisant le reste (voir point P19).

Autres études chiffrant la biodiversité grise des matériaux :
1. Montilla Moreno et al. 2026, « Assessing biodiversity impacts of buildings: an evaluation of building elements and limitations in current assessment methods », Int J LCA 31, art. 118, DOI 10.1007/s11367-026-02688-z, CC BY 4.0. Unité fonctionnelle 1 m² de mur extérieur, 100 ans, modules A1-A3, B4, C3-C4 ; Ecoinvent 3.10 + 17 EPD ; ReCiPe 2016 (H), LC-IMPACT, EN 15804+A2. Valeurs lues (species·yr par m² de mur) : ossature bois légère « 0.63·10-6 to 0.93·10-6 species·yr » (le plus bas) ; autres murs 1.49·10-6 à 2.42·10-6, 0.91·10-6 à 1.41·10-6, 1.29·10-6 à 1.85·10-6 ; part de l'usage des sols dans l'impact des biosourcés 70 à 95 % ; usage des sols moyen des produits biosourcés 2.30·10-8 species·yr (EN 15804+A2) et 2.58·10-8 (EPD) contre 5.13·10-13 à 1.25·10-11 pour les non biosourcés ; aluminium 6.76·10-8 species·yr/kg (ReCiPe) et 5.01·10-8 (LC-IMPACT). Limites lues : indicateur SQP des EPD « incompatible with ReCiPe units » ; certains EPD sans valeur d'usage des sols ; ReCiPe range l'extraction minière dans « artificial areas » ; une seule classe « used forest » ; résultats = « screening tool ».
2. Christiansson et Roos 2023, « Building materials and their impacts on biodiversity - A comparison of wood and concrete building frames », Chalmers, rapport E2023:079, PDF lu. 2 immeubles de 1 051 m², structures porteuses seulement. Table 28 (impacts usage des sols, PDF) : ReCiPe bois 1,77E-03 / béton 4,04E-06 ; Chaudhary et Brooks 6,64E-08 / 1,39E-10 ; Kuipers (HF) 2,40E-06 / 4,66E-09 : « The timber building has the unanimously highest impact across the three methods, ranging from approximately 440 times larger using ReCiPe to approximately 515 times larger using the HF method ». Tables 20-21 (CF Chaudhary et Brooks 2018, écorégion « Sarmatic mixed forest ») : Forest intense CFocc 1,52E-14 PDF/m², CFtrans 6,38E-12 PDF·yr/m² ; Urban intense 1,49E-14 et 6,27E-12. Hypothèses : rotation forestière 75 ans, carrière 30 ans.
3. One Click LCA / G-ON (16 juillet 2026) : entrepôt neuf en France sous RE2020, modules A1-A3 ; « The warehouse had higher total biodiversity impact (79,000 PDF·m²·yr) » ; « Indicators like land use change and invasive species were excluded due to current methodological limitations ».
4. Scherer et al. 2023 (GLAM / UNEP Life Cycle Initiative), DOI 10.1021/acs.est.3c04191 : CF pour 5 groupes d'espèces, 5 usages, 3 intensités, « 825 terrestrial ecoregions » et pays ; données CC BY 4.0 (Zenodo 10114493). Base de LC-IMPACT v2.
5. Expedition Engineering / ICE, novembre 2023 : « This research provides a qualitative appraisal », aucune quantification.
6. Ramboll, 17 février 2026 : qualitatif ; limite lue : « In some tools, including OneClick LCA, land-use change is omitted altogether » ; « Most LCAs rely on global or continental averages ».
7. LPO / Club U2B 2016 : définition d'après le GT « Bâtiment et Biodiversité » du Plan Bâtiment Durable (fin 2015) : « la biodiversité « grise » se comprend comme le cumul des impacts positifs et négatifs sur les écosystèmes et la biodiversité sur l'ensemble du cycle de vie d'un matériau ou d'un produit » ; aucune valeur chiffrée.

#### Limites pour un module « biodiversité grise » par lot de matériaux

1. Flux d'inventaire indispensables : tous les référentiels caractérisent des m²·an d'occupation et des m² de transformation par type d'usage. Une FDES ne publie pas ces flux : elle publie l'indicateur agrégé SQP (« sans unité », RE2020 Tableau 12) et, pour le climat, le GES-luluc. Aucun des référentiels biodiversité lus ne peut être appliqué à partir du seul SQP ; Montilla Moreno et al. 2026 constatent que le SQP est « incompatible with ReCiPe units ».
2. SQP / LANCA mesure des services du sol (érosion, filtration mécanique, recharge de nappe, production biotique), pas la biodiversité (métadonnées EF 3.1). De Laurentiis 2019 signale que LANCA attribue un CF d'érosion négatif (bénéfice) aux sols imperméabilisés, « conceptually debatable ».
3. Granularité des classes : les carrières (« mineral extraction site ») sont assimilées à l'urbain : ReCiPe 0.73 annual crop eq, LC-IMPACT v2 France 6.089e-14 Global PDF/m² (identique à « urban »), EF 3.1 GLO 110.79 Pt/m²a. ReCiPe n'a qu'une classe « used forest » (0.30) ; LC-IMPACT v2 distingue « forest, intensive » (1.397e-14) et plantations (4.804e-14 intense) pour la France.
4. Échelle spatiale : ReCiPe ne fournit que des moyennes mondiales ; LC-IMPACT v2 et EF 3.1 fournissent des valeurs par pays, mais l'origine réelle des matières d'une FDES collective n'est pas localisée.
5. Transformation : horizon et temps de régénération sont des choix de valeur à fort effet (Koellner : « very sensitive » ; LC-IMPACT v2 : t de 80 à 1 186 ans ; ReCiPe : 73.5 / 7.5 / 33.9 ans ; EF : 85 ans artificiel, 20 ans biotique) ; les transformations entre usages anthropiques ne sont pas couvertes.
6. Métriques non commensurables : PDF local (ReCiPe), PDF régional et global (LC-IMPACT, via GEP), species·yr, PDF.m².yr (Carbone 4, One Click LCA), MSA (GLOBIO), Pt (EF). Aucune conversion MSA vers PDF n'a été lue.
7. Incertitude et proxys : LC-IMPACT v2 indique « large data gaps in the CFs », des proxys à utiliser « with caution », une sensibilité forte aux GEP et affinités d'habitat.
8. Divergences d'ordre de grandeur entre méthodes : pour la même structure bois, Christiansson et Roos 2023 obtiennent 1,77E-03 (ReCiPe), 2,40E-06 (Kuipers) et 6,64E-08 PDF (Chaudhary et Brooks) ; Carbone 4 : + 15 % d'impact biodiversité global pour la substitution béton vers bois non tracé.
9. Contrainte juridique INIES : la licence webservice interdit « classements, notations, scorings, étiquettes ou tout dispositif assimilé portant sur les Déclarations Environnementales » et toute réutilisation hors ACV / bilan GES / MFA ; un module de notation biodiversité par produit ou par FDES relèverait de cette interdiction sans accord écrit de l'association INIES. Le webservice coûte 400 € HT (dossier) + 2 800 € HT/an + 20 € HT par utilisateur autorisé.
10. Lots RE2020 : les lots 8 à 13 reposent sur des PEP et des DED ; la seule répartition par lot lue est le graphique de Carbone 4 (p. 15, lots 2 à 9 et 12, valeurs non imprimées, lecture approximative), en PDF.m².yr toutes pressions confondues ; l'usage des sols n'y pèse que 11 % du total.

#### Ce qui manque (non trouvé ou non vérifiable au 17/10/2026)

- Chaudhary et al. 2015 : texte intégral, valeurs de l'exposant z par écorégion, formule exacte du score de vulnérabilité, tables de la Supporting Information (page ACS non accessible).
- LC-IMPACT v1.3 : valeurs numériques par écorégion ou pays (zip de 4,5 Go non téléchargé) ; valeurs des GEP par pays (2_GEP.zip non lu).
- Texte de la norme EN 15804+A2 et du complément national (définition exacte du SQP, caractère obligatoire ou optionnel) ; vérification sur un échantillon de FDES de la présence effective d'une valeur SQP.
- Carbone 4 : les valeurs par lot et par matériau ne sont imprimées nulle part (graphiques seulement) ; les facteurs IMPACT World+ et les proxys ecoinvent employés par Darwin ne sont pas publiés ; la licence du document n'est pas indiquée.
- NOR et page JORF de l'arrêté du 4 août 2021 (Legifrance bloqué).
- Valeur de référence biodiversité par m² de plancher pour un bâtiment français, et par lot 1 à 13 : aucune source lue n'en publie.
- Facteurs CDC Biodiversité / GBS appliqués au bâtiment : aucune source chiffrée trouvée.
- Conversion documentée entre MSA.km², PDF global et species·yr.

#### Sources consultées (2.4)

Lues intégralement : https://lc-impact.eu/doc/Verones_etal_2020_LC-IMPACT.pdf ; pages lc-impact.eu (index, index_v13, index_v2, ecosystem_quality, ecosystem_quality_v2, EQland_stress, EQland_stress_v2, EQLand_MSA_v2, FAQ, about) ; https://zenodo.org/records/18670560 (page, fichiers 6_CF_LAND_USE.zip et 14_CF_LAND_USE_MSA.zip lus) ; https://zenodo.org/records/6200606 (page seule) ; https://zenodo.org/records/10114493 (page seule) ; https://www.rivm.nl/sites/default/files/2018-11/Report%20ReCiPe_Update_20171002_0.pdf ; https://www.rivm.nl/sites/default/files/2024-10/ReCiPe2016_CFs_v1.1_20180117.xlsx ; https://knowledge-for-policy.ec.europa.eu/sites/default/files/EF-v3.1_2.zip (fichier Land use XML et Normalisation_Weighting_Factors_EF_3.1.xlsx) ; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6472660/fullTextXML ; https://publications.polymtl.ca/4975/1/2013_Koellner_Unep-Setac_guideline_global_land_use.pdf ; https://technical-regulation-information-system.ec.europa.eu/et/notification/23190/text/F/FR ; https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/annexeii_arrete_4_aout_2021.pdf ; https://carbone4.com/fr/publications/la-biodiversite-grise-dans-le-batiment-comment-estimer-l-impact-des-materiaux-de-construction-sur-la-nature ; pages inies.fr (accueil, FDES, webservice, FAQ, contexte réglementaire, CGU, bon de commande, chiffres clés, annexe A tarifs) ; https://odr.chalmers.se/bitstreams/59a8a732-cf1b-4cc7-890a-8a94c53054b6/download ; https://www.effinergie.org/web/images/attach/base_doc/2998/fichebiodiversitegrise.pdf ; notices Crossref des DOI cités ; https://www.ffbatiment.fr/techniques-batiment/reglementation-construction/reglementation-thermique-environnementale/dossier/quels-sont-les-deux-indicateurs-carbone-de-la-re2020.

Lues partiellement : https://link.springer.com/article/10.1007/s11367-026-02688-z ; https://oneclicklca.com/en/resources/case-studies/biodiversity-in-construction-lifecycle-assessment ; https://www.ramboll.com/en-gb/insights/decarbonise-for-net-zero/beyond-net-zero-practical-ways-to-measure-nature-impact ; https://expedition.uk.com/wp-content/uploads/2023/11/231103_Embodied-Biodiversity_Report_Compressed.pdf ; https://research-collection.ethz.ch/handle/20.500.11850/643067 ; https://orbit.dtu.dk/en/publications/soil-quality-index-exploring-options-for-a-comprehensive-assessme/.

Non accessibles : https://pubs.acs.org/doi/10.1021/acs.est.5b02507 ; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043936431 (Cloudflare) ; API Zenodo (403) et doi.org/10.5281/zenodo.6200606 (429) ; pages PMC (reCAPTCHA) ; https://www.sciencedirect.com/science/article/pii/S095965261833960X ; https://hal.inrae.fr/hal-04573403v1/document ; https://base-inies.fr/swagger/index.html (page vide en texte). Le PDF de Carbone 4 (formulaire HubSpot https://2dycgm.share-eu1.hsforms.com/2i2gsSg7sQ8anzxmaT8uNeA) a été fourni directement par Cédric le 17/10/2026 et lu intégralement.

Fichiers de travail conservés : recipe2016.pdf, koellner2013.pdf, verones2020.pdf, annexeii_arrete_4_aout_2021.pdf, EQ_LandUse_gloPDF_Country_Aggregated_2025-12-17.xlsx, 6_EQ_Land_Use_Chapter.pdf, b2ad6890-c78d-11e6-9d9d-cec0c932ce01.xml (EF 3.1 Land use), ReCiPe2016_CFs_v1.1_20180117.xlsx, pmc6472660.xml, cgu_ws_2026.pdf, bon_commande_2026.pdf, chalmers_thesis.pdf, carbone4_biodiv_grise.html, Carbone4_2026_biodiversite_grise_batiment_position_paper.pdf (dossier `sources/acv/` du projet).

### 2.5 Cadre français et nomenclatures : ZAN, trame verte et bleue, CBS et BAF, UGF, EUNIS, CORINE Biotopes, HabRef, zones biogéographiques, XSD du RSEE

Date de consultation de toutes les pages : 17/10/2026. Règle appliquée : aucune valeur de mémoire ; chaque valeur a été lue dans un fichier ou une page récupérés pendant la session. Les tirets typographiques des textes originaux sont rendus par des traits d'union ordinaires.

Contrainte d'accès majeure : legifrance.gouv.fr est derrière une protection Cloudflare qui renvoie 403 à tous les téléchargements directs et fait échouer la plupart des lectures. Le texte consolidé des codes a donc été lu dans les PDF officiels-miroirs de codes.droit.org (données DILA, « Code de l'urbanisme (Mise à jour du 2026-09-01), version éditée le 2026-10-01 », 704 pages ; « Code de l'environnement (Mise à jour du 2026-10-07) »), qui portent les hyperliens Legifrance de chaque article (identifiants LEGIARTI donnés ci-dessous). 2 pages Legifrance ont tout de même répondu (JORFTEXT000048465959 et LEGIARTI000048470652) et confirment le texte.

#### 2.5.1 Nomenclature de l'artificialisation des sols (ZAN)

Objet : article L. 101-2-1 et article R. 101-1 du code de l'urbanisme avec son annexe (nomenclature), créés par le décret n° 2022-763 du 29 avril 2022 et réécrits par le décret n° 2023-1096 du 27 novembre 2023 ; décision du Conseil d'État n° 465341 du 4 octobre 2023.

Accès et licence :
- Décret n° 2023-1096 (JORF n° 0275 du 28/11/2023, NOR TREL2307502D) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465959 (lu partiellement).
- Article R. 101-1 consolidé : https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000048470613 (non accessible directement ; texte lu dans le PDF codes.droit.org p. 331-332). Annexe : https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000048470652 (lue, « version en vigueur depuis le 29 novembre 2023 »). R. 101-2 : LEGIARTI000048469670.
- Article L. 101-2-1 : https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000043967077 (PDF codes.droit.org p. 14).
- Décret n° 2022-763 (NOR LOGL2201338D, JORF n° 0101 du 30/04/2022) : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000045727061 (métadonnées lues ; corps et annexe non accessibles).
- Décision CE n° 465341 du 04/10/2023 : https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-10-04/465341 (lue).
- Projet de décret et rapport de présentation soumis à consultation (09/06/2023) : https://www.consultations-publiques.developpement-durable.gouv.fr/IMG/pdf/trel2307502d_pjd-nomenclature-rapport-local-zan.pdf et https://www.consultations-publiques.developpement-durable.gouv.fr/IMG/pdf/trel2307502d_rapport-presentation-dce-nomenclature-rapport-local_zan.pdf (lus intégralement).
- Fiche indicateur « Artificialisation » (portail de l'artificialisation, version 15/05/2024) : https://artificialisation.developpement-durable.gouv.fr/sites/artificialisation/files/inline-files/2024_0122_Fiche_Artificialisation_V5.pdf (lue intégralement).
- Licence : textes officiels (réutilisation libre des données DILA).

Contenu et valeurs. Article L. 101-2-1 (PDF codes.droit.org p. 14) : « L'artificialisation est définie comme l'altération durable de tout ou partie des fonctions écologiques d'un sol, en particulier de ses fonctions biologiques, hydriques et climatiques, ainsi que de son potentiel agronomique par son occupation ou son usage. » ; « a) Artificialisée une surface dont les sols sont soit imperméabilisés en raison du bâti ou d'un revêtement, soit stabilisés et compactés, soit constitués de matériaux composites ; b) Non artificialisée une surface soit naturelle, nue ou couverte d'eau, soit végétalisée, constituant un habitat naturel ou utilisée à usage de cultures. »

Article R. 101-1 en vigueur (rédaction décret 2023-1096, art. 1 ; PDF codes.droit.org p. 331) : II : « le solde entre les surfaces artificialisées et les surfaces désartificialisées est évalué au regard des catégories listées par la nomenclature annexée au présent article. Pour cette évaluation, les surfaces sont qualifiées dans ces catégories selon l'occupation effective du sol observée et non selon les zones ou secteurs délimités par les documents de planification et d'urbanisme. L'occupation effective est mesurée à l'échelle de polygones dont la surface est définie en fonction de seuils de référence fixés dans la nomenclature annexée au présent article selon les standards du Conseil national de l'information géolocalisée. » III : « Peuvent être considérées comme des surfaces non artificialisées [...] 1° Soit les surfaces sur lesquelles sont implantées des installations de production d'énergie solaire photovoltaïque qui respectent les critères fixés par le décret [...] ; 2° Soit les surfaces dont les sols sont végétalisés et à usage de parc ou de jardin public. »

Annexe à l'article R. 101-1 (10 catégories, texte lu dans Legifrance LEGIARTI000048470652 et PDF codes.droit.org p. 444) :

| Groupe | Catégorie (texte exact) | Seuil de référence (*) |
|---|---|---|
| Surfaces artificialisées | 1° Surfaces dont les sols sont imperméabilisés en raison du bâti (constructions, aménagements, ouvrages ou installations). | Supérieur ou égal à 50 m2 d'emprise au sol |
| | 2° Surfaces dont les sols sont imperméabilisés en raison d'un revêtement (artificiel, asphalté, bétonné, couvert de pavés ou de dalles). | Supérieur ou égal à 2 500 m2 d'emprise au sol ou de terrain (cellule couvrant les catégories 2° à 10°) |
| | 3° Surfaces partiellement ou totalement perméables dont les sols sont stabilisés et compactés ou recouverts de matériaux minéraux, ou dont les sols sont constitués de matériaux composites (couverture hétérogène et artificielle avec un mélange de matériaux non minéraux). | idem |
| | 4° Surfaces à usage résidentiel, de production secondaire ou tertiaire, ou d'infrastructures notamment de transport ou de logistique, dont les sols sont couverts par une végétation herbacée (**). | idem |
| | 5° Surfaces entrant dans les catégories 1° à 4°, qui sont en chantier ou en état d'abandon. | idem |
| Surfaces non artificialisées | 6° Surfaces naturelles dont les sols sont soit nus (sable, galets, rochers, pierres ou tout autre matériau minéral, y compris les surfaces d'activités extractives de matériaux en exploitation) soit couverts en permanence d'eau, de neige ou de glace. | idem |
| | 7° Surfaces à usage de cultures dont les sols sont soit arables ou végétalisés (agriculture), y compris si ces surfaces sont en friche, soit recouverts d'eau (pêche, aquaculture, saliculture). | idem |
| | 8° Surfaces dont les sols sont végétalisés et à usage sylvicole. | idem |
| | 9° Surfaces dont les sols sont végétalisés et qui constituent un habitat naturel. | idem |
| | 10° Surfaces dont les sols sont végétalisés et qui n'entrent pas dans les catégories précédentes. | idem |

Notes de l'annexe : « (*) Les infrastructures linéaires sont qualifiées à partir d'une largeur minimale de cinq mètres. » ; « (**) Une surface végétalisée est qualifiée d'herbacée dès lors que moins de vingt-cinq pour cent du couvert végétal est arboré. »

Rapport de présentation du 09/06/2023 (p. 3) : « sont intégrés les seuils de référence [...] (50 m² pour le bâti et 2 500 m² pour les autres catégories de surface ; 5 mètres de large pour les infrastructures linéaires et au moins 25% de boisement d'une surface végétalisée pour qu'elle ne soit pas seulement considérée comme herbacée) ». Même page : « Cette nomenclature n'a pas non plus vocation à s'appliquer au niveau d'un projet, pour lequel l'artificialisation induite est appréciée directement au regard de l'altération durable des fonctions écologiques ainsi que du potentiel agronomique du sol. »

Fiche indicateur OCS GE (p. 3) : unités minimales OCS GE « 500 m² en zone construite et 2500 m² en zone non-construite », « Le seuil de prise en compte des bâtiments est de 50 m². La superficie des zones bâties supérieures à 50 m² et inférieure à 200 m² est portée à 200 m². »

Décision CE n° 465341 (04/10/2023) : article 1er « Le 2ème alinéa du II de l'article R. 101-1 du code de l'urbanisme est annulé. » Motif : le décret 2022-763 n'avait pas fixé lui-même « l'échelle à laquelle l'artificialisation des sols doit être appréciée ».

Limites :
- Le texte des 8 catégories de la version 2022 n'a pas pu être lu : NON VÉRIFIÉ.
- Arrêté « du 29 avril 2022 (seuils) » : NON VÉRIFIÉ : aucun arrêté de ce type n'a été trouvé ; le décret 2023-1096 a inscrit les seuils directement dans l'annexe.
- La nomenclature est une convention de mesure du solde à l'échelle des documents de planification ; elle est explicitement déclarée inapplicable « au niveau d'un projet ».
- Le terme « pleine terre » n'apparaît pas dans l'article R. 101-1 ni dans son annexe.

#### 2.5.2 Trame verte et bleue : L. 371-1, R. 371-16 à R. 371-21, décret 2012-1492, SRADDET

Accès : L. 371-1 : https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000047088033 (PDF codes.droit.org p. 351). R. 371-16 à R. 371-23 : LEGIARTI000032973966, LEGIARTI000026866769, LEGIARTI000026866771, LEGIARTI000026866773, LEGIARTI000026866775, LEGIARTI000026866777, LEGIARTI000026866781, LEGIARTI000026866784 (PDF codes.droit.org p. 1315-1317). Décret n° 2012-1492 du 27/12/2012 : https://aida.ineris.fr/reglementation/decret-ndeg-2012-1492-271212-relatif-a-trame-verte-bleue (lu).

Contenu (texte exact). L. 371-1 : « I. - La trame verte et la trame bleue ont pour objectif d'enrayer la perte de biodiversité en participant à la préservation, à la gestion et à la remise en bon état des milieux nécessaires aux continuités écologiques, tout en prenant en compte les activités humaines, et notamment agricoles, en milieu rural ainsi que la gestion de la lumière artificielle la nuit. » ; « II. - La trame verte comprend : 1° Tout ou partie des espaces protégés au titre du présent livre et du titre Ier du livre IV ainsi que les espaces naturels importants pour la préservation de la biodiversité ; 2° Les corridors écologiques constitués des espaces naturels ou semi-naturels ainsi que des formations végétales linéaires ou ponctuelles, permettant de relier les espaces mentionnés au 1° ; 3° Les surfaces mentionnées au I de l'article L. 211-14. » ; « III. - La trame bleue comprend : 1° Les cours d'eau, parties de cours d'eau ou canaux figurant sur les listes établies en application de l'article L. 214-17 ; 2° Tout ou partie des zones humides [...] ; 3° Les cours d'eau, parties de cours d'eau, canaux et zones humides importants pour la préservation de la biodiversité et non visés aux 1° ou 2° ».

L. 371-3 II : le SRADDET « définit les enjeux régionaux en matière de préservation et de remise en bon état des continuités écologiques » ; III : en Île-de-France, « Schéma régional de cohérence écologique ».

R. 371-19 : « I. - Les continuités écologiques constituant la trame verte et bleue comprennent des réservoirs de biodiversité et des corridors écologiques. II. - Les réservoirs de biodiversité sont des espaces dans lesquels la biodiversité est la plus riche ou la mieux représentée, où les espèces peuvent effectuer tout ou partie de leur cycle de vie et où les habitats naturels peuvent assurer leur fonctionnement en ayant notamment une taille suffisante, qui abritent des noyaux de populations d'espèces à partir desquels les individus se dispersent ou qui sont susceptibles de permettre l'accueil de nouvelles populations d'espèces. [...] III. - Les corridors écologiques assurent des connexions entre des réservoirs de biodiversité, offrant aux espèces des conditions favorables à leur déplacement et à l'accomplissement de leur cycle de vie. Les corridors écologiques peuvent être linéaires, discontinus ou paysagers. [...] IV. - Les cours d'eau, parties de cours d'eau et canaux mentionnés au 1° et au 3° du III de l'article L. 371-1 constituent à la fois des réservoirs de biodiversité et des corridors écologiques. Les zones humides [...] constituent des réservoirs de biodiversité ou des corridors écologiques ou les deux à la fois. »

R. 371-20 : « I. - La remise en bon état des milieux nécessaires aux continuités écologiques consiste dans le rétablissement ou l'amélioration de leur fonctionnalité. [...] II. - La préservation des milieux nécessaires aux continuités écologiques assure au moins le maintien de leur fonctionnalité. » R. 371-21 : « La fonctionnalité des continuités écologiques s'apprécie notamment au regard : - de la diversité et de la structure des milieux qui leur sont nécessaires et de leur niveau de fragmentation ; - des interactions entre milieux, entre espèces et entre espèces et milieux ; - de la densité nécessaire à l'échelle du territoire concerné. »

Limites : définitions qualitatives, sans seuil numérique (ni surface minimale de réservoir, ni largeur de corridor). Les SRCE ont été absorbés par les SRADDET (sauf Île-de-France).

#### 2.5.3 Coefficient de biotope par surface (CBS)

Berlin, Biotopflächenfaktor (BFF). Accès : pages de la Senatsverwaltung (lues intégralement) : https://www.berlin.de/sen/uvk/natur-und-gruen/landschaftsplanung/bff-biotopflaechenfaktor/ ; https://www.berlin.de/sen/uvk/natur-und-gruen/landschaftsplanung/bff-biotopflaechenfaktor/bff-berechnung/ ; https://www.berlin.de/sen/uvk/natur-und-gruen/landschaftsplanung/bff-biotopflaechenfaktor/anwendungsbereiche/ ; PDF « Muster der textlichen Festsetzungen zum Biotopflächenfaktor-Landschaftsplan, Stand Februar 2025 » : https://www.berlin.de/sen/uvk/_assets/natur-gruen/landschaftsplanung/bff-biotopflaechenfaktor/bff-muster_textliche-festsetzungen.pdf (7 pages, lu intégralement). Licence : non indiquée.

Formule (page bff-berechnung) : « BFF = naturhaushaltswirksame Flächen ÷ Grundstücksfläche ». Arrondi à 2 décimales.

Facteurs pour les Landschaftspläne fixés avant décembre 2019 : Versiegelte Flächen 0,0 ; Teilversiegelte Flächen 0,3 ; Halboffene Flächen 0,5 ; Vegetationsflächen ohne Bodenanschluss, moins de 80 cm de substrat 0,5 ; plus de 80 cm 0,7 ; Vegetationsflächen mit Bodenanschluss 1,0 ; Regenwasserversickerung je m² Dachfläche 0,2 ; Vertikalbegrünung 0,5 ; Begrünte Dachflächen 0,7.

Facteurs pour les Landschaftspläne fixés après décembre 2019 (page bff-berechnung et Muster Nummer 4) :
- Wege- und Verkehrsflächen : Versiegelte Flächen 0,0 ; Teilversiegelte Flächen 0,1 ; Durchlässige Belagsflächen 0,2 ; Begrünte Belagsflächen 0,4.
- Vegetationsflächen : unterbaute Vegetationsfläche, substrat 20 à 40 cm 0,5 ; 41 à 80 cm 0,6 ; 81 à 150 cm 0,7 ; plus de 150 cm 0,9 ; Vegetationsfläche mit Bodenanschluss 1,0 (réductions : -0,5 gazon tondu ras, -0,4 prairie extensive, -0,3 herbacée avec haies ou petits arbustes jusqu'à 2 m, -0,2 grands arbustes, -0,1 petits arbres 2 à 10 m).
- Blaue Flächen : Versickerungsfläche 0,2 ; Wasserfläche 0,5 (+0,1 avec végétalisation).
- Gebäudebegrünungen : Extensive Dachbegrünung (< 20 cm, sans arrosage) 0,5 (+0,1 avec rétention technique) ; Einfach-intensive Dachbegrünung (15 à 50 cm) 0,7 ; Intensive Dachbegrünung (> 50 cm) 0,8 ; Bodengebundene Vertikalbegrünung 0,5 (hauteur comptée max 10 m) ; Wandgebundene Vertikalbegrünung 0,7.

Valeurs cibles (page anwendungsbereiche, ÜBG = Überbauungsgrad) : Wohnungen : Neubau 0,60 ; modification : ÜBG jusqu'à 0,37 → 0,60 ; 0,38 à 0,49 → 0,45 ; à partir de 0,50 → 0,30. Gewerbliche Nutzung : 0,30 / 0,30. Kerngebietstypische Nutzungen : 0,30 / 0,30. Öffentliche Einrichtungen : comme Wohnungen. Schulen : 0,30 / 0,30 sur la page ; le Muster (février 2025) prévoit 0,40 en construction neuve. Kindertagesstätten : Neubau 0,60. Technische Infrastruktur : 0,30 / 0,30.

France, L. 151-22 du code de l'urbanisme (version « LOI n°2026-103 du 19 février 2026 - art. 108 », https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546385, PDF codes.droit.org p. 124) : « I. - Le règlement peut imposer une part minimale de surfaces non imperméabilisées ou éco-aménageables, éventuellement pondérées en fonction de leur nature, afin de contribuer au maintien de la biodiversité et de la nature en ville. II. - Dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants [...] et dans les communes de plus de 15 000 habitants en forte croissance démographique [...], le règlement définit, dans les secteurs qu'il délimite, une part minimale de surfaces non imperméabilisées ou éco-aménageables, selon les modalités prévues au I du présent article. III. - [...] à l'exclusion des projets de rénovation, de réhabilitation ou de changement de destination des bâtiments existants qui n'entraînent aucune modification de l'emprise au sol. »

Exemple 1, Eurométropole de Strasbourg, règlement écrit du PLU, dossier approuvé 6 février 2026 (modification simplifiée n° 6), 204 pages : https://sig.strasbourg.eu/datastrasbourg/plu_media/reglement_actuel.pdf (lu intégralement), article 9 « Coefficient de biotope par surface », p. 33-34 : s'applique aux nouveaux bâtiments et extensions > 25 m² d'emprise au sol. Valeur écologique : Espaces plantés en pleine terre 1 ; Plantations sur dalle ou toiture végétalisée, substrat ≥ 80 cm 0,9 ; substrat > 30 cm 0,7 ; Toiture végétalisée extensive ou semi-intensive, substrat ≤ 30 cm 0,6 ; Toiture végétalisée extensive, substrat < 10 cm 0,5 ; Aménagement végétalisé en surface verticale 0,4 ; Surface minérale perméable (pavés, pavés joints gazon, béton poreux, gravier ou sable tassé) 0,2 ; Surface minérale imperméable 0. Bonus écologique (dans la limite de 10 points) : arbre planté, parcelle < 1 000 m² : 1 % par arbre ; parcelle > 1 000 m² : 0,5 % par arbre ; arbre conservé 2 % par arbre ; clôture végétalisée pluri-essences 0,10 % / ml ; toiture BioSolaire sur plus de 40 % de la toiture 10 %. Cibles par zone : 25 %, 30 %, 35 %, 40 %, 50 % minimum selon les zones.

Exemple 2, Grand Annecy, PLUi HMB approuvé le 18 décembre 2025, « Fiche technique Coefficients de biotope et de pleine terre », 26 mars 2026 : https://plui-hmb-approuve-ga.grandannecy.fr/04_REGLEMENT/FICHE_AIDE_instruction_CBS.pdf (lue intégralement) : Surfaces imperméables 0 ; semi-perméables (clinker, dallage mosaïque, dallage sur gravier/sable) 0,3 ; semi-ouvertes (dalle de bois, treillis de pelouse) 0,5 ; Espaces verts sur dalle 1 (terre végétale < 80 cm) 0,5 ; sur dalle 2 (> 80 cm) 0,7 ; Espaces verts en pleine terre 1.

Exemple 3, Paris, PLU, règlement tome 1, version approuvée décembre 2019, article UG.13.1.2 p. 95-96 : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2022-01/C_REG1-V23.pdf : « Svp = Spt + 0,8.Sve + 0,5.Stv + 0,2.Smv » avec 1 pour la pleine terre, 0,8 pour les surfaces au sol avec au moins 0,80 m de terre, 0,5 pour les toitures et terrasses végétalisées avec substrat ≥ 0,10 m, 0,2 pour les murs végétalisés. Ce document est le PLU 2019, antérieur au PLU bioclimatique, dont le règlement en vigueur n'a pas pu être lu : NON VÉRIFIÉ.

Exemple 4 (source secondaire), Avignon, via Cerema/OFB « Retour d'expériences, Livrable 2, avril 2024 » https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable2_RETEX_VF-1.pdf p. 14 : CBS 0,2 à 0,6 selon les zones ; PLT 0,2 à 0,4. Même document p. 12 (synthèse de 10 collectivités) : imperméables 0 ; semi-perméables entre 0,15 et 0,5 ; espaces verts sur dalle et toitures entre 0,1 et 1 selon substrat ; façades entre 0,1 et 0,5 ; pleine terre 1 (parfois 1,2 à titre dérogatoire). Présentation Cerema du 05/12/2024 (https://www.planif-territoires.logement.gouv.fr/IMG/pdf/cerema_etudecbs_cpt.pdf) : « Indicateurs d'occupation des sols (et non de biodiversité) », « Ne reposent que sur du déclaratif », « Terme de « biotope » du CBS trompeur ».

Limites : chaque collectivité fixe ses propres types et coefficients. Lyon, Bordeaux, Marseille, Montpellier, Rennes : règlements non lus (quota de recherche épuisé).

#### 2.5.4 London Plan 2021, Policy G5 et UGF guidance 2023

Accès : London Plan 2021 : https://www.london.gov.uk/sites/default/files/the_london_plan_2021.pdf ; « London Plan Guidance - Urban Greening Factor », GLA, February 2023 (lu intégralement) : https://www.london.gov.uk/sites/default/files/2023-02/London%20Plan%20Guidance%20-%20Urban%20Greening%20Factor.pdf. Copyright Greater London Authority ; licence de réutilisation non indiquée.

Policy G5 (London Plan 2021, p. 323) : « B Boroughs should develop an Urban Greening Factor (UGF) to identify the appropriate amount of urban greening required in new developments. [...] In the interim, the Mayor recommends a target score of 0.4 for developments that are predominately residential, and a target score of 0.3 for predominately commercial development (excluding B2 and B8 uses). » Paragraphe 8.5.6 : « (Factor A x Area) + (Factor B x Area) + (Factor C x Area) etc. divided by Total Site Area. »

Table 8.2 (London Plan p. 325) et Table 3.1 du guidance (p. 8-9) :

| Surface cover type (texte exact) | Factor |
|---|---|
| Semi-natural vegetation (e.g. trees, woodland, species-rich grassland) maintained or established on site | 1 |
| Wetland or open water (semi-natural; not chlorinated) maintained or established on site | 1 |
| Intensive green roof or vegetation over structure; substrate minimum settled depth of 150mm | 0.8 |
| Standard trees planted in connected tree pits with a minimum soil volume equivalent to at least two-thirds of the projected canopy area of the mature tree | 0.8 |
| Extensive green roof with substrate of minimum settled depth of 80mm (or 60mm beneath vegetation blanket) - meets the requirements of GRO Code 2014 | 0.7 |
| Flower-rich perennial planting | 0.7 |
| Rain gardens and other vegetated sustainable drainage elements | 0.7 |
| Hedges (line of mature shrubs one or two shrubs wide) | 0.6 |
| Standard trees planted in pits with soil volumes less than two-thirds of the projected canopy area of the mature tree | 0.6 |
| Green wall - modular system or climbers rooted in soil | 0.6 |
| Groundcover planting | 0.5 |
| Amenity grassland (species-poor, regularly mown lawn) | 0.4 |
| Extensive green roof of sedum mat or other lightweight systems that do not meet GRO Code 2014 | 0.3 |
| Water features (chlorinated) or unplanted detention basins | 0.2 |
| Permeable paving | 0.1 |
| Sealed surfaces (e.g. concrete, asphalt, waterproofing, stone) | 0 |

Guidance 2023 : §3.2.1 : calcul sur « the total site area, equivalent to the red-line boundary » ; §3.2.2 : murs végétalisés comptés sans être ajoutés à la surface du site (UGF > 1 possible) ; surface sous canopée d'arbre sur sol perméable comptée aussi ; Appendix 1 : « Sealed surfaces 0 Includes artificial grass » ; exemple arbre : canopée 50 m² exige 33 m³ de sol pour 0,8. Limites : facteurs fondés sur un proxy d'infiltration (8.5.3) ; cibles « interim ».

#### 2.5.5 Typologies d'habitats

EUNIS (EEA). L'application eunis.eea.europa.eu est retirée (redirection vers BISE : https://biodiversity.europa.eu/resources/search-habitat). Fiches de métadonnées EEA SDI (lues en JSON) :
- « EUNIS habitat classification and crosswalks (tabular data) » : https://sdi.eea.europa.eu/catalogue/srv/api/records/638330ea-90e6-4e41-81ea-e70f25ae7117 (2022-03-28 ; métadonnées révisées 2026-09-25).
- « EUNIS terrestrial habitat classification review (tabular) - version 1, Nov. 2021 » : https://sdi.eea.europa.eu/catalogue/srv/api/records/bfe4c237-e378-4a83-ab21-b3807f96c2e2 ; DOI https://doi.org/10.2909/bfe4c237-e378-4a83-ab21-b3807f96c2e2 ; téléchargement https://sdi.eea.europa.eu/data/bfe4c237-e378-4a83-ab21-b3807f96c2e2 (fichiers : « EUNIS terrestrial habitat classification 2021_1 including crosswalks.xlsx » ; variantes avec crosswalks Annex I et Red List ; README.md).
- « EUNIS marine habitat classification review (tabular) - version 1, 2022 » : https://sdi.eea.europa.eu/catalogue/srv/api/records/8a5eccda-e6ea-4018-a373-5c76a8eeec78.
- « EUNIS habitat classification 2012 (tabular) - version 1, 2019 » : https://sdi.eea.europa.eu/catalogue/srv/api/records/566bf5a0-e41a-48e3-912a-3ec0767da310 ; téléchargement https://sdi.eea.europa.eu/data/566bf5a0-e41a-48e3-912a-3ec0767da310 (fichiers : « EUNIS habitat classification 2007 - Revised descriptions 2012 amended 2019.xls » ; « Crosswalk EUNIS 2007 and Annex I 2008.xls » ; « Crosswalk EUNIS 2007 and PALHAB 2001.xls » ; « Crosswalk Resolution 4 and Annex I (2022).xlsx » ; « Crosswalk between EUNIS habitats classification and Corine Land Cover.pdf »).
- Format : « Microsoft Excel (.xls, .xlsx) ». Licence (texte exact des 3 fiches) : « License CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Copyright holder: European Environment Agency (EEA). » ; « no limitations to public access ».

Contenu :
- Abstract 638330ea : « The review of the EUNIS habitat classification was initiated in 2014 and the revision is on-going. Revised groups version 2019 and 2021 are published in parallel to the EUNIS habitat classification 2012. The review concerns the groups of marine habitats, coastal habitats, grasslands, heathland, forest, sparsely vegetated, vegetated man-made habitats and wetlands. The remaining groups (inland waters and complex habitats) will be revised and published at a later stage. »
- EUNIS 2012 (fichier xls lu) : 5 285 lignes, niveaux 1 à 8 (niveau 1 : 11 groupes A à J plus X ; niveau 2 : 87 ; niveau 3 : 326 ; niveau 4 : 1 238 ; niveau 5 : 2 084 ; niveau 6 : 1 180 ; niveau 7 : 328 ; niveau 8 : 30). Groupes : A Marine habitats ; B Coastal habitats ; C Inland surface waters ; D Mires, bogs and fens ; E Grasslands and lands dominated by forbs, mosses or lichens ; F Heathland, scrub and tundra ; G Woodland, forest and other wooded land ; H Inland unvegetated or sparsely vegetated habitats ; I Regularly or recently cultivated agricultural, horticultural and domestic habitats ; J Constructed, industrial and other artificial habitats ; X Habitat complexes.
- EUNIS terrestre 2021_1 (xlsx lu) : 7 onglets (Coastal N, Grassland R, Heathland S, Forest T, Sparsely vegetated U, Man-made V, Wetlands Q) ; 3 949 lignes ; niveau 1 : 7 ; niveau 2 : 42 ; niveau 3 : 270 ; niveau 4 : 964. Read me : « Revision is up to level 3, levels below this have been inserted from the EUNIS 2012 dataset. » Colonnes de crosswalk : EUNIS 2012 (relation =, #, <, >), Resolution 4 (Berne), Annex I, Red List, et (janvier 2023) MAES, IUCN, Corine Land Cover, EuroVeg Checklist. « Relationships concern revised EUNIS level 3 only ».

Limites : le crosswalk EEA 2021 vise Corine Land Cover, pas CORINE Biotopes ; la correspondance CORINE Biotopes vers EUNIS 2012 est fournie côté français par HabRef (CRSP_CB_EUNIS_2012_70.xlsx). L'onglet Man-made n'a que les niveaux 1 à 4 (89 lignes). Eaux continentales et complexes non révisés.

CORINE Biotopes (1991) et version française. Source lue : table TYPOREF de HabRef v7 (CD_TYPO 22) : « Cette typologie parue en 1991 (Devillers et al.) comporte 2584 codes répartis en 7 grandes familles de milieux ». Références : « Devillers P., Devillers-Terschuren J., Ledant J.-P. & coll., 1991. CORINE biotopes manual. Habitats of the European Community. Data specifications - Part 2. EUR 12587/3 EN. European Commission, Luxembourg, 300 p. » ; version française : « Bissardon M., Guibal L. & Rameau J.-C., 1997. Corine biotopes. Version originale. Types d'habitats français. ENGREF, Nancy, 217 p. » Statistiques HabRef v7 : 2 594 unités valides, 1 486 présentes ou à rechercher en France. Manuel original non ouvert : NON VÉRIFIÉ.

HabRef (INPN, PatriNat). Accès : page INPN https://inpn.mnhn.fr/telechargement/referentiels/habitats : 403 ; data.gouv.fr (API lue) : « INPN - référentiel des typologies d'habitats, milieux et végétation (Habref) », producteur MNHN, « license: notspecified », dernière mise à jour 2026-10-08 ; avertissement : « À la suite d'une attaque informatique sévère affectant les serveurs du MNHN, certains des sites du MNHN sont inaccessibles pour une durée indéterminée ». Page temporaire PatriNat (lue) : https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353 ; « HabRef | 07 | HABREF.zip » : https://assets.patrinat.fr/files/referentiel/HABREF.zip (29 346 558 octets, téléchargé ; contient HABREF_07.zip, 97 fichiers datés 07/08/2025). Licence : NON VÉRIFIÉ : aucune licence indiquée.

Contenu : HabRef v7 (HABREF_70). Fichiers : HABREF_70.csv, HABREF_DESCRIPTION_70.csv, HABREF_CORRESP_HAB_70.csv, HABREF_CORRESP_TAXON_70.csv, HABREF_LIEN_SOURCES_70.csv, HABREF_SOURCES_70.csv, HABREF_TERR_70.csv, TYPOREF_70.csv, Stats_HABREF_70.csv, et dossier typologies/ (xlsx par typologie TYPO_*.xlsx et correspondances CRSP_*.xlsx). Typologies (nombre d'unités valides) : EUNIS 2012 : 5 282 ; EUNIS 2022 : 5 497 ; CORINE biotopes : 2 594 ; Paléarctique 2001 : 6 228 ; Cahiers d'habitats : 800 ; HIC : 275 ; PVF1 : 712 ; PVF2 : 2 377 ; Eurovegchecklist : 1 855 ; NatHab-Atl : 663 ; NatHab-Med : 177 ; OSPAR : 24 ; Barcelone : 189 ; micro-habitats de l'arbre : 69. Correspondances disponibles : CB vers EUNIS 2012, EUNIS 2012 vers 2022, EUNIS 2022 vers HIC, PVF2 vers CORINE/EUNIS/HIC, CH vers CB. Texte HabRef sur EUNIS 2022 : « Les habitats des zones humides, publiés début 2023, n'ont pas pu être pris en compte et seront intégrés à la prochaine version d'HabRef (v8). » Codes EUNIS 2022 modifiés dans HabRef : « un trait d'union a été ajouté après le code de niveau 2 (exemple : R5-1) ».

Limites : v8 annoncée mais non trouvée ; licence inconnue ; liens PatriNat déclarés temporaires.

Typologies françaises d'habitats urbains ou anthropisés. Vérifié : EUNIS 2012, groupe J « Constructed, industrial and other artificial habitats », niveau 2 : J1 Buildings of cities, towns and villages ; J2 Low density buildings ; J3 Extractive industrial sites ; J4 Transport networks and other constructed hard-surfaced areas ; J5 Highly artificial man-made waters and associated structures ; J6 Waste deposits ; niveau 3 (exemples) : J1.1 Residential buildings of city and town centres ; J1.2 Residential buildings of villages and urban peripheries ; J1.3 Urban and suburban public buildings ; J1.4 Urban and suburban industrial and commercial sites still in active use ; J1.5 Disused constructions ; J1.6 Urban and suburban construction and demolition sites ; J4.2 Road networks ; J4.3 Rail networks ; J4.6 Pavements and recreation areas ; J4.7 Constructed parts of cemeteries ; J5.3 Highly artificial non-saline standing waters. Groupe I (I1 Arable land and market gardens ; I2 Cultivated areas of gardens and parks). EUNIS 2021 groupe V « Vegetated man-made habitats » (niveau 3 lu) : V1 Arable land and market gardens (V11 à V15) ; V2 Cultivated areas of gardens and parks (V21 Large-scale ornamental garden areas ; V22 Small-scale ornamental and domestic garden areas ; V23 Recently abandoned garden areas) ; V3 Artificial grasslands and herb dominated habitats (V31 « Agriculturally-improved, re-seeded and heavily fertilised grassland, including sports fields and grass lawns » ; V37 Annual anthropogenic herbaceous vegetation ; V38 Dry perennial anthropogenic herbaceous vegetation ; V39 Mesic perennial anthropogenic herbaceous vegetation) ; V4 Hedgerows (V41 à V44) ; V5 Shrub plantations (V51 à V54 dont V54 Vineyards) ; V6 Tree dominated man-made habitats (V61 Broadleaved fruit and nut tree orchards ; V62 Evergreen orchards and groves ; V63 Lines of planted trees ; V64 à V66). Les habitats bâtis non végétalisés (ex-J) ne figurent pas dans la révision 2021 lue. Typologies ARB Île-de-France, Cerema, Plante & Cité, LPO : NON VÉRIFIÉ (recherche non effectuée).

#### 2.5.6 Zones biogéographiques

EEA, « Biogeographical regions, Europe 2016, ver. 1 » (publié le 2016-01-26) : https://sdi.eea.europa.eu/catalogue/idp/api/records/c6d27566-e699-4d58-a132-bbe3fe01491b (lue) ; https://www.eea.europa.eu/data-and-maps/data/biogeographical-regions-europe-3 ; téléchargement https://sdi.eea.europa.eu/data/c6d27566-e699-4d58-a132-bbe3fe01491b (SHP, Spatialite) ; service REST https://bio.discomap.eea.europa.eu/arcgis/rest/services/BioRegions/BiogeographicalRegions_WM/MapServer. Licence : « License CC-BY 4.0 », « no limitations to public access ». EPSG:3035, échelle 1:10 000 000. 12 entités : Alpine, Anatolian, Arctic, Atlantic, BlackSea, Boreal, Continental, Macaronesia, Mediterranean, Outside, Pannonian, Steppic. Délimitations officielles utilisées pour la directive Habitats 92/43/CEE.

INPN (https://inpn.mnhn.fr/programme/evaluation/espece/54711, lue) : colonnes « Alpin, Atlantique, Continental, Méditerranéen, Marin atlantique, Marin méditerranéen », soit 4 régions terrestres et 2 marines pour la métropole.

Limites : table de correspondance région biogéographique par département ou commune : NON VÉRIFIÉ : aucune source trouvée. Attribution à la commune possible par intersection SIG avec la couche EEA (1:10 000 000, précision limitée).

#### 2.5.7 Format RSEE de la RE2020 : schéma XSD

Page « Gestion des versions du moteur de calcul « Th-BCE 2020 » et du RSEE » (mise à jour le 23/06/2026) : https://rt-re-batiment.developpement-durable.gouv.fr/gestion-des-versions-du-moteur-de-calcul-th-bce-a688.html (lue intégralement). « Règlement de l'évaluation des logiciels RE2020 » (PDF 16 pages, lu) : https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/reglement_evaluation_logiciels_re2020.pdf.

Contenu : « Un RSEE se compose de 3 parties : DATAS_COMP (Données administratives), RSET (étude énergétique), RSEnv (étude environnementale). » Versions RSET/moteur : 2021.E1.0.0 à 2026.E1.0.0 (01/07/2026) ; versions RSEnv : 2021.C1.0.0 à 2026.C1.0.0 ; versions DATAS_COMP : 2021.D1.0.0 à 2026.D1.0.0. Le règlement d'évaluation (p. 6-7) exige un « RSEE au format XML, conforme à la dernière version du schéma XSD publiée », et mentionne une « conversion XSL » pour l'affichage.

Conclusion : le schéma XSD du RSEE est désigné comme « publié » par le règlement d'évaluation, mais aucun lien de téléchargement d'un fichier .xsd n'a été trouvé sur les pages publiques consultées. NON VÉRIFIÉ : URL du XSD non publiée sur les pages lues. Ce constat rejoint celui d'OpenBCE (`docs/rsee.md`).

#### Sources consultées (2.5)

| Source | URL | Statut |
|---|---|---|
| Décret 2023-1096 (JO) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465959 | lue partiellement |
| Annexe à l'art. R. 101-1 (Legifrance) | https://legifrance.gouv.fr/codes/article_lc/LEGIARTI000048470652 | lue partiellement |
| Art. R. 101-1, R. 101-2, L. 101-2-1, L. 151-22 (Legifrance) | LEGIARTI000048470613, 048469670, 043967077, 053546385 | non accessible (403) ; texte lu dans codes.droit.org |
| Code de l'urbanisme, PDF codes.droit.org (MAJ 2026-09-01) | https://codes.droit.org/PDF/Code%20de%20l%27urbanisme.pdf | lue (articles ciblés) |
| Code de l'environnement, PDF codes.droit.org (MAJ 2026-10-07) | https://codes.droit.org/PDF/Code%20de%20l%27environnement.pdf | lue (articles ciblés) |
| Décret 2022-763 (loda, métadonnées) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000045727061 | métadonnées seulement |
| CE n° 465341 (04/10/2023) | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2023-10-04/465341 | lue |
| Projet de décret et rapport de présentation (consultation 2023) | consultations-publiques.developpement-durable.gouv.fr (2 PDF) | lus intégralement |
| Fiche indicateur Artificialisation (15/05/2024) | https://artificialisation.developpement-durable.gouv.fr/sites/artificialisation/files/inline-files/2024_0122_Fiche_Artificialisation_V5.pdf | lue intégralement |
| Décret 2012-1492 (AIDA Ineris) | https://aida.ineris.fr/reglementation/decret-ndeg-2012-1492-271212-relatif-a-trame-verte-bleue | lue partiellement |
| Berlin BFF (3 pages) et Muster février 2025 | berlin.de (voir ci-dessus) | lues intégralement |
| PLU Eurométropole de Strasbourg (approuvé 06/02/2026) | https://sig.strasbourg.eu/datastrasbourg/plu_media/reglement_actuel.pdf | lue |
| Grand Annecy, fiche technique CBS | https://plui-hmb-approuve-ga.grandannecy.fr/04_REGLEMENT/FICHE_AIDE_instruction_CBS.pdf | lue intégralement |
| Paris, règlement PLU 2019 | https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2022-01/C_REG1-V23.pdf | lue (UG.13.1.2) |
| Paris, PLU bioclimatique | https://plubioclimatique.paris.fr/projet/datas/pdf/REG1.pdf | lue partiellement (tronqué) |
| Cerema, étude coefficients (05/12/2024) et Livrable 2 | planif-territoires.logement.gouv.fr ; nature-en-ville.com | lues |
| London Plan 2021 et UGF guidance 2023 | london.gov.uk (2 PDF) | lues |
| EEA SDI, 3 fiches EUNIS et jeux de données | sdi.eea.europa.eu (records 638330ea, bfe4c237, 566bf5a0, 8a5eccda) | lues intégralement ; xlsx/xls lus |
| BISE habitats | https://biodiversity.europa.eu/resources/search-habitat | lue |
| INPN HabRef (téléchargement) | https://inpn.mnhn.fr/telechargement/referentiels/habitats | non accessible (403) |
| data.gouv.fr HabRef (API) ; PatriNat page temporaire et HABREF.zip v7 | data.gouv.fr ; patrinat.fr ; assets.patrinat.fr | lues ; archive lue (TYPOREF, Stats) |
| EEA Biogeographical regions 2016 (fiche, page, REST) | sdi.eea.europa.eu ; eea.europa.eu ; bio.discomap.eea.europa.eu | lues |
| INPN évaluation (régions biogéographiques) | https://inpn.mnhn.fr/programme/evaluation/espece/54711 | lue partiellement |
| RT-RE bâtiment : gestion des versions, évaluation des logiciels, règlement d'évaluation | rt-re-batiment.developpement-durable.gouv.fr | lues |

### 2.6 Écologie quantitative des modules : aire-espèces et connectivité, lumière, bruit, vitrages, sols et substrats, eau, maturation et échec

Date de consultation : 17/10/2026. Contraintes d'exécution : le quota de recherches web de la session a été épuisé en fin de travail ; plusieurs pages ont été refusées (limitation de débit HTTP 429, protections anti-robots, robots.txt) et sont listées en fin de fiche. Aucune valeur ci-dessous ne provient de mémoire : chaque chiffre a été lu dans un document récupéré, dont l'emplacement est indiqué. Quand une valeur n'a pu être lue, c'est écrit « NON VÉRIFIÉ ».

#### 2.6.1 Connectivité : relation aire-espèces, surface minimale, clôtures, voiries

Sources lues :
- Matthews T.J. et al. 2016, « On the form of species-area relationships in habitat islands and true islands », Global Ecology and Biogeography. PDF auteur (accès libre) : https://research.birmingham.ac.uk/files/46558191/Matthews_et_al_On_the_form_of_species_area_relationships_Global_Ecology_and_Biogeography.pdf . Lu intégralement (texte, tableaux 3 et 4, légendes fig. 3).
- Drakare S., Lennon J.J., Hillebrand H. 2006, « The imprint of the geographical, evolutionary and ecological context on species-area relationships », Ecology Letters 9: 215-227, DOI 10.1111/j.1461-0248.2005.00848.x. Article payant : seul le résumé a été lu. Valeurs de z lues dans 2 sources secondaires : préprint bioRxiv https://www.biorxiv.org/content/10.1101/2020.08.19.257337.full.pdf et Sólymos et Lele 2012 https://ftp-public.abmi.ca/home/publications/documents/356_Solymos_etal_2012-01-01_SpeciesAreaRelationships.pdf .
- Beninde J., Veith M., Hochkirch A. 2015, « Biodiversity in cities needs space: a meta-analysis of factors determining intra-urban biodiversity variation », Ecology Letters 18: 581-592 (DOI 10.1111/ele.12427). PDF auteur : https://www.uni-trier.de/fileadmin/fb6/prof/BIO/Hochkirch/Beninde_et_al-2015-Ecology_Letters.pdf . Lu intégralement.
- Benítez-López A., Alkemade R., Verweij P.A. 2010, « The impacts of roads and other infrastructure on mammal and bird populations: a meta-analysis », Biological Conservation 143: 1307-1316. PDF : https://dspace.library.uu.nl/bitstream/handle/1874/203524/verweij-impacts_2010.pdf?sequence=2 . Lu intégralement.
- Jacobson S.L. et al. 2016, « A behavior-based framework for assessing barrier effects to wildlife from vehicle traffic volume », Ecosphere, DOI 10.1002/ecs2.1345. PDF : https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1143&context=esm_fac . Lu intégralement.
- Buton C. 2023, « Impacts écologiques des clôtures et solutions de remédiation possibles », cabinet X-AEQUO avec le soutien de l'OFB : https://www.trameverteetbleue.fr/sites/default/files/references_bibliographiques/impacts_ecologiques_des_clotures_bp_cpv_2023-07-28.pdf . Lu intégralement. Le document précise lui-même qu'il n'a pas de valeur réglementaire ou normative.
- Bruxelles Environnement 2019, fiche « Clôtures et faune » : https://www.vigienature-ecole.fr/sites/default/files/2021-06/RT_Clotures_faune_FR.pdf . Lu intégralement.
- Loi n° 2023-54 du 2 février 2023 (engrillagement), texte JO : https://sosforetfrance.org/wp-content/uploads/2024/11/Loi-sur-lengrillagement-des-forets-joe_20230203_0029_0001.pdf . Lu. Rapport Sénat n° 149 (2022-2023) : https://www.senat.fr/rap/l22-149/l22-1493.html .
- Cerema 2019, ouvrages et clôtures routières : https://www.corse.developpement-durable.gouv.fr/IMG/pdf/cerema2019_ouvrages_clotures_routieres.pdf . Lu intégralement.
- Carsignol J. (Cerema), présentation « Passages à faune » : https://trameverteetbleue.fr/sites/default/files/Journee_echange/passages_a_faune_j.carsignol.pdf . Lu (diapositives partiellement lisibles).

Relations et valeurs exploitables.

Exposant z (S = cA^z) :
- Matthews et al. 2016, Résultats et tableau 4 : îles d'habitat (fragments terrestres), z médian = 0,22 (Q1-Q3 = 0,16-0,32), 135 jeux de données avec ajustement significatif (R² moyen 0,62) ; 51 jeux ont z > 0,25.
- Matthews et al. 2016, fig. 3b : z médian par type d'île d'habitat : fragments forestiers 0,20 (n = 75), îles urbaines 0,27 (n = 21), sommets montagneux 0,30 (n = 12). Seule la différence forêt / urbain est significative (P = 0,01).
- Matthews et al. 2016, fig. 3a : vraies îles, z médian global 0,29 (Q1-Q3 0,20-0,40) ; fig. 3c : pas de différence significative de z entre taxons.
- Matthews et al. 2016, tableau 4 : Watling et Donnelly 2006, îles d'habitat moyenne 0,20, vraies îles 0,26 ; Triantis et al. 2012, vraies îles moyenne 0,32.
- Matthews et al. 2016, Discussion : « as the intervening matrix becomes more hostile/less permeable, the z value increases » ; le modèle puissance n'est le meilleur (AICc) que pour 24 % des 182 jeux.
- Drakare et al. 2006 (résumé) : méta-analyse de 794 relations aire-espèces ; valeurs rapportées par le préprint bioRxiv : z moyen global 0,27 ; imbriqué 0,36 ; indépendant 0,24. Sólymos et Lele 2012 (p. 115) citent aussi « Drakare et al., 2006, found 0.27 ».
- Sólymos et Lele 2012 (p. 113 et 116) : pente globale moyenne z = 0,228 (limites de confiance à 90 % : 0,059-0,412) ; îles non marines 0,239 ; îles-ponts 0,269 ; océaniques 0,163.

Surface minimale de tache (milieu urbain) :
- Beninde et al. 2015, tableau 3 : 24 seuils de surface publiés, de 1 à 140 ha, moyenne 26,7 ha (± 7,4 ES) ; seuils « haut niveau » (espèces sensibles à la surface) : 53,3 ha ± 12,1 ES (n = 11) ; seuils « bas niveau » (espèces adaptées à la ville) : 4,4 ha ± 0,85 ES (n = 13) ; différence significative (P < 0,001). La recommandation « > 50 ha » de l'article est l'arrondi de la moyenne haute.
- Beninde et al. 2015, tableau 2 : effet résumé de la surface de tache sur la richesse : oiseaux 0,76 (P < 0,0001, n = 10), insectes 0,62 (P < 0,0001, n = 6), plantes 0,52 (P < 0,01, n = 4) ; la distance entre taches (connectivité) est non significative.
- Carsignol (Cerema), diapo 3 : population non viable sans apports extérieurs sous 100 ha ; aire minimale du lièvre > 30 ha (ordres de grandeur, sans source lisible).

Clôtures :
- Loi 2023-54, art. L. 372-1 C. env. : « posées 30 centimètres au-dessus de la surface du sol, leur hauteur est limitée à 1,20 mètre » ; mise en conformité avant le 1er janvier 2027 ; texte visant les espaces naturels, pas les parcelles bâties.
- Buton 2023, p. 21 : ouvertures petite faune « de 20 X 20 cm à 15 X 15 cm, placés tous les 10 à 20 m et dans les angles de clôtures » ; clôture non jointive au sol « p. ex. à 15-20 cm de haut » ; « Laisser au moins 10 cm sous les portillons et portails » ; p. 20 : barreaux de portail espacés de 10 cm au plus ; hauteur totale < 2 m en zone à chevreuils, < 2,60 m en zone à cerfs ; p. 19 : exclos unitaires d'environ 25 ha maximum, couloirs faunistiques d'au moins 20 m de large et au plus 500 m de long ; mailles 5 x 20 cm, mailles souples ≥ 15 cm de large, 7,5-10 cm de haut en bas et jusqu'à 20 cm en haut, mailles fines 5 x 10 cm. Aucun taux de franchissement ni de mortalité par type de clôture.
- Bruxelles Environnement 2019 : ouvertures « de 10 à 20 cm² tous les 15 m » (écriture du document), au moins 1 passage si la clôture fait moins de 15 m ; clôture fixée 10 cm au-dessus du sol.
- Cerema 2019 (clôtures routières) : hauteurs grande faune 1,40 m (standard autoroute), 1,60-2,00 m (chevreuil), 2,45-2,80 m (cerf) (annexe 7, p. 32) ; maille ≤ 101,6 mm sur les 0,50 m du bas (p. 10) ; partie enterrée 30 à 50 cm ; « une descente d'eau de 60 à 80 cm est infranchissable pour la petite faune » (p. 17). Aucun taux d'efficacité.
- Recommandation LPO « 15 x 15 cm » : NON VÉRIFIÉ dans une source LPO ; confirmée dans Buton 2023, p. 21.

Effet barrière des voiries :
- Benítez-López et al. 2010, sections 3.2.1 et 4.1 : abondance relative (MSA) groupée = 0,678 pour les oiseaux (IC95 0,636-0,720) et 0,675 pour les mammifères (IC95 0,608-0,742), soit des baisses de 28-36 % (oiseaux, jusqu'à 2,6 km) et 25-38 % (mammifères, jusqu'à 17 km) ; effets jusqu'à environ 1 km (oiseaux) et 5 km (mammifères) ; petits mammifères affectés « within a few meters ».
- Benítez-López et al. 2010, tableau 1 (oiseaux, MSA par classe de distance) : < 10 m 0,398 ; 15-35 m 0,486 ; 38-65 m 0,534 ; 110-125 m 0,667 ; 380-480 m 0,750 ; 1 000-1 075 m 0,836 ; 1 800-2 000 m 1,000. Tableau 2 (mammifères) : non monotone (30-50 m 0,565 ; 75-100 m 0,396 ; 3 500-4 000 m 0,981).
- Benítez-López et al. 2010, tableau 6 (pentes du modèle MSA ~ log distance, oiseaux) : terres agricoles b = 1,523 ; prairies 1,014 ; milieux non forestiers 1,333 ; forêts 0,826 ; forêts tempérées 0,761. Tableau 7 (mammifères) : non forestier 1,142 ; forêts 0,860 ; forêts tempérées 0,260. Pas d'effet significatif de l'intensité du trafic pour les oiseaux (10 jeux de données).
- Jacobson et al. 2016, tableau 2 : trafic faible < 500 véh/j (AADT), modéré 500-4 999, fort 5 000-9 999, très fort > 10 000 ; aucune espèce ne franchit vraisemblablement au-delà de 35 000 véh/j. Valeurs empiriques citées : évitement par le grizzly dès 10 véh/j ; crapauds 30 % de mortalité à 240 véh/j ; cerf-mulet dévié au-delà de 8 000 véh/j.
- Carsignol, diapo 10 et 12 : buses petite faune Ø 400 à 2 000 mm ou dalots 1 000 x 600 mm ; amphibiens : 1 conduit tous les 30 m, Ø 200-600 mm ; diapo 18 : efficacité des passages croissante « surtout jusqu'à 40-60 m de large ».

Limites : les z de Matthews et al. sont issus de fragments isolés, pas de jardins ou parcs urbains individuellement (21 jeux urbains) ; les seuils de surface de Beninde et al. sont des moyennes de seuils rapportés (I² jusqu'à 93 %) ; les méta-analyses routières portent sur des routes, pas sur des voiries internes ; clôtures : aucune donnée quantitative d'efficacité.

Ce qui manque : un z de référence pour les taches urbaines < 1 ha : NON VÉRIFIÉ (plage 0,16-0,32, médiane urbaine 0,27) ; une relation perméabilité / densité d'ouvertures : NON VÉRIFIÉ ; une relation mortalité / trafic pour les voiries < 500 véh/j : seules des valeurs ponctuelles.

#### 2.6.2 Lumière artificielle (ALAN)

Sources lues :
- Sanders D., Frago E., Kehoe R., Patterson C., Gaston K.J. 2021, « A meta-analysis of biological impacts of artificial light at night », Nature Ecology & Evolution 5: 74-81, DOI 10.1038/s41559-020-01322-x. Manuscrit accepté lu intégralement (dépôt Exeter) : https://ore.exeter.ac.uk/rest/bitstreams/169056/retrieve . Données : https://datadryad.org/dataset/doi:10.5061/dryad.wpzgmsbjn .
- Owens A.C.S., Lewis S.M. 2018, « The impact of artificial light at night on nocturnal insects: a review and synthesis », Ecology and Evolution (PMC6262936) : https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6262936/fullTextXML . Lu intégralement.
- Hale J.D. et al. 2015, « The ecological impact of city lighting scenarios: exploring gap crossing thresholds for urban bats », Global Change Biology : https://pmc.ncbi.nlm.nih.gov/articles/PMC4975606 . Lu intégralement.
- EUROBATS, Doc.AC24.6.Rev.1, groupe de travail « Bats and light pollution » : https://www.eurobats.org/sites/default/files/documents/pdf/Advisory_Committee/Doc.AC24.6.Rev_.1_IWG_Bats_LightPollution.pdf . Lu intégralement.
- Rowse E.G., Harris S., Jones G. 2018, Royal Society Open Science 5: 180205 ; lu via https://www.conservationevidence.com/individual-study/7212 .
- Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses : lu sur https://aida.ineris.fr/reglementation/arrete-271218-relatif-a-prevention-a-reduction-a-limitation-nuisances-lumineuses et copie Legifrance PDF https://www.ville-ballancourt.fr/wp-content/uploads/sites/76/koba-documents/Arrete-du-27-decembre-2018-relatif-a-la-prevention-a-la-reduction-et-a-la-limitation-des-nuisances-lumineuses-Legifrance.pdf . Arrêté modificatif du 24 décembre 2019 lu sur AIDA.
- OFB / UMS PatriNat, guide « Trame noire - Méthodes d'élaboration et outils pour sa mise en oeuvre » : https://trameverteetbleue.fr/sites/default/files/references_bibliographiques/guide_trame_noire_ofb_ums_cpa39_mai.pdf . Lu partiellement.
- Gaston et al. 2013 (Biological Reviews) : NON LU (429).

Relations et valeurs exploitables.

Méta-analyse Sanders et al. 2021 : corpus 126 publications, 1 304 tailles d'effet (Hedges' d) ; 82 études de terrain, 42 de laboratoire ; 746 tailles d'effet vertébrés, 388 invertébrés, 143 plantes, 24 communautés microbiennes. Effets (fig. 2) : taux hormonaux (mélatonine, n = 145) « consistently and markedly reduced » ; début d'activité (n = 52) avancé et fin (n = 23) retardée ; abondance (n = 256) : pas d'effet net fort mais variance très large ; activité des chauves-souris (n = 99) : longue queue d'effets fortement négatifs ; diversité (n = 7) : pas d'effet systématique. Intensité (fig. 3c) : « A meta-regression analysis found no relationship between the intensity of artificial light and effect size magnitude » ; expositions surtout autour de 1-2 lux, jusqu'à 100 lux. Spectre et température de couleur : non analysés. Estimations par catégorie lisibles seulement sur figures : NON VÉRIFIÉ en valeur numérique.

Seuils d'éclairement (lux) lus :
- Owens et Lewis 2018 : accouplement d'Helicoverpa zea requiert < 0,05 lux ; Lampyris noctiluca : parade sous 1,3 lux, jamais active au-dessus de 15 lux ; Photuris congener : 0,25 à 2,5 lux ; « About 30%-40% of insects that approach street lamps die soon thereafter » (Eisenbeis 2006) ; environ 30 % des vertébrés et plus de 60 % des invertébrés sont nocturnes.
- Guide Trame noire (p. 17) : effet attractif sur les insectes dès environ 1 lux ; (p. 16) l'éclairage réduirait d'environ 60 % les visites nocturnes de fleurs et d'environ 10 % la formation des fruits ; (p. 40-41) seuil de sensibilité de chiroptères lucifuges : 21,3 mag/arcsec² ; luminance naturelle du ciel sans lune environ 21,6 mag/arcsec² ; barème : 0 au-dessus de 21,3, -1 entre 20 et 21,3, -2 sous 20 mag/arcsec² ; (p. 39) à Douai, luminaires > 3 000 K cartographiés comme sensibles.
- EUROBATS (p. 4, citant Azam et al. 2018, 27 paires de sites, 0,1-30,2 lx) : attraction limitée à 10 m pour Pipistrellus et Nyctalus ; évitement jusqu'à 25 m (Myotis) et 50 m (Eptesicus serotinus) ; « Illuminance had a negative effect on Myotis sp. below 1 lx » ; recommandations : séparer les luminaires des corridors d'au moins 50 m et éviter tout flux vertical intrusif au-delà de 0,1 lx.
- EUROBATS (p. 5) et Rowse et al. 2018 (21 sites) : niveaux 0 / 25 / 50 / 100 % (11 lux à 25 %, 20 lux à 50 %, 36 lux non gradué) ; à 50 et 100 % l'activité des opportunistes augmente et celle des Myotis diminue ; « the 25% lighting level did not significantly affect either P. pipistrellus or Myotis spp. ».
- Hale et al. 2015 (fig. 4) : seuil barrière (probabilité de franchissement ≤ 5 %) pour P. pipistrellus : « barrier lux = -0.46*crossing distance + 46.2 » (distance de trouée en m) ; 95,6 % des chauves-souris choisissent des trajets plus sombres que la médiane de la trouée ; scénario « Bright City » (routes ≥ 20 lux) : surface accessible autour des mares réduite jusqu'à 7 %.

Arrêté du 27 décembre 2018 (valeurs exactes lues) :
- Art. 2 : patrimoine, parcs et jardins (b) et bâtiments non résidentiels (d) : allumage au plus tôt au coucher du soleil, extinction au plus tard à 1 h ; locaux professionnels : extinction 1 h après fin d'occupation, rallumage au plus tôt à 7 h ou 1 h avant l'activité ; parcs de stationnement (e) : extinction 2 h après cessation d'activité ; chantiers (g) : extinction au plus tard 1 h après cessation d'activité.
- Art. 3 II.1 : ULR nominal « strictement inférieure à 1 % » (a, e) ; sur site strictement inférieur à 4 %. Art. 3 II.2 : code de flux CIE n° 3 > 95 %. Art. 3 II.3 : température de couleur « ne dépasse pas la valeur maximale de 3 000 K » (a, d, e).
- Art. 3 II.4, densité surfacique de flux installé (lm/m²) : a (extérieur) < 35 en agglomération / < 25 hors ; b (parcs et jardins) < 25 / < 10 ; d (bâtiments non résidentiels) < 25 / < 20 ; e (stationnement) < 25 / < 20 ; cheminements et places PMR : éclairement ≤ 20 lux.
- Art. 4 : sites d'observation astronomique : ULR 0 pour b, chantiers ≤ 3 000 K ; réserves naturelles et périmètres de protection : ULR 0 pour b, ≤ 2 400 K pour a à f, ≤ 3 000 K pour g ; coeurs de parcs nationaux : ≤ 2 700 K en agglomération, ≤ 2 400 K hors agglomération ; projecteurs > 100 000 lm et lasers interdits dans les espaces naturels visés.
- Art. 8 : application aux installations nouvelles au 1er janvier 2020 ; luminaires dont l'ULR > 50 % remplacés avant le 1er janvier 2025.

Limites : Sanders et al. : absence de relation dose-effet avec l'intensité ; seuils en lux propres à des espèces précises ; le guide Trame noire ne contient pas de valeurs cibles ; Gaston et al. 2013 non lu.

Ce qui manque : une courbe effet / éclairement au sol : NON VÉRIFIÉ (seule relation numérique lue : Hale et al. pour une espèce) ; l'effet quantifié de la température de couleur : NON VÉRIFIÉ ; une distance d'influence standard : Azam et al. 2018 (via EUROBATS) donnent 10 / 25 / 50 m selon les groupes.

#### 2.6.3 Bruit

Sources lues :
- Shannon G. et al. 2016, « A synthesis of two decades of research documenting the effects of noise on wildlife », Biological Reviews, DOI 10.1111/brv.12207. PDF auteur : https://sites.warnercnr.colostate.edu/wp-content/uploads/sites/146/2020/11/biologicalreviews2015.pdf . Lu intégralement.
- Francis C.D., Barber J.R. 2013, « A framework for understanding noise impacts on wildlife: an urgent conservation priority », Frontiers in Ecology and the Environment : https://scholarworks.boisestate.edu/cgi/viewcontent.cgi?article=1384&context=bio_facpubs . Lu intégralement.
- Reijnen R., Foppen R., Veenbaas G. 1997, « Disturbance by traffic of breeding birds: evaluation of the effect and considerations in planning and managing road corridors », Biodiversity and Conservation 6: 567-581 : https://the-eis.com/elibrary/sites/default/files/downloads/literature/Disturbance%20by%20traffic%20of%20breeding%20birds_1997.pdf . Lu intégralement.

Relations et valeurs exploitables :
- Shannon et al. 2016 : 242 études ; « terrestrial wildlife responses begin at noise levels of approximately 40 dBA » ; « 20% of papers documented impacts below 50 dBA » ; 88 % des études rapportent une réponse biologique ; 14 études documentent des réponses sous 50 dB ; richesse spécifique affectée à ≥ 45 dBA ; réponses entre 52 et 68 dBA ; efficacité de chasse des chauves-souris glaneuses réduite au-dessus de 80 dBA ; niveaux naturels 24 à 40 dB ; tableau 5 : 44-73 dBA pour les changements de fréquence vocale des oiseaux, 85 à 98 dBA pour l'accélération cardiaque chez les ongulés. Fig. 3 (N = 131) : courbes cumulatives « weight of evidence », explicitement « accumulation of evidence, not accumulation of response » ; aucune régression dose-réponse.
- Francis et Barber 2013 : « increases in continuous noise of 5-10 decibels (dB, A-weighted) above baseline can reduce bird numbers » (comptages à peu près divisés par 2, citant Ortega et Francis 2012) ; masquage jusqu'à 0,5-1,0 km ; atténuation de 6 dB par doublement de distance (source ponctuelle), 3 dB (source linéaire) ; murs antibruit : réduction de la surface exposée jusqu'à 70 % (modélisé).
- Reijnen et al. 1997, tableau 3 : seuils de bruit sous lesquels la densité n'est pas affectée : boisement 42-52 dB(A) toutes espèces (36-58 par espèce) ; prairie ouverte 47 dB(A) (43-60 par espèce). Tableau 2, distances d'effet : prairie, 10 000 véh/j : 365 m (par espèce) / 190 m (toutes espèces) ; 50 000 véh/j : 930 / 560 m ; boisement, 10 000 véh/j : 305 / 125 m ; 50 000 véh/j : 810 / 365 m. Réduction de densité dans la zone d'effet « never smaller than 30% » ; densité totale réduite de 39 % (prairie) et 35 % (boisement) ; modèle à seuil ; tampon de planification recommandé environ 1 000 m.

Limites : Shannon et al. mélangent dBA, dB SPL et dB non pondérés ; Reijnen et al. : oiseaux nicheurs des Pays-Bas, routes à fort trafic ; aucune méta-analyse quantitative par dB.

Ce qui manque : une fonction continue réponse = f(LAeq) : NON VÉRIFIÉ ; éléments disponibles : seuil d'apparition 40-50 dBA, seuils par milieu (42-52 et 47 dB(A)), réduction minimale de 30 % au-dessus du seuil, règle de 5-10 dB(A) au-dessus du fond.

#### 2.6.4 Collisions d'oiseaux sur vitrages

Sources lues :
- Loss S.R., Will T., Loss S.S., Marra P.P. 2014, « Bird-building collisions in the United States: estimates of annual mortality and species vulnerability », The Condor 116: 8-23, DOI 10.1650/CONDOR-13-090.1 : https://media.audubon.org/documents/loss_et_al_bird-building_collisons_condor_2014.pdf . Lu intégralement.
- Hager S.B. et al. 2017, « Continent-wide analysis of how urbanization affects bird-window collision mortality in North America », Biological Conservation 212: 209-215 : https://blogs.hope.edu/wp-content/uploads/sites/32/2017/07/BirdWindowCollisions_July2017.pdf . Lu intégralement.
- Klem D. Jr., Saenger P.G. 2013, « Evaluating the effectiveness of select visual signals to prevent bird-window collisions », Wilson Journal of Ornithology 125(2): 406-411 : https://www.birdsavers.com/product_images/WilsonJournalOfOrnithology-KlemAndSaenger.pdf . Lu intégralement.
- Schmid H. et al., Schweizerische Vogelwarte, « Vogelfreundliches Bauen mit Glas und Licht » (copie NABU) : https://www.nabu.de/imperia/md/content/nabude/vogelschutz/221212-broschuere-vogelfreundliches-bauen.pdf . Lu intégralement.
- Wiener Umweltanwaltschaft 2022, « Vogelanprall - Muster » : https://wua-wien.at/images/stories/publikationen/wua-vogelanprall-muster-2022.pdf . Lu intégralement.
- Rössler M. 2010, rapports d'essais en tunnel de vol, Hohenau-Ringelsdorf : https://www.bund-nrw.de/fileadmin/nrw/dokumente/Naturschutz/Vogelschlag/Literatur/Roessler_2010_-_Vermeidung_von_Vogelanprall_an_Glasflaechen_-_Pr%C3%BCfberichte_-_Biologische_Station_Hohenau-Ringelsdorf.pdf . Lu intégralement.
- Stadt Nürnberg 2023, « Merkblatt Vogelschlag an Glas » : https://www.nuernberg.de/imperia/md/umweltamt/dokumente/tiere_pflanzen/merkblatt_vogelschlag_glas_2023.pdf . Lu intégralement.
- American Bird Conservancy, « Testing & research » : https://abcbirds.org/strategies/testing-research/ . Lue.
- LEED Pilot Credit SSpc55 « Bird Collision Deterrence » (LEEDuser) : https://leeduser.buildinggreen.com/credit/Pilot-Credits/SSpc55 . Lue.

Relations et valeurs exploitables.

Mortalité par bâtiment et par an (Loss et al. 2014) : 365 à 988 millions d'oiseaux par an aux États-Unis (médiane 599 millions) ; 23 études ; répartition : environ 56 % immeubles bas (4-11 étages), 44 % résidences (1-3 étages), < 1 % tours (≥ 12 étages). Tableau 3 : résidences : 2,1 oiseaux/bâtiment/an (IC95 1,3-3,1) ; immeubles bas : 21,7 oiseaux/bâtiment/an (IC95 5,9-55) ; tours : 24,3 oiseaux/bâtiment/an (IC95 5-76). Facteurs de risque : la mortalité augmente avec le pourcentage et la surface de façade vitrée, la présence et la hauteur de la végétation, et la lumière émise ; aucune taille d'effet chiffrée. Hager et al. 2017 (40 campus, 281 bâtiments, 324 cadavres sur 21 jours ; surface vitrée médiane 156 m²) : meilleur modèle : taille du bâtiment (composante chargée par surface vitrée 0,92, surface de plancher 0,94, étages 0,78) coefficient 0,94 (ES 0,08), urbanisation 0,12, interaction -0,28 ; la végétation locale n'est pas retenue comme facteur important. Vogelwarte, p. 6 : environ 100-115 millions d'oiseaux/an en Allemagne ; p. 12 : arbres de plus de 2 étages à proximité : risque multiplié par 3,6 ; p. 11 : un miroir argenté est percuté 3 fois plus souvent qu'un simple vitrage non traité. Nürnberg 2023 : plus de 4 victimes pour 100 m de façade = forte probabilité (seuil LAG VSW) ; réflexion extérieure maximale 15 % recommandée.

Réflexion (Vogelwarte p. 10-11) : float non traité 8 % de réflexion ; films solaires souvent 25 %, jusqu'à 60 % ; miroir argenté 80-90 % ; même 2 % de réflexion produit des reflets réalistes.

Efficacité des marquages (tunnel de vol) :
- Classes d'efficacité (Vogelwarte tableau 2 p. 29 ; WUA 2022 ; Rössler 2010 tableau 1) : A « hoch wirksam » ≤ 10 % des oiseaux vers la vitre marquée ; B > 10-20 % ; C > 20-42 % ; D > 42 % ; au moins 80 vols d'essai ; norme ONR 191040 : « Vogelschutzglas » si au moins 90 % des oiseaux évitent le marquage.
- Règles dimensionnelles (Vogelwarte p. 30-31) : espacement maximal des bandes horizontales 50 mm, verticales 100 mm, points 90 mm ; largeurs minimales : bandes horizontales 3 mm, verticales 5 mm, points 9 mm ; taux de couverture : marquages semi-transparents 11 % dans le cas idéal, films semi-transparents ≥ 20 %, marquages métalliques efficaces sous 1 % de couverture.
- WUA 2022 : « unmarkierte Stellen von mehr als 5x10 cm (HxB) veranlassen Vögel zum Durchfliegen » (règle 5 x 10 cm) ; bandes de 3 mm tous les 50 mm suffisent ; points adhésifs 1,2-2 cm, écart maximal 9 cm ; marquages UV non conformes aux essais (Birdpen 54 %, birdsticker 47 %, Ornilux Mikado 37 % d'approches).
- Rössler 2010, tableau 9 (584 essais, 30 espèces) : points noirs 27 % de couverture 2,47 % (A) ; 2 rangées de points 10 % de couverture 5,19 % (A) ; bandes verticales 3,5-5 mm, 8,5 % de couverture 10,11 % (B) ; lignes horizontales 2 mm (6,7 %) 11,63 % (B) ; lignes verticales 2 mm 25,00 % (C).
- Klem et Saenger 2013, expérience 2 (68 jours) : 112 impacts : vitre claire témoin 69, ORNILUX Mikado 31, cordes verticales à 10,8 cm 7, cordes à 8,9 cm 5 (P < 0,001) ; ORNILUX : 55 % d'impacts en moins que le témoin ; films extérieurs antérieurs : réduction ≥ 59 % (Klem 2009b cité).
- Nürnberg 2023 : ≥ 25 % de couverture pour des points ≥ 7,5 mm ; ≥ 15 % pour des motifs linéaires ; lignes horizontales à 5 cm d'écart ≥ 3 mm ; verticales 5 mm à 10 cm ; surfaces non marquées ≤ une paume de main.
- ABC : Threat Factor = pourcentage d'oiseaux volant vers le matériau testé (≥ 80 essais) ; « bird-friendly » si TF ≤ 30, soit « a conservative estimated reduction of collisions of at least 50% under real-world conditions ». La règle « 2 x 4 pouces » n'apparaît pas sur la page lue : NON VÉRIFIÉ chez ABC (équivalent lu : 5 x 10 cm, WUA et Vogelwarte).

Référentiels : LEED Pilot Credit 55 (fermé aux inscriptions le 12 août 2022) : Bird Collision Threat Rating total ≤ 15 ; zone 1 = 36 premiers pieds au-dessus du sol + 12 pieds au-dessus d'une toiture végétalisée, pondérée 2 fois ; BCTR = (surface pondérée zone 1 + zone 2) / (2 x surface zone 1 + surface zone 2) ; zone 1 : au plus 15 % de la façade avec TF > 75 ; éclairage extérieur non indispensable éteint de minuit à 6 h ; suivi post-construction de 3 ans.

Limites : taux par bâtiment américains (IC très larges) ; essais en tunnel = choix d'approche, pas mortalité in situ.

Ce qui manque : une relation mortalité = f(surface vitrée, réflexion, distance à la végétation) chiffrée : NON VÉRIFIÉ (facteur 3,6 pour les arbres hauts et 3 pour les miroirs) ; un facteur de réduction par classe de traitement validé en conditions réelles : « ≥ 50 % » d'ABC pour TF ≤ 30 et 55 % / ≥ 59 % de Klem.

#### 2.6.5 Sol : imperméabilisation, substrat sur dalle et toiture

Sources lues :
- Commission européenne 2012, « Guidelines on best practice to limit, mitigate or compensate soil sealing », SWD(2012) 101 ; version italienne lue intégralement : https://ance.it/wp-content/uploads/archive/17048-ENV-12-009_MEP_IT_final_LR-pdf.pdf .
- O'Riordan R. et al. 2021, « The effects of sealing on urban soil carbon and nutrients », SOIL 7: 661-675, DOI 10.5194/soil-7-661-2021 : https://soil.copernicus.org/articles/7/661/2021/soil-7-661-2021.pdf . Lu intégralement.
- Cerema (Neaud C., Martin M., Monod K., Branchu P.) octobre 2024, « Livrable 3 - Pleine terre » pour la DGALN/DHUP : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable3_PleineTerre_VF%20%281%29.pdf . Lu intégralement.
- DRIEAT Île-de-France, fiche « pleine terre dans les PLU » : https://www.drieat.ile-de-france.developpement-durable.gouv.fr/IMG/pdf/fiche_plu_pleine_terre_vfinale.pdf . Lue intégralement.
- DRIEAT / Cerema, synthèse du guide ERC imperméabilisation des sols : https://www.drieat.ile-de-france.developpement-durable.gouv.fr/IMG/pdf/synthese-guide-erc-impermeabilisation-des-sols.pdf . Lue intégralement.
- Cerema janvier 2023, « Sols et changement climatique » : https://www.afes.fr/wp-content/uploads/2024/04/Cerema_SOLS_ChangementClimatique-Janvier2023.pdf . Lu partiellement.
- a'urba juillet 2022, rapport désimperméabilisation : https://www.aurba.org/wp-content/uploads/2023/07/aurba_2023_desimpermeabilisation_rapport.pdf . Lu partiellement.
- ARB Île-de-France 2021, synthèse « Écologie des toitures végétalisées » (programme GROOVES) : https://biodiversite.educagri.fr/files/EcologieDesToituresVegetalisees2021Syn_fichier_arb-idf_-_ecologie_des_toitures_vegetalisees_-_web_bdef.pdf . Lue intégralement. Note rapide Institut Paris Region n° 890 : https://data.iau-idf.fr/fileadmin/DataStorage/user_upload/NR_890_web_1_.pdf . Rapport arthropodes GROOVES (Hamon G.) : https://data.iau-idf.fr/fileadmin/DataStorageKit/ARB/Publications/rapport_arthropodes_guillaume_hamon.pdf . Lu intégralement.
- Brenneisen S. 2006, « Space for urban wildlife: designing green roofs as habitats in Switzerland », Urban Habitats 4(1) : https://www.eaglehill.us/urban-habitats/Vol%204/wildlife_pdf.pdf . Lu intégralement.
- Molineux C.J., Gange A.C., Connop S.P., Newport D.J., manuscrit révisé 2015 (Ecological Engineering) : https://repository.uel.ac.uk/download/5ada5822bd79e505f95da45b10269f64951aa98d49b1360f887a139844befb1e/414976/EcolEng%20Mnuscript%20with%20revisions.pdf . Lu intégralement.
- Williams N.S.G., Lundholm J., MacIvor J.S. 2014, « Do green roofs help urban biodiversity conservation? », Journal of Applied Ecology, DOI 10.1111/1365-2664.12333 : résumé seulement.
- Filazzola A., Shrestha N., MacIvor J.S. 2019, « The contribution of constructed green infrastructure to urban biodiversity: a synthesis and meta-analysis », Journal of Applied Ecology, DOI 10.1111/1365-2664.13475 : résumé et billet de blog seulement.

Relations et valeurs exploitables.

Imperméabilisation et fonctions du sol :
- CE 2012 (section 2.2, p. 12-13) : artificialisation UE 1990-2000 environ 1 000 km²/an ; 2000-2006 : 920 km²/an ; surface imperméabilisée 2006 : environ 100 000 km², 2,3 % du territoire de l'UE, 200 m² par habitant ; section 3 : un sol fonctionnel retient jusqu'à 3 750 t d'eau/ha ; section 7.1 : couche décapée pour revêtements perméables souvent ≥ 30 cm.
- O'Riordan et al. 2021 (horizon 0-10 cm) : sol scellé non remanié : stock de carbone total inférieur de 37 % aux espaces verts (3,10 vs 4,92 kg/m²), matière organique inférieure de 55 % ; densité apparente 1,50 vs 0,86 g/cm³ ; azote total 81,20 vs 115,44 g/m² ; phosphore 39,62 vs 62,62 g/m² ; littérature citée : réductions de carbone de 66 % (New York), 68 % (Chine), 61,86 % (Alabama/Géorgie) ; stocks à 50-100 cm inférieurs de 25 % sous sol scellé. Aucune donnée faune du sol.
- Cerema 2023 (p. 44) : « les sols artificialisés représentent plus de 9 % du territoire dont deux tiers sont imperméabilisés » ; (p. 33) « quelques centimètres sont nécessaires au développement d'une couverture herbacée », un arbre plus d'1 m. a'urba 2022 (p. 20) : artificialisation 9 % du territoire métropolitain en 2018, « constitués pour 44 % de surfaces imperméables ».
- Cerema Livrable 3 (p. 10) : pleine terre = au moins 2 horizons et profondeur « suffisamment profond (> 30 cm) » ; (p. 8) les sols abriteraient près de 60 % de la biodiversité terrestre.

Coefficients de biotope (valeurs lues) :
- Cerema Livrable 3 (p. 24-25, 32) : pondérations observées : surfaces semi-perméables 0,15 à 0,5 ; espaces verts sur dalle ou toiture 0,1 à 1 « en fonction de l'épaisseur du substrat » (aucun seuil chiffré) ; façades 0,1 à 0,5 ; plafonds recommandés par le Cerema : semi-perméable 0,1 (au lieu de 0,3), façades 0,3 (au lieu de 0,5), dalles/toitures 0,5 (au lieu de 0,7) ; objectifs CBS en zone Ua : 0,2 (Grand Dax), 0,3 (Avignon, Strasbourg), 0,5 à 0,8 (Grand Lac selon la taille de l'unité foncière).
- DRIEAT fiche pleine terre (p. 2, exemple) : A = 0,3 (toitures et façades végétalisées), B = 0,6 (dalles végétalisées), C = 0,5 (surfaces perméables), D = 1 (pleine terre) ; (p. 6) SDRIF et SCoT du Grand Paris : minimum 30 % de pleine terre dans les espaces urbanisés hors voirie.
- DRIEAT synthèse ERC : compensation d'imperméabilisation en milieu urbain « majorée à hauteur de 150 % de la surface impactée » ; équivalences : pleine terre (parc, jardin de pluie, noue) 1 : 1 ; perméable déconnecté végétalisé (toiture végétalisée) 1 : 0,5 ; perméable déconnecté non végétalisé (enrobé poreux) 1 : 0,1.

Toitures végétalisées : épaisseur et biodiversité :
- GROOVES synthèse 2021 (p. 11-13) : 36 toitures du Grand Paris : 18 extensives (substrat < 15 cm), 6 semi-intensives (15-30 cm), 8 intensives (> 30 cm), 4 wildroofs ; épaisseur moyenne environ 20 cm ; (p. 20-27) plus de 400 espèces végétales, 292 dans les carrés Vigie-Flore, environ 70 % spontanées ; « La richesse floristique cesse d'augmenter au-delà d'environ 25 cm de substrat » ; relation négative surface de toiture / richesse en plantes spontanées ; effet positif de la hauteur du bâtiment jusqu'à environ 10 m puis stagnation de la flore et baisse des pollinisateurs ; (p. 31-35) 611 espèces d'invertébrés, de 20 à 107 par site ; pollinisateurs : semi-intensives et intensives comparables aux espaces verts urbains, extensives en dessous ; (p. 24) diversité végétale en moyenne similaire aux friches et parcs urbains.
- Note rapide n° 890 : seuil « jusqu'à 25 cm d'épaisseur » pour la flore (« autour de 30 cm ») ; toitures extensives « en moyenne 50 % moins performantes » que les semi-intensives et intensives sur les services évalués ; rétention d'eau de 6 L/m² (3,5 cm) à 532 L/m² (100 cm).
- Rapport arthropodes GROOVES (Hamon) : 458 espèces, 36 toitures ; richesse moyenne par type (fig. 7, p. 14) : wildroof 19, extensive 32, semi-intensive 55, intensive 59 ; hauteur du bâtiment non significative (p = 0,3156), surface non significative (p = 0,5801) ; Homoptères : richesse croissante avec la hauteur de substrat (p < 0,05) ; irrigation vs pluie : -8,419 espèces (IC95 -11,756 à -5,082).
- Brenneisen 2006 : toit Rhypark (Bâle) : 79 espèces de coléoptères et 40 d'araignées, dont 13 et 7 inscrites en listes rouges ; profondeurs testées 6, 12 et 20 cm ; Wollishofen : 15 cm de terre locale sur 5 cm de gravier, 175 espèces végétales dont 9 orchidées ; vers de terre absents faute d'épaisseur.
- Molineux et al. : passage de 5,5 à 8 cm de substrat : richesse spécifique supérieure (P < 0,01), mais seulement pour certains agrégats.
- Williams et al. 2014 (résumé) : les toitures « largely support generalist species particularly insects » ; « it is premature for policymakers to consider green roofs equivalent to ground-level urban habitats ».
- Filazzola et al. 2019 (résumé) : 33 études méta-analysées ; toitures végétalisées > toits nus ; noues > bords de route ; murs végétalisés = murs. Tailles d'effet : NON VÉRIFIÉ.

Limites : aucune source lue ne donne de coefficient d'infiltration par type de revêtement ; O'Riordan et al. : un site, pas de faune ; GROOVES : 36 toitures, plateau à 25 cm sans équation.

Ce qui manque : une fonction richesse ou abondance = f(épaisseur de substrat) : NON VÉRIFIÉ au-delà du plateau à environ 25-30 cm et des classes 19 / 32 / 55 / 59 espèces d'arthropodes ; la valeur écologique des espaces verts sur dalle selon l'épaisseur : NON VÉRIFIÉ (seule la plage 0,1 à 1 des CBS a été lue) ; faune du sol sous imperméabilisation : NON VÉRIFIÉ.

#### 2.6.6 Eau : mares, zones humides créées, infiltration

Sources lues :
- Williams P., Whitfield M., Biggs J. 2008, « How can we make new ponds biodiverse? A case study monitored over 7 years », Hydrobiologia 597: 137-148, DOI 10.1007/s10750-007-9224-9 : résumé lu sur https://link.springer.com/article/10.1007/s10750-007-9224-9 .
- Freshwater Habitats Trust, « Pinkhill Meadow - what are the ponds like after 30 years? » : https://freshwaterhabitats.org.uk/?p=2705 . Lue.
- Williams P. et al., « Nature based measures increase freshwater biodiversity in agricultural catchments » (préprint bioRxiv 10.1101/672915 ; Biological Conservation 2020) : https://www.biorxiv.org/content/10.1101/672915v1.full.pdf . Lu intégralement. Communiqué Université d'York (10 juin 2020) : https://york.ac.uk/news-and-events/news/2020/research/ponds-boost-wildlife .
- Freshwater Habitats Trust, « New ponds support quarter of wetland plants - Million Ponds Project » (11 février 2016) : https://freshwaterhabitats.org.uk/news/new-ponds-support-quarter-of-wetland-plants-million-ponds-project/ .
- Freshwater Habitats Trust / Knepp, « A strategy for clean water pond creation » : https://knepp.co.uk/wp-content/uploads/2022/01/A-strategy-for-clean-water-pond-creation-Knepp.pdf . Lu intégralement.
- Moreno-Mateos D. et al. 2012, « Structural and functional loss in restored wetland ecosystems », PLoS Biology, DOI 10.1371/journal.pbio.1001247 : https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001247 . Lu intégralement.

Relations et valeurs exploitables :
- Williams et al. 2008 (résumé) : mosaïque de 3,2 ha d'environ 40 mares (Pinkhill Meadow) « colonized by approximately 20% of all UK wetland plant and macroinvertebrate species over the 7-year survey period » ; 8 espèces d'invertébrés Nationally Scarce.
- FHT Pinkhill 30 ans : 40 mares creusées en 1990-91 ; richesse en plantes de zones humides « plateauing at around 70 plant species » ; invertébrés aquatiques « plateaued at just over 100 species » ; seuils « Priority Pond » : ≥ 30 espèces de plantes de zones humides ou ≥ 50 macro-invertébrés ; la richesse en invertébrés a diminué dans 3 des 4 mares suivies.
- Williams et al. 2020 (préprint, 3 bassins d'environ 10 km², suivi 2010-2018) : les mares d'eau propre âgées de 5 ans ajoutent 13 espèces aux 60 des plans d'eau préexistants, soit +22 % de richesse gamma ; gain tendanciel +26 % (p < 0,05) ; espèces rares : de 4 à 12 ; en l'absence de mesures, richesse gamma en baisse de 10 % sur 9 ans ; mares d'interception (eaux de ruissellement) : richesse similaire aux mares existantes, peu d'espèces rares ; les mares atteignent en général leur richesse maximale dans les 5 premières années puis déclinent.
- FHT Million Ponds 2016 : 130 mares neuves de 4 ans dans l'Oxfordshire abritaient 25 % des espèces de plantes de zones humides du Royaume-Uni.
- Knepp / FHT (p. 3-4, 10-11) : 1 mare sur 5 en paysage semi-naturel abrite au moins 1 espèce Red Data Book contre 1 sur 100 dans la campagne ordinaire ; 80 % des mares britanniques en mauvais ou très mauvais état ; « The majority of pond plant and animal species live in less than 10cm of water » ; gradients de profondeur 0,2 à 1 m et de surface 1 à environ 1 000 m² recommandés.
- Moreno-Mateos et al. 2012 : vertébrés convergents en environ 5 ans ; macro-invertébrés 5-10 ans ; plantes environ 30 ans pour converger statistiquement, encore sous la référence à 100 ans ; les zones humides créées approchent la référence plus vite que les restaurées ; grandes zones humides (> 100 ha) récupèrent plus tôt ; hydrologie récupérée immédiatement.
- Infiltration des eaux pluviales et biodiversité (noues, jardins de pluie) : Filazzola et al. 2019 (résumé) : noues > bords de route conventionnels, sans valeur chiffrée ; DRIEAT ERC : équivalence noue/jardin de pluie = pleine terre 1 : 1 (valeur de compensation, pas écologique). Part infiltrée vs biodiversité : NON VÉRIFIÉ.

Limites : Pinkhill est un site exceptionnel ; mares agricoles d'eau propre ; chronoséquences courtes.

Ce qui manque : une courbe richesse = f(âge de la mare) avec intervalle (bornes lues : pic dans les 5 premières années ; plateau à 70 plantes / 100 invertébrés après 25 ans) ; la distinction bassin de rétention vs mare d'eau propre, seulement qualitative ; noues et jardins de pluie : aucune valeur : NON VÉRIFIÉ.

#### 2.6.7 Temps : maturation des habitats créés ou restaurés, taux d'échec

Sources lues :
- Jones H.P. et al. 2018, « Restoration and repair of Earth's damaged ecosystems », Proceedings of the Royal Society B, DOI 10.1098/rspb.2017.2577 ; texte intégral lu via Europe PMC (PMC5832705) : https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5832705/fullTextXML .
- Moreno-Mateos et al. 2012 (voir 2.6.6). Lu intégralement.
- Curran M., Hellweg S., Beck J. 2014, « Is there any empirical support for biodiversity offset policy? », Ecological Applications 24: 617-632, DOI 10.1890/13-0243.1 : résumé lu via https://edoc.unibas.ch/34302 et https://marineinfo.org/id/publication/390905 .
- Spake R. et al. 2015, « A meta-analysis of functional group responses to forest recovery outside of the tropics », Conservation Biology 29: 1695-1703, DOI 10.1111/cobi.12548 : https://pmc.ncbi.nlm.nih.gov/articles/PMC4973697 . Lu intégralement.
- zu Ermgassen S.O.S.E. et al. 2019, « The ecological outcomes of biodiversity offsets under 'no net loss' policies: a global review », Conservation Letters, DOI 10.1111/conl.12664 : résumé lu (DOAJ) : https://doaj.org/article/c91e9c4a347c443fa85a6c708bd8e04e .
- Weissgerber M., Roturier S., Julliard R., Guillet F. 2019, « Biodiversity offsetting: certainty of the net loss but uncertainty of the net gain », Biological Conservation 237: 200-208, DOI 10.1016/j.biocon.2019.06.036 : résumé lu ; texte intégral non accessible.
- Sénat, rapport de la commission d'enquête n° 517 (2016-2017) sur la réalité des mesures de compensation (rapporteur R. Dantec) : tome I lu partiellement : https://www.senat.fr/rap/r16-517-1/r16-517-1_mono.html .
- DREAL Auvergne-Rhône-Alpes 2018, rapport de suivi des mesures ERC : https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/IMG/pdf/rapport2018_dreal_suivi_erc_final.pdf . Lu partiellement.
- Rapports CGDD et Cour des comptes sur l'efficacité des mesures compensatoires : NON LUS (quota épuisé).

Relations et valeurs exploitables.

Trajectoires et taux de récupération :
- Jones et al. 2018 : 400 études, 5 142 variables de réponse ; état de départ médian à 10 % de la référence ; les écosystèmes « rarely recovered to reference conditions » ; forêts et prairies les plus proches de la récupération, lacs et rivières les plus loin ; taux de récupération le plus souvent entre 1 et 10 % par an, médiane 2,9 %/an ; le taux diminue de 0,026 % par an écoulé (« Recovery rates slowed down with time ») ; herbacées plus rapides que ligneux ; niveaux trophiques supérieurs plus rapides ; restauration active non associée à une récupération plus complète ni plus rapide que la récupération passive (p > 0,30, 16 études, 436 variables) ; la moitié du jeu de données a ≤ 10 ans de récupération.
- Moreno-Mateos et al. 2012 : à 100 ans, structure biologique en moyenne 26 % sous la référence (soit 77 % de la référence) et fonctionnement biogéochimique 23 % sous la référence ; fonctions biogéochimiques à 50-100 ans : 74 % de la référence ; stockage de carbone inférieur de 50 % à 20 ans ; matière organique du sol 62 % de la référence à 20-30 ans ; climat tempéré : fonctions à 79 % à 30 ans (83 études, 302 zones humides) ; climat froid : 53 % à 50 ans ; fluviales et tidales : récupérées à 20 et 30 ans ; dépressionnaires : non récupérées à 50 ans.
- Curran et al. 2014 (résumé) : 108 études, 1 228 sites de forêt secondaire, 716 sites de forêt ancienne ; « in the best case, species richness converges to OG reference values within a century » ; similarité de Sørensen environ 2 fois plus longue ; similarité de Morisita-Horn des centaines à des milliers d'années ; la restauration active accélère la convergence (facteur non chiffré) ; conclusion : la compensation par restauration entraîne une perte nette.
- Spake et al. 2015 : champignons ectomycorhiziens : 90 ans pour retrouver la richesse des forêts anciennes (plage 45 ans à jamais) ; lichens épiphytes : 180 ans pour atteindre 90 % ; coléoptères saproxyliques : environ 60 ans pour 90 %.

Taux d'échec et efficacité des compensations :
- zu Ermgassen et al. 2019 (résumé) : 15 715 articles passés en revue, 32 rapports évaluant des résultats écologiques, > 300 000 ha de compensations ; « Approximately one-third of NNL policies and individual biodiversity offsets reported achieving NNL » ; « none of four studies demonstrated successful NNL outcomes for forested habitats or species ».
- Weissgerber et al. 2019 (résumé) : 24 projets d'infrastructures en France ; sur 577 ha destinés à compenser, seulement 3 % étaient artificialisés avant les travaux de compensation et environ 81 % étaient des habitats semi-naturels ; gains « relatively uncertain » face à des pertes certaines.
- Sénat 2017, tome I : A65 : surface de compensation réévaluée de 65 ha à 1 372 ha ; LGV Tours-Bordeaux : « dette » initiale de 25 000 ha ramenée à 3 500 ha ; outarde canepetière : 50 ha prévus, 702 ha fixés ; coûts : haie 12 €/ml, mare 10-12 €/m², fauche tardive 450-670 €/ha, gel de prairie 600 €/ha ; durées contractuelles agricoles 5 à 25 ans. Aucun pourcentage de mesures réalisées ou d'échec dans les parties lues.
- DREAL AURA 2018 : une centaine de dossiers ; « peu de suivis des mesures compensatoires sont disponibles » ; recommandations : suivi minimal 5 ans, « un suivi minimum sur 8 à 10 ans est fortement conseillé », effets d'une gestion visibles sur au moins 15 ans alors que « les conventions sont souvent de 5 ans renouvelables ». Aucun taux d'échec chiffré.
- Taux d'échec des créations de milieux en France (haies, vergers, prairies, mares) : NON VÉRIFIÉ.

Limites : Jones et al. : pas de pourcentage global de la référence atteint à 10, 20 ou 50 ans dans le texte ; Moreno-Mateos : zones humides seulement ; Curran et al. et Weissgerber et al. : résumés seulement ; les sources françaises lues ne fournissent pas de taux d'échec.

Ce qui manque : une courbe « % de la référence atteint » à 10, 20, 50 ans par type d'habitat : partiellement disponible pour les zones humides (74-77 % à 50-100 ans ; 79 % à 30 ans en climat tempéré pour les fonctions) ; pour les forêts, des bornes (richesse ~100 ans, composition plusieurs siècles) ; pour prairies, haies, vergers : NON VÉRIFIÉ ; un taux d'échec des créations : seul le « environ un tiers de succès » de zu Ermgassen et al. ; un coefficient d'efficacité de la restauration active : Jones et al. n'en trouvent pas, Curran et al. en trouvent un : contradiction à arbitrer avec les textes intégraux.

#### Sources consultées (2.6)

Lues intégralement : Matthews et al. 2016 (PDF Birmingham) ; préprint bioRxiv 2020.08.19.257337 ; Sólymos et Lele 2012 ; Beninde et al. 2015 ; Benítez-López et al. 2010 ; Jacobson et al. 2016 ; Buton 2023 ; Bruxelles Environnement 2019 ; loi 2023-54 (JO) ; Cerema 2019 clôtures ; Sanders et al. 2021 (manuscrit Exeter) ; Owens et Lewis 2018 ; Hale et al. 2015 ; EUROBATS Doc.AC24.6.Rev.1 ; arrêté du 27 décembre 2018 (AIDA et copie PDF) ; arrêté du 24 décembre 2019 (AIDA) ; Shannon et al. 2016 ; Francis et Barber 2013 ; Reijnen et al. 1997 ; Loss et al. 2014 ; Hager et al. 2017 ; Klem et Saenger 2013 ; Vogelwarte (NABU) ; WUA 2022 ; Rössler 2010 ; Nürnberg 2023 ; CE 2012 (version italienne) ; O'Riordan et al. 2021 ; Cerema Livrable 3 ; DRIEAT fiche pleine terre ; DRIEAT synthèse ERC ; GROOVES synthèse 2021 et rapport arthropodes ; Brenneisen 2006 ; Molineux et al. ; Williams et al. 2020 (bioRxiv) ; Knepp / FHT ; Moreno-Mateos et al. 2012 ; Jones et al. 2018 (Europe PMC) ; Spake et al. 2015.

Lues partiellement ou résumé seulement : Drakare et al. 2006 ; Carsignol (Cerema) ; rapport Sénat n° 149 ; guide Trame noire OFB ; Rowse et al. 2018 (Conservation Evidence) ; ABC testing ; LEED SSpc55 ; Cerema 2023 sols ; a'urba 2022 ; Note rapide 890 ; Williams et al. 2014 ; Filazzola et al. 2019 ; Williams et al. 2008 ; FHT Pinkhill et Million Ponds ; Curran et al. 2014 ; zu Ermgassen et al. 2019 ; Weissgerber et al. 2019 ; Sénat n° 517 ; DREAL AURA 2018.

Non accessibles : Legifrance (loi 2023-54, arrêté 2018) ; plaquettes OFB engrillagement ; HAL (Azam 2018, Weissgerber 2019, Jones 2018) ; Wiley et BES (Hale, Williams 2014, Filazzola, Gaston 2013, Curran) ; PMC (reCAPTCHA) ; Europe PMC (429 sur plusieurs requêtes) ; page Berlin BFF (depuis cet agent) ; rapports CGDD et Cour des comptes (non identifiés).

### 2.7 Méthodes françaises de dimensionnement ERC, guide ARB îdF 2026, BiodiverCity, règlement restauration de la nature, ISO TC 331, coefficients de biotope, textes récents

Date de consultation de toutes les sources : 17/10/2026.
Règle appliquée : aucune valeur de mémoire. Chaque valeur citée a été lue dans un document téléchargé et extrait (PDF) ou dans une page web récupérée. Quand une source officielle n'a pas pu être ouverte, la mention "NON VÉRIFIÉ : page non accessible" est portée.

Fichiers de travail (PDF et textes extraits) : dossier `sources/cadre_fr/` du projet (voir § 6).

---

#### 1. Approche standardisée du dimensionnement de la compensation écologique (CGDD, OFB, Cerema, 2021) et documents associés

##### Objet
- Guide national qui fixe un cadre de conformité pour le dimensionnement des mesures de compensation (étape "C" de la séquence ERC), sans imposer de méthode de calcul unique. Édité par le Commissariat général au développement durable, mai 2021 ; rédaction Alexia Andreadakis (CGDD), Charlotte Bigard (AgroParisTech), Naomi Delille (CGDD), Françoise Sarrazin (OFB), Thomas Schwab (Cerema) (p. 2 du PDF). ISBN 978-2-11-167002-0 (p. 148). 149 pages.
- Lancé au titre de l'action 90c du Plan biodiversité 2018, à la suite du rapport n° 517 du sénateur Dantec (2017) (p. 8 et 12).
- Périmètre : compensation ex ante des atteintes à la biodiversité (espèces, habitats, fonctions) ; exclut la compensation ex post des dommages, la compensation des autres thématiques environnementales (bruit, air, etc.) et la compensation agricole et forestière (p. 22).

##### Accès et licence
- PDF (copie miroir intégrale, 149 pages, identique au document CGDD) : https://www.pays-de-la-loire.developpement-durable.gouv.fr/IMG/pdf/cgdd_2021_approche_standardisee_dimensionnement_compensation_ecologique.pdf (lu intégralement).
- Notice OFB avec lien de téléchargement : https://ofb.gouv.fr/doc/approche-standardisee-du-dimensionnement-de-la-compensation-ecologique-guide-de-mise-en-oeuvre (lue). Le pied de page du site ofb.gouv.fr indique : "Sauf mention contraire, tous les contenus de ce site sont sous licence etalab-2.0".
- URL d'origine notre-environnement.gouv.fr (https://www.notre-environnement.gouv.fr/IMG/pdf/approche_standardise_e_guide.pdf) : NON VÉRIFIÉ : page non accessible (connexion réinitialisée le 17/10/2026).
- Licence du PDF lui-même : le document ne porte aucune mention de licence (seuls crédits photographiques et ISBN, p. 148). Les mentions légales du site ecologie.gouv.fr (https://www.ecologie.gouv.fr/mentions-legales, lues) indiquent : "Sauf mention explicite de propriété intellectuelle détenue par des tiers, les contenus de ce site sont proposés sous licence ouverte Etalab 2.0". L'applicabilité de cette licence au guide lui-même n'est pas écrite dans le guide : à considérer comme probable mais non confirmée document par document.

##### Contenu et valeurs disponibles
- Principe : "gains ≥ pertes" ; l'Approche standardisée "n'impose pas une méthode de dimensionnement unique" mais un cadre en 8 étapes (arbre de décision, figure 10, p. 43) ; la méthode choisie doit être explicitée, justifiée et la même pour pertes et gains (p. 39).
- Les 8 étapes (tableau 1, p. 44) : 1 identifier les impacts non compensables ; 2 évaluer le caractère significatif des impacts résiduels ; 3 apprécier la faisabilité à l'échelle du territoire ; 4 expliciter la méthode et vérifier sa conformité ; 5 vérifier l'exhaustivité des informations (tableau TID) ; 6 vérifier l'absence de risque de non-conformité et ajustements ; 7 vérifier l'équivalence écologique ; 8 vérifier les modalités de suivi et corrections.
- 3 familles de méthodes (encadré 4, p. 36 à 38, issues de l'état de l'art OFB 2020) :
  - ratio minimal : "Métrique à compenser = ratio minimal préétabli x métrique affectée" (p. 36) ; jugée non conforme car ne vérifie pas l'équivalence ;
  - équivalence par pondération : "Métrique à compenser = métrique affectée x (coefficient pertes / coefficient gains)" (p. 37 et p. 74) ;
  - équivalence par écarts de milieux : "Métrique à compenser = métrique affectée x (|Δ pertes / Δ gains|)" (p. 38 et p. 74).
- Unités : "la surface est de loin la métrique de compensation la plus utilisée, mais les linéaires le sont couramment pour les cours d'eau" (p. 38) ; "l'unité choisie étant souvent une surface (m² ou ha)" (p. 74) ; métriques à compenser et affectée dans les mêmes unités (p. 74).
- Tableau des informations requises pour le dimensionnement (TID, tableau 5, p. 69 à 72) : 5 thématiques, 3 composantes (espèces, habitats, fonctions), 42 cellules (p. 67).
- Aucun coefficient national n'est fixé par le guide. Les seules valeurs chiffrées sont celles d'un exemple de méthode analysée (et jugée non conforme à l'étape 4), p. 62 à 64 :
  - espèces protégées : coefficient d'enjeu de 1 (faible) à 5 (très fort), coefficient nature de l'impact de 0,5 (altération) à 1 (destruction), soit un coefficient global de 0,5 à 5 (p. 62) ;
  - zones humides : coefficient type de zone humide de 1,5 à 3 (tableau 2, p. 63) ; coefficient nature de l'impact de 0,5 à 1 (tableau 3, p. 63) ; coefficient patrimonialité 1,5 en Natura 2000 et 1 hors Natura 2000 (p. 64) ; coefficient global de 1,5 à 4,5 (tableau 4, p. 64), visant les "150 % de compensation surfacique demandés par le Sdage pour la période 2010-2015" (p. 64).
- Facteurs de temps, de risque et de distance : traités à l'étape 6 (tableau 6, p. 89 à 91) sous forme d'ajustements qualitatifs (augmentation des surfaces ou linéaires en cas de pertes intermédiaires, garanties financières, sécurisation foncière), sans coefficient chiffré. Étape 7 (p. 98) : "le ratio final admis pourrait être inférieur à un" si connectivité renforcée, "au plus proche de un" pour des milieux dégradés, "supérieur à un" pour un secteur mal connecté ou un habitat mature.
- Exemple d'application RD914 (partie 3, p. 104 à 125) : compensation "sur une surface trois fois plus importante que celle affectée" (p. 111) ; 6 000 m² de pelouses détruites, 11,5 ha acquis puis 52 ha à terme (tableau 9, p. 123) ; estimation financière "137 240 € HT sur 30 ans pour 20 ha" (p. 125) ; coût de restauration d'un milieu ouvert "4 575 euros par an" (p. 110) ; suivi annuel 10 ans puis tous les 5 ans pendant 20 ans (p. 125).
- Rattachement des habitats à Eunis : 3e niveau pour enjeux faibles, 4e niveau ou plus pour enjeux forts (p. 98).

##### Documents connexes vérifiés
- OFB 2020, "Dimensionnement de la compensation ex ante des atteintes à la biodiversité. État de l'art des approches, méthodes disponibles et pratiques en vigueur", Truchon, de Billy, Bezombes, Padilla (UMS PatriNat), collection Comprendre pour agir n° 36, 68 pages. PDF miroir lu intégralement : https://www.normandie.developpement-durable.gouv.fr/IMG/pdf/ofb_diensionnement_de_lacompensation.pdf. Notice OFB : https://ofb.gouv.fr/doc/dimensionnement-ex-ante-de-la-compensation-des-atteintes-a-la-biodiversite-etat-de-art-des (non ouverte, lien seulement). Contenu chiffré : 25 méthodes analysées, 135 projets étudiés dont la moitié utilise une méthode (p. 4) ; approche par ratio minimal "déconseillée" (p. 4) ; exemple figure 3 (p. 26) d'une méthode Tarn-Aveyron 2011 avec ratios de 1,5 à 5 selon risque d'échec et distance (1,5 ; 2 ; 3 / 2 ; 2,5 ; 4 / 3 ; 4 ; 5) ; Sdage Seine Normandie : 100 % si équivalence fonctionnelle et proximité, sinon 150 % (p. 26) ; Sdage Rhône Méditerranée Corse : 200 % pour les zones humides (témoignage DDT 73, p. 26). Aucune mention de licence dans le PDF.
- CGDD 2018, "Évaluation environnementale. Guide d'aide à la définition des mesures ERC", Théma Balises, janvier 2018, 134 pages, ISSN 2552-7556, dépôt légal janvier 2018. PDF miroir lu intégralement : https://www.pays-de-la-loire.developpement-durable.gouv.fr/IMG/pdf/themaguide_erc.pdf. Objet : classification nationale des mesures E, R, C et A (clefs, catégories, sous-catégories) destinée notamment à l'outil GéoMCE ; la compensation est classée en C1 création/renaturation, C2 restauration/réhabilitation, C3 évolution des pratiques de gestion (p. 42 à 44). Aucune valeur de dimensionnement. Licence : "Conditions générales d'utilisation" restrictives (p. 133 : toute reproduction intégrale ou partielle sans autorisation de l'éditeur est illicite) ; ce n'est donc pas une Licence Ouverte selon le texte du document.
- "Méthode d'évaluation de l'équivalence écologique" de l'OFB : aucun document portant ce titre n'a été trouvé. Le guide 2021 cite (p. 66) la thèse de L. Bezombes (2018, Université Grenoble Alpes) "Développement d'un cadre méthodologique pour l'évaluation de l'équivalence écologique" et l'outil "ECOVAL" (note 35, p. 66), ainsi que la méthode MERCI-Cor (Ifrecor, 2017) et la "Méthode nationale d'évaluation des fonctions des zones humides" (OFB, version 2.0, "in prep." en 2021). Ces documents n'ont pas été ouverts : NON VÉRIFIÉ.

##### Limites
- Pas de barème national de coefficients ; les valeurs chiffrées du guide sont un exemple critiqué, pas une référence à réutiliser.
- Le guide vise les projets soumis à procédure (évaluation environnementale, dérogation espèces protégées, loi sur l'eau, Natura 2000), pas la parcelle urbaine ordinaire.
- Les échelles de "significativité" ne sont pas fixées : "Il n'existe pas à l'heure actuelle de seuils établis de significativité par élément de biodiversité et par échelle géographique" (p. 53).

##### Ce qui manque
- Annexes ou fiches d'application distinctes du guide : non trouvées ; le guide contient lui-même ses annexes (canevas, glossaire, p. 127 à 143).
- Licence explicite du PDF.
- Version française officielle sur notre-environnement.gouv.fr non accessible le jour de l'audit.

---

#### 2. Guide ARB îdF / Institut Paris Region (avril 2026)

##### Objet
- Titre exact : "Prendre en compte la biodiversité dans les opérations d'aménagement. Guide de recommandations et d'évaluation", collection Les Études de L'Institut Paris Region, Biodiversité, avril 2026 (couverture). Rédaction : Marc Barra ; direction de l'ARB îdF : Jonathan Flandin (p. 1). 148 pages (PDF, création 2 avril 2026). ISBN 978-2-7371-2282-8 ; n° d'ordonnancement 43.24.06 (p. 1). Référence bibliographique à utiliser indiquée par l'éditeur : "Barra, M. (2025). Prendre en compte la biodiversité dans les opérations d'aménagement : Guide de recommandations et d'évaluation. ARB Île-de-France, L'Institut Paris Region." (p. 1 ; l'année 2025 de cette référence diffère de la date de couverture avril 2026).
- Page de publication : https://www.institutparisregion.fr/nos-travaux/publications/prendre-en-compte-la-biodiversite-dans-les-operations-damenagement/ (datée 08 avril 2026, lue).

##### Accès et licence
- PDF officiel : https://www.institutparisregion.fr/fileadmin/NewEtudes/000pack5/Etude_3162/biodiversite_amenagement_BAT_8avril.pdf (téléchargé, empreinte MD5 identique à la copie FNAU https://fnau.org/wp-content/uploads/2026/04/biodiversite_amenagement_BAT_8avril.pdf). Lu intégralement.
- Licence : aucune mention de licence dans le PDF. Mentions légales du site (https://www.institutparisregion.fr/mentions-legales/, lues) : "Les contenus du site sont la propriété exclusive de L'Institut Paris Region et sont protégés par le droit d'auteur. Toute représentation totale ou partielle de ce site, par quelque procédé que ce soit, sans l'autorisation de L'Institut Paris Region est donc interdite", à l'exception des données et cartes en open data. Donc pas de Licence Ouverte : réutilisation des textes et de la grille soumise à autorisation.

##### Contenu et valeurs disponibles
- Positionnement de la grille : "Ce référentiel n'a pas vocation à scorer le projet ni à lui attribuer des points, il vise plutôt à permettre de se positionner par rapport à un niveau d'ambition ou à s'améliorer" (p. 111). 25 indicateurs en 6 axes, chacun avec 3 niveaux : Insuffisant / Acceptable / Performant (p. 112 à 115), puis fiches détaillées avec "mesure et mode de preuve" (p. 116 à 140).
- Les 6 axes (p. 111) : 1 Sobriété foncière et conservation des sols à l'échelle planification ; 2 Adaptation au contexte local ; 3 Respect des sols et trame brune à l'échelle projet ; 4 Conception des espaces non bâtis ; 5 Conception architecturale et cadre bâti ; 6 Implication citoyenne.
- Les 25 indicateurs (p. 112 à 115 ; la numérotation du guide compte 1 à 25 avec un 3.bis) :
  1. Privilégier l'aménagement sur des espaces déjà imperméabilisés (mesure : % d'imperméabilisation avant/après, p. 116).
  2. Cas d'un aménagement dans une friche (p. 117).
  3. Densification maîtrisée et coefficient de pleine terre, échelle planification (carence en espaces verts, Plan vert, p. 118).
  3.bis Densification maîtrisée et coefficient de pleine terre, échelle opération. Seuils publiés : Insuffisant "< 20 % d'espaces végétalisés et de pleine terre", Acceptable "20-30 %", Performant "au-delà de 30 %" (p. 112) ; objectif "entre 30 et 45 % d'espaces végétalisés de pleine terre au sein de l'opération" (p. 118).
  4. Coefficient de biotope surfacique harmonisé ou équivalent. Seuils publiés : Insuffisant "CBSh < 0,30", Acceptable "0,30 ≤ CBSh < 0,50", Performant "CBSh ≥ 0,50" ; "En secteur dense, un CBS ≥ 0,5 est généralement considéré comme un bon niveau de performance" ; formule "CBSh = Σ(Surface i x Coefficient_biodiversité i) / Surface_totale_du_site" ; renvoi à l'outil POC CBSh du CSTB (p. 119).
  5. Réalisation d'un diagnostic écologique préalable ("4 saisons", "sur 2 ans idéalement" pour le niveau Performant, p. 120).
  6. Conserver la nature existante sur le site (p. 121).
  7. Limiter les impacts en phase chantier (p. 122).
  8. Décliner les trames vertes et bleues à l'échelle de l'opération (p. 123).
  9. Décliner la trame noire (étude d'incidence de la pollution lumineuse ; conception en fonction des espèces lucifuges, p. 124). Pas de valeur en lux ni en kelvin dans la grille ; le corps du guide recommande des sources "de couleur ambrée plutôt que de couleur blanche-bleue", le flux orienté vers le bas et la réduction d'intensité (p. 52).
  10. Diagnostic agro-pédologie et qualité des sols (p. 125).
  11. Hydrologie et gestion des eaux pluviales à la parcelle (p. 126).
  12. Minimiser l'impact du bâti sur les sols (p. 127).
  13. Déclinaison de la trame brune (volumes des fosses de plantation, p. 128).
  14. Conception écologique des espaces végétalisés (espèces locales, variété de strates ; renvoi à la marque Végétal local, p. 129).
  15. Plan de gestion écologique des espaces végétalisés (p. 130).
  16. Gestion des espèces à caractère envahissant (p. 131).
  17. Adapter les formes architecturales à la biodiversité locale (p. 132).
  18. Végétaliser les toitures en quantité et en qualité (mesure : surface de toits végétalisée / surface totale des toitures, p. 133).
  19. Végétaliser les façades en quantité et en qualité (p. 134).
  20. Accueil de l'avifaune sur le bâti (p. 135).
  21. Accueil des chiroptères sur le bâti (p. 136).
  22. Réduire l'empreinte biodiversité liée aux matériaux, "biodiversité grise" (distance moyenne d'approvisionnement en km, part de réemploi, biosourcés, p. 137).
  23. Impliquer les citoyens dans l'élaboration du projet (p. 138).
  24. Mise à disposition d'espaces dédiés pour l'agriculture urbaine (p. 139).
  25. Connaissance de la biodiversité par les habitants (p. 115).
- Valeurs chiffrées supplémentaires dans le corps du guide (toutes citées de la littérature par le guide) :
  - seuil "de 45 % de surfaces végétalisées en pleine terre" à l'échelle du quartier (Szulczewska et al., 2014) et "30 % de surfaces végétales ou en eau, dans un rayon de 250 m" (Cox et al., 2017), "9 m² d'espaces verts par habitant" (Russo & Cirella, 2018), Open Space Ratio "supérieur à 0,5" (Boutreux, 2024) (p. 19) ;
  - règle "3-30-300" (3 arbres visibles, 30 % de couverture arborée, espace végétalisé d'1 ha à moins de 300 m) (p. 21) ;
  - arbres : "ratio d'environ 0,6 m³ à 1 m³ de sol pour chaque m² de houppier projeté", "volumes supérieurs à 30 m³ pour un arbre à développement moyen", fosses "inférieure à 10 m³" associées à des mortalités pouvant "atteindre 50 %" (p. 38) ; sur dalle "reconstitution de sol sur 1,5 m minimum" (p. 40) ;
  - toitures : extensives "entre 0 et 15 cm", semi-intensives "entre 15 et 30 cm", intensives "au-delà de 30 cm" ; substrat "de 8 à 10 cm minimum" et "jusqu'à 30 cm pour accroître la richesse floristique" (p. 55 et 56) ;
  - SDRIF-E (juin 2025) : augmenter la part de pleine terre "là où elle est inférieure à 30 % dans les espaces urbanisés, hors voiries" ; SCoT de la Métropole du Grand Paris : "au moins 30 % dans les secteurs urbains, hors voirie" (p. 23) ; 528 communes franciliennes soumises à l'obligation de l'article L. 151-22 (p. 23).

##### Limites
- Grille déclarée non destinée au scoring ; seuls 2 indicateurs portent des seuils numériques (3.bis et 4). Les autres sont qualitatifs (Insuffisant / Acceptable / Performant).
- Périmètre francilien (Plan vert, SDRIF-E, MOS) pour plusieurs modes de preuve.
- Droit d'auteur réservé : la grille ne peut pas être reprise telle quelle dans une méthode commerciale sans autorisation.

##### Ce qui manque
- Pas de valeurs d'épaisseur de substrat, d'essences ou d'éclairage dans la grille elle-même ; elles sont dans le corps du texte et proviennent de sources tierces.
- Guides antérieurs ("Bâtir en favorisant la biodiversité", "Renaturer les villes") non lus (non nécessaires, le guide d'avril 2026 ayant été trouvé).

---

#### 3. Certification BiodiverCity (CIBI)

##### Objet
- Labels BiodiverCity (marque déposée, dépôt 4 décembre 2013) portés par l'association Conseil International Biodiversité & Immobilier (CIBI, loi 1901, n° W751222179), 6 avenue de Paris, 78000 Versailles (site). 3 labels : Construction (construction neuve et rénovation à l'îlot), Life (actifs existants), Ready (aménagement de quartier) (https://cibi-biodivercity.com/biodivercity/, lue).

##### Accès et licence
- Site : https://cibi-biodivercity.com/ ; page méthode : https://cibi-biodivercity.com/biodivercity/ ; page processus : https://cibi-biodivercity.com/labelliser-votre-projet/ ; page ressources : https://cibi-biodivercity.com/ressources/ (toutes lues).
- Documents publics téléchargés et lus intégralement :
  - "Guide descriptif, Label BiodiverCity, version 2015 - V1", 49 pages : https://cibi-biodivercity.com/wp-content/uploads/2017/11/Guide-descriptif-BiodiverCity-V1-.pdf ;
  - "Architecture des axes Biodivercity Construction V2015" (4 pages, PDF image, mis en ligne août 2026) : https://cibi-biodivercity.com/wp-content/uploads/2026/08/architecture-axes-b-constr-v1.pdf ;
  - plaquette 2023 "Agir pour la biodiversité en ville : 3 labels" : https://cibi-biodivercity.com/wp-content/uploads/2023/11/cibi-biodivercity-plaquette-labels.pdf ;
  - lexique du Conseil scientifique (version 06/2026, 11 pages) : https://cibi-biodivercity.com/wp-content/uploads/2026/10/cibi-lexique-biodivurbaine-conseilscientifique-v-0626.pdf.
- Réservé : le "manuel technique : définition des critères et méthode de notation" et le "logiciel d'évaluation et de calcul de l'étiquette biodiversité" font partie du référentiel (guide descriptif p. 2) mais ne sont pas en téléchargement sur la page Ressources. Le guide descriptif renvoie au manuel technique pour "le détail" de la notation (p. 36) et pour la formule du potentiel écologique "explicitée dans le manuel technique" (p. 31). L'évaluation est réservée aux "assesseurs accrédités" formés et examinés par le CIBI, puis vérifiée par des vérificateurs tiers (BluBird, Certivea, Deloitte, Ernst & Young) (page "Labelliser votre projet").
- Licence : marque déposée et documents "propriété" du CIBI (guide descriptif p. 3 "Rappel propriété") ; aucune licence de réutilisation.

##### Contenu et valeurs disponibles
- 4 axes (page BiodiverCity et plaquette) : 1 Engagement (maître d'ouvrage) ; 2 Moyens mis en œuvre / le projet (maîtrise d'œuvre) ; 3 Évaluation des bénéfices écologiques / potentiel écologique (écologue) ; 4 Bénéfices pour les usagers / aménités.
- Notation : "Chaque axe est indépendamment noté de A à E" ; label obtenu "à condition de n'avoir aucun D ou E et d'avoir au moins un A" (page BiodiverCity). Niveaux (guide descriptif, p. 46) : Base = pas de D ni E, minimum 1 A (ABBB, ABBC, ABCC, ACCC) ; Performant = minimum 2 A (AABB, AABC, AACC) ; Excellent = minimum 3 A (AAAA, AAAB, AAAC).
- Mécanique de notation (guide descriptif p. 36) : "27 préoccupations", "63 objectifs élémentaires" ; "Notation de 0 à 3 en fonction des critères du guide technique [...] Et de 1 à 5 dans le cas du potentiel écologique" ; "Les notes par objectif sont pondérées de 1 à 3 selon leur importance stratégique" ; "le calcul général de la notation se fait sur le nombre total de points par axe" (p. 35) ; cotation "donnée automatiquement par le logiciel" (p. 45).
- Potentiel écologique (axe 3) : formule publiée "PE = Q x C x F" avec Q qualité biologique, C capacité biologique (surfaces, voire volumes), F fonctionnalité (guide descriptif p. 31), d'après "Méthode d'évaluation du Potentiel écologique des milieux", Berthoud et al., 1989 (note 3, p. 31). Le lexique 2026 (p. 7) détaille : "VE = (F1 x F2 x F3) x surface" avec F1 qualité (diversité, rareté, espèces patrimoniales, état naturel), F2 capacité (surface, forme, éléments structurants), F3 fonctions (refuge, reproduction, ressources, échanges).
- Architecture des axes Construction V1 (PDF image, pages 2 à 4) : l'axe 3 demande de "Calculer la Capacité écologique", "la Qualité écologique" et "la Fonctionnalité écologique" des biotopes existants (3.1) et des néo-biotopes créés (3.2, "ZCP"), avec "Estimation des surfaces, de la perméabilité et du nombre de strate pour chaque biotope" ; bonus "BBP : Bâti à biodiversité Positive" (comparer potentiels avant/après) et "BCE : Bonus de Conservation de l'Existant" (Zone Naturelle Réservée). L'axe 2 comporte une préoccupation 2.7 "Application de la démarche ERC au projet immobilier" et 2.6.1 "CALCUL - Exposer les résultats".
- Coefficient de biotope : aucune mention de "coefficient de biotope" ou "CBS" dans le guide descriptif ni dans l'architecture des axes (recherche textuelle). Le CBS n'est donc pas, d'après les documents publics, un élément de la méthode BiodiverCity.

##### Limites
- Les valeurs de notation par critère, les pondérations exactes et le calcul du potentiel écologique (échelles de Q, C, F) sont dans le manuel technique et le logiciel, non publics.
- Les documents publics datent de 2014-2015 (guide descriptif "version 0.3 du 01/07/2014", architecture des axes "V2015") ; aucune version plus récente du référentiel Construction n'est publiée.
- Le label est "une évaluation et non une garantie" (guide descriptif p. 46).

##### Ce qui manque
- Manuel technique, barème de notation détaillé, nomenclature des biotopes et coefficients du potentiel écologique.
- Pour les labels Life et Ready, les architectures des axes (2023) existent en PDF texte (téléchargées) mais n'ont pas été dépouillées en détail ici.

---

#### 4. Règlement (UE) 2024/1991 sur la restauration de la nature, écosystèmes urbains

##### Accès et licence
- EUR-Lex (https://eur-lex.europa.eu/eli/reg/2024/1991/oj?locale=fr et https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:L_202401991) : NON VÉRIFIÉ : page non accessible (le serveur renvoie un défi JavaScript anti-robot AWS WAF, code HTTP 202 avec corps vide, le 17/10/2026). Le Publications Office (op.europa.eu) renvoie 403.
- Texte intégral lu sur un miroir en anglais : https://lawplayer.com/eu/act/32024R1991 ("Compiled from an official source version [...] the official text prevails", données au 2026-07-04). Intitulé : "Regulation (EU) 2024/1991 of the European Parliament and of the Council of 24 June 2024 on nature restoration and amending Regulation (EU) 2022/869".
- Texte français de l'article 8 et des définitions (20) et (21) lu dans la note officielle wallonne "Règlement 2024/1991 relatif à la restauration de la Nature - Article 8 : Restauration des Ecosystèmes Urbains, Note à destination des experts et parties prenantes" (SPW, avril 2026, 23 pages) : https://biodiversite.wallonie.be/files/02.DOCUMENTS/03.Agir/restauration_nature/Note%20%c3%a0%20destination%20des%20experts%20et%20parties%20prenantes%20-%20RRN%20ART8.pdf (lue intégralement). La concordance entre la version anglaise du miroir et la version française citée par la Wallonie a été vérifiée mot à mot pour l'article 8.
- Licence : textes de l'UE réutilisables (politique de réutilisation de la Commission) ; non vérifié sur EUR-Lex ce jour.

##### Contenu et texte exact
- Article 8 "Restauration des écosystèmes urbains" (texte français, note wallonne p. 5, concordant avec l'anglais du miroir) :
  - "1. D'ici au 31 décembre 2030, les États membres veillent à ce qu'il n'y ait pas de perte nette de la surface totale nationale des espaces verts urbains ni du couvert arboré urbain des zones d'écosystème urbain, déterminées conformément à l'article 14, paragraphe 4, par rapport à 2024. Aux fins du présent paragraphe, les États membres peuvent exclure de ces surfaces totales nationales les zones d'écosystème urbain dans lesquelles la part des espaces verts urbains dans les centres urbains et les pôles urbains dépasse 45 % et la part du couvert arboré urbain dépasse 10 %."
  - "2. À compter du 1er janvier 2031, les États membres obtiennent une tendance à l'augmentation de la surface totale nationale des espaces verts urbains, y compris au moyen de l'intégration d'espaces verts urbains dans les bâtiments et infrastructures, dans les zones d'écosystème urbain, déterminées conformément à l'article 14, paragraphe 4, mesurée tous les six ans à compter du 1er janvier 2031, jusqu'à ce qu'un niveau satisfaisant, fixé conformément à l'article 14, paragraphe 5, soit atteint."
  - "3. Les États membres obtiennent, dans chaque zone d'écosystème urbain déterminée conformément à l'article 14, paragraphe 4, une tendance à l'augmentation du couvert arboré urbain, mesurée tous les six ans à compter du 1er janvier 2031, jusqu'à ce qu'un niveau satisfaisant, fixé conformément à l'article 14, paragraphe 5, soit atteint."
- Article 3, point 20 (texte français, note wallonne p. 6, note 1) : "« espaces verts urbains » : la surface totale d'arbres, de fourrés, d'arbustes, de végétation herbacée permanente, de lichens et de mousses, d'étangs et de cours d'eau présents dans les agglomérations ou dans les villes et banlieues, calculée sur la base des données fournies par le service Copernicus de surveillance des terres dans le cadre de la composante Copernicus du programme spatial de l'Union, établi par le règlement (UE) 2021/696…" (fin du point en anglais : "and, if available for the Member State concerned, other appropriate supplementary data provided by that Member State").
- Article 3, point 21 (note wallonne p. 6, note 2) : "« couvert arboré urbain » : la surface totale de couvert arboré dans les agglomérations et dans les villes et banlieues, calculée sur la base des données Tree Cover Density fournies par le service Copernicus de surveillance des terres dans le cadre de la composante Copernicus du programme spatial de l'Union, établi par le règlement (UE) 2021/696…".
- Article 3, points 16 à 19 (anglais, miroir) : (16) "urban centres" et "urban clusters" = unités territoriales classées dans les villes et les "towns and suburbs" selon la typologie par grille de l'article 4b(2) du règlement (CE) n° 1059/2003 ; (17) "cities" = LAU où au moins 50 % de la population vit dans un ou plusieurs centres urbains ; (18) "towns and suburbs" = LAU où moins de 50 % de la population vit dans un centre urbain mais au moins 50 % dans un pôle urbain ; (19) "peri-urban areas" = zones adjacentes incluant au moins tout ce qui est à 1 km des limites des centres ou pôles urbains.
- Article 14, paragraphe 4 (anglais, miroir) : les États membres déterminent et cartographient les "urban ecosystem areas" pour toutes leurs villes et "towns and suburbs" ; la zone comprend soit la ville entière, soit des parties incluant "at least its urban centres, urban clusters and, if deemed appropriate by the Member State concerned, peri-urban areas" ; agrégation possible de zones adjacentes. Article 14, paragraphe 5 : "By 2030", fixation des niveaux satisfaisants pour les espaces verts urbains (8(2)) et le couvert arboré (8(3)) selon le cadre d'orientation de l'article 20(10).
- Article 28 (anglais, miroir) : "This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union." Date de publication au JO : NON VÉRIFIÉ : page non accessible (EUR-Lex). Le guide ARB îdF indique seulement "entré en vigueur en 2024" (p. 2).
- Indicateurs selon la note wallonne (p. 5 à 7) : 2 indicateurs calculés automatiquement sur données Copernicus ; "les indicateurs choisis sont purement surfaciques et donc quantitatifs. La qualité des espaces n'est pas prise en compte" (p. 7) ; 121 communes wallonnes concernées (p. 8).

##### Limites
- Obligation à la charge des États membres, à l'échelle nationale et par "zone d'écosystème urbain", pas de la parcelle : aucune obligation directe sur un projet de construction.
- Mesure par télédétection Copernicus (Tree Cover Density) qui, d'après la note wallonne (p. 6), ne capte pas la plupart des arbres isolés.

##### Ce qui manque
- Texte français officiel vérifié sur EUR-Lex et date exacte de publication au JOUE.
- Déclinaison française de l'article 8 (zones d'écosystème urbain françaises, niveaux satisfaisants) : non recherchée faute de source accessible.

---

#### 5. Normes ISO du TC 331 "Biodiversity"

##### Accès et licence
- Le site www.iso.org renvoie 403 au robot ; les pages ont été lues via l'alias officiel https://committee.iso.org/standard/<n> (même contenu ISO, titre, statut, stade, pages, cycle de vie) et via les flux RSS ISO (committee.iso.org/sites/isoorg/contents/data/standard/...detail.rss). La page du comité TC 331 (https://www.iso.org/committee/9242308.html) : NON VÉRIFIÉ : page non accessible (403). La liste des projets provient de deux miroirs : le catalogue standardspavilion.org (https://www.standardspavilion.org/sites/isoorg/contents/data/committee/80/30/8030847/x/catalogue/p/0/u/1/w/0/d/0) et la page du comité suédois miroir SIS/TK 623 (https://www.sis.se/en/delta-och-paverka/tksidor/tk600699/sistk-623/).
- Licence : normes payantes (ISO 17298 : 135 CHF, page ISO), texte protégé ; seuls titre, résumé et métadonnées sont librement consultables.

##### Normes publiées (confirmées sur les pages ISO, ICS 13.020.20, comité ISO/TC 331 ; les tirets cadratins des titres officiels ISO sont rendus ici par des traits d'union)
- ISO 17298:2025 "Biodiversity - Considering biodiversity in the strategy and operations of organizations - Requirements and guidelines". Statut : Published, stade 60.60 atteint le 2025-10-06 (RSS), publication 2025-10, édition 1, 20 pages. Objet (page ISO) : cadre pour que les organisations évaluent leurs impacts, dépendances et risques, fixent des objectifs, suivent les progrès et s'alignent sur le cadre mondial de Kunming-Montréal (cible 15). URL : https://www.iso.org/standard/17298 (lue via committee.iso.org/standard/17298).
- ISO 17620:2025 "Biodiversity - Process for designing and implementing biodiversity net gain in development projects". Statut : Published, stade 60.60 atteint le 2025-10-14, publication 2025-10, édition 1, 32 pages. Résumé (page ISO) : "specifies a process to design, implement, maintain and monitor biodiversity net gain (BNG) outcomes throughout the life cycle of spatially explicit development projects" ; couvre les habitats terrestres, d'eau douce et intertidaux jusqu'à la laisse de basse mer ; "does not cover the detailed requirements associated with the delivery of biodiversity enhancements or management" ; applicable à tout secteur "including residential, mixed-use, energy, water, extractive industry, transport, communications agriculture, forestry and infrastructure". Cycle : CD renvoyé au WG le 2024-05-16, CD approuvé pour DIS le 2024-07-19. URL : https://www.iso.org/standard/84992.html.
- ISO 17317:2026 "Biodiversity - Requirements and guidelines for the characterization of native species and products derived from native species". Statut : Published, stade 60.60 atteint le 2026-06-17, publication 2026-06, édition 1, 37 pages. Résumé : plantes, algues et champignons natifs et produits dérivés ; "does not apply to native animal species, timber and wood products". URL : https://www.iso.org/standard/84900.html.

##### Projets en cours (d'après les miroirs, non confirmés sur iso.org)
- ISO/WD 13208.2 "Biodiversity - Vocabulary" (stade 20.60) ; ISO/DTS 18244 "Biodiversity and the food sector - Guidelines and requirements on how to improve biodiversity performance of food companies and food retailers" (50.00) ; ISO/CD TR 25182 "Ecological networks - Mapping of standardization needs" (30.99) ; ISO/AWI 26239 "Identification and assessment of nature-related issues: the LEAP (Locate, Evaluate, Assess, Prepare) approach" (20.00) (standardspavilion et SIS). La page SIS ajoute : ISO/WD 25970 (biodiversité des paysages forestiers gérés, 20.60), ISO/NP 25771 et ISO/PWI 25809 (biodiversité marine), ISO/NP 27098 "Biodiversity: Guidelines and requirements for Measurement, Data, Monitoring, and Assessment" (10.20), ISO/PWI TR 25907 (revue des méthodes de mesure, 00.00). Groupes de travail (SIS) : WG 1 Terminology, WG 2 Measurement, data, monitoring and assessment, WG 3 Protection, conservation and restoration, WG 4 Organizations, strategies and sustainable use.

##### Limites
- Aucune norme ISO/TC 331 publiée ne fournit de coefficients ou de barème à l'échelle de la parcelle ; ISO 17620 décrit un processus BNG, pas une métrique.
- Les stades des projets peuvent avoir évolué ; seules les 3 normes publiées sont confirmées à la source.

##### Ce qui manque
- Contenu normatif (payant) ; liste officielle du TC 331 sur iso.org.

---

#### 6. Coefficient de biotope par surface (CBS) et indices parcellaires en France

##### Sources lues intégralement
- Cerema / OFB, "Retour d'expériences sur les coefficients de surfaces non imperméabilisées ou éco-aménageables, Livrable 2", avril 2024, 25 pages, affaire 23-IF-0090, commanditaire DGALN/DHUP : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable2_RETEX_VF-1.pdf. Statut de communication : "Accès libre : document accessible au public sur internet" (p. 4).
- Cerema / OFB, "Les coefficients de surfaces non imperméabilisées et éco-aménageables : des outils de planification pour préserver les sols en milieu urbain, Livrable 3", octobre 2024, 38 pages (auteurs Neaud, Martin, Monod, Branchu) : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable3_PleineTerre_VF%20%281%29.pdf. "Accès libre" (p. 5). Mentions légales cerema.fr : contenus protégés par le droit de la propriété intellectuelle, pas de Licence Ouverte affichée.
- Cerema / OFB, fiche "Le coefficient de pleine terre, un outil de planification au service de la transition écologique des territoires", juillet 2025, 7 pages : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-09/doc00086338.pdf. Notice OFB : https://ofb.gouv.fr/doc/le-coefficient-de-pleine-terre-un-outil-de-planification-au-service-de-la-transition-ecologique (non ouverte).
- DRIEAT Île-de-France, "Coefficients de pleine terre et de biotope : quelques préconisations", septembre 2025, 11 pages, ISBN 978-2-11-179525-9 : https://www.drieat.ile-de-france.developpement-durable.gouv.fr/IMG/pdf/fiche_plu_pleine_terre_vfinale.pdf.
- DGALN (DHUP, DEB), club PLUi, "Fiche n° 8 : Le Coefficient de Biotope par Surface (CBS)", juillet 2015, 9 pages : http://www.bourgogne-franche-comte.developpement-durable.gouv.fr/IMG/pdf/gt_tvb_fiche_8_coefficient_biotope_surface_juillet_2015_cle2fad68.pdf.
- CSTB, GT 7 Biodiversité (CAP 2030), "Guide du Coefficient de Biotope Surfacique harmonisé, version de septembre 2024", nomenclature "version de décembre 2024", 29 pages (dates de slides 23/01/2025) : https://cap2030-gt7-biodiv.dimn-cstb.fr/static/documents/20241217_Guide_CBSh.pdf. Outil : https://cap2030-gt7-biodiv.dimn-cstb.fr/webapp/. Conditions : "L'outil (interface et moteur de calcul) est propriété du CSTB", "mis à disposition sans contrepartie financière", "ne peut pas être utilisé à des fins commerciales" (p. 11).
- Cerema, diaporama "Étude sur les coefficients de surfaces non imperméabilisées ou éco-aménageables 2023-2025", 5 décembre 2024, 30 pages : https://www.planif-territoires.logement.gouv.fr/IMG/pdf/cerema_etudecbs_cpt.pdf.
- ADEME, cahier technique 2006 "Réussir la planification et l'aménagement durables - Écosystèmes dans les territoires", fiche outil CBS (http://multimedia.ademe.fr/catalogues/CTecosystemes/fiches/outil11p6364.pdf) : NON VÉRIFIÉ : page non accessible (proxy 502). Ses valeurs sont connues uniquement par citation du Livrable 3 (voir ci-dessous).
- Plante & Cité, LPO, CAUE : aucun document chiffrant un CBS n'a été ouvert ; le guide ARB îdF cite Plante & Cité (2025) "Connaître et évaluer la biodiversité des sols" et LPO (2022) "Sols vivants" (p. 125) sans valeurs de CBS. NON VÉRIFIÉ.

##### Contenu et valeurs disponibles
- Définition et cadre : "Le CBS correspond à la proportion de surfaces éco-aménageables par rapport à la surface totale du projet" (Livrable 2, p. 11) ; dans un coefficient de pleine terre "il n'y a que deux valeurs : celle des sols de pleine terre égale à 1 et une valeur nulle" (Livrable 3, p. 18) ; "La valeur de la pondération pour un espace de pleine terre est égale à 1, que les pondérations des autres types d'espaces ne doivent pas dépasser" (DRIEAT, p. 2).
- Plages de pondération observées dans 10 collectivités (Livrable 2, p. 12 ; repris Livrable 3 p. 24 et 25 et DRIEAT p. 5) : surfaces imperméables 0 "dans la majorité des cas" ; surfaces semi-perméables ou perméables "entre 0,15 et 0,5" ; espaces verts sur dalles ou toitures "entre 0,1 et 1 en fonction de l'épaisseur du substrat" ; façades végétalisées "entre 0,1 et 0,5" ; pleine terre "le plus souvent 1", parfois "1,2" à titre dérogatoire pour les espaces multifonctionnels.
- Valeurs ADEME 2006 citées par le Cerema (Livrable 3, p. 32) et plafonds recommandés : semi-perméables "au maximum de 0,1 (au lieu de 0,3)", façades végétalisées "au maximum de 0,3 (au lieu de 0,5)", dalles/toitures végétalisées "au max. de 0,5 (au lieu de 0,7)". Mêmes plafonds dans la fiche OFB/Cerema juillet 2025 (p. 6).
- Valeurs Berlin reprises par la fiche club PLUi 2015 (exemple de calcul p. 4) : asphalte 0,0 ; cailloutis avec pelouse 0,5 ; pavés 0,3 ; pleine terre 1,0 ; murs végétalisés 0,5 ; toiture végétalisée 0,7. Exemples de PLU (p. 5) : Montreuil 0,6 pour toitures intensives ou dalles de 80 cm minimum et 0,20 pour toitures extensives (< 0,80 m) ou murs végétalisés ; Grenoble assimile une toiture avec 50 cm de terre à de la pleine terre.
- Objectifs cibles observés : Avignon CBS 0,2 à 0,6 et pleine terre 0,2 à 0,4 selon zonage (Livrable 2, p. 14) ; Grand Dax 0,2, Avignon ou Strasbourg 0,3, Grand Lac 0,5 à 0,8 selon la taille de l'unité foncière (≤ 500 m² : 0,5 ; 501 à 1 000 m² : 0,6 ; 1 001 à 2 000 m² : 0,7 ; > 2 001 m² : 0,8) (Livrable 3, p. 24) ; Roubaix 0,5 logement et 0,3 autres destinations (fiche 2015, p. 8) ; Strasbourg bonus "2 % [...] pour un arbre conservé, dans une limite de 10 %" (Livrable 3, p. 33).
- Définition de la pleine terre proposée (Livrable 3, p. 10 et 27 ; fiche 2025, p. 4) : 5 critères cumulatifs : surface libre de tout revêtement même perméable ; végétalisée ; au moins 2 horizons dont un organique en surface, profondeur "> 30 cm" ; pas d'interface imperméable anthropique en profondeur ; matériaux terreux majoritaires (granulométrie "< 2 mm").
- CBS harmonisé CSTB (nomenclature décembre 2024, lue sur les slides 6 à 10 du guide CBSh) : "35 surfaces [...] regroupées en 4 catégories : surfaces minérales (6), surfaces végétalisées sur dalle (16), surface végétalisées pleine terre (8) et masses d'eau (5)" (Livrable 3, p. 25, version octobre 2022). Coefficients de capacité d'accueil lus dans le guide CBSh :
  - toitures classiques 0 ; toitures végétalisées : extensif moins de 8 cm sédums 0,1 ; extensif + (9 à 12 cm) herbacées 0,2, herbacées + arbustes 0,3 ; semi-intensif (13 à 30 cm) 1 strate 0,3, 2 strates 0,4 ; intensif moins (31 à 60 cm) 1 strate 0,4, 2 strates 0,5, 3 strates 0,6 ; intensif + (plus de 60 cm) 1 strate 0,5, 2 strates 0,6, 3 strates 0,7 (slide 6) ;
  - voiries : minérales imperméables 0 ; semi-perméables et perméables 0,1 ; mixtes (pavés à gazon, etc.) 0,2 ; avec arbres respectivement 0,1 ; 0,2 ; 0,3 (slide 7) ;
  - espaces verts au sol sur dalle : moins de 30 cm 1 strate 0,3, 2 strates 0,4 ; 31 à 80 cm 1 strate 0,4, 2 strates 0,5, 3 strates 0,7 ; plus de 81 cm 1 strate 0,5, 2 strates 0,6, 3 strates 0,8 (slide 8) ;
  - espaces verts en pleine terre : 1 strate 0,7, 2 strates 0,8, 3 strates 0,9 ; espaces agricoles : grande culture 0,6, pré et pâture 0,7, prairie temporaire 0,8, friche agricole < 5 ans 0,7, > 5 ans 0,8 ; prairie permanente 0,9 ; espaces naturels 1 (slide 9) ;
  - masses d'eau : bassins et réservoirs 0,2 ; milieux humides étanches 0,7 ; milieux humides non étanches 1 ; noues d'infiltration 0,7 ; fossés 0,8 (slide 10) ;
  - règle de calcul : la strate "arborée" n'est effective que si elle couvre "au minimum 20 % de l'espace vert" ; scénarios par défaut (coefficients soulignés : 0,1 toitures sédum, 0 minéral imperméable, 0,3 dalle < 30 cm, 0,7 pleine terre 1 strate, 0,6 grande culture, 0,2 bassins) (slide 11).
- Caractère obligatoire du coefficient : loi Climat et Résilience ; obligation pour "près de 40 % des communes en Île-de-France", soit 528 communes (DRIEAT, p. 1).

##### Limites
- Convergence des sources officielles : "les coefficients de biotope par surface correspondent davantage à des indicateurs d'occupation des sols qu'à des indicateurs de biodiversité" (Livrable 3, p. 26) ; "Ne sont pas des coefficients de biodiversité" (DRIEAT, p. 10 ; fiche 2015, p. 6) ; "Ne reposent que sur du déclaratif" (diaporama Cerema, p. 24).
- Le CBSh du CSTB est un "POC", non commercialisable sans accord, et ses coefficients sont "fixés par les experts écologues du GT 7" (guide CBSh, p. 9), sans publication de la méthode d'attribution.
- Les plages de pondération sont des observations de PLU, pas des valeurs normatives.

##### Ce qui manque
- Fiche ADEME 2006 originale (non accessible), guide ADEME "Nature en ville" chiffré, documents Plante & Cité / LPO / CAUE chiffrant un CBS.
- Livrable 1 (bibliographie nationale et internationale) du Cerema, annoncé "en cours" (Livrable 3, p. 4), et partie 4 "diagnostic, suivi et évaluation", annoncée "à venir" (p. 37).

---

#### 7. Textes réglementaires français récents (code de l'urbanisme)

##### Accès et licence
- Legifrance (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043967077 et https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465959) : NON VÉRIFIÉ : page non accessible (403 au 17/10/2026).
- Texte consolidé lu dans le PDF "Code de l'urbanisme (Mise à jour du 2026-09-01)", édition 2026-10-01, produit par Droit.org "à partir des données issues des APIs Legifrance", 704 pages, "ne contient que du droit positif français" : https://codes.droit.org/PDF/Code%20de%20l'urbanisme.pdf (articles cités lus intégralement). Les versions et dates de modification ci-dessous sont celles affichées par ce PDF.
- Portail national de l'artificialisation (Cerema), page définitions : https://artificialisation.developpement-durable.gouv.fr/comprendre-et-sensibiliser/consommation-despaces-et-artificialisation-definitions (lue ; site sous "licence etalab-2.0" sauf mention contraire). Page "cas particuliers" : https://artificialisation.developpement-durable.gouv.fr/mesurer-lartificialisation-avec-locsge/cas-particuliers (lue).
- Projet de décret et rapport de présentation soumis à consultation (TREL2307502D, juin 2023) : https://www.consultations-publiques.developpement-durable.gouv.fr/IMG/pdf/trel2307502d_pjd-nomenclature-rapport-local-zan.pdf (lu, 7 pages). Fiche indicateur "Artificialisation" du portail (15/05/2024, 12 pages, "document de travail") : lue.
- Article de la Fédération des EPL sur le décret publié au JO du 28 novembre 2023 : https://lesepl.fr/2023/12/zan-1-publication-de-la-nouvelle-nomenclature-des-sols/ (lu).

##### Contenu et texte exact
- Article L. 101-2, 6° bis (code de l'urbanisme, version "LOI n°2023-1196 du 18 décembre 2023 - art. 17") : "La lutte contre l'artificialisation des sols, avec un objectif d'absence d'artificialisation nette à terme".
- Article L. 101-2-1 (créé par "LOI n°2021-1104 du 22 août 2021 - art. 192"), texte intégral lu : "L'atteinte des objectifs mentionnés au 6° bis de l'article L. 101-2 résulte de l'équilibre entre : 1° La maîtrise de l'étalement urbain ; 2° Le renouvellement urbain ; 3° L'optimisation de la densité des espaces urbanisés ; 4° La qualité urbaine ; 5° La préservation et la restauration de la biodiversité et de la nature en ville ; 6° La protection des sols des espaces naturels, agricoles et forestiers ; 7° La renaturation des sols artificialisés. L'artificialisation est définie comme l'altération durable de tout ou partie des fonctions écologiques d'un sol, en particulier de ses fonctions biologiques, hydriques et climatiques, ainsi que de son potentiel agronomique par son occupation ou son usage. La renaturation d'un sol, ou désartificialisation, consiste en des actions ou des opérations de restauration ou d'amélioration de la fonctionnalité d'un sol, ayant pour effet de transformer un sol artificialisé en un sol non artificialisé. L'artificialisation nette des sols est définie comme le solde de l'artificialisation et de la renaturation des sols constatées sur un périmètre et sur une période donnés. Au sein des documents de planification et d'urbanisme, lorsque la loi ou le règlement prévoit des objectifs de réduction de l'artificialisation des sols ou de son rythme, ces objectifs sont fixés et évalués en considérant comme : a) Artificialisée une surface dont les sols sont soit imperméabilisés en raison du bâti ou d'un revêtement, soit stabilisés et compactés, soit constitués de matériaux composites ; b) Non artificialisée une surface soit naturelle, nue ou couverte d'eau, soit végétalisée, constituant un habitat naturel ou utilisée à usage de cultures. Un décret en Conseil d'Etat fixe les conditions d'application du présent article. Il établit notamment une nomenclature des sols artificialisés ainsi que l'échelle à laquelle l'artificialisation des sols doit être appréciée dans les documents de planification et d'urbanisme."
- Article L. 151-22 (version "LOI n°2026-103 du 19 février 2026 - art. 108") : "I. - Le règlement peut imposer une part minimale de surfaces non imperméabilisées ou éco-aménageables, éventuellement pondérées en fonction de leur nature, afin de contribuer au maintien de la biodiversité et de la nature en ville. II. - Dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants figurant sur la liste prévue à l'article 1406 bis du code général des impôts et dans les communes de plus de 15 000 habitants en forte croissance démographique figurant sur la liste prévue au dernier alinéa du II de l'article L. 302-5 du code de la construction et de l'habitation, le règlement définit, dans les secteurs qu'il délimite, une part minimale de surfaces non imperméabilisées ou éco-aménageables, selon les modalités prévues au I du présent article. III. - Les dispositions des règlements des plans locaux d'urbanisme prises en application des I et II s'appliquent aux projets soumis à autorisation d'urbanisme au titre du présent code, à l'exclusion des projets de rénovation, de réhabilitation ou de changement de destination des bâtiments existants qui n'entraînent aucune modification de l'emprise au sol." (Le Livrable 3 Cerema d'octobre 2024, p. 17, cite la version antérieure renvoyant à "l'article 232 du code général des impôts" ; le renvoi à l'article 1406 bis résulte de la version 2026 du code.)
- Article R. 151-43 (décret n° 2015-1783 du 28 décembre 2015), 1° : "Imposer, en application de l'article L. 151-22, que les surfaces non imperméabilisées ou éco-aménageables d'un projet représentent une proportion minimale de l'unité foncière. Il précise les types d'espaces, construits ou non, qui peuvent entrer dans le décompte de cette surface minimale en leur affectant un coefficient qui en exprime la valeur pour l'écosystème par référence à celle d'un espace équivalent de pleine terre" ; 2° obligations d'espaces libres et de plantations ; 4° espaces et secteurs contribuant aux continuités écologiques ; 8° clôtures perméables à la faune.
- Article R. 101-1 (décret n° 2023-1096 du 27 novembre 2023, art. 1) : II "le solde entre les surfaces artificialisées et les surfaces désartificialisées est évalué au regard des catégories listées par la nomenclature annexée" ; "les surfaces sont qualifiées [...] selon l'occupation effective du sol observée et non selon les zones ou secteurs délimités par les documents" ; III : peuvent être non artificialisées les surfaces végétalisées sous installations photovoltaïques respectant le décret prévu au 6° du III de l'article 194 de la loi 2021-1104 et "les surfaces dont les sols sont végétalisés et à usage de parc ou de jardin public" (catégories 9° ou 10°). Article R. 101-2 : observatoire de l'artificialisation.
- Annexe à l'article R. 101-1 (nomenclature, décret n° 2023-1096 du 27 novembre 2023), texte lu : surfaces artificialisées 1° sols imperméabilisés en raison du bâti (seuil "Supérieur ou égal à 50 m² d'emprise au sol") ; 2° imperméabilisés par un revêtement ; 3° perméables mais "stabilisés et compactés ou recouverts de matériaux minéraux" ou "matériaux composites" ; 4° "Surfaces à usage résidentiel, de production secondaire ou tertiaire, ou d'infrastructures [...] dont les sols sont couverts par une végétation herbacée" ; 5° surfaces des catégories 1° à 4° en chantier ou en état d'abandon. Surfaces non artificialisées 6° sols nus naturels ou couverts d'eau, neige, glace ; 7° cultures, y compris en friche ; 8° végétalisées à usage sylvicole ; 9° végétalisées constituant un habitat naturel ; 10° végétalisées n'entrant pas dans les catégories précédentes. Seuil des catégories 2° à 10° : "Supérieur ou égal à 2 500 m² d'emprise au sol ou de terrain". Notes : "Les infrastructures linéaires sont qualifiées à partir d'une largeur minimale de cinq mètres" ; "Une surface végétalisée est qualifiée d'herbacée dès lors que moins de vingt-cinq pour cent du couvert végétal est arboré".
- Le rapport de présentation du projet de décret (p. 2) précise que cette nomenclature "n'a pas non plus vocation à s'appliquer au niveau d'un projet, pour lequel l'artificialisation induite est appréciée directement au regard de l'altération durable des fonctions écologiques ainsi que du potentiel agronomique du sol", et qu'elle ne s'applique pas à la première tranche 2021-2031 (consommation d'ENAF seulement). L'article de la FedEpl indique que le décret publié au JO du 28 novembre est "applicable à compter de 2031".
- "Surface végétalisée" : il n'existe pas de définition autonome ; la notion est portée par les catégories 4° et 8° à 10° de la nomenclature et la note (**) sur le seuil de 25 % de couvert arboré.
- Renaturation dans les documents d'urbanisme : L. 141-10, 3° (SCoT, "LOI n°2023-973 du 23 octobre 2023 - art. 16") : le DOO "peut identifier à cette fin des zones préférentielles pour la renaturation, par la transformation de sols artificialisés en sols non artificialisés ainsi que des zones propices à l'accueil de sites naturels de compensation, de restauration et de renaturation" ; L. 151-7, I, 4° (OAP du PLU) : "renaturer, notamment par l'identification de zones propices à l'accueil de sites naturels de compensation, de restauration et de renaturation" ; R. 151-7 (décret n° 2022-1673 du 27 décembre 2022) : les OAP "peuvent également identifier des zones préférentielles pour la renaturation" ; L. 151-6-2 ("LOI n°2021-1104 du 22 août 2021 - art. 200") : les OAP "définissent [...] les actions et opérations nécessaires pour mettre en valeur les continuités écologiques".
- Couvert arboré : aucun objectif chiffré de couvert arboré ou de canopée n'a été trouvé dans le code de l'urbanisme (recherche textuelle "couvert arboré", "canopée"). Seule occurrence chiffrée : parcs de stationnement, article L. 111-19-1 ("LOI n°2025-1129 du 26 novembre 2025 - art. 8") : parcs extérieurs "de plus de 500 mètres carrés" devant intégrer "sur au moins la moitié de leur surface" des revêtements ou dispositifs favorisant la perméabilité, et des dispositifs végétalisés ou ombrières "sur au moins la moitié de leur surface" ; R. 111-25-8 (décret n° 2024-1023 du 13 novembre 2024) : ombrage par "plantation d'arbres à canopée large [...] à raison d'un arbre pour trois emplacements de stationnement".
- "Compensation des surfaces artificialisées" : aucun décret ou arrêté portant ce titre n'a été trouvé. La compensation est traitée par le code de l'environnement (séquence ERC, voir point 1) ; dans le code de l'urbanisme, seules les mentions de "sites naturels de compensation, de restauration et de renaturation" (L. 141-10, L. 151-7) existent. L'article L. 151-22 ne fait pas de la pleine terre une obligation nationale chiffrée : le seuil est fixé localement par chaque PLU(i).

##### Limites
- Textes lus sur un code consolidé tiers (Droit.org, données API Legifrance) et non sur Legifrance même ; les numéros de décret et dates de version affichés sont fiables mais non recoupés sur la source officielle ce jour.
- Le décret n° 2023-1096 du 27 novembre 2023 n'a pas été lu dans sa version JO (fichier préfectoral inaccessible) ; son contenu a été lu via le code consolidé (R. 101-1, R. 101-2, annexe) et confirmé par le portail national.

##### Ce qui manque
- Lecture directe sur Legifrance de L. 101-2-1, L. 151-22, R. 101-1 et de l'annexe ; vérification de la loi n° 2026-103 du 19 février 2026 (art. 108) modifiant L. 151-22.
- Décret n° 2023-1408 du 29 décembre 2023 et arrêté du 29 décembre 2023 (photovoltaïque) : cités par le portail, non lus.

---

#### Synthèse transversale pour la méthode de calcul

- Aucune source officielle française ne publie de coefficient de biodiversité normatif à l'échelle de la parcelle. Les seules grilles chiffrées publiées sont : la nomenclature CBSh du CSTB (35 surfaces, coefficients 0 à 1, usage non commercial), les plafonds Cerema/OFB (0,1 ; 0,3 ; 0,5) et les plages observées dans les PLU (semi-perméable 0,15 à 0,5 ; dalle/toiture 0,1 à 1 ; façade 0,1 à 0,5 ; pleine terre 1).
- Les seuils d'ambition publiés : ARB îdF CBSh < 0,30 / 0,30 à 0,50 / ≥ 0,50 et pleine terre < 20 % / 20 à 30 % / > 30 % ; SDRIF-E et SCoT MGP 30 % de pleine terre hors voirie.
- La compensation réglementaire (CGDD 2021) impose un cadre de démonstration (gains ≥ pertes, 8 étapes, TID) et non des multiplicateurs ; les ratios chiffrés rencontrés (1,5 à 5 ; 100 à 200 %) sont des pratiques locales ou des exemples critiqués.
- Le règlement (UE) 2024/1991 fixe des obligations de résultat aux États (pas de perte nette 2030 vs 2024, tendance à la hausse après 2031, exclusion possible si espaces verts > 45 % et couvert arboré > 10 %), mesurées par Copernicus, sans portée directe sur un permis de construire.
- BiodiverCity publie l'architecture (4 axes, A à E, PE = Q x C x F) mais garde le barème et le calcul dans un manuel technique et un logiciel réservés aux assesseurs.
- ISO 17620:2025 fournit un processus BNG international sans métrique.

---

#### Sources consultées (statut au 17/10/2026)

1. https://www.pays-de-la-loire.developpement-durable.gouv.fr/IMG/pdf/cgdd_2021_approche_standardisee_dimensionnement_compensation_ecologique.pdf - CGDD/OFB/Cerema 2021, 149 p. - lue intégralement.
2. https://ofb.gouv.fr/doc/approche-standardisee-du-dimensionnement-de-la-compensation-ecologique-guide-de-mise-en-oeuvre - notice OFB - lue intégralement.
3. https://www.notre-environnement.gouv.fr/IMG/pdf/approche_standardise_e_guide.pdf - non accessible.
4. https://www.normandie.developpement-durable.gouv.fr/IMG/pdf/ofb_diensionnement_de_lacompensation.pdf - OFB 2020 état de l'art, 68 p. - lue partiellement (résumé, chapitre approches p. 25 à 30, colophon).
5. https://www.pays-de-la-loire.developpement-durable.gouv.fr/IMG/pdf/themaguide_erc.pdf - CGDD 2018 guide ERC, 134 p. - lue partiellement (introduction, partie 1, clef compensation p. 39 à 45, conditions d'utilisation p. 133).
6. https://www.ecologie.gouv.fr/mentions-legales - lue intégralement.
7. https://www.institutparisregion.fr/nos-travaux/publications/prendre-en-compte-la-biodiversite-dans-les-operations-damenagement/ - lue intégralement.
8. https://www.institutparisregion.fr/fileadmin/NewEtudes/000pack5/Etude_3162/biodiversite_amenagement_BAT_8avril.pdf - guide ARB îdF avril 2026, 148 p. - lue intégralement (texte extrait ; chapitre 6 et passages chiffrés lus en détail).
9. https://fnau.org/wp-content/uploads/2026/04/biodiversite_amenagement_BAT_8avril.pdf - copie identique (MD5) - lue intégralement.
10. https://www.institutparisregion.fr/mentions-legales/ - lue intégralement.
11. https://cibi-biodivercity.com/ ; https://cibi-biodivercity.com/biodivercity/ ; https://cibi-biodivercity.com/labelliser-votre-projet/ ; https://cibi-biodivercity.com/ressources/ - lues intégralement.
12. https://cibi-biodivercity.com/wp-content/uploads/2017/11/Guide-descriptif-BiodiverCity-V1-.pdf - 49 p. - lue partiellement (sommaire, présentation, axe 3, logique d'évaluation, étiquette, règles de labellisation).
13. https://cibi-biodivercity.com/wp-content/uploads/2026/08/architecture-axes-b-constr-v1.pdf - 4 p. (image) - lue intégralement.
14. https://cibi-biodivercity.com/wp-content/uploads/2023/11/cibi-biodivercity-plaquette-labels.pdf - 6 p. - lue intégralement.
15. https://cibi-biodivercity.com/wp-content/uploads/2026/10/cibi-lexique-biodivurbaine-conseilscientifique-v-0626.pdf - 11 p. - lue partiellement (entrées potentiel écologique).
16. https://cibi-biodivercity.com/wp-content/uploads/2026/08/cibi-annexe-2-architecture-des-axes-blife.pdf et https://cibi-biodivercity.com/wp-content/uploads/2026/08/ready-architecture-des-axes-23.pdf - téléchargées, non dépouillées.
17. https://eur-lex.europa.eu/eli/reg/2024/1991/oj?locale=fr ; https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:L_202401991 ; https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX:32024R1991 - non accessibles (défi anti-robot).
18. https://op.europa.eu/fr/publication-detail/-/publication/9d4bbc10-4696-11ef-a8ba-01aa75ed71a1/language-fr - non accessible (403).
19. https://lawplayer.com/eu/act/32024R1991 - miroir anglais du règlement - lue intégralement (articles 3, 8, 14, 28).
20. https://biodiversite.wallonie.be/files/02.DOCUMENTS/03.Agir/restauration_nature/Note%20%c3%a0%20destination%20des%20experts%20et%20parties%20prenantes%20-%20RRN%20ART8.pdf - note SPW avril 2026, 23 p. - lue intégralement (texte extrait ; chapitre 2 lu en détail).
21. https://www.eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmfd4x3rfwyy - service fermé, sans contenu.
22. https://www.iso.org/standard/17298 (via committee.iso.org/standard/17298) - lue intégralement.
23. https://www.iso.org/standard/84992.html (via committee.iso.org) - ISO 17620:2025 - lue intégralement.
24. https://www.iso.org/standard/84900.html (via committee.iso.org) - ISO 17317:2026 - lue intégralement.
25. Flux RSS ISO des 3 normes (committee.iso.org/sites/isoorg/contents/data/standard/...detail.rss) - lus intégralement.
26. https://www.iso.org/committee/9242308.html - non accessible (403).
27. https://www.standardspavilion.org/sites/isoorg/contents/data/committee/80/30/8030847/x/catalogue/p/0/u/1/w/0/d/0 - lue intégralement (via résumé WebFetch).
28. https://www.sis.se/en/delta-och-paverka/tksidor/tk600699/sistk-623/ - lue intégralement (via résumé WebFetch).
29. https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable2_RETEX_VF-1.pdf - Cerema/OFB Livrable 2, 25 p. - lue intégralement.
30. https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-10/Livrable3_PleineTerre_VF%20%281%29.pdf - Cerema/OFB Livrable 3, 38 p. - lue intégralement.
31. https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-09/doc00086338.pdf - fiche Cerema/OFB pleine terre juillet 2025, 7 p. - lue intégralement.
32. https://www.drieat.ile-de-france.developpement-durable.gouv.fr/IMG/pdf/fiche_plu_pleine_terre_vfinale.pdf - DRIEAT septembre 2025, 11 p. - lue intégralement.
33. http://www.bourgogne-franche-comte.developpement-durable.gouv.fr/IMG/pdf/gt_tvb_fiche_8_coefficient_biotope_surface_juillet_2015_cle2fad68.pdf - club PLUi fiche 8, 9 p. - lue intégralement.
34. https://www.adaptation-changement-climatique.gouv.fr/agir/espace-documentaire/club-plui-fiche-ndeg8-sur-coefficient-biotope-surface-cbs - page de référencement - lue intégralement.
35. https://cap2030-gt7-biodiv.dimn-cstb.fr/static/documents/20241217_Guide_CBSh.pdf - CSTB guide CBSh, 29 p. - lue intégralement (texte et slides 6 à 10 en image).
36. https://www.planif-territoires.logement.gouv.fr/IMG/pdf/cerema_etudecbs_cpt.pdf - diaporama Cerema 05/12/2024, 30 p. - lue intégralement.
37. https://multimedia.ademe.fr/catalogues/CTecosystemes/fiches/outil11p6364.pdf - fiche ADEME 2006 - non accessible (502).
38. https://www.cerema.fr/fr/mentions-legales - lue intégralement.
39. https://codes.droit.org/PDF/Code%20de%20l'urbanisme.pdf - code consolidé 2026-09-01, 704 p. - lue partiellement (L. 101-2, L. 101-2-1, L. 111-19-1, L. 141-10, L. 151-6-2, L. 151-7, L. 151-22, L. 151-23, L. 153-27, R. 101-1, R. 101-2, R. 111-25-7, R. 111-25-8, R. 151-7, R. 151-43, annexe R. 101-1).
40. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043967077 ; https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048465959 - non accessibles (403).
41. https://www.consultations-publiques.developpement-durable.gouv.fr/IMG/pdf/trel2307502d_pjd-nomenclature-rapport-local-zan.pdf - projet de décret 2023, 7 p. - lue intégralement.
42. Fiche indicateur "Artificialisation" du portail (version 15/05/2024, 12 p., fichier fiche_artif.pdf) - lue intégralement.
43. https://artificialisation.developpement-durable.gouv.fr/ ; .../comprendre-et-sensibiliser/consommation-despaces-et-artificialisation-definitions ; .../mesurer-lartificialisation-avec-locsge/cas-particuliers - lues intégralement.
44. https://lesepl.fr/2023/12/zan-1-publication-de-la-nouvelle-nomenclature-des-sols/ - lue partiellement.
45. https://www.rhone.gouv.fr/index.php/contenu/telechargement/58662/400160/file/joe_20231128_0275_0017(1).pdf - JO du 28/11/2023 - non accessible (connexion coupée).

### 2.8 Références du cahier des charges non lues, et ce qui doit être fourni en fichier

| Référence | État au 17/10/2026 | Ce qu'il faut |
|---|---|---|
| Référentiel Effinature v8.1 | non lu : le référentiel n'est pas public dans sa totalité ; le cahier des charges demande de le demander à Cédric | le fichier de la version de raccordement (point P16), nécessaire au lot 1 pour l'étape E5 et pour `seuils.csv` |
| Dépôt et documentation d'OpenBCE | lu intégralement, dépôt public cloné | rien |
| Méthode Th-BCE 2020, annexe III consolidée | PDF téléchargé (1 854 pages, version du 21/07/2026) ; chapitres 1 et sommaire lus pour la structure documentaire ; les fiches physiques n'ont pas à être lues pour Vi-BCN | rien |
| Format RSEE (XSD) | aucun fichier XSD publié sur les pages du portail lues (constat identique dans OpenBCE) ; structure connue par les RSEE lus | si un XSD officiel existe dans les archives d'ARKEMEP (études RE2020), le joindre : le schéma XSD du RSNat s'en inspirera ; sinon il sera écrit de zéro |
| Carbone 4, biodiversité grise | PDF fourni par Cédric le 17/10/2026 et lu intégralement (30 pages) ; intégré à la fiche 2.4 | rien |
| Chaudhary et al. 2015 | texte intégral et Supporting Information inaccessibles (ACS) | rien d'indispensable : LC-IMPACT v2 (Scherer 2023) remplace cette source |
| LC-IMPACT v1.3 | archive de 4,5 Go non téléchargée | rien : la v2.0 (février 2026) est lue et plus récente |
| EN 15804+A2 et complément national | norme payante, non lue ; la RE2020 (annexe II, tableau 12) en donne les indicateurs | rien pour le lot 0 ; au lot 1, vérifier sur un échantillon de FDES la présence effective du SQP (consultation gratuite) |
| UKHab (classification d'habitats UK) | page de licence inaccessible (403) | rien : UKHab n'est pas réutilisé, seules les valeurs OGL de la métrique le sont |
| Prototype en ligne « OpenNat » du 16/10/2026 | non ouvert, hors périmètre | rien |

### 2.9 Fiches de sources complémentaires A à E (fusion VIBCN)

5 fichiers repris de l'audit parallèle VIBCN du 17 octobre 2026 et livrés dans `audit/fiches/` : `A_metrique_uk.md` (14 fiches : guide, classeur 1.0.4 et fiches d'état de la métrique statutaire anglaise, Small Sites Metric, Biodiversity Metric 4.0 et son Technical Annex 2, UKHab, Green Book, critiques publiées, méthodes écossaise, galloise, australienne et néo-zélandaise, OGL v3), `B_biotopes_cbs_zan.md` (10 fiches : BKompV, Hesse, Bavière, NRW, Bade-Wurtemberg, Berlin, Londres, CBS français, nomenclature ZAN, textes européens sur les sols), `C_modeles_globaux_acv.md` (15 fiches : GLOBIO 3, 3.5 et 4, Benítez-López 2010, GBS, LC-IMPACT, Chaudhary 2015 et 2018, ReCiPe 2016, EF 3.1, EN 15804, INIES, ÖKOBAUDAT, ecoinvent, Carbone 4, cadre UNEP-SETAC), `D_cadre_francais_typologies.md` (12 fiches : Th-BCE et RSEE, EUNIS 2012 et 2022, CORINE Biotopes, HabRef, typologies urbaines françaises, zones biogéographiques, trame verte et bleue, méthodes ERC (ASDEC, MNEFZH, CGDD), arrêté du 27/12/2018, Effinature), `E_pression_reponse_ecologie.md` (50 fiches d'écologie quantitative en 9 thèmes : aire-espèces, routes et clôtures, lumière, bruit, vitrages, sol et substrat, eau, maturation et échec des créations, courbe de récupération de GLOBIO). 101 fiches au total, chacune avec l'URL et son mode de vérification (page ouverte, fichier téléchargé et lu en entier, ou seulement vu dans un résultat de recherche), la licence, l'accessibilité, les limites de transposition et les valeurs relevées avec leur emplacement.

Règle d'emploi : les fiches 2.1 à 2.7 restent la lecture de référence ; A à E les complètent. Elles apportent des sources que 2.1 à 2.7 n'ont pas ouvertes, dont : la grille du Bade-Wurtemberg (ÖKVO, échelle 1 à 64), la directive (UE) 2025/2360 sur la surveillance des sols, le guide des règles environnementales du PLU bioclimatique de Paris (juin 2025), le PLU2 de Lille, le guide ERC du SDAGE Seine-Normandie (janvier 2024), la méthode MUSE (Cerema et ADEME 2022), le guide de la Station ornithologique suisse de Sempach sur le verre et la lumière, Broughton 2021 et 2022 sur le réensauvagement passif. Quand une valeur d'A à E entre dans `donnees/` au lot 1, c'est la fiche qui fournit `source`, `reference_precise` et `url`. Au lot 1, les fiches sont déplacées dans `methode/bibliographie_fiches/`, à côté de `methode/bibliographie.md`, qui renvoie à chaque fiche par son titre.

Divergences et compléments entre A à E et 2.1 à 2.7, arbitrés ici :
- Licence du GBS : la fiche C n'avait trouvé aucune mention de licence sur les 5 PDF qu'elle a ouverts ; la fiche 2.3 a lu la mention CC BY-NC 4.0 (« Contact us for commercial uses ») dans le rapport sectoriel Construction de juin 2026. La lecture de 2.3 prévaut, la fiche C est corrigée en ce sens, le GBS reste exclu (P14).
- Carbone 4 : la fiche C n'a lu que la page de présentation ; la fiche 2.4 a lu le PDF complet de 30 pages. La fiche 2.4 prévaut (parts de 11 % usage des sols, 51 % pollution, 38 % climat ; point P19).
- Paris : la fiche 2.5.3 marque le règlement du PLU bioclimatique « NON VÉRIFIÉ » ; la fiche B a lu le guide des règles environnementales du PLUb (juin 2025, 68 pages) : IVB à 5 coefficients (UG.4, p. 63) et SELC. Ce complément suffit pour `sols.csv` (P12) ; le règlement lui-même reste à lire au lot 1.
- Métrique anglaise : la fiche A et la fiche 2.1 lisent les mêmes fichiers (tableur statutaire 1.0.4, guide de juin 2026, classeur des fiches d'état) et concordent sur les valeurs comparées ici : bandes de distinctivité 8 / 6 / 4 / 2 / 0, états 3 / 2 / 1, multiplicateurs de situation 1,15 / 1,10 / 1,0, facteur temporel 0,965^t plafonné à 30 ans et plus, difficultés 1 / 0,67 / 0,33 / 0,1, risque spatial 1 / 0,75 / 0,5.

## 3. Couverture des 10 tables de données

Méthode de comptage : pour chaque table, le nombre de valeurs nécessaires est estimé d'après le périmètre v1 proposé au § 4 (environ 130 types d'habitats dont 26 types urbains et hors-sol (VB.1 à VB.26, § 4.3), 4 zones biogéographiques, 13 lots de matériaux, 7 modules). Les taux sont des estimations de lot 0, pas des décomptes de lot 1. « Sourcé » veut dire : une valeur lue dans une source primaire ou réglementaire, reprise telle quelle ou par une correspondance de nomenclature. « Convention » veut dire : une valeur que Vi-BCN devra fixer et justifier par écrit (C1, C2...), faute de source. Les sections 2.1 à 2.7 citées sont celles de l'inventaire.

| Table | Contenu | Source pressentie (fiche) | Valeurs nécessaires (estimation) | Couverture sourcée | Trous imposant une convention |
|---|---|---|---|---|---|
| `habitats.csv` | nomenclature, valeur intrinsèque, délai de maturité, difficulté de création, modulation par zone | Nomenclature : EUNIS 2012 niveau 3, EEA, CC BY 4.0 (2.5.5). Valeur intrinsèque : BKompV Anlage 2, 668 valeurs 0 à 24 (2.2), complétée par la KV Hesse pour toitures et façades (10.720 = 19, 10.730 = 13, 10.741 = 19, 10.743 = 13) ; contrôle d'ordre de grandeur par MSA_LU (2.3) et par les bandes UK 8/6/4/2/0 (2.1). Délai de maturité : tableur statutaire UK G-4 par habitat et par condition cible (2.1), classes BKompV Anlage 5 B et W bavarois (2.2), taux de récupération de Jones 2018 et Moreno-Mateos 2012 (2.6.7). Difficulté : tableur UK G-3, 1 / 0,67 / 0,33 / 0,1 (2.1) | 130 types × 4 champs = 520 | Valeur intrinsèque : 130/130 par correspondance (chaque correspondance EUNIS vers code allemand est une convention de transposition, la valeur est sourcée). Délai : environ 115/130 (UK + DE ; les habitats méditerranéens et plusieurs habitats français n'ont pas d'équivalent UK). Difficulté : environ 115/130 (UK). Modulation par zone : 0/130. Total environ 360/520, soit 69 % | (1) la correspondance EUNIS vers BKompV / Hesse / UK, à écrire type par type ; (2) le rééchelonnage des 4 échelles allemandes entre elles (non linéaire, 2.2 § 6.1) ; (3) les délais des habitats méditerranéens ; (4) toute modulation biogéographique ; (5) les stades d'âge J / M / A des boisements et haies à exprimer en années (la Handreichung BKompV donne jeune < 30 ans, moyen 30 à 80, âgé > 80, 2.2 § 5.1) |
| `etat_criteres.csv` | grilles de critères d'état par grand type d'habitat et règle de score | Technical Annex 1 UK (classeur des fiches d'état, OGL v3) : fiches 5A prairies basses (7 critères), 6A prairies moyennes et hautes (5 à 6 critères), 22A urbain (3 critères + critères spécifiques toitures, noues, OMHPDL), 9A arbres isolés (6 critères), 8A haies (10 attributs), 24A boisements (13 indicateurs notés 1 à 3), plus fiches non lues (landes, zones humides, mares, lacs) (2.1). Règles allemandes de correction : ± 3 points sur 24 selon 3 critères (BKompV § 5), 8 Beurteilungsgrößen de la Hesse (2.2) | environ 12 grands types × (6 critères + 1 règle de score) = 85 | Structure des grilles et règles de score : environ 60/85 (fiches UK lues) ; listes d'espèces indicatrices françaises : 0 (les fiches UK renvoient à des listes anglaises : Schedule 9 WCA, Hedgerow Survey Handbook) | (1) les listes d'espèces indicatrices et d'espèces exotiques envahissantes à substituer (sources candidates au lot 1 : listes réglementaires françaises des EEE, listes rouges régionales) ; (2) la grille d'état des habitats méditerranéens ; (3) le passage du score de grille au facteur d'état (point P7) |
| `sols.csv` | coefficient de fonctionnalité par nature de sol et épaisseur de substrat | Valeurs réglementaires ou locales : Berlin BFF après 2019 (imperméable 0 ; semi-perméable 0,1 ; perméable 0,2 ; perméable végétalisé 0,4 ; sur dalle 20 à 40 cm 0,5, 41 à 80 cm 0,6, 81 à 150 cm 0,7, > 150 cm 0,9 ; pleine terre 1,0 ; toiture extensive 0,5, simple intensive 0,7, intensive 0,8) (2.5.3) ; Strasbourg 2026 (1 / 0,9 / 0,7 / 0,6 / 0,5 / 0,4 / 0,2 / 0) ; plafonds Cerema 0,1 / 0,3 / 0,5 (2.6.5, 2.7) ; Grand Annecy 2026 (0 / 0,3 / 0,5 / 0,5 / 0,7 / 1) (2.5.3) ; grilles complémentaires lues dans les fiches B et E (§ 2.9) : Londres UGF 2023, Paris PLU bioclimatique 2025 (IVB), Lille PLU2, Montreuil, SDAGE Seine-Normandie 2024. Valeurs écologiques mesurées : GROOVES (plateau floristique à environ 25 cm ; arthropodes 19 / 32 / 55 / 59 espèces selon wildroof / extensif / semi-intensif / intensif) (2.6.5) ; Biotopwerte des sols nus et revêtements (BKompV 52.x : 0 / 2 / 3 / 4 / 6 ; Hesse 10.5xx : 3 / 6 / 7 / 9) (2.2) ; O'Riordan 2021 (carbone -37 %, matière organique -55 % sous sol scellé) | 12 natures de sol × 1 à 4 classes d'épaisseur = environ 30 | Environ 30/30 par des valeurs réglementaires ou locales, dont le Cerema dit qu'elles sont des « indicateurs d'occupation des sols (et non de biodiversité) » et des choix « fixés par les experts » ; environ 10/30 confortées par une donnée écologique mesurée (toitures : GROOVES ; sols scellés : Biotopwerte, O'Riordan) | (1) la règle de construction des coefficients, proposée au point P12 (fusion VIBCN) : médiane des grilles publiées, plage égale à leur étendue, classes d'épaisseur fixées par GROOVES et MUSE ; la médiane de grilles d'urbanisme reste une convention, pas une mesure écologique ; (2) la fonction richesse = f(épaisseur) au-delà du plateau de 25 à 30 cm (aucune équation lue) ; (3) la faune du sol sous imperméabilisation (aucune donnée) |
| `connectivite.csv` | paramètres aire-espèces, distances, effets des obstacles | Exposant z : Matthews 2016 (îles d'habitat : médiane 0,22, Q1-Q3 0,16 à 0,32 ; urbain 0,27) ; Sólymos et Lele 2012 (0,228) ; Drakare 2006 (0,27, lu en source secondaire) (2.6.1). Effet de taille GLOBIO : Alkemade 2009 Table 7 (< 1 km² 0,3 ; < 10 0,6 ; < 100 0,7 ; < 1 000 0,9 ; < 10 000 0,95 ; > 10 000 1,0, avec SE) ; GLOBIO 3.5 Table 6.1 ; régression GLOBIO 4 (coefficients -0,774 et 0,594 sur log10 km²) (2.3). Seuils urbains : Beninde 2015 (4,4 ha espèces adaptées, 53,3 ha espèces sensibles). Routes : Benítez-López 2010 (MSA par classe de distance, pentes par milieu ; oiseaux 0,678, mammifères 0,675) ; GLOBIO 4 routes (-1,772 et 1,391) ; Jacobson 2016 (classes de trafic) (2.6.1, 2.3). Situation dans la trame : définitions R. 371-19 (2.5.2), multiplicateurs UK 1,15 / 1,10 / 1,0 et risque spatial 1 / 0,75 / 0,5 (2.1). Clôtures : prescriptions dimensionnelles seulement (15 x 15 cm tous les 10 à 20 m ; 10 cm sous les portails) (2.6.1) | effet de taille (1 relation + bornes) ; distance aux réservoirs (3 classes) ; obstacles (voiries 3 classes de trafic × 2 groupes ; clôtures 4 types) ; environ 25 | Effet de taille : sourcé, mais toutes les relations lues sont calibrées pour des taches de 1 ha à plusieurs km², jamais pour des jardins de quelques centaines de m² ; distances et multiplicateurs de trame : sourcés par transposition UK (convention) ; voiries : sourcé pour les routes à trafic (distance d'effet), rien pour les voiries internes (< 500 véh/j) ; clôtures : 0 valeur d'efficacité. Environ 15/25 | (1) l'extrapolation de la relation aire-espèces sous 1 ha ; (2) la perméabilité d'une clôture (aucun taux de franchissement lu) ; (3) l'effet d'une voirie interne à faible trafic ; (4) la définition opérationnelle de « contigu » entre unités |
| `nuisances.csv` | relations pression-réponse : lumière, bruit, vitrages | Lumière : arrêté du 27/12/2018 (3 000 K ; ULR < 1 % ; densités de flux 10 à 35 lm/m² selon le cas ; extinction à 1 h ; 2 400 K et 2 700 K en espaces protégés) ; distances d'évitement des chiroptères 10 / 25 / 50 m (Azam 2018 via EUROBATS) ; 25 % de l'éclairement sans effet mesuré (Rowse 2018) ; seuil de ciel 21,3 mag/arcsec² (guide Trame noire) ; formule de barrière de Hale 2015 pour une espèce ; Sanders 2021 : aucune relation dose-effet trouvée en méta-analyse (2.6.2). Bruit : Shannon 2016 (réponses dès 40 dBA, 20 % des études sous 50 dBA) ; Reijnen 1997 (seuils 42 à 52 dB(A) en boisement, 47 en prairie ; réduction de densité ≥ 30 % au-dessus ; distances d'effet par trafic) ; Francis et Barber 2013 (+5 à +10 dB réduisent les effectifs d'oiseaux) (2.6.3). Vitrages : Loss 2014 (2,1 / 21,7 / 24,3 oiseaux par bâtiment et par an selon la hauteur) ; Vogelwarte (× 3,6 avec arbres hauts, × 3 avec miroir ; réflexion 8 / 25 à 60 / 80 à 90 %) ; classes d'efficacité des marquages A ≤ 10 % d'approches (Rössler 2010, WUA 2022) ; ABC TF ≤ 30 = réduction ≥ 50 % ; Klem 2013 (55 %, ≥ 59 %) ; LEED SSpc55 (zone 1 = 36 pieds) (2.6.4) | lumière : 3 relations (éclairement, température de couleur, horaires) × 3 groupes ; bruit : 2 seuils + 1 pente ; vitrages : 3 facteurs de risque + 4 classes de traitement ; environ 30 | Lumière : seuils et distances sourcés (environ 8/12), relation continue 0 ; bruit : seuils sourcés (4/6), courbe 0 ; vitrages : facteurs sourcés comme ordres de grandeur (6/9), efficacité des traitements sourcée (4/4). Environ 22/30 en seuils, 0 en relations continues | (1) le passage des seuils à un coefficient continu par unité d'habitat (forme à seuil recommandée, comme Reijnen) ; (2) l'effet de la température de couleur (l'arrêté fixe 3 000 K sans courbe écologique) ; (3) la mortalité par m² vitré en France (données américaines et suisses seulement) ; (4) la part de vitrage « exposée » (zone 1 LEED à transposer en mètres) |
| `eau.csv` | coefficients hydriques | Mares et zones humides créées : Williams 2008 et FHT (20 % des espèces de zones humides du Royaume-Uni en 7 ans ; plateau à 70 plantes et 100 invertébrés à 25 ans ; richesse maximale dans les 5 premières années) ; Moreno-Mateos 2012 (vertébrés 5 ans, invertébrés 5 à 10, plantes 30, fonctions 74 à 79 % à 30 à 100 ans) ; UK G-4 mares 5 / 4 / 3 / 2 / 1 ans (2.6.6, 2.1). Infiltration : équivalences DRIEAT 1 : 1 (pleine terre, noue, jardin de pluie), 1 : 0,5 (toiture végétalisée), 1 : 0,1 (enrobé poreux) ; Berlin infiltration 0,2 par m² de toiture ; Londres jardins de pluie 0,7, bassins non plantés 0,2 (2.5, 2.6.5) ; Hesse 10.715 (toiture avec infiltration 6 contre 3) (2.2) | délais et valeurs des milieux humides (6) ; part infiltrée (1 relation) ; ouvrages (noue, bassin, jardin de pluie : 3) ; environ 10 | Milieux humides : 6/6 (délais sourcés) ; ouvrages : 3/3 par valeurs réglementaires ou locales ; part infiltrée vers biodiversité : 0/1. Environ 9/10, dont 3 par convention locale | (1) la relation entre part des eaux pluviales infiltrées et valeur écologique (aucune donnée lue ; le lien n'est documenté que par des équivalences de compensation) ; (2) la distinction bassin de rétention / mare d'eau propre, qualitative seulement |
| `contexte.csv` | multiplicateurs de situation et zones biogéographiques | Zones : couche EEA 2016, CC BY 4.0, 4 régions terrestres en métropole (alpine, atlantique, continentale, méditerranéenne) (2.5.6). Multiplicateurs : UK 1,15 / 1,10 / 1,0 (2.1) ; Hesse doublement de la Zusatzbewertung en site protégé ; BKompV + 3 points pour « Lage zu anderen Biotopen » (2.2) ; définitions françaises R. 371-19 (2.5.2) | 4 zones + 3 situations + typologies = environ 12 | Zones : 4/4. Multiplicateurs : 3/3 par transposition UK (convention). Table zone par commune ou département : 0 (à construire par intersection SIG avec la couche EEA) | (1) la transposition des multiplicateurs UK à la trame verte et bleue française ; (2) l'affectation de la zone au projet (saisie, avec aide par département au lot 1) |
| `materiaux.csv` | occupation des sols par matériau, facteurs de caractérisation, plages d'incertitude | Facteurs de caractérisation : LC-IMPACT v2 chapitre 14 (MSA-loss km²/km² pour la France : cultures 0,626, pâturages 0,586, plantations 0,462, urbain 0,716, mines 1,49 ; CC BY 4.0) ; GLOBIO 3.5 MSA_LU (plantation 0,30, coupe rase 0,50, sélective 0,70, RIL 0,85, cultures 0,10 à 0,30, pâturages 0,30 à 0,60, urbain 0,05) ; LC-IMPACT v2 chapitre 6 (PDF global par m² et par m²·an, France : urbain et carrière 6,089e-14, cultures 2,121e-14, forêt intensive 1,397e-14, extensive 6,894e-15, plantation intense 4,804e-14) ; ReCiPe 2016 (0,30 / 0,55 / 1,00 / 0,70 / 0,33 / 0,73 annual crop eq ; temps de récupération 73,5 ans forêt, 7,5 ans milieux ouverts) ; EF 3.1 LANCA (Pt, services du sol, pas biodiversité) ; temps de régénération : Koellner 2013, EF 85 ans artificiel et 20 ans biotique (2.4). Inventaire d'occupation (m²·an par kg ou m³) : aucune source ouverte (les FDES publient le SQP, sans flux ; ecoinvent sous licence ; GBS sous licence ; Carbone 4, lu en entier, ne publie ni ses proxys ecoinvent ni ses facteurs IMPACT World+ et confirme p. 20 que les FDES ne couvrent ni l'occupation et la transformation des terres ni l'écotoxicité) (2.4). Contrôle d'ordre de grandeur : Carbone 4 2026, bâtiment type de 3 000 m², 272 000 PDF.m².yr en A1-A3 (environ 91 par m² de plancher), répartition par lot lue sur graphique, usage des sols 11 % du total (2.4). Plages d'incertitude : SE d'Alkemade 2009 ; aucune pour LC-IMPACT (2.3, 2.4) | 13 lots × environ 6 matériaux types = 80 inventaires d'occupation ; 8 facteurs de caractérisation ; 8 temps de régénération ; environ 100 | Facteurs de caractérisation : 8/8 (France, licence libre). Temps de régénération : 8/8 (choix de valeur entre sources). Inventaires d'occupation par matériau : 0/80. Total environ 16/100 | Le trou le plus grave de la méthode : (1) l'occupation des sols par kg ou m³ de chaque matériau, à construire par convention (point P8) ; (2) la conversion entre MSA, PDF et m²HE (aucune conversion lue) ; (3) la localisation de l'origine des matières ; (4) l'incertitude des facteurs |
| `seuils.csv` | seuils proposés et coefficients Mnat | Aucune source directe. Points de repère : gain net de 10 % (Environment Act 2021) ; Berlin BFF cibles 0,60 / 0,45 / 0,30 ; Londres UGF 0,4 / 0,3 ; Strasbourg CBS 25 à 50 % ; ARB îdF pleine terre 20 et 30 %, CBSh 0,30 et 0,50 ; SDRIF-E 30 % de pleine terre hors voirie ; DRIEAT 150 % ; règlement (UE) 2024/1991 seuils d'exclusion 45 % d'espaces verts et 10 % de couvert arboré (2.1, 2.5, 2.7) ; niveaux Effinature (référentiel non lu, 2.8) | environ 4 niveaux × 3 typologies × 3 indicateurs = 36 | 0/36 sourcé ; 100 % convention « en attente de validation du Biodiversity Standards Council », avec points de repère cités | (1) les seuils eux-mêmes (point P13) ; (2) les modulations Mnat par typologie, zone et taille de parcelle ; (3) le raccordement aux niveaux Effinature, qui suppose le référentiel (point P16) |
| `conventions.csv` | index des conventions Vi-BCN | Interne, sur le modèle de `docs/lectures.md` d'OpenBCE (1.2) | sans objet | sans objet | sans objet |

Bilan : sur les 7 tables de coefficients écologiques, les valeurs intrinsèques, les délais, les difficultés, les seuils de nuisance et les facteurs de caractérisation des usages des sols sont sourçables ; ce qui ne l'est pas, c'est, dans l'ordre de gravité : l'inventaire d'occupation des sols par matériau (module G), les relations continues dose-réponse des nuisances, la perméabilité des clôtures, la relation aire-espèces sous 1 ha, et les seuils. Toutes ces lacunes ont des points de repère sourcés qui bornent la convention ; aucune n'est une page blanche.

Deux contraintes d'accès découvertes pendant l'audit, à inscrire dans `docs/sources.md` du moteur : Legifrance, EUR-Lex et iso.org bloquent les accès automatisés depuis cet environnement (les textes ont été lus sur codes.droit.org, AIDA, le Conseil d'État, les portails ministériels et des copies officielles) ; les serveurs de l'INPN sont inaccessibles « pour une durée indéterminée » à la suite d'une attaque informatique (HabRef v7 a été récupéré sur la page temporaire de PatriNat).

## 4. Nomenclature d'habitats : proposition

### 4.1 Ce que les sources permettent

- EUNIS 2012 (EEA, CC BY 4.0) : 326 habitats au niveau 3, 11 groupes, fichiers tabulaires téléchargeables, crosswalks officiels vers l'annexe I de la directive Habitats, la Résolution 4 de Berne, Corine Land Cover et la Liste rouge européenne des habitats (2.5.5).
- EUNIS révisé 2021 et 2022 (EEA, CC BY 4.0) : révision jusqu'au niveau 3 pour 7 groupes terrestres (dont V « Vegetated man-made habitats » : jardins, pelouses, haies, alignements, vergers) ; les eaux continentales (P) et les complexes (Z) ne sont pas révisés ; les habitats bâtis non végétalisés de l'ancien groupe J ne figurent pas dans la révision lue ; codes différents de 2012.
- CORINE Biotopes (1991, version française ENGREF 1997) : 2 594 unités dans HabRef, 1 486 présentes ou à rechercher en France ; c'est la typologie des diagnostics écologiques français depuis 30 ans ; HabRef fournit la correspondance CORINE Biotopes vers EUNIS 2012 (fichier CRSP_CB_EUNIS_2012_70.xlsx).
- HabRef v7 (PatriNat, 07/08/2025) : toutes les typologies et correspondances (EUNIS 2012 et 2022, CORINE, Paléarctique, HIC, PVF2), mais licence non indiquée et serveurs INPN hors service ; v8 annoncée.
- Le guide CGDD 2021 recommande EUNIS niveau 3 pour les enjeux faibles et niveau 4 et plus pour les enjeux forts (2.7 § 1).
- Les listes allemandes (BKompV 668 types, Hesse 243 types valorisés) et la liste UK (UKHab, licence propre non lue) ont leurs propres typologies, sans correspondance publiée vers EUNIS (2.2 § 6.2, 2.1 § 5.1).

### 4.2 Proposition

1. Code pivot : EUNIS 2012 au niveau 3 (326 codes), restreint aux habitats présents en France métropolitaine. Raisons : licence CC BY 4.0 de l'EEA, stabilité de la version 2012 (seules les descriptions ont changé en 2012 et 2019), correspondance officielle vers CORINE Biotopes par HabRef (donc compatibilité avec les diagnostics écologiques existants), correspondance vers la Liste rouge européenne des habitats (source candidate pour la composante « rareté et menace » de la valeur intrinsèque, à lire au lot 1 dans les fichiers EEA déjà téléchargés) et recommandation du guide CGDD. Le code EUNIS 2022 est porté en colonne secondaire par la correspondance HabRef, pour ne pas fermer la migration.
2. Niveau 4 autorisé : quand l'écologue dispose d'un diagnostic au niveau 4, le moteur l'accepte et remonte la valeur du niveau 3 sauf si une ligne spécifique de `habitats.csv` existe au niveau 4 (cas prévus : prairies, boisements, zones humides).
3. Extension urbaine et hors-sol « VB » (fusion VIBCN) : les codes EUNIS J (bâti, réseaux, décharges) et I2 (jardins) distinguent les habitats par leur usage, pas par leur valeur écologique. Une liste de 26 types, codés VB.1 à VB.26, est nécessaire ; elle est donnée au § 4.3. Le code VB est court, stable et indépendant de la coexistence d'EUNIS 2012 (groupe J) et d'EUNIS 2022 (groupe V) : le parent EUNIS est une colonne, pas le code, ce qui le fait survivre à la révision du groupe J par l'EEA (la première version de ce document codait sous le parent : J4.6-U1, I2.2-U1). Chaque type porte sa correspondance vers EUNIS 2022 et 2012 (HabRef 7.0), CORINE Biotopes (HabRef), la catégorie de la nomenclature ZAN (2.5.1) et les sources de valeur lues à la source avec leur emplacement : type UK (onglet G-1 et fiche 22A), codes BKompV (34.x, 39.x, 41.x, 51.x, 52.x, 53.x), Hesse (02.xxx, 04.xxx, 09.xxx, 10.5xx, 10.7xx, 11.2xx), Bavière, NRW, facteurs de Berlin (BFF 2019) et de Londres (Table 8.2 et Table 3.1) et, selon le type, Paris, Lille, Montreuil et SDAGE ; chaque type a de 1 à 8 valeurs de référence, 24 types sur 26 en ont au moins 2.
4. Haies, alignements et arbres isolés : unités surfaciques, et non modules linéaires séparés comme au Royaume-Uni (point P11) : une haie est saisie en longueur × largeur (largeur minimale 1 m), un arbre en surface de houppier projetée ; les arbres plantés sont des unités dont la surface de houppier croît par la courbe de maturation du module T.
5. Les habitats littoraux et marins (EUNIS A et B hors B1 et B3 terrestres), les habitats d'outre-mer et les complexes (X) sont hors v1.
6. Fichier de nomenclature livré au lot 1 : `donnees/nomenclature.csv` avec les colonnes code_vibcn, code_eunis_2012, code_eunis_2022, code_corine, libelle_fr, groupe, type (sol, dalle, hors-sol, eau, linéaire), categorie_zan, source de la correspondance, et une colonne par source de valeur (code et valeur lus, avec l'emplacement).

### 4.3 Liste des types urbains et hors-sol VB.1 à VB.26 (fusion VIBCN)

La liste de l'audit VIBCN comptait 21 types ; 5 types de l'extension initiale de ce document qu'elle n'avait pas y sont ajoutés (VB.22 à VB.26, signalés) : 26 types. Les bornes d'épaisseur de substrat sont celles du point P12 (15 cm, 30 cm, 80 cm). Les sources de valeur sont citées par leur code et leur valeur sur leur échelle propre ; leur emplacement exact est dans les fiches 2.1, 2.2, 2.5 et dans les fiches A et B (§ 2.9).

| Code | Type et bornes | Parent EUNIS 2022 / 2012 | CORINE | ZAN | Sources de valeur lues (2.1, 2.2, 2.5 ; fiches A et B) |
|---|---|---|---|---|---|
| VB.1 | Surface imperméabilisée bâtie (emprise de construction) | J1 ou J2 (2012) | 86.1, 86.2 | 1° | BKompV 53.01 (biotopes complexes, 2 à 13) ; Hesse 10.710 toiture nue 3 ; Bavière X4 bâtiment 0 ; NRW HN 0 ; métrique anglaise u1b developed land sealed surface, distinctivité 0 ; Berlin 0 ; Londres 0 |
| VB.2 | Surface imperméabilisée non bâtie (voirie, parking, dallage à joints étanches) | J4.2, J4.6 (2012) | 86 | 2° | BKompV 52.01.01a, 52.02.01a, 52.03.01 : 0 ; Hesse 10.510 et 10.520 : 3 ; Bavière V11 : 0 ; NRW me1/me2 : 0 ; métrique anglaise u1b : 0 ; Berlin 0 ; Londres 0 |
| VB.3 | Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés) | J4.6 (2012) | 86 | 3° | BKompV 52.01.03 : 2, 52.02.03 et 52.03.02 : 3, 52.03.03a : 4 ; Hesse 10.530 : 6 ; Bavière V12 : 1 ; NRW me3/mf1 : 1 ; métrique anglaise u1c artificial unvegetated unsealed surface ; Berlin 0,1 et 0,2 ; Londres 0,1 ; Strasbourg 0,2 ; Grand Annecy 0,3 ; Lille 0,25 |
| VB.4 | Revêtement perméable végétalisé (dalles alvéolées engazonnées) | J4.6 (2012) | 86 | 3° | Hesse 10.540 : 7 ; Berlin 0,4 ; Grand Annecy 0,5 (semi-ouvertes) ; Lille 0,5 ; aucune ligne BKompV ni anglaise |
| VB.5 | Pelouse d'agrément tondue, terrain de sport engazonné | V3-1 (2022) | 85.12 | 4° | BKompV 34.09 Tritt- und Parkrasen : 8 ; Hesse 11.224 : 10 ; Bavière G4 : 3 ; NRW mc1 : 2 ; métrique anglaise modified grassland (délais 7 / 5 / 4 / 2 / 1) ; Londres 0,4 |
| VB.6 | Massif ornemental horticole, couvre-sol planté | V2 (2022) | 85.14 | 4° | BKompV 51.07a.02 : 9 (13 avec vieux arbres) ; Hesse 11.221 : 14 ; métrique anglaise introduced shrub (code 847, 1 an, sans état) ; Londres 0,5 (couvre-sol), 0,7 (vivaces fleuries) |
| VB.7 | Jardin domestique végétalisé | V2-2 (2022), X24 et X25 (2012) | 85.31 | 4° | BKompV 51.08a.01 : 11 (riche), 51.08a.02 : 7 ; Hesse 11.221 : 14, 11.222 : 25, 11.223 : 20 ; Bavière P21 : 5, P22 : 7 ; NRW ka4 : 2, ka6 : 4 ; métrique anglaise vegetated garden (828), distinctivité 2, sans état |
| VB.8 | Friche urbaine herbacée | V3-7 à V3-9 (2022), J1.5 (2012) | 87.1, 87.2 | 4° ou 5° | BKompV 51.04a.01 : 12, 51.04a.02 : 7, 39.05 : 7 ; Hesse 09.123 : 25, 09.124 : 41 ; Bavière P431 à P433 : 2, 4, 8 ; NRW neo6 : 3, neo7 : 4 ; métrique anglaise open mosaic on previously developed land (80), distinctivité 6, délais 10 / 7 / 4 / 2 / 0 ; vacant or derelict land (82) |
| VB.9 | Friche urbaine arbustive (plus de 50 % de ligneux) | S (2022) selon l'espèce dominante | 87.1 | 4° ou 5° | BKompV 39.06 : 12 à 16 selon la station ; NRW : évaluée comme forêt sur station artificielle ; métrique anglaise mixed scrub (délais 10 / 7 / 5 / 3 / 1) |
| VB.10 | Sol nu, chantier, terrassement | J1.6 (2012) | 86 | 5° | BKompV 51.01 : 5 ; Bavière O7 : 1 ; métrique anglaise bare ground (510), vacant or derelict land (82), délais 5 / 4 / 3 / 2 / 1 |
| VB.11 | Toiture végétalisée extensive (substrat de moins de 15 cm) | J1 ou J2 (2012), hors-sol | sans code | 1° | Hesse 10.720 : 19 ; NRW mi1 : 1 (seulement avec plus de 30 cm et plus de 30 % de ligneux) ; métrique anglaise other green roof (89, 1 an, sans état) ; Berlin 0,5 ; Londres 0,7 ou 0,3 ; Strasbourg 0,5 (moins de 10 cm) ou 0,6 |
| VB.12 | Toiture végétalisée semi-intensive (15 à 30 cm) | J1 ou J2 (2012), hors-sol | sans code | 1° | métrique anglaise biodiverse green roof (87), distinctivité 4, délais 10 / 8 / 5 / 3 / 1, difficulté medium ; Berlin 0,7 ; Londres 0,8 ; Strasbourg 0,6 ; Lille 0,6 |
| VB.13 | Toiture végétalisée intensive (plus de 30 cm) | J1 ou J2 (2012), hors-sol | sans code | 1° | Hesse 10.730 : 13 ; métrique anglaise intensive green roof (88), délais 5 / 4 / 3 / 2 / 1, difficulté low ; Berlin 0,8 ; Londres 0,8 ; Strasbourg 0,7 ; Paris 0,8 (50 cm et plus) |
| VB.14 | Dalle ou toiture à substrat profond (plus de 80 cm), assimilable à un sol reconstitué | J1 ou J2 (2012), hors-sol | sans code | 1° | Berlin 0,7 (81 à 150 cm), 0,9 (plus de 150) ; Strasbourg 0,9 ; Grand Annecy 0,7 ; Paris 1,0 ; Lille 1 (1 m et plus) ; Montreuil 0,6 ; MUSE : sols sur dalle exclus de la pleine terre (fiche E) |
| VB.15 | Façade végétalisée enracinée au sol (plantes grimpantes) | J1 ou J2 (2012), hors-sol vertical | sans code | 1° | métrique anglaise ground based green wall (842), difficulté medium ; Berlin 0,5 jusqu'à 10 m ; Londres 0,6 ; Strasbourg 0,4 ; Paris 0,2 jusqu'à 15 m ; Lille 0,4 jusqu'à 10 m |
| VB.16 | Façade végétalisée hors sol (bacs, modules) | J1 ou J2 (2012), hors-sol vertical | sans code | 1° | métrique anglaise facade-bound green wall (843) ; Berlin 0,7 jusqu'à 20 m, 10 imputés ; Londres 0,6 ; Strasbourg 0,4 |
| VB.17 | Haie (saisie en longueur et largeur, point P11) | V4-1 à V4-4 (2022) selon le caractère indigène et la richesse | 84.2 | 4° | BKompV 41.03.03 : 12 / 16 / 19 (J / M / A), 41.04 non indigène : 8 / 11 / 14 ; Hesse 02.200 : 39, 02.500 non indigène : 20, 02.510 urbaine indigène : 30, 02.600 nouvelle : 20 ; Bavière B141 : 5, B142 : 3 ; métrique anglaise 13 types de haies, distinctivité 1 à 8, délais 1 / 5 / 12 (haie indigène), 1 / 10 / 20 (avec arbres) ; Londres 0,6 |
| VB.18 | Arbre isolé ou alignement (saisi en nombre, classe de diamètre et origine, point P11) | V6-3 (2022) | 84.1 | 4° | BKompV 41.05a indigène : 11 / 15 / 18, 41.05b non indigène : 8 / 11 / 14, 41.05.04 allée : 11 / 16 / 19 ; Hesse 04.110 indigène : 34, 04.120 exotique : 23 ; Bavière B311 à B313 : 5 / 9 / 12 ; métrique anglaise urban tree (NE0014), distinctivité 4, surfaces 0,0041 / 0,0163 / 0,0366 / 0,0765 ha par classe de diamètre, délais 30+ / 30+ / 27 / 19 / 10 ; Londres 0,8 (fosse connectée) ou 0,6 |
| VB.19 | Noue, jardin de pluie, bassin paysager alimenté en eau de pluie | J5 (2012) ou C (2012) selon la permanence de l'eau | 89.2 | 6° ou 4° | métrique anglaise SuDS (848), bioswale (849), rain garden (850), difficultés medium / medium, medium / low, low / low, délais 5 / 4 / 3 / 2 / 1 (bioswale 3 / 2 / 1 / 1 / 1) ; Berlin 0,2 (infiltration) ; Londres 0,7 ; SDAGE 1 ou 0,7 à 0,8 |
| VB.20 | Mare créée ou plan d'eau à berges naturelles | C1 (2012), puis Q à la v8 de HabRef | 22.1 | 6° | métrique anglaise ponds (priority et non priority), délais 5 / 4 / 3 / 2 / 1, difficulté low / medium (non priority) ; Londres 1 (zone humide) ; Berlin 0,5 ; mares nouvelles : 10,2 espèces contre 7,9 (Williams 2010, fiche E) |
| VB.21 | Bassin, fontaine ou plan d'eau à eau traitée | J5.3, J5.5 (2012) | 89.2 | 6° | Londres 0,2 (eau chlorée) ; aucune ligne allemande ni anglaise |
| VB.22 (de l'extension initiale) | Potager, jardin partagé, jardin familial | V1 (2022) | 85.32 | 4° | BKompV 51.08a.01 : 11, 51.08a.02 : 7 (jardins familiaux) ; Hesse 11.211 Grabeland : 19 ; métrique anglaise allotments (616), délai 1 an ; Bavière P21 et P22 : 5 et 7 |
| VB.23 (de l'extension initiale) | Jardinière, bac et plantation hors sol au niveau du sol | J1 ou J2 (2012), hors-sol | sans code | 1° | métrique anglaise ground level planters (845), délai 1 an, sans état ; aucune valeur allemande |
| VB.24 (de l'extension initiale) | Bassin de rétention sec ou en eau, non paysager | J5.3 (2012) | 89.2 | 6° ou 2° | Londres 0,2 (bassin de rétention nu) ; métrique anglaise SuDS (848) ; Berlin 0,2 (infiltration) ; SDAGE 0,7 à 0,8 si végétalisé |
| VB.25 (de l'extension initiale) | Voie ferrée, ballast | J4.3 (2012) | 86.43 | 2° ou 3° | BKompV 52.04.01 : 1 ; Bavière V21 : 0, V22 : 1, V23 voie engazonnée : 4 ; aucune ligne anglaise urbaine |
| VB.26 (de l'extension initiale) | Prairie urbaine extensive, fauche tardive, semée ou spontanée | V3-1 si semée et fertilisée, R2 si semi-naturelle (2022) | 85.12 ou 38 | 4° | Hesse 11.225 : 23 ; NRW mc2 : 4 ; métrique anglaise other neutral grassland, délais 10 / 7 / 5 / 3 / 2, difficulté low ; Londres 1 (prairie riche en espèces) |

Notes :
- Les valeurs allemandes sont des points sur leur échelle propre (BKompV sur 24, Hesse sur 80, Bavière sur 15, NRW sur 10) ; les valeurs de Berlin, Londres, Strasbourg, Grand Annecy, Paris, Lille, Montreuil et du SDAGE sont des coefficients de biotope sur 1 ; les distinctivités anglaises sont sur 8. Leur mise sur une échelle commune est l'objet du point P2, non de cette liste ; les coefficients sur 1 alimentent `sols.csv` (P12), les points allemands et anglais `habitats.csv` (P2).
- Les parents 2012 des types hors-sol (J1 ou J2) sont le bâti porteur : un type hors-sol n'entre pas dans le contrôle de fermeture des surfaces au sol.
- 3 lignes de la métrique anglaise citées par code n'ont pas leur distinctivité relevée dans la fiche A (intensive green roof, green walls, SuDS) : à lire dans l'onglet G-1 au lot 1.

Ce qui est écarté de l'extension initiale de ce document :
- Les 2 classes de toitures extensives (moins de 10 cm et 10 à 15 cm) sont fusionnées en VB.11 : aucune source écologique lue ne distingue 10 cm de 15 cm ; GROOVES ne donne qu'un seuil à 25 cm (2.6.5), Paris 2012 un minimum de 8 à 10 cm (fiche E).
- La « toiture biodiverse » n'est pas un type de surface mais un état : la métrique anglaise la définit par des critères (80 à 150 mm de substrat varié, 50 % à 150 mm, fleurs sauvages et sedums, éléments complémentaires ; fiche d'état urbaine, critère G, 2.1 et fiche A) ; elle devient un niveau d'état de VB.12, pas un type.
- Les 3 classes d'âge d'arbres (jeune, moyen, âgé) sont portées par la classe de diamètre de VB.18, qui est ce que l'écologue mesure ; la correspondance diamètre vers stade J / M / A de la BKompV est une convention du lot 1.

### 4.4 Ce qu'il faut encore vérifier

- La licence de HabRef (page INPN inaccessible) : tant qu'elle n'est pas lue, la correspondance CORINE Biotopes est reprise des fichiers EEA là où elle existe, et HabRef n'est cité que comme référence de lecture.
- La Liste rouge européenne des habitats : les catégories par code EUNIS n'ont pas été extraites ; elles le seront au lot 1 depuis le fichier EEA 2021 (colonne Red List) et le rapport Janssen et al. 2016 (à télécharger et lire).
- Pour les 26 types VB du § 4.3 : 24 ont déjà au moins 2 sources de valeur lues ; VB.21 (Londres seul) et VB.23 (métrique anglaise seule) sont à compléter au lot 1 dans la KV Hesse et l'onglet G-1 ; 3 lignes anglaises citées par code n'ont pas leur distinctivité relevée (intensive green roof, green walls, SuDS), à lire dans l'onglet G-1.

## 5. Points de méthode à trancher

Chaque point est présenté seul, avec ce que disent les sources, ma recommandation et la valeur retenue par défaut si le go ne dit rien d'autre. Les points P1 et P16 relèvent de Cédric seul ; les autres deviendront des conventions numérotées au lot 1, soumises au Biodiversity Standards Council avec le texte de la méthode.

### P1. Qui édite la méthode et détient les droits du moteur

Le cahier des charges écrit que Vi-BCN est « éditée par IRICE ». OpenBCE est édité par ARKEMEP (droits ARKEMEP, auteur Cédric PLANTAZ). La répartition des rôles déjà décidée pour les schémas Effinature et BPS place le référentiel chez NORMATYS et la certification chez IRICE.
Recommandation : NORMATYS édite la méthode Vi-BCN et détient les droits du moteur OpenNat, IRICE l'applique dans la certification, le Biodiversity Standards Council la valide ; les en-têtes des livrables du lot 1 et la ligne de droits du code sont écrits en conséquence. C'est le miroir exact d'OpenBCE (méthode d'un éditeur, appliquée par d'autres).
Par défaut : le texte du cahier des charges reste tel quel (IRICE). Ce point ne se tranche pas par défaut : il attend une réponse.

### P2. Échelle de la valeur intrinsèque d'un habitat (de 0 à 1 m²HE par m²)

Sources : MSA GLOBIO (1 seule classe urbaine, 0,05 par avis d'expert dans GLOBIO3 et 3.5, 0,264 à 0,361 par régression dans GLOBIO 4 : 2 générations incompatibles, et aucune valeur pour les milieux urbains fins, 2.3 § 6) ; Biotopwerte allemands (BKompV 0 à 24 sur 668 types, dont une soixantaine de types urbains et périurbains, stades d'âge intégrés ; Hesse 3 à 80 avec toitures et façades ; échelles non convertibles entre elles par un facteur unique, 2.2) ; bandes UK 8 / 6 / 4 / 2 / 0 (calibrées sur la rareté anglaise ; linéarité critiquée par Marshall 2024, qui propose 16 / 8 / 4 / 2, 2.1 § 5).
Recommandation : valeur intrinsèque = Biotoptypenwert de la BKompV divisé par 24, par correspondance EUNIS vers BKompV ; pour les toitures, façades et quelques types urbains absents de la BKompV, valeur de la Hesse rééchelonnée par paires de types d'ancrage communs (convention écrite) ; contrôle d'ordre de grandeur par classe large contre MSA_LU de GLOBIO 3.5 et contre les bandes UK. Raisons : seule la BKompV est à la fois réglementaire, libre de droits (§ 5 UrhG), fine en milieu urbain et graduée par stade d'âge ; la MSA n'a pas la résolution requise ; l'échelle UK est trop grossière et calibrée hors de France. La composante « rareté et menace en France » est ajoutée au lot 1 par la Liste rouge européenne des habitats (crosswalk EEA), par convention bornée.
Par défaut : BKompV / 24.

### P3. Période de référence

Sources : 50 ans pour l'ACV de la RE2020 (période d'étude de référence, article 11 de l'arrêté du 4 août 2021 ; `carbone.py` d'OpenBCE la code) ; 30 ans pour le BNG anglais (Schedule 7A, para. 9(3)), pour la prognose NRW et pour le seuil de majoration de la BKompV ; 25 ans en Bavière ; 3 périodes de végétation en Hesse ; aucune justification scientifique d'une période particulière selon le BfN (Dietrich et al. 2014, 2.2 § 8).
Recommandation : 50 ans, pour l'additivité avec Ic construction et Inat dans la même unité temporelle ; la valeur intégrée à 30 ans est calculée et affichée en indicateur complémentaire, pour la comparabilité avec le BNG et les méthodes allemandes.
Par défaut : 50 ans, avec sortie complémentaire à 30 ans.

### P4. Actualisation

Sources : 3,5 % par an au Royaume-Uni, « the value recommended in the Treasury Green Book », présentée par le texte même comme une technique économique (TA2 § 5.3.1 et 5.3.2 ; 0,965^t, 0,320 au-delà de 30 ans) ; en Allemagne, pas d'actualisation : majoration de surface de 25 % au-delà de 30 ans de développement (BKompV Anlage 5 B), abattement de 1 à 3 points de prognose (Bavière), prognose à 30 ans (NRW), ou rien (Hesse) ; Berlin, historiquement, un taux de 1,13 % sur les coûts au-delà de 5 ans (Bruns 2007).
Recommandation : taux d'actualisation nul. Le module T intègre année par année l'écart entre la valeur cible et la valeur atteinte ; la lenteur de la maturation est donc déjà comptée en m²HE·an perdus (la dette de maturité). Y ajouter une préférence temporelle économique compterait 2 fois le délai et introduirait une valeur monétaire dans une comptabilité écologique. Le taux de 3,5 % est codé comme option d'étude inactive, à la manière des options d'OpenBCE, pour permettre la comparaison avec le BNG.
Par défaut : 0 %, option 3,5 % inactive.

### P5. Bois : origine, régime forestier et certification

Sources : aucun facteur de caractérisation ne distingue un bois certifié d'un bois non certifié ; les facteurs distinguent des régimes : GLOBIO 3.5 plantation 0,30, coupe rase 0,50, coupe sélective 0,70, exploitation à impact réduit 0,85, forêt naturelle 1,0 ; LC-IMPACT v2 pour la France forêt extensive 6,894e-15, forêt intensive 1,397e-14, plantation intense 4,804e-14 PDF global par m² ; Carbone 4 (6 octobre 2026) : une substitution béton vers bois dont la provenance n'est pas maîtrisée peut tripler la pression de changement d'usage des sols et augmenter l'impact biodiversité global d'environ 15 % ; Christiansson et Roos 2023 : la structure bois a 440 à 515 fois l'impact d'usage des sols de la structure béton selon la méthode ; Montilla Moreno 2026 : l'usage des sols fait 70 à 95 % de l'impact des biosourcés (2.3, 2.4).
Recommandation : l'entrée du module G pour le bois est le régime forestier déclaré (forêt naturelle exploitée extensivement, forêt gérée intensivement, plantation, coupe rase) et le pays d'origine ; la certification de gestion forestière n'apporte pas de coefficient propre, elle sert seulement de pièce justificative pour déclarer un régime extensif ou sélectif (convention qui dit quelle certification justifie quel régime) ; sans déclaration, le défaut est « forêt gérée intensivement, origine inconnue » avec la valeur mondiale, non la valeur française.
Par défaut : comme ci-dessus.

### P6. Nomenclature des habitats

Voir § 4. Recommandation : EUNIS 2012 niveau 3 restreint à la métropole, niveau 4 toléré, liste de 26 types urbains et hors-sol VB.1 à VB.26 (§ 4.3, fusion VIBCN) avec correspondances vers EUNIS 2022, CORINE Biotopes, la nomenclature ZAN et les sources de valeurs lues, CORINE Biotopes en code secondaire par HabRef, EUNIS 2022 en colonne de migration.
Par défaut : comme ci-dessus.

### P7. Passage de la grille de critères d'état au facteur d'état

Sources : UK, 3 catégories Good 3, Moderate 2, Poor 1 (donc un habitat en mauvais état vaut 1/3 d'un habitat en bon état), avec catégories « fairly » à 2,5 et 1,5 limitées à un cran, et règles par fiche (critère A essentiel, nombre de critères satisfaits) ; Marshall 2024 propose 4 / 2 / 1 ; BKompV, ± 3 points sur 24 (± 12,5 %) selon 3 critères ; Hesse, ± 3 points par critère et ± 10 au plus (sur 3 à 80) ; Bavière, + 1 point seulement (2.1, 2.2).
Recommandation : facteur d'état = 0,5 + 0,5 × S, où S est le score de la grille entre 0 et 1 (part des critères satisfaits, pondérés), avec un critère essentiel par fiche dont l'échec plafonne S à 0,5 ; le facteur varie donc de 0,5 à 1,0. Raisons : les types allemands intègrent déjà la richesse spécifique dans la valeur intrinsèque (une prairie pauvre en espèces et une prairie riche sont 2 types, 8 et 20), une amplitude de 1 à 3 compterait 2 fois la même chose ; l'amplitude allemande de ± 12,5 % est trop étroite pour une grille de 5 à 7 critères observables. Les 3 catégories UK restent affichées (bon ≥ 0,85, moyen 0,65 à 0,85, mauvais < 0,65) pour la lecture par l'écologue.
Par défaut : 0,5 + 0,5 × S.

### P8. Unité et calcul du module G (biodiversité grise)

Sources : l'unité commune m²HE·an impose une perte de qualité par m²·an d'occupation ; 2 familles de facteurs existent : MSA (GLOBIO via LC-IMPACT v2 chapitre 14, France, licence CC BY 4.0 : cultures 0,626, pâturages 0,586, plantations 0,462, urbain 0,716, mines 1,49 MSA-loss km²/km² ; anomalie de fichier signalée sur la ligne urbaine EXIOBASE) et PDF (LC-IMPACT v2 chapitre 6, ReCiPe 2016, Chaudhary 2015), sans conversion lue entre les deux ; temps de régénération : 73,5 ans (forêt) et 7,5 ans (milieux ouverts) dans ReCiPe, 85 ans (artificiel) et 20 ans (biotique) dans EF 3.1, de 80 à 1 186 ans dans LC-IMPACT v2 ; pas d'inventaire ouvert d'occupation des sols par kg de matériau (FDES : SQP seulement ; ecoinvent, GBS : licences) ; Carbone 4 (2026) a contourné ce trou par un proxy ecoinvent par produit, dimensionné sur l'empreinte carbone déclarée dans la FDES, calcul propriétaire de Darwin non publié ; dans son modèle, l'usage des sols ne fait que 11 % de la biodiversité grise, la pollution 51 % et le climat 38 % (2.3, 2.4).
Recommandation : Inat en m²HE·an = Σ_matériaux [occupation (m²·an) × perte MSA de l'usage] + Σ [transformation (m²) × 0,5 × t_reg × perte MSA], avec les pertes MSA de GLOBIO pour la France et t_reg de ReCiPe (73,5 / 7,5) et EF (85 ans pour l'artificiel), chaque choix en convention. La voie PDF (LC-IMPACT v2) est codée en option d'étude pour l'incertitude et la comparaison, sans entrer dans Inat. L'inventaire d'occupation par matériau est construit au lot 1 par convention à partir de rendements publics (production biologique des forêts françaises par essence en m³/ha/an, rendement des carrières en t/ha/an, emprise des usines rapportée à la production), matériau par matériau, avec sa plage d'incertitude ; il peut être remplacé, projet par projet, par les flux d'occupation issus de l'ACV du projet quand le bureau d'études les possède (saisie documentée). Le principe du dimensionnement d'un proxy sur l'empreinte carbone déclarée (Carbone 4) est retenu comme contrôle de cohérence : à carbone égal, l'occupation conventionnelle d'un matériau ne peut s'écarter de plus d'un facteur à fixer de celle du matériau type.
Par défaut : voie MSA, inventaire par convention, surcharge possible par les flux de l'ACV du projet.

### P9. Source des quantités de matériaux et base INIES

Sources : les quantités par lot existent déjà dans l'étude RE2020 du projet, dans la branche RSEnv du RSEE (composants, lots 1 à 13, Tableau 5 de l'annexe II) ; OpenBCE lit le RSEE (`rsee.py`) mais pas encore RSEnv ; la licence du webservice INIES (CGU du 17/07/2026) interdit « classements, notations, scorings, étiquettes ou tout dispositif assimilé portant sur les Déclarations Environnementales », et coûte 400 € HT plus 2 800 € HT par an (2.4).
Recommandation : OpenNat n'interroge jamais INIES ; les quantités viennent du RSEE du projet (lecture de RSEnv avec le lecteur `rsee.py` repris d'OpenBCE, qui redevient donc réutilisable) ou d'un tableur au format documenté ; les FDES ne sont jamais notées ni classées, seule la masse par matériau type est utilisée. Si le lot 1 montre qu'une déclaration environnementale est indispensable à l'inventaire, l'accord écrit de l'association INIES sera demandé avant tout usage.
Par défaut : comme ci-dessus.

### P10. Multiplicateurs de situation (trame verte et bleue)

Sources : UK 1,15 (identifié dans une stratégie locale), 1,10 (souhaitable), 1,0 (sinon), avec blocage de l'état initial à 1,0 là où une stratégie locale est publiée ; définitions françaises des réservoirs et corridors (R. 371-19), sans seuil numérique ; BKompV + 3 points pour la position (2.1, 2.2, 2.5.2).
Recommandation : 1,15 pour une unité située dans un réservoir de biodiversité identifié (SRADDET, SRCE Île-de-France, PLU), 1,10 dans un corridor identifié, 1,0 hors trame ; le multiplicateur s'applique à l'état initial comme à l'état projet (pour ne pas récompenser la destruction en réservoir) ; plafond du m²HE par m² à 1,15. Convention de transposition citant la source UK.
Par défaut : 1,15 / 1,10 / 1,0.

### P11. Haies, alignements et arbres isolés

Sources : UK, 3 modules à unités non fongibles (surfaces, haies en km, cours d'eau en km) et surfaces équivalentes d'arbres par classe de diamètre (0,0041 ; 0,0163 ; 0,0366 ; 0,0765 ha, formule de la zone de protection racinaire) ; Hesse, surfaces de houppier des plantations 1 / 3 / 5 m² selon la circonférence et comptage du houppier en surplomb des types sous-jacents ; BKompV, stades J / M / A dans la valeur (2.1, 2.2).
Recommandation : un seul module surfacique ; haie = longueur × largeur ; arbre existant = surface de houppier projetée (saisie) ; arbre planté = unité dont la surface croît de la valeur initiale (classe Hesse) à la surface cible selon la courbe de maturation du module T ; le houppier en surplomb d'une autre unité s'ajoute à celle-ci (règle Hesse). Raison : une seule unité additionnable, cohérente avec Cnat, et une maturation traitée une fois pour toutes par le module T.
Par défaut : comme ci-dessus.

### P12. Définition de Bnat et construction de `sols.csv` (fusion VIBCN)

Sources : Bbio = 2 × (Bch + Bfr) + 5 × Becl en points (annexe III, 1.1). Aucune source ne définit un « besoin de nature » de conception, mais un instrument de même objet existe, réglementaire en France, appliqué depuis 1990 à Berlin et depuis 2021 à Londres : le coefficient de biotope par surface, somme des surfaces pondérées par leur nature, rapportée à la surface de la parcelle (L. 151-22 et R. 151-43 du code de l'urbanisme : part minimale de surfaces non imperméabilisées ou éco-aménageables « éventuellement pondérées en fonction de leur nature », coefficient exprimant la valeur de chaque surface « par référence à celle d'un espace équivalent de pleine terre », 2.5.3 et 2.7 § 7 ; BFF = naturhaushaltswirksame Flächen ÷ Grundstücksfläche, 2.5.3 ; UGF, 2.5.4). Grilles de coefficients lues à la source : Berlin BFF 2019 (2.5.3), Strasbourg 2026 (2.5.3), Grand Annecy 2026 (2.5.3), Paris 2019 (Svp, 2.5.3) et PLU bioclimatique 2025 (IVB à 5 coefficients et SELC, fiche B), Londres UGF 2023 (2.5.4), Lille PLU2, Montreuil et Roubaix (fiche B, 2.7 § 6), plages observées par le Cerema dans 10 collectivités (2.5.3, 2.7 § 6), guide ERC du SDAGE Seine-Normandie 2024 (fiche E). Cibles existantes : Berlin 0,60 (logement neuf), 0,45 et 0,30 selon l'emprise, 0,30 (activités) (2.5.3) ; Londres 0,4 (résidentiel) et 0,3 (autres) (2.5.4) ; Strasbourg 25 à 50 % selon la zone (2.5.3) ; Lille 0,2 et 0,4, Roubaix 0,5 et 0,3 (fiche B, 2.7 § 6) ; 30 % de pleine terre hors voirie du SDRIF-E et objectif 30 à 45 % de l'ARB îdF (2.7). Le Cerema avertit que ces coefficients sont des « indicateurs d'occupation des sols (et non de biodiversité) » (2.5.3) : c'est exactement le statut de Bnat, indicateur de conception et non de valeur écologique, comme Bbio est un besoin et non une consommation.
Recommandation : Bnat = 100 × Σ (S_i × c_i) / S_parcelle, où S_i est la surface de chaque unité du plan masse par nature de surface, c_i son coefficient de sol lu dans `sols.csv` et S_parcelle la surface de la parcelle. Bnat se calcule sur les seules données du plan masse (emprises, revêtements, dalles et épaisseurs de substrat, pleine terre, toitures et façades végétalisées, surfaces en eau), sans valeur d'habitat, sans état écologique, sans temps : il est à Cnat ce que Bbio est à Cep, indépendant des aménagements paysagers comme Bbio est indépendant des systèmes. Les surfaces hors-sol (toitures, façades) entrent au numérateur sans entrer dans S_parcelle, comme à Berlin et à Londres, ce qui permet un Bnat supérieur à 100 sur un bâti entièrement végétalisé ; le cas est affiché, pas plafonné. Bnat × 0,01 est un coefficient de biotope au sens de L. 151-22 : il se compare directement aux cibles berlinoises et londoniennes et aux grilles des PLU, et un PLU qui impose un CBS fournit une valeur de contrôle immédiate. Le taux de pleine terre PT (5 critères Cerema : sans revêtement même perméable, végétalisée, au moins 2 horizons et plus de 30 cm, sans interface imperméable, matériaux terreux majoritaires, 2.7 § 6) et la part du périmètre de la parcelle en contact avec un espace végétalisé voisin CONT sont rapportés à côté de Bnat, non pondérés et non sommés, parce qu'aucune source ne donne leur poids. Cette définition remplace la formule à 3 poids de la première version de ce document (0,5 × PT + 0,3 × (1 moins IMP) + 0,2 × CONT), dont les poids n'avaient aucune source.
Construction de `sols.csv`, seule convention de Bnat : une ligne par nature de surface et classe d'épaisseur de substrat ; valeur centrale = médiane des coefficients publiés par Berlin 2019, Londres 2023, Strasbourg 2026, Grand Annecy 2026, Paris 2025 (IVB ramené sur 1), Lille, Montreuil et le SDAGE Seine-Normandie 2024 ; plage = étendue entre ces sources ; classes d'épaisseur fixées par les sources écologiques et non par les grilles : 15 cm, borne de l'extensif (FLL via Baunetz : extensif 5 à 15 cm, intensif à partir de 15 cm ; Paris 2012 : 10 cm minimum ; fiche E) ; 25 à 30 cm, seuil au-delà duquel la richesse floristique des toitures cesse de croître (GROOVES, 36 toitures d'Île-de-France, 2.6.5 et fiche E) ; 40 cm herbacé, 80 cm arbustif, 120 cm arboré (MUSE, Cerema et ADEME 2022, fiche E) ; 80 cm, borne au-delà de laquelle Berlin, Strasbourg, Grand Annecy, Paris, Lille et Montreuil rapprochent la dalle du sol. Coefficients publiés, lus à la source (emplacements : Berlin, page BFF-Berechnung, tableau des plans fixés après décembre 2019, 2.5.3 ; Strasbourg, règlement du 6 février 2026, article 9, p. 33 et 34, 2.5.3 ; Grand Annecy, fiche technique du 26 mars 2026, 2.5.3 ; Londres, London Plan 2021 Table 8.2 p. 325 et LPG UGF février 2023 Table 3.1 p. 8 et 9, 2.5.4 et fiche B ; Paris, guide des règles environnementales de juin 2025, p. 63, UG.4, fiche B ; Lille, extrait du Pacte Lille Bas Carbone du 18 octobre 2022, fiche B ; Montreuil, fiche DGALN 2015, fiche B et 2.7 § 6 ; SDAGE, guide ERC imperméabilisation de janvier 2024, fiche E) :

| Nature de surface | Berlin 2019 | Londres 2023 | Strasbourg 2026 | Grand Annecy 2026 | Paris 2025 (IVB sur 1) | Lille PLU2 | Montreuil | SDAGE SN 2024 |
|---|---|---|---|---|---|---|---|---|
| Surface scellée (bâti, enrobé, dallage étanche) | 0 | 0 | 0 | 0 | sans objet | 0 | sans objet | 0 (réfection) |
| Perméable minéral (stabilisé, gravier, pavés à joints sablés) | 0,1 (partiellement scellé) et 0,2 (drainant) | 0,1 | 0,2 | 0,3 (semi-perméable) | sans objet | 0,25 | sans objet | 0,1 (non végétalisé déconnecté) |
| Perméable végétalisé (dalles alvéolées engazonnées) | 0,4 | sans objet | 0,2 (pavés à joints gazon, rangés en minéral perméable) | 0,5 (semi-ouvertes : treillis de pelouse) | sans objet | 0,5 | sans objet | sans objet |
| Végétation sur dalle, substrat 20 à 40 cm | 0,5 | sans objet | 0,6 (30 cm et moins), 0,7 (plus de 30 cm) | 0,5 (moins de 80 cm) | 0,6 (25 cm et plus) | 0,5 ou 0,7 (15 à 20 cm selon la végétation), 0,6 (plus de 20 cm) | 0,20 (moins de 80 cm) | sans objet |
| Végétation sur dalle, 41 à 80 cm | 0,6 | sans objet | 0,7 | 0,5 | 0,8 (50 cm et plus) | 0,6 | 0,20 | sans objet |
| Végétation sur dalle, 81 à 150 cm | 0,7 | sans objet | 0,9 (80 cm et plus) | 0,7 (plus de 80 cm) | 1,0 (80 cm et plus) | 1 (1 m et plus) | 0,6 (80 cm et plus) | sans objet |
| Végétation sur dalle, plus de 150 cm | 0,9 | sans objet | 0,9 | 0,7 | 1,0 | 1 | 0,6 | sans objet |
| Pleine terre | 1,0 (réduit de 0,5 pour un gazon tondu ras) | 1 (semi-naturel) et 0,4 (gazon) | 1 | 1 | pleine terre obligatoire (SELC), hors IVB | 1 | sans objet | 1 |
| Toiture végétalisée extensive (moins de 15 cm) | 0,5 (moins de 20 cm, sans arrosage) | 0,7 (80 mm, GRO 2014) ou 0,3 (tapis de sedum) | 0,5 (moins de 10 cm), 0,6 (30 cm et moins) | sans objet | 0,6 (25 cm et plus) ou 0,6 (15 cm et plus sur existant) | 0,5 ou 0,7 | 0,20 | 0,5 |
| Toiture semi-intensive (15 à 30 cm) | 0,7 (15 à 50 cm, arrosable) | 0,8 (150 mm et plus) | 0,6 | sans objet | 0,6 | 0,6 | 0,20 | 0,5 |
| Toiture intensive (plus de 30 cm) | 0,8 (plus de 50 cm) | 0,8 | 0,7 (plus de 30 cm), 0,9 (80 cm et plus) | 0,5 (moins de 80 cm), 0,7 (plus de 80 cm) | 0,8 (50 cm et plus), 1,0 (80 cm et plus) | 0,6 | 0,6 (80 cm et plus) | 0,5 |
| Façade végétalisée enracinée au sol | 0,5 (jusqu'à 10 m) | 0,6 | 0,4 | sans objet | 0,2 (jusqu'à 15 m) | 0,4 (jusqu'à 10 m) | 0,20 | sans objet |
| Façade végétalisée hors sol (modules) | 0,7 (jusqu'à 20 m, 10 imputés) | 0,6 | 0,4 | sans objet | 0,2 | 0,4 | 0,20 | sans objet |
| Surface d'infiltration, noue, jardin de pluie | 0,2 (infiltration) | 0,7 (jardin de pluie) | sans objet | sans objet | sans objet | sans objet | sans objet | 1 (noue, jardin de pluie), 0,7 à 0,8 (dispositif gérant la pluie cinquantennale) |
| Eau de pluie à ciel ouvert, zone humide | 0,5 (plan d'eau alimenté par la pluie) | 1 (zone humide), 0,2 (eau chlorée ou bassin nu) | sans objet | sans objet | sans objet | sans objet | sans objet | sans objet |

Les fourchettes relevées par le Cerema dans 10 collectivités servent de contrôle : perméable 0,15 à 0,5, dalle et toiture 0,1 à 1, façade 0,1 à 0,5, pleine terre 1 (2.5.3, 2.7 § 6). La valeur centrale et la plage de chaque ligne sont des médianes et des étendues de grilles d'urbanisme, non des mesures écologiques ; `sols.csv` le dit ligne par ligne (colonne `type` = convention, colonne `justification` = médiane des grilles citées) ; les données écologiques disponibles (GROOVES, Biotopwerte des sols nus et des revêtements, O'Riordan 2021, § 3) confortent environ 10 lignes sur 30. C'est le premier point à soumettre au Biodiversity Standards Council.
Par défaut : définition ci-dessus ; `sols.csv` construit au lot 1 par la règle des médianes.

### P13. Seuils provisoires et coefficients Mnat

Sources : il n'existe ni observatoire ni distribution de référence ; points de repère : gain net de 10 % (Angleterre), BFF 0,60 logement neuf et 0,30 tertiaire (Berlin), UGF 0,4 et 0,3 (Londres), CBS 25 à 50 % (Strasbourg), pleine terre 20 et 30 %, CBSh 0,30 et 0,50 (ARB îdF), 45 % d'espaces verts et 10 % de couvert arboré (règlement (UE) 2024/1991, seuils d'exclusion nationaux) (2.1, 2.5, 2.7).
Recommandation : au lot 1, 3 seuils par indicateur exprimés en fraction de l'état initial et de la parcelle (Snat ≥ 0 : pas de perte nette ; Snat ≥ + 10 % de la valeur initiale intégrée ; Bnat ≥ 50 points, soit un coefficient de biotope de 0,50, entre la cible londonienne de 0,4 et la cible berlinoise de 0,60 pour le logement neuf), modulés par Mnat selon 3 typologies (logement, tertiaire, aménagement), la zone (méditerranéenne : délais plus longs reconnus) et la taille de parcelle (petits sites, à la manière du Small Sites Metric), tous marqués « en attente de validation du Biodiversity Standards Council » ; les 8 cas tests du lot 4 servent à vérifier que les seuils séparent les cas attendus (gain sur friche, perte sur prairie).
Par défaut : comme ci-dessus, chiffres fixés au lot 1.

### P14. Licences du moteur, de la méthode et des données

Sources : OpenBCE est sous AGPL-3.0-or-later ; sources de données : OGL v3 (UK, attribution requise, compatible avec une réutilisation commerciale), § 5 UrhG (règlements allemands, libres), PDF bavarois sans licence et liste NRW à reproduction soumise à autorisation, GLOBIO code EUPL-1.2 et documentation PBL « reproduction autorisée avec mention de la source », GBS CC BY-NC 4.0 (donc exclu d'un outil commercial), LC-IMPACT v2 CC BY 4.0, ReCiPe « reproduction avec mention », EF 3.1 libre avec attribution, EEA CC BY 4.0, HabRef sans licence lue, CSTB CBSh « ne peut pas être utilisé à des fins commerciales », guide ARB îdF à droits réservés, INIES à licence restrictive (2.1 à 2.7).
Recommandation : moteur sous AGPL-3.0-or-later comme OpenBCE ; texte de la méthode et tables `donnees/` sous CC BY 4.0, chaque ligne portant la licence de sa source ; n'embarquer comme valeurs que des sources OGL, § 5 UrhG, CC BY, EUPL et documents publics « reproductibles avec mention » ; citer sans embarquer les valeurs des sources à droits réservés (NRW, Bavière, ARB, CSTB), qui ne servent qu'au contrôle croisé ; ne rien reprendre du GBS (CC BY-NC) ni du CSTB (non commercial) ni d'INIES.
Par défaut : comme ci-dessus.

### P15. Zones biogéographiques

Sources : couche EEA 2016 (CC BY 4.0, 1:10 000 000) ; 4 régions terrestres en métropole selon l'INPN (alpine, atlantique, continentale, méditerranéenne) ; aucune table par commune ou département trouvée (2.5.6).
Recommandation : la zone est une donnée d'entrée du projet (saisie), avec une table d'aide par département construite au lot 1 par intersection de la couche EEA et des contours des départements (convention : zone majoritaire, les départements à cheval listés avec leurs 2 zones) ; outre-mer hors v1.
Par défaut : comme ci-dessus.

### P16. Version du référentiel Effinature de raccordement

Le cahier des charges cite la v8.1 ; d'autres notes de travail citent le référentiel Horizon v25.05 et une V9.1 en préparation. Le référentiel n'est pas public dans sa totalité et n'a pas été lu.
Recommandation : fixer la version de raccordement au lancement du lot 1 et la joindre en fichier ; d'ici là les seuils sont écrits sans référence aux niveaux Effinature.
Par défaut : aucun ; ce point attend une réponse et le fichier.

### P17. Forme de l'utilitaire du lot 3

Sources : OpenBCE n'a pas d'interface graphique ; ses « utilitaires » sont la ligne de commande, l'API HTTP sur bibliothèque standard et le serveur MCP (1.1).
Recommandation : une seule page HTML autonome, servie par l'API Python d'OpenNat (`python -m opennat.utilitaire`), sans framework, sans compte, projets en fichiers, qui lance le calcul par l'API et suit les étapes ; le serveur MCP est conservé comme dans OpenBCE pour l'emploi par un assistant. Raison : c'est le plus proche d'OpenBCE en dépendances et le plus simple à maintenir.
Par défaut : comme ci-dessus.

### P18. Plages d'incertitude par défaut pour le Monte-Carlo

Sources : SE publiés par Alkemade 2009 (0,07 à 0,20 selon les classes) ; intervalles à 95 % de GLOBIO 4 seulement graphiques ; aucune incertitude dans les tables UK ni allemandes ni LC-IMPACT (2.1 à 2.4).
Recommandation : chaque ligne de `donnees/` porte `incertitude_min` et `incertitude_max` ; quand la source donne un SE ou un intervalle, il est repris ; sinon, convention par classe de source : ± 10 % pour un règlement, ± 25 % pour un jugement d'expert publié, ± 50 % pour une convention Vi-BCN, loi triangulaire centrée ; la graine est écrite dans le projet et dans le RSNat.
Par défaut : comme ci-dessus.

### P19. Périmètre des pressions du module G : usage des sols seul, ou usage des sols, climat et pollution

Sources : le cahier des charges définit Inat comme « l'impact des matériaux et du chantier sur les écosystèmes, sur tout le cycle de vie » mais décrit le module G par la seule occupation et transformation des sols ; dans le modèle Carbone 4 (IMPACT World+, 2026), l'usage des sols ne fait que 11 % de la biodiversité grise du bâtiment type, la pollution 51 % (écotoxicité, acidification, eutrophisation, ozone photochimique) et le changement climatique 38 % ; le climat est la seule de ces pressions que les FDES couvrent intégralement, et la RE2020 la calcule déjà (Ic construction, en kg CO2 eq sur 50 ans) ; GLOBIO fournit une relation MSA par degré de réchauffement (coefficients du code public, et pentes par biome d'Arets 2014 reprises par le GBS, qui en tire un facteur de 4,37 x 10^-9 MSA.km² par kg CO2-eq) ; ReCiPe 2016 fournit des facteurs endpoint en species·yr par kg pour l'acidification, l'eutrophisation et l'écotoxicité, sans conversion lue vers la MSA (2.3, 2.4).
Recommandation : en v1, Inat = usage des sols (occupation et transformation, comme prévu) + une composante climat, calculée depuis les kg CO2 eq de l'ACV du projet par un facteur MSA par kg CO2 eq reconstruit depuis GLOBIO (régression climat du code public et pente du biome) et écrit en convention avec sa plage d'incertitude ; la pollution est calculée en indicateur complémentaire, en species·yr avec les facteurs ReCiPe 2016 appliqués aux indicateurs des FDES, affichée à part et non sommée dans Inat tant qu'aucune conversion sourcée vers la MSA n'existe. Raison : sans la composante climat, Inat ignorerait la pression dominante déjà quantifiée dans toute étude RE2020 ; avec une pollution sommée sans conversion sourcée, l'unité m²HE·an perdrait son sens.
Par défaut : usage des sols + climat dans Inat ; pollution en indicateur complémentaire.

## 6. Fichiers sources conservés et organisation du dossier

Le dossier du projet (`opennat/`) contient à la fin du lot 0 :

- `audit.md` : ce document.
- `livraison_lot0.md` : rapport de livraison du lot.
- `lot0/` : les fiches et scripts d'assemblage de l'audit (une fiche par famille de sources, réutilisables au lot 1 pour `methode/bibliographie.md`).
- `audit/fiches/` : les 5 fichiers de fiches de sources A à E (101 fiches) repris de l'audit VIBCN (§ 2.9), réutilisables au lot 1 dans `methode/bibliographie_fiches/`.
- `sources/uk_metric/` : guide utilisateur (June 2026), tableur statutaire 1.0.4, classeur des fiches d'état (juillet 2025), guide et tableur du Small Sites Metric, Technical Annex 2 du BM 4.0, articles de Marshall 2024 et zu Ermgassen 2021, texte OGL v3.
- `sources/biotopwert_de/` : BKompV (HTML gesetze-im-internet, extraction de l'Anlage 2 en 889 lignes), KV Hesse, Biotopwertliste bavaroise (PDF), Arbeitsblatt 61 LANUK et tableur NRW, thèse de Bruns 2007, Handreichung BfN.
- `sources/acv/` : rapport ReCiPe 2016 et tableur des facteurs, Koellner 2013, Verones 2020, LC-IMPACT v2 (chapitre 6 et classeur France), fichier EF 3.1 « Land use », De Laurentiis 2019, annexe II de l'arrêté du 4 août 2021, CGU et bon de commande INIES, rapport Chalmers 2023, page Carbone 4 et, dans `carbone4/`, le position paper de Carbone 4 (PDF de 30 pages fourni par Cédric).
- `sources/cadre_fr/` : codes consolidés (urbanisme, environnement), décret et rapport ZAN, décision du Conseil d'État, Berlin BFF, London Plan et UGF guidance, PLU de Strasbourg, fiche du Grand Annecy, PLU de Paris 2019, documents Cerema et DRIEAT, fichiers EUNIS 2012 et 2021 (EEA), HabRef v7, couche des régions biogéographiques, pages du portail RT-RE, guide CGDD 2021, guide ARB îdF 2026, documents CIBI, note wallonne sur le règlement restauration de la nature, pages ISO.
- `sources/thbce/` : annexe III consolidée du 21/07/2026.
- `sources/ecologie/` : les articles de la fiche 2.6 n'ont pas été conservés en fichiers (lus par extraction de texte) ; leurs URL sont dans la fiche et seront téléchargés au lot 1 pour ceux qui fournissent des coefficients.

Tous ces fichiers sont des copies de travail, non redistribuées : leur licence propre s'applique (§ 5, point P14). Rien de ce dossier n'est publié.
