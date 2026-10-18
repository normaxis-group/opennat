### 3.12 Pseudo-code et seconds cas élémentaires

Pour chaque fiche, le pseudo-code donne l'ordre exact des opérations que le moteur doit suivre, et un second cas élémentaire complète le premier. Le pseudo-code emploie les noms de la nomenclature de la fiche ; `table(clé, paramètre)` désigne la lecture d'une valeur dans `donnees/`. Les nombres des cas ont été vérifiés par le carnet de référence.

#### A01. Conventions générales

```
charger toutes les tables de donnees/
pour chaque ligne : refuser si source, référence ou type manquent, ou si valeur hors de sa plage
N ← table(*, periode_reference) ; N30 ← table(*, periode_complementaire)
V_max ← table(*, plafond_valeur_unitaire)
écrire version_methode, empreinte des tables, graine dans le journal
```

Second cas : une ligne de `sols.csv` sans source arrête le chargement avec le message « sols.csv ligne n : aucune source ».

#### A02. Contexte de l'opération

```
pour chaque unité u des deux états :
    m_u ← table(situation_<situation_u>, multiplicateur_situation)
k_delai ← table(zone_<zone>, multiplicateur_delai)
e ← arrondi(E_bati / S_p, 2)
si typologie = logement :
    clé ← logement_emprise_37 si e ≤ 0,37 ; logement_emprise_38_49 si e < 0,50 ; logement_emprise_50 sinon
sinon si typologie = tertiaire : clé ← tertiaire
sinon : Bnat_min ← non défini
Bnat_min ← table(clé, bnat_min) ; si CBS_PLU : Bnat_min ← max(Bnat_min ; 100 × CBS_PLU)
PT_min ← max(table(*, pleine_terre_min) ; PT_PLU si défini)
```

Second cas : logement, parcelle de 3 000 m², emprise de 1 350 m² : e = 0,45, Bnat_min = 35 ; avec un PLU qui impose un coefficient de biotope de 0,40 : Bnat_min = 40.

#### A03. Fermeture des surfaces

```
pour chaque état k :
    Σ_sol ← somme des A_u des unités de position sol pleine terre, sol sur dalle, eau, linéaire
    ε ← |Σ_sol − S_p|
    si ε > max(τ_abs ; τ_rel × S_p) : arrêter, journal(état, Σ_sol, S_p, ε)
```

Second cas : parcelle de 50 000 m² : tolérance de 250 m². Un écart de 300 m² arrête le calcul.

#### A04. Classement des unités

```
pour chaque unité u :
    si code_u ∈ nomenclature : h_u ← code_u
    sinon si code_u ∈ alias d'un type VB : h_u ← ce type
    sinon si parent de niveau 3 de code_u ∈ nomenclature : h_u ← ce parent
    sinon : arrêter (code inconnu)
    p_u ← position_u si compatible avec la position du type, sinon position du type
    st_u ← stade_u, ou converti depuis la classe de diamètre, ou M
```

Second cas : code saisi « J1.2 » (bâtiments résidentiels des villages) : h = VB.1.

#### A05. Reprise des données du RSEE

```
lire RSEnv/entree_projet/parcelle/surface_parcelle → S_p
pour chaque bâtiment b : lire emprise_au_sol, duree_chantier, sref
E_bati ← Σ emprise ; d_ch ← max(duree_chantier) / 12 ; S_ref ← Σ sref
pour chaque phase p : GES_p ← Σ_b Σ_{c ∈ {composant, chantier}} indicateur101(c, p, b) × sref_b / S_ref
contrôles non bloquants : surface_veg et surface_imper comparées aux unités saisies
```

Second cas : deux bâtiments de 1 000 et 500 m² de S_ref, émissions A1-A3 de 400 et 600 kg/m² : GES_A1-A3 = (400 000 + 300 000) / 1 500 = 466,7 kg/m².

#### A06. Nature de surface

