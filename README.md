# OpenNat

Moteur libre de la méthode de calcul biodiversité **Vi-NAT**, jumeau d'OpenBCE (méthode Th-BCE de la RE2020).

- Éditeur de la méthode et titulaire des droits : NORMATYS. Application dans la certification Effinature : IRICE.
- Validation de la méthode : Biodiversity Standard Council. Tant qu'elle n'est pas validée, la méthode, ses seuils et ses résultats ne sont pas opposables.
- Licences prévues : moteur sous AGPL-3.0-or-later ; texte de la méthode et tables `donnees/` sous CC BY 4.0, chaque ligne portant la licence de sa source.
- Dépôt privé. Aucune publication sans le go écrit de Cédric PLANTAZ.

## État

| Lot | Objet | État |
|---|---|---|
| 0 | Audit et état de l'art (`audit/`) | livré le 17/10/2026, go le 18/10/2026 |
| 1 | Méthode Vi-NAT v1 (`methode/`) et tables sourcées (`donnees/`) | en cours |
| 2 | Moteur | à venir |
| 3 | Utilitaire | à venir |
| 4 | Banc de validation et documentation | à venir |

L'audit du lot 0 emploie encore l'ancien nom de travail « Vi-BCN » ; le nom retenu le 18/10/2026 est Vi-NAT.

## Organisation

- `audit/` : cahier des charges, audit du lot 0, fiches de sources A à E.
- `methode/` : texte de la méthode, conventions, bibliographie.
- `donnees/` : tables de coefficients, une ligne par valeur avec sa source.
- `outils/` : contrôle des tables et rapport de couverture.
- `sources/` : copies de travail des documents sources (hors dépôt).
