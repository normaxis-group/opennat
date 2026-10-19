# Livraison du lot 2 : moteur de calcul OpenNAT

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne.
**État :** lot livré, rien n'est publié. Arrêt et attente du go écrit avant le lot 3 (utilitaire).

## Ce qui est fait

Le moteur `opennat/` applique la méthode OpenNAT v1 telle que l'édition complète la décrit, modules dynamiques compris. Il suit l'architecture d'OpenBCE : Python, un paquet à plat, un module par module de méthode, numpy, tests pytest, banc à part.

```
python -m opennat calcul projet.json      # dossier de résultats et RSNat
```

| Exigence du cahier des charges (§ 5.1) | Réalisation |
|---|---|
| Un module de code par module de méthode, chaque fonction cite son équation | 13 modules de calcul (`conformite`, `pretraitement`, `sol`, `habitats`, `connectivite`, `nuisances`, `eau`, `climat`, `hydrique`, `temps`, `materiaux`, `agregation`, `incertitude`) ; chaque fonction nomme sa fiche et ses équations ; un test le vérifie |
| Aucune valeur numérique en dur, une donnée sans source fait échouer le chargement | Le chargeur `donnees.py` refuse toute ligne sans source, sans référence, de type inconnu, de convention non définie ou hors de sa plage, avec la table, la ligne et la règle. Les constantes des équations publiées (FAO-56, ISO 2533) et les valeurs de règle sont passées dans `donnees/constantes.csv` (70 lignes). Un test cherche les nombres écrits dans le code et échoue s'il en trouve un qui n'est pas une conversion d'unité ou une garde numérique |
| Journal des calculs | `resultats/<projet>/<horodatage>/` : entrées après valeurs par défaut, un dossier par variante avec les sorties de chaque étape dans l'ordre du chapitre 6, trajectoires annuelles, tirages, journal, empreintes, RSNat |
| Exécution par étapes, progression, interruption et reprise | Progression affichée étape par étape et bloc de tirages par bloc ; `--reprendre` relit les tirages écrits et reprend au premier bloc manquant ; reprise refusée si les entrées ou les tables ont changé |
| Variantes | Toutes les variantes d'un projet se calculent sur le même état initial ; l'incertitude donne en plus l'intervalle de l'écart de chaque variante à la référence, sur les mêmes tirages |
| Déterminisme | Chaque paramètre a sa propre graine, dérivée de la graine du calcul et de sa clé : ses tirages ne dépendent ni de l'ordre d'appel ni du découpage en blocs ; deux calculs donnent le même résultat au bit près, une reprise aussi |
| Ligne de commande | `opennat calcul`, `opennat valider`, `opennat controle`, `opennat schemas` |

Formats (§ 5.2) : `schemas/projet.schema.json` (fichier projet, identifiant géométrique prévu), `schemas/rsnat.xsd` et `schemas/rsnat.schema.json` (322 éléments), générés d'une seule spécification (`opennat/rsnat_spec.py`) qui sert aussi à la partie 7 de l'édition.

Reprise du RSEE (fiche A05) : un fichier projet peut citer un RSEE ; le moteur en lit la parcelle, les bâtiments (S_ref, emprise, durée du chantier), les indicateurs 101, 106 à 109 et 116 des contributeurs composants et chantier par phase, la zone climatique (`Datas_Comp/donnees_generales/operation/zone_climatique`), le département et l'altitude. Le lecteur a été éprouvé sur les six RSEE d'ARKEMEP qui portent la branche RSEnv ; il retrouve les valeurs citées en fiche A32. Ces RSEE sont des données de clients : ils ne sont pas copiés dans le dépôt, les tests emploient un RSEE fabriqué.

## Recette du lot 2 (§ 9)

- [x] `opennat calcul` produit le dossier de résultats et le RSNat pour chaque cas test : les 73 cas du banc (8 du cahier des charges et leurs variantes, 31 complémentaires, 29 dynamiques).
- [x] Une ligne de données sans source fait échouer le chargement avec un message clair : « Tables de données refusées : connectivite.csv, ligne 2 (* ; exposant_aire_especes) : aucune source » (test).
- [x] Les trajectoires annuelles sur 50 ans sont présentes pour chaque unité (`09_T_trajectoires.csv` et RSNat).
- [x] Deux exécutions à graine identique donnent un résultat identique, au bit près, et une reprise après interruption aussi (tests).
- [x] Le RSNat est valide selon ses schémas XSD et JSON (contrôle à chaque calcul, et test).

## Banc et tests

`python -m banc.comparer` calcule les 73 cas et les compare au carnet de référence, écrit indépendamment du moteur : **73 cas sur 73 à 0,1 % près**, sur les indicateurs (I_0, I_1, Cnat, Cnat sur 30 ans, Inat, Snat, Bnat, dette de maturité, supplément pour destruction, arrosage, niveau), sur la valeur de chaque unité et sur chacune de ses 50 valeurs annuelles. Durée : 2 min 40 s.

