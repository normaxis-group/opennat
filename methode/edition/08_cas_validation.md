## Partie 8. Cas de validation

Les huit situations types du cahier des charges (§ 7) sont calculées ci-dessous par le carnet de calcul de référence (`outils/carnet_reference.py`), qui applique les fiches algorithmes de la partie 3 sans Monte-Carlo et sans rien partager avec le futur moteur. Chaque cas donne ses hypothèses, toutes les grandeurs intermédiaires et les indicateurs : le moteur devra les retrouver à 0,1 % près (exigence E10). Les cas 7 et 8 se déclinent en variantes.

Le carnet a d'abord été contrôlé sur l'exemple de l'annexe C de la partie 1, qu'il retrouve à l'identique : V_0 = 270,39 ; I_0 = 13 519,3 ; I_1 = 12 051,0 ; Cnat = 1 468,3 ; dette de maturité 860,2 ; Inat = 141 842,9 ; Bnat = 59,0.

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 2 400 | S01 |
| I2 | VB.1 | sol pleine terre | 300 | S01 |
| I3 | VB.8 | sol pleine terre | 300 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I3 | 1 | 1 | 0,5 | 0,25 | 0,625 | 1 | 0,35 | 1 | 1 | 32,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| F | 300 | 0,35 | 1 | 1 | 0,35 |

Valeur du site sans projet V_0 = 32,81 m²HE ; I_0 = 1 640,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 900 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P3 | VB.3 | sol pleine terre | 200 | S02 | créée | 0 | 1 |
| P4 | VB.6 | sol pleine terre | 300 | S08 | créée | 1 | 1 |
| P5 | VB.26 | sol pleine terre | 600 | S08 | créée | 5 | 1 |
| P6 | VB.7 | sol pleine terre | 400 | S08 | créée | 1 | 1 |
| P7 | VB.19 | eau | 200 | S11 | créée | 3 | 1 |
| P8 | FA.3 | lineaire | 100 | S08 | créée | 5 | 1 |
| P9 | VB.18a | arbre | 977 |  | créée | 27 | 1 |
| P10 | VB.11 | hors sol toiture | 600 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 11,67 |
| P4 | 1 | 1 | 0,375 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 49,74 |
| P5 | 1 | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,5306 | 1 | 1 | 182,38 |
| P6 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 81,05 |
| P7 | 0,6 | 1 | 0,5417 | 0,8 | 0,9 | 1 | 0,5306 | 1 | 1 | 51,73 |
| P8 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5306 | 1 | 1 | 30,95 |
| P9 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5306 | 1 | 1 | 269,98 |
| P10 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,3887 | 1 | 1 | 51,29 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 600 | 0,4823 | 1,1 | 1 | 0,5306 |
| T | 600 | 0,3887 | 1 | 1 | 0,3887 |
| isolee_P3 | 200 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 95,7 | 287 | 421 | 542,1 | 592,1 | 642,1 | 728,8 | 728,8 | 728,8 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 640,6 | m²HE·an |
| I_1 | 31 245 | m²HE·an |
| Cnat | -29 604,4 | m²HE·an |
| Cnat relatif | -18,045 |  |
| Cnat sur 30 ans | -15 684,6 | m²HE·an |
| Dette de maturité | 5 195 | m²HE·an |
| Inat climat | 141 126,7 | m²HE·an |
| Inat bois | 74 074,1 | m²HE·an |
| Inat carrières | 2 736 | m²HE·an |
| Inat | 217 936,8 | m²HE·an |
| Snat | -188 332,4 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 9 700 | S08 |
| I2 | FA.3 | lineaire | 300 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,8333 | 0,9167 | 1 | 1,0571 | 1 | 1 | 7 832,3 |
| I2 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1 | 1,0571 | 1 | 1 | 225,96 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| PR | 30 000 | 0,9192 | 1,15 | 1 | 1,0571 |

Valeur du site sans projet V_0 = 8 058,26 m²HE ; I_0 = 402 913,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 2 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 4 000 | S08 | créée | 1 | 1 |
| P4 | VB.5 | sol pleine terre | 700 | S08 | créée | 1 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | conservée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,6817 | 1 | 1 | 1 041,44 |
| P4 | 1 | 1 | 0,3333 | 0,4286 | 0,7143 | 1 | 0,6817 | 1 | 1 | 113,61 |
| P5 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1 | 0,6817 | 1 | 1 | 145,72 |

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 3 600 | S01 |
| I2 | VB.5 | sol pleine terre | 400 | S08 |
| I3 | VB.18b | arbre | 326 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | 1 | 1 | 0,3333 | 0,1429 | 0,5714 | 1 | 0,3555 | 1 | 1 | 27,09 |
| I3 |  | 1 | 0,4583 | 0,3333 | 0,6667 | 1 | 0,3555 | 1 | 1 | 35,41 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| A | 400 | 0,3555 | 1 | 1 | 0,3555 |

Valeur du site sans projet V_0 = 62,5 m²HE ; I_0 = 3 125 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 400 | S01 | créée | 0 | 1 |
| P2 | VB.3 | sol pleine terre | 400 | S02 | créée | 0 | 1 |
| P3 | VB.6 | sol sur dalle | 800 | S06 | créée | 1 | 1 |
| P4 | VB.5 | sol sur dalle | 400 | S05 | créée | 1 | 1 |
| P5 | VB.13 | hors sol toiture | 1 200 | S06 | créée | 5 | 1 |
| P6 | VB.15 | hors sol facade | 300 | S09 | créée | 3 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,3555 | 1 | 1 | 23,71 |
| P3 | 0,7 | 0,7 | 0,375 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 83,22 |
| P4 | 0,6 | 0,6 | 0,3333 | 0,4286 | 0,7143 | 1 | 0,4755 | 1 | 1 | 27,17 |
| P5 | 0,7 | 1 | 0,2639 | 1 | 1 | 1 | 0,4528 | 1 | 1 | 143,38 |
| P6 | 0,4 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 31,37 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| D | 1 500 | 0,4755 | 1 | 1 | 0,4755 |
| T | 1 200 | 0,4528 | 1 | 1 | 0,4528 |
| isolee_P2 | 400 | 0,3555 | 1 | 1 | 0,3555 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 48,1 | 175,7 | 245,9 | 298,5 | 298,5 | 298,5 | 298,5 | 298,5 | 298,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 3 125 | m²HE·an |
| I_1 | 14 089,4 | m²HE·an |
| Cnat | -10 964,4 | m²HE·an |
| Cnat relatif | -3,509 |  |
| Cnat sur 30 ans | -6 244,6 | m²HE·an |
| Dette de maturité | 835,3 | m²HE·an |
| Inat climat | 626 125,5 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 9 405 | m²HE·an |
| Inat | 635 530,5 | m²HE·an |
| Snat | -624 566,1 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.1 | sol pleine terre | 900 | S01 |
| I2 | VB.2 | sol pleine terre | 400 | S01 |
| I3 | VB.7 | sol pleine terre | 200 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| I3 | 1 | 1 | 0,4583 | 0,3333 | 0,6667 | 1 | 0,35 | 1 | 1 | 21,39 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 200 | 0,35 | 1 | 1 | 0,35 |