```
selon h_u et p_u :
    VB.1, VB.2 → S01 ; VB.3, VB.10, VB.25, H5.6 → S02 ; VB.4 → S03
    VB.21, VB.24 → S12 ; autre type en eau → S11
    VB.15 → S09 ; VB.16 → S10
    sur dalle ou en toiture : S04 si e < 15 ; S05 si e ≤ 30 ; S06 si e < 80 ; S07 sinon
    arbre → aucune ; autre → S08
c_u ← table(n_u, coefficient_sol)
```

Second cas : toiture intensive (VB.13) de 90 cm : S07, c = 0,9.

#### A07. Facteur de support

```
f_sol,u ← c_u si p_u = sol sur dalle, sinon 1
```

Second cas : jardin domestique (VB.7) sur 25 cm de substrat : f_sol = c(S05) = 0,6.

#### A08. Pleine terre et imperméabilisation

```
PT ← Σ A_u (état projet, n_u = S08) / S_p ; PT_0 idem à l'état initial
A_imp,k ← Σ A_u (état k, n_u = S01) ; ΔA_imp ← A_imp,1 − A_imp,0
```

Second cas : réhabilitation qui remplace 400 m² d'enrobé par 250 m² de jardin et 150 m² de stabilisé sur une parcelle de 1 500 m² : ΔA_imp = -400 m² (désimperméabilisation).

#### A09. Valeur intrinsèque

```
si (h_u, valeur_intrinseque_stade_<st_u>) existe : v_u ← cette valeur
sinon : v_u ← table(h_u, valeur_intrinseque)
```

Second cas : plantation de conifères exotiques (G3.F) de stade âgé : v = 12 / 24 = 0,5. Toiture intensive (VB.13) : 0,2639.

#### A10. Score d'état des grilles à critères

```
n_app ← nombre de critères de G(h_u) dont la réponse n'est pas « sans objet »
n_ok ← nombre de réponses « oui »
S_u ← n_ok / n_app
si un critère essentiel a la réponse « non » : S_u ← min(S_u ; 0,5)
```

Second cas : prairie de valeur moyenne (grille EP2) : A, B, D, E oui ; C non ; F non (essentiel) : S = 4 / 6 = 0,667, plafonné à 0,5.

#### A11. Score d'état des boisements

```
Q_u ← Σ des 13 notes (note manquante = 1)
S_u ← (Q_u − 13) / 26
```

Second cas : toutes les notes à 3 : Q = 39, S = 1.

#### A12. Facteur d'état et classe

```
si G(h_u) existe : f_u ← 0,5 + 0,5 × S_u ; cl_u ← bon si S_u ≥ 0,85, moyen si S_u ≥ 0,65, mauvais sinon
sinon : f_u ← 1 ; cl_u ← sans état
```

Second cas : S = 0,85 : f = 0,925, classe bon.

#### A13. Valeur d'habitat

```
V^H_u ← A_u × v_u × f_u × f_sol,u × m_u
```

Second cas : chênaie-charmaie (G1.A) de 1 000 m², stade moyen (v = 0,8333), S = 0,6667 (f = 0,8333), en réservoir (m = 1,15) : V^H = 798,61 m²HE.

#### A14. Arbres

```
A_u ← A_hou si relevé, sinon n_arb × table(VB.18, surface_defaut_houppier_<classe>)
st_u ← J, M ou A selon la classe de diamètre
h_u ← VB.18a si indigène, VB.18b sinon (G5.1 hors milieu urbain)
tache_u ← tache de l'unité surplombée
```

Second cas : un platane (non indigène) de très grand diamètre, houppier non relevé : A = 764,5 m², VB.18b, stade A, v = 14 / 24 = 0,5833.

#### A15. Haies

```
A_u ← L_h × max(1 ; l_h)
h_u ← FA.1 si non indigène ; FA.2 si taillée ; FA.3 si n_esp ≥ 5 ; FA.4 sinon
st_u ← A si arbres âgés, M si arbres moyens, J sinon
```

