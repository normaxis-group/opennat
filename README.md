<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="documentation/images/opennat-logo-fond-sombre.svg">
    <img alt="OpenNAT, le bilan nature des projets" src="documentation/images/opennat-logo.svg" width="460">
  </picture>
</p>

# OpenNAT

**Méthode de calcul de la nature consommée par un projet de construction, avec ses tables et son moteur libre.**
Méthode, tables et moteur édités par NORMATYS ; outil de calcul (utilitaire) édité par IRICE. Licences : CC BY 4.0
pour le texte et les tables, AGPL-3.0-or-later pour le moteur et l'utilitaire.

> **Avertissement.** La méthode OpenNAT est en attente de validation du Biodiversity Standard Council. Ses seuils et
> ses résultats ne sont pas opposables : un résultat OpenNAT n'est pas une certification et ne peut pas, à lui seul,
> fonder une allégation environnementale (directive (UE) 2024/825). Le code est fourni sans garantie (articles 15 et
> 16 de la licence AGPL).

## Pourquoi ce projet

Un projet de construction consomme de la nature à deux endroits. Sur son site, il remplace une prairie, une friche ou
un boisement par des bâtiments et des espaces plantés qui mettront des années à valoir ce qu'ils remplacent. Ailleurs,
il prélève des forêts pour son bois, des carrières pour ses granulats, et ses émissions réchauffent le climat. Les
coefficients de biotope des PLU ne regardent que l'état final du site ; les analyses de cycle de vie des bâtiments ne
comptent pas la biodiversité.

OpenNAT mesure les deux dans une même unité, le mètre carré d'habitat équivalent (m²HE), intégrée sur 50 ans. Comme la
RE2020 pour le carbone, le calcul est conventionnel : il ne prédit pas ce qui arrivera au site, il compare des projets
entre eux sous des règles communes. Chaque coefficient porte sa source et sa licence, chaque convention est écrite et
numérotée, et le moteur est vérifié par un carnet de calcul écrit à part, sur le modèle d'OpenBCE pour la RE2020.

## Ce que fait OpenNAT aujourd'hui

- Calcule, pour chaque variante d'un projet, Cnat (consommation de nature sur le site), Inat (biodiversité grise des
  matériaux et du chantier : climat, bois, carrières), Snat = -(Cnat + Inat) et Bnat (coefficient de biotope de l'état
  projet, comparable à celui du PLU), avec le niveau du site (perte nette, absence de perte nette, gain net) et la
  conformité aux seuils proposés pour le permis de construire.
- Suit le site année par année : 191 types d'habitat et leurs grilles d'état, sols, connectivité, nuisances et
  éclairage horaire, eau, bilan hydrique horaire sous le climat de la trajectoire de réchauffement de référence
  (TRACC), maturation des plantations, plan de gestion, calendrier du chantier.
- Reprend d'un RSEE (fichier d'une étude RE2020) la parcelle, les bâtiments et les indicateurs d'ACV.
- Chiffre l'incertitude par tirages sur les intervalles des tables (1 000 par défaut) et désigne les paramètres qui
  pèsent le plus.
- Écrit un récapitulatif standardisé (RSNat, en XML et en JSON, avec ses schémas) et une fiche de synthèse en Word et
  en PDF.
- Ne couvre pas encore : la pollution dans la biodiversité grise (proposée au conseil, branche `candidate-bsc`), les
  seuils de Cnat et d'Inat, la zone climatique déduite du département.

Vérifications : 73 cas du banc retrouvés par le moteur et par le carnet de calcul de référence
(`outils/carnet_reference.py`), 38 930 grandeurs figées en non-régression, tests de propriétés (sens de variation et
invariances), contrôle dimensionnel des équations, ordre de grandeur du module G comparé à l'étude Carbone 4. Détail :
[banc/README.md](banc/README.md).

## Documentation

| Document | Contenu |
|---|---|
| [methode/OpenNAT_v1.md](methode/OpenNAT_v1.md) | texte de la méthode OpenNAT 1 : indicateurs, étapes, fiches algorithmes, exemple de l'annexe C |
| [methode/OpenNAT_v1_edition_complete.md](methode/OpenNAT_v1_edition_complete.md) | édition complète : texte, tables commentées, une fiche par habitat, protocoles de relevé |
| [methode/conventions.md](methode/conventions.md) | les 70 conventions de méthode, numérotées |
| [methode/bibliographie.md](methode/bibliographie.md) | sources des tables et des modèles |
| [JOURNAL_DES_VERSIONS.md](JOURNAL_DES_VERSIONS.md) | versions de la méthode, des données (empreintes) et du moteur |
| [documentation/guide_utilisateur.md](documentation/guide_utilisateur.md) | données à réunir, saisie, calcul, lecture des résultats |
| [documentation/guide_contributeur.md](documentation/guide_contributeur.md) | proposer une valeur avec sa source |
| [documentation/dossier_bsc.md](documentation/dossier_bsc.md) | dossier de soumission au Biodiversity Standard Council et décisions demandées |
| [documentation/conditions_usage_nom.md](documentation/conditions_usage_nom.md) | conditions d'usage du nom OpenNAT |
| [banc/README.md](banc/README.md) | banc de validation, non-régression, contrôle Carbone 4 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | comment contribuer |
| [`llms.txt`](llms.txt) | plan du dépôt pour un assistant d'IA |