Valeur du site sans projet V_0 = 21,39 m²HE ; I_0 = 1 069,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 900 | S01 | conservée | 0 | 1 |
| P2 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 250 | S08 | créée | 1 | 1 |
| P4 | VB.7 | sol pleine terre | 200 | S08 | améliorée | 2 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3649 | 1 | 1 | 34,84 |
| P4 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3649 | 1 | 1 | 27,87 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 450 | 0,3649 | 1 | 1 | 0,3649 |
| isolee_P2 | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 21,4 | 61,9 | 70,9 | 71,5 | 71,5 | 71,5 | 71,5 | 71,5 | 71,5 | 71,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 069,4 | m²HE·an |
| I_1 | 3 512,8 | m²HE·an |
| Cnat | -2 443,5 | m²HE·an |
| Cnat relatif | -2,285 |  |
| Cnat sur 30 ans | -1 442 | m²HE·an |
| Dette de maturité | 60,2 | m²HE·an |
| Inat climat | 44 813,6 | m²HE·an |
| Inat bois | 16 666,7 | m²HE·an |
| Inat carrières | 256,5 | m²HE·an |
| Inat | 61 736,8 | m²HE·an |
| Snat | -59 293,3 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 9 700 | S08 |
| I2 | FA.3 | lineaire | 300 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,8333 | 0,9167 | 1,15 | 1,0571 | 1 | 1 | 9 007,15 |
| I2 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1,15 | 1,0571 | 1 | 1 | 259,85 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| PR | 30 000 | 0,9192 | 1,15 | 1 | 1,0571 |

Valeur du site sans projet V_0 = 9 267 m²HE ; I_0 = 463 350,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 2 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 4 000 | S08 | créée | 1 | 1 |
| P4 | VB.5 | sol pleine terre | 700 | S08 | créée | 1 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | conservée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1,15 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1,15 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1,15 | 0,6817 | 1 | 1 | 1 197,66 |
| P4 | 1 | 1 | 0,3333 | 0,4286 | 0,7143 | 1,15 | 0,6817 | 1 | 1 | 130,65 |
| P5 | 1 | 1 | 0,7917 | 0,8 | 0,9 | 1,15 | 0,6817 | 1 | 1 | 167,58 |

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | créée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 |
| P2 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 |
| P3 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 |
| P4 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 |
| P5 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 17,5 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |
| isolee_P5 | 300 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 166,7 | 465,2 | 763,6 | 1 304,5 | 1 452,4 | 1 471,6 | 1 490,9 | 1 529,4 | 1 539 | 1 539 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 71 596,3 | m²HE·an |
| Cnat | -32 862,2 | m²HE·an |
| Cnat relatif | -0,848 |  |
| Cnat sur 30 ans | -17 582,6 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 32 691,2 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 |

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 |

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.6 | sol pleine terre | 3 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,3333 | 0,5714 | 0,7857 | 1 | 0,5539 | 1 | 1 | 435,14 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 757 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 600 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 400 | S08 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4684 | 1 | 1 | 250,43 |

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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | créée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 |
| P2 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 |
| P3 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 |
| P4 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 |
| P5 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 17,5 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |
| isolee_P5 | 300 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 166,7 | 465,2 | 763,6 | 1 304,5 | 1 452,4 | 1 471,6 | 1 490,9 | 1 529,4 | 1 539 | 1 539 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 71 596,3 | m²HE·an |
| Cnat | -32 862,2 | m²HE·an |
| Cnat relatif | -0,848 |  |
| Cnat sur 30 ans | -17 582,6 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 32 691,2 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | créée | 3 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | créée | 5 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | créée | 5 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | créée | 32 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | créée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 |
| P2 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 |
| P3 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 |
| P4 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 |
| P5 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 17,5 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |
| isolee_P5 | 300 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 166,7 | 465,2 | 763,6 | 1 304,5 | 1 452,4 | 1 471,6 | 1 490,9 | 1 529,4 | 1 539 | 1 539 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 71 596,3 | m²HE·an |
| Cnat | -32 862,2 | m²HE·an |
| Cnat relatif | -0,848 |  |
| Cnat sur 30 ans | -17 582,6 | m²HE·an |
| Dette de maturité | 5 356,2 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 32 691,2 | m²HE·an |
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

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.20 | eau | 300 | S11 | créée | 3,8 | 1 |
| P2 | FA.3 | lineaire | 600 | S08 | créée | 6,2 | 1 |
| P3 | VB.26 | sol pleine terre | 3 000 | S08 | créée | 6,2 | 1 |
| P4 | G1.A | sol pleine terre | 800 | S08 | créée | 40 | 0,33 |
| P5 | VB.3 | sol pleine terre | 300 | S02 | créée | 0 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0,6 | 1 | 0,625 | 0,7778 | 0,8889 | 1 | 0,6725 | 1 | 1 | 112,08 |
| P2 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,6725 | 1 | 1 | 235,39 |
| P3 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 1 050,79 |
| P4 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6725 | 1 | 1 | 373,6 |
| P5 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 17,5 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| N | 4 700 | 0,6114 | 1,1 | 1 | 0,6725 |
| isolee_P5 | 300 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 136,9 | 375,6 | 614,4 | 1 069,5 | 1 445 | 1 460,5 | 1 475,9 | 1 506,7 | 1 537,5 | 1 539 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 70 264,7 | m²HE·an |
| Cnat | -31 530,5 | m²HE·an |
| Cnat relatif | -0,814 |  |
| Cnat sur 30 ans | -16 397,3 | m²HE·an |
| Dette de maturité | 6 687,8 | m²HE·an |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 31 359,5 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Synthèse et propriétés vérifiées