Second cas : haie taillée de troènes indigènes de 60 m sur 0,8 m : A = 60 m² (largeur portée à 1 m), FA.2, stade J.

#### A16. Toitures, façades, bacs

```
toiture : h_u ← VB.11 si e < 15 et critère G non satisfait ; VB.12 si e ≤ 30 ou critère G satisfait ; VB.13 sinon
façade : A_u ← L_fac × min(H_fac ; 10) ; h_u ← VB.15 si enracinée, VB.16 sinon
contrôle : Σ toitures ≤ Σ emprise bâtie
```

Second cas : toiture de 35 cm sur 800 m² : VB.13, nature S06.

#### A17. Taches

```
pour chaque unité u de nature ≠ S01 et de position ≠ arbre :
    si tache_u absente : tache_u ← identifiant propre à u
A_k ← Σ A_u de la tache k + A_ext,k
pour chaque arbre : tache ← tache de l'unité surplombée (A_k inchangée)
```

Second cas : un cheminement stabilisé de 150 m² sans voisin forme sa propre tache (A = 150 m²).

#### A18. Effet de taille

```
k_taille,k ← min(1 ; max(k_min ; (A_k / A_ref)^z))
```

Second cas : A = 2 500 m² : 0,5321 ; A = 10 000 m² : 0,7218.

#### A19. Connectivité et clôtures

```
conn_k ← déduite de d_k et A_nat,k si saisis, sinon déclarée
k_C,k ← k_taille,k × m_conn(conn_k) × (k_clot si clôture étanche, sinon 1)
pour chaque unité u : k_C,u ← k_C,k de sa tache, ou 1 si n_u = S01
```

Second cas : tache de 2 500 m² contiguë à un réservoir, sans clôture : k_C = 0,5321 x 1,15 = 0,6119.

#### A20. Lumière

```
si distances saisies : L_u ← L0 si d_lum > 50 m, L1 si conforme, L2 sinon ; sinon L_u déclaré
k_lum,u ← table(lumiere_<classe>, facteur_lumiere)
```

Second cas : jardin à 60 m du point lumineux le plus proche : L0, k = 1, même si l'éclairage n'est pas conforme.

#### A21. Bruit

```
seuil ← 42 dB(A) si milieu boisé, 47 sinon
k_bruit,u ← 0,7 si L_u > seuil, sinon 1
```

Second cas : haie (milieu boisé) à 45 dB(A) : k = 0,7 ; prairie au même niveau : k = 1.

#### A22. Vitrages

```
A_vit,nt ← Σ surfaces vitrées exposées non traitées
k_vit,u ← 0,95 si une façade non traitée de plus de 10 m² est à moins de 15 m de u, sinon 1
```

Second cas : hall de 8 m² de vitrage non traité à 5 m d'un massif : k = 1 (sous le seuil de 10 m²).

#### A23. Alimentation en eau

```
k_E,u ← 0,8 si p_u = eau et alimentation artificielle, sinon 1
```

Second cas : noue (VB.19) alimentée par les toitures : k_E = 1.

#### A24. Eaux pluviales

```
A_inf ← Σ A_drain des ouvrages qui infiltrent en surface
P_inf ← A_inf / (A_imp,1 + surfaces de toiture)
```

Second cas : voirie de 300 m² drainée vers un puits d'infiltration enterré : A_inf = 0 (le puits n'infiltre pas en surface).

#### A25. Valeur à maturité

```
k_N,u ← k_lum,u × k_bruit,u × k_vit,u
V_u ← min(V_max × A_u ; V^H_u × k_C,u × k_N,u × k_E,u)
```

Second cas : la chênaie de A13 (V^H = 798,61), dans une tache de k_C = 0,6119, exposée à 50 dB(A) (k_bruit = 0,7) : V = 342,08 m²HE.

