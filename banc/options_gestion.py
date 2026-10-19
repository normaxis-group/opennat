# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Option pour la décision D7 (conventions C-M2 et C-M3) : fin du plan de gestion progressive.

Aujourd'hui (fiche A56-2), quand le plan de gestion écologique s'achève, une prairie ou une haie passe en une année à
la valeur de la gestion courante (gazon d'agrément, haie au stade jeune). L'option étale la perte sur N années :
f = 1 - (1 - f_cible) × min(1 ; durée écoulée depuis la fin du plan / N). Elle ne touche que les unités qui sortent
d'un plan ; une unité déclarée en gestion courante dès la livraison garde sa valeur courante d'emblée.

Le script remplace la fonction le temps du calcul, sans modifier le moteur ni les tables, et calcule Cnat pour les
73 cas du banc avec N = 0 (actuel), 2 et 3 ans.

Usage : python -m banc.options_gestion   (écrit banc/options_gestion.json)
"""
import json
import os
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
from opennat import chaine, projet, temps  # noqa: E402
from opennat import numerique as nm  # noqa: E402
from opennat.donnees import Parametres, Tables  # noqa: E402

ORIGINE = temps.facteur_gestion
DUREES = (0, 2, 3)


def progressif(n_annees):
    def facteur(P, u, reg, duree):
        cible = ORIGINE(P, u, reg, duree)
        if n_annees <= 0 or reg != 'courante' or u.get('gestion') in ('courante', 'abandon'):
            return cible
        return 1 - (1 - cible) * nm.mini(1.0, duree / n_annees)
    return facteur


def cnat_cas(T, nom):
    P = Parametres(T)
    e, j = projet.normaliser(P, projet.lire(os.path.join(ICI, 'cas', nom)))
    r = chaine.calculer(P, e, e['variantes'][0], j)
    return float(r['etapes']['E3']['indicateurs']['cnat']), e['gestion'].get('plan_annees', 0)


def main():
    T = Tables()
    noms = sorted(os.listdir(os.path.join(ICI, 'cas')))
    res = {}
    try:
        for n in DUREES:
            temps.facteur_gestion = progressif(n)
            res[n] = {nom: cnat_cas(T, nom) for nom in noms}
    finally:
        temps.facteur_gestion = ORIGINE
    sortie = {'cas': {}, 'resume': {}}
    for nom in noms:
        c0, plan = res[0][nom]
        sortie['cas'][nom] = dict(plan=plan, **{f'cnat_{n}_ans': res[n][nom][0] for n in DUREES})
    for n in DUREES[1:]:
        ecarts = [res[n][k][0] - res[0][k][0] for k in noms]
        touches = [e for e in ecarts if abs(e) > 1e-6]
        sortie['resume'][f'{n}_ans'] = dict(cas_touches=len(touches), cas=len(noms),
                                            ecart_median=statistics.median(touches) if touches else 0.0,
                                            ecart_min=min(touches) if touches else 0.0,
                                            ecart_max=max(touches) if touches else 0.0)
    a = sortie['cas']['exemple_de_l_annexe_c.json']
    sortie['annexe_c'] = a
    with open(os.path.join(ICI, 'options_gestion.json'), 'w', encoding='utf-8') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print('annexe C :', {k: round(v, 1) for k, v in a.items()})
    for k, v in sortie['resume'].items():
        print(k, v)
    return sortie


if __name__ == '__main__':
    main()
