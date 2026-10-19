# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Calcul complet d'un projet : toutes les variantes (fiche A41), incertitude (fiche A39), dossier de résultats,
journal et reprise (fiche A42), RSNat (partie 7).

Dossier de résultats : `resultats/<identifiant>/<horodatage>/`, avec `00_entrees.json`, un sous-dossier par variante
contenant les sorties de chaque étape dans l'ordre du chapitre 6 (`01_E1_contexte.json` à `13_E5_conformite.json`,
`09_T_trajectoires.csv`), `12_E4_tirages.csv`, `journal.txt`, `rsnat.xml`, `rsnat.json` et `empreinte.txt`."""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import time

import numpy as np

from . import VERSION_METHODE, VERSION_MOTEUR
from . import chaine, incertitude, projet, recapitulatif
from .donnees import Parametres, Tables


class CalculInterrompu(RuntimeError):
    """Calcul arrêté à la demande entre deux blocs de tirages ; l'argument est le dossier à reprendre."""


class ErreurReprise(RuntimeError):
    """Reprise refusée : les entrées ou les tables ont changé."""


def _json(x):
    if isinstance(x, dict):
        return {str(k): _json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_json(v) for v in x]
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, (np.floating, np.integer, np.bool_)):
        return x.item()
    return x


def _ecrire_json(chemin, x):
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(_json(x), f, ensure_ascii=False, indent=1)


def empreinte_entrees(e: dict, tables: Tables) -> str:
    h = hashlib.sha256(json.dumps(_json(e), sort_keys=True, ensure_ascii=False).encode())
    h.update(tables.empreinte.encode())
    return h.hexdigest()


UNITE_CLES = {
    '02_E2': ('id', 'code', 'position', 'surface', 'stade', 'grille', 'statut', 'liee', 'tache'),
    '03_S': ('id', 'nature', 'c', 'f_sol'),
    '04_H': ('id', 'v', 'S', 'f', 'classe', 'm', 'VH'),
    '05_C': ('id', 'tache', 'kC'),
    '06_N': ('id', 'kL', 'lumiere', 'k_bruit', 'k_vit', 'kN'),
    '07_E': ('id', 'kE', 'V'),
    '08_W': ('id', 'groupe_hydrique', 'RU', 'bilan', 'kW_niveaux', 'arrosage_m3'),
}


