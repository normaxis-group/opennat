## Partie 8. Cas de validation

Les huit situations types du cahier des charges (§ 7) sont calculées ci-dessous par le carnet de calcul de référence (`outils/carnet_reference.py`), qui applique les fiches algorithmes de la partie 3 sans Monte-Carlo et sans rien partager avec le futur moteur. Chaque cas donne ses hypothèses, toutes les grandeurs intermédiaires et les indicateurs : le moteur devra les retrouver à 0,1 % près (exigence E10). Les cas 7 et 8 se déclinent en variantes.

Le carnet a d'abord été contrôlé sur l'exemple de l'annexe C de la partie 1, qu'il retrouve à l'identique : V_0 = 270,39 ; I_0 = 13 277,1 ; I_1 = 10 059,9 ; Cnat = 3 217,2 ; dette de maturité 673,1 ; Inat = 141 842,9 ; Bnat = 59. Les grandeurs des modules dynamiques (bilan hydrique horaire, éclairage horaire, maturation, gestion, calendrier) sont données par unité dans chaque cas.

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
| Zone climatique, altitude | H2a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 32,81 m²HE ; I_0 = 1 623 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| I3 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 20 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 20 | 1 |
| P3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 20 | 1 |
| P4 | arbustif | 117 | 53,1 | 55,2 | 64,2 | 1 | 1 | 0,963 | 1 | 18 | 1 |
| P5 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 | 18 | 0,533 |
| P6 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 | 18 | 1 |
| P7 | humide pluie | 65 | 42 | 48,6 | 57,7 | 1 | 0,984 | 0,893 | 1 | 18 | 1 |
| P8 | arbustif | 117 | 53,1 | 55,2 | 64,2 | 1 | 1 | 0,963 | 1 | 18 | 0,75 |
| P9 | arbore | 130 | 67,1 | 68,4 | 76,7 | 1 | 1 | 0,963 | 1 | 18 | 1 |
| P10 | toiture extensive | 20 | 15,4 | 29,9 | 34,9 | 1 | 0,971 | 0,956 | 1 | 18 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 73,3 | 317,6 | 437,1 | 522,6 | 505,2 | 567,2 | 629,5 | 624,1 | 618,7 |
| V_0 x k_W, m²HE | 32,8 | 32,8 | 32,8 | 32,8 | 32,8 | 32,7 | 32,7 | 32,4 | 32,1 | 31,8 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 623 | m²HE·an |
| I_1 | 27 545 | m²HE·an |
| Cnat | -25 921,9 | m²HE·an |
| Cnat relatif | -15,971 |  |
| Cnat sur 30 ans | -14 087,4 | m²HE·an |
| Dette de maturité | 5 059,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 141 126,7 | m²HE·an |
| Inat bois | 74 074,1 | m²HE·an |
| Inat carrières | 2 736 | m²HE·an |
| Inat | 217 936,8 | m²HE·an |
| Snat | -192 014,8 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 8 058,26 m²HE ; I_0 = 394 899,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 24 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 24 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 26 | 1 |
| P4 | gazon | 98 | 12,5 | 18,6 | 27,2 | 1 | 0,995 | 0,952 | 1 | 26 | 1 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 24 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 145,7 | 145,7 | 831,3 | 1 299,9 | 1 295,5 | 1 291,2 | 1 286,8 | 1 274,2 | 1 259,2 | 1 244,1 |
| V_0 x k_W, m²HE | 8 058,3 | 8 058,3 | 8 058,3 | 8 051,9 | 8 020,2 | 7 988,4 | 7 956,7 | 7 873,5 | 7 777,3 | 7 681 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 394 899,3 | m²HE·an |
| I_1 | 61 090,3 | m²HE·an |
| Cnat | 333 809 | m²HE·an |
| Cnat relatif | 0,845 |  |
| Cnat sur 30 ans | 203 528,2 | m²HE·an |
| Dette de maturité | 2 781 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 355 075,5 | m²HE·an |
| Inat bois | 222 222,2 | m²HE·an |
| Inat carrières | 7 695 | m²HE·an |
| Inat | 584 992,7 | m²HE·an |
| Snat | -918 801,7 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 62,5 m²HE ; I_0 = 3 090,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| I2 | gazon | 98 | 12,5 | 18,6 | 27,2 | 1 | 0,995 | 0,952 | 1 |
| I3 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 22 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 22 | 1 |
| P3 | arbustif | 80 | 37,9 | 42,2 | 52,6 | 1 | 0,976 | 0,914 | 1 | 26 | 1 |
| P4 | gazon | 60 | 18 | 24,7 | 34,2 | 0,998 | 0,964 | 0,917 | 1 | 26 | 1 |
| P5 | prairie | 80 | 15,1 | 23,8 | 36 | 0,968 | 0,933 | 0,885 | 1 | 26 | 1 |
| P6 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 26 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 4 | 113,5 | 264,1 | 291,5 | 289,5 | 287,5 | 284,4 | 281,7 | 279 |
| V_0 x k_W, m²HE | 62,5 | 62,5 | 62,5 | 62,5 | 62,5 | 62,4 | 62,4 | 61,9 | 61 | 60,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 3 090,7 | m²HE·an |
| I_1 | 13 438,3 | m²HE·an |
| Cnat | -10 347,7 | m²HE·an |
| Cnat relatif | -3,348 |  |
| Cnat sur 30 ans | -5 936,9 | m²HE·an |
| Dette de maturité | 888,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 626 125,5 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 9 405 | m²HE·an |
| Inat | 635 530,5 | m²HE·an |
| Snat | -625 182,8 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 21,39 m²HE ; I_0 = 1 047,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| I3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 14 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 14 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 14 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 14 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 21,4 | 52 | 70,8 | 71,4 | 71,2 | 70,9 | 70,6 | 70 | 69,2 | 68,5 |
| V_0 x k_W, m²HE | 21,4 | 21,4 | 21,4 | 21,4 | 21,3 | 21,2 | 21,1 | 20,9 | 20,6 | 20,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 1 047,7 | m²HE·an |
| I_1 | 3 439,4 | m²HE·an |
| Cnat | -2 391,7 | m²HE·an |
| Cnat relatif | -2,283 |  |
| Cnat sur 30 ans | -1 419,9 | m²HE·an |
| Dette de maturité | 70,2 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 44 813,6 | m²HE·an |
| Inat bois | 16 666,7 | m²HE·an |
| Inat carrières | 256,5 | m²HE·an |
| Inat | 61 736,8 | m²HE·an |
| Snat | -59 345,1 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 9 267 m²HE ; I_0 = 454 134,2 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 24 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 24 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 26 | 1 |
| P4 | gazon | 98 | 12,5 | 18,6 | 27,2 | 1 | 0,995 | 0,952 | 1 | 26 | 1 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 24 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 167,6 | 167,6 | 956 | 1 494,9 | 1 489,9 | 1 484,8 | 1 479,8 | 1 465,4 | 1 448 | 1 430,7 |
| V_0 x k_W, m²HE | 9 267 | 9 267 | 9 267 | 9 259,7 | 9 223,2 | 9 186,7 | 9 150,2 | 9 054,5 | 8 943,9 | 8 833,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 454 134,2 | m²HE·an |
| I_1 | 70 253,8 | m²HE·an |
| Cnat | 383 880,4 | m²HE·an |
| Cnat relatif | 0,845 |  |
| Cnat sur 30 ans | 234 057,4 | m²HE·an |
| Dette de maturité | 3 198,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 355 075,5 | m²HE·an |
| Inat bois | 222 222,2 | m²HE·an |
| Inat carrières | 7 695 | m²HE·an |
| Inat | 584 992,7 | m²HE·an |
| Snat | -968 873,1 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 37 950,4 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 1 | 1 | 1 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 185,2 | 730,5 | 1 070 | 1 369,9 | 1 438,4 | 918,8 | 942,8 | 968,6 | 963,4 | 952,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,1 | 770,9 | 767,8 | 764,6 | 756,6 | 747,3 | 738 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 37 950,4 | m²HE·an |
| I_1 | 50 370 | m²HE·an |
| Cnat | -12 419,6 | m²HE·an |
| Cnat relatif | -0,327 |  |
| Cnat sur 30 ans | -8 103,6 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 12 248,6 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 316,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 108,8 | 248,2 | 250,2 | 249,2 | 248,2 | 247,2 | 244,6 | 241,6 | 238,6 |
| V_0 x k_W, m²HE | 435,1 | 435,1 | 435,1 | 434,8 | 433 | 431,3 | 429,5 | 425 | 419,8 | 414,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 316,7 | m²HE·an |
| I_1 | 11 873,9 | m²HE·an |
| Cnat | 9 442,9 | m²HE·an |
| Cnat relatif | 0,443 |  |
| Cnat sur 30 ans | 5 881,5 | m²HE·an |
| Dette de maturité | 394,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 256 594 | m²HE·an |
| Inat bois | 37 037 | m²HE·an |
| Inat carrières | 8 122,5 | m²HE·an |
| Inat | 301 753,5 | m²HE·an |
| Snat | -311 196,4 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 316,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 108,8 | 248,2 | 250,2 | 249,2 | 248,2 | 247,2 | 244,6 | 241,6 | 238,6 |
| V_0 x k_W, m²HE | 435,1 | 435,1 | 435,1 | 434,8 | 433 | 431,3 | 429,5 | 425 | 419,8 | 414,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 316,7 | m²HE·an |
| I_1 | 11 873,9 | m²HE·an |
| Cnat | 9 442,9 | m²HE·an |
| Cnat relatif | 0,443 |  |
| Cnat sur 30 ans | 5 881,5 | m²HE·an |
| Dette de maturité | 394,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 198 770 | m²HE·an |
| Inat bois | 1 666 666,7 | m²HE·an |
| Inat carrières | 2 137,5 | m²HE·an |
| Inat | 1 867 574,2 | m²HE·an |
| Snat | -1 877 017,1 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 435,14 m²HE ; I_0 = 21 316,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 108,8 | 248,2 | 250,2 | 249,2 | 248,2 | 247,2 | 244,6 | 241,6 | 238,6 |
| V_0 x k_W, m²HE | 435,1 | 435,1 | 435,1 | 434,8 | 433 | 431,3 | 429,5 | 425 | 419,8 | 414,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 21 316,7 | m²HE·an |
| I_1 | 11 873,9 | m²HE·an |
| Cnat | 9 442,9 | m²HE·an |
| Cnat relatif | 0,443 |  |
| Cnat sur 30 ans | 5 881,5 | m²HE·an |
| Dette de maturité | 394,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 198 770 | m²HE·an |
| Inat bois | 1 000 000 | m²HE·an |
| Inat carrières | 2 137,5 | m²HE·an |
| Inat | 1 200 907,5 | m²HE·an |
| Snat | -1 210 350,4 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 37 950,4 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 1 | 1 | 1 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 185,2 | 730,5 | 1 070 | 1 369,9 | 1 438,4 | 918,8 | 942,8 | 968,6 | 963,4 | 952,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,1 | 770,9 | 767,8 | 764,6 | 756,6 | 747,3 | 738 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 37 950,4 | m²HE·an |
| I_1 | 50 370 | m²HE·an |
| Cnat | -12 419,6 | m²HE·an |
| Cnat relatif | -0,327 |  |
| Cnat sur 30 ans | -8 103,6 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 12 248,6 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas 8b. Même aménagement en zone méditerranéenne

