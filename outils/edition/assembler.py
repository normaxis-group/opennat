# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Assemble l'édition complète de la méthode OpenNAT en un seul fichier Markdown.

Ordre : page de titre et sommaire, partie 1 (texte de la méthode, methode/OpenNAT_v1.md, titres décalés d'un
niveau), parties 2 à 8 (methode/edition/), partie 9 (conventions), partie 10 (bibliographie).
Régénère d'abord les parties construites depuis les données.
"""
import os
import re
import subprocess
import sys

from commun import EDITION, RACINE

ICI = os.path.dirname(os.path.abspath(__file__))


def decaler(texte, niveaux=1, depuis=None):
    lignes = texte.splitlines()
    if depuis:
        lignes = lignes[next(i for i, l in enumerate(lignes) if l.startswith(depuis)):]
    out = []
    for l in lignes:
        if l.startswith('#'):
            out.append('#' * niveaux + l)
        else:
            out.append(l)
    return '\n'.join(out)


def lire(chemin):
    with open(chemin, encoding='utf-8') as f:
        return f.read()


def main():
    for script in ('partie2_donnees.py', 'partie4_habitats.py', 'partie5_exemples.py', 'partie7_rsnat.py',
                   'partie8_cas.py'):
        subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ICI, script)], check=True, cwd=ICI)
    v1 = lire(os.path.join(RACINE, 'methode', 'OpenNAT_v1.md'))
    partie1 = decaler(v1, 1, depuis='## 1. Objet')
    partie1 = partie1.replace('### Annexe A : tables de coefficients',
                              '### Annexe A : tables de coefficients (détail en partie 2)')
    partie1 = partie1.replace('### Annexe B : correspondances de nomenclatures',
                              '### Annexe B : correspondances de nomenclatures (détail en parties 2 et 4)')
    conventions = decaler(lire(os.path.join(RACINE, 'methode', 'conventions.md')), 1)
    conventions = conventions.replace('## Conventions de la méthode OpenNAT v1', '## Partie 9. Conventions', 1)
    biblio = decaler(lire(os.path.join(RACINE, 'methode', 'bibliographie.md')), 1)
    biblio = biblio.replace('## Bibliographie de la méthode OpenNAT v1', '## Partie 10. Bibliographie', 1)
    tete = """# Méthode de calcul OpenNAT, version 1, édition complète

Méthode conventionnelle de calcul de la consommation de nature d'une opération de construction ou d'aménagement, et de la biodiversité grise de ses matériaux.

Éditeur : NORMATYS. Application dans la certification Effinature : IRICE. Moteur de calcul libre : le moteur OpenNAT, qui porte le nom de la méthode.
Version 1, édition complète du 18 octobre 2026, avec les modules dynamiques : climat horaire et trajectoire de réchauffement de référence, bilan hydrique horaire, éclairage horaire, maturation et gestion, calendrier du chantier au pas mensuel. Projet soumis à la validation du Biodiversity Standard Council : la méthode, ses conventions et ses seuils ne sont pas opposables tant que le conseil ne les a pas validés.
Texte et tables de données sous licence CC BY 4.0, chaque valeur portant la licence de sa source. Moteur sous licence AGPL-3.0-or-later.

## Organisation de l'édition complète

L'édition complète suit le plan de l'annexe III de l'arrêté du 4 août 2021 (méthode Th-BCE 2020) : un texte général, des données conventionnelles séparées, des fiches algorithmes qui décrivent les éléments codés dans le cœur de calcul, des fiches d'application pour les configurations particulières.

| Partie | Contenu |
|---|---|
| 1 | Texte de la méthode : objet, définitions, principes, données d'entrée, algorithme, modules (dont le bilan hydrique), indicateurs, incertitude, seuils, récapitulatif, exemple complet |
| 2 | Données conventionnelles : nomenclature et toutes les valeurs des tables, avec leur source, et synthèse mensuelle des années types horaires des huit zones climatiques |
| 3 | Fiches algorithmes A01 à A58, au format des fiches de la méthode Th-BCE, avec leur pseudo-code et un second cas élémentaire ; les fiches A43 à A58 décrivent les modules dynamiques |
| 4 | Fiches habitats H001 à H191, avec les listes complètes de correspondances et d'espèces |
| 5 | Fiches d'application F01 à F30 et leurs exemples chiffrés |
| 6 | Protocoles de relevé des grilles d'état et liste des espèces exotiques envahissantes |
| 7 | Récapitulatif standardisé RSNat : schéma, dictionnaire des données, exemple |
| 8 | Cas de validation : les huit cas du cahier des charges, trente et un cas complémentaires et vingt-neuf cas dynamiques |
| 9 | Conventions |
| 10 | Bibliographie |
"""
    morceaux = [tete, '## Partie 1. Texte de la méthode\n', partie1]
    for nom in ('02_donnees_conventionnelles.md', '03a_fiches_algorithmes.md', '03b_fiches_algorithmes.md',
                '03c_fiches_algorithmes.md', '03d_fiches_algorithmes.md', '03e_pseudo_code.md',
                '03f_fiches_dynamiques.md', '04_fiches_habitats.md',
                '05_fiches_application.md', '05b_exemples_application.md', '06_protocoles.md', '07_rsnat.md', '08_cas_validation.md'):
        morceaux.append(lire(os.path.join(EDITION, nom)))
    morceaux += [conventions, biblio]
    texte = '\n\n'.join(m.strip() for m in morceaux) + '\n'
    texte = re.sub(r'\n{3,}', '\n\n', texte)
    sortie = os.path.join(RACINE, 'methode', 'OpenNAT_v1_edition_complete.md')
    with open(sortie, 'w', encoding='utf-8') as f:
        f.write(texte)
    print(sortie, len(texte), 'caractères')


if __name__ == '__main__':
    main()
