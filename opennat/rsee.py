# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Reprise des données du RSEE (fiche A05).

Lit dans le RSEE d'une étude RE2020 la parcelle, les bâtiments (surface de référence, emprise, durée du chantier),
les indicateurs d'ACV des contributeurs « composants » et « chantier » (indicateur 101 et indicateurs de pollution
106 à 109 et 116, par phase), la zone climatique, le département et l'altitude. Seuls les RSEE qui portent la
branche RSEnv fournissent la parcelle, l'emprise et les indicateurs.
"""
from __future__ import annotations

import re

from lxml import etree

INDICATEURS = ('101', '106', '107', '108', '109', '116')
PHASES = ('A1-A3', 'A4-A5', 'B', 'C', 'D')
CONTRIBUTEURS = ('composant', 'chantier')


def _nombre(e, chemin):
    x = e.find(chemin)
    return float(x.text) if x is not None and x.text and x.text.strip() else None


def lire(chemin: str) -> dict:
    with open(chemin, 'rb') as f:
        racine = etree.fromstring(f.read(), etree.XMLParser(huge_tree=True))
    res = dict(batiments=[], parcelle={}, rsenv=False)
    for e in racine.iter('zone_climatique'):
        m = re.search(r'H[123][a-d]?', e.text or '')
        if m:
            res['zone_climatique'] = m.group(0)
        break
    simu = racine.find('.//RSET/Entree_Projet/Simu')
    if simu is not None:
        dep = simu.find('Departement')
        res['departement'] = dep.text.strip() if dep is not None and dep.text else None
        res['altitude'] = _nombre(simu, 'Altitude')
    rsenv = racine.find('.//RSEnv')
    if rsenv is None:
        return res
    res['rsenv'] = True
    p = rsenv.find('entree_projet/parcelle')
    if p is not None:
        for tag, cle in (('surface_parcelle', 'surface'), ('surface_veg', 'surface_vegetalisee_rsee'),
                         ('surface_imper', 'surface_impermeable_rsee'), ('surface_arrosee', 'surface_arrosee_rsee')):
            v = _nombre(p, tag)
            if v is not None and (v > 0 or cle != 'surface'):
                res['parcelle'][cle] = v
    d = rsenv.find('entree_projet/date_etude')
    if d is not None and d.text:
        res['date_etude'] = d.text.strip()
    sorties = {(b.findtext('index') or '').strip(): b for b in rsenv.findall('sortie_projet/batiment')}
    for b in rsenv.findall('entree_projet/batiment'):
        idx = (b.findtext('index') or '').strip()
        sref = _nombre(b, 'sref')
        if sref is None:                                                                   # (A05-3) somme des zones
            sref = sum(_nombre(z, 'sref') or 0.0 for z in b.findall('zone'))
        bat = dict(nom=(b.findtext('nom') or idx).strip(), sref=sref, emprise_au_sol=_nombre(b, 'emprise_au_sol') or 0.0,
                   duree_chantier=_nombre(b, 'duree_chantier') or 0.0, ges={}, pollution={})
        s = sorties.get(idx)
        if s is not None:
            for c in CONTRIBUTEURS:                                                        # (A05-4)
                coll = s.find(f'contributeur/{c}/indicateurs_acv_collection')
                if coll is None:
                    continue
                for ind in coll.findall('indicateur'):
                    ref = ind.get('ref')
                    if ref not in INDICATEURS:
                        continue
                    for v in ind.findall('valeur_phase_acv'):
                        ph = v.get('ref')
                        if ph not in PHASES or not v.text:
                            continue
                        if ref == '101':
                            bat['ges'][ph] = bat['ges'].get(ph, 0.0) + float(v.text)
                        else:
                            bat['pollution'].setdefault(ref, {})
                            bat['pollution'][ref][ph] = bat['pollution'][ref].get(ph, 0.0) + float(v.text)
        res['batiments'].append(bat)
    return res