**Résultat attendu** : délais identiques (convention C-E2) ; bilan hydrique et tenue de la mare propres au climat méditerranéen.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 0,5 | 0,5 | 0,5 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 173,4 | 689,8 | 1 017,8 | 1 314,7 | 1 387,5 | 867,7 | 894 | 925,9 | 928,1 | 924,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 48 230,1 | m²HE·an |
| Cnat | -9 613,5 | m²HE·an |
| Cnat relatif | -0,249 |  |
| Cnat sur 30 ans | -6 442,4 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 9 442,5 | m²HE·an |
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
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 0,5 | 0,5 | 0,5 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 143 | 585,2 | 896,5 | 1 229,8 | 1 377,6 | 850,9 | 874,3 | 909,1 | 927 | 924,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 47 245,9 | m²HE·an |
| Cnat | -8 629,3 | m²HE·an |
| Cnat relatif | -0,223 |  |
| Cnat sur 30 ans | -5 550,2 | m²HE·an |
| Dette de maturité | 5 436,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 8 458,3 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Synthèse et propriétés vérifiées

| Cas | Attendu | Cnat | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|
| Cas 1. Friche urbaine imperméabilisée devenue résidence avec jardin | gain : Cnat négatif | -25 922 | 217 937 | -192 015 | 66,7 | 2 |
| Cas 2. Prairie naturelle en périphérie construite en logements | forte perte : Cnat positif et élevé | 333 809 | 584 993 | -918 802 | 50 | 0 |
| Cas 3. Bureaux sur dalle avec toiture végétalisée | Bnat porté par la dalle et la toiture ; Cnat négatif sur un site déjà imperméable | -10 348 | 635 531 | -625 183 | 46 | 2 |
| Cas 4. Réhabilitation sans emprise nouvelle | petit gain par la désimperméabilisation de la cour et l'amélioration du jardin | -2 392 | 61 737 | -59 345 | 32 | 2 |
| Cas 5. Projet en réservoir de biodiversité | perte plus forte que le cas 2, du fait du multiplicateur de situation | 383 880 | 584 993 | -968 873 | 50 | 0 |
| Cas 6. Mare et haies créées sur une culture intensive | gain à maturité, dette de maturité élevée | -12 420 | 171 | 12 249 | 92,8 | 2 |
| Cas 7a. Bâtiment en béton | Inat climat dominant | 9 443 | 301 754 | -311 196 | 46,7 | 0 |
| Cas 7b. Même bâtiment en bois, origine non justifiée | climat plus faible, occupation des forêts plus forte | 9 443 | 1 867 574 | -1 877 017 | 46,7 | 0 |
| Cas 7c. Même bâtiment en bois issu de coupe sélective justifiée | Inat le plus faible des trois | 9 443 | 1 200 908 | -1 210 350 | 46,7 | 0 |
| Cas 8a. Aménagement en zone continentale | référence | -12 420 | 171 | 12 249 | 92,8 | 2 |
| Cas 8b. Même aménagement en zone méditerranéenne | délais identiques (convention C-E2) ; bilan hydrique et tenue de la mare propres au climat méditerranéen | -9 614 | 171 | 9 443 | 92,8 | 2 |
| Cas 8c. Zone méditerranéenne, délais allongés de 25 % (borne haute de C-E2) | perte de valeur intégrée par allongement des délais | -8 629 | 171 | 8 458 | 92,8 | 2 |

Propriétés vérifiées par ces cas :

- Une friche imperméabilisée transformée en résidence avec jardin gagne de la nature : Cnat = -25 922 m²HE·an (cas 1).
- La construction d'une prairie riche fait perdre au site la plus grande part de sa valeur : Cnat relatif = 0,845 (cas 2).
- La même opération en réservoir perd davantage : 383 880 contre 333 809 m²HE·an, soit le rapport du multiplicateur de situation (cas 5).
- Les bureaux sur dalle atteignent le seuil de Bnat du tertiaire grâce à la dalle et à la toiture, mais pas celui de la pleine terre, nulle (cas 3).
- La réhabilitation gagne un peu de nature par la cour désimperméabilisée et le jardin amélioré (cas 4).
- La mare, les haies et le boisement créés sur une culture laissent une dette de maturité de 4 440 m²HE·an (cas 6).
- Bois et béton (cas 7) : Inat vaut 301 754 pour le béton, 1 867 574 pour le bois d'origine non justifiée et 1 200 908 pour le bois de coupe sélective justifiée.
- Zone méditerranéenne (cas 8) : les délais sont les mêmes (C-E2), mais la mare non raccordée s'assèche au printemps sous le climat de Marignane ; Cnat passe de -12 420 à -9 614 m²HE·an, et à -8 629 avec des délais allongés de 25 %.

### Lecture du cas 7

Avec les conventions de la v1, le bâtiment en bois a une biodiversité grise plusieurs fois plus forte que le même bâtiment en béton. Le climat est plus faible pour le bois, mais l'occupation des forêts, comptée en surface et en durée à la perte de MSA du régime d'exploitation, l'emporte largement. Le sens de l'écart est celui de la littérature citée par l'audit (Christiansson et Roos 2023 ; Carbone 4, 2026, pour qui une substitution par du bois de provenance non maîtrisée triple la pression de changement d'usage des sols) ; son ampleur dépend de trois conventions à soumettre au Biodiversity Standard Council : le rapport de 2 m³ de bois rond par m³ de produit (C-G4), le choix d'une approche attributionnelle qui compte toute la forêt de production comme une perte par rapport à la forêt naturelle (C-G5), et l'absence de prise en compte de l'occupation des usines et des carrières de ciment pour les autres matériaux (C-G7), qui avantage le béton. Ce cas est le premier à recalibrer.

### Contrôle du module G face à l'étude Carbone 4

Le banc de validation (lot 4) situe le module G face au bâtiment type de l'étude Carbone 4 (octobre 2026 : 50 logements, 3 000 m², structure béton, phases A1-A3, méthode IMPACT World+). Ramenés au m² de plancher et au périmètre commun (climat et usage des sols), OpenNAT donne 54 m²HE·an et Carbone 4 44 PDF.m².yr, soit un rapport de 1,0 à 1,5 selon l'empreinte carbone supposée, les deux métriques étant rapprochées à 1 pour 1 faute de conversion publiée. Deux écarts de structure subsistent : la pollution, la moitié du résultat de Carbone 4, n'est pas comptée dans Inat (point P19) ; le bois est pénalisé plusieurs fois plus fort, par les conventions C-G4, C-G5 et C-G7 déjà désignées ci-dessus. Le détail, les hypothèses et le calcul sont dans la note « Contrôle d'ordre de grandeur du module G face à l'étude Carbone 4 » (`documentation/controle_carbone4.md`, `python -m banc.carbone4`).

### Cas complémentaires

Trente et un cas complémentaires déclinent une même opération type (part d'emprise bâtie, 15 % de voirie, jardins, prairie urbaine et haie sur le reste, toiture extensive sur la moitié de l'emprise, arbres plantés) sur cinq sites initiaux, trois tailles de parcelle, trois emprises, deux typologies, trois durées de chantier, trois situations, trois éclairages et quatre zones. Ils forment, avec les huit cas précédents, le jeu de référence du banc de validation du moteur (lot 4).

#### Synthèse des cas complémentaires

| Cas | V_0 | Cnat | Cnat relatif | Dette | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|---|---|
| Cas C01 | 108,7 | 702 | 0,132 | 404 | 63 753 | -64 455 | 62,5 | 0 |
| Cas C02 | 774,7 | 5 723 | 0,151 | 2 857 | 318 764 | -324 487 | 62,5 | 0 |
| Cas C03 | 4 203,8 | 31 054 | 0,151 | 15 504 | 1 275 058 | -1 306 111 | 62,5 | 0 |
| Cas C04 | 302 | 10 171 | 0,687 | 404 | 63 753 | -73 924 | 62,5 | 0 |
| Cas C05 | 2 151,8 | 73 186 | 0,694 | 2 857 | 318 764 | -391 950 | 62,5 | 0 |
| Cas C06 | 11 676,6 | 397 137 | 0,694 | 15 504 | 1 275 058 | -1 672 195 | 62,5 | 0 |
| Cas C07 | 123,2 | 1 408 | 0,233 | 404 | 63 753 | -65 161 | 62,5 | 0 |
| Cas C08 | 877,4 | 10 753 | 0,25 | 2 857 | 318 764 | -329 517 | 62,5 | 0 |
| Cas C09 | 4 761 | 58 350 | 0,25 | 15 504 | 1 275 058 | -1 333 408 | 62,5 | 0 |
| Cas C10 | 302 | 10 298 | 0,69 | 404 | 63 753 | -74 050 | 62,5 | 0 |
| Cas C11 | 2 151,8 | 74 086 | 0,697 | 2 857 | 318 764 | -392 850 | 62,5 | 0 |
| Cas C12 | 11 676,6 | 402 019 | 0,697 | 15 504 | 1 275 058 | -1 677 077 | 62,5 | 0 |
| Cas C13 | 0 | -4 625 | non défini | 404 | 63 753 | -59 128 | 62,5 | 2 |
| Cas C14 | 0 | -32 228 | non défini | 2 857 | 318 764 | -286 537 | 62,5 | 2 |
| Cas C15 | 0 | -174 881 | non défini | 15 504 | 1 275 058 | -1 100 177 | 62,5 | 2 |
| Cas C16 | 2 151,8 | 80 424 | 0,763 | 2 039 | 478 147 | -558 571 | 51,2 | 0 |
| Cas C17 | 2 151,8 | 86 747 | 0,823 | 1 298 | 637 529 | -724 276 | 40 | 0 |
| Cas C18 | 2 151,8 | 82 644 | 0,784 | 1 783 | 531 274 | -613 918 | 47,5 | 0 |
| Cas C19 | 877,4 | 10 078 | 0,234 | 2 023 | 318 764 | -328 843 | 62,5 | 0 |
| Cas C20 | 877,4 | 12 122 | 0,282 | 4 385 | 318 764 | -330 887 | 62,5 | 0 |
| Cas C21 | 2 367 | 80 831 | 0,697 | 3 132 | 318 764 | -399 595 | 62,5 | 0 |
| Cas C22 | 2 474,6 | 84 653 | 0,698 | 3 270 | 318 764 | -403 417 | 62,5 | 0 |
| Cas C23 | 774,7 | 6 386 | 0,168 | 2 795 | 318 764 | -325 151 | 62,5 | 0 |
| Cas C24 | 774,7 | 7 699 | 0,203 | 2 673 | 318 764 | -326 463 | 62,5 | 0 |
| Cas C25 | 774,7 | 5 921 | 0,155 | 2 857 | 318 764 | -324 686 | 62,5 | 0 |
| Cas C26 | 774,7 | 5 976 | 0,155 | 2 857 | 318 764 | -324 740 | 62,5 | 0 |
| Cas C27 | 774,7 | 5 982 | 0,154 | 2 857 | 318 764 | -324 746 | 62,5 | 0 |
| Cas C28 | 2 151,8 | 81 324 | 0,765 | 2 039 | 478 147 | -559 471 | 51,2 | 0 |
| Cas C29 | 2 151,8 | 87 647 | 0,824 | 1 298 | 637 529 | -725 176 | 40 | 0 |
| Cas C30 | 0 | -24 989 | non défini | 2 039 | 478 147 | -453 157 | 51,2 | 2 |
| Cas C31 | 0 | -18 666 | non défini | 1 298 | 637 529 | -618 863 | 40 | 2 |

