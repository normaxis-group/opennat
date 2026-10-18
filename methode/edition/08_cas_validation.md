## Partie 8. Cas de validation

Les huit situations types du cahier des charges (§ 7) sont calculées ci-dessous par le carnet de calcul de référence (`outils/carnet_reference.py`), qui applique les fiches algorithmes de la partie 3 sans Monte-Carlo et sans rien partager avec le futur moteur. Chaque cas donne ses hypothèses, toutes les grandeurs intermédiaires et les indicateurs : le moteur devra les retrouver à 0,1 % près (exigence E10). Les cas 7 et 8 se déclinent en variantes.

Le carnet a d'abord été contrôlé sur l'exemple de l'annexe C de la partie 1, qu'il retrouve à l'identique : V_0 = 270,39 ; I_0 = 13 519,3 ; I_1 = 12 847,4 ; Cnat = 671,9 ; dette de maturité 876,5 ; Inat = 141 842,9 ; Bnat = 59,0.

### Cas 1. Friche urbaine imperméabilisée devenue résidence avec jardin

**Résultat attendu** : gain : Cnat négatif.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 3 000 m² |
| Emprise du bâti | 900 m² |
| Zone biogéographique | atlantique |
| Typologie | logement |
| Durée du chantier | 20 mois (d_ch = 1,667 an) |
| Surface de référence | 2 200 m² |
| Émissions des composants et du chantier | A1-A5 : 520, B : 380, C : 60 |
| Bois | 40 m³ (coupe rase) |
| Granulats | 3 200 t |
| Surface infiltrée en surface | 700 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 3 000 | 0 | satisfait |
| projet | 3 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 2 400 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | VB.1 | sol pleine terre | 300 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I3 | VB.8 | sol pleine terre | 300 | S08 | 1 | 1 | 0,5 | 0,25 | 0,625 | 1 | 0,35 | 1 | 1 | 32,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| F | 300 | 0,35 | 1 | 1 | 0,35 |

Valeur du site sans projet V_0 = 32,81 m²HE ; I_0 = 1 640,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 900 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 300 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.3 | sol pleine terre | 200 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 33,34 | créée | 0 | 1 |
| P4 | VB.6 | sol pleine terre | 300 | S08 | 1 | 1 | 0,375 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 49,74 | créée | 1 | 1 |
| P5 | VB.26 | sol pleine terre | 600 | S08 | 1 | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,5306 | 1 | 1 | 182,38 | créée | 5 | 1 |
| P6 | VB.7 | sol pleine terre | 400 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 81,05 | créée | 1 | 1 |
| P7 | VB.19 | eau | 200 | S11 | 0,6 | 1 | 0,5417 | 0,8 | 0,9 | 1 | 0,5306 | 1 | 1 | 51,73 | créée | 3 | 1 |
| P8 | FA.3 | lineaire | 100 | S08 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5306 | 1 | 1 | 30,95 | créée | 5 | 1 |
| P9 | VB.18a | arbre | 977 |  |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 269,98 | créée | 27 | 1 |
| P10 | VB.11 | hors sol toiture | 600 | S04 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,3887 | 1 | 1 | 51,29 | créée | 1 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 600 | 0,4823 | 1,1 | 1 | 0,5306 |
| T | 600 | 0,3887 | 1 | 1 | 0,3887 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 117,3 | 308,6 | 442,7 | 563,8 | 613,8 | 663,8 | 750,5 | 750,5 | 750,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 640,6 | m²HE·an |
| I_1 | 32 306,9 | m²HE·an |
| Cnat | -30 666,3 | m²HE·an |
| Cnat relatif | -18,692 |  |
| Cnat sur 30 ans | -16 313,1 | m²HE·an |
| Dette de maturité | 5 216,7 | m²HE·an |
| Inat climat | 141 126,7 | m²HE·an |
| Inat bois | 74 074,1 | m²HE·an |
| Inat carrières | 2 736 | m²HE·an |
| Inat | 217 936,8 | m²HE·an |
| Snat | -187 270,5 | m²HE·an |
| Bnat | 66,7 | points |
| Pleine terre | 0,467 |  |
| Imperméabilisation nette | -1 500 | m² |

