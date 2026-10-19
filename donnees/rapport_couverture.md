# Rapport de couverture des tables de données OpenNAT

Produit par `outils/controle_donnees.py`. Une ligne = une valeur.

| Table | Lignes | Primaire | Transposition | Secondaire | Convention |
|---|---|---|---|---|---|
| `chantier.csv` | 51 | 0 | 12 | 0 | 39 |
| `climat.csv` | 128 | 128 | 0 | 0 | 0 |
| `connectivite.csv` | 11 | 1 | 4 | 1 | 5 |
| `constantes.csv` | 70 | 30 | 0 | 0 | 40 |
| `contexte.csv` | 15 | 2 | 3 | 0 | 10 |
| `eau.csv` | 3 | 0 | 0 | 0 | 3 |
| `eclairage.csv` | 18 | 7 | 1 | 0 | 10 |
| `etat_criteres.csv` | 100 | 2 | 94 | 0 | 4 |
| `habitats.csv` | 1732 | 0 | 1725 | 0 | 7 |
| `hydrique.csv` | 75 | 28 | 23 | 0 | 24 |
| `materiaux.csv` | 20 | 10 | 1 | 1 | 8 |
| `nuisances.csv` | 10 | 0 | 0 | 5 | 5 |
| `seuils.csv` | 9 | 0 | 8 | 0 | 1 |
| `sols.csv` | 13 | 0 | 2 | 0 | 11 |
| `succession.csv` | 19 | 11 | 1 | 0 | 7 |
| **Total** | 2274 | 219 | 1874 | 7 | 174 |

Part des valeurs lues dans une source primaire ou transposées d'une source primaire : 92 %. Sources secondaires : 0 %. Conventions : 8 %.

Types : primaire = valeur lue telle quelle dans la source ; transposition = valeur lue dans une source primaire et appliquée à OpenNAT par une correspondance ou un changement d'échelle écrit en convention ; secondaire = valeur lue dans une source qui en cite une autre, à remplacer par la source primaire ; convention = valeur fixée par OpenNAT et justifiée.

## Conventions citées par les tables

| Convention | Lignes |
|---|---|
| C-B1 | 1 |
| C-C1 | 3 |
| C-C2 | 5 |
| C-C3 | 3 |
| C-E1 | 3 |
| C-E2 | 4 |
| C-E3 | 3 |
| C-E4 | 2 |
| C-E5 | 1 |
| C-E6 | 7 |
| C-E7 | 2 |
| C-G2 | 6 |
| C-G3 | 4 |
| C-G4 | 2 |
| C-G5 | 4 |
| C-G6 | 2 |
| C-G7 | 1 |
| C-G8 | 1 |
| C-H1 | 185 |
| C-H2 | 3 |
| C-H3 | 9 |
| C-H5 | 144 |
| C-H6 | 88 |
| C-H7 | 1 |
| C-H8 | 10 |
| C-I2 | 7 |
| C-K1 | 37 |
| C-K2 | 13 |
| C-K3 | 2 |
| C-L1 | 4 |
| C-L2 | 7 |
| C-L3 | 2 |
| C-L4 | 12 |
| C-M1 | 4 |
| C-M2 | 15 |
| C-N1 | 4 |
| C-N2 | 3 |
| C-N3 | 3 |
| C-S1 | 16 |
| C-T1 | 2 |
| C-T2 | 191 |
| C-T4 | 1 |
| C-T5 | 1 |
| C-T6 | 1 |
| C-W1 | 26 |
| C-W10 | 2 |
| C-W11 | 7 |
| C-W12 | 3 |
| C-W13 | 6 |
| C-W2 | 38 |
| C-W3 | 96 |
| C-W4 | 19 |
| C-W5 | 1 |
| C-W6 | 34 |
| C-W7 | 2 |
| C-W8 | 1 |
| C-W9 | 11 |

Conventions de `conventions.md` sans ligne de données (elles portent sur l'algorithme) : C-G1, C-H4, C-I1, C-M3, C-P1, C-R1, C-R2, C-R3, C-R4, C-R5, C-S2, C-T3, C-T7.
