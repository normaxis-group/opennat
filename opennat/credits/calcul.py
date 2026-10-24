# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Calcul des crédits OpenNAT : formules (X1) à (X9) de la méthode OpenNAT Crédits 1.

Le gain se calcule tirage par tirage (convention C-X9) : la chaîne d'OpenNAT 1 est jouée, avec les mêmes valeurs
tirées, sur l'état projet prévu, sur la variante d'obligations et sur un état par relevé ; le scénario de référence
se déduit de l'état initial (chapitre 6.1, convention C-X4). Les tirages se font par blocs, comme l'étape E4
(fiche A39) : les tirages d'un paramètre ne dépendent que de la graine et du paramètre."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import os

import numpy as np

from .. import VERSION_METHODE, VERSION_MOTEUR, chaine, projet as projet_
from .. import schema as schema_
from ..donnees import RACINE, Parametres, Tables
from ..temps import facteur_gestion
from . import VERSION_METHODE_CREDITS
from .donnees import TableCredits

SCHEMA = os.path.join(RACINE, 'schemas', 'credits.schema.json')
CENTILES = (5, 10, 50, 90)
FACTEURS_RISQUE = ('maitrise_fonciere', 'financement_gestion', 'gestionnaire', 'secheresse', 'incendie',
                   'inondation_erosion', 'pression_fonciere', 'especes_exotiques', 'frequentation')
CLES_ETAT = ('score', 'criteres', 'notes')


class ErreurCredits(ValueError):
    """Fichier crédits refusé ou incohérent avec le fichier projet."""


# ---------------------------------------------------------------- entrées

def lire(chemin: str) -> dict:
    with open(chemin, encoding='utf-8') as f:
        c = json.load(f)
    with open(SCHEMA, encoding='utf-8') as f:
        err = schema_.erreurs(c, json.load(f))
    if err:
        raise ErreurCredits('Fichier crédits refusé :\n' + '\n'.join(err))
    p = c['projet']
    if not os.path.isabs(p):
        c['projet'] = os.path.join(os.path.dirname(os.path.abspath(chemin)), p)
    return c


def _variante(e: dict, nom: str) -> dict:
    for v in e['variantes']:
        if v['nom'] == nom:
            return v
    raise ErreurCredits(f'variante « {nom} » absente du fichier projet')


def _sans_difficulte(v: dict, TC) -> dict:
    """Convention C-X19 : la difficulté de création ou d'amélioration (C-T7), qui exprime le risque d'échec, est
    neutralisée dans les calculs de crédits, où ce risque est porté par le constat avant émission et la réserve."""
    v = copy.deepcopy(v)
    if TC('credits', 'neutraliser_difficulte'):
        for u in v['unites']:
            u['difficulte_neutralisee'] = True
    return v


def _variante_releve(v_proj: dict, releve: dict, journal: list) -> tuple[dict, list[str]]:
    """État relevé : chaque unité relevée remplace l'unité prévue de même identifiant ; une unité non relevée prend
    un score d'état nul (règle 8.3, toutes ses réponses à « non »)."""
    prevues = {u['id']: u for u in v_proj['unites']}
    rel = {u['id']: u for u in releve['unites']}
    inconnues = set(rel) - set(prevues)
    if inconnues:
        raise ErreurCredits(f'relevé de l\'année {releve["annee"]} : unités inconnues de l\'état projet {sorted(inconnues)}')
    unites, absentes = [], []
    for i, u0 in prevues.items():
        if i in rel:
            u = {k: v for k, v in u0.items() if k not in CLES_ETAT or not any(c in rel[i] for c in CLES_ETAT)}
            u.update(rel[i])
        else:
            u = {k: v for k, v in u0.items() if k not in CLES_ETAT}
            u['criteres'] = {}
            absentes.append(i)
        unites.append(u)
    if absentes:
        journal.append(f'relevé de l\'année {releve["annee"]} : unités non relevées, score nul : {", ".join(absentes)}')
    v = copy.deepcopy(v_proj)
    v['unites'] = unites
    v['nom'] = f'{v_proj["nom"]}, relevé de l\'année {releve["annee"]}'
    return v, absentes


