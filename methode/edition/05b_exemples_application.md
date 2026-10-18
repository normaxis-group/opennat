### 5.6 Exemples chiffrés

Chaque fiche d'application est illustrée ci-dessous par des variantes d'une même situation, calculées par le carnet de référence (`outils/carnet_reference.py`). Sauf mention contraire : parcelle de 2 000 m², zone continentale, chantier de 12 mois, hors trame verte et bleue, sans nuisance, taches de connexion faible. Les valeurs sont en m²HE, m²HE·an, points et pourcentage.

#### Exemple de la fiche F01. Réhabilitation : cour laissée en enrobé ou désimperméabilisée

Un immeuble de 600 m² d'emprise sur une parcelle de 2 000 m² entièrement revêtue est réhabilité. Variante A : la cour reste en enrobé. Variante B : 900 m² de cour deviennent jardin commun et prairie.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Variante B | 0 | 0 | 6 098 | -6 098 | 282 | 0 | 45 | 45 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 500 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 500 | 0,4583 | 0,8333 | 1 | 0,425 | 1 | 1 | 81,15 | 1 | 1 |
| P4 | VB.26 | 400 | 0,625 | 0,8333 | 1 | 0,425 | 1 | 1 | 88,54 | 5 | 1 |

#### Exemple de la fiche F02. Extension sur une prairie de fauche

Une maison de 400 m² d'emprise sur une parcelle de 2 000 m² de prairie de fauche s'agrandit de 200 m². Variante A : extension au sol. Variante B : surélévation, sans emprise nouvelle, avec toiture extensive.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 535,9 | 26 253 | 22 193 | 4 060 | 0 | 0 | 70 | 70 |
| Variante B | 535,9 | 26 253 | 27 783 | -1 530 | 34 | 0 | 90 | 80 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.1 | 200 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | E2.2 | 1 400 | 0,8333 | 0,8333 | 1 | 0,4684 | 1 | 1 | 455,34 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | E2.2 | 1 600 | 0,8333 | 0,8333 | 1 | 0,4823 | 1 | 1 | 535,9 | 0 | 1 |
| P4 | VB.11 | 400 | 0,2639 | 0,8333 | 1 | 0,3555 | 1 | 1 | 31,28 | 1 | 1 |

#### Exemple de la fiche F04. Culture ou prairie permanente à l'état initial

Le même lotissement de 2 000 m² est construit sur une culture intensive (variante A) ou sur une prairie permanente pâturée en état moyen (variante B). Le projet est identique.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 253,3 | 12 409 | 7 959 | 4 450 | 178 | 0 | 50 | 50 |
| Variante B | 457,4 | 22 406 | 7 959 | 14 447 | 178 | 0 | 50 | 50 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 1 000 | 0,4583 | 0,8333 | 1 | 0,435 | 1 | 1 | 166,12 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 1 000 | 0,4583 | 0,8333 | 1 | 0,435 | 1 | 1 | 166,12 | 1 | 1 |

#### Exemple de la fiche F07. Friche riche ou terrain vague

Une friche urbaine de 2 000 m² est construite. Variante A : friche en mosaïque riche (critère D satisfait, aucune espèce envahissante). Variante B : terrain vague envahi par une espèce exotique (critère C essentiel échoué).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 506,6 | 24 818 | 6 062 | 18 755 | 136 | 0 | 40 | 40 |
| Variante B | 380 | 18 613 | 6 062 | 12 551 | 136 | 0 | 40 | 40 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

#### Exemple de la fiche F08. Jardin en pleine terre ou sur dalle de parking

Un jardin commun de 800 m² est aménagé. Variante A : en pleine terre. Variantes B, C et D : sur la dalle d'un parking souterrain, avec 30, 60 et 100 cm de substrat.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 0 | 0 | 6 062 | -6 062 | 136 | 0 | 40 | 40 |
| Variante B | 0 | 0 | 3 405 | -3 405 | 82 | 0 | 24 | 0 |
| Variante C | 0 | 0 | 4 213 | -4 213 | 95 | 0 | 28 | 0 |
| Variante D | 0 | 0 | 5 561 | -5 561 | 122 | 0 | 36 | 0 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 0,6 | 0,4141 | 1 | 1 | 75,92 | 1 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 0,7 | 0,4141 | 1 | 1 | 88,57 | 1 | 1 |

