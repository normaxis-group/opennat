### 3.13 Modules dynamiques : climat, bilan hydrique, éclairage, maturation, gestion et chantier

Les fiches A43 à A58 décrivent les calculs qui font d'OpenNAT une simulation et non un barème : le climat horaire et son évolution sur la période, le bilan hydrique horaire de chaque unité végétalisée, l'éclairage nocturne heure par heure, la courbe de maturation, la gestion et la succession, le calendrier du chantier au pas mensuel. Elles complètent les fiches A20 (lumière), A26 (calendrier), A28 (maturation) et A31 (intégration), dont elles remplacent les équations simplifiées de la première rédaction.

Ordre d'appel : A43 à A46 une fois par projet et par niveau de réchauffement ; A47 à A50 pour chaque unité végétalisée de l'état initial et de l'état projet ; A51 à A53 dans le module N, à la place de l'équation A20-2 ; A54 à A58 dans le module T.

#### Fiche A43. Climat horaire conventionnel

**Introduction**

Le calcul a besoin d'un climat horaire : pluie, température, humidité, vent, rayonnement, hauteur du soleil. Comme la RE2020, OpenNAT emploie une année météorologique type par zone climatique. Les fichiers de la RE2020 ne sont pas employés : le ministère en réserve l'usage au calcul réglementaire RE2020. OpenNAT emploie les fichiers climatiques prospectifs publiés en juin 2025 par l'ADEME, Météo-France, le CSTB et la DHUP sous Licence Ouverte 2.0, aux trois niveaux de la TRACC.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| zone | Zone climatique RE2020 du département du projet | énumération | H1a, H1b, H1c, H2a, H2b, H2c, H2d, H3 |
| z_site | Altitude du site (RSET, `Simu/Altitude`) | m | 0 à 2 500 |
| n | Niveau de réchauffement | énumération | +2 ; +2,7 ; +4 °C |

Paramètres intrinsèques :

| Nom | Description | Unité | Origine |
|---|---|---|---|
| station(zone), z_st | Station de référence et son altitude | m | `climat.csv`, `station_*` |
| T2m, Hur, RR, FF, Tc, Rgh, Ps, Hs | Variables horaires de l'année type | °C, %, mm, m/s, °C, W/m², hPa, degré | `donnees/climat/tracc_<n>.csv.gz` |

Constantes : gradient thermique de l'atmosphère type Γ = 0,0065 K/m (norme ISO 2533).

Sorties : pour chaque heure h de l'année type (8 760 heures, en temps universel) : T(h), P(h), Hur(h), u_10(h), R_s(h), p_atm(h), H_s(h).

**Description mathématique**

(A43-1) Δz = z_site - z_st ; si z_site est inconnu, Δz = 0

(A43-2) T(h) = T2m(h) - Γ x Δz