| Cas | Attendu | Cnat | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|
| Cas 1. Friche urbaine imperméabilisée devenue résidence avec jardin | gain : Cnat négatif | -29 604 | 217 937 | -188 332 | 66,7 | 2 |
| Cas 2. Prairie naturelle en périphérie construite en logements | forte perte : Cnat positif et élevé | 340 184 | 584 993 | -925 177 | 50 | 0 |
| Cas 3. Bureaux sur dalle avec toiture végétalisée | Bnat porté par la dalle et la toiture ; Cnat négatif sur un site déjà imperméable | -10 964 | 635 531 | -624 566 | 46 | 2 |
| Cas 4. Réhabilitation sans emprise nouvelle | petit gain par la désimperméabilisation de la cour et l'amélioration du jardin | -2 443 | 61 737 | -59 293 | 32 | 2 |
| Cas 5. Projet en réservoir de biodiversité | perte plus forte que le cas 2, du fait du multiplicateur de situation | 391 212 | 584 993 | -976 205 | 50 | 0 |
| Cas 6. Mare et haies créées sur une culture intensive | gain à maturité, dette de maturité élevée | -32 862 | 171 | 32 691 | 92,8 | 2 |
| Cas 7a. Bâtiment en béton | Inat climat dominant | 9 611 | 301 754 | -311 365 | 46,7 | 0 |
| Cas 7b. Même bâtiment en bois, origine non justifiée | climat plus faible, occupation des forêts plus forte | 9 611 | 1 867 574 | -1 877 185 | 46,7 | 0 |
| Cas 7c. Même bâtiment en bois issu de coupe sélective justifiée | Inat le plus faible des trois | 9 611 | 1 200 908 | -1 210 519 | 46,7 | 0 |
| Cas 8a. Aménagement en zone continentale | référence | -32 862 | 171 | 32 691 | 92,8 | 2 |
| Cas 8b. Même aménagement en zone méditerranéenne | identique en v1 (convention C-E2) | -32 862 | 171 | 32 691 | 92,8 | 2 |
| Cas 8c. Zone méditerranéenne, délais allongés de 25 % (borne haute de C-E2) | perte de valeur intégrée par allongement des délais | -31 531 | 171 | 31 360 | 92,8 | 2 |

Propriétés vérifiées par ces cas :

- Une friche imperméabilisée transformée en résidence avec jardin gagne de la nature : Cnat = -29 604 m²HE·an (cas 1).
- La construction d'une prairie riche fait perdre l'essentiel de sa valeur au site : Cnat relatif = 0,844 (cas 2).
- La même opération en réservoir perd davantage : 391 212 contre 340 184 m²HE·an, soit le rapport du multiplicateur de situation (cas 5).
- Les bureaux sur dalle atteignent le seuil de Bnat du tertiaire grâce à la dalle et à la toiture, mais pas celui de la pleine terre, nulle (cas 3).
- La réhabilitation gagne un peu de nature par la cour désimperméabilisée et le jardin amélioré (cas 4).
- La mare, les haies et le boisement créés sur une culture laissent une dette de maturité de 5 356 m²HE·an (cas 6).
- Bois et béton (cas 7) : Inat vaut 301 754 pour le béton, 1 867 574 pour le bois d'origine non justifiée et 1 200 908 pour le bois de coupe sélective justifiée.
- Zone méditerranéenne (cas 8) : sans différence en v1 ; avec des délais allongés de 25 %, Cnat passe de -32 862 à -31 531 m²HE·an.

### Lecture du cas 7

Avec les conventions de la v1, le bâtiment en bois a une biodiversité grise plusieurs fois plus forte que le même bâtiment en béton. Le climat est plus faible pour le bois, mais l'occupation des forêts, comptée en surface et en durée à la perte de MSA du régime d'exploitation, l'emporte largement. Le sens de l'écart est celui de la littérature citée par l'audit (Christiansson et Roos 2023 ; Carbone 4, 2026, pour qui une substitution par du bois de provenance non maîtrisée triple la pression de changement d'usage des sols) ; son ampleur dépend de trois conventions à soumettre au Biodiversity Standard Council : le rapport de 2 m³ de bois rond par m³ de produit (C-G4), le choix d'une approche attributionnelle qui compte toute la forêt de production comme une perte par rapport à la forêt naturelle (C-G5), et l'absence de prise en compte de l'occupation des usines et des carrières de ciment pour les autres matériaux (C-G7), qui avantage le béton. Ce cas est le premier à recalibrer.

### Cas complémentaires

Trente et un cas complémentaires déclinent une même opération type (part d'emprise bâtie, 15 % de voirie, jardins, prairie urbaine et haie sur le reste, toiture extensive sur la moitié de l'emprise, arbres plantés) sur cinq sites initiaux, trois tailles de parcelle, trois emprises, deux typologies, trois durées de chantier, trois situations, trois éclairages et quatre zones. Ils forment, avec les huit cas précédents, le jeu de référence du banc de validation du moteur (lot 4).

#### Synthèse des cas complémentaires

