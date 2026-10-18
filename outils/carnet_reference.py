# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Carnet de calcul de référence de la méthode OpenNAT.

Ce carnet n'est pas le moteur (lot 2). Il applique les fiches algorithmes A02 à A40 de la façon la plus
directe possible, sans Monte-Carlo, pour produire les calculs de référence du banc de validation (lot 4,
§ 7 du cahier des charges) : le moteur devra retrouver ces résultats. Il lit tous ses coefficients dans
donnees/ et imprime chaque grandeur intermédiaire.

Un cas est un dictionnaire : voir outils/edition/cas_validation.py.
"""
import csv
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _table(nom):
    with open(os.path.join(RACINE, 'donnees', nom), encoding='utf-8') as f:
        return {(r['cle'], r['parametre']): float(r['valeur']) for r in csv.DictReader(f, delimiter=';')}


H, SOL, CTX, CON, NUI, EAU, MAT, SEU = (_table(n) for n in (
    'habitats.csv', 'sols.csv', 'contexte.csv', 'connectivite.csv', 'nuisances.csv', 'eau.csv', 'materiaux.csv',
    'seuils.csv'))
with open(os.path.join(RACINE, 'donnees', 'nomenclature_habitats.csv'), encoding='utf-8') as f:
    NOMEN = {r['code_vinat']: r for r in csv.DictReader(f, delimiter=';')}
N = int(CTX[('*', 'periode_reference')])

SANS_GRILLE = {'VB.1', 'VB.2', 'VB.3', 'VB.4', 'VB.10', 'VB.25', 'H5.6', 'I1.1', 'I1.2', 'I1.3', 'I1.4',
               'FB.1', 'FB.2', 'FB.4'}
MINERAUX = {'VB.1', 'VB.2', 'VB.3', 'VB.4'}
BOISE = ('G', 'F', 'FA', 'VB.18', 'VB.9')


def nature(u):                                                     # fiche A06
    h, p, e = u['code'], u['position'], u.get('epaisseur', 0)
    if h in ('VB.1', 'VB.2'):
        return 'S01'
    if h in ('VB.3', 'VB.10', 'VB.25', 'H5.6'):
        return 'S02'
    if h == 'VB.4':
        return 'S03'
    if h in ('VB.21', 'VB.24'):
        return 'S12'
    if p == 'eau':
        return 'S11'
    if h == 'VB.15':
        return 'S09'
    if h == 'VB.16':
        return 'S10'
    if p in ('sol_sur_dalle', 'hors_sol_toiture'):
        return 'S04' if e < 15 else 'S05' if e <= 30 else 'S06' if e < 80 else 'S07'
    if p == 'arbre':
        return None
    return 'S08'


def valeur_intrinseque(u):                                         # fiche A09
    st = u.get('stade')
    if st and (u['code'], f'valeur_intrinseque_stade_{st}') in H:
        return H[(u['code'], f'valeur_intrinseque_stade_{st}')]
    return H[(u['code'], 'valeur_intrinseque')]


def score(u):                                                      # fiches A10 à A12
    if u['code'] in SANS_GRILLE or 'criteres' not in u:
        return None, 1.0, 'sans état'
    ok, n, ess = u['criteres']
    s = ok / n
    if ess:
        s = min(s, 0.5)
    f = 0.5 + 0.5 * s
    cl = 'bon' if s >= 0.85 else 'moyen' if s >= 0.65 else 'mauvais'
    return s, f, cl


def k_taille(a):                                                   # fiche A18
    z, aref, kmin = (CON[('*', 'exposant_aire_especes')], CON[('*', 'surface_reference')],
                     CON[('*', 'facteur_taille_minimum')])
    return min(1.0, max(kmin, (a / aref) ** z))


def evaluer_etat(unites, taches, contexte):
    """Applique les fiches A06 à A25 à un état. Renvoie la liste des unités enrichies."""
    # fiche A17 : toute unité de valeur non nulle relève d'une tache ; sans identifiant, elle forme la sienne
    for u in unites:
        if not u.get('tache') and u['position'] != 'arbre' and nature(u) != 'S01':
            u['tache'] = 'isolee_' + u['id']
    surf_tache = {}
    for u in unites:
        if u.get('tache') and u['position'] != 'arbre' and nature(u) != 'S01':
            surf_tache[u['tache']] = surf_tache.get(u['tache'], 0) + u['surface']
    kc = {}
    for t, a in surf_tache.items():
        info = taches.get(t, {})
        a_eff = a + info.get('exterieur', 0)
        mconn = CON[(f'connexion_{info.get("connexion", "faible")}', 'multiplicateur_connectivite')]
        kclot = CON[('*', 'facteur_cloture_etanche')] if info.get('cloture') == 'etanche' else 1.0
        kc[t] = (a_eff, k_taille(a_eff), mconn, kclot, k_taille(a_eff) * mconn * kclot)
    res = []
    for u in unites:
        n = nature(u)
        c = SOL[(n, 'coefficient_sol')] if n else None
        fsol = c if u['position'] == 'sol_sur_dalle' else 1.0               # fiche A07
        v = valeur_intrinseque(u)
        s, f, cl = score(u)
        m = CTX[(f'situation_{u.get("situation", "hors_trame")}', 'multiplicateur_situation')]
        vh = u['surface'] * v * f * fsol * m                                 # fiche A13
        t = u.get('tache')
        k_c = kc[t][4] if t in kc else 1.0                                  # fiche A19
        klum = NUI[({'L0': 'lumiere_aucune', 'L1': 'lumiere_conforme', 'L2': 'lumiere_non_conforme'}
                    [u.get('eclairage', 'L0')], 'facteur_lumiere')]
        seuil = (NUI[('*', 'seuil_bruit_milieu_boise')] if u['code'].startswith(BOISE)
                 else NUI[('*', 'seuil_bruit_milieu_ouvert')])
        kbr = NUI[('*', 'facteur_bruit_au_dela_seuil')] if u.get('bruit', 0) > seuil else 1.0
        kvit = NUI[('*', 'facteur_vitrage_non_traite')] if u.get('vitrage') else 1.0
        kn = klum * kbr * kvit                                              # fiche A25
        ke = (EAU[('alimentation_artificielle', 'facteur_eau')]
              if u['position'] == 'eau' and u.get('alimentation') == 'artificielle' else 1.0)
        vmax = CTX[('*', 'plafond_valeur_unitaire')] * u['surface']
        V = min(vmax, vh * k_c * kn * ke)
        res.append(dict(u, nature=n, c=c, f_sol=fsol, v=v, S=s, f=f, classe=cl, m=m, VH=vh, kC=k_c,
                        kN=kn, kE=ke, V=V))
    return res, kc


def delai(u, cl, contexte):                                        # fiche A28
    kz = CTX[(f'zone_{contexte["zone"]}', 'multiplicateur_delai')] * contexte.get('k_delai_etude', 1.0)
    for p in (f'delai_maturite_{cl}', 'delai_maturite_sans_etat'):
        if (u['code'], p) in H:
            return kz * H[(u['code'], p)], p
    if cl != 'sans état':
        for alt in ('moyen', 'mauvais'):
            if (u['code'], f'delai_maturite_{alt}') in H:
                return kz * H[(u['code'], f'delai_maturite_{alt}')], f'delai_maturite_{alt}'
    return 0.0, 'aucun délai (C-T3)'


def trajectoires(projet, initial_par_id, d_ch, contexte):
    r_ch = CTX[('*', 'reduction_chantier_sans_protection')]
    d_ind = CTX[('*', 'duree_indisponibilite_renouvellement')]
    for u in projet:
        statut = u.get('statut', 'creee')
        D = H.get((u['code'], 'difficulte_creation' if statut == 'creee' else 'difficulte_amelioration'), 1.0)
        traj = []
        if statut == 'creee':
            d, src = delai(u, u['classe'], contexte)
        elif statut == 'amelioree':
            u0 = initial_par_id[u['liee']]
            trajet = f'{u0["classe"]}_{u["classe"]}'
            d = H.get((u['code'], f'delai_amelioration_{trajet}'), 0.0)
            src = f'delai_amelioration_{trajet}'
        else:
            d, src = 0.0, 'conservée'
        u.update(D=D if statut != 'conservee' else 1.0, d=d, source_delai=src)
        renouv = sorted(u.get('renouvellements', []))
        for t in range(1, N + 1):
            phi = min(1.0, max(0.0, d_ch - (t - 1)))                     # fiche A26
            tau = t - d_ch
            g = 0.0 if tau <= 0 else (1.0 if d == 0 else min(1.0, tau / d))
            r = 0.0 if u.get('protection') else r_ch
            if statut == 'conservee':
                x = u['V'] * (1 - r * phi)                                   # A27
            elif statut == 'amelioree':
                v0 = initial_par_id[u['liee']]['V']
                x = v0 * (1 - r * phi) + max(0.0, D * u['V'] - v0) * g       # A29
            else:
                x = D * u['V'] * g                                           # A28
            for R in renouv:                                                 # A30
                if R <= t < R + d_ind:
                    x = 0.0
                elif t >= R + d_ind:
                    x = D * u['V'] * (1.0 if d == 0 else min(1.0, (t - R - d_ind + 1) / d))
            traj.append(x)
        u['traj'] = traj
    return projet


def materiaux(cas):                                                # fiches A32 à A36
    cf = MAT[('climat', 'facteur_caracterisation')]
    sref = cas.get('sref', 0.0)
    ges = cas.get('ges', {})
    clim = {p: cf * sref * g * MAT[(p, 'annees_persistance')] for p, g in ges.items()}
    occ = 10000 / MAT[('foret', 'production_biologique')] * MAT[('foret', 'rapport_bois_rond_produit')]
    cle = {'plantation': 'foret_plantation', 'coupe_rase': 'foret_coupe_rase',
           'coupe_selective': 'foret_selective', 'faible_impact': 'foret_impact_reduit'}
    bois = sum(q * (1 + n) * occ * (1 - MAT[(cle[r], 'msa_usage')]) for r, q, n in cas.get('bois', []))
    gran = cas.get('granulats', 0.0) * MAT[('carriere', 'occupation_par_tonne')] * (1 - MAT[('carriere', 'msa_usage')])
    return dict(CF=cf, clim=clim, inat_clim=sum(clim.values()), inat_bois=bois, inat_carr=gran,
                inat=sum(clim.values()) + bois + gran, occ_bois=occ)


def bnat(projet, sp, a_inf=0.0):                                   # fiche A38
    num = sum(u['surface'] * u['c'] for u in projet if u['c'] is not None) + SOL[('S13', 'coefficient_sol')] * a_inf
    return 100 * num / sp, num


def seuil_bnat(typologie, e):                                      # fiche A02
    if typologie == 'logement':
        cle = 'logement_emprise_37' if e <= 0.37 else 'logement_emprise_38_49' if e < 0.50 else 'logement_emprise_50'
    elif typologie == 'tertiaire':
        cle = 'tertiaire'
    else:
        return None
    return SEU[(cle, 'bnat_min')]


def calculer(cas):
    ctx = cas['contexte']
    sp = cas['parcelle']
    ferm = {}
    for etat in ('initial', 'projet'):                              # fiche A03
        som = sum(u['surface'] for u in cas[etat] if u['position'] in
                  ('sol_pleine_terre', 'sol_sur_dalle', 'eau', 'lineaire'))
        tol = max(CTX[('*', 'tolerance_fermeture_absolue')], CTX[('*', 'tolerance_fermeture_relative')] * sp)
        ferm[etat] = (som, abs(som - sp), abs(som - sp) <= tol)
    ini, kc0 = evaluer_etat(cas['initial'], cas.get('taches', {}), ctx)
    pro, kc1 = evaluer_etat(cas['projet'], cas.get('taches', {}), ctx)
    par_id = {u['id']: u for u in ini}
    d_ch = cas['duree_chantier_mois'] / 12
    trajectoires(pro, par_id, d_ch, ctx)
    v0 = sum(u['V'] for u in ini)
    site = [sum(u['traj'][t] for u in pro) for t in range(N)]
    i0, i1 = N * v0, sum(site)
    i0_30, i1_30 = 30 * v0, sum(site[:30])
    dm = sum(u['D'] * u['V'] - x for u in pro if u.get('statut', 'creee') in ('creee', 'amelioree')
             for x in u['traj'])
    mat = materiaux(cas)
    b, num = bnat(pro, sp, cas.get('infiltration', 0.0))
    pt = sum(u['surface'] for u in pro if u['nature'] == 'S08') / sp
    pt0 = sum(u['surface'] for u in ini if u['nature'] == 'S08') / sp
    aimp0 = sum(u['surface'] for u in ini if u['nature'] == 'S01')
    aimp1 = sum(u['surface'] for u in pro if u['nature'] == 'S01')
    e = cas.get('emprise', 0.0) / sp
    bmin = seuil_bnat(ctx['typologie'], round(e, 2))
    cnat = i0 - i1
    gain_net = (i0 > 0 and cnat <= -0.10 * i0) or (i0 == 0 and cnat < 0)
    niveau = 2 if gain_net else 1 if cnat <= 0 else 0
    return dict(fermeture=ferm, initial=ini, projet=pro, kc0=kc0, kc1=kc1, v0=v0, site=site, i0=i0, i1=i1,
                i0_30=i0_30, i1_30=i1_30, dm=dm, cnat=cnat, cnat_rel=cnat / i0 if i0 else None,
                cnat_30=i0_30 - i1_30, mat=mat, inat=mat['inat'], snat=-(cnat + mat['inat']), bnat=b,
                bnat_num=num, pt=pt, pt0=pt0, aimp0=aimp0, aimp1=aimp1, e=e, bnat_min=bmin,
                pt_min=SEU[('*', 'pleine_terre_min')], niveau=niveau, d_ch=d_ch)