Lecture :

- La taille de la parcelle change peu la consommation relative (C04 à C06 : 0,63 à 0,64) : l'effet de taille des taches touche l'état initial comme l'état projet.
- La prairie de fauche et la chênaie-charmaie de stade moyen donnent les mêmes résultats (C04 à C06 et C10 à C12) : leurs valeurs de biotope allemandes sont égales (20 sur 24) et leurs grilles d'état sont remplies de la même façon. La méthode ne distingue ici un boisement d'une prairie que par son stade.
- Plus l'emprise augmente, plus Cnat et Inat augmentent et plus Bnat baisse (C05, C16, C17).
- Un chantier plus long creuse la perte (C19, C08, C20 : 6, 18 et 36 mois).
- La situation en corridor ou en réservoir augmente la perte dans le rapport des multiplicateurs (C05, C21, C22).
- L'éclairage de la prairie créée réduit le gain (C02, C23, C24).
- La zone biogéographique ne change pas les délais (C-E2) ; les écarts entre C02 et C25 à C27 viennent du climat de la station de référence (Trappes, Rennes, Marignane, Mâcon à 900 m) et restent faibles, le facteur hydrique ne comptant que l'écart au climat local.
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 108,74 m²HE ; I_0 = 5 326,9 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 28,3 | 77 | 100,9 | 110,5 | 91 | 93,3 | 95,1 | 94 | 92,9 |
| V_0 x k_W, m²HE | 108,7 | 108,7 | 108,7 | 108,6 | 108,2 | 107,8 | 107,3 | 106,2 | 104,9 | 103,6 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 5 326,9 | m²HE·an |
| I_1 | 4 625 | m²HE·an |
| Cnat | 701,9 | m²HE·an |
| Cnat relatif | 0,132 |  |
| Cnat sur 30 ans | 484,1 | m²HE·an |
| Dette de maturité | 404,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -64 454,8 | m²HE·an |
| Bnat | 62,5 | points |
| Pleine terre | 0,55 |  |
| Imperméabilisation nette | 450 | m² |

