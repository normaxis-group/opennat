# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Banc de non-régression : fige les sorties du moteur et signale toute grandeur qui bouge.

Le banc de validation (`banc.comparer`) confronte le moteur au carnet de référence sur les grandeurs que le carnet
calcule. Le banc de non-régression va plus loin : il fige toutes les grandeurs numériques de toutes les étapes de
chaque cas (E1 à E5, modules S, H, C, N, E, W, T, G, détail de chaque unité ; une série est résumée par sa
longueur, sa somme, son minimum et son maximum), plus une analyse d'incertitude complète de l'exemple de l'annexe C
et de sa variante « plan de gestion de 50 ans » (200 tirages, graine par défaut). Il porte l'empreinte des tables :
si les données changent, le banc l'écrit et demande d'inscrire la nouvelle version au journal des versions avant
de régénérer l'instantané.

Usage :
    python -m banc.regression            contrôle (sortie 0 si rien n'a bougé)
    python -m banc.regression --ecrire   régénère `banc/regression.json` après une évolution voulue
"""
import copy
import json
import math
import os
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat import VERSION_METHODE, VERSION_MOTEUR, chaine, incertitude, projet  # noqa: E402
from opennat.donnees import Parametres, Tables  # noqa: E402

INSTANTANE = os.path.join(ICI, 'regression.json')
TOL_REL, TOL_ABS = 1e-6, 1e-9
TIRAGES = 200


def aplatir(x, prefixe='', sortie=None) -> dict:
    """Toutes les feuilles numériques d'un résultat, à plat ; une série devient longueur, somme, minimum, maximum."""
    sortie = {} if sortie is None else sortie
    if isinstance(x, dict):
        for k, v in x.items():
            aplatir(v, f'{prefixe}/{k}', sortie)
    elif isinstance(x, np.ndarray) and x.ndim == 0:
        aplatir(x.item(), prefixe, sortie)
    elif isinstance(x, (list, tuple, np.ndarray)):
        if len(x) and all(isinstance(y, (int, float, np.integer, np.floating)) and not isinstance(y, bool) for y in x):
            a = np.asarray(x, dtype=float)
            sortie.update({f'{prefixe}#n': float(a.size), f'{prefixe}#somme': float(a.sum()),
                           f'{prefixe}#min': float(a.min()), f'{prefixe}#max': float(a.max())})
        else:
            for i, v in enumerate(x):
                cle = v.get('id', i) if isinstance(v, dict) else i
                aplatir(v, f'{prefixe}/{cle}', sortie)
    elif isinstance(x, bool):
        sortie[prefixe] = float(x)
    elif isinstance(x, (int, float, np.integer, np.floating)):
        sortie[prefixe] = float(x)
    return sortie


def sorties_cas(T: Tables, chemin: str) -> dict:
    P = Parametres(T)
    e, journal = projet.normaliser(P, projet.lire(chemin))
    r = chaine.calculer(P, e, e['variantes'][0], journal)
    return aplatir(r)


def sorties_incertitude(T: Tables) -> dict:
    p = projet.lire(os.path.join(ICI, 'cas', 'exemple_de_l_annexe_c.json'))
    v = copy.deepcopy(p['variantes'][0])
    v.update(nom='Plan de gestion de 50 ans', reference=False, gestion={'plan_annees': 50})
    p['variantes'].append(v)
    p['options'] = {'tirages': TIRAGES}
    e, _ = projet.normaliser(Parametres(T), p)
    inc = incertitude.analyser(T, e, None)
    s = {}
    for i, r in inc.items():
        for x in r['Intervalle']:
            for q in ('p5', 'p50', 'p95'):
                s[f'variante_{i}/{x["indicateur"]}/{q}'] = x[q]
        s[f'variante_{i}/influents'] = ' ; '.join(f'{y["table"]}:{y["cle"]}:{y["parametre"]}'
                                                   for y in r['Parametre_Influent'])
    return s


def calculer_tout(dire=print) -> dict:
    T = Tables()
    cas = {}
    t0 = time.time()
    for nom in sorted(os.listdir(os.path.join(ICI, 'cas'))):
        cas[nom] = sorties_cas(T, os.path.join(ICI, 'cas', nom))
    dire(f'{len(cas)} cas calculés ({time.time() - t0:.0f} s)')
    t0 = time.time()
    inc = sorties_incertitude(T)
    dire(f'incertitude de l\'exemple de l\'annexe C, {TIRAGES} tirages ({time.time() - t0:.0f} s)')
    return dict(methode=VERSION_METHODE, moteur=VERSION_MOTEUR, empreinte_tables=T.empreinte, cas=cas,
                incertitude=inc)


def proche(a, b) -> bool:
    if isinstance(a, str) or isinstance(b, str):
        return a == b
    if math.isnan(a) and math.isnan(b):
        return True
    return abs(a - b) <= max(TOL_ABS, TOL_REL * abs(b))


def comparer(nouveau: dict, ancien: dict) -> list[str]:
    ecarts = []
    if nouveau['empreinte_tables'] != ancien['empreinte_tables']:
        ecarts.append(f'tables modifiées (empreinte {ancien["empreinte_tables"][:12]} devenue '
                      f'{nouveau["empreinte_tables"][:12]}) : inscrire la version des données au journal des '
                      f'versions, puis régénérer par python -m banc.regression --ecrire')
    for nom in sorted(set(ancien['cas']) | set(nouveau['cas'])):
        a, n = ancien['cas'].get(nom), nouveau['cas'].get(nom)
        if a is None or n is None:
            ecarts.append(f'{nom} : cas {"ajouté" if a is None else "retiré"}')
            continue
        for k in sorted(set(a) | set(n)):
            if k not in a or k not in n:
                ecarts.append(f'{nom} {k} : grandeur {"ajoutée" if k not in a else "retirée"}')
            elif not proche(n[k], a[k]):
                ecarts.append(f'{nom} {k} : {n[k]!r} contre {a[k]!r}')
    for k in sorted(set(ancien['incertitude']) | set(nouveau['incertitude'])):
        a, n = ancien['incertitude'].get(k), nouveau['incertitude'].get(k)
        if a is None or n is None or not proche(n, a):
            ecarts.append(f'incertitude {k} : {n!r} contre {a!r}')
    return ecarts


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    nouveau = calculer_tout()
    n = sum(len(x) for x in nouveau['cas'].values()) + len(nouveau['incertitude'])
    if '--ecrire' in argv:
        with open(INSTANTANE, 'w', encoding='utf-8') as f:
            json.dump(nouveau, f, ensure_ascii=False, indent=0, sort_keys=True)
            f.write('\n')
        print(f'instantané écrit : {n} grandeurs, tables {nouveau["empreinte_tables"][:12]}')
        return 0
    with open(INSTANTANE, encoding='utf-8') as f:
        ancien = json.load(f)
    ecarts = comparer(nouveau, ancien)
    for x in ecarts[:40]:
        print('ÉCART ' + x)
    print(f'{n - len(ecarts)} grandeurs sur {n} inchangées' + (f', {len(ecarts)} écarts' if ecarts else ''))
    return 1 if ecarts else 0


if __name__ == '__main__':
    sys.exit(main())
