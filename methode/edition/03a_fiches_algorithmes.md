## Partie 3. Fiches algorithmes

Les fiches algorithmes décrivent les éléments codés dans le cœur de calcul OpenNAT. Elles suivent le plan des fiches algorithmes de la méthode Th-BCE 2020 : une introduction qui dit l'objet de la fiche ; une nomenclature qui liste les variables, avec leur nom, leur description, leur unité, leur plage et, le cas échéant, leur valeur conventionnelle ; une description mathématique, faite d'équations numérotées qui n'emploient que des variables de la nomenclature. S'y ajoutent, pour chaque fiche, les cas limites et contrôles, un cas élémentaire chiffré et les renvois aux tables et aux conventions.

La nomenclature distingue cinq types de variables, comme la méthode Th-BCE :
- les entrées, qui viennent du fichier projet, du RSEE ou d'une autre fiche ;
- les paramètres, intrinsèques (propres au type d'habitat ou au matériau, lus dans `donnees/`) ou d'intégration (propres à la mise en œuvre dans le projet, saisis) ;
- les variables internes, calculées et utilisées dans la fiche ;
- les constantes ;
- les sorties, qui font le lien avec les autres fiches.

Les équations sont numérotées par fiche : (A09-3) est la troisième équation de la fiche A09. Le renvoi entre crochets donne l'équation correspondante du texte de la méthode (partie 1) : [H3].

Les fiches sont appelées dans l'ordre suivant, qui est celui du chapitre 6 de la méthode :

| Ordre | Fiches | Étape ou module |
|---|---|---|
| 1 | A01, A02 | Généralités, contexte (E1) |
| 2 | A03 à A05 | Prétraitement (E2) |
| 3 | A06 à A08 | Module S, sol |
| 4 | A09 à A16 | Module H, habitats |
| 5 | A17 à A19 | Module C, connectivité |
| 6 | A20 à A22 | Module N, nuisances |
| 7 | A23 à A25 | Module E, eau, et valeur à maturité |
| 8 | A26 à A31 | Module T, temps |
| 9 | A32 à A36 | Module G, biodiversité grise |
| 10 | A37, A38 | Agrégation (E3), Bnat |
| 11 | A39 | Incertitude (E4) |
| 12 | A40 à A42 | Conformité (E5), variantes, journal des calculs |

### 3.1 Généralités et contexte

#### Fiche A01. Conventions générales du cœur de calcul

**Introduction**

Cette fiche fixe ce qui vaut pour toutes les autres : le pas de temps, les unités, les signes, l'arrondi, le traitement des valeurs manquantes et l'ordre de lecture des tables.

**Nomenclature**

Constantes :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| N | Période de référence | an | 50 (`contexte.csv`, `periode_reference`) |
| N30 | Période complémentaire | an | 30 (`contexte.csv`, `periode_complementaire`) |
| Δt | Pas de temps de la simulation | an | 1 |
| V_max | Plafond de valeur par m² | m²HE/m² | 1,15 (`contexte.csv`, `plafond_valeur_unitaire`) |

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| version_methode | Version de la méthode | texte | « OpenNAT 1 » |
| version_donnees | Empreinte des tables de `donnees/` | texte | SHA-256 |
| graine | Graine du générateur aléatoire | entier | 0 à 2^63 - 1 |

**Description mathématique**

Le temps est discret : l'année t va de 1 à N. Une grandeur annuelle X(t) représente la valeur moyenne de l'année t. Une grandeur intégrée est la somme des grandeurs annuelles :

(A01-1) I_X = somme pour t de 1 à N de X(t) x Δt

Signes : une valeur d'habitat est positive ou nulle ; Cnat est positif quand le site perd de la nature ; Inat est positif ou nul ; Snat est négatif quand l'opération consomme plus de nature qu'elle n'en rend.

Arrondi : aucun résultat intermédiaire n'est arrondi. Les sorties affichées et écrites dans le RSNat portent une décimale (valeurs en m²HE et m²HE·an) ou quatre décimales (facteurs sans unité).

Valeurs manquantes : une entrée obligatoire absente arrête le calcul avec un message qui nomme l'entrée et l'unité concernées. Une entrée facultative absente prend sa valeur par défaut, écrite dans le journal des calculs (fiche A42).

Lecture des tables : au démarrage, le cœur de calcul charge toutes les tables de `donnees/` et refuse toute ligne sans source, sans référence précise ou dont la valeur sort de sa plage (contrôle de `outils/controle_donnees.py`). Une valeur est appelée par sa clé et son paramètre ; aucune valeur numérique de méthode n'est écrite dans le code.

**Cas limites et contrôles**

Une parcelle sans aucune unité végétalisée ni en eau, à l'état initial comme à l'état projet, donne I_0 = I_1 = 0 et Cnat = 0. Ce n'est pas une erreur.

**Renvois**

Conventions C-T1, C-T5, C-H7. Exigences E1, E2, E7 du cahier des charges.

#### Fiche A02. Contexte de l'opération (étape E1)

**Introduction**

L'étape E1 lit le contexte et en déduit, pour chaque unité, le multiplicateur de situation, et pour l'opération, la zone biogéographique, le multiplicateur de délai et les seuils applicables.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| zone | Zone biogéographique | énumération | atlantique, continentale, méditerranéenne, alpine |
| typologie | Typologie de l'opération | énumération | logement, tertiaire, industrie, aménagement |
| situation_u | Situation de l'unité u dans la trame verte et bleue | énumération | réservoir, corridor, hors trame |
| E_bati | Emprise au sol du bâti | m² | 0 à S_p |
| S_p | Surface de la parcelle | m² | supérieure à 0 |
| CBS_PLU | Coefficient de biotope imposé par le PLU | sans unité | 0 à 1, facultatif |
| PT_PLU | Part de pleine terre imposée par le PLU | sans unité | 0 à 1, facultative |

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur ou origine |
|---|---|---|---|
| m_res | Multiplicateur en réservoir | sans unité | 1,15 (`contexte.csv`, `situation_reservoir`) |
| m_cor | Multiplicateur en corridor | sans unité | 1,10 (`contexte.csv`, `situation_corridor`) |
| m_hors | Multiplicateur hors trame | sans unité | 1 (`contexte.csv`, `situation_hors_trame`) |
| k_z | Multiplicateur de délai de la zone | sans unité | 1 (`contexte.csv`, `zone_*`) |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| m_u | Multiplicateur de situation de l'unité | sans unité |
| k_delai | Multiplicateur de délai de l'opération | sans unité |
| e | Part d'emprise du bâti | sans unité |
| Bnat_min | Seuil de Bnat applicable | points |
| PT_min | Seuil de pleine terre applicable | sans unité |

**Description mathématique**

(A02-1) m_u = m_res si situation_u = réservoir ; m_cor si situation_u = corridor ; m_hors sinon [1]

(A02-2) k_delai = k_z(zone)

(A02-3) e = E_bati / S_p

(A02-4) Bnat_min = seuil de `seuils.csv` choisi par la typologie et, pour le logement, par la classe d'emprise : e jusqu'à 0,37 ; de 0,38 à 0,49 ; 0,50 et plus. Pour l'industrie et l'aménagement, Bnat_min n'est pas défini.

(A02-5) Si CBS_PLU est donné : Bnat_min = max(Bnat_min ; 100 x CBS_PLU).

(A02-6) PT_min = max(`pleine_terre_min` ; PT_PLU si elle est donnée).

La classe d'emprise se lit sur e arrondi à deux décimales.

**Cas limites et contrôles**

E_bati supérieur à S_p arrête le calcul. Une unité sans situation déclarée est hors trame.

**Cas élémentaire**

Parcelle de 2 000 m², emprise de 700 m², logement, PLU sans coefficient de biotope : e = 0,35 ; Bnat_min = 45 ; PT_min = 0,15. Une unité en corridor reçoit m_u = 1,10.

**Renvois**

`contexte.csv`, `seuils.csv`. Conventions C-E1, C-E2, C-E6, C-P1.

### 3.2 Prétraitement des surfaces (étape E2)

#### Fiche A03. Fermeture des surfaces

**Introduction**

Le contrôle de fermeture vérifie que les unités au sol décrivent toute la parcelle, sans manque ni recouvrement, à l'état initial comme à l'état projet de chaque variante.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| S_p | Surface de la parcelle | m² | supérieure à 0 |
| A_u | Surface de l'unité u | m² | supérieure à 0 |
| position_u | Position de l'unité u | énumération | sol pleine terre, sol sur dalle, eau, linéaire, hors-sol toiture, hors-sol façade, arbre |

Paramètres :

| Nom | Description | Unité | Valeur ou origine |
|---|---|---|---|
| τ_rel | Tolérance relative | sans unité | 0,005 (`contexte.csv`, `tolerance_fermeture_relative`) |
| τ_abs | Tolérance absolue | m² | 1 (`contexte.csv`, `tolerance_fermeture_absolue`) |

Variables internes :

| Nom | Description | Unité |
|---|---|---|
| Σ_sol | Somme des surfaces au sol d'un état | m² |
| ε | Écart de fermeture | m² |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| fermeture_ok | Résultat du contrôle par état | booléen |

**Description mathématique**

(A03-1) Σ_sol = somme des A_u pour position_u dans {sol pleine terre, sol sur dalle, eau, linéaire}

(A03-2) ε = | Σ_sol - S_p |

(A03-3) fermeture_ok = (ε <= max(τ_abs ; τ_rel x S_p)) [2]

Les unités hors-sol (toiture, façade) et les arbres ne sont pas comptés : une toiture se superpose à l'emprise du bâti ; un houppier surplombe d'autres unités.

**Cas limites et contrôles**

Si fermeture_ok est faux pour un état, le calcul s'arrête à l'étape E2 et le journal donne Σ_sol, S_p et ε. Une haie est une unité linéaire dont la surface est longueur x largeur : elle entre dans la fermeture, car elle occupe le sol.

**Cas élémentaire**

S_p = 2 000 m², unités au sol de 1 200, 600 et 199 m² : Σ_sol = 1 999 m², ε = 1 m², tolérance max(1 ; 10) = 10 m² : contrôle satisfait.

**Renvois**

Convention C-E3.

#### Fiche A04. Classement des unités et nomenclature

**Introduction**

Chaque unité reçoit son type de la nomenclature, sa position, son statut et, pour les types ligneux, son stade. Les codes EUNIS 2012 du groupe J sont convertis en types VB.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| code_u | Code d'habitat saisi | texte | code de `nomenclature_habitats.csv` ou code EUNIS rattaché |
| position_u | Position saisie | énumération | voir fiche A03 |
| statut_u | Statut à l'état projet | énumération | conservée, créée, améliorée |
| stade_u | Stade d'un type ligneux | énumération | jeune, moyen, âgé, ou classe de diamètre |
| e_u | Épaisseur de substrat | cm | 0 à 300 |

Paramètres intrinsèques : la table `nomenclature_habitats.csv` (code, position par défaut, codes rattachés).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| h_u | Type OpenNAT de l'unité | code |
| p_u | Position retenue | énumération |
| st_u | Stade retenu (J, M, A) | énumération |

**Description mathématique**

(A04-1) h_u = code_u si code_u est un code OpenNAT ; sinon le type VB dont la colonne `alias_eunis_2012` contient code_u ; sinon le type dont la colonne `code_eunis_2012` égale le parent de niveau 3 de code_u.

(A04-2) p_u = position_u si elle est saisie et compatible avec le type ; sinon la position par défaut du type.

Compatibilités : un type de position « sol » peut être saisi en pleine terre ou sur dalle ; un type « hors-sol » ne peut être saisi qu'en hors-sol ; un type « eau », « arbre » ou « linéaire » garde sa position.

(A04-3) st_u = stade_u converti : jeune = J, moyen = M, âgé = A ; pour une classe de diamètre, petit = J, moyen = M, grand et très grand = A (convention C-H5) ; défaut M.

**Cas limites et contrôles**

Un code inconnu arrête le calcul. Un code EUNIS de niveau 4 ou 5 est accepté et remonté à son parent de niveau 3 (audit, § 4.2). Une épaisseur de substrat est exigée pour toute unité sur dalle ou hors-sol en toiture.

**Cas élémentaire**

Code saisi « J4.2 » : h_u = VB.2. Code saisi « E2.22 » : h_u = E2.2. Arbre de 70 cm de diamètre : st_u = A.

**Renvois**

`nomenclature_habitats.csv`. Conventions C-H5.

#### Fiche A05. Reprise des données du RSEE

**Introduction**

Quand le projet a fait l'objet d'une étude RE2020, ses données se reprennent du RSEE, sans nouvelle saisie. La fiche dit quels éléments sont lus, comment ils sont convertis et comment ils se contrôlent.

**Nomenclature**

Entrées (éléments du RSEE, branche RSEnv) :

| Nom | Élément | Unité |
|---|---|---|
| sp_rsee | `entree_projet/parcelle/surface_parcelle` | m² |
| sveg_rsee | `entree_projet/parcelle/surface_veg` | m² |
| simp_rsee | `entree_projet/parcelle/surface_imper` | m² |
| sarr_rsee | `entree_projet/parcelle/surface_arrosee` | m² |
| emp_rsee | `entree_projet/batiment/emprise_au_sol` | m² |
| dch_rsee | `entree_projet/batiment/duree_chantier` | mois |
| sref_rsee | `entree_projet/batiment/sref` (ou somme des `zone/sref`) | m² |
| ges_{c,p} | indicateur 101 du contributeur c (composant, chantier), phase p (A1-A3, A4-A5, B, C, D) | kg CO2 éq./m² |
| pol_{i,c,p} | indicateurs 106 à 109 et 116, mêmes contributeurs et phases | unités de l'annexe II |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| S_p | Surface de la parcelle | m² |
| E_bati | Emprise au sol | m² |
| d_ch | Durée du chantier | an |
| S_ref | Surface de référence | m² |
| GES_p | Émissions des contributeurs composants et chantier par phase | kg CO2 éq./m² |

**Description mathématique**

(A05-1) S_p = sp_rsee ; E_bati = somme des emp_rsee des bâtiments

(A05-2) d_ch = max des dch_rsee des bâtiments / 12

(A05-3) S_ref = somme des sref_rsee des bâtiments

(A05-4) GES_p = (somme sur les bâtiments b de ges_{composant,p,b} x S_ref,b + ges_{chantier,p,b} x S_ref,b) / S_ref

Contrôles de cohérence, non bloquants, écrits au journal :

(A05-5) | sveg_rsee - surface des unités végétalisées en pleine terre de l'état projet | <= 5 % de S_p

(A05-6) | simp_rsee - surface des unités S01 de l'état projet | <= 5 % de S_p

**Cas limites et contrôles**

Un RSEE sans branche RSEnv ne fournit ni la parcelle, ni l'emprise, ni les indicateurs : ces données se saisissent. Les indicateurs du RSEE sont exprimés par m² de surface de référence ; une opération de plusieurs bâtiments les pondère par la S_ref de chacun (A05-4). Les codes d'indicateur 101 à 136 suivent l'ordre de la liste de l'annexe II de l'arrêté du 4 août 2021 ; aucun texte publié ne donne cette numérotation, elle est contrôlée sur un RSEE réel par l'égalité des totaux d'énergie primaire (indicateurs 120 + 121 = 122 et 123 + 124 = 125).

**Cas élémentaire**

Un bâtiment, S_ref 890,26 m², emprise 973 m², durée de chantier 12 mois, parcelle 1 897 m² : S_p = 1 897 ; E_bati = 973 ; d_ch = 1 ; S_ref = 890,26.

**Renvois**

Annexe II de l'arrêté du 4 août 2021. Convention C-G1.

### 3.3 Module S : sol

#### Fiche A06. Nature de surface et coefficient de sol

**Introduction**

Chaque unité reçoit une nature de surface (S01 à S13) et le coefficient correspondant. La nature dépend du type, de la position et de l'épaisseur de substrat.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| h_u | Type de l'unité | code | nomenclature |
| p_u | Position | énumération | voir fiche A03 |
| e_u | Épaisseur de substrat | cm | 0 à 300 |
| alim_u | Alimentation d'une unité en eau | énumération | naturelle, artificielle |

Paramètres intrinsèques : `sols.csv`, coefficients c(S01) à c(S13).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| n_u | Nature de surface | code S01 à S12 |
| c_u | Coefficient de sol | sans unité |

**Description mathématique**

(A06-1) n_u =
- S01 si h_u est VB.1 ou VB.2 ;
- S02 si h_u est VB.3, VB.10, VB.25 ou H5.6 ;
- S03 si h_u est VB.4 ;
- S11 si p_u = eau et h_u n'est ni VB.21 ni VB.24 ;
- S12 si h_u est VB.21 ou VB.24 ;
- S09 si h_u est VB.15 ; S10 si h_u est VB.16 ;
- pour p_u = sol sur dalle ou hors-sol toiture : S04 si e_u < 15, S05 si 15 <= e_u <= 30, S06 si 30 < e_u < 80, S07 si e_u >= 80 ;
- S08 sinon (unité végétalisée en pleine terre).

(A06-2) c_u = c(n_u) [S1]

Un arbre (position arbre) n'a pas de nature de surface propre : il surplombe une autre unité.

**Cas limites et contrôles**

Le sol nu de chantier (VB.10) et la voie ferrée (VB.25) sont classés en S02 : leur sol reste perméable. Une jardinière hors-sol (VB.23) sans épaisseur déclarée est classée S04.

**Cas élémentaire**

Pelouse (VB.5) sur dalle avec 40 cm de substrat : n_u = S06, c_u = 0,7. Toiture biodiverse (VB.12) de 15 cm : n_u = S05, c_u = 0,6. Noue (VB.19) : S11, 0,6.

**Renvois**

`sols.csv`. Convention C-S1.

#### Fiche A07. Facteur de support

**Introduction**

Le facteur de support corrige la valeur d'habitat d'un type au sol quand il est posé sur dalle, faute de continuité avec le sol en place.

**Nomenclature**

Entrées : h_u, p_u, c_u (fiche A06).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| f_sol,u | Facteur de support | sans unité, 0 à 1 |

**Description mathématique**

(A07-1) f_sol,u = c_u si p_u = sol sur dalle ; 1 sinon [S2]

Pour les types hors-sol (toitures, façades, jardinières), la valeur intrinsèque tient déjà compte du support : f_sol,u = 1.

**Cas limites et contrôles**

Une unité sur dalle de 80 cm et plus garde 0,9 de sa valeur ; en dessous de 15 cm, 0,5.

**Cas élémentaire**

Prairie urbaine VB.26 sur dalle de 50 cm : f_sol = c(S06) = 0,7.

**Renvois**

Convention C-S2.

#### Fiche A08. Pleine terre et imperméabilisation

**Introduction**

La fiche calcule les indicateurs de sol du site : taux de pleine terre et imperméabilisation nette créée.

**Nomenclature**

Entrées : A_u, n_u, p_u des deux états ; S_p.

Sorties :

| Nom | Description | Unité |
|---|---|---|
| PT | Taux de pleine terre végétalisée de l'état projet | sans unité |
| PT_0 | Taux de pleine terre végétalisée de l'état initial | sans unité |
| ΔA_imp | Imperméabilisation nette créée | m² |
| A_imp,0, A_imp,1 | Surfaces scellées des deux états | m² |

**Description mathématique**

(A08-1) PT = somme des A_u de l'état projet tels que n_u = S08 / S_p [S3]

(A08-2) A_imp,k = somme des A_u de l'état k tels que n_u = S01

(A08-3) ΔA_imp = A_imp,1 - A_imp,0 [S4]

La pleine terre s'entend au sens du Cerema : sol sans revêtement, végétalisé, en continuité avec le sous-sol, sans interface imperméable.

**Cas limites et contrôles**

Une noue végétalisée en pleine terre (VB.19) n'est pas comptée en pleine terre : elle est en S11. Un ΔA_imp négatif signale une désimperméabilisation.

**Cas élémentaire**

État initial : 600 m² d'enrobé ; état projet : 700 m² de bâti et 300 m² de voirie, 850 m² en pleine terre, parcelle de 2 000 m² : PT = 0,425 ; ΔA_imp = 400 m².

**Renvois**

Fiche A38 (Bnat), fiche A40 (conformité).

### 3.4 Module H : habitats

#### Fiche A09. Valeur intrinsèque

**Introduction**

La valeur intrinsèque est la valeur d'un m² d'un type d'habitat en bon état, en pleine terre, hors de tout effet de contexte, sur l'échelle de 0 à 1 m²HE par m².

**Nomenclature**

Entrées : h_u, st_u.

Paramètres intrinsèques :

| Nom | Description | Unité | Origine |
|---|---|---|---|
| v(h) | Valeur intrinsèque du type | m²HE/m² | `habitats.csv`, `valeur_intrinseque` |
| v_J(h), v_M(h), v_A(h) | Valeurs par stade des types ligneux | m²HE/m² | `habitats.csv`, `valeur_intrinseque_stade_*` |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| v_u | Valeur intrinsèque de l'unité | m²HE/m² |

**Description mathématique**

(A09-1) v_u = v_{st_u}(h_u) si le type a des valeurs par stade ; v(h_u) sinon [H1]

Origine des valeurs : v(h) = W_BKompV(h) / 24, où W_BKompV est la valeur de biotope de l'annexe 2 de la BKompV pour le code retenu par la nomenclature (convention C-H1). Pour les types sans équivalent BKompV, v(h) = (distinctivité anglaise / 8) x r, avec r = 1,056 (convention C-H3).

**Cas limites et contrôles**

v_u est compris entre 0 et 1. Les types scellés valent 0.

**Cas élémentaire**

Hêtraie (G1.6) déclarée âgée : v_A = 20 / 24 = 0,8333. Toiture extensive (VB.11) : 2 / 8 x 1,056 = 0,2639.

**Renvois**

`habitats.csv`, partie 4. Conventions C-H1, C-H3, C-H5.

#### Fiche A10. Score d'état des grilles à critères

**Introduction**

Le score d'état mesure, de 0 à 1, l'état d'une unité à partir des critères observables de la grille de son type.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| x_{u,k} | Réponse au critère k de la grille de l'unité u | booléen | oui, non, sans objet |

Paramètres intrinsèques :

| Nom | Description | Unité | Origine |
|---|---|---|---|
| G(h) | Grille du type | code | convention C-H6 |
| ess_k | Le critère k est essentiel | booléen | `etat_criteres.csv`, suffixe `_essentiel` |
| S_plaf | Plafond en cas d'échec d'un critère essentiel | sans unité | 0,5 (`etat_criteres.csv`, `plafond_score_si_essentiel_echoue`) |

Variables internes :

| Nom | Description | Unité |
|---|---|---|
| n_app | Nombre de critères applicables | entier |
| n_ok | Nombre de critères satisfaits | entier |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| S_u | Score d'état | sans unité, 0 à 1 |

**Description mathématique**

(A10-1) n_app = nombre de critères k de G(h_u) dont la réponse n'est pas « sans objet »

(A10-2) n_ok = nombre de critères k tels que x_{u,k} = oui

(A10-3) S_u = n_ok / n_app [H2]

(A10-4) si un critère essentiel k a x_{u,k} = non : S_u = min(S_u ; S_plaf)

Critères sans objet : dans la grille urbaine EU1, les critères D, E1, E2, F et G ne s'appliquent qu'aux types qu'ils désignent (friche, noues et bassins, toiture intensive, toiture biodiverse) ; dans la grille des haies EH1, les attributs E1 et E2 ne s'appliquent qu'aux haies avec arbres.

**Cas limites et contrôles**

Une unité sans réponse reçoit n_ok = 0 et S_u = 0 (défaut « tous non » du chapitre 4) : l'écologue doit renseigner la grille pour obtenir mieux que la moitié de la valeur. Pour un habitat créé, les réponses sont les critères visés et justifiés.

**Cas élémentaire**

Friche urbaine VB.8, grille EU1 : A oui, B oui, C non (essentiel), D oui ; E1, E2, F, G sans objet : n_app = 4, n_ok = 3, S = 0,75, plafonné à 0,5.

**Renvois**

`etat_criteres.csv`, partie 6 (protocoles de relevé). Conventions C-H6, C-H8.

#### Fiche A11. Score d'état des boisements

**Introduction**

La grille des boisements (EB1) ne répond pas par oui ou non : chacun de ses 13 indicateurs est noté de 1 à 3, comme dans la fiche 24A de la métrique anglaise.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| q_{u,k} | Note de l'indicateur k | entier | 1, 2, 3 |

Sorties : S_u.

**Description mathématique**

(A11-1) Q_u = somme des q_{u,k} pour k de 1 à 13 (de 13 à 39)

(A11-2) S_u = (Q_u - 13) / 26

La classe anglaise (bon au-delà de 32, moyen de 26 à 32, mauvais en dessous) correspond à S_u au-delà de 0,73, de 0,5 à 0,73, et en dessous de 0,5 ; OpenNAT garde ses propres classes (fiche A12) pour le choix des délais.

**Cas limites et contrôles**

Un indicateur non noté vaut 1.

**Cas élémentaire**

Notes : 3, 2, 3, 2, 3, 2, 2, 3, 2, 2, 1, 2, 2 : Q = 29, S = 16 / 26 = 0,6154.

**Renvois**

`etat_criteres.csv` (EB1). Convention C-H6.
