# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Récapitulatif standardisé de crédits RSNat-C (chapitre 14 de la méthode OpenNAT Crédits) : construction, écriture
en JSON et en XML, validation contre `schemas/rsnatc.schema.json` et `schemas/rsnatc.xsd`.

La signature électronique du vérificateur se pose sur la plateforme (lot 3) : le bloc `Signature` est livré vide."""
from __future__ import annotations

import hashlib
import json
import os

from lxml import etree

from .. import schema as schema_
from ..donnees import RACINE

SCHEMA_JSON = os.path.join(RACINE, 'schemas', 'rsnatc.schema.json')
SCHEMA_XSD = os.path.join(RACINE, 'schemas', 'rsnatc.xsd')
NOMS_GAIN = (('i_projet', 'I_Projet'), ('i_reference', 'I_Reference'), ('i_obligations', 'I_Obligations'),
             ('gain', 'Gain'))
NOMS_CENTILE = (('centrale', 'Centrale'), ('p5', 'P5'), ('p10', 'P10'), ('p50', 'P50'), ('p90', 'P90'),
                ('retenu', 'Retenu'))


def _r(x, n=4):
    return None if x is None else round(float(x), n)


def _grandeurs(d: dict) -> dict:
    return {nom: {b: _r(d[k][a]) for a, b in NOMS_CENTILE if a in d[k]} for k, nom in NOMS_GAIN}


def construire(res: dict, date: str) -> dict:
    prep, g, em, rq = res['prep'], res['gains'], res['emissions'], res['risque']
    e, c = prep['e'], prep['c']
    nature = 'constate' if prep['releves'] else 'previsionnel'
    d = {
        'Format': 'RSNat-C 1',
        'Nature': nature,
        'Date': date,
        'Versions': {'Methode_Credits': res['versions']['methode_credits'], 'Methode': res['versions']['methode'],
                     'Moteur': res['versions']['moteur'], 'Tables': res['versions']['tables'],
                     'Tables_Credits': res['versions']['tables_credits'], 'Graine': int(res['versions']['graine']),
                     'Tirages': int(res['versions']['tirages'])},
        'Projet': {'Identifiant': c.get('identifiant', e['projet']['identifiant']), 'Nom': e['projet'].get('nom', ''),
                   'Variante_Projet': prep['v_proj']['nom'],
                   'Variante_Obligations': prep['v_obl']['nom'] if prep['v_obl'] else '',
                   'Gain_Exige': _r(prep['gain_exige'] or 0.0), 'Taille_Credit': _r(res['U']),
                   'Certification': prep['certification'],
                   'Calendrier': ' '.join(str(a) for a in prep['calendrier'])},
        'Reference': [{'Unite': i, 'Situation': s['situation'], 'Annees_Abandon': _r(s.get('annees_abandon', 0.0))}
                      for i, s in sorted(prep['situations'].items())],
        'Obligations': [{'Objet': o['objet'], 'Source': o['source'], 'Traduction': o.get('traduction', '')}
                        for o in c.get('obligations', {}).get('liste', [])],
        'Releves': [{'Annee': r['annee'], 'Annee_Periode': r['annee_periode'], 'Date': r['date'] or '',
                     'Ecologue': r['ecologue'] or '', 'Unites_Relevees': r['relevees'],
                     'Unites_Non_Relevees': len(r['non_relevees'])} for r in prep['releves']],
        'Prevision': dict(_grandeurs(g['prevision']), Unites_Previsionnelles=_r(em['unites_previsionnelles'], 2),
                          Plafond=em['plafond']),
        'Verifications': [dict(Rang=i, Annee=r['annee'], Annee_Periode=r['annee_periode'], **_grandeurs(v),
                               Credits_Emis_Cumul=l['credits_emis_cumul'], Emission=l['emission'],
                               Reserve_Cumul=_r(l['reserve_cumul'], 2), Versement_Reserve=_r(l['versement_reserve'], 2),
                               Inversion=l['inversion'])
                          for i, (r, v, l) in enumerate(zip(prep['releves'], g['verifications'], em['verifications']), 1)],
        'Risque': {'Facteurs': [{'Facteur': f['facteur'], 'Niveau': f['niveau']} for f in rq['facteurs']],
                   'Facteur_Hydrique': _r(rq['facteur_hydrique']) if rq['facteur_hydrique'] is not None else -1.0,
                   'Note': _r(rq['note']), 'Taux_Reserve': _r(rq['taux']), 'Eligible': rq['eligible']},
        'Eligibilite': {'Eligible': res['eligibilite']['eligible'], 'Indicatif': res['eligibilite']['indicatif'],
                        'Motifs': list(res['eligibilite']['motifs'])},
        'Journal': list(prep['journal']),
        'Signature': {'Signataire': '', 'Valeur': ''},
    }
    if res['cout']:
        k = res['cout']
        d['Cout'] = {'Restauration': _r(k['postes']['restauration'], 2), 'Validation': _r(k['postes']['validation'], 2),
                     'Gestion': _r(k['postes']['gestion'], 2), 'Releves': _r(k['postes']['releves'], 2),
                     'Verifications': _r(k['postes']['verifications'], 2),
                     'Frais_Registre': _r(k['postes']['frais_registre'], 2), 'Garantie': _r(k['postes']['garantie'], 2),
                     'Total': _r(k['total'], 2), 'Par_Credit': _r(k['par_credit'], 2) if k['par_credit'] else 0.0}
    if g['operation']:
        d['Operation'] = {'Inat': _r(g['operation']['inat']), 'Snat': _r(g['operation']['snat'])}
    sorties = {k: v for k, v in d.items() if k not in ('Date', 'Signature')}
    d['Empreinte'] = {'Entrees': res['empreinte_entrees'],
                      'Sorties': hashlib.sha256(json.dumps(sorties, sort_keys=True, ensure_ascii=False).encode())
                      .hexdigest()}
    return d


# ---------------------------------------------------------------- schémas (une seule spécification pour les deux)

_G = {'Centrale': 'n', 'P5?': 'n', 'P10?': 'n', 'P50?': 'n', 'P90?': 'n', 'Retenu': 'n'}
_GAINS = {'I_Projet': _G, 'I_Reference': _G, 'I_Obligations': _G, 'Gain': _G}
SPEC = {
    'Format': 's', 'Nature': 's', 'Date': 's',
    'Versions': {'Methode_Credits': 's', 'Methode': 's', 'Moteur': 's', 'Tables': 's', 'Tables_Credits': 's',
                 'Graine': 'i', 'Tirages': 'i'},
    'Projet': {'Identifiant': 's', 'Nom': 's', 'Variante_Projet': 's', 'Variante_Obligations': 's', 'Gain_Exige': 'n',
               'Taille_Credit': 'n'},
    'Reference': ['Unite_Reference', {'Unite': 's', 'Situation': 's', 'Annees_Abandon': 'n'}],
    'Obligations': ['Obligation', {'Objet': 's', 'Source': 's', 'Traduction': 's'}],
    'Releves': ['Releve', {'Annee': 'i', 'Annee_Periode': 'i', 'Date': 's', 'Ecologue': 's', 'Unites_Relevees': 'i',
                           'Unites_Non_Relevees': 'i'}],
    'Prevision': dict(_GAINS, Unites_Previsionnelles='n', Plafond='i'),
    'Verifications': ['Verification', dict({'Rang': 'i', 'Annee': 'i', 'Annee_Periode': 'i'}, **_GAINS,
                                           Credits_Emis_Cumul='i', Emission='i', Reserve_Cumul='n',
                                           Versement_Reserve='n', Inversion='i')],
    'Risque': {'Facteurs': ['Facteur_Risque', {'Facteur': 's', 'Niveau': 's'}], 'Facteur_Hydrique': 'n', 'Note': 'n',
               'Taux_Reserve': 'n', 'Eligible': 'b'},
    'Eligibilite': {'Eligible': 'b', 'Indicatif': 'b', 'Motifs': ['Motif', 's']},
    'Journal': ['Ligne', 's'],
    'Signature': {'Signataire': 's', 'Valeur': 's'},
    'Cout?': {'Restauration': 'n', 'Validation': 'n', 'Gestion': 'n', 'Releves': 'n', 'Verifications': 'n',
              'Frais_Registre': 'n', 'Garantie': 'n', 'Total': 'n', 'Par_Credit': 'n'},
    'Operation?': {'Inat': 'n', 'Snat': 'n'},
    'Empreinte': {'Entrees': 's', 'Sorties': 's'},
}
_JT = {'s': {'type': 'string'}, 'n': {'type': 'number'}, 'i': {'type': 'integer'}, 'b': {'type': 'boolean'}}
_XT = {'s': 'xs:string', 'n': 'xs:double', 'i': 'xs:integer', 'b': 'xs:boolean'}


def _json_schema(s):
    if isinstance(s, str):
        return dict(_JT[s])
    if isinstance(s, list):
        return {'type': 'array', 'items': _json_schema(s[1])}
    props = {k.rstrip('?'): _json_schema(v) for k, v in s.items()}
    return {'type': 'object', 'additionalProperties': False, 'properties': props,
            'required': [k for k in s if not k.endswith('?')]}


def _xsd(parent, nom, s, optionnel=False, liste=False):
    el = etree.SubElement(parent, XS + 'element', name=nom)
    if optionnel:
        el.set('minOccurs', '0')
    if liste:
        el.set('minOccurs', '0')
        el.set('maxOccurs', 'unbounded')
    if isinstance(s, str):
        el.set('type', _XT[s])
        return
    ct = etree.SubElement(el, XS + 'complexType')
    seq = etree.SubElement(ct, XS + 'sequence')
    if isinstance(s, list):
        _xsd(seq, s[0], s[1], liste=True)
        return
    for k, v in s.items():
        _xsd(seq, k.rstrip('?'), v, optionnel=k.endswith('?'))


XS = '{http://www.w3.org/2001/XMLSchema}'


def ecrire_schemas():
    sj = dict({'$schema': 'https://json-schema.org/draft/2020-12/schema', 'title': 'RSNat-C 1'}, **_json_schema(SPEC))
    with open(SCHEMA_JSON, 'w', encoding='utf-8') as f:
        json.dump(sj, f, ensure_ascii=False, indent=1)
    racine = etree.Element(XS + 'schema', nsmap={'xs': 'http://www.w3.org/2001/XMLSchema'})
    _xsd(racine, 'RSNatC', SPEC)
    with open(SCHEMA_XSD, 'wb') as f:
        f.write(etree.tostring(racine, xml_declaration=True, encoding='UTF-8', pretty_print=True))


# ---------------------------------------------------------------- XML

LISTES = {'Reference': 'Unite_Reference', 'Obligations': 'Obligation', 'Releves': 'Releve',
          'Verifications': 'Verification', 'Facteurs': 'Facteur_Risque', 'Motifs': 'Motif', 'Journal': 'Ligne'}


def _xml(parent, cle, x):
    if isinstance(x, dict):
        el = etree.SubElement(parent, cle)
        for k, v in x.items():
            _xml(el, k, v)
    elif isinstance(x, list):
        el = etree.SubElement(parent, cle)
        for v in x:
            _xml(el, LISTES[cle], v)
    else:
        el = etree.SubElement(parent, cle)
        el.text = ('true' if x else 'false') if isinstance(x, bool) else str(x)


def vers_xml(d: dict) -> bytes:
    racine = etree.Element('RSNatC')
    for k, v in d.items():
        _xml(racine, k, v)
    return etree.tostring(racine, xml_declaration=True, encoding='UTF-8', pretty_print=True)


def valider(d: dict, xml: bytes) -> dict:
    with open(SCHEMA_JSON, encoding='utf-8') as f:
        ej = schema_.erreurs(d, json.load(f))
    xsd = etree.XMLSchema(etree.parse(SCHEMA_XSD))
    doc = etree.fromstring(xml)
    ex = [] if xsd.validate(doc) else [str(x) for x in xsd.error_log]
    return dict(json=ej, xml=ex)


def ecrire(d: dict, dossier: str) -> dict:
    os.makedirs(dossier, exist_ok=True)
    xml = vers_xml(d)
    with open(os.path.join(dossier, 'rsnatc.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    with open(os.path.join(dossier, 'rsnatc.xml'), 'wb') as f:
        f.write(xml)
    return valider(d, xml)
