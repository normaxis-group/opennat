# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Lecture du fichier projet : validation contre `schemas/projet.schema.json`, reprise du RSEE (fiche A05),
valeurs par défaut écrites au journal (fiche A01)."""
from __future__ import annotations

import copy
import json
import os

from . import rsee
from . import schema
from .donnees import RACINE, Parametres

SCHEMA = os.path.join(RACINE, 'schemas', 'projet.schema.json')


class ErreurProjet(ValueError):
    """Fichier projet refusé."""


def charger_schema() -> dict:
    with open(SCHEMA, encoding='utf-8') as f:
        return json.load(f)


def valider(projet: dict) -> list[str]:
    return schema.erreurs(projet, charger_schema())


def lire(chemin: str) -> dict:
    with open(chemin, encoding='utf-8') as f:
        projet = json.load(f)
    base = os.path.dirname(os.path.abspath(chemin))
    r = projet.get('projet', {}).get('rsee')
    if r and not os.path.isabs(r):
        projet['projet']['rsee'] = os.path.join(base, r)
    return projet


def normaliser(P: Parametres, projet: dict) -> tuple[dict, list[str]]:
    """Entrées après reprise du RSEE et valeurs par défaut ; journal des valeurs appliquées."""
    err = valider(projet)
    if err:
        raise ErreurProjet('Fichier projet refusé :\n' + '\n'.join(err))
    e = copy.deepcopy(projet)
    journal = []
    chemin_rsee = e['projet'].get('rsee')
    if chemin_rsee:                                                                         # fiche A05
        r = rsee.lire(chemin_rsee)
        journal.append(f'RSEE repris : {os.path.basename(chemin_rsee)} (branche RSEnv : {"oui" if r["rsenv"] else "non"})')
        for k, v in r['parcelle'].items():
            if k not in e['parcelle']:
                e['parcelle'][k] = v
                journal.append(f'parcelle, {k} = {v:g} (RSEE)')
        if not e.get('batiments') and r['batiments']:
            e['batiments'] = r['batiments']
            journal.append(f'{len(r["batiments"])} bâtiment(s) repris du RSEE (S_ref, emprise, durée de chantier, '
                           f'indicateurs 101, 106 à 109 et 116 des contributeurs composants et chantier)')
        for k in ('zone_climatique', 'departement', 'altitude'):
            if r.get(k) is not None and e['contexte'].get(k) is None:
                e['contexte'][k] = r[k]
                journal.append(f'contexte, {k} = {r[k]} (RSEE)')
    ctx = e['contexte']
    sol = ctx.setdefault('sol', {})
    if 'texture' not in sol:
        sol['texture'] = 'limon'
        journal.append('sol du site : limon (défaut, convention C-W4)')
    if 'profondeur' not in sol:
        sol['profondeur'] = P.central('*', 'profondeur_sol_defaut')
        journal.append(f'profondeur de sol du site : {sol["profondeur"]:g} m (défaut, convention C-W4)')
    ch = e.setdefault('chantier', {})
    if 'annee_debut' not in ch:
        ch['annee_debut'] = int(P.central('*', 'annee_debut_defaut'))
        journal.append(f'année de début du chantier : {ch["annee_debut"]} (défaut, convention C-K3)')
    if 'mois_debut' not in ch:
        ch['mois_debut'] = int(P.central('chantier', 'mois_debut_defaut'))
        journal.append(f'mois de début du chantier : {ch["mois_debut"]} (défaut, convention C-K3)')
    e.setdefault('gestion', {})
    if 'plan_annees' not in e['gestion']:
        e['gestion']['plan_annees'] = 0
        journal.append('aucun plan de gestion écologique déclaré : gestion courante dès la livraison (convention C-M3)')
    e.setdefault('taches', {})
    e.setdefault('batiments', [])
    opt = e.setdefault('options', {})
    opt.setdefault('tirages', int(P.central('incertitude', 'tirages_defaut')))
    opt.setdefault('graine', int(P.central('incertitude', 'graine_defaut')))
    opt.setdefault('bloc', int(P.central('incertitude', 'taille_bloc')))
    if not any(v.get('reference') for v in e['variantes']):
        e['variantes'][0]['reference'] = True
    for i, v in enumerate(e['variantes'], 1):
        v['index'] = i
    return e, journal


def chantier_variante(e: dict, v: dict, journal: list) -> dict:
    """Calendrier du chantier d'une variante : durée déclarée, sinon la plus longue des bâtiments (A05-2)."""
    ch = dict(e['chantier'], **v.get('chantier', {}))
    bats = v.get('batiments', e['batiments'])
    if 'duree_mois' not in ch:
        ch['duree_mois'] = max((b.get('duree_chantier', 0.0) for b in bats), default=0.0)
        journal.append(f'variante {v["index"]} : durée du chantier {ch["duree_mois"]:g} mois (bâtiments, fiche A05-2)')
    ch.setdefault('mois_destruction', ch['mois_debut'])
    return ch