**Conformité (fiche A40)** : Bnat 66,7 pour un seuil de 45 : atteint ; pleine terre 46,7 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 2. Prairie naturelle en périphérie construite en logements

**Résultat attendu** : forte perte : Cnat positif et élevé.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 10 000 m² |
| Emprise du bâti | 3 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 24 mois (d_ch = 2 an) |
| Surface de référence | 6 000 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 350, C : 50 |
| Bois | 120 m³ (coupe rase) |
| Granulats | 9 000 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 10 000 | 0 | satisfait |
| projet | 10 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 9 700 | S08 | 1 | 1 | 0,8333 | 0,8333 | 0,9167 | 1 | 1,0571 | 1 | 1 | 7 832,3 |
| I2 | FA.3 | lineaire | 300 | S08 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1 | 1,0571 | 1 | 1 | 225,96 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| PR | 30 000 | 0,9192 | 1,15 | 1 | 1,0571 |

Valeur du site sans projet V_0 = 8 058,26 m²HE ; I_0 = 402 913,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 2 000 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 4 000 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,6817 | 1 | 1 | 1 041,44 | créée | 1 | 1 |
| P4 | VB.5 | sol pleine terre | 700 | S08 | 1 | 1 | 0,3333 | 0,4286 | 0,7143 | 1 | 0,6817 | 1 | 1 | 113,61 | créée | 1 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1 | 0,6817 | 1 | 1 | 145,72 | conservée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| JA | 5 000 | 0,6197 | 1,1 | 1 | 0,6817 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 145,7 | 145,7 | 1 300,8 | 1 300,8 | 1 300,8 | 1 300,8 | 1 300,8 | 1 300,8 | 1 300,8 | 1 300,8 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 402 913,1 | m²HE·an |
| I_1 | 62 728,6 | m²HE·an |
| Cnat | 340 184,5 | m²HE·an |
| Cnat relatif | 0,844 |  |
| Cnat sur 30 ans | 205 034,7 | m²HE·an |
| Dette de maturité | 2 310,1 | m²HE·an |
| Inat climat | 355 075,5 | m²HE·an |
| Inat bois | 222 222,2 | m²HE·an |
| Inat carrières | 7 695 | m²HE·an |
| Inat | 584 992,7 | m²HE·an |
| Snat | -925 177,2 | m²HE·an |
| Bnat | 50 | points |
| Pleine terre | 0,5 |  |
| Imperméabilisation nette | 5 000 | m² |

**Conformité (fiche A40)** : Bnat 50 pour un seuil de 45 : atteint ; pleine terre 50 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas 3. Bureaux sur dalle avec toiture végétalisée

**Résultat attendu** : Bnat porté par la dalle et la toiture ; Cnat négatif sur un site déjà imperméable.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 4 000 m² |
| Emprise du bâti | 2 400 m² |
| Zone biogéographique | continentale |
| Typologie | tertiaire |
| Durée du chantier | 22 mois (d_ch = 1,833 an) |
| Surface de référence | 9 000 m² |
| Émissions des composants et du chantier | A1-A5 : 560, B : 420, C : 45 |
| Bois | aucun |
| Granulats | 11 000 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 4 000 | 0 | satisfait |
| projet | 4 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 3 600 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | VB.5 | sol pleine terre | 400 | S08 | 1 | 1 | 0,3333 | 0,1429 | 0,5714 | 1 | 0,3555 | 1 | 1 | 27,09 |
| I3 | VB.18b | arbre | 326 |  |  | 1 | 0,4583 | 0,3333 | 0,6667 | 1 | 0,3555 | 1 | 1 | 35,41 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| A | 400 | 0,3555 | 1 | 1 | 0,3555 |