| Cas | V_0 | Cnat | Cnat relatif | Dette | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|---|---|
| Cas C01 | 108,7 | -85 | -0,016 | 434 | 63 753 | -63 668 | 62,5 | 1 |
| Cas C02 | 774,7 | 120 | 0,003 | 3 069 | 318 764 | -318 884 | 62,5 | 0 |
| Cas C03 | 4 203,8 | 651 | 0,003 | 16 651 | 1 275 058 | -1 275 709 | 62,5 | 0 |
| Cas C04 | 302 | 9 580 | 0,634 | 434 | 63 753 | -73 333 | 62,5 | 0 |
| Cas C05 | 2 151,8 | 68 976 | 0,641 | 3 069 | 318 764 | -387 741 | 62,5 | 0 |
| Cas C06 | 11 676,6 | 374 295 | 0,641 | 16 651 | 1 275 058 | -1 649 352 | 62,5 | 0 |
| Cas C07 | 123,2 | 636 | 0,103 | 434 | 63 753 | -64 389 | 62,5 | 0 |
| Cas C08 | 877,4 | 5 254 | 0,12 | 3 069 | 318 764 | -324 019 | 62,5 | 0 |
| Cas C09 | 4 761 | 28 512 | 0,12 | 16 651 | 1 275 058 | -1 303 569 | 62,5 | 0 |
| Cas C10 | 302 | 9 580 | 0,634 | 434 | 63 753 | -73 333 | 62,5 | 0 |
| Cas C11 | 2 151,8 | 68 976 | 0,641 | 3 069 | 318 764 | -387 741 | 62,5 | 0 |
| Cas C12 | 11 676,6 | 374 295 | 0,641 | 16 651 | 1 275 058 | -1 649 352 | 62,5 | 0 |
| Cas C13 | 0 | -5 522 | non défini | 434 | 63 753 | -58 231 | 62,5 | 2 |
| Cas C14 | 0 | -38 614 | non défini | 3 069 | 318 764 | -280 150 | 62,5 | 2 |
| Cas C15 | 0 | -209 536 | non défini | 16 651 | 1 275 058 | -1 065 521 | 62,5 | 2 |
| Cas C16 | 2 151,8 | 78 266 | 0,727 | 2 178 | 478 147 | -556 413 | 51,2 | 0 |
| Cas C17 | 2 151,8 | 86 474 | 0,804 | 1 369 | 637 529 | -724 003 | 40 | 0 |
| Cas C18 | 2 151,8 | 81 135 | 0,754 | 1 898 | 531 274 | -612 409 | 47,5 | 0 |
| Cas C19 | 877,4 | 4 421 | 0,101 | 2 235 | 318 764 | -323 185 | 62,5 | 0 |
| Cas C20 | 877,4 | 6 505 | 0,148 | 4 319 | 318 764 | -325 269 | 62,5 | 0 |
| Cas C21 | 2 367 | 76 201 | 0,644 | 3 365 | 318 764 | -394 965 | 62,5 | 0 |
| Cas C22 | 2 474,6 | 79 813 | 0,645 | 3 514 | 318 764 | -398 577 | 62,5 | 0 |
| Cas C23 | 774,7 | 1 387 | 0,036 | 2 973 | 318 764 | -320 151 | 62,5 | 0 |
| Cas C24 | 774,7 | 3 287 | 0,085 | 2 830 | 318 764 | -322 051 | 62,5 | 0 |
| Cas C25 | 774,7 | 120 | 0,003 | 3 069 | 318 764 | -318 884 | 62,5 | 0 |
| Cas C26 | 774,7 | 120 | 0,003 | 3 069 | 318 764 | -318 884 | 62,5 | 0 |
| Cas C27 | 774,7 | 120 | 0,003 | 3 069 | 318 764 | -318 884 | 62,5 | 0 |
| Cas C28 | 2 151,8 | 78 266 | 0,727 | 2 178 | 478 147 | -556 413 | 51,2 | 0 |
| Cas C29 | 2 151,8 | 86 474 | 0,804 | 1 369 | 637 529 | -724 003 | 40 | 0 |
| Cas C30 | 0 | -29 324 | non défini | 2 178 | 478 147 | -448 822 | 51,2 | 2 |
| Cas C31 | 0 | -21 117 | non défini | 1 369 | 637 529 | -616 412 | 40 | 2 |

Lecture :

- La taille de la parcelle change peu la consommation relative (C04 à C06 : 0,63 à 0,64) : l'effet de taille des taches touche l'état initial comme l'état projet.
- La prairie de fauche et la chênaie-charmaie de stade moyen donnent les mêmes résultats (C04 à C06 et C10 à C12) : leurs valeurs de biotope allemandes sont égales (20 sur 24) et leurs grilles d'état sont remplies de la même façon. La méthode ne distingue ici un boisement d'une prairie que par son stade.
- Plus l'emprise augmente, plus Cnat et Inat augmentent et plus Bnat baisse (C05, C16, C17).
- Un chantier plus long creuse la perte (C19, C08, C20 : 6, 18 et 36 mois).
- La situation en corridor ou en réservoir augmente la perte dans le rapport des multiplicateurs (C05, C21, C22).
- L'éclairage de la prairie créée réduit le gain (C02, C23, C24).
- La zone biogéographique ne change rien en v1 (C25 à C27, convention C-E2).
- Un parking revêtu transformé en résidence avec jardins gagne toujours de la nature (C13 à C15, C30, C31) ; sa valeur initiale nulle laisse Cnat relatif non défini et le niveau 2 se juge sur Cnat < 0.

### Cas C01. Culture intensive, 1 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 000 m² |
| Emprise du bâti | 300 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 660 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 13 m³ (coupe rase) |
| Granulats | 990 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 000 | 0 | satisfait |
| projet | 1 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 1 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,435 | 1 | 1 | 108,74 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 1 000 | 0,435 | 1 | 1 | 0,435 |

Valeur du site sans projet V_0 = 108,74 m²HE ; I_0 = 5 436,9 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 150 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 275 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 192 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 82 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 55 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 150 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 40,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 38,23 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,3813 | 1 | 1 | 18,35 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 10,92 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,35 | 1 | 1 | 11,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 550 | 0,3813 | 1 | 1 | 0,3813 |
| T | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 31,7 | 69,2 | 92,6 | 111,6 | 113,6 | 115,7 | 119,1 | 119,1 | 119,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 5 436,9 | m²HE·an |
| I_1 | 5 521,6 | m²HE·an |
| Cnat | -84,7 | m²HE·an |
| Cnat relatif | -0,016 |  |
| Cnat sur 30 ans | 122,7 | m²HE·an |
| Dette de maturité | 433,8 | m²HE·an |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -63 668,2 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 450 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 1.

### Cas C02. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 120 | m²HE·an |
| Cnat relatif | 0,003 |  |
| Cnat sur 30 ans | 1 299,4 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -318 884,4 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C03. Culture intensive, 20 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 20 000 m² |
| Emprise du bâti | 6 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 13 200 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 264 m³ (coupe rase) |
| Granulats | 19 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 20 000 | 0 | satisfait |
| projet | 20 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 20 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,8408 | 1 | 1 | 4 203,75 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 20 000 | 0,8408 | 1 | 1 | 0,8408 |

Valeur du site sans projet V_0 = 4 203,75 m²HE ; I_0 = 210 187,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 6 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 5 500 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 3 850 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 1 650 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 1 100 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 3 000 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 548,38 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 478,11 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,7371 | 1 | 1 | 709,53 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 422,32 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,5539 | 1 | 1 | 365,42 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 11 000 | 0,7371 | 1 | 1 | 0,7371 |
| T | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 183,5 | 2 593,5 | 3 499,9 | 4 234,4 | 4 312,6 | 4 390,8 | 4 523,7 | 4 523,7 | 4 523,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 210 187,6 | m²HE·an |
| I_1 | 209 536,5 | m²HE·an |
| Cnat | 651,1 | m²HE·an |
| Cnat relatif | 0,003 |  |
| Cnat sur 30 ans | 7 051,1 | m²HE·an |
| Dette de maturité | 16 651 | m²HE·an |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 275 708,9 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 9 000 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C04. Prairie de fauche en état moyen, 1 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 000 m² |
| Emprise du bâti | 300 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 660 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 13 m³ (coupe rase) |
| Granulats | 990 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 000 | 0 | satisfait |
| projet | 1 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 1 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,435 | 1 | 1 | 302,04 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 1 000 | 0,435 | 1 | 1 | 0,435 |

