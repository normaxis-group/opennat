# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 2 de l'édition complète : données conventionnelles, imprimées depuis donnees/."""
import csv
import os
from collections import OrderedDict

from commun import DON, SOURCES, TYPES, ecrire, lire, nombre, tableau

TABLES = OrderedDict([
    ('contexte.csv', ('Contexte, période et temps', 'Période de référence, actualisation, fermeture des surfaces, '
                      'situation dans la trame verte et bleue, zones biogéographiques, chantier.')),
    ('sols.csv', ('Coefficients de sol', 'Natures de surface du module S et de Bnat, médianes des grilles de '
                  'coefficient de biotope relevées (convention C-S1).')),
    ('connectivite.csv', ('Connectivité', 'Effet de taille des taches, connectivité, clôtures (module C).')),
    ('nuisances.csv', ('Nuisances', 'Lumière artificielle, bruit, vitrages (module N).')),
    ('eau.csv', ('Eau', 'Alimentation des milieux en eau, gestion des eaux pluviales (module E).')),
    ('materiaux.csv', ('Matériaux et climat', 'Facteur de caractérisation du climat, occupation des sols du '
                       'bois et des carrières, indicateurs de pollution (module G).')),
    ('seuils.csv', ('Seuils proposés', 'Seuils de Bnat, de la pleine terre et de Cnat, en attente de validation '
                    'du Biodiversity Standard Council.')),
    ('etat_criteres.csv', ('Grilles d\'état', 'Critères et règles des onze grilles d\'état (module H).')),
])

PARAM = {
    'valeur_intrinseque': 'valeur intrinsèque', 'valeur_intrinseque_stade_J': 'valeur, stade jeune',
    'valeur_intrinseque_stade_M': 'valeur, stade moyen', 'valeur_intrinseque_stade_A': 'valeur, stade âgé',
    'delai_maturite_bon': 'délai, bon état', 'delai_maturite_moyen': 'délai, état moyen',
    'delai_maturite_mauvais': 'délai, mauvais état', 'delai_maturite_sans_etat': 'délai, sans état',
    'delai_amelioration_mauvais_moyen': 'amélioration, mauvais vers moyen',
    'delai_amelioration_mauvais_bon': 'amélioration, mauvais vers bon',
    'delai_amelioration_moyen_bon': 'amélioration, moyen vers bon',
    'difficulte_creation': 'difficulté de création', 'difficulte_amelioration': 'difficulté d\'amélioration',
}


def plage(r):
    a, b = nombre(r['incertitude_min']), nombre(r['incertitude_max'])
    return a if a == b else f'{a} à {b}'


def registre(lignes, avec_cle=True):
    ent = (['Clé'] if avec_cle else []) + ['Paramètre', 'Valeur', 'Unité', 'Plage', 'Type', 'Conv.',
                                           'Source et référence précise']
    rows = []
    for r in lignes:
        rows.append(([r['cle']] if avec_cle else []) + [
            PARAM.get(r['parametre'], r['parametre'].replace('_', ' ')), nombre(r['valeur']), r['unite'],
            plage(r), TYPES[r['type']], r['convention'], f'{r["source"]}, {r["reference_precise"]}'])
    return tableau(ent, rows)