**Conformité (fiche A40)** : Bnat 62,5 pour un seuil de 45 : atteint ; pleine terre 55 % pour un seuil de 15 % : atteint ; niveau du site : 0.

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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 37 950,4 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,2 | 772,5 | 633,5 | 649,7 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,1 | 770,9 | 767,8 | 764,6 | 756,6 | 747,3 | 738 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 37 950,4 | m²HE·an |
| I_1 | 32 227,7 | m²HE·an |
| Cnat | 5 722,7 | m²HE·an |
| Cnat relatif | 0,151 |  |
| Cnat sur 30 ans | 3 872,9 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -324 487,1 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 4 203,75 m²HE ; I_0 = 205 934,7 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 059,9 | 2 897,4 | 3 821 | 4 192,2 | 3 437,6 | 3 525,4 | 3 593,9 | 3 552,8 | 3 511,7 |
| V_0 x k_W, m²HE | 4 203,8 | 4 203,8 | 4 203,8 | 4 200,3 | 4 183,3 | 4 166,3 | 4 149,2 | 4 105,4 | 4 055,1 | 4 004,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 205 934,7 | m²HE·an |
| I_1 | 174 881,1 | m²HE·an |
| Cnat | 31 053,6 | m²HE·an |
| Cnat relatif | 0,151 |  |
| Cnat sur 30 ans | 21 015,7 | m²HE·an |
| Dette de maturité | 15 503,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 306 111,4 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 302,04 m²HE ; I_0 = 14 796,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 28,3 | 77 | 100,9 | 110,5 | 91 | 93,3 | 95,1 | 94 | 92,9 |
| V_0 x k_W, m²HE | 302 | 302 | 302 | 301,8 | 300,6 | 299,3 | 298,1 | 295 | 291,4 | 287,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 14 796,3 | m²HE·an |
| I_1 | 4 625 | m²HE·an |
| Cnat | 10 171,3 | m²HE·an |
| Cnat relatif | 0,687 |  |
| Cnat sur 30 ans | 6 226,5 | m²HE·an |
| Dette de maturité | 404,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -73 924,2 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 105 413,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,2 | 772,5 | 633,5 | 649,7 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 150,1 | 2 141,3 | 2 132,6 | 2 123,9 | 2 101,5 | 2 075,7 | 2 050 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 105 413,6 | m²HE·an |
| I_1 | 32 227,7 | m²HE·an |
| Cnat | 73 185,8 | m²HE·an |
| Cnat relatif | 0,694 |  |
| Cnat sur 30 ans | 44 783,7 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -391 950,3 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 11 676,62 m²HE ; I_0 = 572 018 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 059,9 | 2 897,4 | 3 821 | 4 192,2 | 3 437,6 | 3 525,4 | 3 593,9 | 3 552,8 | 3 511,7 |
| V_0 x k_W, m²HE | 11 676,6 | 11 676,6 | 11 676,6 | 11 667,2 | 11 619,8 | 11 572,5 | 11 525,2 | 11 403,5 | 11 263,8 | 11 124,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 572 018 | m²HE·an |
| I_1 | 174 881,1 | m²HE·an |
| Cnat | 397 136,9 | m²HE·an |
| Cnat relatif | 0,694 |  |
| Cnat sur 30 ans | 243 014,8 | m²HE·an |
| Dette de maturité | 15 503,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 672 194,7 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 123,15 m²HE ; I_0 = 6 033 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 28,3 | 77 | 100,9 | 110,5 | 91 | 93,3 | 95,1 | 94 | 92,9 |
| V_0 x k_W, m²HE | 123,2 | 123,2 | 123,2 | 123,1 | 122,6 | 122,1 | 121,6 | 120,3 | 118,8 | 117,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 6 033 | m²HE·an |
| I_1 | 4 625 | m²HE·an |
| Cnat | 1 408 | m²HE·an |
| Cnat relatif | 0,233 |  |
| Cnat sur 30 ans | 912,3 | m²HE·an |
| Dette de maturité | 404,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -65 160,9 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 42 980,8 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,2 | 772,5 | 633,5 | 649,7 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 877,4 | 877,4 | 877,4 | 876,7 | 873,1 | 869,5 | 866 | 856,8 | 846,3 | 835,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 42 980,8 | m²HE·an |
| I_1 | 32 227,7 | m²HE·an |
| Cnat | 10 753 | m²HE·an |
| Cnat relatif | 0,25 |  |
| Cnat sur 30 ans | 6 923,3 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -329 517,5 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 4 760,96 m²HE ; I_0 = 233 231,5 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 059,9 | 2 897,4 | 3 821 | 4 192,2 | 3 437,6 | 3 525,4 | 3 593,9 | 3 552,8 | 3 511,7 |
| V_0 x k_W, m²HE | 4 761 | 4 761 | 4 761 | 4 757,1 | 4 737,8 | 4 718,5 | 4 699,2 | 4 649,6 | 4 592,6 | 4 535,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 233 231,5 | m²HE·an |
| I_1 | 174 881,1 | m²HE·an |
| Cnat | 58 350,4 | m²HE·an |
| Cnat relatif | 0,25 |  |
| Cnat sur 30 ans | 37 568,9 | m²HE·an |
| Dette de maturité | 15 503,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 333 408,2 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 302,04 m²HE ; I_0 = 14 922,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 28,3 | 77 | 100,9 | 110,5 | 91 | 93,3 | 95,1 | 94 | 92,9 |
| V_0 x k_W, m²HE | 302 | 302 | 302 | 302 | 302 | 302 | 302 | 299 | 293,9 | 288,8 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 14 922,6 | m²HE·an |
| I_1 | 4 625 | m²HE·an |
| Cnat | 10 297,6 | m²HE·an |
| Cnat relatif | 0,69 |  |
| Cnat sur 30 ans | 6 304,2 | m²HE·an |
| Dette de maturité | 404,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -74 050,5 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 106 313,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,2 | 772,5 | 633,5 | 649,7 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 130 | 2 093,6 | 2 057,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 106 313,3 | m²HE·an |
| I_1 | 32 227,7 | m²HE·an |
| Cnat | 74 085,6 | m²HE·an |
| Cnat relatif | 0,697 |  |
| Cnat sur 30 ans | 45 337 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -392 850 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 11 676,62 m²HE ; I_0 = 576 900,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 059,9 | 2 897,4 | 3 821 | 4 192,2 | 3 437,6 | 3 525,4 | 3 593,9 | 3 552,8 | 3 511,7 |
| V_0 x k_W, m²HE | 11 676,6 | 11 676,6 | 11 676,6 | 11 676,6 | 11 676,6 | 11 676,6 | 11 676,6 | 11 558,1 | 11 360,7 | 11 163,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 576 900,3 | m²HE·an |
| I_1 | 174 881,1 | m²HE·an |
| Cnat | 402 019,2 | m²HE·an |
| Cnat relatif | 0,697 |  |
| Cnat sur 30 ans | 246 017,3 | m²HE·an |
| Dette de maturité | 15 503,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 677 077 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 28,3 | 77 | 100,9 | 110,5 | 91 | 93,3 | 95,1 | 94 | 92,9 |
| V_0 x k_W, m²HE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 4 625 | m²HE·an |
| Cnat | -4 625 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -2 746,2 | m²HE·an |
| Dette de maturité | 404,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 38 462 | m²HE·an |
| Inat bois | 24 444,4 | m²HE·an |
| Inat carrières | 846,4 | m²HE·an |
| Inat | 63 752,9 | m²HE·an |
| Snat | -59 127,9 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,2 | 772,5 | 633,5 | 649,7 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 32 227,7 | m²HE·an |
| Cnat | -32 227,7 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -19 140,9 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -286 536,7 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 1 059,9 | 2 897,4 | 3 821 | 4 192,2 | 3 437,6 | 3 525,4 | 3 593,9 | 3 552,8 | 3 511,7 |
| V_0 x k_W, m²HE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 174 881,1 | m²HE·an |
| Cnat | -174 881,1 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -103 866,6 | m²HE·an |
| Dette de maturité | 15 503,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 769 239,9 | m²HE·an |
| Inat bois | 488 888,9 | m²HE·an |
| Inat carrières | 16 929 | m²HE·an |
| Inat | 1 275 057,8 | m²HE·an |
| Snat | -1 100 176,7 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 105 413,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 160,6 | 426,2 | 542,2 | 588,6 | 494,3 | 505,3 | 513,9 | 508,7 | 503,6 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 150,1 | 2 141,3 | 2 132,6 | 2 123,9 | 2 101,5 | 2 075,7 | 2 050 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 105 413,6 | m²HE·an |
| I_1 | 24 989,2 | m²HE·an |
| Cnat | 80 424,4 | m²HE·an |
| Cnat relatif | 0,763 |  |
| Cnat sur 30 ans | 49 104,6 | m²HE·an |
| Dette de maturité | 2 039,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -558 571,1 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 105 413,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 131,6 | 334 | 400,2 | 426,4 | 373,2 | 379,4 | 384,2 | 381,3 | 378,4 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 150,1 | 2 141,3 | 2 132,6 | 2 123,9 | 2 101,5 | 2 075,7 | 2 050 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 105 413,6 | m²HE·an |
| I_1 | 18 666,3 | m²HE·an |
| Cnat | 86 747,3 | m²HE·an |
| Cnat relatif | 0,823 |  |
| Cnat sur 30 ans | 52 882,2 | m²HE·an |
| Dette de maturité | 1 298,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -724 276,2 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 105 413,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 150,2 | 393,6 | 492,5 | 531,9 | 451,8 | 461,1 | 468,4 | 464 | 459,6 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 150,1 | 2 141,3 | 2 132,6 | 2 123,9 | 2 101,5 | 2 075,7 | 2 050 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 105 413,6 | m²HE·an |
| I_1 | 22 770 | m²HE·an |
| Cnat | 82 643,5 | m²HE·an |
| Cnat relatif | 0,784 |  |
| Cnat sur 30 ans | 50 430 | m²HE·an |
| Dette de maturité | 1 782,7 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 320 516,6 | m²HE·an |
| Inat bois | 203 703,7 | m²HE·an |
| Inat carrières | 7 053,8 | m²HE·an |
| Inat | 531 274,1 | m²HE·an |
| Snat | -613 917,6 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 42 980,8 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 4 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 4 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 4 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 4 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 4 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 195,3 | 533,9 | 640,5 | 742,6 | 777 | 637,5 | 652,6 | 662,3 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 877,4 | 877,4 | 877,4 | 876,7 | 873,1 | 869,5 | 866 | 856,8 | 846,3 | 835,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 42 980,8 | m²HE·an |
| I_1 | 32 902,3 | m²HE·an |
| Cnat | 10 078,4 | m²HE·an |
| Cnat relatif | 0,234 |  |
| Cnat sur 30 ans | 6 248,7 | m²HE·an |
| Dette de maturité | 2 023,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -328 842,9 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 877,37 m²HE ; I_0 = 42 980,8 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| I2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 36 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 36 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 38 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 38 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 38 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 38 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 38 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 0 | 0 | 556,8 | 765 | 625,7 | 643,8 | 661,4 | 654,7 | 647,1 |
| V_0 x k_W, m²HE | 877,4 | 877,4 | 877,4 | 876,7 | 873,1 | 869,5 | 866 | 856,8 | 846,3 | 835,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 42 980,8 | m²HE·an |
| I_1 | 30 858,6 | m²HE·an |
| Cnat | 12 122,2 | m²HE·an |
| Cnat relatif | 0,282 |  |
| Cnat sur 30 ans | 8 292,5 | m²HE·an |
| Dette de maturité | 4 385,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -330 886,6 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 366,99 m²HE ; I_0 = 115 954,9 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 211,9 | 580,7 | 767,8 | 843,1 | 690,1 | 707,9 | 721,8 | 713,5 | 705,1 |
| V_0 x k_W, m²HE | 2 367 | 2 367 | 2 367 | 2 365,1 | 2 355,5 | 2 345,9 | 2 336,3 | 2 311,6 | 2 283,3 | 2 255 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 115 954,9 | m²HE·an |
| I_1 | 35 124,4 | m²HE·an |
| Cnat | 80 830,5 | m²HE·an |
| Cnat relatif | 0,697 |  |
| Cnat sur 30 ans | 49 453,4 | m²HE·an |
| Dette de maturité | 3 132,2 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -399 595 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 474,58 m²HE ; I_0 = 121 225,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 220,2 | 604 | 799,7 | 878,3 | 718,4 | 737 | 751,5 | 742,8 | 734,1 |
| V_0 x k_W, m²HE | 2 474,6 | 2 474,6 | 2 474,6 | 2 472,6 | 2 462,5 | 2 452,5 | 2 442,5 | 2 416,7 | 2 387,1 | 2 357,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 121 225,6 | m²HE·an |
| I_1 | 36 572,7 | m²HE·an |
| Cnat | 84 652,9 | m²HE·an |
| Cnat relatif | 0,698 |  |
| Cnat sur 30 ans | 51 788,3 | m²HE·an |
| Dette de maturité | 3 269,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -403 417,3 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 37 950,4 m²HE·an.

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
| P4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 0,916 | 1 | 249,52 |
| P5 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,5434 | 1 | 1 | 130,75 |
| P6 |  | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,5434 | 1 | 1 | 77,83 |
| P7 | 0,5 | 1 | 0,2639 | 0,6667 | 0,8333 | 1 | 0,4083 | 1 | 1 | 67,34 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| J | 2 750 | 0,5434 | 1 | 1 | 0,5434 |
| T | 750 | 0,4083 | 1 | 1 | 0,4083 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 192,2 | 521,7 | 683,7 | 749,8 | 621,4 | 637,6 | 650,4 | 643 | 635,5 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,1 | 770,9 | 767,8 | 764,6 | 756,6 | 747,3 | 738 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 37 950,4 | m²HE·an |
| I_1 | 31 564,1 | m²HE·an |
| Cnat | 6 386,3 | m²HE·an |
| Cnat relatif | 0,168 |  |
| Cnat sur 30 ans | 4 301,3 | m²HE·an |
| Dette de maturité | 2 795,4 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -325 150,8 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 37 950,4 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,75 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 185,9 | 497,5 | 643,1 | 704,8 | 597,5 | 613,8 | 626,8 | 619,7 | 612,5 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,1 | 770,9 | 767,8 | 764,6 | 756,6 | 747,3 | 738 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 37 950,4 | m²HE·an |
| I_1 | 30 251,9 | m²HE·an |
| Cnat | 7 698,5 | m²HE·an |
| Cnat relatif | 0,203 |  |
| Cnat sur 30 ans | 5 148,5 | m²HE·an |
| Dette de maturité | 2 673,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -326 463 | m²HE·an |
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
| Zone climatique, altitude | H2a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 318,5 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 | 16 | 1 |
| P4 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 53,1 | 55,2 | 64,2 | 1 | 1 | 0,963 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 67,1 | 68,4 | 76,7 | 1 | 1 | 0,963 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 15,4 | 29,9 | 34,9 | 1 | 0,971 | 0,956 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,3 | 773,8 | 635 | 651,9 | 666,2 | 660,5 | 654,7 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,5 | 773,5 | 772,5 | 771,5 | 766,1 | 758,4 | 750,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 318,5 | m²HE·an |
| I_1 | 32 397,3 | m²HE·an |
| Cnat | 5 921,2 | m²HE·an |
| Cnat relatif | 0,155 |  |
| Cnat sur 30 ans | 3 964,4 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -324 685,6 | m²HE·an |
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
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 16 | 1 |
| P4 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 99,3 | 101,4 | 120,9 | 1 | 1 | 0,95 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,6 | 775,3 | 637,3 | 655,3 | 671,9 | 668,8 | 665,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 32 641 | m²HE·an |
| Cnat | 5 975,6 | m²HE·an |
| Cnat relatif | 0,155 |  |
| Cnat sur 30 ans | 3 964,4 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -324 740 | m²HE·an |
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
| Zone climatique, altitude | H1c, 900 m |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 13,4 | 5,9 | 6 | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 13,4 | 5,9 | 6 | 1 | 1 | 1 | 1 | 16 | 1 |
| P4 | prairie | 130 | 13,4 | 5,9 | 6 | 1 | 1 | 1 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 32,4 | 29,7 | 28,6 | 1 | 1 | 1 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 42 | 40,7 | 40,4 | 1 | 1 | 1 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 26,7 | 19,3 | 16 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 195,3 | 533,9 | 704,6 | 775,3 | 637,3 | 655,3 | 673,8 | 673,8 | 673,8 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 734,1 | m²HE·an |
| I_1 | 32 752,2 | m²HE·an |
| Cnat | 5 981,9 | m²HE·an |
| Cnat relatif | 0,154 |  |
| Cnat sur 30 ans | 3 964,8 | m²HE·an |
| Dette de maturité | 2 857,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 192 310 | m²HE·an |
| Inat bois | 122 222,2 | m²HE·an |
| Inat carrières | 4 232,2 | m²HE·an |
| Inat | 318 764,4 | m²HE·an |
| Snat | -324 746,3 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 106 313,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 160,6 | 426,2 | 542,2 | 588,6 | 494,3 | 505,3 | 513,9 | 508,7 | 503,6 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 130 | 2 093,6 | 2 057,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 106 313,3 | m²HE·an |
| I_1 | 24 989,2 | m²HE·an |
| Cnat | 81 324,1 | m²HE·an |
| Cnat relatif | 0,765 |  |
| Cnat sur 30 ans | 49 657,9 | m²HE·an |
| Dette de maturité | 2 039,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -559 470,8 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 2 151,81 m²HE ; I_0 = 106 313,3 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 131,6 | 334 | 400,2 | 426,4 | 373,2 | 379,4 | 384,2 | 381,3 | 378,4 |
| V_0 x k_W, m²HE | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 151,8 | 2 130 | 2 093,6 | 2 057,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 106 313,3 | m²HE·an |
| I_1 | 18 666,3 | m²HE·an |
| Cnat | 87 647 | m²HE·an |
| Cnat relatif | 0,824 |  |
| Cnat sur 30 ans | 53 435,5 | m²HE·an |
| Dette de maturité | 1 298,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -725 175,9 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 160,6 | 426,2 | 542,2 | 588,6 | 494,3 | 505,3 | 513,9 | 508,7 | 503,6 |
| V_0 x k_W, m²HE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 24 989,2 | m²HE·an |
| Cnat | -24 989,2 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -14 820 | m²HE·an |
| Dette de maturité | 2 039,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 288 465 | m²HE·an |
| Inat bois | 183 333,3 | m²HE·an |
| Inat carrières | 6 348,4 | m²HE·an |
| Inat | 478 146,7 | m²HE·an |
| Snat | -453 157,5 | m²HE·an |
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
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| P3 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| P4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 0,533 |
| P5 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| P6 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| P7 | toiture extensive | 20 | 14,9 | 14,9 | 19,7 | 1 | 1 | 1 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 131,6 | 334 | 400,2 | 426,4 | 373,2 | 379,4 | 384,2 | 381,3 | 378,4 |
| V_0 x k_W, m²HE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 0 | m²HE·an |
| I_1 | 18 666,3 | m²HE·an |
| Cnat | -18 666,3 | m²HE·an |
| Cnat relatif | non défini |  |
| Cnat sur 30 ans | -11 042,4 | m²HE·an |
| Dette de maturité | 1 298,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 384 619,9 | m²HE·an |
| Inat bois | 244 444,4 | m²HE·an |
| Inat carrières | 8 464,5 | m²HE·an |
| Inat | 637 528,9 | m²HE·an |
| Snat | -618 862,6 | m²HE·an |
| Bnat | 40 | points |
| Pleine terre | 0,25 |  |
| Imperméabilisation nette | -1 250 | m² |