Valeur du site sans projet V_0 = 302,04 m²HE ; I_0 = 15 101,9 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 150 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 275 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 192 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 82 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 55 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 150 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 40,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 38,23 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,3813 | 1 | 1 | 18,35 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 10,92 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,35 | 1 | 1 | 11,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 550 | 0,3813 | 1 | 1 | 0,3813 |
| T | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 31,7 | 69,2 | 92,6 | 111,6 | 113,6 | 115,7 | 119,1 | 119,1 | 119,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 15 101,9 | m²HE·an |
| I_1 | 5 521,6 | m²HE·an |
| Cnat | 9 580,3 | m²HE·an |
| Cnat relatif | 0,634 |  |
| Cnat sur 30 ans | 5 921,7 | m²HE·an |
| Dette de maturité | 433,8 | m²HE·an |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -73 333,2 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 450 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C05. Prairie de fauche en état moyen, 5 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 68 976,4 | m²HE·an |
| Cnat relatif | 0,641 |  |
| Cnat sur 30 ans | 42 613,2 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -387 740,8 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C06. Prairie de fauche en état moyen, 20 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 20 000 m² |
| Emprise du bâti | 6 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 13 200 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 264 m³ (coupe rase) |
| Granulats | 19 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 20 000 | 0 | satisfait |
| projet | 20 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 20 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,8408 | 1 | 1 | 11 676,62 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 20 000 | 0,8408 | 1 | 1 | 0,8408 |

Valeur du site sans projet V_0 = 11 676,62 m²HE ; I_0 = 583 831 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 6 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 5 500 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 3 850 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 1 650 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 1 100 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 3 000 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 548,38 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 478,11 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,7371 | 1 | 1 | 709,53 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 422,32 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,5539 | 1 | 1 | 365,42 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 11 000 | 0,7371 | 1 | 1 | 0,7371 |
| T | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 183,5 | 2 593,5 | 3 499,9 | 4 234,4 | 4 312,6 | 4 390,8 | 4 523,7 | 4 523,7 | 4 523,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 583 831 | m²HE·an |
| I_1 | 209 536,5 | m²HE·an |
| Cnat | 374 294,5 | m²HE·an |
| Cnat relatif | 0,641 |  |
| Cnat sur 30 ans | 231 237,1 | m²HE·an |
| Dette de maturité | 16 651 | m²HE·an |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 649 352,3 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 9 000 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C07. Friche urbaine en mosaïque, 1 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 000 m² |
| Emprise du bâti | 300 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 660 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 13 m³ (coupe rase) |
| Granulats | 990 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 000 | 0 | satisfait |
| projet | 1 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.8 | sol pleine terre | 700 | S08 |
| I2 | VB.2 | sol pleine terre | 300 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,5 | 0,75 | 0,875 | 1 | 0,4021 | 1 | 1 | 123,15 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 700 | 0,4021 | 1 | 1 | 0,4021 |

Valeur du site sans projet V_0 = 123,15 m²HE ; I_0 = 6 157,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 150 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 275 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 192 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 82 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 55 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 150 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 40,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 38,23 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,3813 | 1 | 1 | 18,35 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 10,92 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,35 | 1 | 1 | 11,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 550 | 0,3813 | 1 | 1 | 0,3813 |
| T | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 31,7 | 69,2 | 92,6 | 111,6 | 113,6 | 115,7 | 119,1 | 119,1 | 119,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 6 157,6 | m²HE·an |
| I_1 | 5 521,6 | m²HE·an |
| Cnat | 636 | m²HE·an |
| Cnat relatif | 0,103 |  |
| Cnat sur 30 ans | 555,1 | m²HE·an |
| Dette de maturité | 433,8 | m²HE·an |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -64 388,9 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 150 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C08. Friche urbaine en mosaïque, 5 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.8 | sol pleine terre | 3 500 | S08 |
| I2 | VB.2 | sol pleine terre | 1 500 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,5 | 0,75 | 0,875 | 1 | 0,573 | 1 | 1 | 877,37 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 3 500 | 0,573 | 1 | 1 | 0,573 |

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 43 868,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 43 868,4 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 5 254,2 | m²HE·an |
| Cnat relatif | 0,12 |  |
| Cnat sur 30 ans | 4 379,9 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -324 018,7 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 750 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C09. Friche urbaine en mosaïque, 20 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 20 000 m² |
| Emprise du bâti | 6 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 13 200 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 264 m³ (coupe rase) |
| Granulats | 19 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 20 000 | 0 | satisfait |
| projet | 20 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.8 | sol pleine terre | 14 000 | S08 |
| I2 | VB.2 | sol pleine terre | 6 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,5 | 0,75 | 0,875 | 1 | 0,7773 | 1 | 1 | 4 760,96 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 14 000 | 0,7773 | 1 | 1 | 0,7773 |

Valeur du site sans projet V_0 = 4 760,96 m²HE ; I_0 = 238 048,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 6 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 5 500 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 3 850 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 1 650 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 1 100 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 3 000 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 548,38 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 478,11 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,7371 | 1 | 1 | 709,53 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 422,32 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,5539 | 1 | 1 | 365,42 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 11 000 | 0,7371 | 1 | 1 | 0,7371 |
| T | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 183,5 | 2 593,5 | 3 499,9 | 4 234,4 | 4 312,6 | 4 390,8 | 4 523,7 | 4 523,7 | 4 523,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 238 048,1 | m²HE·an |
| I_1 | 209 536,5 | m²HE·an |
| Cnat | 28 511,6 | m²HE·an |
| Cnat relatif | 0,12 |  |
| Cnat sur 30 ans | 23 767,4 | m²HE·an |
| Dette de maturité | 16 651 | m²HE·an |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 303 569,4 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 3 000 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C10. Chênaie-charmaie de stade moyen, 1 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 000 m² |
| Emprise du bâti | 300 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 660 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 13 m³ (coupe rase) |
| Granulats | 990 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 000 | 0 | satisfait |
| projet | 1 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | G1.A | sol pleine terre | 1 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,435 | 1 | 1 | 302,04 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 1 000 | 0,435 | 1 | 1 | 0,435 |

Valeur du site sans projet V_0 = 302,04 m²HE ; I_0 = 15 101,9 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 150 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 275 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 192 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 82 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 55 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 150 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 40,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 38,23 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,3813 | 1 | 1 | 18,35 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 10,92 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,35 | 1 | 1 | 11,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 550 | 0,3813 | 1 | 1 | 0,3813 |
| T | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 31,7 | 69,2 | 92,6 | 111,6 | 113,6 | 115,7 | 119,1 | 119,1 | 119,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 15 101,9 | m²HE·an |
| I_1 | 5 521,6 | m²HE·an |
| Cnat | 9 580,3 | m²HE·an |
| Cnat relatif | 0,634 |  |
| Cnat sur 30 ans | 5 921,7 | m²HE·an |
| Dette de maturité | 433,8 | m²HE·an |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -73 333,2 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 450 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C11. Chênaie-charmaie de stade moyen, 5 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | G1.A | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 68 976,4 | m²HE·an |
| Cnat relatif | 0,641 |  |
| Cnat sur 30 ans | 42 613,2 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -387 740,8 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C12. Chênaie-charmaie de stade moyen, 20 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 20 000 m² |
| Emprise du bâti | 6 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 13 200 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 264 m³ (coupe rase) |
| Granulats | 19 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 20 000 | 0 | satisfait |
| projet | 20 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | G1.A | sol pleine terre | 20 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,8408 | 1 | 1 | 11 676,62 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 20 000 | 0,8408 | 1 | 1 | 0,8408 |

