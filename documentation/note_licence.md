# OpenNAT : droits, licences et conventions entre NORMATYS et IRICE

Note de décision pour Cédric PLANTAZ, 19 octobre 2026. Ni avis juridique, ni acte : le projet de clauses en annexe est à relire avant toute signature.

## La question

OpenNAT a été construit comme OpenBCE pour la RE2020 : une méthode publique, des tables publiques et un moteur libre. Le dépôt prévoit le texte et les tables sous CC BY 4.0 et le moteur sous AGPL. Depuis le 19 octobre, la répartition est arrêtée : NORMATYS édite la méthode et détient les droits sur la méthode, les tables et le moteur ; IRICE édite l'outil de calcul (l'utilitaire) et applique la méthode dans la certification Effinature.

Les conventions signées le 11 octobre 2026 entre NORMATYS et IRICE (NTY-CNV-2026-001 à 005) ne parlent pas d'OpenNAT. La note dit ce qu'elles impliquent pour OpenNAT, où elles le contredisent, et quel acte le placer.

## Ce que disent les conventions signées

| Convention | Clause | Portée pour OpenNAT |
|---|---|---|
| 001-B, Effinature, article 3 | relèvent du référentiel, propriété de NORMATYS, les textes qui énoncent des exigences, des seuils, des pondérations ou des règles de calcul ; restent à IRICE les outils qui servent à appliquer, calculer ou contrôler (plateforme d'évaluation, outils et feuilles de calcul) | la méthode et les tables vont à NORMATYS ; l'utilitaire va à IRICE ; le moteur, outil de calcul, irait à IRICE si on lit l'article à la lettre |
| 001-B, article 4 | NORMATYS décide l'adoption, la publication en accès libre et la date d'application de chaque version ; le comité scientifique valide les versions définitives | la publication d'OpenNAT relève de NORMATYS, après validation du Biodiversity Standard Council (nom du comité scientifique dans la convention 005-A) |
| 001-B, article 7 | licence exclusive à IRICE pour la certification des opérations ; l'exclusivité porte sur l'organisme qui certifie | si OpenNAT entre dans le référentiel Effinature, une licence libre sur son texte contredirait l'exclusivité, sauf à la limiter (voir plus bas) |
| 001-B, articles 3 et 8 | la marque Effinature appartient à NORMAXIS et n'est pas dans la convention ; aucune partie ne fait état de l'accréditation hors de sa portée | la marque, non le texte, est ce qui réserve Effinature à IRICE ; OpenNAT n'est pas dans la portée d'accréditation |
| 005-A, article 5 | les programmes de R&D sur les règles de calcul sont décidés par NORMATYS et lui appartiennent ; ceux sur les outils (plateforme, outil BPS, feuilles de calcul) sont décidés par IRICE et lui appartiennent ; registre mensuel des temps pour le crédit d'impôt recherche | deux programmes à ouvrir : OpenNAT méthode et moteur (NORMATYS), utilitaire OpenNAT (IRICE) |

Deux constats en sortent. Le premier est un conflit : rien ne range le moteur chez NORMATYS, et l'article 3 de la convention Effinature le range plutôt chez IRICE. Le second est une conciliation possible : la convention ne réserve à IRICE que la certification, pas l'usage du texte, et la marque Effinature n'est pas dans son objet.

## Le moteur : règle de calcul ou outil

Le moteur d'OpenNAT n'est pas un outil d'application au sens de l'article 3 : il ne traite pas un dossier, il exécute la méthode. Le banc de validation le compare au carnet de référence, unité par unité et année par année, et le texte de la méthode en tient la spécification complète (fiches algorithmes A01 à A58). C'est la forme exécutable des règles de calcul, comme le moteur publié avec la méthode Th-BCE de la RE2020. L'utilitaire, lui, sert à saisir un projet, lancer le calcul et éditer une fiche : c'est l'outil d'application, et il revient à IRICE.

Le classement tient, mais il faut l'écrire : sans clause expresse, la lettre de l'article 3 donne le moteur à IRICE.

## Licence libre et exclusivité

CC BY et AGPL sont des licences non exclusives et irrévocables. Une fois le texte, les tables et le moteur publiés sous ces licences, n'importe qui peut les employer, y compris un autre organisme qui voudrait certifier sur la base d'OpenNAT. Ce qui reste réservé à IRICE tient à trois choses que la licence libre ne touche pas :

- la marque Effinature (NORMAXIS), que nul autre ne peut délivrer ;
- le programme de certification d'IRICE (règles de certification et méthodes d'évaluation, article 6 de la convention Effinature) et son accréditation ;
- le nom OpenNAT, s'il est déposé : la licence libre autorise à reprendre le contenu, pas à présenter un calcul modifié comme un calcul OpenNAT.

Un risque d'ordre logiciel s'ajoute. L'AGPL impose de publier le code source d'un logiciel qui intègre le moteur et qui est offert à des utilisateurs par le réseau. Si IRICE intégrait le moteur à la plateforme effinature.com, l'ensemble pourrait être tenu pour une œuvre dérivée du moteur, et la plateforme devrait alors être publiée. NORMATYS, titulaire des droits sur le moteur, peut lever ce risque en concédant à IRICE une seconde licence, propre, qui l'autorise à intégrer le moteur à ses outils sans les obligations de l'AGPL (double licence). C'est aussi un avantage réel et réservé pour IRICE, qui ne retire rien au public.

## Montages possibles