(A43-3) p_atm(h) = Ps(h) / 10 x ((293 - Γ x Δz) / 293)^5,26 (kPa, forme de l'équation 7 de la FAO-56)

(A43-4) L'humidité relative est celle de la station : e_a(h) = e°(T(h)) x Hur(h) / 100.

(A43-5) P(h) = RR(h) x ρ_mois (fiche A45)

**Cas limites et contrôles**

Un site à plus de 800 m d'altitude reste calculé sur la station de sa zone, corrigée ; l'écart est écrit au journal. Les fichiers prospectifs ont 8 760 heures (année non bissextile) ; une heure manquante arrête le calcul.

**Cas élémentaire**

Trappes (H1a, 167 m), +2 °C, 15 juillet à 12 h UTC : T2m = 21,61 °C. Pour un site à 300 m, Δz = 133 m et T = 21,61 - 0,0065 x 133 = 20,75 °C.

**Renvois**

Conventions C-W1, C-W13. Table `climat.csv`. Fiche A44.

#### Fiche A44. Évapotranspiration de référence horaire

**Introduction**

L'évapotranspiration de référence ET0 est la demande en eau de l'atmosphère, mesurée sur un gazon de référence bien alimenté. La fiche l'obtient heure par heure par l'équation de Penman-Monteith de la FAO-56 (Allen et al., 1998).

**Nomenclature**

Entrées : sorties de la fiche A43.

Constantes : albédo 0,23 ; constante solaire G_sc = 4,92 MJ/m²/h ; constante de Stefan-Boltzmann horaire σ = 2,043 x 10^-10 MJ/K⁴/m²/h.

Variables internes : e°(T), Δ, γ, u_2, R_s, R_so, R_ns, R_nl, R_n, G.

Sorties : ET0(h), en mm.

**Description mathématique**

(A44-1) e°(T) = 0,6108 x exp(17,27 T / (T + 237,3)) ; Δ = 4 098 e°(T) / (T + 237,3)² ; γ = 0,665 x 10^-3 x p_atm

(A44-2) u_2 = u_10 x 4,87 / ln(67,8 x 10 - 5,42) (vent ramené à 2 m, équation 47)

(A44-3) R_s = 0,0036 x Rgh ; R_a = G_sc x d_r x sin(H_s) quand H_s > 0, avec d_r = 1 + 0,033 cos(2π J / 365) ; R_so = (0,75 + 2 x 10^-5 x z_site) x R_a

(A44-4) R_ns = 0,77 x R_s ; R_nl = σ (T + 273,16)⁴ (0,34 - 0,14 √e_a) (1,35 R_s / R_so - 0,35), le rapport R_s / R_so étant borné entre 0,3 et 1 et gardé la nuit à sa dernière valeur relevée avec un soleil à plus de 10° (équations 37 à 39)

(A44-5) R_n = R_ns - R_nl ; G = 0,1 R_n le jour (H_s > 0), 0,5 R_n la nuit (équations 45 et 46)

(A44-6) ET0 = max(0 ; [0,408 Δ (R_n - G) + γ (37 / (T + 273,16)) u_2 (e°(T) - e_a)] / [Δ + γ (1 + 0,34 u_2)]) (équation 53)

**Cas limites et contrôles**

Les valeurs négatives (rosée) sont ramenées à 0. Contrôle : l'ET0 annuelle à +2 °C vaut de 0,86 à 1,00 fois l'ETP Penman normale 1991-2020 de Météo-France aux huit stations (`climat.csv`, `etp_penman_normale`) ; un écart hors de 0,8 à 1,1 est signalé.

**Cas élémentaire**

Trappes, +2 °C, 15 juillet à 12 h UTC : Rgh = 592,9 W/m², T = 21,61 °C, Hur = 72,8 %, u_10 = 1,99 m/s : ET0 = 0,375 mm. Journée du 15 juillet : 2,9 mm ; mois de juillet : 109,7 mm ; année : 666 mm (693 mm à +2,7 °C, 776 mm à +4 °C ; ETP Penman normale de Météo-France : 772 mm).

**Renvois**

Convention C-W2. FAO-56, chapitre 4.

#### Fiche A45. Recalage des pluies

**Introduction**

La note technique des fichiers prospectifs signale que leurs cumuls de pluie s'approchent des maxima des simulations, faute d'années types choisies sur ce critère. Un bilan hydrique calculé tel quel sous-estimerait le stress. La fiche recale les pluies horaires sur les normales mensuelles observées.

**Nomenclature**

Entrées : RR(h) de la fiche A43.

Paramètres intrinsèques : P_norm,mois(zone), normale mensuelle 1991-2020 de la station (`climat.csv`, `pluie_normale_m01` à `m12`, données climatologiques de base mensuelles de Météo-France).

Sorties : ρ_mois, P(h).

**Description mathématique**

(A45-1) ρ_mois = P_norm,mois / somme des RR(h) du mois dans l'année type ; ρ_mois = 0 si le mois est sec dans l'année type

(A45-2) P(h) = RR(h) x ρ_mois

Le recalage garde la chronologie des averses et leur intensité relative ; il ne change pas avec le niveau de réchauffement (convention C-W3).

**Cas limites et contrôles**

Un mois sans pluie dans l'année type reste sec, quelle que soit la normale : l'écart est écrit au journal.

**Cas élémentaire**

Trappes, +2 °C, juillet : l'année type porte 148,9 mm, la normale 56,2 mm ; ρ_07 = 0,3776. Sur l'année, 981 mm deviennent 685 mm.

**Renvois**

Convention C-W3. Table `climat.csv`.

#### Fiche A46. Climat de chaque année de la période

**Introduction**

La période de 50 ans traverse le réchauffement. La fiche affecte à chaque année civile un niveau de réchauffement de la TRACC et les poids des trois années types.

**Nomenclature**

Entrées : a_0, année de début du chantier (fiche A58).

Paramètres : jalons de la TRACC (arrêté du 23 janvier 2026) : (2030 ; +2 °C), (2050 ; +2,7 °C), (2100 ; +4 °C).

Sorties : ΔT(a) et poids w_n(a) pour a de a_0 à a_0 + 49.

**Description mathématique**

(A46-1) ΔT(a) = 2 si a <= 2030 ; interpolation linéaire entre les jalons sinon

(A46-2) Si ΔT <= 2,7 : w_2,7 = (ΔT - 2) / 0,7 ; w_2 = 1 - w_2,7 ; w_4 = 0. Sinon : w_4 = (ΔT - 2,7) / 1,3 ; w_2,7 = 1 - w_4 ; w_2 = 0.

(A46-3) Une grandeur X calculée sur les trois années types vaut, l'année a : X(a) = somme des w_n(a) x X_n.

**Cas limites et contrôles**

Une révision de la TRACC change les jalons sans changer la fiche. Au-delà de 2100, ΔT reste à +4 °C.

**Cas élémentaire**

a_0 = 2027 : 2027 à 2030, +2 °C ; 2035, +2,175 °C (0,75 et 0,25) ; 2040, +2,35 °C ; 2050, +2,7 °C ; 2064, +3,064 °C (0,72 à +2,7 °C, 0,28 à +4 °C) ; 2076, +3,376 °C (0,48 et 0,52).

**Renvois**

Convention C-W13.

#### Fiche A47. Groupes hydriques

**Introduction**

Chaque unité végétalisée a besoin d'eau selon sa végétation. La fiche range les unités dans neuf groupes hydriques, dont la table `hydrique.csv` donne les coefficients.

**Nomenclature**

Entrées : code h_u, position, alimentation déclarée des milieux humides.

Sorties : groupe g_u ou « sans bilan ».

**Description mathématique**

(A47-1) Sans bilan : surfaces minérales et scellées (VB.1 à VB.4, VB.10, VB.25, H5.6), bassins à eau traitée et bassins de rétention (VB.21, VB.24), façades (VB.15, VB.16), groupe J, cultures temporaires I2, cours d'eau, milieux humides et prairies humides (C2, C3, D, E3) alimentés par une nappe ou un cours d'eau.

(A47-2) Mare : VB.20 et C1. Milieu humide alimenté par la pluie : VB.19, et les types C2, C3, D, E3 déclarés alimentés par la pluie. Toiture extensive : VB.11. Gazon : VB.5, VB.22. Végétation xérophile : E1, F5, F6, H. Conifères : G3. Arboré : G (hors G3), VB.18a, VB.18b. Arbustif : F (hors F5, F6), FA, FB, VB.6, VB.9. Prairie : tous les autres types végétalisés, dont VB.7, VB.8, VB.12, VB.13, VB.23, VB.26, E2, E4 à E7, I1.

**Cas limites et contrôles**

Un type nouveau de la nomenclature sans groupe explicite tombe dans le groupe prairie : le journal le signale.

**Cas élémentaire**

VB.26, prairie ; FA.3, arbustif ; VB.18a, arboré ; VB.12 (toiture biodiverse), prairie sur substrat ; E3.4 déclarée alimentée par la nappe, sans bilan.

**Renvois**

Convention C-W6. Table `hydrique.csv`.

#### Fiche A48. Réserve utile

**Introduction**

La réserve utile est l'eau que le sol ou le substrat retient et que les racines peuvent prendre. Elle dépend de la texture, de la profondeur d'enracinement et, hors sol, de l'épaisseur du substrat.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| tex | Classe de texture (unité ou site) | énumération | neuf classes du tableau 19 de la FAO-56 |
| prof | Profondeur de sol (unité ou site) | m | 0,1 à 3 |
| e_u | Épaisseur de substrat | cm | positions sur dalle et hors-sol |

Paramètres intrinsèques : θ_cc(tex), θ_pf(tex), Z_r(g), réserve volumique du substrat (`hydrique.csv`).

Sorties : RU_u en mm.

**Description mathématique**

(A48-1) Sur dalle et hors sol : RU_u = 10 x e_u x 0,20

(A48-2) En pleine terre : RU_u = 1 000 x (θ_cc - θ_pf) x min(Z_r(g_u) ; prof) ; à défaut de déclaration, tex = limon et prof = 1 m (convention C-W4).

**Cas limites et contrôles**

Un arbre planté en fosse sur dalle se déclare sur dalle avec l'épaisseur de la fosse. Une réserve nulle (substrat absent) donne un stress maximal : le facteur hydrique tombe au plancher.

**Cas élémentaire**

Prairie sur limon d'un mètre : 1 000 x (0,25 - 0,12) x 1 = 130 mm. Arbre sur sable : 1 000 x (0,12 - 0,045) x min(1,5 ; 1) = 75 mm. Toiture de 15 cm : 30 mm. Haie sur argile de 60 cm : 1 000 x (0,36 - 0,22) x 0,6 = 84 mm.

**Renvois**

Conventions C-W4, C-W5. FAO-56, tableaux 19 et 22.

#### Fiche A49. Bilan hydrique horaire

**Introduction**

La fiche suit, heure par heure, l'eau du réservoir de chaque unité : la pluie et les apports de ruissellement le remplissent, l'évapotranspiration le vide, l'excédent percole. Elle en tire l'indice de stress de Granier, le volume d'arrosage et, pour une mare, la tenue en eau.

**Nomenclature**

Entrées : P(h), ET0(h), T(h) (fiches A43 à A45) ; RU_u (A48) ; g_u (A47) ; arrosage déclaré ; surfaces raccordées S_imp et S_perm ; pour une mare, profondeur H et nature du fond.

Paramètres intrinsèques : K_c saison, K_c hors saison, p (`hydrique.csv`) ; seuil de stress REW = 0,4 ; seuil d'arrosage 0,5 ; coefficients de ruissellement 0,9 et 0,1 ; infiltration du fond (0 ; 0,3 ; 1 mm/j) ; saison de végétation (5 °C sur six jours).

Variables internes : D(h) déplétion, REW(h), K_s(h), saison(h).

Sorties : IS_u,n, déficit relatif de transpiration, arrosage annuel (mm), pour une mare assec de printemps et jours en eau.

**Description mathématique**

(A49-1) saison(h) = vrai si la moyenne des températures des 144 heures précédentes dépasse 5 °C

(A49-2) apport_u = (0,9 x S_imp + 0,1 x S_perm) / A_u

(A49-3) REW(h) = 1 - D(h - 1) / RU_u ; K_s = 1 si REW >= 1 - p, REW / (1 - p) sinon (FAO-56, équation 84)

(A49-4) ET_a(h) = K_s x K_c(saison) x ET0(h)

(A49-5) D(h) = min(RU_u ; max(0 ; D(h - 1) - P(h) x (1 + apport_u) + ET_a(h)))

(A49-6) Arrosage : à 2 h UTC, en saison, si REW < 0,5, le volume D(h) est apporté et D(h) = 0.

(A49-7) IS_u = somme, sur les heures en saison, de max(0 ; (0,4 - REW(h)) / 0,4) / 24

(A49-8) Mare : hauteur d'eau W(h) = min(H ; max(0 ; W(h - 1) + P(h) x (1 + apport_u) - 1,05 x ET0(h) - i_fond / 24)) ; assec de printemps si W(h) = 0 à une heure quelconque de mars à juin.

L'année type est jouée deux fois ; seule la seconde est retenue, pour que le réservoir parte au 1er janvier de son état de fin d'année.

**Cas limites et contrôles**

Une unité de surface nulle est ignorée. Un apport de ruissellement supérieur à 20 fois la surface de l'unité est signalé (bassin de rétention à déclarer comme tel).

**Cas élémentaire**

Prairie sur limon d'un mètre à Trappes : IS = 2,1 jours-équivalents à +2 °C, 11,2 à +2,7 °C, 26,2 à +4 °C (déficit de transpiration de 12 % en saison). Gazon de 0,75 m de racines arrosé : IS = 0, arrosage de 198 mm par an, soit 0,198 m³ par m². Mare de 0,8 m à fond argileux à Marignane, sans bassin versant : à sec au printemps, 210 jours en eau ; raccordée à une surface imperméable égale à la sienne : en eau au printemps, 312 jours en eau.

**Renvois**

Conventions C-W6 à C-W8, C-W10 à C-W12. FAO-56, équations 84 et 85 ; Granier et al. (1999).

#### Fiche A50. Facteur hydrique

**Introduction**

La végétation d'une zone est adaptée au climat de cette zone. Le facteur hydrique ne pénalise donc que le stress que le projet ajoute par ses choix (substrat mince, sol pauvre ou peu profond, absence d'apport) et celui que le réchauffement ajoute au fil de la période.

