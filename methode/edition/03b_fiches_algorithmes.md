#### Fiche A12. Facteur d'état et classe d'état

**Introduction**

Le facteur d'état convertit le score en coefficient multiplicateur ; la classe d'état sert au choix des délais de maturité et à l'affichage.

**Nomenclature**

Entrées : S_u (fiches A10, A11), G(h_u).

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| f_min | Facteur d'état minimal | sans unité | 0,5 (`etat_criteres.csv`, `facteur_etat_minimum`) |
| s_bon | Seuil de la classe bon | sans unité | 0,85 |
| s_moy | Seuil de la classe moyen | sans unité | 0,65 |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| f_u | Facteur d'état | sans unité, 0,5 à 1 |
| cl_u | Classe d'état | bon, moyen, mauvais, sans état |

**Description mathématique**

(A12-1) f_u = f_min + (1 - f_min) x S_u si G(h_u) existe ; f_u = 1 sinon [H3]

(A12-2) cl_u = bon si S_u >= s_bon ; moyen si s_moy <= S_u < s_bon ; mauvais si S_u < s_moy ; sans état si G(h_u) n'existe pas

**Cas limites et contrôles**

f_u ne descend jamais sous 0,5 : un habitat très dégradé garde la moitié de la valeur de son type. Un habitat plus dégradé encore change de type (une prairie retournée devient une culture).

**Cas élémentaire**

S = 0,6667 : f = 0,8333, classe moyen. S = 0,5 : f = 0,75, classe mauvais.

**Renvois**

Convention C-H2.

#### Fiche A13. Valeur d'habitat de l'unité

**Introduction**

La valeur d'habitat combine la surface, la valeur intrinsèque, l'état, le support et la situation. Les effets de taille, de connectivité, de nuisance et d'eau s'y appliquent ensuite (fiche A25).

**Nomenclature**

Entrées : A_u (fiche A03), v_u (A09), f_u (A12), f_sol,u (A07), m_u (A02).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| V^H_u | Valeur d'habitat de l'unité | m²HE |

**Description mathématique**

(A13-1) V^H_u = A_u x v_u x f_u x f_sol,u x m_u [H4]

**Cas limites et contrôles**

Pour un arbre, A_u est la surface du houppier projeté (fiche A14) ; pour une haie, longueur x largeur (fiche A15) ; pour une façade, surface de façade plafonnée à 10 m de hauteur (fiche A16).

**Cas élémentaire**

Prairie urbaine VB.26 de 450 m², v = 0,625, S = 0,6667, pleine terre, hors trame : V^H = 450 x 0,625 x 0,8333 x 1 x 1 = 234,38 m²HE.

**Renvois**

Fiches A09 à A12.

#### Fiche A14. Arbres isolés et alignements

**Introduction**

Un arbre isolé, un alignement ou un groupe d'arbres hors boisement forme une unité de position « arbre ». Sa surface est le houppier projeté ; il surplombe une autre unité sans la remplacer.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| n_arb | Nombre d'arbres de l'unité | entier | 1 et plus |
| A_hou | Houppier projeté relevé, total de l'unité | m² | facultatif |
| cl_diam | Classe de diamètre | énumération | petit, moyen, grand, très grand |
| indigene | Essence indigène | booléen | oui, non |

Paramètres intrinsèques :

| Nom | Description | Unité | Origine |
|---|---|---|---|
| A_def(cl) | Surface par défaut d'un arbre de la classe | m² | `habitats.csv`, `surface_defaut_houppier_*` (zone de protection racinaire anglaise : 40,7 ; 162,9 ; 366,4 ; 764,5 m²) |

Sorties : A_u, h_u (VB.18a si indigène, VB.18b sinon, G5.1 hors milieu urbain), st_u.

**Description mathématique**

(A14-1) A_u = A_hou si le houppier est relevé ; n_arb x A_def(cl_diam) sinon

(A14-2) st_u = J si cl_diam = petit ; M si moyen ; A si grand ou très grand (convention C-H5)

Un arbre planté est une unité créée : sa surface est le houppier visé à maturité, et sa valeur suit la maturation de la fiche A28 (délais de la ligne « Individual trees » de la métrique anglaise : 32, 27 et 10 ans selon la classe visée).

**Cas limites et contrôles**

Le houppier ne s'ajoute pas à la surface de la tache (fiche A17) : la valeur de l'arbre s'ajoute à celle de l'unité qu'il surplombe, comme dans la méthode de la Hesse (audit, point P11). Un houppier relevé supérieur à 2 fois la surface par défaut de sa classe est signalé au journal.