Valeur du site sans projet V_0 = 11 676,62 m²HE ; I_0 = 583 831 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 6 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 5 500 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 3 850 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 1 650 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 1 100 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 3 000 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 548,38 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 478,11 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,7371 | 1 | 1 | 709,53 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 422,32 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,5539 | 1 | 1 | 365,42 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 11 000 | 0,7371 | 1 | 1 | 0,7371 |
| T | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 183,5 | 2 593,5 | 3 499,9 | 4 234,4 | 4 312,6 | 4 390,8 | 4 523,7 | 4 523,7 | 4 523,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 583 831 | m²HE·an |
| I_1 | 209 536,5 | m²HE·an |
| Cnat | 374 294,5 | m²HE·an |
| Cnat relatif | 0,641 |  |
| Cnat sur 30 ans | 231 237,1 | m²HE·an |
| Dette de maturité | 16 651 | m²HE·an |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 649 352,3 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 9 000 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C13. Parking entièrement revêtu, 1 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 1 000 m² |
| Emprise du bâti | 300 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 660 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 13 m³ (coupe rase) |
| Granulats | 990 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 1 000 | 0 | satisfait |
| projet | 1 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 1 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 0 m²HE ; I_0 = 0 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 150 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 275 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 192 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 82 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 55 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 150 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 40,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 38,23 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,3813 | 1 | 1 | 18,35 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,3813 | 1 | 1 | 10,92 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,35 | 1 | 1 | 11,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 550 | 0,3813 | 1 | 1 | 0,3813 |
| T | 150 | 0,35 | 1 | 1 | 0,35 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 31,7 | 69,2 | 92,6 | 111,6 | 113,6 | 115,7 | 119,1 | 119,1 | 119,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 5 521,6 | m²HE·an |
| Cnat | -5 521,6 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -3 139,4 | m²HE·an |
| Dette de maturité | 433,8 | m²HE·an |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -58 231,3 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | -550 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas C14. Parking entièrement revêtu, 5 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 5 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 0 m²HE ; I_0 = 0 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | -38 614,1 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -21 941,1 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -280 150,3 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | -2 750 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas C15. Parking entièrement revêtu, 20 000 m², emprise 30 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 20 000 m² |
| Emprise du bâti | 6 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 13 200 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 264 m³ (coupe rase) |
| Granulats | 19 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 20 000 | 0 | satisfait |
| projet | 20 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 20 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 0 m²HE ; I_0 = 0 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 6 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 5 500 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 3 850 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 1 650 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 1 100 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 3 000 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 548,38 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 1 478,11 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,7371 | 1 | 1 | 709,53 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,7371 | 1 | 1 | 422,32 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,5539 | 1 | 1 | 365,42 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 11 000 | 0,7371 | 1 | 1 | 0,7371 |
| T | 3 000 | 0,5539 | 1 | 1 | 0,5539 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 183,5 | 2 593,5 | 3 499,9 | 4 234,4 | 4 312,6 | 4 390,8 | 4 523,7 | 4 523,7 | 4 523,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 209 536,5 | m²HE·an |
| Cnat | -209 536,5 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -119 061,5 | m²HE·an |
| Dette de maturité | 16 651 | m²HE·an |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 065 521,3 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | -11 000 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas C16. Prairie de fauche en état moyen, 5 000 m², emprise 45 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 2 250 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 950 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 99 m³ (coupe rase) |
| Granulats | 7 425 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 250 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 000 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 700 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 200 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 125 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 193,48 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 184,7 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5066 | 1 | 1 | 88,66 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 52,77 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4464 | 1 | 1 | 110,43 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 000 | 0,5066 | 1 | 1 | 0,5066 |
| T | 1 125 | 0,4464 | 1 | 1 | 0,4464 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 180,3 | 388,9 | 502,1 | 593,9 | 603,7 | 613,4 | 630 | 630 | 630 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 29 324,4 | m²HE·an |
| Cnat | 78 266,1 | m²HE·an |
| Cnat relatif | 0,727 |  |
| Cnat sur 30 ans | 47 830,8 | m²HE·an |
| Dette de maturité | 2 177,8 | m²HE·an |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -556 412,8 | m²HE·an |
| Bnat | 51,2 | points |
| Pleine terre | 0,4 |  |
| Imperméabilisation nette | 3 000 | m² |

**Conformité (fiche A40)** : Bnat 51,2 pour un seuil de 35 : atteint ; pleine terre 40 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C17. Prairie de fauche en état moyen, 5 000 m², emprise 60 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 3 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 6 600 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 132 m³ (coupe rase) |
| Granulats | 9 900 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 625 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 438 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 188 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 125 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 500 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 109,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 104,1 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4568 | 1 | 1 | 49,97 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 29,74 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 156,87 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 250 | 0,4568 | 1 | 1 | 0,4568 |
| T | 1 500 | 0,4755 | 1 | 1 | 0,4755 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 148,9 | 313,8 | 377,6 | 429,3 | 434,8 | 440,4 | 449,7 | 449,7 | 449,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 21 116,6 | m²HE·an |
| Cnat | 86 473,9 | m²HE·an |
| Cnat relatif | 0,804 |  |
| Cnat sur 30 ans | 52 432,1 | m²HE·an |
| Dette de maturité | 1 369,4 | m²HE·an |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -724 002,8 | m²HE·an |
| Bnat | 40 | points |
| Pleine terre | 0,25 |  |
| Imperméabilisation nette | 3 750 | m² |

