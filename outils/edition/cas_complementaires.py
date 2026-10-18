# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Cas complémentaires du banc de validation : une même opération type déclinée sur plusieurs sites initiaux,
tailles de parcelle, typologies, durées de chantier, situations et éclairages.

Opération type : une part d'emprise bâtie e, 15 % de voirie, le reste en jardins (50 %), prairie urbaine (35 %)
et haie champêtre (15 %) en pleine terre, une toiture extensive sur la moitié de l'emprise, des arbres plantés
couvrant 10 % des espaces verts. Émissions par m² de S_ref de 480 (A1-A5), 330 (B) et 50 (C) kg CO2 éq. ;
S_ref = 2,2 x emprise ; 0,02 m³ de bois et 1,5 t de granulats par m² de S_ref.
"""
from cas_validation import DYN, U, ctx

PT = 'sol_pleine_terre'

SITES = {
    'culture': ('culture intensive', lambda s: [U('I1', 'I1.1', PT, s)]),
    'prairie': ('prairie de fauche en état moyen', lambda s: [U('I1', 'E2.2', PT, s, tache='I', criteres=(4, 6, False))]),
    'friche': ('friche urbaine en mosaïque', lambda s: [U('I1', 'VB.8', PT, 0.7 * s, tache='I', criteres=(3, 4, False)),
                                                       U('I2', 'VB.2', PT, 0.3 * s)]),
    'bois': ('chênaie-charmaie de stade moyen', lambda s: [U('I1', 'G1.A', PT, s, tache='I', stade='M',
                                                               criteres=(4, 6, False))]),
    'enrobe': ('parking entièrement revêtu', lambda s: [U('I1', 'VB.2', PT, s)]),
}


def projet(s, e, eclairage='L0', situation='hors_trame'):
    emprise, voirie = e * s, 0.15 * s
    vert = s - emprise - voirie
    k = dict(situation=situation)
    unites = [U('P1', 'VB.1', PT, emprise), U('P2', 'VB.2', PT, voirie),
              U('P3', 'VB.7', PT, 0.5 * vert, tache='J', criteres=(2, 3, False), **k),
              U('P4', 'VB.26', PT, 0.35 * vert, tache='J', criteres=(4, 6, False), eclairage=eclairage, **k),
              U('P5', 'FA.3', 'lineaire', 0.15 * vert, tache='J', stade='M', criteres=(6, 8, False), **k),
              U('P6', 'VB.18a', 'arbre', 0.10 * vert, tache='J', stade='M', criteres=(4, 6, False), **k),
              U('P7', 'VB.11', 'hors_sol_toiture', 0.5 * emprise, tache='T', epaisseur=10, criteres=(2, 3, False))]
    return unites


def cas(num, site, s, e=0.30, typo='logement', mois=18, zone='continentale', eclairage='L0',
        situation='hors_trame'):
    lib, initial = SITES[site]
    sref = 2.2 * e * s
    ini = initial(s)
    if situation != 'hors_trame':
        ini = [dict(u, situation=situation) for u in ini]
    return dict(
        nom=f'Cas C{num:02d}. {lib.capitalize()}, ' + f'{int(s):,}'.replace(',', ' ') + ' m²' +
            f', emprise {int(e * 100)} %, {typo}, chantier {mois} mois' +
            (f', {situation}' if situation != 'hors_trame' else '') +
            (f', éclairage {eclairage}' if eclairage != 'L0' else '') + (f', zone {zone}' if zone != 'continentale' else ''),
        attendu='voir la synthèse des cas complémentaires', parcelle=s, emprise=e * s, duree_chantier_mois=mois, sref=sref,
        contexte=ctx(zone, typo), **DYN, taches={'I': {}, 'J': {}, 'T': {}},
        initial=ini, projet=projet(s, e, eclairage, situation),
        ges={'phase_A1_A5': 480, 'phase_B': 330, 'phase_C': 50},
        bois=[('coupe_rase', 0.02 * sref, 0)], granulats=1.5 * sref)


CAS_SUPP = []
n = 0
for site in ('culture', 'prairie', 'friche', 'bois', 'enrobe'):
    for s in (1000, 5000, 20000):
        n += 1
        CAS_SUPP.append(cas(n, site, s))
for e, typo in ((0.45, 'logement'), (0.60, 'logement'), (0.50, 'tertiaire')):
    n += 1
    CAS_SUPP.append(cas(n, 'prairie', 5000, e=e, typo=typo))
for mois in (6, 36):
    n += 1
    CAS_SUPP.append(cas(n, 'friche', 5000, mois=mois))
for situation in ('corridor', 'reservoir'):
    n += 1
    CAS_SUPP.append(cas(n, 'prairie', 5000, situation=situation))
for ecl in ('L1', 'L2'):
    n += 1
    CAS_SUPP.append(cas(n, 'culture', 5000, eclairage=ecl))
for zone in ('atlantique', 'mediterraneenne', 'alpine'):
    n += 1
    CAS_SUPP.append(cas(n, 'culture', 5000, zone=zone))
for site in ('bois', 'enrobe'):
    for e in (0.45, 0.60):
        n += 1
        CAS_SUPP.append(cas(n, site, 5000, e=e))