**Cas élémentaire**

Deux tilleuls indigènes de diamètre moyen, houppier non relevé : A_u = 2 x 162,86 = 325,7 m² ; h = VB.18a ; st = M ; v = 15 / 24 = 0,625.

**Renvois**

Point P11 de l'audit, convention C-H5.

#### Fiche A15. Haies

**Introduction**

Une haie forme une unité linéaire saisie en longueur et largeur. Son type (FA.1 à FA.4) dépend du caractère indigène des essences et de leur nombre.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| L_h | Longueur | m | supérieure à 0 |
| l_h | Largeur de la haie et de son ourlet | m | au moins 1 |
| n_esp | Nombre moyen d'espèces ligneuses indigènes par 25 m | entier | 0 et plus |
| taillee | Haie taillée régulièrement | booléen | oui, non |
| indigene | Essences surtout indigènes | booléen | oui, non |
| arbres | Haie avec arbres de haut jet | booléen | oui, non |

Sorties : A_u, h_u, st_u.

**Description mathématique**

(A15-1) A_u = L_h x l_h

(A15-2) h_u = FA.1 si non indigène ; sinon FA.2 si taillée ; sinon FA.3 si n_esp >= 5 ; sinon FA.4 (définitions EUNIS 2012)

(A15-3) st_u = M si la haie porte des arbres de haut jet de stade moyen, A s'ils sont âgés, J sinon

Les attributs E1 et E2 de la grille EH1 ne s'appliquent qu'aux haies avec arbres (fiche A10).

**Cas limites et contrôles**

Largeur inférieure à 1 m : portée à 1 m et signalée au journal.

**Cas élémentaire**

Haie champêtre de 40 m sur 2 m, six espèces indigènes par 25 m, non taillée, arbres moyens : A = 80 m², FA.3, stade M, v = 16 / 24 = 0,6667.

**Renvois**

`habitats.csv` (FA.1 à FA.4), point P11 de l'audit.

#### Fiche A16. Toitures, façades et bacs végétalisés

**Introduction**

Les surfaces végétalisées hors sol s'ajoutent aux unités au sol sans entrer dans la fermeture des surfaces. Leur valeur intrinsèque tient compte du support.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| A_toit | Surface de toiture végétalisée | m² | 0 et plus |
| e_toit | Épaisseur de substrat | cm | 3 à 300 |
| L_fac | Longueur de façade végétalisée | m | 0 et plus |
| H_fac | Hauteur végétalisée | m | 0 et plus |
| type_fac | Façade enracinée au sol ou hors sol | énumération | enracinée, hors sol |

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| H_max | Hauteur imputable | m | 10 (convention C-B1) |

Sorties : A_u, h_u, n_u.

**Description mathématique**

(A16-1) h_u (toiture) = VB.11 si e_toit < 15 ; VB.12 si 15 <= e_toit <= 30 ou si la toiture satisfait le critère G de la grille EU1 ; VB.13 si e_toit > 30

(A16-2) A_u (façade) = L_fac x min(H_fac ; H_max)

(A16-3) h_u (façade) = VB.15 si enracinée ; VB.16 sinon

La nature de surface des toitures suit la classe d'épaisseur (fiche A06) ; celle des façades est S09 ou S10.

**Cas limites et contrôles**

Une toiture végétalisée ne se superpose qu'à une unité bâtie (VB.1) : sa surface ne peut dépasser l'emprise des bâtiments qui la portent. Une toiture biodiverse de 12 cm de substrat varié qui satisfait le critère G est classée VB.12 malgré son épaisseur moyenne inférieure à 15 cm.

**Cas élémentaire**

Façade enracinée de 30 m de long, végétalisée sur 14 m : A = 30 x 10 = 300 m², VB.15, S09.

**Renvois**

Conventions C-H3, C-S2, C-B1.

### 3.5 Module C : connectivité

#### Fiche A17. Construction des taches

**Introduction**

Une tache est un ensemble d'unités végétalisées ou en eau contiguës. La contiguïté est déclarée par l'écologue ; une voirie, un bâtiment ou une clôture étanche la rompent.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| tache_u | Identifiant de tache déclaré pour l'unité | texte | facultatif |
| A_ext,k | Surface végétalisée extérieure contiguë à la tache k | m² | 0 et plus |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| T | Ensemble des taches de l'état | liste |
| A_k | Surface de la tache k | m² |

**Description mathématique**