**Nomenclature**

Entrées : IS_u,n (A49), groupe g_u.

Paramètres : β_g, tolérance 5 jours-équivalents, plancher 0,5, facteur d'assec 0,5 (`hydrique.csv`).

Sorties : k_W,u,n pour chaque niveau ; k_W,u(t) pour chaque année (par A46-3).

**Description mathématique**

(A50-1) IS_ref,g = indice du groupe g sur un limon d'un mètre (substrat de 10 cm pour une toiture extensive), sans arrosage ni apport, à +2 °C, dans la zone du projet

(A50-2) k_W,u,n = max(0,5 ; 1 - β_g x max(0 ; IS_u,n - IS_ref,g - 5) / 100)

(A50-3) Mare : k_W,u,n = 0,5 en cas d'assec de printemps, 1 sinon

(A50-4) k_W,u(t) = somme des w_n(a_0 + t - 1) x k_W,u,n

**Cas limites et contrôles**

Le facteur s'applique à l'état initial comme à l'état projet (fiche A31). Une unité sans bilan a k_W = 1.

**Cas élémentaire**

Toiture biodiverse de 15 cm à Trappes, groupe prairie (β = 0,4) : IS = 31,6 à +2 °C contre IS_ref = 2,1 ; k_W = 1 - 0,4 x (31,6 - 2,1 - 5) / 100 = 0,902. À +4 °C : IS = 45,7 et k_W = 0,846. En 2076 (0,48 et 0,52) : k_W = 0,866.

