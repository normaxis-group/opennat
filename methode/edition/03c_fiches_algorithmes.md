### 3.8 Module T : temps

#### Fiche A26. Calendrier et chantier

**Introduction**

La simulation suit l'opération année par année sur 50 ans. L'année 1 commence avec le chantier. La fiche calcule, pour chaque année, la part occupée par le chantier et le temps écoulé depuis sa fin.

**Nomenclature**

Entrées : d_ch (fiche A05 ou saisie), en années, réel positif.

Variables internes et sorties :

| Nom | Description | Unité |
|---|---|---|
| φ_t | Part de l'année t occupée par le chantier | sans unité, 0 à 1 |
| τ_t | Temps écoulé depuis la fin du chantier, à la fin de l'année t | an |

**Description mathématique**

(A26-1) φ_t = min(1 ; max(0 ; d_ch - (t - 1))) [T1]

(A26-2) τ_t = t - d_ch

Le calcul se fait au pas mensuel (fiche A58) : φ_m = 1 pour chaque mois du chantier, 0 ensuite ; φ_t est la moyenne annuelle de φ_m. Le départ de la maturation des unités créées n'est plus la fin du chantier mais le premier mois favorable aux plantations (fiche A58) ; τ_t ne sert qu'aux unités sans délai.

**Cas limites et contrôles**