def preparer(chemin: str, tirages: int | None = None, graine: int | None = None) -> dict:
    """Lit le fichier crédits et son fichier projet ; prépare les variantes à calculer."""
    c = lire(chemin)
    T = Tables()
    TC = TableCredits()
    brut = projet_.lire(c['projet'])
    opt = brut.setdefault('options', {})
    oc = c.get('options', {})
    opt['tirages'] = tirages if tirages is not None else oc.get('tirages', int(TC('credits', 'tirages_minimum')))
    if graine is not None or 'graine' in oc:
        opt['graine'] = graine if graine is not None else oc['graine']
    if 'bloc' in oc:
        opt['bloc'] = oc['bloc']
    journal: list[str] = []
    e, j = projet_.normaliser(Parametres(T), brut)
    journal += j
    v_proj = _sans_difficulte(_variante(e, c['variante_projet']), TC)
    ob = c.get('obligations', {})
    if 'variante' in ob and 'gain_exige' in ob:
        raise ErreurCredits('obligations : donner une variante ou un gain exigé, pas les deux (chapitre 6.2)')
    v_obl = _sans_difficulte(_variante(e, ob['variante']), TC) if 'variante' in ob else None
    d_mois = projet_.chantier_variante(e, v_proj, [])['duree_mois']
    decal = math.ceil(d_mois / 12 - 1e-9)
    n = int(TC('credits', 'periode_credit'))
    releves = []
    for rl in sorted(c.get('releves', []), key=lambda x: x['annee']):
        y = decal + rl['annee']
        if y > n:                                     # le dernier relevé du calendrier clôt la période de crédit
            journal.append(f'relevé de l\'année {rl["annee"]} : rapporté à la dernière année de la période ({n})')
            y = n
        v, absentes = _variante_releve(v_proj, rl, journal)
        releves.append(dict(annee=rl['annee'], annee_periode=y, date=rl.get('date'), ecologue=rl.get('ecologue'),
                            variante=v, non_relevees=absentes, relevees=len(rl['unites'])))
    if len({r['annee'] for r in releves}) != len(releves):
        raise ErreurCredits('deux relevés portent la même année')
    ids0 = {u['id'] for u in e['etat_initial']}
    ref = c['scenario_reference']
    inconnues = set(ref.get('unites', {})) - ids0
    if inconnues:
        raise ErreurCredits(f'scénario de référence : unités inconnues de l\'état initial {sorted(inconnues)}')
    situations = {i: dict(ref.get('unites', {}).get(i, {'situation': ref.get('defaut', 'usage_maintenu')}))
                  for i in ids0}
    return dict(c=c, T=T, TC=TC, e=e, journal=journal, v_proj=v_proj, v_obl=v_obl, gain_exige=ob.get('gain_exige'),
                releves=releves, situations=situations, n=n, decal=decal)


# ---------------------------------------------------------------- calcul d'un bloc

def _vec(x, n: int) -> np.ndarray:
    a = np.asarray(x, dtype=float)
    return np.full(n, float(a)) if a.ndim == 0 else a


def _reference(P: Parametres, initial: list[dict], situations: dict, n_tir: int, n: int) -> list[np.ndarray]:
    """Chapitre 6.1 : valeur annuelle du scénario de référence. Usage maintenu, ligneux, minéral : valeur de l'état
    initial sous le même climat (règle de l'état initial, C-M3) ; abandon : succession de la convention C-M2."""
    serie = [np.zeros(n_tir) for _ in range(n)]
    for u in initial:
        s = situations[u['id']]
        for t in range(n):
            x = _vec(u['V'], n_tir) * _vec(u['kW'][t], n_tir)
            if s['situation'] == 'abandon':
                x = x * _vec(facteur_gestion(P, u, 'abandon', s.get('annees_abandon', 0.0) + t), n_tir)
            serie[t] = serie[t] + x
    return serie


