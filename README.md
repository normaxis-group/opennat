# OpenNAT

Méthode de calcul biodiversité **OpenNAT** et son moteur libre, qui porte le même nom, sur le modèle d'OpenBCE (méthode Th-BCE de la RE2020).

- Éditeur de la méthode et titulaire des droits : NORMATYS. Application dans la certification Effinature : IRICE.
- Validation de la méthode : Biodiversity Standard Council. Tant qu'elle n'est pas validée, la méthode, ses seuils et ses résultats ne sont pas opposables.
- Licences prévues : moteur sous AGPL-3.0-or-later ; texte de la méthode et tables `donnees/` sous CC BY 4.0, chaque ligne portant la licence de sa source.
- Dépôt privé. Aucune publication sans le go écrit de Cédric PLANTAZ.

## État

| Lot | Objet | État |
|---|---|---|
| 0 | Audit et état de l'art (`audit/`) | livré le 17/10/2026, go le 18/10/2026 |
| 1 | Méthode OpenNAT v1 (`methode/`) et tables sourcées (`donnees/`) | version noyau livrée le 18/10/2026 ; édition complète livrée le même jour (lot 1 bis, 949 pages), complétée et dotée des modules dynamiques (lot 1 ter, `livraison_lot1ter.md`) |
| 2 | Moteur (`opennat/`), banc de 73 cas (`banc/`), tests (`tests/`) | livré le 19/10/2026 (`livraison_lot2.md`) |
| 3 | Utilitaire (`opennat/utilitaire/`) | livré le 19/10/2026 (`livraison_lot3.md`) |
| 4 | Banc de validation et documentation | à venir |

L'audit du lot 0 emploie encore l'ancien nom de travail « Vi-BCN » ; le nom retenu par Cédric PLANTAZ le 18/10/2026 est OpenNAT, pour la méthode comme pour le moteur.

## Organisation

- `audit/` : cahier des charges, audit du lot 0, fiches de sources A à E.
- `methode/` : texte de la méthode, conventions, bibliographie.
- `donnees/` : tables de coefficients, une ligne par valeur avec sa source.
- `outils/` : contrôle des tables, rapport de couverture, constructeurs des tables, carnet de calcul de référence, modules dynamiques (`climat.py` : climat horaire TRACC et ET0 ; `dynamique.py` : bilan hydrique, éclairage, maturation, gestion, chantier), génération de l'édition (`edition/`).
- `opennat/` : le moteur, un module par module de la méthode (voir ci-dessous).
- `schemas/` : schéma du fichier projet, schémas XSD et JSON du RSNat, exemple de l'annexe C.
- `banc/` : les 73 cas du carnet de référence en fichiers projet, leurs résultats attendus, le comparateur.
- `tests/` : tests du chargeur, des modules (cas élémentaires des fiches), de bout en bout, et recherche des constantes dans le code.
- `sources/` : copies de travail des documents sources (hors dépôt).

## Moteur

Python 3.11 ou plus, numpy et lxml.

```
python -m opennat calcul projet.json                 # calcul complet, 1 000 tirages par défaut
python -m opennat calcul projet.json --tirages 0     # valeurs centrales seules
python -m opennat calcul projet.json --reprendre resultats/<projet>/<horodatage>
python -m opennat valider projet.json                # contrôle du fichier projet
python -m opennat controle                           # contrôle des tables de donnees/
python -m banc.comparer                              # banc : 73 cas contre le carnet de référence
python -m pytest                                     # tests
```

Le calcul écrit `resultats/<projet>/<horodatage>/` : entrées après valeurs par défaut, sorties de chaque étape par variante, trajectoires, tirages, journal, empreintes, `rsnat.xml` et `rsnat.json`. Un fichier projet peut citer un RSEE (`projet.rsee`) : la parcelle, les bâtiments, les indicateurs d'ACV, la zone climatique, le département et l'altitude s'en reprennent.

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

## Utilitaire

```
python -m opennat.utilitaire                 # ouvre http://127.0.0.1:8770/ dans le navigateur
python -m opennat.utilitaire --port 8780 --dossier D:/etudes/resultats --sans-navigateur
```

Un serveur local (bibliothèque standard, n'écoute que sur la machine) et une page web autonome, sans compte : les projets sont des fichiers JSON ouverts et enregistrés depuis le navigateur, les résultats s'écrivent dans le dossier de travail. Onglets de saisie : projet et contexte (avec reprise d'un RSEE), état initial, état projet, sol, connectivité, nuisances, eau, matériaux (avec import d'un tableur CSV), variantes ; contrôles en direct (schéma, fermeture des surfaces, saisie de chaque unité) ; calcul en arrière-plan avec suivi des étapes, arrêt et reprise ; résultats, comparaison des variantes, résultats intermédiaires, RSNat XML et JSON, fiche de synthèse en Word et en PDF (python-docx, et LibreOffice pour le PDF).

Tableur des matériaux : CSV à séparateur point-virgule, colonnes `categorie;regime;quantite;remplacements;justification`, catégorie `bois` (m³, régime forestier) ou `granulats` (t).
