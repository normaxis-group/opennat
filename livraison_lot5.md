# Livraison du lot 5 : dossier de soumission au Biodiversity Standard Council

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, branche `lot5`, non fusionnée ; aucun dépôt en ligne.
**Versions :** méthode OpenNAT 1, données 1.2.2, moteur 0.2.0.
**État :** projet de dossier, non transmis. Arrêt et attente du go écrit.

## Ce qui est fait

« OpenNAT, dossier de soumission au Biodiversity Standard Council » (15 pages, Word et PDF au papier NORMATYS, dans `livraison/`) : objet de la demande, méthode en bref, vérifications, dix décisions demandées avec la recommandation de l'éditeur, calendrier en deux séances, annexe des 70 conventions, annexe des sources lues pour le dossier.

Les options sont calculées par le moteur sur des copies des tables ; les tables en vigueur ne changent pas de valeur.

| Pièce | Contenu |
|---|---|
| `banc/options_bois.py` et `.json` | quatre options pour le bois (C-G4, C-G5) : actuel, rendement alloué (R = 1,15), pondération relative sur LC-IMPACT, ReCiPe et EF (perte de la coupe rase 0,36 au lieu de 0,50), les deux ; effet sur les cas 7a à 7c, l'annexe C et l'écart avec Carbone 4 |
| `banc/options_pollution.py` et `.json` | voies pour la pollution (C-G8, P19) : eutrophisation terrestre par GLOBIO (3,1 m²HE·an par mol N éq.), eutrophisations par ReCiPe en espèce·an, forfait calé sur Carbone 4 ; chiffrées sur les médianes de neuf bâtiments de RSEE réels (fichiers clients hors dépôt) |
| `documentation/dossier_bsc.md` | source du dossier |

## Ce que les calculs montrent

1. Bois : le rapport bois sur béton du cas 7 passe de 6,2 à 4,8 (O2), 4,1 (O1) ou 3,2 (O3). Recommandation : O2 tout de suite, ses trois sources étant lues ; O3 après lecture complète de la note d'EPD-Norge et des facteurs de conversion de la CEE-ONU, lus par extraits seulement (le site de la CEE-ONU oppose une vérification anti-robot, que je n'ai pas contournée).
2. Pollution : les facteurs ouverts ne retrouvent pas la part de 51 % de Carbone 4. L'eutrophisation terrestre par GLOBIO pèse 0,8 à 1,6 % du climat, les eutrophisations par ReCiPe 0,24 %. L'écart tient à l'écotoxicité et à l'acidification, qu'aucun facteur ouvert ne relie aux unités du RSEE. Recommandation : eutrophisation terrestre dans Inat, eutrophisations en espèce·an à part, chantier de l'écotoxicité, et pas de seuil d'Inat ni de Snat avant.
3. Usines (C-G7) : de l'ordre de 8 m²HE·an par m² de plancher manqueraient face à Carbone 4 ; recommandation de l'afficher plutôt que d'ajouter un proxy.

## Correction de données en route

Sept énoncés de `donnees/conventions.csv` étaient tronqués (C-H7, C-E1, C-C1, C-N2, C-G2, C-W8, C-L3) : le générateur (`outils/controle_donnees.py`) coupait la première phrase à toute abréviation, par exemple « article R. ». Corrigé ; aucune valeur ne change. Données 1.2.2, inscrite au journal des versions avec son empreinte ; instantané de non-régression régénéré (seule l'empreinte change). L'édition complète, dont la partie 9 vient de `methode/conventions.md`, n'est pas touchée.

## Écarts

1. Le dossier ne dit rien de la composition ni du fonctionnement du conseil, qui ne sont pas fixés.
2. La licence entre NORMATYS et IRICE conditionne la publication (D10) ; elle n'est pas traitée ici.
3. La relecture des 191 fiches habitats par un écologue est une condition de D6, non engagée.

## Ce que le go déclenche

À décider : fusionner la branche `lot5` dans la branche principale ; transmettre le dossier au conseil, ou le reprendre ; lire les deux sources du rendement alloué pour lever la réserve sur l'option O3.