**Renvois**

Convention C-W9.

#### Fiche A51. Heures éclairées de nuit

**Introduction**

L'effet de l'éclairage sur la faune nocturne dépend d'abord de sa durée. La fiche compte, sur l'année type, les heures de nuit de la saison d'activité des chiroptères pendant lesquelles l'éclairage est allumé.

**Nomenclature**

Entrées : heure d'extinction h_ext et heure de rallumage h_ral en heure légale (ou « toute la nuit ») ; part de temps allumé sous détection de présence δ (1 sans détection).

Paramètres : saison d'activité d'avril à octobre ; nuit si H_s <= 0 à la station de référence ; heure légale = UTC + 2 d'avril à octobre (`eclairage.csv`).

Sorties : x_nuit,u.

**Description mathématique**

(A51-1) N_nuit = nombre d'heures h d'avril à octobre avec H_s(h) <= 0

(A51-2) Pour chaque heure de nuit, h_l = heure légale. Allumée si h_l >= 12 et h_l < h_ext (extinction le soir), ou si h_ext < 12 et (h_l >= 12 ou h_l < h_ext) (extinction après minuit), ou si h_l >= h_ral avant midi (rallumage du matin).

(A51-3) x_nuit,u = δ x N_allumées / N_nuit

**Cas limites et contrôles**

