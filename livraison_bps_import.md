# Livraison : import d'un projet du BPS dans OpenNAT

25 octobre 2026, branche `bps-import` (issue de `main`, commit c9c6f1a), non poussée. Demande de Cédric : le BPS en ligne (biodiversity-performance.com, référentiel BPS_BATI) doit déterminer ses indicateurs avec ses propres outils et produire un export que le moteur OpenNAT sait lire (note de conception « BPS en ligne autonome », indice B, validée le 25/10/2026, D1 à D12).

## Ce qui est livré

| Fichier | Contenu |
|---|---|
| `opennat/effinature/bps.py` | `importer_bps` : lecture d'un export « BPS export 1 », production du fichier projet et du fichier crédits ; fichier à part pour ne pas toucher à l'import Effinature |
| `opennat/effinature/__init__.py` | `executer` reconnaît le format « BPS export 1 » et appelle `importer_bps` (5 lignes) |
| `opennat/__main__.py` | aide de la commande `effinature` complétée |
| `banc/effinature/bps_demonstration.export.json` | export du site FICTIF de démonstration du BPS (immeuble de bureaux de 5 000 m² à Aix-en-Provence), produit par l'application du BPS |
| `tests/test_bps.py` | 11 tests : projet valide et fermé, référence en usage maintenu sans obligation, unités liées à l'état initial (fiche A41), relevés et calendrier C-X12, crédits calculables, erreurs |

## Le format « BPS export 1 »

Les unités du BPS sont déjà des unités OpenNAT : identifiant stable, code de la nomenclature, position, surface, épaisseur, arbres (nombre, classe de diamètre, stade), statut (conservée, créée, améliorée) avec l'unité initiale liée, grille d'état. La conversion est directe : ni traduction de typologies, ni répartition d'habitats, ni hypothèse.

| Bloc | Devient dans OpenNAT |
|---|---|
| `etat_initial` (relevé de l'état initial, phase Initiale du BPS) | état initial ; identifiants préfixés `I-` |
| `projet_prevu` (relevé réalisé à la Livraison, à défaut relevé de Conception) | variante « Projet », seule variante |
| `releves` (relevés de suivi V1, V2, V3, puis suivis quinquennaux) | `releves` du fichier crédits, par année |
| `calendrier` | calendrier propre, contrôlé (convention C-X12) |
| `evaluation` | champ `certification` : « BPS_BATI v1.1, phase …, score …, classe … ; évalué, hors accréditation » |
| `risque`, `gain_exige` | facteurs de l'annexe A ; obligation réglementaire en gain exigé |

Référence du crédit : `usage_maintenu` pour toutes les unités, sans variante d'obligations. Le BPS évalue des bâtiments en exploitation : seule l'amélioration apportée par le propriétaire crédite. Une unité déclarée conservée ou améliorée sans unité initiale correspondante est comptée créée, et le journal le dit.

## Résultat sur le site de démonstration (1 000 tirages, graine 1)

Gain retenu 4 415 m²HE·an sur 50 ans, 3,53 crédits prévisionnels, plafond 3 crédits, réserve 20 %. Relevés des années 1 et 2 : gain constaté 40 et 224 m²HE·an, aucune émission (plantations jeunes). Calcul en 5 s en ligne de commande, 7,6 s depuis l'application du BPS. Ordre de grandeur conforme à la note de conception : un site déjà aménagé ne rapporte que quelques crédits.

## Contrôles

- `python -m pytest` : 204 tests passés, dont les 11 de l'import BPS (4 min 30).
- `python -m banc.regression` : 38 930 grandeurs sur 38 930 inchangées.
- `python -m banc.credits.comparer` : 20 cas conformes sur 20.
- Côté BPS : tests Pest du relevé et du potentiel, dont un calcul réel par ce moteur (branche `feat/releve-surfaces-opennat` du dépôt bps).

## Hors de cette branche

- Contribution de maintien : un site évalué au BPS n'y est pas éligible (méthode, chapitre 3). L'export porte la surface entretenue, au cas où NORMATYS ouvrirait une version 2 aux bâtiments existants (D11).
- Moteur en production dans l'image du conteneur du BPS : décision au déploiement (D12).
