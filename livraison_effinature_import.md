# Livraison : import d'un dossier Effinature 8.1 dans OpenNAT

25 octobre 2026, branche `effinature-import` (issue de `credits-lot1`), non poussée. Demande de Cédric : « construis l'import d'un dossier Effinature 8.1 vers le fichier projet OpenNAT, testé sur un dossier fictif, sans toucher aux données clients ».

## Ce qui est livré

| Fichier | Contenu |
|---|---|
| `opennat/effinature/__init__.py` | sous-paquet comme `opennat/credits/`, hors du contrôle E2 des valeurs de la méthode OpenNAT 1 (les conventions de l'import y sont nommées) ; lecture d'un export de dossier (format « Effinature export 1 »), production du fichier projet, du fichier crédits, de la fiche de relevé et du journal ; reprise d'une fiche de relevé remplie (`releves_depuis_csv`) |
| `opennat/__main__.py` | commande `python -m opennat effinature export.json --sortie DOSSIER [--periode-hve N] [--releves fiche.csv]` |
| `banc/effinature/dossier_fictif.export.json` | dossier FICTIF (résidence de 6 000 m², 13, Effinature 8.1), aucune donnée d'un client d'IRICE |
| `tests/test_effinature.py` | 12 tests : schéma, fermeture des surfaces, correspondance CBS, aucun état inventé, calendrier C-X12, crédits calculables, aller-retour de la fiche, erreurs |
| `opennat/numerique.py`, `opennat/conformite.py` | correction d'un défaut du moteur, voir plus bas |

Aucune base Effinature n'a été lue : seul le code de la plateforme (modèles et calculateurs) a servi à fixer le format.

## Ce que l'import reprend d'un dossier Effinature

| Donnée Effinature | Devient dans OpenNAT |
|---|---|
| Calcul CBS, état projet : parcelle, emprise bâtie, surfaces par nature | unités de la variante « Projet » : bâti VB.1, VRD perméables VB.3 et VB.4, toitures VB.11 à VB.13, façade VB.15, noue VB.19, mare VB.20, potager VB.22, jardinières VB.23 ; surface non décrite comptée imperméabilisée (VB.2) |
| Pleine terre et terre sur dalle du CBS | réparties entre les habitats déclarés à l'IVE (prairie VB.26, massif VB.6, pelouse VB.5, jardin VB.7) ; habitat non reconnu : pelouse, le type le moins valorisé |
| Habitats de l'IVE (phase réalisation, sinon projet) | répartition ci-dessus ; haies en unité linéaire FA.2, prises sur la pleine terre |
| Palette, strate arborée | arbres VB.18a (locaux) et VB.18b (exotiques), jeunes plants, houppier par défaut de la classe « petit » |
| CBS initial (rénovation) ou habitats initiaux de l'IVE | état initial ; le reste non décrit doit être déclaré (`reste_initial`), sinon l'import s'arrête |
| Taux de pleine terre du PLU | variante « Classique » : même bâti, pleine terre minimale en pelouse, le reste imperméabilisé ; c'est l'opération sans Effinature, déclarée en obligation du fichier crédits |
| Contrôle de livraison, contrôles HVE | calendrier propre des relevés (convention C-X12) |
| Risque déclaré par le porteur | facteurs de l'annexe A ; non déclaré, chaque facteur est noté élevé |

L'import n'invente aucun état écologique. Les unités sortent sans grille renseignée : le moteur compte alors tous les critères à « non » (fiche A10), ce qui minore le gain jusqu'au premier relevé.

## Comment la certification produit les crédits

Le crédit mesure ce que l'opération Effinature fait de plus que l'opération classique (variante « Classique »). La certification apporte les deux constats dont le crédit a besoin :

1. **Contrôle de conformité à la livraison** = relevé de l'année 1. L'évaluateur constate ce qui a été réalisé et remplit la fiche de relevé (grilles d'état d'OpenNAT, unité par unité).
2. **Contrôle HVE après deux ans d'exploitation** = relevé de l'année 2, puis à chaque contrôle HVE suivant (tous les 5 ans par défaut, `--periode-hve`).

La fiche de relevé (`<id>.fiche_releve.csv`) liste, pour chaque unité, les critères de sa grille (EP2 prairie, EU1 urbain, EA1 arbres, EM1 mare...). Remplie, elle revient dans le fichier crédits par `--releves`. La règle B (C-X13) admet ce relevé fait par le Biodiversity Partner si le vérificateur visite et contrôle au moins une unité sur cinq.

Avec la convention C-X12, le calendrier minimal compte 12 relevés (années 1, 2, 7, 12... 47, 50). Ils ne coûtent presque rien de plus s'ils tombent pendant des contrôles HVE déjà payés.

## Résultats sur le dossier fictif (1 000 tirages, graine 1)

| Hypothèse d'état | Gain retenu sur 50 ans | Crédits (plafond) | Réserve |
|---|---|---|---|
| Aucun relevé (tous critères à « non ») | 7 870 m²HE·an | 5 | 25 % |
| Espaces verts en bon état (5 critères sur 6) | 23 036 m²HE·an | 17 | 25 % |

Avec une fiche remplie aux années 1 et 2, le gain constaté reste négatif (-181 et -254 m²HE·an) : les plantations sont jeunes, aucune émission n'a lieu avant une dizaine d'années. Les contrôles de livraison et HVE servent de constat ; les crédits arrivent plus tard, d'où les ventes à terme (chapitre 12.1).

Calcul OpenNAT 1 du même projet : Snat +7 555 m²HE·an pour la variante Projet, -11 693 pour la variante Classique.

## Correction du moteur

`conformite.py` (fiche A40-3) combinait la conformité au CBS et à la pleine terre du PLU par un `and` Python, qui plante sur les tableaux de tirages. Aucun cas du banc n'avait à la fois un PLU déclaré et des tirages. Remplacé par `nm.et`, qui garde le comportement aux valeurs centrales.

## Reste à faire ou à décider

- **Export côté plateforme Effinature** : non construit. Il faut une commande qui écrit ce format pour un dossier donné, et seulement avec l'accord écrit du maître d'ouvrage (option crédits, convention NORMATYS). IRICE ne transmet rien de lui-même (ISO/IEC 17065, § 4.5 et 4.2).
- **Zones biogéographique et climatique** : à fournir dans l'export, faute de table département-zone dans OpenNAT.
- **Périodicité des contrôles HVE** : 5 ans par défaut, à confirmer.
- **Fiche de relevé dans le contrôle HVE** : la grille OpenNAT doit entrer dans le protocole des contrôles de livraison et HVE (procédure IRICE à réviser, avec avis du comité d'impartialité pour le rôle de vérificateur).
- Épaisseurs de substrat par défaut (dalle 50 et 100 cm, toitures 10, 20, 40 et 15 cm) : conventions de l'import, à relire.

## Contrôles

- `python -m pytest` : 193 tests passés, dont les 12 de l'import.
- `python -m banc.regression` : 38 930 grandeurs sur 38 930 inchangées après la correction du moteur.
- `python -m banc.credits.comparer` : 20 cas conformes sur 20.