Un éclairage permanent de sécurité est allumé toute la nuit (x_nuit = δ). Un éclairage d'activité économique éteint une heure après la fin d'activité se déclare avec l'heure réelle d'extinction.

**Cas élémentaire**

Trappes : 2 157 heures de nuit d'avril à octobre. Extinction à 1 h : 805 heures allumées, x = 0,3732. Extinction à 23 h : x = 0,1748. Extinction à 22 h et rallumage à 6 h : x = 0,2063.

**Renvois**

Conventions C-L2, C-L4. Arrêté du 27 décembre 2018, article 2.

#### Fiche A52. Facteur spectral et facteur de distance

**Introduction**

À durée égale, une lumière riche en bleu dérange plus qu'une lumière ambrée, et un luminaire proche plus qu'un luminaire lointain.

**Nomenclature**

Entrées : température de couleur T_c (K) ; distance d_u de l'unité au luminaire le plus proche (m).

Paramètres : points (1 800 K ; 0,5), (2 200 ; 0,6), (2 400 ; 0,7), (2 700 ; 0,8), (3 000 ; 0,9), (4 000 ; 1) ; distances 10 et 50 m (`eclairage.csv`).

Sorties : s(T_c), g(d_u).

**Description mathématique**

(A52-1) s(T_c) = interpolation linéaire entre les points ; 0,5 sous 1 800 K ; 1 au-delà de 4 000 K

