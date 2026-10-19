# Livraison du lot 6 : écotoxicité, acidification et biodiversité grise

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, branche `main` ; aucun dépôt en ligne.
**Versions :** méthode OpenNAT 1, données 1.2.2, moteur 0.2.0 (inchangés : le lot ne modifie ni tables ni moteur).
**État :** note livrée, rien n'est transmis. Arrêt et attente du go écrit.

## Ce qui est fait

- « OpenNAT, pollution et biodiversité grise » (5 pages, Word et PDF au papier NORMATYS, dans `livraison/`) : un pont publié et ouvert pour chacun des cinq indicateurs de pollution du RSEE, chiffré sur neuf bâtiments réels, explication de l'écart avec Carbone 4, options pour le conseil, transposition prête à appliquer (convention C-G8 réécrite, cinq lignes de `materiaux.csv`, équation A36-2).
- `banc/options_pollution.py` et `.json` réécrits : les cinq ponts avec leurs plages.
- Dossier de soumission mis à jour : décision D3 (recommandation P5), sources ajoutées, calendrier.

## Ce que les calculs montrent

| Indicateur | Pont | m²HE·an par m² de S_ref, bâtiment médian |
|---|---|---|
| 106 acidification | ReCiPe 2016 par la densité d'espèces terrestres | 1,4 à 2,3 |
| 107 eutrophisation des eaux douces | ReCiPe 2016, IMPACT World+ | 0,3 à 2,7 |
| 108 eutrophisation marine | IMPACT World+ | 0,5 |
| 109 eutrophisation terrestre | GLOBIO 3.5 | 0,6 à 1,2 |
| 116 écotoxicité | IMPACT World+ (0,5 / 2,5 m / 365 jours) | 0,001 |

Pollution totale : 4 à 9 % du climat sur le bâtiment médian, 0 à 13 % bâtiment par bâtiment. Carbone 4 trouve 134 % : son modèle (ecoinvent mis à l'échelle du carbone, écotoxicité à long terme des métaux par IMPACT World+) ne se reconstruit pas depuis les données d'une étude RE2020. Recommandation : P5, les cinq ponts additionnés à Inat avec leurs plages, en disant que l'écotoxicité à long terme des métaux n'est pas comptée.

## Sources lues

Bulle et al. 2019, IMPACT World+ (article et supplément, Polytechnique Montréal, CC BY 4.0) ; ReCiPe 2016, rapport RIVM et tableur v1.1 (densités d'espèces, facteurs d'acidification et d'eutrophisation) ; GLOBIO 3.5, tableau 4.1 ; arrêté du 4 août 2021, annexe II.

## Écarts

1. Les facteurs EF du dépassement cumulé (1,31, 0,74 et 3,02 mol H+ éq. par kg de SO2, NOx et NH3) ont été relus le 19/10/2026 sur la méthode EF publiée par ÖKOBAU.DAT (version 01.03.010) : réserve levée.
2. Le pont 116 applique la conversion d'IMPACT World+ à des CTUe de la variante EF d'USEtox : ordre de grandeur seulement.
3. Les médianes viennent de neuf bâtiments ; un cas de banc portant ces indicateurs serait à ajouter si P5 est retenue.

## Ce que le go déclenche

Transmettre le dossier et la note au conseil, ou les reprendre ; appliquer la transposition P5 dès qu'elle est retenue.