Valeur du site sans projet V_0 = 62,5 m²HE ; I_0 = 3 125 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 400 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.3 | sol pleine terre | 400 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 66,68 | créée | 0 | 1 |
| P3 | VB.6 | sol sur dalle | 800 | S06 | 0,7 | 0,7 | 0,375 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 83,22 | créée | 1 | 1 |
| P4 | VB.5 | sol sur dalle | 400 | S05 | 0,6 | 0,6 | 0,3333 | 0,4286 | 0,7143 | 1 | 0,4755 | 1 | 1 | 27,17 | créée | 1 | 1 |
| P5 | VB.13 | hors sol toiture | 1 200 | S06 | 0,7 | 1 | 0,2639 | 1 | 1 | 1 | 0,4528 | 1 | 1 | 143,38 | créée | 5 | 1 |
| P6 | VB.15 | hors sol facade | 300 | S09 | 0,4 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 31,37 | créée | 3 | 0,67 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| D | 1 500 | 0,4755 | 1 | 1 | 0,4755 |
| T | 1 200 | 0,4528 | 1 | 1 | 0,4528 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 91 | 218,7 | 288,9 | 341,5 | 341,5 | 341,5 | 341,5 | 341,5 | 341,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 3 125 | m²HE·an |
| I_1 | 16 195,1 | m²HE·an |
| Cnat | -13 070,1 | m²HE·an |
| Cnat relatif | -4,182 |  |
| Cnat sur 30 ans | -7 490,8 | m²HE·an |
| Dette de maturité | 878,2 | m²HE·an |
| Inat climat | 626 125,5 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 9 405 | m²HE·an |
| Inat | 635 530,5 | m²HE·an |
| Snat | -622 460,4 | m²HE·an |
| Bnat | 46 | points |
| Pleine terre | 0 |  |
| Imperméabilisation nette | -1 200 | m² |

**Conformité (fiche A40)** : Bnat 46 pour un seuil de 25 : atteint ; pleine terre 0 % pour un seuil de 15 % : non atteint ; niveau du site : 2.

### Cas 4. Réhabilitation sans emprise nouvelle

**Résultat attendu** : petit gain par la désimperméabilisation de la cour et l'amélioration du jardin.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 500 m² |
| Emprise du bâti | 900 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 14 mois (d_ch = 1,167 an) |
| Surface de référence | 1 600 m² |
| Émissions des composants et du chantier | A1-A5 : 180, B : 260, C : 30 |
| Bois | 15 m³ (coupe selective) |
| Granulats | 300 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 500 | 0 | satisfait |
| projet | 1 500 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | VB.1 | sol pleine terre | 900 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | VB.2 | sol pleine terre | 400 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I3 | VB.7 | sol pleine terre | 200 | S08 | 1 | 1 | 0,4583 | 0,3333 | 0,6667 | 1 | 0,35 | 1 | 1 | 21,39 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 200 | 0,35 | 1 | 1 | 0,35 |

Valeur du site sans projet V_0 = 21,39 m²HE ; I_0 = 1 069,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 900 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | conservée | 0 | 1 |
| P2 | VB.3 | sol pleine terre | 150 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 25 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 250 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3649 | 1 | 1 | 34,84 | créée | 1 | 1 |
| P4 | VB.7 | sol pleine terre | 200 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3649 | 1 | 1 | 27,87 | améliorée | 2 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 450 | 0,3649 | 1 | 1 | 0,3649 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 21,4 | 78,1 | 87,2 | 87,7 | 87,7 | 87,7 | 87,7 | 87,7 | 87,7 | 87,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 069,4 | m²HE·an |
| I_1 | 4 309,2 | m²HE·an |
| Cnat | -3 239,9 | m²HE·an |
| Cnat relatif | -3,03 |  |
| Cnat sur 30 ans | -1 913,3 | m²HE·an |
| Dette de maturité | 76,5 | m²HE·an |
| Inat climat | 44 813,6 | m²HE·an |
| Inat bois | 16 666,7 | m²HE·an |
| Inat carrières | 256,5 | m²HE·an |
| Inat | 61 736,8 | m²HE·an |
| Snat | -58 496,9 | m²HE·an |
| Bnat | 32 | points |
| Pleine terre | 0,3 |  |
| Imperméabilisation nette | -400 | m² |

