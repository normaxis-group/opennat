# Livraison du lot 1 ter : édition complétée et modules dynamiques de la méthode OpenNAT v1

**Date :** 18 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne.
**État :** lot livré, rien n'est publié. Arrêt et attente du go écrit avant le lot 2 (moteur).

## Demandes traitées

1. « On complète l'édition (listes complètes des fiches habitats, calculs des fiches d'application, cas supplémentaires) avant le moteur. » Fait : l'édition est passée de 949 à 1 857 pages, au-delà des 1 854 pages de l'annexe III de la RE2020.
2. « Y'a pas moyen de complexifier le calcul comme en re2020 ? », avec les quatre mécanismes retenus : bilan hydrique horaire, éclairage horaire, maturation et succession, chantier et climat futur. Fait : quatre modules dynamiques, seize fiches algorithmes A43 à A58, 23 conventions, cinq tables sourcées, 29 cas dynamiques.

## Ce que le calcul simule désormais

Comme la RE2020 simule le bâtiment heure par heure sur une année météorologique type, OpenNAT simule chaque unité végétalisée heure par heure sur trois années types, puis chaque unité mois par mois sur 50 ans.

| Mécanisme | Calcul | Sources |
|---|---|---|
| Climat | Année type horaire de la station de la zone climatique RE2020 (8 stations), aux niveaux +2, +2,7 et +4 °C de la TRACC ; altitude corrigée ; pluies recalées sur les normales 1991-2020 ; chaque année de la période pondérée selon la TRACC (+3,4 °C en 2076) | Fichiers climatiques prospectifs ADEME, Météo-France, CSTB, DHUP (2025, Licence Ouverte) ; données mensuelles Météo-France (Licence Ouverte) ; arrêté TRACC du 23 janvier 2026 |
| Bilan hydrique horaire | ET0 de Penman-Monteith au pas horaire ; réserve utile par texture et profondeur, ou par épaisseur de substrat ; neuf groupes hydriques ; indice de stress de Granier ; facteur hydrique rapporté au climat local ; arrosage ; tenue en eau des mares | FAO-56 (équation 53, tableaux 12, 19, 22) ; Granier et al. (1999) ; ETCCDI |
| Éclairage horaire | Heures de nuit éclairées d'avril à octobre selon l'heure d'extinction et de rallumage ; température de couleur ; distance au luminaire ; détection de présence | Arrêté du 27 décembre 2018 ; Azam et al. (2018) ; Longcore et al. (2018) |
| Maturation et gestion | Courbe de Chapman-Richards selon la forme (herbacée, arbustive, arborée) ; plan de gestion déclaré ; gestion courante (prairie tondue comme une pelouse) ou abandon (friche puis fourré) après le plan | Richards (1959) ; Pienaar et Turnbull (1973) ; BKompV, 11 couples exploité et abandonné |
| Chantier | Pas mensuel ; plantations de novembre à mars ; supplément de Cnat pour une destruction pendant la nidification, l'hibernation des chiroptères ou la reproduction des amphibiens | BCAE 8 de la PAC ; conventions |

La météo conventionnelle de la RE2020 n'est pas utilisée : le ministère en réserve l'usage au calcul réglementaire RE2020. Les fichiers prospectifs de l'ADEME sont libres. Leur note technique reconnaît que leurs pluies sont proches des maxima : elles sont recalées sur les normales observées (convention C-W3).

Contrôle indépendant : l'évapotranspiration calculée vaut de 0,86 à 1,00 fois l'ETP Penman normale de Météo-France aux huit stations (0,93 en moyenne), l'écart attendu entre les deux formules.

## Effet sur l'exemple de l'annexe C

| Grandeur | Calcul statique | Calcul dynamique |
|---|---|---|
| I_0 | 13 519,3 | 13 277,1 |
| I_1 | 12 051,0 | 10 059,9 |
| Cnat | 1 468,3 (11 %) | 3 217,2 (24 %) |
| Snat | -143 311 | -145 060 |

Hypothèses : Trappes, limon d'un mètre, chantier de 18 mois commencé en septembre 2027, plan de gestion de dix ans. L'écart vient d'abord de la gestion : la prairie passe en gestion courante à la fin du plan. Un plan couvrant les 50 ans ramène Cnat à 1 476, très près du calcul statique : la mécanique est cohérente.

Ce que les 29 cas dynamiques montrent (partie 8) :
- défricher en mai plutôt qu'en septembre coûte 243,6 m²HE·an ;
- une toiture de 8 cm au lieu de 15 coûte 298 m²HE·an ; une de 30 cm en rend 93 ;
- éclairer la prairie toute la nuit en 4 000 K coûte 474 ; l'éteindre à 23 h en 2 700 K, à 20 m, en rend 165 ;
- sans plan de gestion, Cnat monte de 426 ; un plan de 50 ans le baisse de 1 741 ;
- à Marignane, une mare sans bassin versant s'assèche au printemps ; raccordée ou à fond étanche, elle tient ;
- d'une zone climatique à l'autre, l'écart reste faible (moins de 73 m²HE·an), parce que la végétation de chaque zone est jugée sur son propre climat ; c'est le réchauffement au fil de la période et les choix de conception qui pèsent.

## Volume

VOLUME_A_COMPLETER

## Fichiers

| Objet | Fichier |
|---|---|
| Édition complète, Word et PDF | `livraison/Méthode de calcul OpenNAT v1, édition complète.docx` et `.pdf` |
| Texte de la méthode seul (23 pages) | `livraison/Méthode de calcul OpenNAT v1.docx` et `.pdf` |
| Modules dynamiques | `outils/climat.py`, `outils/dynamique.py`, branchés dans `outils/carnet_reference.py` |
| Tables nouvelles | `donnees/climat.csv`, `donnees/climat/` (années types), `hydrique.csv`, `eclairage.csv`, `succession.csv`, `chantier.csv` ; constructeurs `outils/construire_climat.py`, `outils/construire_dynamique.py` |
| Fiches A43 à A58 | `methode/edition/03f_fiches_dynamiques.md` |
| Conventions C-W1 à C-W13, C-L1 à C-L4, C-M1 à C-M3, C-K1 à C-K3 | `methode/conventions.md` (70 conventions en tout) |
| Cas dynamiques D01 à D29 | `outils/edition/cas_dynamiques.py`, déroulés en partie 8 |
| RSNat | `schemas/rsnat.xsd` (312 éléments), exemple de l'annexe C validé |

## Points à vérifier avant toute publication

Les trois points du lot 1 bis restent ouverts (licence HabRef, liste UE des espèces exotiques envahissantes, cinq sources secondaires). S'y ajoutent :
1. Les coefficients de stress (sensibilités β, tolérance de 5 jours-équivalents), le facteur spectral, la perte de 0,25 pour l'éclairage, les délais de succession et la sensibilité mensuelle de la faune sont des valeurs de secours : à soumettre au Biodiversity Standard Council avec leurs plages.
2. L'article de Longcore et al. (2018) n'a été lu que par son résumé ; celui d'Azam et al. (2018) aussi (texte intégral payant).
3. La référence exacte de l'arrêté qui porte la BCAE 8 n'a pas été relue sur Légifrance ; la source citée est le ministère de l'Agriculture.
4. La convention C-W3 garde des pluies annuelles constantes : elle sous-estime probablement les sécheresses d'été futures.

## Ce que le go déclenche

Lot 2, moteur : un module de code par fiche algorithme, dont les modules W (climat et bilan hydrique horaire) et T au pas mensuel ; le carnet de référence et ses 68 cas (8 du cahier des charges, 31 complémentaires, 29 dynamiques) servent de banc.