| Montage | Contenu | Effets |
|---|---|---|
| A, recommandé | méthode et tables sous CC BY 4.0, moteur sous AGPL, propriété de NORMATYS ; utilitaire propriété d'IRICE ; seconde licence du moteur à IRICE pour ses outils ; nom OpenNAT déposé par NORMATYS ; exclusivité d'IRICE maintenue sur Effinature | modèle d'OpenBCE ; adoption et vérification par tous ; la valeur d'IRICE reste dans la certification, la marque et l'intégration à ses outils |
| B | méthode publiée en accès libre mais tous droits réservés ; moteur fermé, concédé à IRICE seul | exclusivité forte ; plus de banc ouvert ni de moteur vérifiable par un tiers, ce qui affaiblit la méthode devant le conseil et les maîtres d'ouvrage ; contraire à la promesse d'OpenNAT |
| C | tout cédé à IRICE | contraire au partage arrêté (NORMATYS propriétaire des règles) et à la directive (UE) 2024/825, qui sépare le propriétaire du système de l'organisme qui contrôle |

## Recommandation

Retenir le montage A et le fixer par une convention dédiée, NTY-CNV-2026-006, plutôt que par un avenant à la convention Effinature : OpenNAT est une méthode distincte, appelée à servir Effinature mais aussi d'autres usages (permis de construire, comparaison de variantes), et la convention Effinature restera lisible. La convention 006 :

1. désigne la méthode OpenNAT, ses tables et son moteur comme propriété de NORMATYS, le moteur étant la forme exécutable des règles de calcul, par dérogation expresse à la lettre de l'article 3 de la convention 001-B ;
2. range l'utilitaire de calcul OpenNAT parmi les outils d'IRICE ; ses fichiers portent aujourd'hui la licence AGPL du moteur, qu'IRICE peut garder ou, grâce à la licence du point 4, remplacer par une licence de son choix ;
3. fixe la publication sous CC BY 4.0 (texte et tables) et AGPL-3.0-or-later (moteur), après validation du Biodiversity Standard Council ;
4. concède à IRICE une licence non exclusive du moteur pour l'intégrer à ses outils sans les obligations de l'AGPL, pour la durée de la convention ;
5. précise que l'exclusivité de l'article 7 de la convention 001-B continue de porter sur la certification Effinature, OpenNAT lui-même restant d'usage libre ;
6. ouvre les deux programmes de R&D de l'article 5 de la convention 005-A ;
7. prévoit le dépôt du nom OpenNAT par NORMATYS.

Il faut aussi accomplir les formalités de l'article L. 227-10 du code de commerce, comme pour les conventions 001 à 005 : même représentant des deux côtés.

Avant la publication, deux points sont à régler à part : le dépôt du nom OpenNAT, et la mention au Cofrac du changement d'organisation (déjà prévue pour les conventions 001 à 005), puisque l'utilitaire d'IRICE servira dans des dossiers Effinature.

## Annexe. Projet de clauses de la convention NTY-CNV-2026-006

Article 1. Objet. La convention organise les droits sur la méthode de calcul OpenNAT, ses tables de données, son moteur de calcul et son utilitaire de calcul, et les conditions de leur publication et de leur usage par IRICE. Elle complète les conventions NTY-CNV-2026-001 et 005, qui restent applicables.

Article 2. Propriété de NORMATYS. La méthode OpenNAT (texte, fiches algorithmes, conventions de calcul), ses tables de données et son moteur de calcul appartiennent à NORMATYS. Le moteur est la forme exécutable des règles de calcul de la méthode, dont il reproduit les fiches ; il relève à ce titre des règles de calcul au sens de l'article 3 de la convention NTY-CNV-2026-001, et non des outils mentionnés à son cinquième alinéa.

Article 3. Propriété d'IRICE. L'utilitaire de calcul OpenNAT, interface de saisie, de lancement du calcul, de lecture des résultats et d'édition des fiches de synthèse, est un outil d'IRICE au sens du même article. IRICE en est l'éditeur ; il appelle le moteur de NORMATYS sans le modifier.

Article 4. Publication. Après validation de la version définitive par le Biodiversity Standard Council, NORMATYS publie le texte et les tables sous licence Creative Commons Attribution 4.0 et le moteur sous licence GNU Affero General Public License, version 3 ou ultérieure.

Article 5. Licence d'intégration. NORMATYS concède à IRICE, pour la durée de la convention, une licence non exclusive d'utilisation, de reproduction et d'intégration du moteur dans ses outils, y compris offerts par le réseau, sans les obligations de la licence publique de l'article 4. La contrepartie financière est fixée par avenant ; jusque-là, la licence est consentie sans redevance.

Article 6. Effet sur la licence Effinature. La licence exclusive de l'article 7 de la convention NTY-CNV-2026-001 porte sur la certification au regard du référentiel Effinature. Elle ne restreint pas l'usage public de la méthode OpenNAT, que le référentiel Effinature peut appeler.

Article 7. Nom. NORMATYS dépose le nom OpenNAT ; l'usage du nom pour un calcul qui ne suit pas une version adoptée de la méthode est interdit.

Article 8. Recherche et développement. Les travaux sur la méthode, les tables et le moteur forment un programme de NORMATYS ; les travaux sur l'utilitaire, un programme d'IRICE, au sens de l'article 5 de la convention NTY-CNV-2026-005.

Articles 9 à 12. Durée, résiliation, formalités de l'article L. 227-10 du code de commerce, droit applicable : comme la convention NTY-CNV-2026-001.