def main():
    out = ['## Partie 2. Données conventionnelles', '',
           'Les données conventionnelles jouent ici le rôle du chapitre 2 de la méthode Th-BCE : elles sont '
           'séparées des fiches algorithmes, qui les appellent par leur clé et leur paramètre. Elles sont '
           'imprimées ci-dessous telles qu\'elles figurent dans les tables `donnees/` de la version 1 ; la table '
           'fait foi en cas d\'écart avec une transcription.', '',
           'Chaque valeur porte une plage d\'incertitude (borne basse et borne haute) utilisée par l\'analyse '
           'd\'incertitude, un type et, le cas échéant, le numéro de la convention qui la fixe. Types : primaire, '
           'valeur lue telle quelle dans la source ; transposée, valeur lue dans une source primaire et appliquée '
           'par une correspondance ou un changement d\'échelle écrit en convention ; secondaire, valeur lue dans '
           'une source qui en cite une autre, à remplacer ; convention, valeur fixée et justifiée par la méthode.',
           '']
    # 2.1 nomenclature
    nomen = list(csv.DictReader(open(os.path.join(DON, 'nomenclature_habitats.csv'), encoding='utf-8'),
                                delimiter=';'))
    out += ['### 2.1 Nomenclature des habitats', '',
            f'La nomenclature compte {len(nomen)} types : '
            f'{sum(1 for n in nomen if n["code_vinat"].startswith("VB"))} types urbains et hors-sol, codés VB, '
            f'et {sum(1 for n in nomen if not n["code_vinat"].startswith("VB"))} types EUNIS 2012 de niveau 3 '
            'présents en France métropolitaine (HabRef v7), hors milieux littoraux et marins, grottes, glaciers et '
            'reliefs volcaniques. Pour chaque type, la table donne le code BKompV d\'où vient la valeur '
            'intrinsèque, la ligne de la métrique anglaise d\'où viennent les délais et difficultés, et la '
            'justification de ces deux correspondances. Les codes EUNIS 2012 du groupe J se saisissent par le type '
            'VB indiqué en colonne « Rattachés ».', '']
    out.append(tableau(['Code', 'Libellé', 'EUNIS 2012', 'Rattachés', 'Position', 'BKompV',
                        'Métrique anglaise'],
                       [[n['code_vinat'], n['libelle_fr'], n['code_eunis_2012'], n['alias_eunis_2012'],
                         n['position'].replace('_', ' '), n['bkompv_code'] or 'aucun', n['uk_habitat']]
                        for n in nomen]))
    out += ['', '#### Justification des correspondances', '']
    out.append(tableau(['Code', 'Justification'], [[n['code_vinat'], n['justification']] for n in nomen]))

    # 2.2 habitats : tableaux synoptiques puis registre complet
    hab = lire('habitats.csv')
    par = {}
    for r in hab:
        par.setdefault(r['cle'], {})[r['parametre']] = r
    out += ['', '### 2.2 Valeurs des habitats', '',
            'Les valeurs des habitats sont construites par `outils/construire_habitats.py` depuis l\'annexe 2 de la '
            'BKompV et le tableur statutaire anglais 1.0.4 : aucune n\'est saisie à la main. Les tableaux '
            'synoptiques ci-dessous les regroupent par type ; le registre qui suit donne chaque valeur avec sa '
            'référence précise.', '', '#### Valeurs intrinsèques et stades', '']
    g = lambda c, p: nombre(par[c][p]['valeur']) if p in par.get(c, {}) else ''
    out.append(tableau(['Code', 'Libellé', 'Valeur', 'Stade J', 'Stade M', 'Stade A', 'Difficulté de création',
                        'Difficulté d\'amélioration'],
                       [[n['code_vinat'], n['libelle_fr'], g(n['code_vinat'], 'valeur_intrinseque'),
                         g(n['code_vinat'], 'valeur_intrinseque_stade_J'),
                         g(n['code_vinat'], 'valeur_intrinseque_stade_M'),
                         g(n['code_vinat'], 'valeur_intrinseque_stade_A'),
                         g(n['code_vinat'], 'difficulte_creation'),
                         g(n['code_vinat'], 'difficulte_amelioration')] for n in nomen]))
    out += ['', '#### Délais de maturité et d\'amélioration, en années', '']
    out.append(tableau(['Code', 'Bon', 'Moyen', 'Mauvais', 'Sans état', 'Mauvais vers moyen', 'Mauvais vers bon',
                        'Moyen vers bon'],
                       [[n['code_vinat']] + [g(n['code_vinat'], p) for p in (
                           'delai_maturite_bon', 'delai_maturite_moyen', 'delai_maturite_mauvais',
                           'delai_maturite_sans_etat', 'delai_amelioration_mauvais_moyen',
                           'delai_amelioration_mauvais_bon', 'delai_amelioration_moyen_bon')] for n in nomen]))
    out += ['', 'Une case vide signifie que la métrique anglaise ne prévoit pas ce délai (« Not Possible ») : '
                'l\'habitat ne peut pas être créé ou amélioré dans cette classe d\'état. Un délai de 32 ans '
                'transpose le « 30+ » anglais (convention C-T2).', '',
            '#### Registre des valeurs des habitats', '']
    for n in nomen:
        lignes = [r for r in hab if r['cle'] == n['code_vinat']]
        out += [f'**{n["code_vinat"]} {n["libelle_fr"]}**', '', registre(lignes, avec_cle=False), '']
    autres = [r for r in hab if r['cle'] not in {n['code_vinat'] for n in nomen}]
    if autres:
        out += ['**Valeurs communes et arbres**', '', registre(autres), '']

    # 2.3 et suivantes : tables de coefficients
    for i, (nom, (titre, objet)) in enumerate(TABLES.items(), 3):
        lignes = lire(nom)
        out += [f'### 2.{i} {titre} (`{nom}`)', '', objet, '', registre(lignes), '']
        if nom == 'etat_criteres.csv':
            out += ['Le libellé de chaque critère est dans la colonne « justification » de la table ; il est '
                    'repris en entier dans les fiches habitats (partie 4) et dans les protocoles de relevé '
                    '(partie 6).', '']
            out.append(tableau(['Grille', 'Critère', 'Libellé'],
                               [[r['cle'], r['parametre'].replace('critere_', '').replace('_essentiel',
                                 ' (essentiel)').replace('indicateur_', 'indicateur ').replace('_', ' '),
                                 r['justification']] for r in lignes if r['cle'] != '*']))
            out.append('')

    # extraits des sources
    out += ['### 2.11 Extraits des sources primaires utilisés', '',
            'Les deux tableaux suivants reproduisent les lignes des sources primaires effectivement appelées par '
            'la nomenclature : la liste allemande des valeurs de biotopes (texte réglementaire libre de droits) et '
            'les lignes de la métrique anglaise (Open Government Licence v3.0).', '',
            '#### Annexe 2 de la BKompV, types appelés', '']
    bk = {}
    with open(os.path.join(SOURCES, 'biotopwert_de', 'bkompv_anlage2.csv'), encoding='utf-8') as f:
        for code, libelle, val in csv.reader(f):
            if val.strip().isdigit():
                bk.setdefault(code.strip(), (libelle, val))
    appeles = sorted({n['bkompv_code'] for n in nomen if n['bkompv_code']})
    lignes = []
    for c in appeles:
        base = c[:-1] if c[-1] in 'JMA' and c[:-1] + 'J' in bk else c
        for code in ([base + s for s in 'JMA' if base + s in bk] if base != c else [c]):
            lignes.append([code, bk[code][0], bk[code][1], nombre(int(bk[code][1]) / 24)])
    out.append(tableau(['Code', 'Biotoptyp (libellé de l\'annexe 2)', 'Biotoptypenwert (sur 24)',
                        'Valeur OpenNAT (sur 1)'], lignes))
    out += ['', '#### Métrique statutaire anglaise, lignes appelées', '']
    uk = sorted({n['uk_habitat'] for n in nomen})
    out.append(tableau(['Ligne de la métrique', 'Types OpenNAT qui y renvoient'],
                       [[u, ', '.join(n['code_vinat'] for n in nomen if n['uk_habitat'] == u)] for u in uk]))
    # liste allemande complète et onglets anglais complets
    out += ['### 2.12 Annexe 2 de la BKompV, liste complète', '',
            "Liste complète des types de biotopes de l'annexe 2 de la BKompV et de leur valeur sur 24, dans l'ordre "
            "du texte (extraction du 18/10/2026). Les intitulés de rubrique, sans valeur, structurent la liste. "
            "Les types appelés par la nomenclature OpenNAT sont repris en 2.11.", '']
    lignes = []
    with open(os.path.join(SOURCES, 'biotopwert_de', 'bkompv_anlage2.csv'), encoding='utf-8') as f:
        for code, libelle, val in csv.reader(f):
            if code == 'Code':
                continue
            lignes.append([code.strip(), libelle, val, nombre(int(val) / 24) if val.strip().isdigit() else ''])
    out.append(tableau(['Code', 'Biotoptyp', 'Valeur sur 24', 'Valeur sur 1'], lignes))
    ext = os.path.join(SOURCES, 'uk_metric', 'extraits')

    def onglet(nom, colonnes, entetes, filtre=lambda r: True, debut=2):
        rows = []
        with open(os.path.join(ext, nom + '.csv'), encoding='utf-8') as f:
            for i, r in enumerate(csv.reader(f)):
                if i < debut or not filtre(r):
                    continue
                rows.append([r[c] if c < len(r) else '' for c in colonnes])
        return tableau(entetes, rows)

    out += ['', '### 2.13 Métrique statutaire anglaise, onglets utilisés', '',
            "Reproduction des colonnes utilisées des onglets G-1, G-4 et G-5 du tableur statutaire 1.0.4 "
            "(Defra et Natural England, Open Government Licence v3.0). « Not Possible » signifie que la création ou "
            "l'amélioration n'est pas admise par la métrique pour cette classe d'état.", '',
            '#### Onglet G-1, habitats, distinctivité et difficultés', '',
            onglet('G-1 All Habitats', (2, 11, 12, 14, 15, 16, 17),
                   ['Habitat', 'Distinctivité', 'Score', 'Difficulté de création', 'Multiplicateur',
                    "Difficulté d'amélioration", 'Multiplicateur'], lambda r: bool(r[2])), '',
            '#### Onglet G-4, délais de création par condition visée (années)', '',
            onglet('G-4 Temporal multipliers', (6, 7, 8, 9, 10, 11, 12),
                   ['Habitat', 'Bon', 'Assez bon', 'Moyen', 'Assez mauvais', 'Mauvais', 'Sans état'],
                   lambda r: len(r) > 7 and bool(r[6]) and r[6] != 'Habitat Description', 3), '',
            "#### Onglet G-4, multiplicateur temporel par année (option d'actualisation, convention C-T5)", '',
            onglet('G-4 Temporal multipliers', (1, 2, 3), ['Année', "% de l'unité d'origine", 'Multiplicateur'],
                   lambda r: len(r) > 3 and r[1] not in ('', 'Year', 'Temporal multipliers'), 3), '',
            "#### Onglet G-5, délais d'amélioration (années)", '',
            onglet('G-5 Enhancement Temporal', (3, 16, 18, 23),
                   ['Habitat', 'Mauvais vers moyen', 'Mauvais vers bon', 'Moyen vers bon'],
                   lambda r: len(r) > 23 and bool(r[3]), 3), '']
    print(ecrire('02_donnees_conventionnelles.md', '\n'.join(out)))


if __name__ == '__main__':
    main()