**Conformité (fiche A40)** : Bnat 40 pour un seuil de 25 : atteint ; pleine terre 25 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C18. Prairie de fauche en état moyen, 5 000 m², emprise 50 %, tertiaire, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 2 500 m² |
| Zone biogéographique | continentale |
| Typologie | tertiaire |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 5 500 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 110 m³ (coupe rase) |
| Granulats | 8 250 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 875 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 612 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 262 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 175 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 250 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4919 | 1 | 1 | 164,39 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4919 | 1 | 1 | 156,93 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4919 | 1 | 1 | 75,33 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4919 | 1 | 1 | 44,84 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 125,58 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 750 | 0,4919 | 1 | 1 | 0,4919 |
| T | 1 250 | 0,4568 | 1 | 1 | 0,4568 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 169 | 362,1 | 458,4 | 536,4 | 544,7 | 553 | 567,1 | 567,1 | 567,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 26 455,9 | m²HE·an |
| Cnat | 81 134,6 | m²HE·an |
| Cnat relatif | 0,754 |  |
| Cnat sur 30 ans | 49 440 | m²HE·an |
| Dette de maturité | 1 898 | m²HE·an |
| Inat climat | 320 516,6 | m²HE·an |
| Inat bois | 203 703,7 | m²HE·an |
| Inat carrières | 7 053,8 | m²HE·an |
| Inat | 531 274,1 | m²HE·an |
| Snat | -612 408,7 | m²HE·an |
| Bnat | 47,5 | points |
| Pleine terre | 0,35 |  |
| Imperméabilisation nette | 3 250 | m² |