def _ecrire_variante(dossier: str, r: dict):
    os.makedirs(dossier, exist_ok=True)
    et = r['etapes']
    unites = lambda pref: {etat: [{k: u.get(k) for k in UNITE_CLES[pref]} for u in r[etat]]  # noqa: E731
                           for etat in ('initial', 'projet')}
    fichiers = [('01_E1_contexte.json', et['E1']), ('02_E2_pretraitement.json', dict(et['E2'], unites=unites('02_E2'))),
                ('03_S_sol.json', dict(et['S'], unites=unites('03_S'))), ('04_H_habitats.json', dict(unites=unites('04_H'))),
                ('05_C_connectivite.json', dict(et['C'], unites=unites('05_C'))),
                ('06_N_nuisances.json', dict(et['N'], unites=unites('06_N'))),
                ('07_E_eau.json', dict(et['E'], unites=unites('07_E'))), ('08_W_hydrique.json', dict(unites=unites('08_W'))),
                ('09_T_temps.json', dict(et['T'], unites=[dict(id=u['id'], d=u['d'], D=u['D'], forme=u['forme'],
                                                                mois_depart=u['mois_depart'], source_delai=u['source_delai'])
                                                           for u in r['projet']])),
                ('10_G_materiaux.json', et['G']), ('11_E3_agregation.json', et['E3']), ('13_E5_conformite.json', et['E5'])]
    for nom, x in fichiers:
        _ecrire_json(os.path.join(dossier, nom), x)
    with open(os.path.join(dossier, '09_T_trajectoires.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['unite', 'annee', 'valeur_mensuelle_moyenne', 'facteur_hydrique', 'facteur_gestion', 'valeur'])
        for u in r['projet']:
            for t, (b, k, g, x) in enumerate(zip(u['traj_base'], u['kW'], u['f_gestion'], u['traj']), 1):
                w.writerow([u['id'], t, f'{b:.6f}', f'{k:.6f}', f'{g:.6f}', f'{x:.6f}'])
        for t, x in enumerate(et['E3']['integration']['ref'], 1):
            w.writerow(['etat_initial', t, '', '', '', f'{x:.6f}'])


def calculer(chemin_projet: str, sortie: str | None = None, tirages: int | None = None, graine: int | None = None,
             reprendre: str | None = None, dire=print, suivi=None, arret=None) -> dict:
    """Calcul complet. `suivi(variante, étape, avancement)` reçoit la progression ; `arret()` vrai interrompt le
    calcul entre deux blocs de tirages (le dossier reste reprenable)."""
    suivi = suivi or (lambda *a: None)
    t0 = time.time()
    T = Tables()
    P = Parametres(T)
    brut = projet.lire(chemin_projet)
    opt = brut.setdefault('options', {})
    if tirages is not None:
        opt['tirages'] = tirages
    if graine is not None:
        opt['graine'] = graine
    e, journal = projet.normaliser(P, brut)
    emp = empreinte_entrees(e, T)
    if reprendre:
        dossier = reprendre
        with open(os.path.join(dossier, 'empreinte.txt'), encoding='utf-8') as f:
            ancienne = dict(l.strip().split(' : ', 1) for l in f if ' : ' in l)
        if ancienne.get('entrees') != emp:
            raise ErreurReprise('les entrées ou les tables ont changé depuis le calcul interrompu : reprise refusée')
        dire(f'reprise du calcul dans {dossier}')
    else:
        horo = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
        dossier = os.path.join(sortie or 'resultats', e['projet']['identifiant'], horo)
        os.makedirs(dossier, exist_ok=True)
    _ecrire_json(os.path.join(dossier, '00_entrees.json'), e)
    with open(os.path.join(dossier, 'empreinte.txt'), 'w', encoding='utf-8') as f:
        f.write(f'entrees : {emp}\ntables : {T.empreinte}\n')
    resultats = []
    cache = {}
    for v in e['variantes']:
        t = time.time()
        r = chaine.calculer(P, e, v, journal, cache, lambda et, i=v['index']: suivi(i, et, None))
        resultats.append(r)
        _ecrire_variante(os.path.join(dossier, f'variante_{v["index"]}'), r)
        ind = r['etapes']['E3']['indicateurs']
        dire(f'variante {v["index"]} ({v["nom"]}) : étapes E1, E2, S, H, C, N, E, W, T, G, E3, E5 en '
             f'{time.time() - t:.1f} s ; Cnat {ind["cnat"]:.1f}, Inat {ind["inat"]:.1f}, Snat {ind["snat"]:.1f} m²HE·an')
    inc = {}
    if e['options']['tirages'] > 0:
        t = time.time()
        dire(f'E4 incertitude : {e["options"]["tirages"]} tirages, graine {e["options"]["graine"]}')
        def prog(a, b):
            dire(f'  tirages {a} sur {b} ({time.time() - t:.0f} s)')
            suivi(None, 'E4', a / b)
            if arret and arret():
                raise CalculInterrompu(dossier)
        suivi(None, 'E4', 0.0)
        inc = incertitude.analyser(T, e, dossier, prog)
        _ecrire_json(os.path.join(dossier, '12_E4_incertitude.json'), inc)
    suivi(None, 'RSNat', None)
    date = dt.date.today().isoformat()
    emp_rsee = recapitulatif.empreinte_fichier(e['projet']['rsee']) if e['projet'].get('rsee') else None
    d = recapitulatif.construire(e, resultats, inc, T.empreinte, date, emp_rsee)
    err = recapitulatif.ecrire(d, dossier)
    for k, liste in err.items():
        for x in liste:
            journal.append(f'RSNat {k} non conforme à son schéma : {x}')
    with open(os.path.join(dossier, 'empreinte.txt'), 'a', encoding='utf-8') as f:
        f.write(f'rsnat_entrees : {d["Empreinte"]["entrees"]}\nrsnat_sorties : {d["Empreinte"]["sorties"]}\n')
    with open(os.path.join(dossier, 'journal.txt'), 'w', encoding='utf-8') as f:
        f.write(f'{VERSION_METHODE}, moteur {VERSION_MOTEUR}, calcul du {date}\n'
                f'durée : {time.time() - t0:.1f} s\n\n' + '\n'.join(journal) + '\n')
    dire(f'résultats : {dossier}')
    return dict(dossier=dossier, entrees=e, resultats=resultats, incertitude=inc, rsnat=d, erreurs_schema=err,
                journal=journal)