`python -m pytest` : 47 tests. Chargeur et refus des tables ; tirages reproductibles et indépendants du découpage ; absence de constante dans le code ; un test par fiche sur son cas élémentaire (A04, A06, A10 à A12, A14 à A16, A18, A19, A32 à A35, A38, A43 à A46, A48 à A51, A53, A54, A56 à A58) ; lecture d'un RSEE fabriqué ; calcul de bout en bout avec RSEE et deux variantes (écart de bois de -22 222 m²HE·an, celui de la fiche A41) ; déterminisme et reprise ; fermeture des surfaces bloquante ; six cas du banc ; une propriété (remplacer 100 m² de voirie par une prairie fait baisser Cnat et monter Bnat).

## Performances

Calcul aux valeurs centrales de l'annexe C : 4 s (le bilan hydrique horaire en prend la plus grande part). Analyse d'incertitude : les tirages se calculent par blocs de 100, toute la chaîne étant jouée sur des tableaux ; 1 000 tirages de l'annexe C : 3 min.

Résultat sur l'annexe C (1 000 tirages, graine 20261018) :

| Indicateur | Valeur centrale | Centile 5 | Médiane | Centile 95 |
|---|---|---|---|---|
| Cnat (m²HE·an) | 3 217 | 1 042 | 2 951 | 4 525 |
| Inat (m²HE·an) | 141 843 | 106 850 | 171 851 | 267 048 |
| Snat (m²HE·an) | -145 060 | -270 615 | -174 807 | -109 037 |
| Bnat (points) | 59,0 | 57,4 | 59,6 | 62,5 |

Paramètres les plus influents sur Snat : le facteur de caractérisation du climat (corrélation de rang -0,97), puis la production biologique des forêts (0,21) et le rapport de bois rond par m³ de produit (-0,19). Les deux suivants (0,08) sont au niveau du bruit. La médiane d'Inat dépasse la valeur centrale parce que la loi du facteur climat est dissymétrique (fiche A39) : la valeur affichée reste le calcul central.

## Corrections apportées aux données et à l'édition

- La grille d'état de chaque type est désormais écrite dans la nomenclature (colonne `grille_etat`) : le moteur ne lit plus les sources anglaises. En l'écrivant, une erreur de la règle d'affectation est apparue : les fourrés (« Mixed scrub ») tombaient dans la grille des landes, parce que le mot « heath » était cherché dans le nom du groupe ; ils relèvent de la grille des fourrés EF1. Les fiches habitats sont régénérées.
- Les surfaces scellées, revêtues ou nues et les cultures sont explicitement sans grille, comme l'annexe C le traitait déjà (convention C-H6 complétée).
- Bornes des classes d'emprise du seuil de Bnat (0,37 et 0,50) ajoutées à `seuils.csv` ; constantes des équations et valeurs de règle dans `constantes.csv` (partie 2 de l'édition).
- L'édition complète est régénérée : 2 078 pages (`livraison/`), le texte de la méthode seul 23 pages.
- Fiche A42 réécrite avec les fichiers réels du journal ; fiche A25 recalée sur le facteur d'éclairage horaire ; partie 7 complétée du dictionnaire du fichier projet, généré depuis son schéma, et d'un exemple de RSNat écrit par le moteur.

## Écarts avec le cahier des charges

1. **Reprise par étape.** La fiche A42 prévoit qu'aucune étape déjà écrite ne se recalcule. Le moteur l'applique à l'étape E4, seule étape longue ; les étapes E1 à E3 et E5 se refont en quelques secondes à chaque reprise. La fiche A42 le dit.
2. **Interfaces.** OpenBCE a aussi une API HTTP et un serveur MCP. Le moteur OpenNAT n'a que la ligne de commande ; l'API servira l'utilitaire du lot 3.
3. **Paramètres influents.** Les corrélations de rang sont bruitées sous 1 000 tirages : avec 200 tirages, un paramètre sans effet a pris 0,26 de corrélation par hasard avec le facteur climat, qui domine Snat. Le défaut reste 1 000 tirages.
4. **Zone climatique.** Le moteur ne déduit pas la zone du département : il la lit dans le RSEE ou la demande. La table des zones par département d'OpenBCE est marquée « à vérifier » et n'a pas été reprise.

## Questions ouvertes

Les questions du lot 1 restent posées (calibrage du bois, licence de la convention NORMATYS-IRICE, relecture des correspondances par un écologue d'IRICE, licence HabRef). La question du lot 3 viendra avec son go.

## Ce que le go déclenche

Lot 3, utilitaire : saisie par onglets qui suivent la méthode, contrôle de fermeture en direct, import et export du fichier projet, lancement du calcul avec suivi des étapes, résultats (indicateurs, détail par module, trajectoire, biodiversité grise par poste, incertitude, comparaison des variantes), édition du RSNat et d'une fiche de synthèse PDF, consultation des résultats intermédiaires.