**Conformité (fiche A40)** : Bnat 47,5 pour un seuil de 25 : atteint ; pleine terre 35 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C19. Friche urbaine en mosaïque, 5 000 m², emprise 30 %, logement, chantier 6 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.8 | sol pleine terre | 3 500 | S08 |
| I2 | VB.2 | sol pleine terre | 1 500 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,5 | 0,75 | 0,875 | 1 | 0,573 | 1 | 1 | 877,37 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 3 500 | 0,573 | 1 | 1 | 0,573 |

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 43 868,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 218,1 | 477,9 | 561,5 | 728,5 | 783,2 | 797,6 | 812 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 43 868,4 | m²HE·an |
| I_1 | 39 447,8 | m²HE·an |
| Cnat | 4 420,6 | m²HE·an |
| Cnat relatif | 0,101 |  |
| Cnat sur 30 ans | 3 546,3 | m²HE·an |
| Dette de maturité | 2 234,9 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -323 185 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 750 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C20. Friche urbaine en mosaïque, 5 000 m², emprise 30 %, logement, chantier 36 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 36 mois (d_ch = 3 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.8 | sol pleine terre | 3 500 | S08 |
| I2 | VB.2 | sol pleine terre | 1 500 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,5 | 0,75 | 0,875 | 1 | 0,573 | 1 | 1 | 877,37 |
| I2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 3 500 | 0,573 | 1 | 1 | 0,573 |

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 43 868,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 0 | 0 | 519,7 | 776 | 790,4 | 804,8 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 43 868,4 | m²HE·an |
| I_1 | 37 363,7 | m²HE·an |
| Cnat | 6 504,7 | m²HE·an |
| Cnat relatif | 0,148 |  |
| Cnat sur 30 ans | 5 630,4 | m²HE·an |
| Dette de maturité | 4 319 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -325 269,1 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 750 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C21. Prairie de fauche en état moyen, 5 000 m², emprise 30 %, logement, chantier 18 mois, corridor

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1,1 | 0,6197 | 1 | 1 | 2 366,99 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 366,99 m²HE ; I_0 = 118 349,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1,1 | 0,5434 | 1 | 1 | 313,88 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1,1 | 0,5434 | 1 | 1 | 299,63 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1,1 | 0,5434 | 1 | 1 | 143,83 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1,1 | 0,5434 | 1 | 1 | 85,61 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 236,5 | 519 | 702,7 | 851,6 | 867,5 | 883,3 | 910,3 | 910,3 | 910,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 118 349,6 | m²HE·an |
| I_1 | 42 149 | m²HE·an |
| Cnat | 76 200,6 | m²HE·an |
| Cnat relatif | 0,644 |  |
| Cnat sur 30 ans | 47 066,5 | m²HE·an |
| Dette de maturité | 3 365,3 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -394 965 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C22. Prairie de fauche en état moyen, 5 000 m², emprise 30 %, logement, chantier 18 mois, reservoir

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | E2.2 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1,15 | 0,6197 | 1 | 1 | 2 474,58 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 474,58 m²HE ; I_0 = 123 729,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1,15 | 0,5434 | 1 | 1 | 328,14 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1,15 | 0,5434 | 1 | 1 | 313,25 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1,15 | 0,5434 | 1 | 1 | 150,37 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1,15 | 0,5434 | 1 | 1 | 89,5 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 245,8 | 539,5 | 731,6 | 887,3 | 903,9 | 920,4 | 948,6 | 948,6 | 948,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 123 729,1 | m²HE·an |
| I_1 | 43 916,4 | m²HE·an |
| Cnat | 79 812,7 | m²HE·an |
| Cnat relatif | 0,645 |  |
| Cnat sur 30 ans | 49 293,1 | m²HE·an |
| Dette de maturité | 3 513,6 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -398 577,2 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C23. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois, éclairage L1

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 0,9 | 1 | 245,15 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 215,4 | 469,8 | 625,9 | 753,1 | 767,5 | 781,9 | 806,4 | 806,4 | 806,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 37 347,5 | m²HE·an |
| Cnat | 1 386,6 | m²HE·an |
| Cnat relatif | 0,036 |  |
| Cnat sur 30 ans | 2 021,2 | m²HE·an |
| Dette de maturité | 2 973,2 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -320 151,1 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C24. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois, éclairage L2

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 0,75 | 1 | 204,29 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 211,3 | 457,5 | 597,3 | 712,2 | 726,6 | 741,1 | 765,6 | 765,6 | 765,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 35 447,6 | m²HE·an |
| Cnat | 3 286,5 | m²HE·an |
| Cnat relatif | 0,085 |  |
| Cnat sur 30 ans | 3 104 | m²HE·an |
| Dette de maturité | 2 830,2 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -322 051 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C25. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois, zone atlantique

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | atlantique |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 120 | m²HE·an |
| Cnat relatif | 0,003 |  |
| Cnat sur 30 ans | 1 299,4 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -318 884,4 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C26. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois, zone mediterraneenne

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 120 | m²HE·an |
| Cnat relatif | 0,003 |  |
| Cnat sur 30 ans | 1 299,4 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -318 884,4 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C27. Culture intensive, 5 000 m², emprise 30 %, logement, chantier 18 mois, zone alpine

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 1 500 m² |
| Zone biogéographique | alpine |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 3 300 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 66 m³ (coupe rase) |
| Granulats | 4 950 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | I1.1 | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,25 |  | 1 | 1 | 0,6197 | 1 | 1 | 774,68 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| isolee_I1 | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 734,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 1 500 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 375 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 962 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 412 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 275 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 750 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 285,34 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 272,39 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 218,1 | 477,9 | 645 | 780,3 | 794,7 | 809,2 | 833,7 | 833,7 | 833,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 38 614,1 | m²HE·an |
| Cnat | 120 | m²HE·an |
| Cnat relatif | 0,003 |  |
| Cnat sur 30 ans | 1 299,4 | m²HE·an |
| Dette de maturité | 3 068,5 | m²HE·an |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -318 884,4 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 2 250 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C28. Chênaie-charmaie de stade moyen, 5 000 m², emprise 45 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 2 250 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 950 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 99 m³ (coupe rase) |
| Granulats | 7 425 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | G1.A | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 250 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 000 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 700 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 200 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 125 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 193,48 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 184,7 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5066 | 1 | 1 | 88,66 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 52,77 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4464 | 1 | 1 | 110,43 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 000 | 0,5066 | 1 | 1 | 0,5066 |
| T | 1 125 | 0,4464 | 1 | 1 | 0,4464 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 180,3 | 388,9 | 502,1 | 593,9 | 603,7 | 613,4 | 630 | 630 | 630 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 29 324,4 | m²HE·an |
| Cnat | 78 266,1 | m²HE·an |
| Cnat relatif | 0,727 |  |
| Cnat sur 30 ans | 47 830,8 | m²HE·an |
| Dette de maturité | 2 177,8 | m²HE·an |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -556 412,8 | m²HE·an |
| Bnat | 51,2 | points |
| Pleine terre | 0,4 |  |
| Imperméabilisation nette | 3 000 | m² |

**Conformité (fiche A40)** : Bnat 51,2 pour un seuil de 35 : atteint ; pleine terre 40 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C29. Chênaie-charmaie de stade moyen, 5 000 m², emprise 60 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 3 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 6 600 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 132 m³ (coupe rase) |
| Granulats | 9 900 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | G1.A | sol pleine terre | 5 000 | S08 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 1 | 1 | 0,8333 | 0,6667 | 0,8333 | 1 | 0,6197 | 1 | 1 | 2 151,81 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| I | 5 000 | 0,6197 | 1 | 1 | 0,6197 |

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 107 590,5 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 625 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 438 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 188 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 125 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 500 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 109,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 104,1 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4568 | 1 | 1 | 49,97 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 29,74 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 156,87 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 250 | 0,4568 | 1 | 1 | 0,4568 |
| T | 1 500 | 0,4755 | 1 | 1 | 0,4755 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 148,9 | 313,8 | 377,6 | 429,3 | 434,8 | 440,4 | 449,7 | 449,7 | 449,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 107 590,5 | m²HE·an |
| I_1 | 21 116,6 | m²HE·an |
| Cnat | 86 473,9 | m²HE·an |
| Cnat relatif | 0,804 |  |
| Cnat sur 30 ans | 52 432,1 | m²HE·an |
| Dette de maturité | 1 369,4 | m²HE·an |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -724 002,8 | m²HE·an |
| Bnat | 40 | points |
| Pleine terre | 0,25 |  |
| Imperméabilisation nette | 3 750 | m² |

**Conformité (fiche A40)** : Bnat 40 pour un seuil de 25 : atteint ; pleine terre 25 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas C30. Parking entièrement revêtu, 5 000 m², emprise 45 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 2 250 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 4 950 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 99 m³ (coupe rase) |
| Granulats | 7 425 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 5 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 0 m²HE ; I_0 = 0 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 2 250 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 1 000 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 700 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 300 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 200 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 125 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 193,48 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 184,7 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5066 | 1 | 1 | 88,66 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5066 | 1 | 1 | 52,77 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4464 | 1 | 1 | 110,43 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 000 | 0,5066 | 1 | 1 | 0,5066 |
| T | 1 125 | 0,4464 | 1 | 1 | 0,4464 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 180,3 | 388,9 | 502,1 | 593,9 | 603,7 | 613,4 | 630 | 630 | 630 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 29 324,4 | m²HE·an |
| Cnat | -29 324,4 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -16 723,5 | m²HE·an |
| Dette de maturité | 2 177,8 | m²HE·an |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -448 822,3 | m²HE·an |
| Bnat | 51,2 | points |
| Pleine terre | 0,4 |  |
| Imperméabilisation nette | -2 000 | m² |

**Conformité (fiche A40)** : Bnat 51,2 pour un seuil de 35 : atteint ; pleine terre 40 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas C31. Parking entièrement revêtu, 5 000 m², emprise 60 %, logement, chantier 18 mois

**Résultat attendu** : voir la synthèse des cas complémentaires.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 3 000 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Surface de référence | 6 600 m² |
| Émissions des composants et du chantier | A1-A5 : 480, B : 330, C : 50 |
| Bois | 132 m³ (coupe rase) |
| Granulats | 9 900 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 5 000 | 0 | satisfait |
| projet | 5 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| I1 | VB.2 | sol pleine terre | 5 000 | S01 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| I1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |

Taches de l'état initial (fiches A17 à A19) :

Aucune tache.

Valeur du site sans projet V_0 = 0 m²HE ; I_0 = 0 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| P1 | VB.1 | sol pleine terre | 3 000 | S01 | créée | 0 | 1 |
| P2 | VB.2 | sol pleine terre | 750 | S01 | créée | 0 | 1 |
| P3 | VB.7 | sol pleine terre | 625 | S08 | créée | 1 | 1 |
| P4 | VB.26 | sol pleine terre | 438 | S08 | créée | 5 | 1 |
| P5 | FA.3 | lineaire | 188 | S08 | créée | 5 | 1 |
| P6 | VB.18a | arbre | 125 |  | créée | 27 | 1 |
| P7 | VB.11 | hors sol toiture | 1 500 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| P3 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 109,05 |
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 104,1 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4568 | 1 | 1 | 49,97 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4568 | 1 | 1 | 29,74 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4755 | 1 | 1 | 156,87 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 1 250 | 0,4568 | 1 | 1 | 0,4568 |
| T | 1 500 | 0,4755 | 1 | 1 | 0,4755 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 148,9 | 313,8 | 377,6 | 429,3 | 434,8 | 440,4 | 449,7 | 449,7 | 449,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 21 116,6 | m²HE·an |
| Cnat | -21 116,6 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -12 122,2 | m²HE·an |
| Dette de maturité | 1 369,4 | m²HE·an |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -616 412,3 | m²HE·an |
| Bnat | 40 | points |
| Pleine terre | 0,25 |  |
| Imperméabilisation nette | -1 250 | m² |

**Conformité (fiche A40)** : Bnat 40 pour un seuil de 25 : atteint ; pleine terre 25 % pour un seuil de 15 % : atteint ; niveau du site : 2.
