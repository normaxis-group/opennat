# Livraison du lot 8 : dépôt du nom, transmission au conseil, version candidate

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`. Documents sur `main` ; version candidate sur la branche `candidate-bsc`, non fusionnée. Aucun dépôt en ligne.
**État :** rien n'est déposé, envoyé ni adopté. Arrêt et attente du go écrit.

## Ce qui est fait

1. **Dépôt du nom OpenNAT** : fiche « OpenNAT, dépôt du nom à l'INPI » (2 pages, Word et PDF dans `livraison/`) : marque verbale, déposant NORMATYS, classes 9, 41 et 42 avec leurs libellés, redevance de 270 € (barème de l'INPI applicable au 2 juillet 2026), points de vigilance. Sans recherche d'antériorité, à la demande de Cédric. À déposer avant toute transmission du nom hors des parties.
2. **Transmission au Biodiversity Standard Council** : `livraison/transmission_bsc/` contient la lettre de transmission au papier NORMATYS (une page de lettre, une page de pièces jointes, Word et PDF) et les huit pièces numérotées. Lettre adressée aux membres du comité, aux soins du secrétariat assuré par IRICE ; non envoyée. Générateur : `outils/transmission_bsc.py`.
3. **Version candidate** (branche `candidate-bsc`) : les trois options que le dossier recommande au conseil, appliquées au moteur, aux tables et au texte, pour qu'une décision du conseil se traduise par une seule fusion :
   - bois, option O2 (décision D1) : qualités d'habitat des régimes forestiers recalées sur LC-IMPACT, ReCiPe et EF (coupe rase 0,639, plantation 0,494, coupe sélective 0,783, faible impact 0,892) ; convention C-G5 réécrite ;
   - pollution, option P5 (décision D3) : cinq facteurs `pollution_<code>` dans `materiaux.csv`, poste Inat_pol dans le module G (fiche A36-2), élément `inat_pollution` et valeurs converties dans le RSNat, ligne dans la fiche de synthèse et l'utilitaire ; convention C-G8 réécrite ;
   - gestion (décision D7) : fin de plan étalée sur deux ans (`transition_fin_plan` dans `succession.csv`, fiche A56-4, convention C-M3), dans le moteur et dans le carnet de référence.

## Vérifications de la version candidate

- Le moteur retrouve le carnet de référence sur les 73 cas à 0,1 %, après recalcul des résultats attendus ; 143 tests sur 143 passent.
- Contrôle des tables et contrôle dimensionnel sans défaut (86 unités ; les cinq facteurs de pollution sont déclarés « non contrôlés », leurs unités de départ étant propres à chaque indicateur).
- Instantané de non-régression régénéré : 1 631 grandeurs sur 39 368 ont changé, dans le module G (633), dans l'agrégation, indicateurs et trajectoire du site compris (716), dans les trajectoires des unités du projet (258) et dans l'analyse d'incertitude ; aucune dans les autres modules.
- Exemple de l'annexe C : Cnat 3 170,5 m²HE·an (3 217,2 avant), Inat 126 398 (141 843), Snat -129 569 (-145 060). L'annexe C du texte est recalculée ; sa phrase « près de 100 fois la perte du site », déjà fausse, devient « environ 40 fois ».
- Données 1.3.0 candidate inscrites au journal des versions avec leur empreinte.

## Ce qui reste à faire à l'adoption

Régénérer l'édition complète et les documents qui citent les chiffres de la version en vigueur (guides, dossier, contrôle Carbone 4), et ajouter au banc un cas portant des indicateurs de pollution.

## Ce que le go déclenche

Déposer le nom ; signer la convention 007 ; transmettre au conseil quand ses membres sont connus ; fusionner la branche candidate après ses décisions.

## Complément (19/10/2026, sur la branche candidate)

- Le carnet de référence calcule désormais la pollution convertie de son côté (`outils/carnet_reference.py`), et le convertisseur de cas transmet les indicateurs au fichier projet.
- Cas D30 ajouté au banc : l'exemple de l'annexe C avec les indicateurs de pollution médians des neuf bâtiments réels. Le moteur retrouve le carnet (145 tests sur 145) ; la pollution ajoute 5 574 m²HE·an à Inat (6,6 % du climat). Banc : 74 cas.
- Test de propriété : la pollution ne fait jamais baisser Inat, Inat_pol lui est proportionnel, et Cnat n'en dépend pas.
- Édition complète régénérée en Markdown sur la branche (parties 2, 4, 5, 7 et 8 : facteurs de pollution, élément `inat_pollution` du récapitulatif, cas D30, chiffres recalculés). Le rendu Word et PDF se fera à l'adoption ; les sections rédigées à la main qui citent les chiffres de la version en vigueur (lecture du cas 7, contrôle Carbone 4) seront reprises à ce moment.