(A52-2) g(d) = 1 si d <= 10 ; 0 si d >= 50 ; (50 - d) / 40 sinon

**Cas limites et contrôles**

Une unité éclairée par plusieurs luminaires prend la distance du plus proche et la température de couleur la plus élevée.

**Cas élémentaire**

s(2 700) = 0,8 ; s(3 500) = 0,95 ; g(20) = 0,75 ; g(35) = 0,375.

**Renvois**

Conventions C-L3, C-L4. Azam et al. (2018) ; Longcore et al. (2018).

#### Fiche A53. Facteur d'éclairage

**Introduction**

La fiche combine durée, spectre et distance. Elle remplace l'équation A20-2 ; les classes L1 et L2 restent admises comme raccourcis de saisie.

**Nomenclature**

Entrées : x_nuit,u (A51), s, g (A52).

Paramètres : perte maximale 0,25.

Sorties : k_lum,u, qui entre dans k_N,u (fiche A20).

**Description mathématique**

(A53-1) k_lum,u = 1 - 0,25 x x_nuit,u x s(T_c) x g(d_u) [N3]

(A53-2) Raccourcis : L0, aucun éclairage, k_lum = 1 ; L1, extinction à 1 h, 3 000 K, au pied ; L2, toute la nuit, 4 000 K, au pied (k_lum = 0,75).

**Cas limites et contrôles**

k_lum est compris entre 0,75 et 1.

**Cas élémentaire**

Trappes, L1 : 1 - 0,25 x 0,3732 x 0,9 x 1 = 0,9160. Extinction à 23 h, 2 700 K, à 20 m : 1 - 0,25 x 0,1748 x 0,8 x 0,75 = 0,9738. Toute la nuit en ambre sous détection (30 % du temps), au pied : 1 - 0,25 x 0,3 x 0,5 x 1 = 0,9625.

**Renvois**

Convention C-L1. Fiche A20.

#### Fiche A54. Courbe de maturation

**Introduction**

Un milieu créé ne gagne pas sa valeur en ligne droite. Une prairie semée donne vite la plus grande part de sa flore ; un boisement planté vaut peu les premières années, puis accélère. La fiche emploie la fonction de croissance de Chapman-Richards, ramenée à 1 au délai de maturité de la métrique anglaise.

**Nomenclature**

Entrées : τ, temps depuis le départ de la maturation (A58), en années ; d_u, délai de maturité (A28-1).

Paramètres : k x d = 3 ; exposant c = 1 (herbacé), 2 (arbustif), 3 (arboré) (`succession.csv`).

Sorties : g_u(τ).

**Description mathématique**

(A54-1) Forme : arborée pour G, VB.18a, VB.18b ; arbustive pour F, FA, FB, VB.6, VB.9 ; herbacée sinon.

(A54-2) g_u(τ) = 0 si τ <= 0 ; 1 si d_u = 0 ; min(1 ; [(1 - e^(-3 τ / d_u)) / (1 - e^(-3))]^c) sinon [T3]

**Cas limites et contrôles**

g_u(d_u) = 1 pour toutes les formes : le délai de maturité garde son sens. Un renouvellement (A30) repart de τ = 0.

**Cas élémentaire**

d = 10 ans, τ = 1 ; 2,5 ; 5 ; 7,5 ; 10. Herbacée : 0,273 ; 0,555 ; 0,818 ; 0,941 ; 1. Arbustive : 0,074 ; 0,308 ; 0,668 ; 0,886 ; 1. Arborée : 0,020 ; 0,171 ; 0,546 ; 0,834 ; 1. La droite de la première rédaction donnait 0,1 ; 0,25 ; 0,5 ; 0,75 ; 1.

**Renvois**

Convention C-M1. Richards (1959) ; Pienaar et Turnbull (1973).

#### Fiche A55. Régime de gestion

**Introduction**

La valeur visée d'un milieu créé suppose une gestion écologique : fauche tardive, taille douce, maintien des bois morts. La fiche dit, pour chaque année, sous quel régime l'unité est gérée.

**Nomenclature**

Entrées : durée du plan de gestion écologique P (projet ou unité), en années depuis la livraison ; régime déclaré pour l'après-plan (gestion courante par défaut, ou abandon) ; régime imposé d'une unité (gestion courante ou abandon dès la livraison).

Sorties : régime(t) et durée écoulée dans ce régime.

**Description mathématique**