#### A26. Calendrier

```
pour t de 1 à N : φ_t ← min(1 ; max(0 ; d_ch − (t − 1))) ; τ_t ← t − d_ch
```

Second cas : chantier de 6 mois (d_ch = 0,5) : φ_1 = 0,5, τ_1 = 0,5.

#### A27. Unités conservées

```
r ← 0 si protégée, sinon r_ch
pour t de 1 à N : V_u(t) ← V_u × (1 − r × φ_t)
```

Second cas : unité protégée : V_u(t) = V_u toutes les années, chantier compris.

#### A28. Unités créées

```
d_u ← k_delai × délai(h_u, cl_u) ; à défaut délai « sans état » ; à défaut meilleure classe accessible ; à défaut 0
pour t de 1 à N :
    g ← 0 si τ_t ≤ 0 ; 1 si d_u = 0 ; min(1 ; τ_t / d_u) sinon
    V_u(t) ← D_c × V_u × g
```

Second cas : boisement créé (G1.A), bon état visé (d = 32 ans, D = 0,33), V_u = 400 m²HE, d_ch = 1 : l'année 17, g = 0,5 et V = 0,33 x 400 x 0,5 = 66 m²HE.

#### A29. Unités améliorées

```
d_u ← k_delai × délai_amélioration(h_u, cl_0, cl_u)
pour t de 1 à N :
    base ← V_u,0 × (1 − r × φ_t)
    si D_a × V_u > V_u,0 : V_u(t) ← base + (D_a × V_u − V_u,0) × g(t)
    sinon : V_u(t) ← base
```

Second cas : pâture mésotrophe (E2.1, v = 0,5417) de 2 000 m², mauvais état (S = 0,4) vers bon état (S = 0,9), D_a = 1, délai 15 ans, d_ch = 1 : V_u,0 = 758,38 ; V_u = 1 029,23 ; l'année 9, g = 8 / 15 et V = 902,83 m²HE.

#### A30. Renouvellements

```
pour chaque réfection R :
    pour R ≤ t < R + d_ind : V_u(t) ← 0
    pour t ≥ R + d_ind : V_u(t) ← D_c × V_u × min(1 ; (t − R − d_ind + 1) / d_u)
```