**Conformité (fiche A40)** : Bnat 40 pour un seuil de 25 : atteint ; pleine terre 25 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas dynamiques

Vingt-neuf cas reprennent l'exemple de l'annexe C (et le cas 6 pour la mare) en ne changeant qu'une donnée des modules dynamiques : calendrier du chantier, substrat de la toiture, sol, arrosage, zone climatique, éclairage, plan de gestion, année de début, raccordement et fond de la mare, abattage d'arbres à gîtes. L'écart se lit par rapport à l'exemple de l'annexe C (Cnat = 3 217,2) ou au cas 6 en zone H3 pour D25 à D27 (Cnat du cas 6 en zone H1a : -12 419,6).

#### Synthèse des cas dynamiques

| Cas | Donnée changée | I_1 | Cnat | Écart | ΔI_ch | Arrosage (m³/an) |
|---|---|---|---|---|---|---|
| Cas D01 | Chantier commencé en mai : défrichement pendant la nidification | 10 023 | 3 497 | 280 | 243,6 | 0 |
| Cas D02 | Chantier commencé en janvier : plantations reportées à novembre de l'année suivante | 9 950 | 3 327 | 110 | 0 | 0 |
| Cas D03 | Toiture extensive de 8 cm au lieu de 15 cm | 9 762 | 3 515 | 298 | 0 | 0 |
| Cas D04 | Toiture semi-intensive de 30 cm | 10 153 | 3 124 | -93 | 0 | 0 |
| Cas D05 | Toiture intensive de 50 cm (gazon et massifs, type VB.13) | 9 603 | 3 674 | 457 | 0 | 0 |
| Cas D06 | Prairie urbaine arrosée | 10 110 | 3 167 | -50 | 0 | 34,3 |
| Cas D07 | Sol sableux | 9 756 | 2 926 | -291 | 0 | 0 |
| Cas D08 | Sol argileux | 10 098 | 3 256 | 39 | 0 | 0 |
| Cas D09 | Sol limoneux de 40 cm sur dalle rocheuse | 9 608 | 2 795 | -422 | 0 | 0 |
| Cas D10 | Zone climatique H1b (Nancy) | 10 226 | 3 233 | 16 | 0 | 0 |
| Cas D11 | Zone climatique H1c (Mâcon) | 10 329 | 3 190 | -27 | 0 | 0 |
| Cas D12 | Zone climatique H2a (Rennes) | 10 198 | 3 193 | -24 | 0 | 0 |
| Cas D13 | Zone climatique H2b (Tours) | 10 246 | 3 183 | -34 | 0 | 0 |
| Cas D14 | Zone climatique H2c (Agen) | 10 248 | 3 246 | 29 | 0 | 0 |
| Cas D15 | Zone climatique H2d (Carpentras) | 10 235 | 3 284 | 67 | 0 | 0 |
| Cas D16 | Zone climatique H3 (Marignane) | 10 189 | 3 290 | 73 | 0 | 0 |
| Cas D17 | Prairie éclairée toute la nuit en 4 000 K | 9 586 | 3 691 | 474 | 0 | 0 |
| Cas D18 | Prairie éclairée jusqu'à 23 h en 2 700 K, luminaires à 20 m | 10 225 | 3 052 | -165 | 0 | 0 |
| Cas D19 | Prairie éclairée toute la nuit en ambre avec détection de présence (30 % du temps) | 10 193 | 3 085 | -133 | 0 | 0 |
| Cas D20 | Sans plan de gestion écologique | 9 633 | 3 644 | 426 | 0 | 0 |
| Cas D21 | Plan de gestion de trente ans | 10 985 | 2 292 | -926 | 0 | 0 |
| Cas D22 | Plan de gestion couvrant les cinquante ans | 11 801 | 1 476 | -1 741 | 0 | 0 |
| Cas D23 | Abandon de l'entretien à la fin du plan de dix ans | 11 044 | 2 233 | -984 | 0 | 0 |
| Cas D24 | Chantier commencé en 2045 | 9 879 | 3 141 | -77 | 0 | 0 |
| Cas D25 | Cas 6 en zone H3, mare sans bassin versant | 48 230 | -9 614 | 2 806 | 0 | 0 |
| Cas D26 | Cas 6 en zone H3, mare raccordée à 3 000 m² de prairie | 50 575 | -11 959 | 461 | 0 | 0 |
| Cas D27 | Cas 6 en zone H3, mare à fond étanche raccordée à 3 000 m² de prairie | 50 969 | -12 352 | 68 | 0 | 0 |
| Cas D28 | Arbres âgés à gîtes abattus en janvier | 9 588 | 3 986 | 769 | 32,2 | 0 |
| Cas D29 | Arbres âgés à gîtes abattus en octobre | 9 711 | 3 832 | 614 | 0 | 0 |

Lecture :

- Calendrier : un défrichement en mai ajoute 243,6 m²HE·an pour la nidification ; un début en janvier reporte les plantations à novembre et coûte 110 m²HE·an ; l'abattage d'arbres âgés à gîtes en janvier ajoute 32,2 m²HE·an que l'abattage en octobre évite.
- Substrat : la toiture de 8 cm coûte 298 m²HE·an, celle de 30 cm en rend 93.
- Sol : sur un sable, Cnat baisse de 291 m²HE·an. L'état initial, sur le même sol, perd lui aussi, et davantage : la friche herbacée initiale est plus étendue que les milieux créés. Le sol pauvre pénalise le projet dans l'absolu (I_1 plus faible), pas face à l'état initial.
- Éclairage : la prairie éclairée toute la nuit en 4 000 K coûte 474 m²HE·an ; éteinte à 23 h, en 2 700 K, à 20 m, elle en rend 165.
- Gestion : sans plan, Cnat monte de 426 ; un plan de trente ans le baisse de 926, un plan de cinquante ans de 1 741. L'abandon après le plan vaut mieux que la tonte d'une pelouse : la friche abandonnée garde plus de valeur que la pelouse (BKompV).
- Climat : d'une zone à l'autre, l'écart reste sous 73 m²HE·an, parce que la végétation de chaque zone est jugée sur son propre climat ; un début en 2045 décale la période vers un climat plus chaud et baisse Cnat de 77 m²HE·an, l'état initial perdant davantage que le projet.
- Mare en zone H3 : sans bassin versant, elle s'assèche au printemps ; raccordée à 3 000 m² de prairie, elle tient mieux (Cnat -11 959) ; avec un fond étanche, elle reste en eau (Cnat -12 352, contre -9 614).

### Cas D01. Chantier commencé en mai : défrichement pendant la nidification

**Résultat attendu** : supplément de Cnat pour la friche et le fourré détruits en période sensible (fiche A57).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | mai 2027 ; période 2027 à 2076 |
| Mois de destruction | mai |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 18 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 18 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 18 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 18 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 53,5 | 147,4 | 215,9 | 249,9 | 205 | 204,3 | 202,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 023,2 | m²HE·an |
| Cnat | 3 497,5 | m²HE·an |
| Cnat relatif | 0,263 |  |
| Cnat sur 30 ans | 2 268,4 | m²HE·an |
| Dette de maturité | 710,9 | m²HE·an |
| Supplément pour destruction en période sensible | 243,6 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 340,3 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D02. Chantier commencé en janvier : plantations reportées à novembre de l'année suivante

**Résultat attendu** : maturation plus tardive, Cnat plus élevé que l'exemple (fiche A58).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | janvier 2027 ; période 2027 à 2076 |
| Mois de destruction | janvier |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 22 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 22 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 22 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 22 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 32,7 | 124 | 208,5 | 249,3 | 205 | 204,3 | 202,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 9 949,7 | m²HE·an |
| Cnat | 3 327,4 | m²HE·an |
| Cnat relatif | 0,251 |  |
| Cnat sur 30 ans | 2 098,4 | m²HE·an |
| Dette de maturité | 786,6 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 170,3 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D03. Toiture extensive de 8 cm au lieu de 15 cm

**Résultat attendu** : valeur et facteur hydrique plus faibles (fiche A48).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.11 | hors sol toiture | 500 | S04 | créée | 1 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,5 | 1 | 0,2639 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 49,27 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | toiture extensive | 16 | 19,8 | 19 | 24,3 | 1 | 1 | 0,987 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 85,2 | 186,4 | 229,8 | 242,4 | 195,2 | 194,8 | 193,4 | 191,5 | 189,6 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 9 762,1 | m²HE·an |
| Cnat | 3 515 | m²HE·an |
| Cnat relatif | 0,265 |  |
| Cnat sur 30 ans | 2 113,4 | m²HE·an |
| Dette de maturité | 479,9 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 357,8 | m²HE·an |
| Bnat | 56,5 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 56,5 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D04. Toiture semi-intensive de 30 cm