def bloc(prep: dict, P: Parametres, n_tir: int, cache: dict) -> dict:
    """Joue les variantes sur un jeu de paramètres (valeurs centrales, ou bloc de tirages) ; renvoie les gains
    cumulés de la validation et de chaque vérification, tirage par tirage."""
    e, n = prep['e'], prep['n']
    j: list[str] = []
    r = chaine.calculer(P, e, prep['v_proj'], j, cache)
    prev = {u['id']: [_vec(x, n_tir) for x in u['traj']] for u in r['projet']}
    faune = _vec(r['etapes']['T']['supplement_destruction'], n_tir)
    ref = _reference(P, r['initial'], prep['situations'], n_tir, n)
    if prep['v_obl'] is not None:
        ro = chaine.calculer(P, e, prep['v_obl'], j, cache)
        obl = [_vec(x, n_tir) for x in ro['etapes']['E3']['integration']['site']]
        faune_obl = _vec(ro['etapes']['T']['supplement_destruction'], n_tir)
    else:
        obl, faune_obl = None, np.zeros(n_tir)
    g_exige = prep['gain_exige'] or 0.0

    def seuil(t):
        """I_ref et I_obl intégrés de l'année 1 à t ; I_seuil = max des deux, tirage par tirage (formule X5)."""
        iref = sum(ref[:t], np.zeros(n_tir))
        if obl is not None:
            iobl = sum(obl[:t], np.zeros(n_tir)) - faune_obl
        else:
            iobl = iref + g_exige * t / n
        return iref, iobl, np.maximum(iref, iobl)

    iprev = sum((sum(s, np.zeros(n_tir)) for s in prev.values()), np.zeros(n_tir)) - faune
    iref, iobl, ise = seuil(n)
    out = dict(prevision=dict(i_projet=iprev, i_reference=iref, i_obligations=iobl, gain=iprev - ise),
               verifications=[], secheresse=None, operation=None)
    traj = [prev]
    delais = {u['id']: (u['code'], u['d']) for u in r['projet']}
    for rl in prep['releves']:
        v = dict(rl['variante'], unites=[dict(u) for u in rl['variante']['unites']])
        for u in v['unites']:                    # règle 8.3 : horloge de maturation de l'état prévu
            code, d = delais[u['id']]
            if u['code'] == code:
                u['delai_impose'] = d
        rr = chaine.calculer(P, e, v, j, cache)
        traj.append({u['id']: [_vec(x, n_tir) for x in u['traj']] for u in rr['projet']})
        bornes = [0] + [x['annee_periode'] for x in prep['releves'][:len(traj) - 1]]
        t = bornes[-1]
        iobs = np.zeros(n_tir)
        for y in range(1, t + 1):                            # règle 8.3 : plus faible des deux états encadrants
            k = next(i for i in range(1, len(bornes)) if bornes[i - 1] < y <= bornes[i])
            for uid in prev:
                iobs = iobs + np.minimum(traj[k - 1][uid][y - 1], traj[k][uid][y - 1])
        iobs = iobs - faune
        iref, iobl, ise = seuil(t)
        out['verifications'].append(dict(i_projet=iobs, i_reference=iref, i_obligations=iobl, gain=iobs - ise))
    if not P.tirage:
        veg = [(u['surface'], float(u['kW_niveaux']['2_7'])) for u in r['projet'] if u.get('groupe_hydrique')]
        s = sum(a for a, _ in veg)
        out['secheresse'] = sum(a * k for a, k in veg) / s if s else None
        if prep['e']['batiments'] or prep['v_proj'].get('batiments'):
            ind = r['etapes']['E3']['indicateurs']
            out['operation'] = dict(inat=float(ind['inat']), snat=float(ind['snat']))
    return out


# ---------------------------------------------------------------- tirages et centiles

def _concat(blocs: list[dict]) -> dict:
    def cat(f):
        return np.concatenate([f(b) for b in blocs])
    res = dict(prevision={k: cat(lambda b, k=k: b['prevision'][k]) for k in blocs[0]['prevision']},
               verifications=[])
    for i in range(len(blocs[0]['verifications'])):
        res['verifications'].append({k: cat(lambda b, k=k, i=i: b['verifications'][i][k])
                                     for k in blocs[0]['verifications'][i]})
    return res


