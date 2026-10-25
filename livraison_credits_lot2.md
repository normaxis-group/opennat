# Livraison du lot 2 des crédits OpenNAT : moteur

24 octobre 2026, branche `credits-lot1`, non poussée. Go de Cédric : « Go lot 2 : moteur des crédits OpenNAT. »

## Livré

| Fichier | Contenu |
|---|---|
| `opennat/credits/calcul.py` | formules (X1) à (X9) : variantes jouées avec les mêmes tirages, scénario de référence (usage maintenu, abandon selon C-M2, ligneux, minéral), variante d'obligations ou gain exigé, composition des états relevés (règle 8.3), 10e centile, émissions cumulées plafonnées, réserve, inversions, grille de risque avec le facteur sécheresse calculé par le module W, éligibilité, coût de revient |
| `opennat/credits/rsnatc.py` | RSNat-C en JSON et en XML, schémas générés d'une seule spécification (`schemas/rsnatc.schema.json`, `schemas/rsnatc.xsd`), empreintes des entrées et des sorties ; bloc Signature livré vide (signature au lot 3) |
| `opennat/credits/donnees.py`, `donnees/credits/credits.csv` | 26 valeurs de méthode sourcées, contrôlées comme les tables d'OpenNAT 1, hors de `donnees/` pour ne pas changer l'empreinte des tables d'OpenNAT 1 |
| `opennat/credits/commande.py`, `opennat/__main__.py` | `python -m opennat credits fichier.credits.json [--tirages N] [--graine G] [--sortie DOSSIER]` |
| `schemas/credits.schema.json` | fichier crédits : projet, variante, scénario de référence, obligations, relevés, risque, coûts, options |
| `outils/carnet_credits.py` | carnet de référence des crédits, sans import du moteur |
| `banc/credits/` | trois exemples, 20 cas, attendus du carnet, comparateur (`python -m banc.credits.comparer`) |
| `tests/test_credits.py` | 31 tests : banc, propriétés, plafond, inversion, risque, centile, découpage des tirages, reproductibilité et schémas du RSNat-C, coût, isolement d'OpenNAT 1 |

## Trois exemples calculés (1 000 tirages, 10e centile)

| Exemple | Surface | Gain prévu sur 50 ans | Réserve | Plafond | Premiers relevés |
|---|---|---|---|---|---|
| Culture restaurée en prairie de fauche avec une haie | 1 ha | 138 339 m²HE·an (161 520 en valeur centrale) | 20 % | 110 crédits | gain encore négatif à l'année 5 : aucune émission |
| Friche urbaine abandonnée, renaturée (prairie, mare, haie, arbres) | 3 000 m² | 11 395 m²HE·an | 25 % | 8 crédits | gain négatif à l'année 3 |
| Parking désimperméabilisé, avec obligation de 20 % de pleine terre | 2 000 m² | 16 405 m²HE·an | 30 % | 11 crédits | 155 m²HE·an à l'année 1 : aucune émission |

Ces exemples sont des cas d'école, pas des projets réels. Ils montrent que les crédits arrivent tard : la prairie restaurée ne dépasse la culture qu'elle remplace qu'après plusieurs années de maturation, et le 10e centile retarde encore les émissions. Pour un porteur, le revenu des crédits commence vers la dixième année ; les achats à terme (chapitre 12.1) seront nécessaires pour financer les travaux.

## Corrections de méthode apportées par le moteur

- **Convention C-X19, nouvelle** : la difficulté de création d'OpenNAT 1 (C-T7) est neutralisée dans les crédits. Avec elle, la culture restaurée en prairie (difficulté 0,33) avait un gain prévu négatif et n'aurait jamais reçu de crédit, même réussie. Le risque d'échec est déjà porté par le constat avant émission et par la réserve. Décision DC10 ajoutée au dossier du conseil. Validée par Cédric le 24/10/2026 (« Je valide la convention C-X19 : difficulté neutralisée dans les crédits. »).
- **Règle 8.3 précisée** : l'état relevé garde le délai de maturité de l'état prévu. Le test de monotonie a montré qu'un meilleur état relevé faisait baisser le gain, parce qu'OpenNAT 1 donne un délai plus long à un milieu en bon état.
- **Dernier relevé** : le relevé de l'année 50 après les travaux tombe au-delà de la période de crédit, qui court depuis le début des travaux ; il est rapporté à la dernière année de la période.
- **Supplément de destruction en période sensible** : compté dans I_projet (et dans I_obligations quand il y a une variante), ce que le texte n'écrivait pas ; à ajouter au chapitre 7 à la prochaine révision.

## Écarts au cahier des charges

- Tolérance du banc : 10⁻⁶ au lieu de 10⁻⁹. Le carnet de référence d'OpenNAT 1 et le moteur divergent déjà de l'ordre de 10⁻⁸ sur les trajectoires (banc d'OpenNAT 1 contrôlé à 10⁻³) ; les nombres de crédits, eux, sont identiques au crédit près sur les 20 cas.
- Signature XAdES ou JWS du vérificateur : reportée au lot 3 (plateforme), où se trouvent les clés.
- Vieillissement des ligneux dans le scénario de référence : non simulé ; une unité déclarée « ligneux » garde la valeur de l'état initial, ce que le journal signale.
- Opérations de construction : calculées par le moteur (Inat et Snat publiés), mais le carnet de référence des crédits ne couvre que la restauration ; aucun cas de construction au banc.

## Points relevés dans OpenNAT 1, hors périmètre

- Une unité dont le type a une grille d'état mais qui n'a aucune réponse saisie vaut un score nul pour le moteur (fiche A10) et « sans état » pour le carnet de référence. Les 73 cas du banc renseignent toujours leurs grilles, d'où un écart jamais vu. À aligner (le moteur suit la fiche).
- Rappel du lot 1 : les difficultés citées par C-T7 seraient celles de la métrique écossaise ; à vérifier.

## Contrôles

- `python -m banc.credits.comparer` : 20 cas conformes sur 20.
- `python -m pytest` : 180 tests passés (dont les 31 des crédits et le banc des 73 cas d'OpenNAT 1), en 4 min 12 s.
- `python -m banc.regression` : 38 930 grandeurs sur 38 930 inchangées ; l'empreinte des tables d'OpenNAT 1 n'a pas bougé. Les deux clés internes ajoutées au module T (`difficulte_neutralisee`, `delai_impose`) ne sont posées que par le module des crédits.
- 1 000 tirages d'un exemple : 2,4 s.

## Suite

Lot 3 (registre et plateforme) après l'avis d'avocat ; C-X19 validée par Cédric le 24/10/2026, reste soumise au conseil (DC10).