Variante D, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 0,9 | 0,4141 | 1 | 1 | 113,87 | 1 | 1 |

#### Exemple de la fiche F09. Prairie conservée avec ou sans protection en chantier

Une prairie de fauche de 1 200 m² est conservée pendant un chantier de 24 mois. Variante A : clôturée et protégée. Variante B : sans protection (convention C-T4).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 415 | 20 330 | 20 330 | 7,276 x 10^-12 | 0 | 0 | 60 | 60 |
| Variante B | 415 | 20 330 | 20 123 | 208 | 0 | 0 | 60 | 60 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | E2.2 | 1 200 | 0,8333 | 0,9167 | 1 | 0,4528 | 1 | 1 | 415,01 | 0 | 1 |
| P2 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | E2.2 | 1 200 | 0,8333 | 0,9167 | 1 | 0,4528 | 1 | 1 | 415,01 | 0 | 1 |
| P2 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

#### Exemple de la fiche F10. Deux grands arbres conservés, abattus ou transplantés

Deux chênes indigènes de grand diamètre (houppier de 733 m² par défaut) se trouvent sur une pelouse de 2 000 m² construite pour moitié. Variante A : conservés et protégés. Variante B : abattus. Variante C : transplantés (unité créée de stade jeune, fiche F10).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 496,5 | 24 556 | 15 845 | 8 711 | 111 | 0 | 50 | 50 |
| Variante B | 496,5 | 24 556 | 5 015 | 19 795 | 111 | 0 | 50 | 50 |
| Variante C | 496,5 | 24 556 | 9 324 | 15 487 | 1 819 | 0 | 50 | 50 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 1 | 1 |
| P3 | VB.18a | 733 | 0,75 | 0,9167 | 1 | 0,435 | 1 | 1 | 219,19 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 1 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 1 | 1 |
| P3 | VB.18a | 733 | 0,4583 | 0,8333 | 1 | 0,435 | 1 | 1 | 121,76 | 27 | 1 |

#### Exemple de la fiche F11. Haie existante renforcée ou remplacée

Une haie indigène pauvre de 150 m sur 2 m borde une culture. Variante A : haie laissée en l'état. Variante B : haie renforcée (amélioration, état mauvais vers bon). Variante C : haie arrachée et replantée en haie riche (création).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 247,1 | 12 130 | 12 130 | -1,819 x 10^-12 | 0 | 0 | 100 | 100 |
| Variante B | 247,1 | 12 130 | 12 768 | -638 | 13 | 0 | 100 | 100 |
| Variante C | 247,1 | 12 130 | 12 337 | -207 | 375 | 0 | 100 | 100 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | FA.4 | 300 | 0,5 | 0,75 | 1 | 0,35 | 1 | 1 | 39,38 | 0 | 1 |
| P2 | I1.1 | 1 700 | 0,25 | 1 | 1 | 0,4888 | 1 | 1 | 207,74 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | FA.4 | 300 | 0,5 | 1 | 1 | 0,35 | 1 | 1 | 52,5 | 0 | 1 |
| P2 | I1.1 | 1 700 | 0,25 | 1 | 1 | 0,4888 | 1 | 1 | 207,74 | 0 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | FA.3 | 300 | 0,6667 | 0,9375 | 1 | 0,35 | 1 | 1 | 65,63 | 12 | 1 |
| P2 | I1.1 | 1 700 | 0,25 | 1 | 1 | 0,4888 | 1 | 1 | 207,74 | 0 | 1 |

#### Exemple de la fiche F12. Isolant biosourcé, bois d'œuvre et réemploi

Même bâtiment de 1 500 m² de S_ref. Variante A : isolation minérale. Variante B : isolation en fibre de bois (40 m³ de bois de plus, régime non justifié, et 30 kg CO2 éq./m² de moins en production). Variante C : structure de réemploi (60 kg CO2 éq./m² de moins, 1 000 t de granulats de moins).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 0 | 0 | 6 062 | -6 062 | 136 | 145 712 | 40 | 40 |
| Variante B | 0 | 0 | 6 062 | -6 062 | 136 | 215 720 | 40 | 40 |
| Variante C | 0 | 0 | 6 062 | -6 062 | 136 | 136 725 | 40 | 40 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 800 | 0,4583 | 0,8333 | 1 | 0,4141 | 1 | 1 | 126,53 | 1 | 1 |

