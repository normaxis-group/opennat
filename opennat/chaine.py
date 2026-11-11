# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Chaîne de calcul d'une variante, dans l'ordre du chapitre 6 de la partie 1 (exigence E5) :
E1, E2, S, H, C, N, E, W, T, G, E3, E5. L'étape E4 (incertitude) rejoue cette chaîne avec des paramètres tirés.

La même fonction sert au calcul central (paramètres scalaires) et aux tirages (paramètres en tableaux)."""
from __future__ import annotations

from collections import OrderedDict

from . import agregation, climat, connectivite, eau, habitats, hydrique, materiaux, nuisances, pretraitement, sol, temps
from . import conformite as conf
from .donnees import Parametres
from .habitats import ErreurSaisie
from .projet import chantier_variante

ETAPES = (('01', 'E1', 'contexte'), ('02', 'E2', 'pretraitement'), ('03', 'S', 'sol'), ('04', 'H', 'habitats'),
          ('05', 'C', 'connectivite'), ('06', 'N', 'nuisances'), ('07', 'E', 'eau'), ('08', 'W', 'hydrique'),
          ('09', 'T', 'temps'), ('10', 'G', 'materiaux'), ('11', 'E3', 'agregation'), ('13', 'E5', 'conformite'))


class ErreurCalcul(RuntimeError):
    """Calcul arrêté par un contrôle bloquant."""


def _unites_etat(P, unites, journal):
    return [pretraitement.classer(P, u, journal) for u in unites]


def _module_s_h(P, unites, journal):
    for u in unites:
        u['nature'] = sol.nature(P, u)                                                       # A06
        u['c'] = sol.coefficient(P, u['nature'])
        u['f_sol'] = sol.facteur_support(u, u['c']) if u['c'] is not None else 1.0            # A07
        u['v'] = habitats.valeur_intrinseque(P, u)                                           # A09
        u['S'] = habitats.score(P, u, u['grille'], journal)                                  # A10, A11
        u['f'], u['classe'] = habitats.etat(P, u['S'])                                       # A12
        u['m'] = habitats.multiplicateur_situation(P, u.get('situation'))                    # A02-1
        u['VH'] = habitats.valeur_habitat(u)                                                 # A13


def _module_c(P, unites, infos):
    surf = connectivite.taches(unites)                                                       # A17
    kc = connectivite.facteurs(P, surf, infos)                                               # A18, A19
    for u in unites:
        t = u.get('tache')
        u['kC'] = kc[t]['k_C'] if t in kc else 1.0                                           # A19-4
    return kc


def _module_n_e(P, unites, zone):
    for u in unites:
        n = nuisances.nuisances(P, u, zone)                                                  # A20 à A22, A51 à A53
        u.update(kL=n['k_lum'], lumiere=n['lumiere'], k_bruit=n['k_bruit'], k_vit=n['k_vit'], kN=n['k_N'])
        u['kE'] = eau.k_eau(P, u)                                                            # A23
        u['V'] = eau.valeur_maturite(P, u)                                                   # A25


def _module_w(P, unites, ctx, cache):
    for u in unites:
        w = hydrique.facteurs(P, u, ctx['sol'], ctx, cache)                                  # A47 à A50
        u.update(groupe_hydrique=w['groupe'], RU=w['RU'], kW_niveaux=w['kW'], bilan=w['bilan'],
                 arrosage_m3=w['arrosage_m3'])


def calculer(P: Parametres, e: dict, v: dict, journal: list, cache_w: dict | None = None, suivi=None) -> dict:
    """Calcule une variante. Renvoie les sorties de chaque étape et les grandeurs internes. `suivi(étape)` est
    appelé au début de chaque étape (progression de l'utilitaire)."""
    suivi = suivi or (lambda _: None)
    cache_w = {} if cache_w is None else cache_w
    ctx = e['contexte']
    sp = e['parcelle']['surface']
    bats = v.get('batiments', e['batiments'])
    emprise = sum(b.get('emprise_au_sol', 0.0) for b in bats) if bats else v.get('emprise', e['parcelle'].get('emprise', 0.0))
    if emprise > sp:
        raise ErreurCalcul(f'emprise du bâti ({emprise:g} m²) supérieure à la parcelle ({sp:g} m²) (fiche A02)')
    out = OrderedDict()
    # E1
    suivi('E1')
    c1 = conf.contexte(P, e, emprise)
    out['E1'] = dict(c1, zone_biogeographique=ctx['zone_biogeographique'], typologie=ctx['typologie'],
                     zone_climatique=ctx['zone_climatique'], altitude=ctx.get('altitude'), emprise=emprise)
    # E2
    suivi('E2')
    try:
        ini = _unites_etat(P, e['etat_initial'], journal)
        pro = _unites_etat(P, v['unites'], journal)
    except ErreurSaisie as x:
        raise ErreurCalcul(str(x)) from x
    ids = {u['id'] for u in ini}
    for u in pro:
        if u.get('statut') in ('conservee', 'amelioree') and u.get('liee') not in ids:
            raise ErreurCalcul(f'unité {u["id"]} : unité initiale liée « {u.get("liee")} » introuvable (fiche A41)')
    ferm = {'initial': pretraitement.fermeture(P, ini, sp), 'projet': pretraitement.fermeture(P, pro, sp)}
    out['E2'] = dict(fermeture=ferm)
    for k, f in ferm.items():
        if not f['conforme']:
            raise ErreurCalcul(f'fermeture des surfaces de l\'état {k} : somme au sol {f["somme"]:g} m², parcelle '
                               f'{sp:g} m², écart {f["ecart"]:g} m² au-delà de la tolérance {f["tolerance"]:g} m² (fiche A03)')
    # S et H
    suivi('S')
    try:
        _module_s_h(P, ini, journal)
        _module_s_h(P, pro, journal)
    except ErreurSaisie as x:
        raise ErreurCalcul(str(x)) from x
    out['S'] = sol.indicateurs(ini, pro, sp)
    suivi('H')
    pretraitement.coherence_rsee(P, e['parcelle'], pro, journal)
    out['H'] = dict()
    # C
    suivi('C')
    infos = dict(e['taches'], **v.get('taches', {}))
    kc0, kc1 = _module_c(P, ini, infos), _module_c(P, pro, infos)
    out['C'] = dict(taches_initiales=kc0, taches_projet=kc1)
    # N et E
    suivi('N')
    _module_n_e(P, ini, ctx['zone_climatique'])
    _module_n_e(P, pro, ctx['zone_climatique'])
    suivi('E')
    toitures = sum(u['surface'] for u in pro if u['position'] == 'hors_sol_toiture')
    inf = eau.infiltration(v.get('ouvrages_pluviaux', []), out['S']['impermeable_projet'], toitures)
    out['N'] = dict(surface_vitree_non_traitee=nuisances.surface_vitree_non_traitee(v.get('facades_vitrees', [])))
    out['E'] = inf
    # W
    suivi('W')
    _module_w(P, ini, ctx, cache_w)
    _module_w(P, pro, ctx, cache_w)
    out['W'] = dict()
    # T
    suivi('T')
    ch = chantier_variante(e, v, journal)
    n = int(P('*', 'periode_reference'))
    annees = [ch['annee_debut'] + t for t in range(n)]
    plan = v.get('gestion', e['gestion']).get('plan_annees', 0)
    par_id = {u['id']: u for u in ini}
    rang = temps.trajectoires(P, pro, par_id, ch, plan, c1['k_delai'], annees)
    for u in ini:
        u['kW'] = climat.par_annee(P, u['kW_niveaux'], annees)
    faune, faune_det = temps.destruction(P, ini, pro, ch['mois_destruction'])
    out['T'] = dict(chantier=ch, annees=[annees[0], annees[-1]], rang_plantation=rang, plan_gestion_annees=plan,
                    supplement_destruction=faune, destruction=faune_det)
    # G
    suivi('G')
    out['G'] = materiaux.module_g(P, bats, v.get('materiaux', {}), journal)
    # E3
    suivi('E3')
    n30 = int(P('*', 'periode_complementaire'))
    it = agregation.integration(ini, pro, n, n30)
    ind = agregation.indicateurs(it, faune, out['G']['inat'], sp, out['G']['sref'], n)
    bn = agregation.bnat(P, pro, inf['a_inf'], sp)
    arrosage = sum(sum(climat.par_annee(P, u['arrosage_m3'], annees)) for u in pro) / n
    out['E3'] = dict(integration=it, indicateurs=ind, bnat=bn, arrosage_m3_an=arrosage)
    # E5
    suivi('E5')
    out['E5'] = conf.conformite(P, ind, bn, out['S']['pleine_terre'], it['i0'], c1, ctx)
    return dict(etapes=out, initial=ini, projet=pro)