def _resume(central: dict, tir: dict | None, centile: float) -> dict:
    """Valeur centrale, centiles 5, 10, 50, 90 et valeur retenue (centile de la convention C-X9, ou valeur centrale
    sans tirage)."""
    out = {}
    for k, x in central.items():
        d = dict(centrale=float(x[0]))
        if tir is not None:
            p = np.percentile(tir[k], CENTILES)
            d.update({f'p{c}': float(v) for c, v in zip(CENTILES, p)})
            d['retenu'] = float(np.percentile(tir[k], centile))
        else:
            d['retenu'] = d['centrale']
        out[k] = d
    return out


def calculer_gains(prep: dict, progression=None) -> dict:
    """Formules (X1), (X2), (X5), (X6) : gains centraux et tirés."""
    T, e = prep['T'], prep['e']
    cache: dict = {}
    central = bloc(prep, Parametres(T), 1, cache)
    n_total, graine, taille = e['options']['tirages'], e['options']['graine'], e['options']['bloc']
    tir = None
    if n_total > 0:
        blocs = []
        for debut in range(0, n_total, taille):
            fin = min(n_total, debut + taille)
            blocs.append(bloc(prep, Parametres(T, graine, n_total, debut, fin), fin - debut, cache))
            if progression:
                progression(fin, n_total)
        tir = _concat(blocs)
    c = prep['TC']('credits', 'centile_gain')
    return dict(prevision=_resume(central['prevision'], tir and tir['prevision'], c),
                verifications=[_resume(v, tir and tir['verifications'][i], c)
                               for i, v in enumerate(central['verifications'])],
                secheresse=central['secheresse'], operation=central['operation'], tirages=n_total)


# ---------------------------------------------------------------- risque, émissions, coût

def risque(prep: dict, secheresse: float | None) -> dict:
    """Chapitre 11.1 et annexe A : taux de réserve et éligibilité au regard du risque (convention C-X11)."""
    TC = prep['TC']
    dec = dict(prep['c'].get('risque', {}))
    inconnus = set(dec) - set(FACTEURS_RISQUE)
    if inconnus:
        raise ErreurCredits(f'risque : facteurs inconnus {sorted(inconnus)} (annexe A)')
    if secheresse is None:
        niv_s = 'faible'
    elif secheresse >= TC('secheresse', 'facteur_hydrique_faible'):
        niv_s = 'faible'
    elif secheresse >= TC('secheresse', 'facteur_hydrique_moyen'):
        niv_s = 'moyen'
    elif secheresse >= TC('secheresse', 'facteur_hydrique_eleve'):
        niv_s = 'eleve'
    else:
        niv_s = 'redhibitoire'
    dec['secheresse'] = niv_s
    facteurs, notes = [], []
    for f in FACTEURS_RISQUE:
        niv = dec.get(f)
        if niv is None:
            niv = 'eleve'
            notes.append(f'facteur {f} non renseigné : noté élevé')
        facteurs.append(dict(facteur=f, niveau=niv))
    n_eleve = sum(1 for x in facteurs if x['niveau'] == 'eleve')
    redhib = [x['facteur'] for x in facteurs if x['niveau'] == 'redhibitoire']
    note = TC('credits', 'taux_reserve_base') + TC('credits', 'pas_reserve_risque_eleve') * n_eleve
    rmax = TC('credits', 'taux_reserve_maximum')
    eligible = not redhib and note <= rmax + 1e-12
    return dict(facteurs=facteurs, facteur_hydrique=secheresse, note=round(note, 4), taux=round(min(note, rmax), 4),
                eligible=eligible, redhibitoires=redhib, notes=notes)


def _plancher(x: float) -> int:
    return int(math.floor(x + 1e-9))


