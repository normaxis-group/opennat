# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit donnees/habitats.csv depuis les sources primaires.

Entrées :
- donnees/nomenclature_habitats.csv : correspondances écrites à la main (types OpenNAT,
  code BKompV, ligne de la métrique anglaise, justification) ;
- sources/biotopwert_de/bkompv_anlage2.csv : extraction de l'annexe 2 de la BKompV ;
- sources/uk_metric/extraits/*.csv : onglets G-1, G-3, G-4 et G-6 du tableur statutaire 1.0.4.

Aucune valeur n'est saisie dans ce script : il lit, convertit et écrit, chaque ligne avec
sa source et sa référence précise. Les conventions appliquées sont citées par leur numéro
(methode/conventions.md).
"""
import csv
import os
import statistics
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RACINE, 'sources')
DON = os.path.join(RACINE, 'donnees')

URL_BKOMPV = 'https://www.gesetze-im-internet.de/bkompv/anlage_2.html'
URL_UK = ('https://assets.publishing.service.gov.uk/media/6867e62810d550c668de3b4e/'
          'The_Statutory_Metric_Macro_Disabled_1.0.4.xlsx')
LIC_BKOMPV = 'texte réglementaire, § 5 UrhG'
LIC_UK = 'Open Government Licence v3.0'

COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max',
            'source', 'reference_precise', 'url', 'licence', 'type', 'convention',
            'justification']

DIFFICULTE = {'Low': 1.0, 'Medium': 0.67, 'High': 0.33, 'Very High': 0.1}

# Convention C-I1 (plages d'incertitude par classe de source, point P18 de l'audit)
PLAGE = {'reglement': 0.10, 'expert': 0.25, 'convention': 0.50}


def lire_bkompv():
    valeurs = {}
    chemin = os.path.join(SRC, 'biotopwert_de', 'bkompv_anlage2.csv')
    with open(chemin, encoding='utf-8') as f:
        for i, (code, nom, val) in enumerate(csv.reader(f), 1):
            if val.strip().isdigit():
                # le code 44.03.02J apparaît deux fois dans le texte publié : la première
                # occurrence est gardée, la nomenclature n'y renvoie pas
                valeurs.setdefault(code.strip(), (int(val), nom, i))
    return valeurs


def lire_extrait(nom):
    with open(os.path.join(SRC, 'uk_metric', 'extraits', nom + '.csv'), encoding='utf-8') as f:
        return list(csv.reader(f))


def lire_uk():
    g1 = {}
    for r in lire_extrait('G-1 All Habitats'):
        if r[0] in ('1', '2') or not r[2]:
            continue
        g1.setdefault(r[2], {'distinctivite': r[12], 'ligne_g1': r[0]})
    g3 = {}
    for r in lire_extrait('G-3 Multipliers'):
        if r[0] in ('1', '2') or not r[1]:
            continue
        g3[r[1]] = {'creation': r[3], 'amelioration': r[5], 'ligne_g3': r[0]}
    g4 = {}
    for r in lire_extrait('G-4 Temporal multipliers'):
        if len(r) > 11 and r[6] and r[0] not in ('2', '3'):
            g4.setdefault(r[6], {'bon': r[7], 'moyen': r[9], 'mauvais': r[11], 'sans_etat': r[12],
                                  'ligne_g4': r[0]})
    # année « 30+ » : la table des multiplicateurs temporels de G-4 lui associe la ligne
    # suivant l'année 31, soit 32 ans (convention C-T2)
    haies = {}
    for r in lire_extrait('G-6 Hedgerow Data'):
        if r[0] in ('1', '2') or not r[2]:
            continue
        haies[r[2]] = {'distinctivite': r[4], 'mauvais': r[5], 'moyen': r[7], 'bon': r[9],
                       'difficulte': next((x for x in r[30:] if x in DIFFICULTE), ''),
                       'ligne_g6': r[0]}
    arbres = {}
    for r in lire_extrait('G-3 Multipliers'):
        if len(r) > 27 and r[24] in ('Small', 'Medium', 'Large', 'Very large'):
            arbres[r[24]] = {'diametre_m': r[25], 'rpa_ha': r[27], 'ligne_g3': r[0]}
    return g1, g3, g4, haies, arbres


def annees(texte):
    t = (texte or '').strip()
    if t == '30+':
        return 32.0, 'C-T2'
    try:
        return float(t), ''
    except ValueError:
        return None, ''


def ligne(cle, parametre, valeur, unite, classe, source, ref, url, licence, typ,
          convention='', justification=''):
    p = PLAGE[classe]
    v = float(valeur)
    haut = v * (1 + p)
    if parametre.startswith(('difficulte', 'valeur_intrinseque')):
        haut = min(haut, 1.0)  # un multiplicateur de risque et une valeur ramenée à 1 ne dépassent pas 1
    return {'cle': cle, 'parametre': parametre, 'valeur': round(v, 4), 'unite': unite,
            'incertitude_min': round(v * (1 - p), 4), 'incertitude_max': round(haut, 4),
            'source': source, 'reference_precise': ref, 'url': url, 'licence': licence,
            'type': typ, 'convention': convention, 'justification': justification}


def main():
    bk = lire_bkompv()
    g1, g3, g4, haies, arbres = lire_uk()
    with open(os.path.join(DON, 'nomenclature_habitats.csv'), encoding='utf-8') as f:
        nomen = list(csv.DictReader(f, delimiter=';'))

    erreurs = []
    sorties = []

    # 1. rapport de transposition UK vers l'échelle BKompV (convention C-H3) : médiane, sur
    # les types qui ont les deux valeurs, de (BKompV / 24) / (distinctivité UK / 8)
    rapports = []
    for n in nomen:
        code, uk = n['bkompv_code'], n['uk_habitat']
        if code and code in bk and uk in g1:
            d = float(g1[uk]['distinctivite'] or 0)
            if d > 0:
                rapports.append((bk[code][0] / 24) / (d / 8))
    r_uk = statistics.median(rapports)
    sorties.append(ligne('*', 'rapport_transposition_uk', r_uk, 'sans unité', 'convention',
                         'BKompV Anlage 2 ; Statutory Biodiversity Metric 1.0.4, G-1',
                         f'médiane sur {len(rapports)} types appariés de la nomenclature',
                         URL_BKOMPV + ' ; ' + URL_UK, LIC_BKOMPV + ' ; ' + LIC_UK,
                         'convention', 'C-H3',
                         'Rapport médian entre la valeur BKompV ramenée à 1 et la distinctivité '
                         'anglaise ramenée à 1, pour les types présents dans les deux listes'))

    for n in nomen:
        cle, code, uk = n['code_vinat'], n['bkompv_code'], n['uk_habitat']
        # valeur intrinsèque (équation H1, conventions C-H1 et C-H3)
        if code:
            if code not in bk:
                erreurs.append(f'{cle} : code BKompV {code} introuvable')
                continue
            val, nom, num = bk[code]
            sorties.append(ligne(cle, 'valeur_intrinseque', val / 24, 'm²HE/m²', 'reglement',
                                 'BKompV Anlage 2 (BGBl. I 2020, 1088)',
                                 f'code {code}, « {nom} », Biotoptypenwert {val} sur 24 '
                                 f'(ligne {num} de l\'extraction)', URL_BKOMPV, LIC_BKOMPV,
                                 'transposition', 'C-H1',
                                 n['justification']))
            # stades J, M, A disponibles pour les types ligneux (convention C-H5)
            base = code[:-1] if code[-1] in 'JMA' and code[:-1] + 'J' in bk else None
            if base:
                for st in 'JMA':
                    if base + st in bk:
                        v, nm, nl = bk[base + st]
                        sorties.append(ligne(cle, f'valeur_intrinseque_stade_{st}', v / 24,
                                             'm²HE/m²', 'reglement',
                                             'BKompV Anlage 2 (BGBl. I 2020, 1088)',
                                             f'code {base + st}, « {nm} », {v} sur 24',
                                             URL_BKOMPV, LIC_BKOMPV, 'transposition', 'C-H5'))
        else:
            if uk not in g1:
                erreurs.append(f'{cle} : ligne anglaise {uk} introuvable')
                continue
            d = float(g1[uk]['distinctivite'])
            sorties.append(ligne(cle, 'valeur_intrinseque', d / 8 * r_uk, 'm²HE/m²',
                                 'convention',
                                 'Statutory Biodiversity Metric 1.0.4 (Defra, Natural England)',
                                 f'onglet G-1, ligne {g1[uk]["ligne_g1"]}, « {uk} », '
                                 f'distinctivité {d:g} sur 8, multipliée par le rapport C-H3',
                                 URL_UK, LIC_UK, 'convention', 'C-H3', n['justification']))

        # délais de maturité et difficultés (module T, équations T3 et T4)
        if n['position'] == 'lineaire' and uk in haies:
            h = haies[uk]
            for cond in ('bon', 'moyen', 'mauvais'):
                a, conv = annees(h[cond])
                if a is not None:
                    sorties.append(ligne(cle, f'delai_maturite_{cond}', a, 'an', 'reglement',
                                         'Statutory Biodiversity Metric 1.0.4',
                                         f'onglet G-6, ligne {h["ligne_g6"]}, « {uk} », '
                                         f'condition {cond}', URL_UK, LIC_UK, 'transposition',
                                         conv))
            if h['difficulte'] in DIFFICULTE:
                sorties.append(ligne(cle, 'difficulte_creation', DIFFICULTE[h['difficulte']],
                                     'sans unité', 'reglement',
                                     'Statutory Biodiversity Metric 1.0.4',
                                     f'onglet G-6, ligne {h["ligne_g6"]}, difficulté '
                                     f'{h["difficulte"]} ; onglet G-3, table Difficulty',
                                     URL_UK, LIC_UK, 'transposition'))
            continue
        if uk not in g4 or uk not in g3:
            erreurs.append(f'{cle} : ligne anglaise {uk} absente de G-3 ou G-4')
            continue
        t = g4[uk]
        for cond in ('bon', 'moyen', 'mauvais', 'sans_etat'):
            a, conv = annees(t[cond])
            if a is not None:
                libelle = ('habitat sans évaluation d\'état (colonne Condition Assessment N/A)'
                           if cond == 'sans_etat' else f'condition cible {cond}')
                sorties.append(ligne(cle, f'delai_maturite_{cond}', a, 'an', 'reglement',
                                     'Statutory Biodiversity Metric 1.0.4',
                                     f'onglet G-4, ligne {t["ligne_g4"]}, « {uk} », {libelle}',
                                     URL_UK, LIC_UK, 'transposition', conv))
        m = g3[uk]
        for nature, cle_g3 in (('creation', 'creation'), ('amelioration', 'amelioration')):
            sorties.append(ligne(cle, f'difficulte_{nature}', float(m[cle_g3]), 'sans unité',
                                 'reglement', 'Statutory Biodiversity Metric 1.0.4',
                                 f'onglet G-3, ligne {m["ligne_g3"]}, « {uk} »', URL_UK,
                                 LIC_UK, 'transposition'))

    # surfaces de référence des arbres par classe de diamètre (point P11, convention C-H5)
    for taille, a in arbres.items():
        sorties.append(ligne('VB.18', f'surface_defaut_houppier_{taille.lower().replace(" ", "_")}',
                             float(a['rpa_ha']) * 10000, 'm²', 'reglement',
                             'Statutory Biodiversity Metric 1.0.4',
                             f'onglet G-3, table Individual trees, ligne {a["ligne_g3"]}, '
                             f'{taille}, diamètre {a["diametre_m"]} m, RPA {a["rpa_ha"]} ha',
                             URL_UK, LIC_UK, 'transposition', 'C-H5',
                             'Surface de la zone de protection racinaire, retenue par défaut '
                             'quand le houppier n\'est pas relevé'))

    if erreurs:
        print('\n'.join(erreurs), file=sys.stderr)
        sys.exit(1)
    with open(os.path.join(DON, 'habitats.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        w.writerows(sorties)
    print(f'habitats.csv : {len(sorties)} lignes, {len(nomen)} types, rapport C-H3 = {r_uk:.3f}')


if __name__ == '__main__':
    main()