#### Exemple de la fiche F13. Toiture : nue, extensive, biodiverse, intensive, biosolaire

Une toiture de 1 000 m² sur un bâtiment de 1 000 m² d'emprise. Variante A : toiture nue. B : extensive de 8 cm. C : biodiverse de 20 cm. D : intensive de 40 cm. E : biosolaire, 600 m² végétalisés en extensif hors emprise des panneaux.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Variante B | 0 | 0 | 4 671 | -4 671 | 103 | 0 | 25 | 0 |
| Variante C | 0 | 0 | 6 408 | -6 408 | 554 | 0 | 30 | 0 |
| Variante D | 0 | 0 | 5 127 | -5 127 | 252 | 0 | 35 | 0 |
| Variante E | 0 | 0 | 2 509 | -2 509 | 55 | 0 | 15 | 0 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.11 | 1 000 | 0,2639 | 0,8333 | 1 | 0,435 | 1 | 1 | 95,65 | 1 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.12 | 1 000 | 0,5278 | 1 | 1 | 0,435 | 1 | 1 | 229,57 | 10 | 0,67 |

Variante D, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.13 | 1 000 | 0,2639 | 1 | 1 | 0,435 | 1 | 1 | 114,78 | 5 | 1 |

Variante E, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.11 | 600 | 0,2639 | 0,8333 | 1 | 0,3887 | 1 | 1 | 51,29 | 1 | 1 |

#### Exemple de la fiche F14. Façade enracinée ou hors sol

Une façade de 40 m de long est végétalisée sur 10 m de haut (400 m²). Variante A : sans végétalisation. Variante B : plantes grimpantes enracinées au sol. Variante C : mur végétalisé hors sol.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Variante B | 0 | 0 | 1 013 | -1 013 | 34 | 0 | 8 | 0 |
| Variante C | 0 | 0 | 1 013 | -1 013 | 34 | 0 | 10 | 0 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.15 | 400 | 0,2639 | 0,8333 | 1 | 0,3555 | 1 | 1 | 31,28 | 3 | 0,67 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.16 | 400 | 0,2639 | 0,8333 | 1 | 0,3555 | 1 | 1 | 31,28 | 3 | 0,67 |

#### Exemple de la fiche F15. Mare naturelle, mare alimentée par le réseau, bassin

Un plan d'eau de 200 m² est créé dans une pelouse de 2 000 m². Variante A : mare à berges naturelles alimentée par la pluie. Variante B : même mare remplie par le réseau d'eau potable (convention C-E4). Variante C : bassin à eau traitée (VB.21).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 241,2 | 11 942 | 13 470 | -1 528 | 92 | 0 | 96 | 90 |
| Variante B | 241,2 | 11 942 | 12 926 | -984 | 74 | 0 | 96 | 90 |
| Variante C | 241,2 | 11 942 | 11 379 | 563 | 14 | 0 | 92 | 90 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.5 | 1 800 | 0,3333 | 0,7143 | 1 | 0,5066 | 1 | 1 | 217,09 | 0 | 1 |
| P2 | VB.20 | 200 | 0,625 | 0,8889 | 1 | 0,5066 | 1 | 1 | 56,29 | 3 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.5 | 1 800 | 0,3333 | 0,7143 | 1 | 0,5066 | 1 | 1 | 217,09 | 0 | 1 |
| P2 | VB.20 | 200 | 0,625 | 0,8889 | 1 | 0,5066 | 1 | 0,8 | 45,03 | 3 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.5 | 1 800 | 0,3333 | 0,7143 | 1 | 0,5066 | 1 | 1 | 217,09 | 0 | 1 |
| P2 | VB.21 | 200 | 0,2083 | 0,6111 | 1 | 0,5066 | 1 | 1 | 12,9 | 1 | 1 |