def emissions(g_prev: float, gains: list[float], r: float, U: float) -> dict:
    """Formules (X3), (X4), (X7), (X8), (X9) et constat des inversions (chapitre 11.3)."""
    up = round(max(g_prev, 0.0) * (1 - r) / U, 2)
    plafond = _plancher(up)
    cap_res = plafond * r / (1 - r)
    emis, res, lignes = 0, 0.0, []
    for g in gains:
        base = _plancher(max(g, 0.0) * (1 - r) / U)
        inversion = max(0, emis - base)
        cumul = max(emis, min(plafond, base))
        c_res = round(min(cap_res, max(g, 0.0) * r / U), 2)
        versement = round(max(0.0, c_res - res), 2)
        lignes.append(dict(gain=g, credits_emis_cumul=cumul, emission=cumul - emis, reserve_cumul=round(max(res, c_res), 2),
                           versement_reserve=versement, inversion=inversion))
        emis, res = cumul, max(res, c_res)
    return dict(unites_previsionnelles=up, plafond=plafond, verifications=lignes)


def cout(prep: dict, plafond: int) -> dict | None:
    """Coût de revient d'un crédit : coût total sur la période de crédit, sans actualisation (convention C-T5),
    divisé par le plafond d'émission."""
    k = prep['c'].get('couts')
    if not k:
        return None
    TC = prep['TC']
    n_rel = len(TC.calendrier())
    postes = dict(restauration=k.get('restauration', 0.0), validation=k.get('validation', 0.0),
                  gestion=k.get('gestion_annuelle', 0.0) * TC('credits', 'periode_credit'),
                  releves=k.get('releve', 0.0) * n_rel, verifications=k.get('verification', 0.0) * n_rel,
                  frais_registre=k.get('frais_registre', 0.0), garantie=k.get('garantie', 0.0))
    total = sum(postes.values())
    return dict(postes=postes, total=total, par_credit=total / plafond if plafond else None, credits=plafond)


# ---------------------------------------------------------------- calcul complet

def _empreinte(x) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()


def calculer(chemin: str, tirages: int | None = None, graine: int | None = None, progression=None) -> dict:
    """Calcul complet d'un fichier crédits : gains, risque, émissions, coût, éligibilité, empreintes."""
    prep = preparer(chemin, tirages, graine)
    TC = prep['TC']
    g = calculer_gains(prep, progression)
    rq = risque(prep, g['secheresse'])
    U = TC('credits', 'taille_credit')
    em = emissions(g['prevision']['gain']['retenu'], [v['gain']['retenu'] for v in g['verifications']],
                   rq['taux'], U)
    motifs = []
    if g['prevision']['gain']['retenu'] <= 0:
        motifs.append('gain prévu au centile retenu nul ou négatif (chapitre 4.1)')
    if not rq['eligible']:
        motifs.append('risque : ' + (f'facteurs rédhibitoires {", ".join(rq["redhibitoires"])}' if rq['redhibitoires']
                                     else f'note {rq["note"]:.2f} au-delà du maximum'))
    indicatif = g['tirages'] < TC('credits', 'tirages_minimum')
    if indicatif:
        motifs.append(f'{g["tirages"]} tirages, moins que le minimum de la convention C-X9 : calcul indicatif')
    ligneux = [i for i, s in prep['situations'].items() if s['situation'] == 'ligneux']
    if ligneux:
        prep['journal'].append('scénario de référence : vieillissement des ligneux non simulé par le moteur '
                               f'(unités {", ".join(sorted(ligneux))}), valeur de l\'état initial maintenue')
    entrees = dict(projet=prep['e'], credits={k: v for k, v in prep['c'].items() if k != 'projet'},
                   tables=prep['T'].empreinte, tables_credits=TC.empreinte)
    return dict(prep=prep, gains=g, risque=rq, emissions=em, cout=cout(prep, em['plafond']), U=U,
                eligibilite=dict(eligible=not motifs or (indicatif and len(motifs) == 1), motifs=motifs,
                                 indicatif=indicatif),
                versions=dict(methode_credits=VERSION_METHODE_CREDITS, methode=VERSION_METHODE, moteur=VERSION_MOTEUR,
                              tables=prep['T'].empreinte, tables_credits=TC.empreinte,
                              graine=prep['e']['options']['graine'], tirages=g['tirages']),
                empreinte_entrees=_empreinte(entrees))