Les versions Word et PDF des documents sont dans `livraison/`.

## Installation et emploi

**Version en ligne** : l'outil de calcul tourne sur https://opennat.irice-certification.com, sans compte (mode public : identifiants de calcul aléatoires, tirages et calculs simultanés bornés, projets et résultats effacés après 24 heures, fiche de synthèse en Word). Pour des projets confidentiels, installer l'outil sur son poste :

Python 3.11 ou plus, numpy et lxml ; python-docx pour la fiche de synthèse, LibreOffice pour sa version PDF, pytest
pour les tests.

    git clone https://github.com/normaxis-group/opennat.git
    cd opennat
    pip install -e ".[dev,fiche]"
    python -m opennat controle                           # tables de donnees/ et contrôle dimensionnel
    python -m pytest
    python -m opennat valider projet.json                # contrôle du fichier projet
    python -m opennat calcul projet.json                 # calcul complet, 1 000 tirages par défaut
    python -m opennat calcul projet.json --tirages 0     # valeurs centrales seules
    python -m opennat calcul projet.json --reprendre resultats/<projet>/<horodatage>
    python -m opennat.utilitaire                         # outil de calcul : http://127.0.0.1:8770/
    python -m banc.comparer                              # banc : les cas contre le carnet de référence
    python -m banc.regression                            # non-régression
    python -m banc.carbone4                              # ordre de grandeur du module G face à Carbone 4

Le calcul écrit `resultats/<projet>/<horodatage>/` : entrées après valeurs par défaut, sorties de chaque étape par
variante, trajectoires, tirages, journal, empreintes, `rsnat.xml` et `rsnat.json`. Le fichier projet suit
[schemas/projet.schema.json](schemas/projet.schema.json) ; `banc/cas/exemple_de_l_annexe_c.json` en est un exemple
complet. Il peut citer un RSEE (`projet.rsee`) : la parcelle, les bâtiments, les indicateurs d'ACV, la zone climatique,
le département et l'altitude s'en reprennent.

Un `Dockerfile` est fourni (python:3.12-slim, numpy, lxml, python-docx, sans LibreOffice). Il lance l'utilitaire, à
publier sur la seule machine (`-p 127.0.0.1:8770:8770`), et sert aussi pour la ligne de commande.

## Utilitaire

```
python -m opennat.utilitaire                 # ouvre http://127.0.0.1:8770/ dans le navigateur
python -m opennat.utilitaire --port 8780 --dossier D:/etudes/resultats --sans-navigateur
```

