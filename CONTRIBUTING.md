# Contribuer à OpenNAT

Les contributions sont bienvenues : valeurs sourcées, relectures écologiques, cas de test, code. Le projet est en
français, comme la méthode.

## Proposer une valeur

C'est la contribution la plus utile. Chaque coefficient des tables de `donnees/` est une ligne qui porte sa valeur,
son intervalle, sa source précise et la licence de cette source. Une proposition donne :

- la table et la ligne visées (clé et paramètre), avec la valeur en vigueur ;
- la valeur proposée, son intervalle d'incertitude et ce qui la fonde : publication, référentiel public, texte
  réglementaire ou relevés documentés, avec la page, le tableau ou l'équation ;
- la licence de la source : une valeur dont la reprise est interdite ne peut pas entrer dans les tables.

Le format d'une ligne, la place de chaque table et le modèle de proposition sont dans le
[guide du contributeur](documentation/guide_contributeur.md). Un avis sans source reste utile : il signale une ligne à
reprendre, que NORMATYS instruit. Une proposition qui modifie une convention de méthode est soumise au Biodiversity
Standard Council.

## Signaler une lecture de la méthode

Ouvrir un ticket qui cite la fiche algorithme (A01 à A58), la convention (`methode/conventions.md`) ou la section du
texte concernée, la lecture du moteur et la lecture proposée, avec ce qui la fonde. Un fichier projet joint ne contient
que ce qui sert au cas : ni nom d'opération, ni adresse, ni RSEE réel.

## Proposer du code

- Un module du moteur par module de la méthode, avec en tête les fiches suivies ; le numéro de l'équation en
  commentaire, à côté de la ligne qui l'applique.
- Aucune constante dans le code : toute valeur vient d'une table de `donnees/` (le test `tests/test_sans_constante.py`
  le vérifie).
- Des tests sans données réelles : fichiers projet et RSEE fabriqués dans le test ou dans `banc/cas/`.
- Une modification qui change un résultat met à jour le banc (`python -m banc.comparer`), l'instantané de
  non-régression (`python -m banc.regression`) et le [journal des versions](JOURNAL_DES_VERSIONS.md).
- `python -m pytest` doit passer avant toute proposition.

## Licence des contributions

Le moteur (`opennat/`, hors utilitaire) est distribué sous AGPL-3.0-or-later, NORMATYS titulaire des droits ;
l'utilitaire (`opennat/utilitaire/`) sous la même licence, IRICE titulaire des droits ; le texte de la méthode et les
tables sous CC BY 4.0, NORMATYS titulaire des droits. Les contributions le sont aux mêmes conditions. Le titulaire peut
aussi concéder son composant sous une autre licence ; pour qu'une contribution importante puisse y être incluse, un
accord de contribution sera proposé à son auteur avant intégration.

Le nom OpenNAT n'est pas couvert par ces licences : ses conditions d'usage sont dans
[documentation/conditions_usage_nom.md](documentation/conditions_usage_nom.md).

## Échanges

Les questions, propositions de valeurs et signalements passent par les tickets du dépôt.