**Conformité (fiche A40)** : Bnat 32 pour un seuil de 25 : atteint ; pleine terre 30 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 5. Projet en réservoir de biodiversité

**Résultat attendu** : perte plus forte que le cas 2, du fait du multiplicateur de situation.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 10 000 m² |
| Emprise du bâti | 3 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 24 mois (d_ch = 2 an) |
| Surface de référence | 6 000 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 350, C : 50 |
| Bois | 120 m³ (coupe rase) |
| Granulats | 9 000 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 10 000 | 0 | satisfait |
| projet | 10 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 9 700 | S08 | 1 | 1 | 0,8333 | 0,8333 | 0,9167 | 1,15 | 1,0571 | 1 | 1 | 9 007,15 |
| I2 | FA.3 | lineaire | 300 | S08 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1,15 | 1,0571 | 1 | 1 | 259,85 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| PR | 30 000 | 0,9192 | 1,15 | 1 | 1,0571 |

Valeur du site sans projet V_0 = 9 267 m²HE ; I_0 = 463 350,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | 0 | 1 | 0 |  | 1 | 1,15 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 2 000 | S01 | 0 | 1 | 0 |  | 1 | 1,15 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 4 000 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1,15 | 0,6817 | 1 | 1 | 1 197,66 | créée | 1 | 1 |
| P4 | VB.5 | sol pleine terre | 700 | S08 | 1 | 1 | 0,3333 | 0,4286 | 0,7143 | 1,15 | 0,6817 | 1 | 1 | 130,65 | créée | 1 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1,15 | 0,6817 | 1 | 1 | 167,58 | conservée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| JA | 5 000 | 0,6197 | 1,1 | 1 | 0,6817 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 167,6 | 167,6 | 1 495,9 | 1 495,9 | 1 495,9 | 1 495,9 | 1 495,9 | 1 495,9 | 1 495,9 | 1 495,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 463 350,1 | m²HE·an |
| I_1 | 72 137,9 | m²HE·an |
| Cnat | 391 212,1 | m²HE·an |
| Cnat relatif | 0,844 |  |
| Cnat sur 30 ans | 235 789,9 | m²HE·an |
| Dette de maturité | 2 656,6 | m²HE·an |
| Inat climat | 355 075,5 | m²HE·an |
| Inat bois | 222 222,2 | m²HE·an |
| Inat carrières | 7 695 | m²HE·an |
| Inat | 584 992,7 | m²HE·an |
| Snat | -976 204,9 | m²HE·an |
| Bnat | 50 | points |
| Pleine terre | 0,5 |  |
| Imperméabilisation nette | 5 000 | m² |

**Conformité (fiche A40)** : Bnat 50 pour un seuil de 45 : atteint ; pleine terre 50 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas 6. Mare et haies créées sur une culture intensive

**Résultat attendu** : gain à maturité, dette de maturité élevée.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | continentale |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Surface de référence | 0 m² |
| Émissions des composants et du chantier | aucun bâtiment |
| Bois | aucun |
| Granulats | 200 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 | 1 | 1 | 0,25 |  | 1 | 1 | 1 | 1 | 1 | 1 250 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 1 250 m²HE ; I_0 = 62 500 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 50,01 | créée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 199,2 | 497,7 | 796,1 | 1 337 | 1 484,9 | 1 504,1 | 1 523,4 | 1 561,9 | 1 571,6 | 1 571,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 62 500 | m²HE·an |
| I_1 | 73 221,7 | m²HE·an |
| Cnat | -10 721,7 | m²HE·an |
| Cnat relatif | -0,172 |  |
| Cnat sur 30 ans | -4 298,2 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 10 550,7 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 7a. Bâtiment en béton

