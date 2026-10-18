# Rapport de couverture des tables de données OpenNAT

Produit par `outils/controle_donnees.py`. Une ligne = une valeur.

| Table | Lignes | Primaire | Transposition | Secondaire | Convention |
|---|---|---|---|---|---|
| `connectivite.csv` | 11 | 1 | 4 | 1 | 5 |
| `contexte.csv` | 15 | 2 | 3 | 0 | 10 |
| `eau.csv` | 3 | 0 | 0 | 0 | 3 |
| `etat_criteres.csv` | 92 | 2 | 86 | 0 | 4 |
| `habitats.csv` | 1227 | 0 | 1220 | 0 | 7 |
| `materiaux.csv` | 20 | 10 | 1 | 1 | 8 |
| `nuisances.csv` | 10 | 0 | 0 | 5 | 5 |
| `seuils.csv` | 7 | 0 | 6 | 0 | 1 |
| `sols.csv` | 13 | 0 | 2 | 0 | 11 |
| **Total** | 1398 | 15 | 1322 | 7 | 54 |

Part des valeurs lues dans une source primaire ou transposées d'une source primaire : 96 %. Sources secondaires : 1 %. Conventions : 4 %.

Types : primaire = valeur lue telle quelle dans la source ; transposition = valeur lue dans une source primaire et appliquée à OpenNAT par une correspondance ou un changement d'échelle écrit en convention ; secondaire = valeur lue dans une source qui en cite une autre, à remplacer par la source primaire ; convention = valeur fixée par OpenNAT et justifiée.

## Conventions citées par les tables

| Convention | Lignes |
|---|---|
| C-C1 | 3 |
| C-C2 | 5 |
| C-C3 | 3 |
| C-E1 | 3 |
| C-E2 | 4 |
| C-E3 | 2 |
| C-E4 | 2 |
| C-E5 | 1 |
| C-E6 | 5 |
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
| C-H3 | 7 |
| C-H5 | 138 |
| C-H6 | 78 |
| C-H7 | 1 |
| C-H8 | 9 |
| C-N1 | 4 |
| C-N2 | 3 |
| C-N3 | 3 |
| C-S1 | 13 |
| C-T1 | 2 |
| C-T2 | 100 |
| C-T4 | 1 |
| C-T5 | 1 |
| C-T6 | 1 |

Conventions de `conventions.md` sans ligne de données (elles portent sur l'algorithme) : C-B1, C-G1, C-H4, C-I1, C-I2, C-P1, C-S2, C-T3, C-T7.
