# Banc de validation et de non-régression

Le banc vérifie trois choses, chacune par une commande.

| Commande | Ce qui est vérifié | Durée |
|---|---|---|
| `python -m banc.comparer [motif]` | Le moteur retrouve le carnet de calcul de référence sur les 73 cas (exigence E10) | 1 à 3 min |
| `python -m banc.regression` | Aucune des 38 930 grandeurs figées dans `regression.json` n'a bougé, ni l'empreinte des tables | 1 à 2 min |
| `python -m banc.carbone4` | Ordre de grandeur du module G face à l'étude Carbone 4 (écrit `carbone4.json`) | 1 s |

`python -m pytest` lance le tout, avec les tests de propriétés et le contrôle dimensionnel (`tests/test_banc.py`, `tests/test_proprietes.py`).

## Les huit cas tests du cahier des charges

Chaque cas a un fichier d'entrée (`banc/cas/`), un calcul de référence fait indépendamment du moteur, des résultats attendus et une tolérance.

- Calcul de référence : `outils/carnet_reference.py`, qui applique les fiches algorithmes de la partie 3 sans rien partager avec le moteur (aucun import de `opennat/`). Chaque cas y est déroulé pas à pas, grandeurs intermédiaires comprises, dans la partie 8 de l'édition complète de la méthode (`methode/edition/08_cas_validation.md`, section du même nom que le cas). Les hypothèses des cas sont dans `outils/edition/cas_validation.py`.
- Résultats attendus : `banc/attendus.json`, écrit par le carnet (`python banc/convertir_cas.py`), pour chaque cas : V_0, I_0, I_1, Cnat, Cnat sur 30 ans, dette de maturité, supplément de destruction, Inat, Snat, Bnat, part de pleine terre, arrosage, niveau, et pour chaque unité sa valeur V et sa trajectoire annuelle sur 50 ans.
- Tolérance : 0,1 % en relatif, ou 0,05 en absolu pour une grandeur proche de zéro, sur chacune de ces grandeurs et sur chaque année de chaque trajectoire.
- Résultat attendu qualitatif : celui du cahier des charges, vérifié par `tests/test_banc.py::test_resultats_attendus_des_huit_cas`.

| Cas du cahier des charges | Fichier d'entrée | Attendu | Cnat | Inat | Snat | Bnat | Niveau |
|---|---|---|---|---|---|---|---|
| 1. Friche urbaine imperméabilisée devenue résidence avec jardin | `cas_1.json` | gain : Cnat négatif | -25 922 | 217 937 | -192 015 | 66,7 | 2 |
| 2. Prairie naturelle en périphérie, construite en logements | `cas_2.json` | forte perte : Cnat relatif au-delà de 0,5 | 333 809 | 584 993 | -918 802 | 50 | 0 |
| 3. Bureaux sur dalle avec toiture végétalisée | `cas_3.json` | pleine terre nulle, Bnat porté par la dalle et la toiture | -10 348 | 635 531 | -625 183 | 46 | 2 |
| 4. Réhabilitation sans emprise nouvelle | `cas_4.json` | petit gain, moins du quart de celui du cas 1 | -2 392 | 61 737 | -59 345 | 32 | 2 |
| 5. Projet en réservoir de biodiversité | `cas_5.json` | perte plus forte que le cas 2 | 383 880 | 584 993 | -968 873 | 50 | 0 |
| 6. Mare et haies créées (effet de maturation) | `cas_6.json` | gain, dette de maturité élevée | -12 420 | 171 | 12 249 | 92,8 | 2 |
| 7. Bâtiment bois face au même bâtiment béton | `cas_7a.json`, `cas_7b.json`, `cas_7c.json` | même Cnat ; Inat bois non justifié > bois justifié > béton | 9 443 | 301 754 ; 1 867 574 ; 1 200 908 | -311 196 ; -1 877 017 ; -1 210 350 | 46,7 | 0 |
| 8. Site méditerranéen face au même site continental | `cas_8a.json`, `cas_8b.json`, `cas_8c.json` | Cnat continental < méditerranéen < méditerranéen à délais allongés | -12 420 ; -9 614 ; -8 629 | 171 | 12 249 ; 9 443 ; 8 458 | 92,8 | 2 |
| Exemple de l'annexe C | `exemple_de_l_annexe_c.json` | valeurs de l'annexe C | 3 217 | 141 843 | -145 060 | 59 | 0 |

Valeurs en m²HE·an, Bnat en points. Les 60 autres cas (C01 à C31, D01 à D29) déclinent une opération type sur cinq sites, trois tailles, trois emprises, trois durées de chantier, trois situations, trois éclairages, quatre zones, et chacun des mécanismes dynamiques (calendrier du chantier, toitures, arrosage, sols, zones climatiques, niveaux de réchauffement, mares, éclairage horaire, gestion).

## Non-régression

`regression.json` fige toutes les grandeurs numériques de toutes les étapes de chacun des 73 cas (une série est résumée par sa longueur, sa somme, son minimum et son maximum) et une analyse d'incertitude de l'exemple de l'annexe C avec sa variante « plan de gestion de 50 ans » (200 tirages, graine par défaut : centiles et paramètres influents). Tolérance : 10⁻⁶ en relatif.

Quand une évolution est voulue (correction de fiche, nouvelle donnée) :

1. lancer `python -m banc.regression` et lire chaque écart signalé ;
2. si les tables ont changé, inscrire la nouvelle version des données et son empreinte au `JOURNAL_DES_VERSIONS.md` (le test `test_version_des_donnees_au_journal` le vérifie) ;
3. régénérer l'instantané par `python -m banc.regression --ecrire` et le committer avec l'évolution, en citant les grandeurs qui ont bougé dans le message.

## Contrôle d'ordre de grandeur du module G

`carbone4.py` ramène le bâtiment type de l'étude Carbone 4 (octobre 2026) et le module G d'OpenNAT au m² de plancher, avec des hypothèses déclarées. La lecture des écarts est dans `documentation/controle_carbone4.md`.