d_ch = 0 (aménagement sans chantier lourd) : φ_t = 0 pour tout t et τ_t = t. Un chantier de plus de 10 ans est signalé au journal ; une opération phasée se calcule par phases (fiche d'application F05).

**Cas élémentaire**

d_ch = 1,5 : φ_1 = 1 ; φ_2 = 0,5 ; φ_3 = 0 ; τ_1 = -0,5 ; τ_2 = 0,5 ; τ_3 = 1,5.

**Renvois**

Convention C-T1.

#### Fiche A27. Unités conservées

**Introduction**

Une unité conservée garde sa valeur, diminuée pendant le chantier quand aucune mesure de protection n'est prévue.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| V_u | Valeur à maturité de l'unité à l'état projet (fiche A25) | m²HE | 0 et plus |
| prot_u | Protection prévue pendant le chantier | booléen | oui, non |

Paramètres intrinsèques : r_ch = 0,25 (`contexte.csv`, `reduction_chantier_sans_protection`).

Sorties : V_u(t) pour t de 1 à N.

**Description mathématique**

(A27-1) r_u = 0 si prot_u ; r_ch sinon

(A27-2) V_u(t) = V_u x (1 - r_u x φ_t) [T2]

La valeur V_u d'une unité conservée est calculée avec les facteurs de l'état projet : si le projet isole une prairie conservée (taille de tache plus faible) ou l'éclaire, sa valeur baisse dès la fin du chantier.

**Cas limites et contrôles**

Une protection se justifie par le plan d'installation de chantier : clôture fixe, balisage, interdiction de stockage, de circulation et de dépôt de terre dans l'emprise protégée et sous le houppier des arbres.

**Cas élémentaire**

Prairie conservée, V_u = 100 m²HE, sans protection, d_ch = 1,5 : V(1) = 75 ; V(2) = 87,5 ; V(3) et suivantes = 100.

**Renvois**

Convention C-T4. Fiche d'application F09.

#### Fiche A28. Unités créées et maturation

**Introduction**

Un habitat créé part de zéro à la fin du chantier et gagne sa valeur cible, pondérée par sa probabilité de réussite, en un délai propre à son type et à l'état visé.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| V_u | Valeur à maturité visée (fiche A25, état visé) | m²HE | 0 et plus |
| cl_u | Classe d'état visée (fiche A12) | énumération | bon, moyen, mauvais, sans état |

Paramètres intrinsèques :

| Nom | Description | Unité | Origine |
|---|---|---|---|
| d(h, cl) | Délai de maturité | an | `habitats.csv`, `delai_maturite_*` |
| D_c(h) | Difficulté de création | sans unité | `habitats.csv`, `difficulte_creation` |
| k_delai | Multiplicateur de délai de la zone | sans unité | fiche A02 |

Variables internes :

| Nom | Description | Unité |
|---|---|---|
| d_u | Délai retenu | an |
| g_u(t) | Part de maturité atteinte | sans unité, 0 à 1 |

Sorties : V_u(t).

**Description mathématique**

(A28-1) d_u = k_delai x d(h_u, cl_u) ; si le type n'a qu'un délai « sans état », d_u = k_delai x d(h_u, sans état) ; si le type n'a aucun délai, d_u = 0 (convention C-T3).

(A28-2) g_u = courbe de maturation de la fiche A54, τ étant compté au mois près depuis le départ fixé par la fiche A58 ; la droite min(1 ; τ / d_u) de la première rédaction est remplacée.

(A28-3) V_u(t) = D_c(h_u) x V_u x g_u(t) [T3]

Si le délai pour la classe visée n'existe pas (« Not Possible » de la métrique anglaise), l'état visé est hors d'atteinte par création : le calcul retient la meilleure classe accessible inférieure et l'écrit au journal.

**Cas limites et contrôles**

Une unité créée sur l'emprise d'une unité initiale détruite ne reprend rien de sa valeur : la destruction et la création sont deux écritures distinctes (fiche A31). Un habitat transplanté (placage de prairie, déplacement de mare) est une unité créée, sauf justification d'une amélioration (fiche A29).

**Cas élémentaire**

Prairie urbaine VB.26 de l'annexe C, V_u = 90,10, classe moyen, d = 5 ans, D = 1, chantier de 18 mois commencé en septembre, plantée en janvier (rang 17) : moyennes annuelles 12,40 l'année 2 ; 48,21 l'année 3 ; 69,24 l'année 4 ; 87,12 l'année 6 ; 90,10 à partir de l'année 8, avant facteurs hydrique et de gestion.

**Renvois**

Conventions C-T1, C-T2, C-T3, C-T7, C-E2, C-M1, C-K2. Fiches A54, A58.

#### Fiche A29. Unités améliorées

**Introduction**

Une unité améliorée garde son type mais passe d'une classe d'état à une meilleure, en un délai et avec une difficulté propres à l'amélioration.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| V_u,0 | Valeur de l'unité initiale liée, avec les facteurs de l'état initial | m²HE | 0 et plus |
| V_u | Valeur visée, avec les facteurs de l'état projet | m²HE | 0 et plus |
| cl_0, cl_u | Classes initiale et visée | énumération | mauvais, moyen, bon |

Paramètres intrinsèques : d_a(h, cl_0, cl_u) (`habitats.csv`, `delai_amelioration_*`), D_a(h) (`difficulte_amelioration`).

Sorties : V_u(t).

**Description mathématique**

(A29-1) d_u = k_delai x d_a(h_u, cl_0, cl_u)

(A29-2) Si D_a x V_u > V_u,0 : V_u(t) = V_u,0 x (1 - r_u x φ_t) + (D_a x V_u - V_u,0) x g_u(t), avec g_u défini comme en (A28-2) [T4]

(A29-3) Sinon : V_u(t) = V_u,0 x (1 - r_u x φ_t)

r_u suit la fiche A27 : une unité améliorée est aussi une unité conservée pendant le chantier.

**Cas limites et contrôles**

Une amélioration qui change le type (une pelouse devenue prairie fleurie) est une création sur une unité détruite, pas une amélioration. Une amélioration sans gain (D_a x V_u <= V_u,0) garde la valeur initiale.

**Cas élémentaire**

Prairie de fauche E2.2 de 1 000 m², mauvais état (S = 0,4) vers bon état (S = 0,9), v = 20 / 24 = 0,8333, k = 1 : V_u,0 = 1 000 x 0,8333 x 0,7 = 583,3 ; V_u = 1 000 x 0,8333 x 0,95 = 791,7 ; D_a = 0,67 ; D_a x V_u = 530,4 < 583,3 : pas de gain retenu. L'écart montre le poids de la difficulté d'amélioration de la métrique anglaise pour les prairies riches.

**Renvois**

Conventions C-T4, C-T7.

#### Fiche A30. Renouvellements

**Introduction**

Certaines unités sont refaites pendant la période : toiture végétalisée reprise lors de la réfection de l'étanchéité, massif replanté. La fiche les traite comme une destruction suivie d'une nouvelle création.

**Nomenclature**

Entrées : années de réfection R_{u,1}, R_{u,2}... (entiers de 2 à N).

Paramètres intrinsèques : durée d'indisponibilité d_ind = 1 an (`contexte.csv`).

Sorties : V_u(t) modifiée.

**Description mathématique**

(A30-1) Pour chaque réfection R : V_u(t) = 0 pour R <= t < R + d_ind

(A30-2) Après réfection, la maturation recommence : V_u(t) = D_c x V_u x min(1 ; (t - R - d_ind + 1) / d_u) pour t >= R + d_ind

**Cas limites et contrôles**

Une réfection de toiture prévue dans le plan d'entretien (par exemple tous les 25 à 30 ans pour une étanchéité) doit être saisie. Les remplacements de matériaux qui l'accompagnent entrent dans le module G (fiche A34, nombre de remplacements).

**Cas élémentaire**

Toiture biodiverse VB.12, D = 0,67, V = 98,55, d = 10, refaite l'année 30 : V(29) = 66,03 ; V(30) = 0 ; V(31) = 6,60 ; V(40) = 66,03.

**Renvois**

Convention C-T6.

#### Fiche A31. Intégration, dette de maturité et sorties temporelles

**Introduction**

La fiche additionne les trajectoires et produit les valeurs intégrées du site avec et sans projet, la dette de maturité et les sorties à 30 ans.

**Nomenclature**

Entrées : V_u et k_W,u(t) des unités de l'état initial ; V_u(t) des unités de l'état projet (fiches A27 à A30, multipliées par k_W,u(t) et f_g,u(t)) ; N, N30.

Sorties :

| Nom | Description | Unité |
|---|---|---|
| V_0 | Valeur du site sans projet | m²HE |
| V_1(t) | Valeur du site avec projet, année t | m²HE |
| I_0, I_1 | Valeurs intégrées sur N ans | m²HE·an |
| I_0,30, I_1,30 | Valeurs intégrées sur 30 ans | m²HE·an |
| DM | Dette de maturité | m²HE·an |

**Description mathématique**

(A31-1) V_0 = somme des V_u de l'état initial

(A31-2) V_1(t) = somme des V_u(t) de l'état projet (conservées, créées, améliorées)

(A31-3) I_0 = somme pour t de 1 à N des V_u x k_W,u(t) de l'état initial ; I_1 = somme pour t de 1 à N de V_1(t) [T7]. L'état initial subit le même climat que le projet (fiche A50).

(A31-4) I_0,30 et I_1,30 : mêmes sommes sur 30 ans

(A31-5) DM = somme pour t de 1 à N, sur les unités créées et améliorées, de (D x V_u - moyenne annuelle des valeurs mensuelles), avant facteurs hydrique et de gestion [T8]

Les unités initiales détruites (ni conservées ni améliorées) n'apparaissent pas dans V_1(t) : leur perte est dans l'écart I_0 - I_1.

**Cas limites et contrôles**

Option d'étude inactive (convention C-T5) : avec un taux d'actualisation a, chaque terme annuel est multiplié par (1 - a)^t, et I_0 devient la somme actualisée de V_0.

**Cas élémentaire**

Voir l'annexe C de la partie 1 : V_0 = 270,39 ; I_0 = 13 277,1 ; I_1 = 10 059,9 ; DM = 673,1 m²HE·an.

**Renvois**

Conventions C-T1, C-T5.

### 3.9 Module G : biodiversité grise

#### Fiche A32. Lecture des indicateurs d'ACV

**Introduction**

Le module G lit dans le RSEE les émissions de gaz à effet de serre et les indicateurs de pollution des contributeurs « composants » et « chantier », par phase du cycle de vie.

**Nomenclature**

Entrées : ges_{c,p,b}, pol_{i,c,p,b}, S_ref,b (fiche A05).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| GES_p | Émissions des composants et du chantier, phase p, par m² de S_ref | kg CO2 éq./m² |
| POL_{i,p} | Indicateur de pollution i, phase p, par m² de S_ref | unités de l'annexe II |

**Description mathématique**

(A32-1) GES_p = (somme sur b et c de ges_{c,p,b} x S_ref,b) / S_ref, c dans {composant, chantier}

(A32-2) POL_{i,p} = (somme sur b et c de pol_{i,c,p,b} x S_ref,b) / S_ref, i dans {106, 107, 108, 109, 116}

Phases : A1-A3 (production), A4-A5 (transport et chantier), B (exploitation : remplacements et entretien), C (fin de vie), D (au-delà du cycle de vie, lu mais non utilisé).

**Cas limites et contrôles**

Les indicateurs du RSEE sont statiques (non pondérés dans le temps) ; l'Ic construction de la RE2020 est dynamique. OpenNAT lit l'indicateur statique 101 et applique sa propre pondération temporelle (fiche A33). Sans RSEE, les GES_p se saisissent depuis l'étude ACV du projet.

**Cas élémentaire**

Un RSEE donne, pour un bâtiment, 353,9 (A1-A3), 123,8 (A4-A5), 406,8 (B), 57,0 (C) kg CO2 éq./m² sur l'indicateur 101 du bâtiment ; les contributeurs énergie et eau étant exclus, OpenNAT retient leur part composants et chantier.

**Renvois**

Annexe II de l'arrêté du 4 août 2021. Convention C-G1.

#### Fiche A33. Composante climat

**Introduction**

Les émissions de gaz à effet de serre des matériaux et du chantier réchauffent le climat, ce qui réduit l'abondance des espèces sur les terres émergées. La fiche convertit ces émissions en perte d'habitat équivalent.

**Nomenclature**

Entrées : GES_p (fiche A32), S_ref.

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| S_terres | Surface terrestre libre de glace | m² | 1,30 x 10^14 |
| p_cult | Part des cultures et infrastructures | sans unité | 0,13 |
| π | Perte de MSA par °C, médiane des biomes | MSA/°C | 0,071 |
| δ | Facteur de retard de réponse | sans unité | 2 |
| TCRE | Réchauffement par kg de CO2 émis | °C/kg | 4,5 x 10^-16 |
| a_p | Années de persistance de la phase p | an | 50, 50, 25, 0, 0 |

Variables internes : CF (m²HE par kg CO2 éq. : habitat équivalent perdu chaque année tant que le réchauffement persiste).

Sorties : Inat_clim, Inat_clim,p (m²HE·an).

**Description mathématique**

(A33-1) CF = S_terres x (1 - p_cult) x (π / δ) x TCRE [G3]

(A33-2) Inat_clim,p = CF x S_ref x GES_p x a_p

(A33-3) Inat_clim = somme sur les phases de Inat_clim,p [G2]

Numériquement : CF = 1,30 x 10^14 x 0,87 x 0,0355 x 4,5 x 10^-16 = 1,807 x 10^-3 m²HE par kg, perdus chaque année de persistance. Un kg de CO2 émis en début de période coûte 50 x 1,807 x 10^-3 = 0,0903 m²HE·an.

**Cas limites et contrôles**

Le facteur ne dépend pas du lieu de l'opération : le réchauffement est global. Il ne s'applique qu'au CO2 éq. des contributeurs composants et chantier : les consommations d'énergie en exploitation relèvent de l'Ic énergie de la RE2020, pas d'Inat.

**Cas élémentaire**

S_ref = 1 400 m² ; GES : A1-A3 350, A4-A5 120, B 400, C 55 : somme des GES_p x a_p = 470 x 50 + 400 x 25 = 33 500 kg·an/m² ; Inat_clim = 1,807 x 10^-3 x 1 400 x 33 500 = 84 748 m²HE·an.

**Renvois**

`materiaux.csv`. Conventions C-G2, C-G3. Décision du 18/10/2026 sur le point P19.

#### Fiche A34. Bois et occupation des forêts

**Introduction**

Le bois mis en œuvre occupe pendant sa croissance une surface de forêt dont la qualité d'habitat dépend du régime d'exploitation. La fiche calcule cette occupation et la perte d'habitat qui en résulte.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| Q_r | Volume de bois mis en œuvre du régime r | m³ | 0 et plus |
| n_remp,r | Nombre de remplacements pendant N ans | entier | 0 et plus |
| justif_r | Pièce qui justifie le régime | texte | facultative |

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| P | Production biologique des forêts françaises | m³/ha/an | 5,4 |
| R | Bois rond par m³ de produit | m³/m³ | 2 |
| MSA_r | Qualité d'habitat de la forêt d'origine | MSA | 0,30 ; 0,50 ; 0,70 ; 0,85 |

Variables internes : O_bois (m²·an par m³).

Sorties : Inat_bois (m²HE·an).

**Description mathématique**

(A34-1) O_bois = 10 000 x R / P

(A34-2) r = régime déclaré si justif_r est fournie ; coupe rase sinon (convention C-G5)

(A34-3) Inat_bois = somme sur r de Q_r x (1 + n_remp,r) x O_bois x (1 - MSA_r) [G4]

**Cas limites et contrôles**

Les panneaux et produits reconstitués (OSB, fibres, lamellé-collé) comptent par leur volume de bois ; le liège, la paille et les autres biosourcés ne sont pas couverts en v1 (fiche d'application F12). Le bois de réemploi ne compte pas.

**Cas élémentaire**

30 m³ de bois, régime non justifié : O_bois = 3 703,7 m²·an/m³ ; Inat_bois = 30 x 3 703,7 x 0,5 = 55 556 m²HE·an. Avec une coupe sélective justifiée : 33 333.

**Renvois**

`materiaux.csv`. Conventions C-G4, C-G5. Point P5 de l'audit.

#### Fiche A35. Carrières et autres matériaux

**Introduction**

Les granulats, sables et roches occupent les sols des carrières. Les autres matériaux sont négligés en v1, faute d'inventaire ouvert.

**Nomenclature**

Entrées : M (masse de granulats, sables et roches, t), n_remp.

Paramètres intrinsèques : o_c = 0,9 m²·an/t ; MSA_c = 0,05.

Sorties : Inat_carr (m²HE·an).

**Description mathématique**

(A35-1) Inat_carr = M x (1 + n_remp) x o_c x (1 - MSA_c) [G5]

(A35-2) Inat_sols = Inat_bois + Inat_carr [G6]

La masse de granulats d'un béton se déduit de son volume : environ 1,8 à 1,9 t de granulats par m³ de béton courant, valeur à prendre dans la formulation du projet.

**Cas limites et contrôles**

Les granulats recyclés ne comptent pas. L'occupation des usines (acier, verre, plâtre, isolants, plastiques) est négligée (convention C-G7) : c'est l'écart connu principal du module.

**Cas élémentaire**

1 800 t : Inat_carr = 1 800 x 0,9 x 0,95 = 1 539 m²HE·an.

**Renvois**

Conventions C-G6, C-G7.

#### Fiche A36. Indicateurs de pollution

**Introduction**

L'acidification, l'eutrophisation et l'écotoxicité nuisent aux écosystèmes. Chaque indicateur du RSEE est converti en habitat équivalent perdu par un facteur publié (convention C-G8) et ajouté à Inat ; le détail par indicateur reste affiché.

**Nomenclature**

Entrées : POL_{i,p} (fiche A32).

Sorties : POL_i = somme sur les phases A1-A3, A4-A5, B et C de POL_{i,p} x S_ref, pour i = 106 (mol H+ éq.), 107 (kg P éq.), 108 (kg N éq.), 109 (mol N éq.), 116 (CTUe).

**Description mathématique**

(A36-1) POL_i = S_ref x somme des POL_{i,p} pour p hors D

(A36-2) Inat_pol = somme sur i de POL_i x F_i

**Cas limites et contrôles**

Les indicateurs ne s'additionnent qu'après conversion par leur facteur F_i ; un indicateur absent du RSEE compte pour zéro.

**Cas élémentaire**

POL_116 de 1,82 CTUe/m² pour 1 400 m² : 2 548 CTUe, soit Inat_pol = 2 548 x 5,479 x 10^-4 = 1,40 m²HE·an.

**Renvois**

Convention C-G8.