**Résultat attendu** : moins de stress hydrique (fiche A48).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 60 | 20,1 | 28,4 | 39,7 | 0,948 | 0,915 | 0,87 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,4 | 157,5 | 221,1 | 252,7 | 207,3 | 206,4 | 204,2 | 201,8 | 199,5 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 153 | m²HE·an |
| Cnat | 3 124 | m²HE·an |
| Cnat relatif | 0,235 |  |
| Cnat sur 30 ans | 1 929,7 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 966,9 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D05. Toiture intensive de 50 cm (gazon et massifs, type VB.13)

**Résultat attendu** : facteur hydrique de 1 mais valeur intrinsèque plus faible que la toiture biodiverse (distinctivité faible de la métrique anglaise).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.13 | hors sol toiture | 500 | S06 | créée | 5 | 1 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,7 | 1 | 0,2639 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 49,27 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 100 | 9,8 | 18,8 | 32,1 | 0,989 | 0,953 | 0,9 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 70,5 | 163,7 | 224,1 | 241,3 | 193,7 | 192,9 | 190,8 | 188,5 | 186,2 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 9 603,1 | m²HE·an |
| Cnat | 3 674 | m²HE·an |
| Cnat relatif | 0,277 |  |
| Cnat sur 30 ans | 2 213,3 | m²HE·an |
| Dette de maturité | 535,2 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 516,8 | m²HE·an |
| Bnat | 61,5 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 61,5 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D06. Prairie urbaine arrosée

**Résultat attendu** : facteur hydrique de 1, consommation d'eau d'arrosage affichée (fiche A49).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 0 | 0 | 0 | 1 | 1 | 1 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,5 | 219,2 | 250,6 | 205,4 | 205 | 203,5 | 201,8 | 200,1 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 109,7 | m²HE·an |
| Cnat | 3 167,4 | m²HE·an |
| Cnat relatif | 0,239 |  |
| Cnat sur 30 ans | 1 972,9 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 34,3 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 010,2 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D07. Sol sableux

**Résultat attendu** : réserve utile plus faible, stress hydrique accru (fiche A48).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture sable, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 12 682 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 75 | 16,4 | 25 | 36,9 | 0,963 | 0,929 | 0,881 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 68 | 39,7 | 43,8 | 53,8 | 0,991 | 0,967 | 0,906 | 1 |
| U0-4 | arbore | 75 | 53,1 | 54,6 | 66,1 | 0,982 | 0,97 | 0,878 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 75 | 16,4 | 25 | 36,9 | 0,963 | 0,929 | 0,881 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 75 | 16,4 | 25 | 36,9 | 0,963 | 0,929 | 0,881 | 1 | 16 | 1 |
| U1-6 | arbustif | 68 | 39,7 | 43,8 | 53,8 | 0,991 | 0,967 | 0,906 | 1 | 16 | 0,75 |
| U1-7 | arbore | 75 | 53,1 | 54,6 | 66,1 | 0,982 | 0,97 | 0,878 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 23,6 | 66,4 | 152,3 | 213,5 | 243,3 | 199,4 | 198,1 | 195,8 | 193,7 | 191,6 |
| V_0 x k_W, m²HE | 261,8 | 261,8 | 261,8 | 261,4 | 259,3 | 257,2 | 255,1 | 251,7 | 248,8 | 245,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 12 682 | m²HE·an |
| I_1 | 9 756,3 | m²HE·an |
| Cnat | 2 925,8 | m²HE·an |
| Cnat relatif | 0,231 |  |
| Cnat sur 30 ans | 1 825,3 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 768,6 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D08. Sol argileux

**Résultat attendu** : réserve utile plus forte.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture argile, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 354,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 140 | 0,4 | 8,7 | 24 | 1 | 0,994 | 0,932 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 126 | 32,3 | 36,1 | 46,7 | 1 | 1 | 0,95 | 1 |
| U0-4 | arbore | 140 | 44,5 | 48,1 | 60,3 | 1 | 1 | 0,925 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 140 | 0,4 | 8,7 | 24 | 1 | 0,994 | 0,932 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 140 | 0,4 | 8,7 | 24 | 1 | 0,994 | 0,932 | 1 | 16 | 1 |
| U1-6 | arbustif | 126 | 32,3 | 36,1 | 46,7 | 1 | 1 | 0,95 | 1 | 16 | 0,75 |
| U1-7 | arbore | 140 | 44,5 | 48,1 | 60,3 | 1 | 1 | 0,925 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,5 | 219,2 | 250,5 | 205,5 | 205,1 | 203,4 | 201,1 | 198,9 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,3 | 270 | 269,7 | 269,3 | 267,1 | 263,7 | 260,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 354,1 | m²HE·an |
| I_1 | 10 097,6 | m²HE·an |
| Cnat | 3 256,4 | m²HE·an |
| Cnat relatif | 0,244 |  |
| Cnat sur 30 ans | 2 005,6 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 099,3 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D09. Sol limoneux de 40 cm sur dalle rocheuse

**Résultat attendu** : réserve utile bornée par la profondeur de sol.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 0.4 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 12 403,2 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 52 | 22 | 30,2 | 41,1 | 0,941 | 0,908 | 0,864 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 52 | 42,6 | 47,1 | 56,2 | 0,974 | 0,947 | 0,892 | 1 |
| U0-4 | arbore | 52 | 56,6 | 57,7 | 68,2 | 0,954 | 0,945 | 0,861 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 52 | 22 | 30,2 | 41,1 | 0,941 | 0,908 | 0,864 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 52 | 22 | 30,2 | 41,1 | 0,941 | 0,908 | 0,864 | 1 | 16 | 1 |
| U1-6 | arbustif | 52 | 42,6 | 47,1 | 56,2 | 0,974 | 0,947 | 0,892 | 1 | 16 | 0,75 |
| U1-7 | arbore | 52 | 56,6 | 57,7 | 68,2 | 0,954 | 0,945 | 0,861 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 22,9 | 65 | 149,4 | 209,6 | 239,2 | 196,3 | 195,1 | 193 | 191 | 189 |
| V_0 x k_W, m²HE | 255,8 | 255,8 | 255,8 | 255,4 | 253,4 | 251,4 | 249,4 | 246,2 | 243,5 | 240,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 12 403,2 | m²HE·an |
| I_1 | 9 607,8 | m²HE·an |
| Cnat | 2 795,4 | m²HE·an |
| Cnat relatif | 0,225 |  |
| Cnat sur 30 ans | 1 745,7 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 638,3 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D10. Zone climatique H1b (Nancy)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1b, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 458,4 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,911 | 1 | 89,62 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 10,1 | 14 | 22,1 | 1 | 1 | 0,972 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 32,8 | 37 | 45 | 1 | 1 | 0,957 | 1 |
| U0-4 | arbore | 130 | 45,7 | 49,5 | 56,9 | 1 | 1 | 0,951 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 10,1 | 14 | 22,1 | 1 | 1 | 0,972 | 0,911 | 16 | 0,533 |
| U1-5 | prairie | 130 | 10,1 | 14 | 22,1 | 1 | 1 | 0,972 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 32,8 | 37 | 45 | 1 | 1 | 0,957 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,7 | 49,5 | 56,9 | 1 | 1 | 0,951 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 32,1 | 35,7 | 46,2 | 0,932 | 0,917 | 0,875 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,3 | 156,9 | 220,1 | 252,2 | 207,6 | 207,3 | 206,3 | 204,8 | 203,3 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 269,3 | 267,6 | 265,9 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 458,4 | m²HE·an |
| I_1 | 10 225,6 | m²HE·an |
| Cnat | 3 232,8 | m²HE·an |
| Cnat relatif | 0,24 |  |
| Cnat sur 30 ans | 1 976,4 | m²HE·an |
| Dette de maturité | 671,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 075,7 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D11. Zone climatique H1c (Mâcon)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1c, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 519,3 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,913 | 1 | 89,8 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 20 | 17,2 | 16,1 | 1 | 1 | 1 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 41,6 | 40,6 | 39,4 | 1 | 1 | 1 | 1 |
| U0-4 | arbore | 130 | 53 | 53,1 | 53,5 | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 20 | 17,2 | 16,1 | 1 | 1 | 1 | 0,913 | 16 | 0,533 |
| U1-5 | prairie | 130 | 20 | 17,2 | 16,1 | 1 | 1 | 1 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 41,6 | 40,6 | 39,4 | 1 | 1 | 1 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 53 | 53,1 | 53,5 | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 43,6 | 42,1 | 33,2 | 0,925 | 0,931 | 0,967 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,3 | 156,8 | 220 | 252,4 | 208 | 208,1 | 208,4 | 208,9 | 209,4 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 519,3 | m²HE·an |
| I_1 | 10 329,1 | m²HE·an |
| Cnat | 3 190,2 | m²HE·an |
| Cnat relatif | 0,236 |  |
| Cnat sur 30 ans | 1 961,4 | m²HE·an |
| Dette de maturité | 672,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 033,1 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D12. Zone climatique H2a (Rennes)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H2a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 390,8 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,924 | 1 | 90,85 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 53,1 | 55,2 | 64,2 | 1 | 1 | 0,963 | 1 |
| U0-4 | arbore | 130 | 67,1 | 68,4 | 76,7 | 1 | 1 | 0,963 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 0,924 | 16 | 0,533 |
| U1-5 | prairie | 130 | 24,2 | 30,5 | 42,9 | 1 | 0,995 | 0,945 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 53,1 | 55,2 | 64,2 | 1 | 1 | 0,963 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 67,1 | 68,4 | 76,7 | 1 | 1 | 0,963 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 46,4 | 53,4 | 62,8 | 0,931 | 0,903 | 0,866 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,4 | 157,5 | 221,1 | 252,9 | 207,4 | 206,8 | 205,3 | 203,5 | 201,7 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,3 | 270,1 | 269,8 | 269,5 | 267,8 | 265,3 | 262,7 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 390,8 | m²HE·an |
| I_1 | 10 197,8 | m²HE·an |
| Cnat | 3 193 | m²HE·an |
| Cnat relatif | 0,238 |  |
| Cnat sur 30 ans | 1 959 | m²HE·an |
| Dette de maturité | 675,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 035,9 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D13. Zone climatique H2b (Tours)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H2b, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 429,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,919 | 1 | 90,36 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 36,7 | 38,7 | 51,6 | 1 | 1 | 0,96 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 58,6 | 62,5 | 73,5 | 1 | 1 | 0,941 | 1 |
| U0-4 | arbore | 130 | 70 | 76,1 | 82,2 | 1 | 0,991 | 0,942 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 36,7 | 38,7 | 51,6 | 1 | 1 | 0,96 | 0,919 | 16 | 0,533 |
| U1-5 | prairie | 130 | 36,7 | 38,7 | 51,6 | 1 | 1 | 0,96 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 58,6 | 62,5 | 73,5 | 1 | 1 | 0,941 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 70 | 76,1 | 82,2 | 1 | 0,991 | 0,942 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 56,9 | 59,9 | 76,5 | 0,939 | 0,927 | 0,86 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,4 | 157,4 | 221 | 253,4 | 208,4 | 208,2 | 206,7 | 204,6 | 202,6 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,3 | 270,3 | 270,2 | 268,8 | 266,4 | 264,1 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 429,1 | m²HE·an |
| I_1 | 10 246,1 | m²HE·an |
| Cnat | 3 183 | m²HE·an |
| Cnat relatif | 0,237 |  |
| Cnat sur 30 ans | 1 947,3 | m²HE·an |
| Dette de maturité | 673,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 025,8 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D14. Zone climatique H2c (Agen)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H2c, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 494,2 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,919 | 1 | 90,35 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 33,6 | 30,9 | 42,8 | 1 | 1 | 0,983 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 59,7 | 57 | 62,8 | 1 | 1 | 1 | 1 |
| U0-4 | arbore | 130 | 73,1 | 71,3 | 75,8 | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 33,6 | 30,9 | 42,8 | 1 | 1 | 0,983 | 0,919 | 16 | 0,533 |
| U1-5 | prairie | 130 | 33,6 | 30,9 | 42,8 | 1 | 1 | 0,983 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 59,7 | 57 | 62,8 | 1 | 1 | 1 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 73,1 | 71,3 | 75,8 | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 63,9 | 59,6 | 67,6 | 0,899 | 0,916 | 0,884 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,6 | 219,4 | 251,5 | 206,9 | 207,2 | 207 | 206,2 | 205,5 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270 | 269,2 | 268,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 494,2 | m²HE·an |
| I_1 | 10 248,1 | m²HE·an |
| Cnat | 3 246,1 | m²HE·an |
| Cnat relatif | 0,241 |  |
| Cnat sur 30 ans | 1 985,6 | m²HE·an |
| Dette de maturité | 673,8 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 089 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D15. Zone climatique H2d (Carpentras)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H2d, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 519,3 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,913 | 1 | 89,81 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 74,6 | 76 | 70,5 | 1 | 1 | 1 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 94,9 | 94,9 | 90,7 | 1 | 1 | 1 | 1 |
| U0-4 | arbore | 130 | 104,4 | 104,9 | 101,7 | 1 | 1 | 1 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 74,6 | 76 | 70,5 | 1 | 1 | 1 | 0,913 | 16 | 0,533 |
| U1-5 | prairie | 130 | 74,6 | 76 | 70,5 | 1 | 1 | 1 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 94,9 | 94,9 | 90,7 | 1 | 1 | 1 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 104,4 | 104,9 | 101,7 | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 104 | 102,1 | 108,4 | 0,902 | 0,91 | 0,885 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,1 | 156,3 | 219 | 251 | 206,5 | 206,7 | 206,6 | 206,2 | 205,9 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 519,3 | m²HE·an |
| I_1 | 10 234,9 | m²HE·an |
| Cnat | 3 284,4 | m²HE·an |
| Cnat relatif | 0,243 |  |
| Cnat sur 30 ans | 2 000,7 | m²HE·an |
| Dette de maturité | 672,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 127,2 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D16. Zone climatique H3 (Marignane)

