# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Import d'un projet du BPS (Biodiversity Performance Score, référentiel BPS_BATI) : fichier projet et fichier crédits.

L'entrée est un export « BPS export 1 », produit par l'application du BPS depuis son relevé de surfaces. Ses unités
sont déjà des unités OpenNAT (type d'habitat de la nomenclature, surface, position, épaisseur, arbres, grille d'état) :
la conversion est directe, sans traduction de typologies, ni répartition d'habitats, ni hypothèse.

Le BPS évalue des bâtiments en exploitation. La référence du crédit est l'usage maintenu (chapitre 6.1, convention
C-X4) : la variante « Projet » est l'état réalisé après les améliorations du propriétaire, comparé à l'état initial
maintenu tel quel ; seules les améliorations créditent. Le BPS est une évaluation hors accréditation : le champ
`certification` du fichier crédits le dit (« évalué, hors accréditation »), et le dispositif de la contribution de
maintien ne s'y applique pas (méthode, chapitre 3).
"""
from __future__ import annotations

import re

from ..donnees import Tables
from . import ErreurImport

FORMAT_BPS = 'BPS export 1'

# Champs d'une unité du BPS repris dans le fichier projet (schéma projet, $defs/unite).
CHAMPS_UNITE = ('id', 'code', 'position', 'surface', 'epaisseur', 'nombre_arbres', 'classe_diametre', 'stade',
                'statut', 'liee', 'criteres', 'notes')
STATUTS = ('conservee', 'creee', 'amelioree')
PREFIXE_INITIAL = 'I-'


class ErreurBps(ErreurImport):
    """Export du BPS incomplet ou incohérent."""


def _unite(u: dict, tables: Tables, prefixe: str = '', initiaux: set[str] | None = None, journal: list | None = None) -> dict:
    if u.get('code') not in tables.nomenclature:
        raise ErreurBps(f'unité {u.get("id")} : type d\'habitat inconnu de la nomenclature OpenNAT « {u.get("code")} »')
    d = {k: u[k] for k in CHAMPS_UNITE if u.get(k) not in (None, '', {}, [])}
    d['id'] = prefixe + str(u['id'])
    if d.get('statut') not in STATUTS:
        d.pop('statut', None)
    # Unité conservée ou améliorée : liée à une unité de l'état initial (fiche A41) ; sans elle, comptée créée.
    if initiaux is None:
        d.pop('liee', None)
    elif d.get('statut') in ('conservee', 'amelioree'):
        liee = PREFIXE_INITIAL + str(d.get('liee') or u['id'])
        if liee in initiaux:
            d['liee'] = liee
        else:
            d.pop('liee', None)
            d['statut'] = 'creee'
            if journal is not None:
                journal.append(f'unité {d["id"]} : unité initiale liée introuvable, comptée créée')
    else:
        d.pop('liee', None)
    if 'position' not in d:
        pos = tables.nomenclature[d['code']]['position']
        d['position'] = 'sol_pleine_terre' if pos == 'sol' else pos
    d['surface'] = round(float(d.get('surface', 0)), 2)
    return d


def verifier_calendrier(cal: list[int]) -> list[int]:
    """Convention C-X12 : premier relevé au plus tard à l'année 3, cinq ans au plus entre deux relevés, dernier à 50."""
    if not cal or cal != sorted(set(cal)) or cal[0] > 3 or cal[-1] != 50 or any(b - a > 5 for a, b in zip(cal, cal[1:])):
        raise ErreurBps(f'calendrier {cal} contraire à la convention C-X12')
    return cal


