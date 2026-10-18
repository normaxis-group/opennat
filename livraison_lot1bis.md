# Livraison du lot 1 bis : édition complète de la méthode OpenNAT v1

**Date :** 18 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, git privé, aucun dépôt en ligne.
**État :** lot livré, rien n'est publié. Arrêt et attente du go écrit avant le lot 2 (moteur).

## Ce qui est fait

L'édition complète suit le plan de l'annexe III de la RE2020 : texte général, données conventionnelles séparées, fiches algorithmes, fiches d'application.

| Partie | Contenu | Fichier source |
|---|---|---|
| 1 | Texte de la méthode (version noyau du lot 1, mise à jour) | `methode/OpenNAT_v1.md` |
| 2 | Données conventionnelles : nomenclature, tableaux synoptiques, registre de toutes les valeurs avec leur source, extraits des sources primaires | `methode/edition/02_donnees_conventionnelles.md`, généré |
| 3 | 42 fiches algorithmes A01 à A42 au format Th-BCE : nomenclature des variables, équations numérotées, cas limites, cas élémentaire chiffré, renvois | `methode/edition/03a` à `03d` |
| 4 | 191 fiches habitats H001 à H191 : définition, correspondances EUNIS 2022, CORINE Biotopes et habitats d'intérêt communautaire, espèces caractéristiques, valeur et stades, grille d'état, délais, difficultés, valeurs de référence, trajectoire de création | `methode/edition/04_fiches_habitats.md`, généré |
| 5 | 25 fiches d'application F01 à F25 | `methode/edition/05_fiches_application.md` |
| 6 | Protocoles de relevé des 12 grilles d'état, liste des espèces exotiques envahissantes de l'Union | `methode/edition/06_protocoles.md` |
| 7 | RSNat : schéma XSD (252 éléments), dictionnaire des données, exemple validé contre le schéma | `methode/edition/07_rsnat.md`, `schemas/` |
| 8 | Huit cas de validation déroulés par un carnet de calcul de référence indépendant du moteur | `methode/edition/08_cas_validation.md`, `outils/carnet_reference.py` |
| 9 | 47 conventions | `methode/conventions.md` |
| 10 | Bibliographie | `methode/bibliographie.md` |

Assemblage : `outils/edition/assembler.py` produit `methode/OpenNAT_v1_edition_complete.md`, que `outils/methode_docx.py` convertit en Word au papier NORMATYS : `livraison/Méthode de calcul OpenNAT v1, édition complète.docx` et son PDF.

## Volume

L'édition complète rendue par LibreOffice fait **949 pages** : partie 1, 17 pages ; partie 2, 346 ; partie 3, 42 ; partie 4, 467 ; partie 5, 5 ; partie 6, 8 ; partie 7, 21 ; partie 8, 30 ; parties 9 et 10, 12. C'est la moitié de l'annexe III (1 854 pages), et moins que les 1 400 à 1 500 pages annoncées au lot 1 : les fiches algorithmes, les fiches d'application, les protocoles et les cas de validation sont plus courts que prévu, parce que chacun dit ce qu'il a à dire sans remplissage.

Ce qui peut encore s'ajouter, avec du contenu réel :
- partie 4 : listes complètes des espèces, des correspondances CORINE et des habitats d'intérêt communautaire, variantes sur dalle de chaque trajectoire, exemple de saisie par fiche (environ 200 pages) ;
- partie 5 : un calcul chiffré par fiche d'application, fait par le carnet de référence (environ 100 pages) ;
- partie 8 : une trentaine de cas supplémentaires (typologies, tailles de parcelle, zones, chantiers phasés), qui serviront aussi au banc du lot 4 (environ 120 pages) ;
- partie 3 : pseudo-code et deuxième cas élémentaire par fiche (environ 80 pages) ;
- partie 2 : liste allemande complète (668 valeurs) et onglets anglais complets (environ 40 pages).

Soit environ 1 500 pages. Atteindre 1 854 pages demanderait d'ajouter du volume qui n'apporte rien au calcul.

## Ajouts aux données depuis le lot 1

- Délais d'amélioration de la métrique anglaise (onglet G-5) : 501 valeurs ; l'équation T4 les utilise au lieu des délais de création.
- Grille d'état des vergers (EV1, fiche 17A anglaise) et règle d'affectation des grilles par type (convention C-H6 complétée).
- Surfaces par défaut des houppiers par classe de diamètre (onglet G-3), qui manquaient.
- Conventions de relevé C-R1 à C-R5 ; C-H8 étendue aux listes régionales d'espèces envahissantes ; C-C3 complétée (murets).
- Définitions françaises des 165 types EUNIS, traduites et adaptées des définitions de l'Agence européenne pour l'environnement (CC BY 4.0), et définitions des 26 types urbains.

## Ce que les cas de validation montrent

- Les sens attendus par le cahier des charges sont retrouvés : gain sur la friche imperméabilisée (cas 1), forte perte sur la prairie (cas 2, 84 % de la valeur intégrée), perte plus forte en réservoir dans le rapport du multiplicateur 1,15 (cas 5), dette de maturité sur les habitats créés (cas 6).
- Les bureaux sur dalle (cas 3) atteignent le seuil de Bnat du tertiaire mais pas la pleine terre minimale de 15 %, nulle.
- La zone méditerranéenne (cas 8) ne change rien en v1, faute de source qui module les délais.
- **Bois contre béton (cas 7)** : avec les conventions actuelles, le bâtiment en bois a une biodiversité grise six fois plus forte que le même bâtiment en béton (1,87 million contre 0,30 million de m²HE·an), quatre fois s'il vient d'une coupe sélective justifiée. L'occupation des forêts l'emporte sur le climat gagné. Le sens de l'écart est celui de la littérature citée par l'audit ; son ampleur repose sur trois conventions (C-G4 rapport de 2 m³ de bois rond par m³ de produit, C-G5 approche attributionnelle, C-G7 usines et carrières de ciment négligées, ce qui avantage le béton). C'est le premier point à recalibrer avant le Biodiversity Standard Council.

## Points à vérifier avant toute publication

1. Licence de HabRef (PatriNat) : les correspondances et les espèces caractéristiques des fiches habitats en viennent ; sa licence n'a pas pu être lue (serveurs de l'INPN hors service).
2. Liste des espèces exotiques envahissantes de l'Union : la mise à jour du règlement d'exécution (UE) 2025/1422 n'a pas été relue.
3. Les cinq sources secondaires du lot 1 (aire-espèces, éclairage, bruit, carrières, FCBA).

## Questions ouvertes

Posées une par une à Cédric :
1. Le calibrage du bois (cas 7) : le soumettre tel quel au Biodiversity Standard Council avec ses trois conventions explicites, ou le reprendre avant (inventaire des usines et cimenteries, approche conséquentielle pour la forêt française).
2. La licence de la convention NORMATYS-IRICE, qui doit permettre la publication sous CC BY 4.0 et AGPL.
3. La relecture des 191 correspondances par un écologue d'IRICE.

## Ce que le go déclenche

Lot 2, moteur : un module de code par fiche algorithme (les fiches de la partie 3 servent de spécification), chargeur des tables avec refus des lignes sans source, journal des calculs, Monte-Carlo, RSNat validé par `schemas/rsnat.xsd`, ligne de commande `opennat calcul projet.json`, et retour aux résultats du carnet de référence sur les huit cas.
