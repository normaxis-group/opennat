# Livraison du lot 7 : finitions et note sur les licences

**Date :** 19 octobre 2026
**Dépôt :** `_OUTILS/opennat/`, branche `main` ; aucun dépôt en ligne.
**Versions :** méthode OpenNAT 1, données 1.2.2, moteur 0.2.0 (inchangés).
**État :** livré, rien n'est transmis ni signé. Arrêt et attente du go écrit.

## Ce qui est fait

1. Graphique de trajectoire de l'utilitaire : graduations rondes, bande du chantier, trait de fin du plan de gestion, légende complétée.
2. Guide utilisateur au papier IRICE hors portée d'accréditation (l'outil est édité par IRICE), limites mises à jour après le lot 6. Le gabarit commun reçoit un papier `irice-hors-portee` (sans le bloc Cofrac), utilisable aussi pour BPS et Efficarbone ; `outils/methode_docx.py` prend l'option `--papier`.
3. Facteurs EF d'acidification relus sur la méthode publiée par ÖKOBAU.DAT (version 01.03.010) : 1,31, 0,74 et 3,02 mol H+ éq. par kg de SO2, NOx et NH3 ; réserve de la note pollution levée.
4. Fin de plan de gestion progressive chiffrée (`banc/options_gestion.py`) : sur l'exemple de l'annexe C, Cnat passe de 3 217 à 3 171 m²HE·an sur deux ans, 3 147 sur trois ; médiane de -61 m²HE·an sur les 65 cas concernés. Ajoutée à la décision D7 du dossier (recommandation : deux ans, comme l'abandon en C-M2).
5. Note « OpenNAT, droits, licences et conventions NORMATYS-IRICE » (4 pages, Word et PDF dans `livraison/`) : lecture des conventions signées NTY-CNV-2026-001 à 005, conflit sur le moteur (article 3 de la convention Effinature), conciliation de la licence libre et de l'exclusivité, trois montages, recommandation et projet de clauses d'une convention NTY-CNV-2026-007.

## Constat de rendu

Après la reprise de session, LibreOffice ne voyait plus les polices installées pour l'utilisateur et remplaçait Poppins par Liberation Serif. Les polices ont été chargées pour la session (AddFontResource) ; chaque PDF livré a été contrôlé (Poppins incorporée). Consigné dans la mémoire des rendus.

## Ce que le go déclenche

Trancher le montage des droits (recommandation : A) ; faire rédiger ou relire la convention 007 ; décider du dépôt du nom OpenNAT ; transmettre au Biodiversity Standard Council le dossier et la note pollution, ou les reprendre.

## Suite donnée (19/10/2026)

Montage A retenu par Cédric. Convention NTY-CNV-2026-007-A préparée au gabarit NORMATYS (5 pages), non envoyée en signature : kDrive `GESTION\IRICE\RÉFÉRENTIELS NORMATYS\01_CONVENTIONS\NTY-CNV-2026-007-A_CONVENTION_NORMATYS_IRICE_METHODE_OPENNAT` (.docx et .pdf), source dans `03_SOURCES_CONVENTIONS`. Référence 007 et non 006, déjà employée par un avenant abandonné le 11/10/2026.