def importer_bps(export: dict) -> dict:
    """Export du BPS → fichier projet, fichier crédits et journal des hypothèses."""
    if export.get('format') != FORMAT_BPS:
        raise ErreurBps(f'format attendu : « {FORMAT_BPS} »')
    journal: list[str] = []
    tables = Tables()
    p = export.get('projet') or {}
    if not p.get('reference'):
        raise ErreurBps('projet : référence BPS absente')
    ident = 'bps_' + re.sub(r'[^A-Za-z0-9]+', '_', str(p['reference'])).strip('_')
    ctx = export.get('contexte') or {}
    for k in ('zone_biogeographique', 'zone_climatique', 'typologie'):
        if not ctx.get(k):
            raise ErreurBps(f'contexte : {k} à renseigner dans l\'export')
    parcelle = export.get('parcelle') or {}
    if not parcelle.get('surface'):
        raise ErreurBps('parcelle : surface absente')

    initial = [_unite(u, tables, PREFIXE_INITIAL) for u in (export.get('etat_initial') or {}).get('unites', [])]
    ids_initiaux = {u['id'] for u in initial}
    prevu = [_unite(u, tables, '', ids_initiaux, journal) for u in (export.get('projet_prevu') or {}).get('unites', [])]
    if not initial:
        raise ErreurBps('état initial absent : le relevé de l\'état initial est la référence du crédit')
    if not prevu:
        raise ErreurBps('état projet absent : ni relevé réalisé ni relevé de conception')
    origine = (export.get('projet_prevu') or {}).get('origine', 'realise')
    journal.append(f'variante Projet : relevé {"réalisé (Livraison)" if origine == "realise" else "de conception"}, '
                   f'{len(prevu)} unités ; état initial : {len(initial)} unités')
    sans_grille = sum(1 for u in prevu if not u.get('criteres') and not u.get('notes')
                      and tables.nomenclature[u['code']].get('grille_etat'))
    if sans_grille:
        journal.append(f'{sans_grille} unité(s) de la variante Projet sans grille d\'état : critères à « non » (fiche A10) '
                       'jusqu\'au premier relevé')

    contexte = {k: ctx[k] for k in ('zone_biogeographique', 'zone_climatique', 'typologie')}
    if p.get('departement'):
        contexte['departement'] = str(p['departement'])
    projet = {
        'format': 'OpenNAT projet 1',
        'projet': {k: v for k, v in dict(identifiant=ident, nom=p.get('nom'), adresse=p.get('adresse'),
                                          commune_insee=p.get('code_insee')).items() if v},
        'contexte': contexte,
        'parcelle': {k: float(v) for k, v in dict(surface=parcelle['surface'], emprise=parcelle.get('emprise')).items()
                     if v is not None},
        'etat_initial': initial,
        'variantes': [dict(nom='Projet', reference=True, unites=prevu)],
        'options': dict(tirages=0),
    }

    ids = {u['id'] for u in prevu}
    releves, annees = [], set()
    for r in sorted(export.get('releves') or [], key=lambda x: x['annee']):
        if r['annee'] in annees:
            raise ErreurBps(f'deux relevés portent l\'année {r["annee"]}')
        annees.add(r['annee'])
        unites = []
        for u in r.get('unites', []):
            if str(u['id']) not in ids:
                journal.append(f'relevé de l\'année {r["annee"]} : unité {u["id"]} absente de l\'état réalisé, ignorée')
                continue
            unites.append(_unite(u, tables, '', ids_initiaux))
        rel = dict(annee=int(r['annee']), unites=unites)
        if r.get('date'):
            rel['date'] = r['date']
        if r.get('releve_par'):
            rel['ecologue'] = r['releve_par'] + (f' ({r["qualite"]})' if r.get('qualite') else '')
        releves.append(rel)
    if releves:
        journal.append(f'{len(releves)} relevé(s) de suivi : années {", ".join(str(r["annee"]) for r in releves)}')

    ev = export.get('evaluation') or {}
    certification = ', '.join(x for x in (
        f'{ev.get("referentiel", "BPS_BATI")} v{ev["version"]}' if ev.get('version') else ev.get('referentiel', 'BPS_BATI'),
        f'phase {ev["phase"]}' if ev.get('phase') else None,
        f'score {ev["score"]} %' if ev.get('score') is not None else None,
        f'classe {ev["classe"]}' if ev.get('classe') else None,
    ) if x) + ' ; évalué, hors accréditation'

    credits = {
        'format': 'OpenNAT crédits 1',
        'identifiant': ident + '_credits',
        'projet': ident + '.projet.json',
        'variante_projet': 'Projet',
        'scenario_reference': dict(defaut='usage_maintenu'),
        'certification': certification,
        'calendrier': verifier_calendrier([int(a) for a in export.get('calendrier') or []]),
        'releves': releves,
        'options': dict(tirages=0),
    }
    journal.append('référence : usage maintenu de l\'état initial pour toutes les unités (bâtiment en exploitation, '
                   'seules les améliorations créditent)')
    if export.get('gain_exige'):
        credits['obligations'] = dict(gain_exige=float(export['gain_exige']))
        journal.append(f'obligation réglementaire déclarée : gain exigé de {export["gain_exige"]} m²HE·an')
    if export.get('risque'):
        credits['risque'] = dict(export['risque'])
    else:
        journal.append('risque non déclaré : chaque facteur sera noté élevé (annexe A)')
    return dict(identifiant=ident, projet=projet, credits=credits, journal=journal)
