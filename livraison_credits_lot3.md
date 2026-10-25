# Livraison du lot 3 des crédits OpenNAT : registre et plateforme

24 octobre 2026. Go de Cédric : « GO LOT 3 », donné avant l'avis d'avocat que le cahier des charges (indice B) mettait en condition du lot 3. Conséquence retenue : tout est construit, mais les cessions restent désactivées et rien n'est déployé tant que l'avis n'est pas rendu.

## Où

Application à part, `C:\laragon\www\opennat-registre`, dépôt git local (commit 33e7272), **sans dépôt distant ni déploiement**. Squelette repris de la plateforme OpenNAT (Laravel 13, Livewire, Filament), sans rien d'IRICE : le registre relève de la société dédiée en constitution (D1). Base SQLite locale ; aucune base du groupe n'est touchée.

## Ce que fait le registre

- **Grand livre** (`app/Registre/GrandLivre.php`) : validation sur RSNat-C prévisionnel signé (plafond, taux de réserve, versions figées), activation sur pièces (ORE, plan de gestion, garantie), émission par vérification (lot numéroté, série, millésime, versement à la réserve), inversion annulée dans la réserve commune lot par lot et, si la réserve est épuisée, projet suspendu avec le déficit inscrit au journal, cession unique du porteur à un acheteur contrôlé (désactivée), retrait avec attestation signée, annulation motivée, invariant de conservation. Quantités en centièmes de crédit.
- **Contrôle des RSNat-C** (`ControleRsnatc.php`) : format, rattachement, versions figées (C-X18), 1 000 tirages au moins (C-X9), éligibilité, rang attendu, cohérence avec les crédits déjà émis, et recalcul indépendant en PHP des formules X3, X4, X7 à X9. Un RSNat-C retouché à la main est refusé.
- **Signatures** Ed25519 au format JWS : le vérificateur signe le RSNat-C, le registre signe chaque attestation de retrait ; vérification publique d'une attestation collée dans `/verifier`.
- **Journal chaîné** par empreintes SHA-256, vérifiable ; empreinte du jour, pièces, RSNat-C, lots et retraits mis en **file d'ancrage** (envoi sur la chaîne au lot 4).
- **Chevauchement** : une parcelle cadastrale déjà engagée dans un projet déposé, validé, actif ou suspendu est refusée.
- **Parcours** : porteur (dépôt, pièces, crédits, retrait), vérificateur (dépôt du `rsnatc.json` du moteur, contrôles affichés, signature), acheteur (crédits, retrait), opérateur (`/operations` : désignation, validation, activation, émission, connaissance du client, contrôles d'intégrité, journal). Inscription des porteurs et acheteurs avec création de l'organisation ; vérificateurs et opérateur créés par `php artisan registre:creer-compte`.
- **Public sans compte** : accueil et chiffres, projets, fiche projet (lots, retraits, RSNat-C signés, pièces publiques et leurs empreintes, parcelles), attestation de retrait, vérification, API en lecture `/api/v1`, export CSV.
- **Exploitation** : `registre:controler` (tous les jours à 6 h), `registre:ancrer-le-jour` (23 h 55), base de démonstration `DemonstrationSeeder`.

## Recette

| N° | Critère | État |
|---|---|---|
| R1 | avis juridique sur la phase 1 | en attente : aucun cabinet consulté |
| R6 | aucune émission sans RSNat-C signé, valide, projet actif, sous le plafond | tenu, testé (RSNat-C non signé, fichier altéré, émission gonflée) |
| R8 | conservation (côté registre) | tenu sur le parcours complet et après inversion |
| R9 | rapprochement base et chaîne | reporté au lot 4 (il faut la chaîne) ; la cohérence interne est contrôlée chaque jour |
| R11 | chevauchement de parcelles refusé | tenu, testé (même parcelle saisie autrement) |
| R12 | inversion annulée dans la réserve | tenu, testé, y compris réserve épuisée |
| R13 | attestation sans formule interdite | tenu, testé |
| R14 | consultation publique sans donnée personnelle | tenu, testé sur les pages, l'API et l'export |

`php artisan test` : 12 tests, 12 passés, sur les RSNat-C réels du moteur (cas X04 et X05, 1 000 tirages). Parcours vérifié dans le navigateur sur la base de démonstration : 21 crédits émis en deux lots, retrait de 3 crédits, signature vérifiée, invariants tenus, chaîne intacte.

## Écarts au cahier des charges

- Cessions construites mais désactivées (`REGISTRE_CESSIONS_ACTIVES=false`), comme la connaissance du client par prestataire : contrôle manuel par l'opérateur en attendant l'avis.
- Attestation de retrait en page web et en JWS signé ; pas encore de PDF.
- Clés privées chiffrées par la clé de l'application ; service de gestion de clés au lot 4.
- Non faits : signalement d'un événement de perte avec mise en attente dans la réserve (chapitre 11.2, champ prévu), suspension automatique d'un projet sans vérification (9.5), revalidation décennale, inscription des unités d'un site agréé, contrôle des chevauchements par géométrie, écriture par API pour les acheteurs institutionnels, version anglaise, audit d'accessibilité et test d'intrusion.

## Suite

Lot 4 (contrats de la phase 1 sur réseau de test, ancrage, rapprochement R9) ; avis d'avocat ; dénomination de la société du registre et sa charte.