(A17-1) Toute unité dont la nature n'est pas S01 et dont la position n'est pas « arbre » appartient à une tache, revêtements perméables (S02, S03) compris.

(A17-2) Les unités de même identifiant tache_u forment une tache ; une unité sans identifiant forme sa propre tache.

(A17-3) A_k = somme des A_u des unités de la tache k + A_ext,k [C1]

(A17-4) Un arbre reçoit la tache de l'unité qu'il surplombe ; il ne s'ajoute pas à A_k.

**Cas limites et contrôles**

Une toiture végétalisée isolée forme sa propre tache, même sur un bâtiment entouré d'espaces verts : le bâti rompt la continuité au sol. Un cheminement stabilisé isolé forme aussi la sienne : sans cette règle, un revêtement minéral échapperait à l'effet de taille et vaudrait plus qu'une petite pelouse. Une façade enracinée rejoint la tache du sol où elle s'enracine.

**Cas élémentaire**

Prairie de 450 m², jardins de 320 m², haie de 80 m² déclarés en tache P2, sans espace extérieur contigu : A_P2 = 850 m².

**Renvois**

Fiche A18.

#### Fiche A18. Effet de taille des taches

**Introduction**

Une petite tache d'habitat abrite moins d'espèces qu'une grande, selon une relation aire-espèces. La fiche calcule le facteur de taille de chaque tache.

**Nomenclature**

Entrées : A_k (fiche A17).

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| z | Exposant de la relation aire-espèces | sans unité | 0,22 (`connectivite.csv`) |
| A_ref | Surface sans effet de taille | m² | 44 000 (`connectivite.csv`) |
| k_min | Plancher du facteur | sans unité | 0,35 (`connectivite.csv`) |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| k_taille,k | Facteur de taille de la tache | sans unité, 0,35 à 1 |

**Description mathématique**

(A18-1) k_taille,k = min(1 ; max(k_min ; (A_k / A_ref)^z)) [C2]

**Cas limites et contrôles**

Le plancher est atteint pour A_k <= A_ref x k_min^(1/z) = 44 000 x 0,35^(1 / 0,22), soit 372 m². Le facteur vaut 1 au-delà de 4,4 ha.

**Cas élémentaire**

| A_k (m²) | 100 | 372 | 500 | 850 | 1 400 | 5 000 | 20 000 | 44 000 |
|---|---|---|---|---|---|---|---|---|
| k_taille | 0,35 | 0,35 | 0,3734 | 0,4197 | 0,4684 | 0,6197 | 0,8408 | 1 |

**Renvois**

Convention C-C1.

#### Fiche A19. Connectivité et clôtures

**Introduction**

La fiche combine l'effet de taille avec la connexion de la tache aux espaces naturels voisins et l'effet des clôtures.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| conn_k | Connexion de la tache | énumération | forte, moyenne, faible |
| clot_k | Clôture de la tache | énumération | aucune, perméable, étanche |
| d_k | Distance bord à bord à l'espace naturel le plus proche | m | facultative |
| A_nat,k | Surface de cet espace | m² | facultative |

Paramètres intrinsèques :

| Nom | Description | Unité | Valeur |
|---|---|---|---|
| m_forte, m_moy, m_faible | Multiplicateurs de connectivité | sans unité | 1,15 ; 1,10 ; 1 |
| d_conn | Distance de connexion moyenne | m | 200 |
| A_nat,min | Surface d'un espace naturel qui donne une connexion forte | m² | 10 000 |
| k_clot | Facteur de clôture étanche | sans unité | 0,9 |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| k_C,k | Facteur de connectivité de la tache | sans unité |

**Description mathématique**

(A19-1) conn_k = forte si la tache est contiguë à un réservoir, à un corridor ou à un espace naturel d'au moins A_nat,min ; moyenne si d_k <= d_conn sans obstacle infranchissable ; faible sinon. Si d_k et A_nat,k sont saisis, conn_k se déduit d'eux ; sinon il est déclaré.

(A19-2) m_conn,k = m_forte, m_moy ou m_faible selon conn_k

(A19-3) k_C,k = k_taille,k x m_conn,k x (k_clot si clot_k = étanche, 1 sinon) [C3]

(A19-4) k_C,u = k_C,k pour toute unité u de la tache k ; k_C,u = 1 pour une unité scellée (S01), de valeur nulle.

**Cas limites et contrôles**

Une clôture est perméable si elle offre au moins un passage de 15 x 15 cm tous les 20 m (convention C-C3). Une autoroute, une voie ferrée clôturée ou un cours d'eau canalisé sont des obstacles infranchissables pour la connexion moyenne.