**Résultat attendu** : Inat climat dominant.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 3 000 m² |
| Emprise du bâti | 1 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 000 m² |
| Émissions des composants et du chantier | A1-A5 : 560, B : 300, C : 60 |
| Bois | 20 m³ (coupe rase) |
| Granulats | 9 500 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 3 000 | 0 | satisfait |
| projet | 3 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 | créée | 1 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 125,2 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 757 | m²HE·an |
| I_1 | 12 145,8 | m²HE·an |
| Cnat | 9 611,1 | m²HE·an |
| Cnat relatif | 0,442 |  |
| Cnat sur 30 ans | 5 916,9 | m²HE·an |
| Dette de maturité | 375,6 | m²HE·an |
| Inat climat | 256 594 | m²HE·an |
| Inat bois | 37 037 | m²HE·an |
| Inat carrières | 8 122,5 | m²HE·an |
| Inat | 301 753,5 | m²HE·an |
| Snat | -311 364,7 | m²HE·an |
| Bnat | 46,7 | points |
| Pleine terre | 0,467 |  |
| Imperméabilisation nette | 1 600 | m² |

**Conformité (fiche A40)** : Bnat 46,7 pour un seuil de 45 : atteint ; pleine terre 46,7 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas 7b. Même bâtiment en bois, origine non justifiée

**Résultat attendu** : climat plus faible, occupation des forêts plus forte.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 3 000 m² |
| Emprise du bâti | 1 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 000 m² |
| Émissions des composants et du chantier | A1-A5 : 400, B : 300, C : 70 |
| Bois | 900 m³ (coupe rase) |
| Granulats | 2 500 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 3 000 | 0 | satisfait |
| projet | 3 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 | créée | 1 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 125,2 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 757 | m²HE·an |
| I_1 | 12 145,8 | m²HE·an |
| Cnat | 9 611,1 | m²HE·an |
| Cnat relatif | 0,442 |  |
| Cnat sur 30 ans | 5 916,9 | m²HE·an |
| Dette de maturité | 375,6 | m²HE·an |
| Inat climat | 198 770 | m²HE·an |
| Inat bois | 1 666 666,7 | m²HE·an |
| Inat carrières | 2 137,5 | m²HE·an |
| Inat | 1 867 574,2 | m²HE·an |
| Snat | -1 877 185,3 | m²HE·an |
| Bnat | 46,7 | points |
| Pleine terre | 0,467 |  |
| Imperméabilisation nette | 1 600 | m² |

**Conformité (fiche A40)** : Bnat 46,7 pour un seuil de 45 : atteint ; pleine terre 46,7 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas 7c. Même bâtiment en bois issu de coupe sélective justifiée

**Résultat attendu** : Inat le plus faible des trois.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 3 000 m² |
| Emprise du bâti | 1 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 000 m² |
| Émissions des composants et du chantier | A1-A5 : 400, B : 300, C : 70 |
| Bois | 900 m³ (coupe selective) |
| Granulats | 2 500 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 3 000 | 0 | satisfait |
| projet | 3 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 | créée | 1 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 125,2 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 | 250,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 757 | m²HE·an |
| I_1 | 12 145,8 | m²HE·an |
| Cnat | 9 611,1 | m²HE·an |
| Cnat relatif | 0,442 |  |
| Cnat sur 30 ans | 5 916,9 | m²HE·an |
| Dette de maturité | 375,6 | m²HE·an |
| Inat climat | 198 770 | m²HE·an |
| Inat bois | 1 000 000 | m²HE·an |
| Inat carrières | 2 137,5 | m²HE·an |
| Inat | 1 200 907,5 | m²HE·an |
| Snat | -1 210 518,6 | m²HE·an |
| Bnat | 46,7 | points |
| Pleine terre | 0,467 |  |
| Imperméabilisation nette | 1 600 | m² |

