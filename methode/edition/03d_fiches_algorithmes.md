### 3.10 Agrégation et Bnat

#### Fiche A37. Agrégation des indicateurs (étape E3)

**Introduction**

L'étape E3 réunit les sorties des modules T et G en indicateurs de l'opération.

**Nomenclature**

Entrées : I_0, I_1, I_0,30, I_1,30, DM (fiche A31) ; Inat_clim, Inat_bois, Inat_carr (fiches A33 à A35) ; S_p, S_ref.

Sorties :

| Nom | Description | Unité |
|---|---|---|
| Cnat | Consommation de nature sur le site | m²HE·an |
| Cnat_moy | Consommation moyenne annuelle | m²HE |
| Cnat_rel | Consommation relative | sans unité |
| Cnat_30 | Consommation sur 30 ans | m²HE·an |
| Inat | Biodiversité grise | m²HE·an |
| Snat | Solde de nature | m²HE·an |
| ratios | Cnat / S_p, Inat / S_ref | m²HE·an/m² |

**Description mathématique**

(A37-1) Cnat = I_0 - I_1 [A1]

(A37-2) Cnat_moy = Cnat / N

(A37-3) Cnat_rel = Cnat / I_0 si I_0 > 0 ; non défini sinon

(A37-4) Cnat_30 = I_0,30 - I_1,30

(A37-5) Inat = Inat_clim + Inat_bois + Inat_carr [G1]

(A37-6) Snat = -(Cnat + Inat) [A2]

**Cas limites et contrôles**

Sur un site sans valeur initiale (I_0 = 0), Cnat est négatif ou nul et Cnat_rel n'est pas défini : le niveau 2 (gain net de 10 %) se juge alors sur Cnat < 0.

**Cas élémentaire**

Annexe C : Cnat = 671,9 ; Cnat_rel = 0,050 ; Inat = 141 843 ; Snat = -142 515 m²HE·an.

**Renvois**

Fiches A31, A33 à A35.

#### Fiche A38. Bnat

**Introduction**

Bnat mesure la place laissée à la nature par le plan masse, indépendamment des habitats qui y seront aménagés. C'est un coefficient de biotope par surface multiplié par 100.

**Nomenclature**

Entrées : A_u et n_u des unités de l'état projet (au sol, en eau, en toiture, en façade) ; A_inf (fiche A24) ; S_p.

Paramètres intrinsèques : c(S01) à c(S13) (`sols.csv`).

Sorties :

| Nom | Description | Unité |
|---|---|---|
| Bnat | Besoin de nature de la conception | points |
| CBS | Coefficient de biotope équivalent | sans unité |

**Description mathématique**

(A38-1) Num = somme des A_u x c(n_u) pour les unités de l'état projet, hors arbres + c(S13) x A_inf

(A38-2) Bnat = 100 x Num / S_p [A3]

(A38-3) CBS = Bnat / 100

Les toitures et façades entrent au numérateur sans entrer au dénominateur : Bnat peut dépasser 100 (convention C-B1).

**Cas limites et contrôles**

Les arbres n'entrent pas dans Bnat : ils surplombent des surfaces déjà comptées, et Bnat ignore le type d'habitat. Une même surface ne compte qu'une fois : une toiture qui porte à la fois des panneaux et de la végétation (toiture biosolaire) compte pour sa seule surface végétalisée.

**Cas élémentaire**

Annexe C : Num = 150 x 0,2 + 850 x 1 + 500 x 0,6 = 1 180 ; Bnat = 59,0.

**Renvois**

`sols.csv`. Conventions C-S1, C-B1.

### 3.11 Incertitude, conformité, variantes et journal

#### Fiche A39. Analyse d'incertitude (étape E4)

**Introduction**

Chaque coefficient porte une plage d'incertitude. L'étape E4 propage ces plages dans toute la chaîne de calcul par tirages aléatoires.

**Nomenclature**

Entrées : toutes les entrées du projet ; graine ; n_tir (nombre de tirages, 1 000 au moins).

Paramètres intrinsèques : pour chaque valeur de `donnees/` appelée par le calcul, la valeur centrale c, la borne basse a et la borne haute b.

Sorties :

| Nom | Description | Unité |
|---|---|---|
| X_5, X_50, X_95 | Centiles 5, 50 et 95 de chaque indicateur X (Cnat, Inat, Snat, Bnat) | unité de X |
| ρ_j | Corrélation de rang de Spearman entre le paramètre j et Snat | sans unité |
| top5 | Les cinq paramètres de plus forte corrélation en valeur absolue | liste |

**Description mathématique**

(A39-1) Pour chaque tirage s de 1 à n_tir et chaque paramètre j appelé : x_{j,s} tiré selon une loi triangulaire de mode c_j, de bornes a_j et b_j ; si a_j = b_j, x_{j,s} = c_j.

(A39-2) Le calcul des fiches A02 à A38 est refait avec les x_{j,s}. Les entrées du projet ne sont pas tirées.

(A39-3) X_q = centile q de la série des X_s

(A39-4) ρ_j = corrélation de Pearson entre les rangs des x_{j,s} et les rangs des Snat_s

(A39-5) top5 = les cinq j de plus grand | ρ_j |