#### Exemple de la fiche F16. Éclairage de la prairie : aucun, conforme, permanent

Une prairie urbaine de 1 200 m² est créée à côté d'un stationnement éclairé. Variantes A, B et C : classes d'éclairage L0, L1 et L2 (fiche A20).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 253,3 | 12 409 | 7 063 | 5 346 | 622 | 0 | 60 | 60 |
| Variante B | 253,3 | 12 409 | 6 470 | 5 939 | 569 | 0 | 60 | 60 |
| Variante C | 253,3 | 12 409 | 5 297 | 7 112 | 466 | 0 | 60 | 60 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.2 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.26 | 1 200 | 0,625 | 0,8333 | 1 | 0,4528 | 1 | 1 | 282,97 | 5 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.2 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.26 | 1 200 | 0,625 | 0,8333 | 1 | 0,4528 | 0,916 | 1 | 259,21 | 5 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.2 | 800 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.26 | 1 200 | 0,625 | 0,8333 | 1 | 0,4528 | 0,75 | 1 | 212,23 | 5 | 1 |

#### Exemple de la fiche F17. Jardins clos par une clôture étanche ou perméable

Des jardins de 1 500 m² sont clos. Variante A : clôture perméable (passages de 15 x 15 cm tous les 20 m). Variante B : clôture étanche (convention C-C3).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 253,3 | 12 409 | 13 053 | -644 | 293 | 0 | 75 | 75 |
| Variante B | 253,3 | 12 409 | 11 747 | 661 | 263 | 0 | 75 | 75 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 500 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.7 | 1 500 | 0,4583 | 0,8333 | 1 | 0,4755 | 1 | 1 | 272,42 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 500 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.7 | 1 500 | 0,4583 | 0,8333 | 1 | 0,428 | 1 | 1 | 245,18 | 1 | 1 |

#### Exemple de la fiche F20. Stationnement en enrobé, en pavés drainants ou en dalles engazonnées

Un stationnement de 1 000 m² est aménagé sur une pelouse de 2 000 m². Variantes A, B et C : enrobé (VB.2), pavés à joints sablés (VB.3), dalles alvéolées engazonnées (VB.4).

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 241,2 | 11 942 | 5 127 | 6 816 | 0 | 0 | 50 | 50 |
| Variante B | 241,2 | 11 942 | 8 679 | 3 263 | 73 | 0 | 60 | 50 |
| Variante C | 241,2 | 11 942 | 7 791 | 4 152 | 54 | 0 | 72,5 | 50 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.2 | 1 000 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 0 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.3 | 1 000 | 0,1667 | 1 | 1 | 0,435 | 1 | 1 | 72,51 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 0 | 1 |

Variante C, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.4 | 1 000 | 0,125 | 1 | 1 | 0,435 | 1 | 1 | 54,37 | 0 | 1 |
| P2 | VB.5 | 1 000 | 0,3333 | 0,7143 | 1 | 0,435 | 1 | 1 | 103,55 | 0 | 1 |

#### Exemple de la fiche F22. État initial après débroussaillage préalable

Une prairie de fauche en bon état a été labourée un an avant le dépôt. Variante A : état initial saisi tel que constaté (culture). Variante B : état antérieur documenté, comme l'impose la convention C-R5.

| Variante | V_0 | I_0 | I_1 | Cnat | Dette | Inat | Bnat | Pleine terre (%) |
|---|---|---|---|---|---|---|---|---|
| Variante A | 337,7 | 16 543 | 7 959 | 8 584 | 178 | 0 | 50 | 50 |
| Variante B | 773,9 | 37 914 | 7 959 | 29 955 | 178 | 0 | 50 | 50 |

Variante A, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 1 000 | 0,4583 | 0,8333 | 1 | 0,435 | 1 | 1 | 166,12 | 1 | 1 |

Variante B, unités de l'état projet :

| Unité | Type | A (m²) | v | f | f_sol | k_C | k_N | k_E | V | d | D |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | VB.1 | 600 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P2 | VB.2 | 400 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| P3 | VB.7 | 1 000 | 0,4583 | 0,8333 | 1 | 0,435 | 1 | 1 | 166,12 | 1 | 1 |