(A55-1) a_l(t) = t - 1 - d_mois / 12, années écoulées depuis la livraison au début de l'année t

(A55-2) régime(t) = régime imposé s'il y en a un ; plan si a_l(t) < P ; régime d'après-plan sinon, depuis a_l(t) - P années

Les unités conservées et l'état initial gardent leur gestion actuelle.

**Cas limites et contrôles**

P = 0 (aucun plan déclaré) : gestion courante dès la livraison. Un plan de plus de 50 ans couvre toute la période.

**Cas élémentaire**

Chantier de 18 mois, plan de 10 ans : a_l(t) >= 10 à partir de t = 13 ; la gestion courante commence l'année 13.

**Renvois**

Convention C-M3.

#### Fiche A56. Facteur de gestion et succession

**Introduction**

Une prairie tondue comme une pelouse perd la moitié de sa valeur ; une prairie abandonnée se ferme peu à peu en friche puis en fourré. La fiche traduit le régime de gestion en un facteur appliqué à la valeur de l'année.

**Nomenclature**

Entrées : régime(t), durée dans le régime, v_u, f_u, groupe g_u, position.

Paramètres : valeur intrinsèque de VB.5 et des stades jeunes (`habitats.csv`) ; rapports d'abandon de la BKompV, délais de 2 et 15 ans, score 0,75 de la friche embroussaillée (`succession.csv`).

Sorties : f_g,u(t).

**Description mathématique**

(A56-1) Plan : f_g = 1

(A56-2) Gestion courante : prairie ou végétation xérophile en pleine terre (hors VB.5, VB.7, VB.22) : f_g = min(1 ; v(VB.5) / v_u) ; haie : f_g = min(1 ; v(h_u, stade J) / v_u) ; autres : f_g = 1

(A56-3) Abandon d'un milieu herbacé : f_g = 1 pendant 2 ans ; puis r_ab(h_u), rapport de la variante abandonnée au type exploité de la BKompV (moyenne des couples à défaut) jusqu'à 15 ans ; puis f_g = v(VB.9) x (0,5 + 0,5 x 0,75) / (v_u x f_u)

**Cas limites et contrôles**

Un milieu ligneux ou aquatique abandonné garde f_g = 1 dans la présente version. f_g n'est jamais supérieur à 1 en gestion courante.

**Cas élémentaire**

Prairie urbaine VB.26 (v = 0,6250, f = 0,8333) en gestion courante : f_g = 0,3333 / 0,6250 = 0,5333. Haie FA.3 de stade moyen : 0,5 / 0,6667 = 0,75. Abandon de VB.26 (BKompV 34.07b.01, 15 points, contre 34.07b.03, 11 points) : 0,733 de la 3e à la 15e année, puis 0,5 x 0,875 / (0,625 x 0,8333) = 0,84.

**Renvois**

Conventions C-M2, C-M3. BKompV, annexe 2.

#### Fiche A57. Destruction en période sensible

**Introduction**

Détruire un fourré en mai tue les couvées ; abattre un vieil arbre creux en janvier tue les chiroptères en hibernation. La fiche ajoute à Cnat le coût de ces destructions, en plus de la perte d'habitat.

**Nomenclature**

Entrées : unités de l'état initial non conservées ni améliorées ; mois de destruction m_d (déclaré, à défaut premier mois du chantier).

Paramètres : sensibilité mensuelle des oiseaux nicheurs, des chiroptères et des amphibiens ; perte d'une année (`chantier.csv`).

Sorties : ΔI_ch et son détail par unité.

**Description mathématique**

(A57-1) Groupes de faune d'une unité : oiseaux pour F, FA, G, VB.18, VB.9, E, VB.8, VB.26 ; chiroptères pour un arbre ou un boisement de stade âgé, ou des gîtes déclarés ; amphibiens pour C1, C3, D, VB.19, VB.20.

(A57-2) s_u = sensibilité la plus forte de ses groupes au mois m_d

(A57-3) ΔI_ch = somme des V_u x s_u x 1 an [T9]

**Cas limites et contrôles**

Une destruction étalée sur plusieurs mois se déclare au mois le plus sensible. ΔI_ch ne s'applique pas à l'état initial dégradé volontairement (convention C-R5), qui se saisit dans son état antérieur.

**Cas élémentaire**