**Résultat attendu** : effet du climat local et de son évolution.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 479,7 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,913 | 1 | 89,83 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 |
| U0-4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 0,913 | 16 | 0,533 |
| U1-5 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 123,9 | 127,1 | 144,7 | 0,917 | 0,904 | 0,834 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,7 | 219,6 | 251,5 | 206,8 | 206,6 | 205,5 | 204 | 202,5 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 270,4 | 269,7 | 268,6 | 267,5 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 479,7 | m²HE·an |
| I_1 | 10 189,5 | m²HE·an |
| Cnat | 3 290,2 | m²HE·an |
| Cnat relatif | 0,244 |  |
| Cnat sur 30 ans | 1 997,5 | m²HE·an |
| Dette de maturité | 672,4 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 133,1 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D17. Prairie éclairée toute la nuit en 4 000 K

**Résultat attendu** : facteur d'éclairage de 0,75 (fiche A53).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,75 | 1 | 73,77 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,75 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 65,9 | 147,8 | 204,5 | 233,9 | 196,3 | 195,7 | 193,9 | 191,7 | 189,5 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 9 586,1 | m²HE·an |
| Cnat | 3 691 | m²HE·an |
| Cnat relatif | 0,278 |  |
| Cnat sur 30 ans | 2 294,1 | m²HE·an |
| Dette de maturité | 629 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 533,9 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D18. Prairie éclairée jusqu'à 23 h en 2 700 K, luminaires à 20 m

**Résultat attendu** : facteur d'éclairage proche de 1 (fiche A53).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,974 | 1 | 95,78 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,974 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 69 | 159,5 | 224,2 | 255,8 | 208 | 207,3 | 205,4 | 203 | 200,7 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 224,7 | m²HE·an |
| Cnat | 3 052,3 | m²HE·an |
| Cnat relatif | 0,23 |  |
| Cnat sur 30 ans | 1 881,7 | m²HE·an |
| Dette de maturité | 688,4 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 895,2 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D19. Prairie éclairée toute la nuit en ambre avec détection de présence (30 % du temps)

**Résultat attendu** : facteur d'éclairage intermédiaire.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,963 | 1 | 94,67 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,963 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,8 | 158,9 | 223,2 | 254,7 | 207,4 | 206,7 | 204,8 | 202,5 | 200,1 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 192,5 | m²HE·an |
| Cnat | 3 084,6 | m²HE·an |
| Cnat relatif | 0,232 |  |
| Cnat sur 30 ans | 1 902,5 | m²HE·an |
| Dette de maturité | 685,4 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 927,4 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D20. Sans plan de gestion écologique

**Résultat attendu** : gestion courante dès la livraison (fiche A55, C-M3).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 0 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 132,6 | 177,5 | 203,4 | 205 | 204,3 | 202,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 9 633,5 | m²HE·an |
| Cnat | 3 643,6 | m²HE·an |
| Cnat relatif | 0,274 |  |
| Cnat sur 30 ans | 2 414,6 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 486,5 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D21. Plan de gestion de trente ans

**Résultat attendu** : gestion courante après trente ans.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 30 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,5 | 219,1 | 250,1 | 251,5 | 250,7 | 248,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 10 985,5 | m²HE·an |
| Cnat | 2 291,6 | m²HE·an |
| Cnat relatif | 0,173 |  |
| Cnat sur 30 ans | 1 154,3 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 134,4 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D22. Plan de gestion couvrant les cinquante ans

**Résultat attendu** : aucune perte de gestion.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 50 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 1 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 1 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,5 | 219,1 | 250,1 | 251,5 | 250,7 | 248,4 | 245,5 | 242,6 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 11 800,7 | m²HE·an |
| Cnat | 1 476,4 | m²HE·an |
| Cnat relatif | 0,111 |  |
| Cnat sur 30 ans | 1 154,3 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -143 319,2 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D23. Abandon de l'entretien à la fin du plan de dix ans

**Résultat attendu** : friche puis embroussaillement des milieux herbacés (fiche A56, C-M2).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 277,1 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,84 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1,146 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 68,2 | 156,5 | 219,1 | 250,1 | 214,3 | 213,6 | 236,7 | 234 | 231,2 |
| V_0 x k_W, m²HE | 270,4 | 270,4 | 270,4 | 270,2 | 269,4 | 268,5 | 267,7 | 265 | 261,6 | 258,3 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 277,1 | m²HE·an |
| I_1 | 11 044 | m²HE·an |
| Cnat | 2 233,1 | m²HE·an |
| Cnat relatif | 0,168 |  |
| Cnat sur 30 ans | 1 680,8 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 076 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D24. Chantier commencé en 2045

**Résultat attendu** : climat plus chaud sur la période : facteurs hydriques plus faibles (fiche A46).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2045 ; période 2045 à 2094 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 26,83 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 270,39 m²HE ; I_0 = 13 019,6 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | conservée | 0 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 18 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 24 | 67,7 | 154,9 | 216,7 | 246,7 | 201,7 | 200,6 | 198,3 | 195,9 | 193,6 |
| V_0 x k_W, m²HE | 267,8 | 267,7 | 267,5 | 267,1 | 265,6 | 264 | 262,3 | 258,9 | 255,6 | 252,2 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 019,6 | m²HE·an |
| I_1 | 9 879,1 | m²HE·an |
| Cnat | 3 140,6 | m²HE·an |
| Cnat relatif | 0,241 |  |
| Cnat sur 30 ans | 1 948,7 | m²HE·an |
| Dette de maturité | 673,1 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -144 983,4 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D25. Cas 6 en zone H3, mare sans bassin versant

**Résultat attendu** : assec de printemps (fiche A49, C-W12).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 0,5 | 0,5 | 0,5 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 173,4 | 689,8 | 1 017,8 | 1 314,7 | 1 387,5 | 867,7 | 894 | 925,9 | 928,1 | 924,6 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 48 230,1 | m²HE·an |
| Cnat | -9 613,5 | m²HE·an |
| Cnat relatif | -0,249 |  |
| Cnat sur 30 ans | -6 442,4 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 9 442,5 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas D26. Cas 6 en zone H3, mare raccordée à 3 000 m² de prairie

**Résultat attendu** : mare en eau au printemps.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 1 | 1 | 0,5 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 185,2 | 730,5 | 1 070 | 1 370,7 | 1 443,6 | 923,8 | 950,1 | 975,3 | 966,2 | 951,5 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 50 575,2 | m²HE·an |
| Cnat | -11 958,6 | m²HE·an |
| Cnat relatif | -0,31 |  |
| Cnat sur 30 ans | -8 036,5 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 11 787,6 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas D27. Cas 6 en zone H3, mare à fond étanche raccordée à 3 000 m² de prairie

**Résultat attendu** : mare en eau toute l'année.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 5 000 m² |
| Emprise du bâti | 0 m² |
| Zone biogéographique | mediterraneenne |
| Typologie | amenagement |
| Durée du chantier | 6 mois (d_ch = 0,5 an) |
| Zone climatique, altitude | H3, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | septembre 2027 ; période 2027 à 2076 |
| Mois de destruction | septembre |
| Plan de gestion écologique | 10 ans |
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

