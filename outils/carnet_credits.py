# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Carnet de calcul de référence de la méthode OpenNAT Crédits, aux valeurs centrales.

Comme `outils/carnet_reference.py`, ce carnet n'importe rien du moteur (`opennat/`) : il relit le fichier crédits
et le fichier projet, les convertit au format des cas du carnet, calcule chaque état par `carnet_reference.calculer`,
puis applique lui-même les formules (X1) à (X9) de la méthode OpenNAT Crédits, la règle de saisie 8.3, le scénario de
référence (chapitre 6.1), la grille de risque (annexe A) et la convention C-X19. Le banc compare ses résultats à
ceux du moteur (`banc/credits/comparer.py`).

Usage : python outils/carnet_credits.py fichier.credits.json
"""
import copy
import csv
import json
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import carnet_reference as CR  # noqa: E402
import dynamique as DY  # noqa: E402

RACINE = os.path.dirname(ICI)
with open(os.path.join(RACINE, 'donnees', 'credits', 'credits.csv'), encoding='utf-8') as f:
    TC = {(r['cle'], r['parametre']): float(r['valeur']) for r in csv.DictReader(f, delimiter=';')}
ETAT = ('score', 'criteres', 'notes')
RISQUES = ('maitrise_fonciere', 'financement_gestion', 'gestionnaire', 'secheresse', 'incendie',
           'inondation_erosion', 'pression_fonciere', 'especes_exotiques', 'frequentation')


def unite_cas(u, neutre):
    """Unité du fichier projet vers le format du carnet (inverse de banc/convertir_cas.py)."""
    x = {k: v for k, v in u.items() if k not in ETAT + ('exposition_vitrage', 'niveau_sonore', 'nombre_arbres')}
    if 'score' in u:
        s = u['score']
        x['criteres'] = (s['satisfaits'], s['applicables'], bool(s.get('essentiel_echoue')))
    elif 'criteres' in u and not u['criteres']:
        x['criteres'] = (0, 1, False)                                   # règle 8.3 : unité non relevée, score nul
    if u.get('exposition_vitrage'):
        x['vitrage'] = True
    if 'niveau_sonore' in u:
        x['bruit'] = u['niveau_sonore']
    if neutre:
        x['difficulte_neutralisee'] = True                              # C-X19
    return x


def cas_variante(p, v, neutre=True):
    ctx = p['contexte']
    ch = dict(p.get('chantier', {}), **v.get('chantier', {}))
    cas = dict(nom=p['projet']['nom'], parcelle=p['parcelle']['surface'], emprise=p['parcelle'].get('emprise', 0.0),
               contexte=dict(zone=ctx['zone_biogeographique'], typologie=ctx['typologie'],
                             zone_climatique=ctx['zone_climatique'], altitude=ctx.get('altitude')),
               sol=ctx.get('sol', {}), annee_debut=ch.get('annee_debut', 2027), mois_debut=ch.get('mois_debut', 1),
               duree_chantier_mois=ch.get('duree_mois', 0.0), plan_gestion_annees=p.get('gestion', {}).get('plan_annees', 0),
               taches=p.get('taches', {}), initial=[unite_cas(u, False) for u in p['etat_initial']],
               projet=[unite_cas(u, neutre) for u in v['unites']])
    if 'mois_destruction' in ch:
        cas['mois_destruction'] = ch['mois_destruction']
    if p.get('batiments') or v.get('batiments'):
        raise ValueError('carnet des crédits : bâtiments non pris en charge (opérations de restauration seulement)')
    return cas


def releve(v, rl):
    prevues = {u['id']: u for u in v['unites']}
    rel = {u['id']: u for u in rl['unites']}
    out = []
    for i, u0 in prevues.items():
        if i in rel:
            u = {k: x for k, x in u0.items() if k not in ETAT or not any(c in rel[i] for c in ETAT)}
            u.update(rel[i])
        else:
            u = {k: x for k, x in u0.items() if k not in ETAT}
            u['criteres'] = {}
        out.append(u)
    return dict(v, unites=out)


def calculer(chemin):
    with open(chemin, encoding='utf-8') as f:
        c = json.load(f)
    with open(os.path.join(os.path.dirname(os.path.abspath(chemin)), c['projet']), encoding='utf-8') as f:
        p = json.load(f)
    var = {v['nom']: v for v in p['variantes']}
    vp = var[c['variante_projet']]
    N = int(TC[('credits', 'periode_credit')])
    U = TC[('credits', 'taille_credit')]
    rp = CR.calculer(cas_variante(p, vp))
    # scénario de référence (chapitre 6.1)
    ref_u = c['scenario_reference'].get('unites', {})
    defaut = c['scenario_reference'].get('defaut', 'usage_maintenu')
    v9 = CR.H[('VB.9', 'valeur_intrinseque')]
    ref = [0.0] * N
    for u in rp['initial']:
        s = ref_u.get(u['id'], {'situation': defaut})
        for t in range(N):
            x = u['V'] * u['kW'][t]
            if s['situation'] == 'abandon':
                x *= DY.facteur_gestion(u, 'abandon', s.get('annees_abandon', 0.0) + t, v9)
            ref[t] += x
    ob = c.get('obligations', {})
    if 'variante' in ob:
        ro = CR.calculer(cas_variante(p, var[ob['variante']]))
        obl = ro['site']
        f_obl = ro['faune']
    else:
        obl, f_obl = None, 0.0
    g_ex = ob.get('gain_exige', 0.0)

    def seuil(t):
        iref = sum(ref[:t])
        iobl = sum(obl[:t]) - f_obl if obl is not None else iref + g_ex * t / N
        return iref, iobl, max(iref, iobl)

    prev = {u['id']: u['traj'] for u in rp['projet']}
    d_prev = {u['id']: (u['code'], u['d']) for u in rp['projet']}
    iprev = sum(rp['site']) - rp['faune']
    _, _, s = seuil(N)
    g_prev = iprev - s
    ch = dict(p.get('chantier', {}), **vp.get('chantier', {}))
    decal = math.ceil(ch.get('duree_mois', 0.0) / 12 - 1e-9)
    trajs, bornes, gains = [prev], [0], []
    for rl in sorted(c.get('releves', []), key=lambda x: x['annee']):
        cas_r = cas_variante(p, releve(vp, rl))
        for u in cas_r['projet']:                                       # règle 8.3 : délai de l'état prévu
            u0 = d_prev[u['id']]
            if u['code'] == u0[0]:
                u['delai_impose'] = u0[1]
        rr = CR.calculer(cas_r)
        trajs.append({u['id']: u['traj'] for u in rr['projet']})
        bornes.append(min(N, decal + rl['annee']))
        t = bornes[-1]
        iobs = 0.0
        for y in range(1, t + 1):
            k = next(i for i in range(1, len(bornes)) if bornes[i - 1] < y <= bornes[i])
            iobs += sum(min(trajs[k - 1][i][y - 1], trajs[k][i][y - 1]) for i in prev)
        _, _, s = seuil(t)
        gains.append(iobs - rp['faune'] - s)
    # risque (annexe A)
    veg = [(u['surface'], u['kW_niveaux']['2_7']) for u in rp['projet'] if u['kW_niveaux'].get('2_7') is not None
           and DY.groupe_hydrique(u)]
    a = sum(x for x, _ in veg)
    fh = sum(x * k for x, k in veg) / a if a else None
    niveaux = dict(c.get('risque', {}))
    niveaux['secheresse'] = ('faible' if fh is None or fh >= TC[('secheresse', 'facteur_hydrique_faible')] else
                             'moyen' if fh >= TC[('secheresse', 'facteur_hydrique_moyen')] else
                             'eleve' if fh >= TC[('secheresse', 'facteur_hydrique_eleve')] else 'redhibitoire')
    n_el = sum(1 for k in RISQUES if niveaux.get(k, 'eleve') == 'eleve')
    note = TC[('credits', 'taux_reserve_base')] + TC[('credits', 'pas_reserve_risque_eleve')] * n_el
    r = min(note, TC[('credits', 'taux_reserve_maximum')])
    # émissions (X3), (X4), (X7) à (X9)
    up = round(max(g_prev, 0.0) * (1 - r) / U, 2)
    plafond = math.floor(up + 1e-9)
    emis, res, lignes = 0, 0.0, []
    for g in gains:
        base = math.floor(max(g, 0.0) * (1 - r) / U + 1e-9)
        cumul = max(emis, min(plafond, base))
        c_res = round(min(plafond * r / (1 - r), max(g, 0.0) * r / U), 2)
        lignes.append(dict(gain=g, emis=cumul, emission=cumul - emis, reserve=round(max(res, c_res), 2),
                           inversion=max(0, emis - base)))
        emis, res = cumul, max(res, c_res)
    return dict(g_prev=g_prev, i_prev=iprev, i_ref=sum(ref), facteur_hydrique=fh, taux=r, up=up, plafond=plafond,
                verifications=lignes)


if __name__ == '__main__':
    print(json.dumps(calculer(sys.argv[1]), ensure_ascii=False, indent=1))