**Conformité (fiche A40)** : Bnat 46,7 pour un seuil de 45 : atteint ; pleine terre 46,7 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas 8a. Aménagement en zone continentale

**Résultat attendu** : référence.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | continentale |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Surface de référence | 0 m² |
| Émissions des composants et du chantier | aucun bâtiment |
| Bois | aucun |
| Granulats | 200 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 | 1 | 1 | 0,25 |  | 1 | 1 | 1 | 1 | 1 | 1 250 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 1 250 m²HE ; I_0 = 62 500 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 50,01 | créée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 199,2 | 497,7 | 796,1 | 1 337 | 1 484,9 | 1 504,1 | 1 523,4 | 1 561,9 | 1 571,6 | 1 571,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 62 500 | m²HE·an |
| I_1 | 73 221,7 | m²HE·an |
| Cnat | -10 721,7 | m²HE·an |
| Cnat relatif | -0,172 |  |
| Cnat sur 30 ans | -4 298,2 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 10 550,7 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 8b. Même aménagement en zone méditerranéenne

**Résultat attendu** : identique en v1 (convention C-E2).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Surface de référence | 0 m² |
| Émissions des composants et du chantier | aucun bâtiment |
| Bois | aucun |
| Granulats | 200 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 | 1 | 1 | 0,25 |  | 1 | 1 | 1 | 1 | 1 | 1 250 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 1 250 m²HE ; I_0 = 62 500 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 50,01 | créée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 199,2 | 497,7 | 796,1 | 1 337 | 1 484,9 | 1 504,1 | 1 523,4 | 1 561,9 | 1 571,6 | 1 571,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 62 500 | m²HE·an |
| I_1 | 73 221,7 | m²HE·an |
| Cnat | -10 721,7 | m²HE·an |
| Cnat relatif | -0,172 |  |
| Cnat sur 30 ans | -4 298,2 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 10 550,7 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 8c. Zone méditerranéenne, délais allongés de 25 % (borne haute de C-E2)

**Résultat attendu** : perte de valeur intégrée par allongement des délais.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Surface de référence | 0 m² |
| Émissions des composants et du chantier | aucun bâtiment |
| Bois | aucun |
| Granulats | 200 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 | 1 | 1 | 0,25 |  | 1 | 1 | 1 | 1 | 1 | 1 250 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 1 250 m²HE ; I_0 = 62 500 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 | créée | 3,8 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 | créée | 6,2 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 | créée | 6,2 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 | créée | 40 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 1 | 1 | 1 | 50,01 | créée | 0 | 1 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 169,4 | 408,1 | 646,9 | 1 102 | 1 477,5 | 1 493 | 1 508,4 | 1 539,2 | 1 570 | 1 571,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 62 500 | m²HE·an |
| I_1 | 71 890 | m²HE·an |
| Cnat | -9 390 | m²HE·an |
| Cnat relatif | -0,15 |  |
| Cnat sur 30 ans | -3 113 | m²HE·an |
| Dette de maturité | 6 687,8 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 9 219 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Synthèse et propriétés vérifiées

