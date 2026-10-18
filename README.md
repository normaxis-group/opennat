# OpenNAT

Méthode de calcul biodiversité **OpenNAT** et son moteur libre, qui porte le même nom, sur le modèle d'OpenBCE (méthode Th-BCE de la RE2020).

- Éditeur de la méthode et titulaire des droits : NORMATYS. Application dans la certification Effinature : IRICE.
- Validation de la méthode : Biodiversity Standard Council. Tant qu'elle n'est pas validée, la méthode, ses seuils et ses résultats ne sont pas opposables.
- Licences prévues : moteur sous AGPL-3.0-or-later ; texte de la méthode et tables `donnees/` sous CC BY 4.0, chaque ligne portant la licence de sa source.
- Dépôt privé. Aucune publication sans le go écrit de Cédric PLANTAZ.

## État

| Lot | Objet | État |
|---|---|---|
| 0 | Audit et état de l'art (`audit/`) | livré le 17/10/2026, go le 18/10/2026 |
| 1 | Méthode OpenNAT v1 (`methode/`) et tables sourcées (`donnees/`) | version noyau livrée le 18/10/2026 ; édition complète (949 pages) livrée le même jour (lot 1 bis) |
| 2 | Moteur | à venir |
| 3 | Utilitaire | à venir |
| 4 | Banc de validation et documentation | à venir |

L'audit du lot 0 emploie encore l'ancien nom de travail « Vi-BCN » ; le nom retenu par Cédric PLANTAZ le 18/10/2026 est OpenNAT, pour la méthode comme pour le moteur.

## Organisation

- `audit/` : cahier des charges, audit du lot 0, fiches de sources A à E.
- `methode/` : texte de la méthode, conventions, bibliographie.
- `donnees/` : tables de coefficients, une ligne par valeur avec sa source.
- `outils/` : contrôle des tables et rapport de couverture.
- `sources/` : copies de travail des documents sources (hors dépôt).