Un même paramètre appelé par plusieurs unités (par exemple la valeur intrinsèque d'un type présent deux fois) prend la même valeur dans un tirage : les tirages portent sur les paramètres, pas sur leurs occurrences.

La valeur centrale affichée est celle du calcul aux valeurs centrales, pas X_50.

**Cas limites et contrôles**

Générateur : générateur pseudo-aléatoire de la bibliothèque numpy (PCG64), initialisé par la graine. À graine et à entrées identiques, les résultats sont identiques au bit près (exigence E7).

**Cas élémentaire**

Paramètre CF de plage 5,43 x 10^-4 à 5,19 x 10^-3 et de mode 1,807 x 10^-3 : sa moyenne triangulaire est (a + b + c) / 3 = 2,51 x 10^-3, supérieure au mode ; les tirages déplacent donc Inat_clim vers le haut en moyenne. C'est pourquoi la valeur affichée reste le calcul central et l'intervalle est donné à côté.

**Renvois**

Conventions C-I1, C-I2.

#### Fiche A40. Conformité et attestations (étape E5)

**Introduction**

L'étape E5 compare les indicateurs aux seuils et prépare les deux attestations : au dépôt du permis de construire et à l'achèvement.

**Nomenclature**

Entrées : Bnat, PT, Cnat, Cnat_rel, I_0 ; Bnat_min, PT_min, CBS_PLU, PT_PLU (fiche A02).

Paramètres intrinsèques : `seuils.csv`.

Sorties :

| Nom | Description | Unité |
|---|---|---|
| conf_Bnat | Bnat >= Bnat_min | booléen |
| conf_PT | PT >= PT_min | booléen |
| conf_PLU | Respect du coefficient de biotope et de la pleine terre du PLU | booléen ou sans objet |
| niveau_Cnat | Niveau atteint par le site | 0, 1, 2 |
| attestation_permis | Contenu de l'attestation au permis | bloc XML |
| attestation_achevement | Contenu de l'attestation à l'achèvement | bloc XML |

**Description mathématique**

(A40-1) conf_Bnat = (Bnat >= Bnat_min) ; sans objet si Bnat_min n'est pas défini

(A40-2) conf_PT = (PT >= PT_min)

(A40-3) conf_PLU = (Bnat >= 100 x CBS_PLU) et (PT >= PT_PLU) quand le PLU les fixe

(A40-4) niveau_Cnat = 2 si Cnat <= -0,10 x I_0 ; 1 si Cnat <= 0 ; 0 sinon

(A40-5) L'attestation au permis conclut à la conformité si conf_Bnat, conf_PT et conf_PLU sont vrais (ou sans objet). Si conf_PLU est faux, elle mentionne le minimum du PLU et l'écart, et ne conclut pas à la conformité (convention C-P1).

**Cas limites et contrôles**

L'attestation au permis ne porte que sur les données du plan masse ; elle n'affiche ni Cnat, ni Inat, ni Snat. L'attestation à l'achèvement reprend tout le RSNat, sur les surfaces réalisées.

**Cas élémentaire**

Bnat = 59,0, Bnat_min = 45, PT = 0,425, PT_min = 0,15, PLU sans exigence : conformité au permis. Cnat = 671,9 > 0 : niveau 0 à l'achèvement.

**Renvois**

`seuils.csv`. Conventions C-E6, C-E7, C-P1. Partie 7 (RSNat).

#### Fiche A41. Variantes

**Introduction**

Un projet peut porter plusieurs variantes de l'état projet. L'état initial et le contexte leur sont communs.

**Nomenclature**

Entrées : état initial, contexte, et pour chaque variante v : unités de l'état projet, données de matériaux, éclairage, clôtures.

Sorties : tous les indicateurs par variante ; écarts entre chaque variante et la variante de référence.

**Description mathématique**

(A41-1) Pour chaque variante v, les fiches A03 à A40 sont appliquées à (état initial, état projet v).

(A41-2) ΔX_v = X_v - X_ref pour chaque indicateur X

L'analyse d'incertitude d'une comparaison se fait avec les mêmes tirages pour toutes les variantes : les écarts ΔX_v ont alors leur propre intervalle, plus étroit que celui de chaque variante.

**Cas limites et contrôles**

Les variantes ne peuvent pas modifier l'état initial : une variante qui conserve une haie la déclare conservée, elle ne la retire pas de l'état initial.

**Cas élémentaire**

Variante B de l'annexe C avec bois justifié en coupe sélective : ΔInat = 33 333 - 55 556 = -22 222 m²HE·an.

**Renvois**

Point 4.5 de la partie 1.

#### Fiche A42. Journal des calculs et reprise

**Introduction**

Chaque étape écrit ses sorties dans un dossier de résultats, pour qu'on puisse relire tout résultat intermédiaire et reprendre un calcul interrompu.

**Nomenclature**

Sorties : dossier de résultats d'un calcul, contenant pour chaque étape un fichier de sorties et un fichier de journal.

**Description mathématique**

(A42-1) Dossier `resultats/<identifiant du projet>/<horodatage>/`, avec :
- `00_entrees.json` : entrées après valeurs par défaut ;
- `01_E1_contexte.json` à `12_E5_conformite.json` : sorties de chaque étape et module, dans l'ordre du chapitre 6 de la partie 1 ;
- `08_T_trajectoires.csv` : une ligne par unité et par année ;
- `11_E4_tirages.csv` : une ligne par tirage ;
- `journal.txt` : valeurs par défaut appliquées, contrôles non bloquants, durées ;
- `rsnat.xml` et `rsnat.json` : récapitulatif standardisé ;
- `empreinte.txt` : SHA-256 des entrées, des tables et des sorties.

(A42-2) Reprise : une étape dont le fichier de sorties existe et dont les entrées ont la même empreinte n'est pas recalculée.

**Cas limites et contrôles**

Un calcul interrompu pendant l'étape E4 reprend au premier tirage non écrit, avec la même graine.

**Renvois**

Exigences E5, E8 du cahier des charges.