| Cas | Attendu | Cnat | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|
| Cas 1. Friche urbaine imperméabilisée devenue résidence avec jardin | gain : Cnat négatif | -30 666 | 217 937 | -187 271 | 66,7 | 2 |
| Cas 2. Prairie naturelle en périphérie construite en logements | forte perte : Cnat positif et élevé | 340 184 | 584 993 | -925 177 | 50 | 0 |
| Cas 3. Bureaux sur dalle avec toiture végétalisée | Bnat porté par la dalle et la toiture ; Cnat négatif sur un site déjà imperméable | -13 070 | 635 531 | -622 460 | 46 | 2 |
| Cas 4. Réhabilitation sans emprise nouvelle | petit gain par la désimperméabilisation de la cour et l'amélioration du jardin | -3 240 | 61 737 | -58 497 | 32 | 2 |
| Cas 5. Projet en réservoir de biodiversité | perte plus forte que le cas 2, du fait du multiplicateur de situation | 391 212 | 584 993 | -976 205 | 50 | 0 |
| Cas 6. Mare et haies créées sur une culture intensive | gain à maturité, dette de maturité élevée | -10 722 | 171 | 10 551 | 92,8 | 2 |
| Cas 7a. Bâtiment en béton | Inat climat dominant | 9 611 | 301 754 | -311 365 | 46,7 | 0 |
| Cas 7b. Même bâtiment en bois, origine non justifiée | climat plus faible, occupation des forêts plus forte | 9 611 | 1 867 574 | -1 877 185 | 46,7 | 0 |
| Cas 7c. Même bâtiment en bois issu de coupe sélective justifiée | Inat le plus faible des trois | 9 611 | 1 200 908 | -1 210 519 | 46,7 | 0 |
| Cas 8a. Aménagement en zone continentale | référence | -10 722 | 171 | 10 551 | 92,8 | 2 |
| Cas 8b. Même aménagement en zone méditerranéenne | identique en v1 (convention C-E2) | -10 722 | 171 | 10 551 | 92,8 | 2 |
| Cas 8c. Zone méditerranéenne, délais allongés de 25 % (borne haute de C-E2) | perte de valeur intégrée par allongement des délais | -9 390 | 171 | 9 219 | 92,8 | 2 |

Propriétés vérifiées par ces cas :

- Une friche imperméabilisée transformée en résidence avec jardin gagne de la nature : Cnat = -30 666 m²HE·an (cas 1).
- La construction d'une prairie riche fait perdre l'essentiel de sa valeur au site : Cnat relatif = 0,844 (cas 2).
- La même opération en réservoir perd davantage : 391 212 contre 340 184 m²HE·an, soit le rapport du multiplicateur de situation (cas 5).
- Les bureaux sur dalle atteignent le seuil de Bnat du tertiaire grâce à la dalle et à la toiture, mais pas celui de la pleine terre, nulle (cas 3).
- La réhabilitation gagne un peu de nature par la cour désimperméabilisée et le jardin amélioré (cas 4).
- La mare, les haies et le boisement créés sur une culture laissent une dette de maturité de 5 356 m²HE·an (cas 6).
- Bois et béton (cas 7) : Inat vaut 301 754 pour le béton, 1 867 574 pour le bois d'origine non justifiée et 1 200 908 pour le bois de coupe sélective justifiée.
- Zone méditerranéenne (cas 8) : sans différence en v1 ; avec des délais allongés de 25 %, Cnat passe de -10 722 à -9 390 m²HE·an.

### Lecture du cas 7

Avec les conventions de la v1, le bâtiment en bois a une biodiversité grise plusieurs fois plus forte que le même bâtiment en béton. Le climat est plus faible pour le bois, mais l'occupation des forêts, comptée en surface et en durée à la perte de MSA du régime d'exploitation, l'emporte largement. Le sens de l'écart est celui de la littérature citée par l'audit (Christiansson et Roos 2023 ; Carbone 4, 2026, pour qui une substitution par du bois de provenance non maîtrisée triple la pression de changement d'usage des sols) ; son ampleur dépend de trois conventions à soumettre au Biodiversity Standard Council : le rapport de 2 m³ de bois rond par m³ de produit (C-G4), le choix d'une approche attributionnelle qui compte toute la forêt de production comme une perte par rapport à la forêt naturelle (C-G5), et l'absence de prise en compte de l'occupation des usines et des carrières de ciment pour les autres matériaux (C-G7), qui avantage le béton. Ce cas est le premier à recalibrer.