Exemple de l'annexe C défriché en mai : friche herbacée 210,77 x 1 + friche arbustive 32,79 x 1 = 243,56 m²HE·an ; les arbres sont conservés. Défriché en septembre : 0.

**Renvois**

Convention C-K1. BCAE 8 de la conditionnalité de la PAC.

#### Fiche A58. Calendrier mensuel et plantations

**Introduction**

La fiche place le chantier et les plantations dans le calendrier, au mois près. Un chantier qui finit en mai ne plante qu'en novembre : six mois de maturation perdus.

**Nomenclature**

Entrées : année a_0 et mois m_0 de début du chantier ; durée d_mois en mois.

Paramètres : mois favorables aux plantations (novembre à mars), avance de deux mois (`chantier.csv`).

Sorties : rang de plantation m_pl ; mois de départ de chaque unité.

**Description mathématique**

(A58-1) Mois civil du rang i : ((m_0 - 1 + i - 1) mod 12) + 1

(A58-2) m_pl = premier rang i >= max(1 ; d_mois - 1) dont le mois civil est favorable

(A58-3) Départ de la maturation : fin du rang m_pl - 1 pour un milieu à délai non nul ; fin du chantier (rang d_mois) sinon

(A58-4) Valeur de l'année t : moyenne des valeurs mensuelles des rangs 12 (t - 1) + 1 à 12 t [T6]

**Cas limites et contrôles**

Un aménagement sans chantier lourd (d_mois = 0) plante au premier mois favorable de la période.

**Cas élémentaire**

Début en septembre, 18 mois : plantation au rang 17 (janvier). Début en janvier, 18 mois : rang 23 (novembre de l'année suivante). Début en avril, 6 mois : rang 8 (novembre). Début en novembre, 3 mois : rang 2 (décembre).

**Renvois**

Conventions C-K2, C-K3.

#### Pseudo-code des fiches A43 à A58

**A43 à A45. Climat horaire**

```
pour chaque niveau n dans (+2 ; +2,7 ; +4) :
  lire l'année type de la station de la zone
  pour chaque mois : ρ_mois ← P_norm,mois / cumul du mois
  pour chaque heure h : T ← T2m - 0,0065 x (z_site - z_st) ; P ← RR x ρ_mois ; calculer ET0(h) (A44-1 à A44-6)
```

**A46. Années de la période**

```
pour a de a_0 à a_0 + 49 : ΔT ← jalons TRACC ; w_n(a) ← (A46-2)
```

**A47 à A50. Bilan hydrique**

```
pour chaque unité u de l'état initial et de l'état projet :
  g ← groupe(u) ; si sans bilan : k_W,u,n ← 1 ; continuer
  RU ← réserve(u) ; apport ← (0,9 S_imp + 0,1 S_perm) / A_u
  pour chaque niveau n : jouer deux fois l'année ; garder IS, arrosage, assec de la seconde
  IS_ref ← même calcul pour le groupe g sur le sol de référence à +2 °C
  k_W,u,n ← (A50-2) ou (A50-3)
  pour chaque année t : k_W,u(t) ← somme des w_n x k_W,u,n
```

**A51 à A53. Éclairage**

```
pour chaque unité éclairée : x ← heures allumées de nuit / heures de nuit (avril à octobre) x δ ; k_lum ← 1 - 0,25 x x x s(T_c) x g(d)
```

**A54 à A58. Trajectoire mensuelle**

```
m_pl ← (A58-2)
pour chaque unité u du projet :
  départ ← m_pl - 1 si d_u > 0, sinon d_mois
  pour m de 1 à 600 : τ ← (m - départ) / 12 ; valeur(m) ← (T2), (T3) ou (T4) avec g_u(τ) de (A54-2)
  pour t de 1 à 50 : base(t) ← moyenne des valeur(m) de l'année ; f_g ← (A56) selon le régime (A55) ; V_u(t) ← base(t) x k_W,u(t) x f_g
ΔI_ch ← (A57-3)
```

**Second cas élémentaire, fiches A49 et A50**

Haie champêtre FA.3 sur limon d'un mètre à Trappes (RU = 117 mm, β = 0,6) : IS = 33,3 à +2 °C (égal à IS_ref, k_W = 1), 37,4 à +2,7 °C (écart de 4,1, sous la tolérance de 5 : k_W = 1), 47,7 à +4 °C : k_W = 1 - 0,6 x (47,7 - 33,3 - 5) / 100 = 0,943.
