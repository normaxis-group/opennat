# Livraison du lot 3 : utilitaire de calcul OpenNAT

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne.
**État :** lot livré, rien n'est publié. Arrêt et attente du go écrit avant le lot 4 (banc de validation et documentation).

## Ce qui est fait

```
python -m opennat.utilitaire
```

L'utilitaire ouvre `http://127.0.0.1:8770/` dans le navigateur. Comme l'API d'OpenBCE, le serveur n'emploie que la bibliothèque standard de Python et le moteur ; il n'écoute que sur la machine. La page est autonome : aucune bibliothèque ni police chargée depuis Internet. Pas de compte : les projets sont des fichiers JSON, ouverts et enregistrés depuis le navigateur ; les résultats s'écrivent dans le dossier de travail. Charte NORMATYS, éditeur de la méthode : encre, bleu et vert de la fleur, logo.

| Exigence du cahier des charges (§ 6) | Réalisation |
|---|---|
| 1. Saisie par onglets qui suivent la méthode, contrôles en direct | Neuf onglets : projet et contexte, état initial, état projet, sol, connectivité, nuisances, eau, matériaux, variantes. Chaque unité a un détail : surface, grille d'état avec le libellé de chaque critère et les critères essentiels signalés (ou résumé de grille), éclairage (raccourci ou horaires, température de couleur, distance, détection), eau et sol, gestion et chantier. Panneau de contrôles mis à jour à chaque saisie : schéma du fichier projet, saisie de chaque unité, fermeture des surfaces de l'état initial et de chaque variante |
| 2. Import et export du fichier projet, import des matériaux depuis un tableur | Ouvrir, enregistrer, exemple de l'annexe C ; import d'un RSEE (parcelle, bâtiments, indicateurs d'ACV, zone climatique, département, altitude ; le fichier est lu puis oublié) ; import d'un tableur CSV de matériaux au format documenté, avec modèle téléchargeable et lignes refusées signalées |
| 3. Lancement du calcul avec suivi des étapes, sans bloquer l'interface | Calcul en arrière-plan ; étapes E1 à E5 de chaque variante allumées au fur et à mesure, barre d'avancement des tirages, journal ; arrêt entre deux blocs de tirages et reprise du même dossier |
| 4. Résultats | Indicateurs et niveau, seuils et conformité, attestation au permis, trajectoire du site sur 50 ans face au site sans projet sous le même climat, détail du site, biodiversité grise par poste et par phase, incertitude et paramètres influents, détail par unité, journal ; comparaison des variantes côte à côte avec l'intervalle des écarts |
| 5. Fiche standardisée | RSNat XML et JSON validés ; fiche de synthèse en Word au papier NORMATYS (Calibri 10, langue française, pagination « Page X sur Y », tableaux d'un bloc) et en PDF par LibreOffice, avec version de la méthode, des données et empreintes de contrôle |
| 6. Résultats intermédiaires | Liste des fichiers du dossier de résultats et lecture de chacun |

La mention « en attente de validation du Biodiversity Standard Council » figure sur la page de résultats et sur la fiche (exigence E11).

## Recette du lot 3 (§ 9)

- [x] Un projet se saisit entièrement sans toucher au JSON : tous les champs du schéma ont leur place dans l'interface, sauf les indicateurs de pollution par bâtiment, qui ne viennent que du RSEE.
- [x] Une erreur de fermeture des surfaces est signalée avant le calcul : pastille « écart » et somme au sol dans le panneau de contrôles ; le bouton de calcul reste inactif tant qu'un contrôle échoue.
- [x] L'avancement des étapes s'affiche pendant le calcul.
- [x] Les résultats intermédiaires de chaque étape sont consultables.
- [x] La fiche PDF et le RSNat s'éditent et portent version et empreinte.
- [x] Deux variantes se comparent côte à côte : sur l'exemple de l'annexe C, la variante « plan de gestion de 50 ans » ramène Cnat de 3 217 à 1 476 m²HE·an ; l'écart de Snat (+1 741) a son intervalle propre, de 1 350 à 2 035, calculé sur les mêmes tirages.

Éprouvé dans le navigateur : chargement de l'exemple, grille de critères, création d'une variante et saisie dans le tableau, calcul de deux variantes avec 100 tirages, comparaison, lecture des fichiers intermédiaires, fiche PDF (trois pages, regardées), import d'un tableur de matériaux, arrêt d'un calcul au tiers des tirages puis reprise jusqu'au bout. Aucune erreur dans la console.

## Tests

`tests/test_utilitaire.py` lance le serveur et vérifie la page et le référentiel (191 habitats, grilles et libellés), les contrôles en direct (fermeture, code inconnu), l'import d'un tableur et d'un RSEE fabriqué, un calcul de bout en bout par l'API (étapes, résultats, fichiers, RSNat, fiche Word et PDF) et le refus d'un chemin hors du dossier de résultats. Avec les tests du moteur : 51 tests.

## Écarts

1. La biodiversité grise n'est pas donnée par lot : le moteur ne lit pas encore les composants lot par lot dans le RSEE. Elle est donnée par poste (climat, bois, carrières) et par phase.
2. Les indicateurs de pollution par bâtiment ne se saisissent pas dans l'interface ; ils viennent du RSEE.
3. La fiche PDF demande LibreOffice ; sans lui, la fiche est proposée en Word.

## Ce que le go déclenche

Lot 4, banc de validation et documentation : les huit cas tests et leurs calculs de référence existent déjà (banc de 73 cas) ; restent les tests de non-régression et de propriétés à étendre, le contrôle d'ordre de grandeur du module G face à l'étude Carbone 4 avec l'explication des écarts, le guide utilisateur, le guide du contributeur (proposer une valeur avec sa source) et le journal des versions de la méthode et des données.
