# Livraison du lot 4 des crédits OpenNAT : contrats de la phase 1

24 octobre 2026. Go de Cédric : « Go lot 4 : contrats de la phase 1 sur réseau de test. »

## Où

Dossier `contrats/` de l'application du registre (`C:\laragon\www\opennat-registre`), dépôt git local, commits 0ee6a10
et suivant. Aucun dépôt distant, aucun déploiement sur un réseau public.

## Livré

- **Deux contrats** Solidity 0.8.24 sur OpenZeppelin 5.3, 239 lignes : `AncrageOpenNAT` (empreintes datées, une seule
  fois) et `RegistreOpenNAT` (jetons non cessibles ERC-5192 pour les lots et les attestations de retrait, plafond par
  projet, centièmes, rôles séparés, émission et annulation jamais sur la même clé, pause). Pas de mise à jour du code :
  une nouvelle version se déploie à côté et reprend l'historique depuis le registre.
- **Service de chaîne** (`contrats/scripts/`) : déploiement avec cession de l'administration au multisignature,
  synchronisation idempotente depuis le grand livre public du registre (`/api/v1/grand-livre`, sans donnée
  personnelle, bénéficiaires par empreinte), rapprochement, recette de bout en bout.
- **Côté registre** : confirmation des ancrages (`registre:ancrages-confirmes`), réception du rapport de rapprochement
  (`registre:rapprochement`), blocage de toutes les opérations du grand livre au moindre écart, déblocage motivé
  (`registre:debloquer`), bandeau sur l'écran des opérations.
- **Dossier d'audit** (`contrats/AUDIT.md`) prêt à joindre aux demandes de devis.

## Recette

| N° | Critère | Résultat |
|---|---|---|
| R6 | émission sous plafond, par le seul rôle émetteur | tenu (tests des contrats et du registre) |
| R8 | conservation sur 10 000 opérations aléatoires | tenu : 10 000 opérations comparées à un modèle, refus compris, en 13 s |
| R9 | écart provoqué détecté en moins d'une minute, opérations bloquées | tenu : détecté en 6 ms ; le registre de démonstration s'est bloqué sur le vrai rapport, puis a été débloqué avec motif |
| R10 | audit externe sans anomalie critique ou haute ouverte | à faire : deux devis à demander, sur votre accord |
| R17 | aucun jeton de la phase 1 transférable | tenu : transfert, transfert sûr, approbation, approbation globale refusés |
| R18 | redéploiement complet avec reprise de l'historique | tenu : réseau neuf, redéploiement, resynchronisation, rapprochement sans écart |

Autres contrôles : couverture 100 % des instructions, branches, fonctions et lignes ; Slither 0.11.6 sans résultat
(après correction du contrôle d'adresse nulle qu'il avait signalé) ; deuxième synchronisation sans aucune écriture
(idempotence) ; registre : 15 tests PHPUnit passés.

Gaz mesuré : `emettre` 226 403, `retirer` 227 143, `ancrer` 53 855, `definirPlafond` 52 540.

## Ce qui reste pour un vrai réseau de test

Le déploiement sur Arbitrum Sepolia est prêt (`hardhat.config.js`, `scripts/deployer.js`) mais n'a pas été fait : il faut
une adresse de déploiement approvisionnée en ETH de test (robinet public, qui demande une connexion ou une vérification
anti-robot que je ne peux pas faire), une adresse RPC, et les clés des rôles rangées dans le coffre du groupe. Il faudra
aussi créer le Safe de test (trois signatures sur cinq). Le coût réel par opération se mesurera alors.

## Écarts au cahier des charges

- Réseau de test public non atteint (voir ci-dessus) ; recette faite sur le réseau interne de Hardhat avec le grand livre
  réel du registre local.
- Contrats non remplaçables plutôt que remplaçables après un délai de 30 jours : plus simple à auditer, et R18 montre que
  le redéploiement reprend tout l'historique.
- Clés de rôle encore locales ; service de gestion de clés et Safe à mettre en place avec le déploiement de test.