Valeur du site sans projet V_0 = 774,68 m²HE ; I_0 = 38 616,6 m²HE·an.

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

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| I1 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | mare |  |  |  |  | 1 | 1 | 1 | 1 | 4 | 1 |
| P2 | arbustif | 117 | 122,9 | 122,6 | 130,4 | 1 | 1 | 0,985 | 1 | 4 | 0,75 |
| P3 | prairie | 130 | 98,2 | 101,9 | 108,6 | 1 | 1 | 0,978 | 1 | 4 | 0,533 |
| P4 | arbore | 130 | 140,5 | 139,9 | 148,3 | 1 | 1 | 0,978 | 1 | 4 | 1 |
| P5 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 6 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 185,2 | 730,5 | 1 070 | 1 370,7 | 1 443,6 | 923,8 | 950,1 | 982 | 984,2 | 980,7 |
| V_0 x k_W, m²HE | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 774,7 | 772,7 | 769,3 | 766 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 38 616,6 | m²HE·an |
| I_1 | 50 968,6 | m²HE·an |
| Cnat | -12 352 | m²HE·an |
| Cnat relatif | -0,32 |  |
| Cnat sur 30 ans | -8 060 | m²HE·an |
| Dette de maturité | 4 439,5 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 0 | m²HE·an |
| Inat bois | 0 | m²HE·an |
| Inat carrières | 171 | m²HE·an |
| Inat | 171 | m²HE·an |
| Snat | 12 181 | m²HE·an |
| Bnat | 92,8 | points |
| Pleine terre | 0,88 |  |
| Imperméabilisation nette | 0 | m² |

**Conformité (fiche A40)** : pas de seuil de Bnat pour cette typologie ; pleine terre 88 % pour un seuil de 15 % : atteint ; niveau du site : 2.

### Cas D28. Arbres âgés à gîtes abattus en janvier

**Résultat attendu** : supplément de Cnat pour les chiroptères en hibernation (fiche A57).

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | janvier 2027 ; période 2027 à 2076 |
| Mois de destruction | janvier |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,75 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 32,2 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 275,75 m²HE ; I_0 = 13 542,2 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | créée | 27 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 22 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 22 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 22 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 22 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 22 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 8,7 | 99,9 | 185 | 230,6 | 193,1 | 198,1 | 202,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 275,8 | 275,8 | 275,8 | 275,6 | 274,7 | 273,9 | 273 | 270,3 | 266,8 | 263,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 542,2 | m²HE·an |
| I_1 | 9 588,4 | m²HE·an |
| Cnat | 3 986 | m²HE·an |
| Cnat relatif | 0,294 |  |
| Cnat sur 30 ans | 2 652,6 | m²HE·an |
| Dette de maturité | 1 147,8 | m²HE·an |
| Supplément pour destruction en période sensible | 32,2 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 828,8 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.

### Cas D29. Arbres âgés à gîtes abattus en octobre

**Résultat attendu** : pas de supplément : période favorable.

**Hypothèses**

| Donnée | Valeur |
|---|---|
| Parcelle | 2 000 m² |
| Emprise du bâti | 700 m² |
| Zone biogéographique | continentale |
| Typologie | logement |
| Durée du chantier | 18 mois (d_ch = 1,5 an) |
| Zone climatique, altitude | H1a, altitude de la station |
| Sol du site | texture limon, profondeur 1.0 |
| Début du chantier | octobre 2027 ; période 2027 à 2076 |
| Mois de destruction | octobre |
| Plan de gestion écologique | 10 ans |
| Surface de référence | 1 400 m² |
| Émissions des composants et du chantier | A1-A5 : 470, B : 400, C : 55, D : -40 |
| Bois | 30 m³ (coupe rase) |
| Granulats | 1 800 t |
| Surface infiltrée en surface | 0 m² |

**Étape E2, fermeture (fiche A03)**

| État | Somme au sol (m²) | Écart (m²) | Contrôle |
|---|---|---|---|
| initial | 2 000 | 0 | satisfait |
| projet | 2 000 | 0 | satisfait |

**État initial (fiches A06 à A25)**

| Unité | Type | Position | A (m²) | Nature |
|---|---|---|---|---|
| U0-1 | VB.8 | sol pleine terre | 1 200 | S08 |
| U0-2 | VB.2 | sol pleine terre | 600 | S01 |
| U0-3 | VB.9 | sol pleine terre | 200 | S08 |
| U0-4 | VB.18a | arbre | 100 |  |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U0-1 | 1 | 1 | 0,5 | 0,5 | 0,75 | 1 | 0,4684 | 1 | 1 | 210,77 |
| U0-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U0-3 | 1 | 1 | 0,5 | 0,4 | 0,7 | 1 | 0,4684 | 1 | 1 | 32,79 |
| U0-4 |  | 1 | 0,75 | 0,8333 | 0,9167 | 1 | 0,4684 | 1 | 1 | 32,2 |

Taches de l'état initial (fiches A17 à A19) :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P1 | 1 400 | 0,4684 | 1 | 1 | 0,4684 |

Valeur du site sans projet V_0 = 275,75 m²HE ; I_0 = 13 542,2 m²HE·an.

**État projet (fiches A06 à A30)**

| Unité | Type | Position | A (m²) | Nature | Statut | d (an) | D |
|---|---|---|---|---|---|---|---|
| U1-1 | VB.1 | sol pleine terre | 700 | S01 | créée | 0 | 1 |
| U1-2 | VB.2 | sol pleine terre | 300 | S01 | créée | 0 | 1 |
| U1-3 | VB.3 | sol pleine terre | 150 | S02 | créée | 0 | 1 |
| U1-4 | VB.26 | sol pleine terre | 450 | S08 | créée | 5 | 1 |
| U1-5 | VB.7 | sol pleine terre | 320 | S08 | créée | 1 | 1 |
| U1-6 | FA.3 | lineaire | 80 | S08 | créée | 5 | 1 |
| U1-7 | VB.18a | arbre | 100 |  | créée | 27 | 1 |
| U1-8 | VB.12 | hors sol toiture | 500 | S05 | créée | 10 | 0,67 |

Facteurs de calcul :

| Unité | c | f_sol | v | S | f | m | k_C | k_N | k_E | V (m²HE) |
|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-2 | 0 | 1 | 0 |  | 1 | 1 | 1 | 1 | 1 | 0 |
| U1-3 | 0,2 | 1 | 0,1667 |  | 1 | 1 | 0,35 | 1 | 1 | 8,75 |
| U1-4 | 1 | 1 | 0,625 | 0,6667 | 0,8333 | 1 | 0,4197 | 0,916 | 1 | 90,1 |
| U1-5 | 1 | 1 | 0,4583 | 0,6667 | 0,8333 | 1 | 0,4197 | 1 | 1 | 51,29 |
| U1-6 | 1 | 1 | 0,6667 | 0,75 | 0,875 | 1 | 0,4197 | 1 | 1 | 19,59 |
| U1-7 |  | 1 | 0,625 | 0,8333 | 0,9167 | 1 | 0,4197 | 1 | 1 | 24,04 |
| U1-8 | 0,6 | 1 | 0,5278 | 1 | 1 | 1 | 0,3734 | 1 | 1 | 98,55 |

Taches de l'état projet :

| Tache | A_k (m²) | k_taille | m_conn | k_clot | k_C |
|---|---|---|---|---|---|
| P2 | 850 | 0,4197 | 1 | 1 | 0,4197 |
| P3 | 500 | 0,3734 | 1 | 1 | 0,3734 |
| isolee_U1-3 | 150 | 0,35 | 1 | 1 | 0,35 |

**Modules dynamiques, état initial (fiches A47 à A53)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum |
|---|---|---|---|---|---|---|---|---|---|
| U0-1 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 |
| U0-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 |
| U0-3 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 |
| U0-4 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 |

**Modules dynamiques, état projet (fiches A47 à A58)**

| Unité | Groupe | RU (mm) | IS +2 | IS +2,7 | IS +4 | k_W +2 | k_W +2,7 | k_W +4 | k_lum | Départ (rang) | f_g an 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1-1 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-2 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-3 | sans bilan |  |  |  |  | 1 | 1 | 1 | 1 | 18 | 1 |
| U1-4 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 0,916 | 16 | 0,533 |
| U1-5 | prairie | 130 | 2,1 | 11,2 | 26,2 | 1 | 0,984 | 0,924 | 1 | 16 | 1 |
| U1-6 | arbustif | 117 | 33,3 | 37,4 | 47,7 | 1 | 1 | 0,943 | 1 | 16 | 0,75 |
| U1-7 | arbore | 130 | 45,8 | 48,9 | 61,4 | 1 | 1 | 0,915 | 1 | 16 | 1 |
| U1-8 | prairie | 30 | 31,6 | 35,3 | 45,7 | 0,902 | 0,887 | 0,846 | 1 | 16 | 1 |

**Trajectoire du site (fiche A31)**

| Année | 1 | 2 | 3 | 5 | 10 | 15 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_1(t), m²HE | 0 | 44,1 | 132,5 | 195,9 | 232,1 | 193,7 | 198,6 | 202,4 | 200,1 | 197,8 |
| V_0 x k_W, m²HE | 275,8 | 275,8 | 275,8 | 275,6 | 274,7 | 273,9 | 273 | 270,3 | 266,8 | 263,4 |

**Indicateurs (fiches A33 à A38)**

| Indicateur | Valeur | Unité |
|---|---|---|
| I_0 | 13 542,2 | m²HE·an |
| I_1 | 9 710,7 | m²HE·an |
| Cnat | 3 831,5 | m²HE·an |
| Cnat relatif | 0,283 |  |
| Cnat sur 30 ans | 2 498,2 | m²HE·an |
| Dette de maturité | 1 022,3 | m²HE·an |
| Supplément pour destruction en période sensible | 0 | m²HE·an |
| Arrosage annuel moyen | 0 | m³ |
| Inat climat | 84 748,3 | m²HE·an |
| Inat bois | 55 555,6 | m²HE·an |
| Inat carrières | 1 539 | m²HE·an |
| Inat | 141 842,9 | m²HE·an |
| Snat | -145 674,4 | m²HE·an |
| Bnat | 59 | points |
| Pleine terre | 0,425 |  |
| Imperméabilisation nette | 400 | m² |

**Conformité (fiche A40)** : Bnat 59 pour un seuil de 45 : atteint ; pleine terre 42,5 % pour un seuil de 15 % : atteint ; niveau du site : 0.