**Cas élémentaire**

Tache de 850 m² à 120 m d'un parc de 2 ha, clôture étanche : k_taille = 0,4197 ; connexion moyenne 1,10 ; k_C = 0,4197 x 1,10 x 0,9 = 0,4155.

**Renvois**

Conventions C-C2, C-C3.

### 3.6 Module N : nuisances

#### Fiche A20. Lumière artificielle

**Introduction**

L'éclairage artificiel nocturne réduit l'usage des habitats par la faune nocturne, chiroptères en tête. La fiche classe chaque unité selon l'éclairage qui l'atteint.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| d_lum,u | Distance au point lumineux le plus proche | m | facultative |
| conf_u | Éclairage conforme à l'arrêté du 27 décembre 2018 et éteint en milieu de nuit | booléen | oui, non |
| L_u | Classe d'éclairage déclarée | énumération | L0, L1, L2 |

Paramètres intrinsèques : `nuisances.csv` (facteurs 1 ; 0,9 ; 0,75 ; distance d'influence 50 m).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| k_lum,u | Facteur d'éclairage | sans unité |

**Description mathématique**

(A20-1) L_u = L0 si d_lum,u > 50 m ou si aucun point lumineux ; L1 si conf_u ; L2 sinon. À défaut de distances, L_u est déclaré.

(A20-2) k_lum,u se calcule heure par heure par les fiches A51 à A53, selon la durée d'allumage de nuit, la température de couleur et la distance. Les classes L0, L1 et L2 restent des raccourcis de saisie (A53-2) : 1 ; 0,916 à Trappes ; 0,75.

Un éclairage est conforme (classe L1) s'il respecte l'arrêté du 27 décembre 2018 : température de couleur de 3 000 K au plus (2 400 K dans les espaces protégés), extinction au plus tard une heure après la fin de l'activité, flux orienté vers le bas.

**Cas limites et contrôles**

Un éclairage de sécurité permanent est de classe L2 même s'il respecte la température de couleur.

**Cas élémentaire**

Prairie à 20 m de candélabres de 3 000 K éteints à 22 h, à Trappes : 7,6 % des heures de nuit d'avril à octobre sont éclairées (A51) ; k_lum = 1 - 0,25 x 0,0756 x 0,9 x 0,75 = 0,987 (A53).

**Renvois**

Conventions C-N1, C-L1 à C-L4. Arrêté du 27 décembre 2018. Fiches A51 à A53.

#### Fiche A21. Bruit

**Introduction**

Le bruit routier réduit la densité d'oiseaux nicheurs au-delà de seuils propres au milieu.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| L_u | Niveau sonore à l'unité (indicateur Lden ou équivalent des cartes de bruit) | dB(A) | facultatif |

Paramètres intrinsèques : seuils 47 dB(A) en milieu ouvert, 42 dB(A) en milieu boisé, facteur 0,7 (`nuisances.csv`).

Sorties : k_bruit,u.

**Description mathématique**

(A21-1) Milieu boisé : types des groupes G, F (fourrés), FA (haies) et arbres ; milieu ouvert : les autres types végétalisés.

(A21-2) k_bruit,u = 0,7 si L_u dépasse le seuil du milieu ; 1 sinon ou si L_u n'est pas saisi.

**Cas limites et contrôles**

Les niveaux sonores se lisent dans les cartes de bruit stratégiques ou une étude acoustique. Les unités minérales ne sont pas concernées.

**Cas élémentaire**

Bosquet (G5.2) le long d'une route à 50 dB(A) : k = 0,7. Prairie au même niveau : k = 0,7. Prairie à 45 dB(A) : k = 1.

**Renvois**

Convention C-N2.

#### Fiche A22. Vitrages

**Introduction**

Les façades vitrées non traitées causent des collisions d'oiseaux. La fiche applique un facteur aux unités végétalisées exposées et calcule l'indicateur de surface vitrée.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| A_vit,f | Surface vitrée exposée de la façade f | m² | 0 et plus |
| trait_f | Vitrage traité contre les collisions | booléen | oui, non |
| d_vit,u | Distance de l'unité à la façade exposée la plus proche | m | facultative |

Paramètres intrinsèques : facteur 0,95, distance 15 m, surface minimale 10 m² (`nuisances.csv`).

Sorties : k_vit,u ; indicateur A_vit,nt (surface vitrée exposée non traitée).

**Description mathématique**

(A22-1) A_vit,nt = somme des A_vit,f des façades non traitées

(A22-2) k_vit,u = 0,95 si une façade non traitée de plus de 10 m² est à moins de 15 m de u ; 1 sinon

**Cas limites et contrôles**

Une façade est exposée si son vitrage reflète ou laisse voir de la végétation ou le ciel (verrières, angles vitrés, garde-corps vitrés compris).

**Cas élémentaire**

Jardin à 8 m d'un hall vitré de 40 m² non traité : k = 0,95.

**Renvois**

Convention C-N3.

### 3.7 Module E : eau, et valeur à maturité

#### Fiche A23. Alimentation des milieux en eau

**Introduction**

Un milieu en eau alimenté artificiellement fonctionne moins bien qu'un milieu alimenté par la nappe, un cours d'eau ou la pluie.

**Nomenclature**

Entrées : alim_u (naturelle, artificielle) pour les unités de position eau.

Paramètres intrinsèques : facteurs 1 et 0,8 (`eau.csv`).

Sorties : k_E,u.

**Description mathématique**

(A23-1) k_E,u = 0,8 si p_u = eau et alim_u = artificielle ; 1 sinon [E1]

**Cas limites et contrôles**

Une mare alimentée par les eaux de toiture est d'alimentation naturelle. Un bassin dont l'eau est traitée relève du type VB.21, pas de ce facteur.

**Cas élémentaire**

Mare créée remplie par le réseau d'eau potable en été : k_E = 0,8.

**Renvois**

Convention C-E4.

#### Fiche A24. Eaux pluviales infiltrées

**Introduction**

La fiche calcule la part des eaux pluviales de la parcelle infiltrées ou gérées à ciel ouvert et la surface qui ouvre droit au bonus d'infiltration de Bnat.

**Nomenclature**

Entrées :

| Nom | Description | Unité | Plage |
|---|---|---|---|
| A_drain,i | Surface imperméable dont l'eau est conduite vers l'ouvrage i | m² | 0 et plus |
| surface_i | L'ouvrage i infiltre en surface (noue, jardin de pluie, pleine terre) | booléen | oui, non |

Sorties :

| Nom | Description | Unité |
|---|---|---|
| A_inf | Surface extérieure infiltrée en surface | m² |
| P_inf | Part des surfaces imperméables gérées à ciel ouvert | sans unité |

**Description mathématique**

(A24-1) A_inf = somme des A_drain,i des ouvrages qui infiltrent en surface

(A24-2) P_inf = A_inf / (A_imp,1 + surface des toitures)

A_inf entre dans Bnat avec le coefficient 0,2 (fiche A38).

**Cas limites et contrôles**

Un puits d'infiltration enterré ne compte pas : seule l'infiltration en surface, à travers un sol vivant, ouvre droit au bonus.

**Cas élémentaire**

Toiture de 700 m² et voirie de 300 m² ; la toiture est conduite vers une noue : A_inf = 700 m², P_inf = 700 / 1 700 = 0,41 (la toiture compte au dénominateur).

**Renvois**

Conventions C-E5, C-B1.

#### Fiche A25. Valeur à maturité et plafond

**Introduction**

La valeur à maturité d'une unité réunit sa valeur d'habitat et les effets de taille, de connectivité, de nuisance et d'eau. Elle est plafonnée.

**Nomenclature**

Entrées : V^H_u (A13), k_C,u (A19), k_lum,u, k_bruit,u, k_vit,u (A20 à A22), k_E,u (A23), A_u.

Paramètres intrinsèques : V_max = 1,15 m²HE/m².

Sorties :

| Nom | Description | Unité |
|---|---|---|
| k_N,u | Facteur de nuisances | sans unité |
| V_u | Valeur de l'unité à maturité | m²HE |

**Description mathématique**

(A25-1) k_N,u = k_lum,u x k_bruit,u x k_vit,u [N1]

(A25-2) V_u = min(V_max x A_u ; V^H_u x k_C,u x k_N,u x k_E,u) [H5]

**Cas limites et contrôles**

Le plafond n'agit que pour une unité de valeur intrinsèque élevée, en bon état, en réservoir et dans une tache très connectée : par exemple v = 1, m = 1,15, k_C = 1,15 donnerait 1,3225 m²HE/m², ramené à 1,15.

**Cas élémentaire**

Prairie de l'annexe C : V^H = 234,38 ; k_C = 0,4197 ; k_N = 0,9160 (éclairage conforme éteint à 1 h, fiche A53) ; k_E = 1 : V = 234,38 x 0,4197 x 0,9160 = 90,10 m²HE.

**Renvois**

Convention C-H7.