Second cas : jardinière (VB.23, délai d'un an) replantée l'année 25 : valeur nulle l'année 25, pleine dès l'année 26.

#### A31. Intégration

```
V_0 ← Σ V_u (état initial) ; I_0 ← N × V_0 ; I_0,30 ← 30 × V_0
pour t de 1 à N : V_1(t) ← Σ V_u(t) (état projet)
I_1 ← Σ_t V_1(t) ; I_1,30 ← Σ_{t ≤ 30} V_1(t)
DM ← Σ_t Σ_{u créées ou améliorées} (D × V_u − V_u(t))
```

Second cas : une seule unité créée de V = 100 m²HE, D = 1, d = 10 ans, d_ch = 1 : DM = 100 x 1 (année 1) + 100 x (0,9 + 0,8 + ... + 0) = 550 m²HE·an.

#### A32. Indicateurs d'ACV

```
pour chaque phase p : GES_p ← moyenne pondérée par S_ref des indicateurs 101 composants + chantier
pour chaque indicateur i ∈ {106, 107, 108, 109, 116} : POL_{i,p} idem
```

Second cas : un bâtiment sans contributeur chantier saisi : GES_A4-A5 ne contient que le transport des composants.

#### A33. Climat

```
CF ← S_terres × (1 − p_cult) × (π / δ) × TCRE
Inat_clim ← Σ_p CF × S_ref × GES_p × a_p
```

Second cas : S_ref = 3 000 m², A1-A5 = 600, B = 250 kg/m² : Inat_clim = 1,807 x 10^-3 x 3 000 x (600 x 50 + 250 x 25) = 196 511 m²HE·an.

#### A34. Bois

```
O_bois ← 10 000 × R / P
pour chaque lot r : régime ← déclaré si justifié, sinon coupe rase
Inat_bois ← Σ_r Q_r × (1 + n_remp) × O_bois × (1 − MSA_régime)
```

Second cas : 100 m³ de bois de plantation (MSA 0,30) : Inat_bois = 100 x 3 703,7 x 0,7 = 259 259 m²HE·an.

#### A35. Carrières

```
Inat_carr ← M × (1 + n_remp) × o_c × (1 − MSA_c)
Inat_sols ← Inat_bois + Inat_carr
```

Second cas : 5 000 t de granulats : 4 275 m²HE·an.

#### A36. Pollution

```
pour chaque indicateur i : POL_i ← S_ref × Σ_{p ≠ D} POL_{i,p}
```

Second cas : indicateur 106 de 1,2 mol H+ éq./m² en A1-A3 et 0,3 en B pour 2 000 m² : POL_106 = 3 000 mol H+ éq.

#### A37. Agrégation

```
Cnat ← I_0 − I_1 ; Cnat_moy ← Cnat / N ; Cnat_rel ← Cnat / I_0 si I_0 > 0
Cnat_30 ← I_0,30 − I_1,30
Inat ← Inat_clim + Inat_bois + Inat_carr ; Snat ← −(Cnat + Inat)
```

Second cas : I_0 = 0 (parking) et I_1 = 5 000 : Cnat = -5 000, Cnat_rel non défini.

#### A38. Bnat

```
Num ← Σ_{u ≠ arbre} A_u × c(n_u) + c(S13) × A_inf
Bnat ← 100 × Num / S_p
```

Second cas : parcelle de 1 000 m² : 100 m² de dalles engazonnées (0,45), 300 m² de pleine terre, 500 m² de toiture extensive (0,5), 100 m² de façade enracinée (0,4) : Bnat = 63,5.

#### A39. Incertitude

```
gen ← PCG64(graine)
pour s de 1 à n_tir :
    pour chaque paramètre j appelé : x_{j,s} ← triangulaire(a_j, c_j, b_j) tiré par gen
    recalculer A02 à A38 avec les x_{j,s}
    stocker Cnat_s, Inat_s, Snat_s, Bnat_s
centiles 5, 50, 95 ; ρ_j ← Spearman(x_j, Snat) ; top5 ← 5 plus grands |ρ_j|
```

Second cas : un paramètre de plage nulle (a = b = c), comme la période de référence, n'est pas tiré.

#### A40. Conformité

```
conf_Bnat ← Bnat ≥ Bnat_min (si défini)
conf_PT ← PT ≥ PT_min
conf_PLU ← Bnat ≥ 100 × CBS_PLU et PT ≥ PT_PLU (si définis)
niveau ← 2 si gain net de 10 %, 1 si Cnat ≤ 0, 0 sinon
attestation_permis.conforme ← conf_Bnat et conf_PT et conf_PLU
```

Second cas : logement, emprise de 40 %, Bnat = 30 : seuil 35, attestation non conforme.

#### A41. Variantes

```
pour chaque variante v : appliquer A03 à A40 à (état initial, état projet v)
ΔX_v ← X_v − X_ref
incertitude des écarts : mêmes tirages pour toutes les variantes
```

Second cas : deux variantes qui ne diffèrent que par la toiture : ΔInat = 0, ΔCnat et ΔBnat non nuls.

#### A42. Journal

```
créer resultats/<projet>/<horodatage>/
écrire 00_entrees.json, puis un fichier par étape dans l'ordre du chapitre 6
écrire rsnat.xml, rsnat.json, empreinte.txt
à la reprise : sauter les étapes dont les entrées ont la même empreinte
```

Second cas : un calcul interrompu au tirage 600 sur 1 000 reprend au tirage 601 avec la même graine et donne le même résultat qu'un calcul sans interruption.