Un serveur local (bibliothèque standard, qui n'écoute que sur la machine sauf option `--hote`) et une page web
autonome, sans compte : les projets sont des fichiers JSON ouverts et enregistrés depuis le navigateur, les résultats
s'écrivent dans le dossier de travail. Onglets de saisie : projet et contexte (avec reprise d'un RSEE), état initial,
état projet, sol, connectivité, nuisances, eau, matériaux (avec import d'un tableur CSV), variantes ; contrôles en
direct (schéma, fermeture des surfaces, saisie de chaque unité) ; calcul en arrière-plan avec suivi des étapes, arrêt
et reprise ; résultats, comparaison des variantes, résultats intermédiaires, RSNat XML et JSON, fiche de synthèse en
Word et en PDF au papier d'IRICE, éditeur de l'outil.

Tableur des matériaux : CSV à séparateur point-virgule, colonnes `categorie;regime;quantite;remplacements;justification`,
catégorie `bois` (m³, régime forestier) ou `granulats` (t).

## Organisation du code

- `opennat/` : le moteur, un module par module de la méthode (tableau ci-dessous) ; `opennat/utilitaire/` : l'outil de
  calcul.
- `donnees/` : les tables, une ligne par valeur avec son intervalle, sa source et sa licence (2 535 lignes).
- `methode/` : texte de la méthode, conventions, bibliographie, sources de l'édition complète.
- `schemas/` : schéma du fichier projet, schémas XSD et JSON du RSNat, exemple de l'annexe C.
- `banc/` : les cas en fichiers projet, leurs résultats attendus, le comparateur, l'instantané de non-régression, le
  contrôle Carbone 4 et les études d'options soumises au conseil. Aucun RSEE réel.
- `outils/` : contrôle et construction des tables, carnet de calcul de référence, modules dynamiques, génération de
  l'édition et des documents Word.
- `tests/` : chargeur, modules (cas élémentaires des fiches), bout en bout, utilitaire, banc et non-régression,
  propriétés, contrôle dimensionnel, recherche des constantes dans le code.
- `audit/` : cahier des charges, audit et fiches de sources du lot 0, rédigés sous l'ancien nom de travail « Vi-BCN ».
- `documentation/`, `livraison/` : guides, notes et dossiers, en Markdown d'une part, en Word et PDF de l'autre.
- `sources/`, `resultats/` : copies de travail des sources et résultats de calcul, hors dépôt.

| Module | Étape ou module de la méthode | Fiches |
|---|---|---|
| `donnees.py` | chargement et contrôle des tables, tirages | A01, A39 |
| `projet.py`, `rsee.py`, `schema.py` | fichier projet, reprise du RSEE | A05 |
| `conformite.py` | E1 contexte, E5 conformité | A02, A40 |
| `pretraitement.py` | E2 prétraitement | A03, A04, A14 à A16 |
| `sol.py` | S sol | A06 à A08 |
| `habitats.py` | H habitats | A09 à A13 |
| `connectivite.py` | C connectivité | A17 à A19 |
| `nuisances.py` | N nuisances, éclairage horaire | A20 à A22, A51 à A53 |
| `eau.py` | E eau, valeur à maturité | A23 à A25 |
| `climat.py`, `hydrique.py` | W climat et bilan hydrique horaire | A43 à A50 |
| `temps.py` | T temps, maturation, gestion, chantier | A26 à A30, A54 à A58 |
| `materiaux.py` | G biodiversité grise | A32 à A36 |
| `agregation.py` | E3 agrégation, Bnat | A31, A37, A38 |
| `incertitude.py` | E4 incertitude | A39 |
| `chaine.py`, `calcul.py` | ordre des étapes, variantes, journal, reprise | A41, A42 |
| `rsnat.py`, `recapitulatif.py`, `rsnat_spec.py` | RSNat | partie 7 |
| `dimensions.py` | contrôle dimensionnel des unités et des équations (E12) | toutes |

## Données

Les valeurs d'habitat viennent de la valeur de biotope de l'ordonnance fédérale allemande de compensation (BKompV) et
de la métrique statutaire anglaise de biodiversité (grilles d'état, délais, difficulté de création) ; les facteurs de
biodiversité grise, de GLOBIO 3.5 et des rapports du GIEC, avec les données forestières de l'IGN et du FCBA ; le climat
horaire, des fichiers prospectifs de Météo-France pour la TRACC. La version candidate soumise au conseil y ajoute
LC-IMPACT, ReCiPe et l'Environmental Footprint (bois et pollution). Chaque ligne des tables cite sa source précise et sa licence ; les sources
elles-mêmes ne sont pas dans le dépôt. Liste complète : [methode/bibliographie.md](methode/bibliographie.md).

## État des travaux

| Lot | Objet | État |
|---|---|---|
| 0 | Audit et état de l'art (`audit/`) | livré le 17/10/2026 |
| 1 | Méthode OpenNAT 1 (`methode/`) et tables sourcées (`donnees/`), édition complète | livré le 18/10/2026 (lots 1, 1 bis, 1 ter) |
| 2 | Moteur, banc, tests | livré le 19/10/2026 |
| 3 | Utilitaire | livré le 19/10/2026 |
| 4 | Banc de validation et de non-régression, propriétés, contrôle dimensionnel, guides, journal des versions | livré le 19/10/2026 |
| 5 | Dossier de soumission au Biodiversity Standard Council | livré le 19/10/2026 |
| 6 | Écotoxicité, acidification et biodiversité grise | livré le 19/10/2026 |
| 7 | Finitions, note sur les licences et les conventions NORMATYS-IRICE | livré le 19/10/2026 |
| 8 | Dépôt du nom, transmission au conseil, version candidate (branche `candidate-bsc`) | livré le 19/10/2026 ; rien n'est déposé ni transmis |

Chaque lot a sa note de livraison (`livraison_lot<N>.md`).

## Citer, contribuer, licences

- Citation : voir [CITATION.cff](CITATION.cff).
- Contributions : voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [guide du contributeur](documentation/guide_contributeur.md).
- Moteur (`opennat/`) : GNU Affero General Public License v3.0 ou ultérieure ([LICENSE](LICENSE)), NORMATYS titulaire
  des droits. Utilitaire (`opennat/utilitaire/`) : même licence, IRICE titulaire des droits. Toute version modifiée
  distribuée ou mise à disposition par réseau doit l'être avec son code source.
- Texte de la méthode, tables et guides (`methode/`, `donnees/`, guides de `documentation/`) : Creative Commons Attribution 4.0
  International ([LICENSE-CC-BY-4.0.txt](LICENSE-CC-BY-4.0.txt)), NORMATYS titulaire des droits ; chaque ligne des
  tables garde en outre la licence de sa source.
- Le nom OpenNAT, les logos et les papiers à en-tête ne sont pas couverts par ces licences : voir les
  [conditions d'usage du nom](documentation/conditions_usage_nom.md).

---

*English summary.* OpenNAT is a calculation method (CC BY 4.0) and an open-source engine (AGPL-3.0) measuring the
nature a construction project consumes, on its site and elsewhere through its materials, in square metres of
equivalent habitat over 50 years. Every coefficient carries its source and licence, and the engine is checked against
an independently written reference workbook. The method awaits validation by the Biodiversity Standard Council; its
results have no regulatory value.
