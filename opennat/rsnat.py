# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Récapitulatif standardisé RSNat (partie 7 ; fiches A40 et A42) : construction, schémas XSD et JSON, validation.

Le RSNat se construit d'abord en dictionnaire, dont les clés sont les noms des éléments de `rsnat_spec.py` ; le même
dictionnaire s'écrit en XML (dans l'ordre du schéma) et en JSON. Les deux sorties sont validées contre leurs schémas
(exigence E9)."""
from __future__ import annotations

import hashlib
import json
import os

from lxml import etree

from . import numerique as nm
from .donnees import RACINE as RACINE_DEPOT
from .rsnat_spec import ENUMS, RACINE, E, F

XS = 'http://www.w3.org/2001/XMLSchema'
BASE = {'texte': 'xs:string', 'decimal': 'xs:decimal', 'entier': 'xs:integer', 'booleen': 'xs:boolean', 'date': 'xs:date'}
JSON_TYPES = {'texte': 'string', 'decimal': 'number', 'entier': 'integer', 'booleen': 'boolean', 'date': 'string'}
XSD = os.path.join(RACINE_DEPOT, 'schemas', 'rsnat.xsd')
SCHEMA_JSON = os.path.join(RACINE_DEPOT, 'schemas', 'rsnat.schema.json')
# fiche A01 : une décimale pour les valeurs, quatre pour les facteurs et les ratios
UNE_DECIMALE = ('m²HE', 'm²HE·an', 'm²', 'm³', 'points', 'mm', 'jours-équivalents', 'kg CO2 éq./m² Sref')


class ErreurRSNat(ValueError):
    """RSNat non conforme à son schéma."""


# ------------------------------------------------------------------ schémas

def construire_xsd() -> etree._ElementTree:
    def xs(tag, **att):
        el = etree.Element(f'{{{XS}}}{tag}')
        for k, v in att.items():
            el.set(k, str(v))
        return el

    racine = etree.Element(f'{{{XS}}}schema', nsmap={'xs': XS})
    racine.set('elementFormDefault', 'qualified')
    doc = xs('annotation')
    etree.SubElement(doc, f'{{{XS}}}documentation').text = (
        'Récapitulatif standardisé RSNat (nom provisoire) de la méthode OpenNAT, version 1. NORMATYS, CC BY 4.0. '
        'Généré depuis opennat/rsnat_spec.py.')
    racine.append(doc)
    for nom, valeurs in ENUMS.items():
        st = xs('simpleType', name=nom)
        r = etree.SubElement(st, f'{{{XS}}}restriction', base='xs:string')
        for v in valeurs:
            etree.SubElement(r, f'{{{XS}}}enumeration', value=v)
        racine.append(st)

    def element(noeud):
        att = {'name': noeud.nom}
        if noeud.min != 1:
            att['minOccurs'] = noeud.min
        if noeud.max != 1:
            att['maxOccurs'] = noeud.max
        if isinstance(noeud, E):
            el = xs('element', **att)
            ann = etree.SubElement(el, f'{{{XS}}}annotation')
            etree.SubElement(ann, f'{{{XS}}}documentation').text = noeud.description
            seq = etree.SubElement(etree.SubElement(el, f'{{{XS}}}complexType'), f'{{{XS}}}sequence')
            for enf in noeud.enfants:
                seq.append(element(enf))
            return el
        att['type'] = BASE.get(noeud.type, noeud.type)
        el = xs('element', **att)
        ann = etree.SubElement(el, f'{{{XS}}}annotation')
        etree.SubElement(ann, f'{{{XS}}}documentation').text = noeud.description + (f' ({noeud.unite})' if noeud.unite else '')
        return el

    racine.append(element(RACINE))
    return etree.ElementTree(racine)


def construire_schema_json() -> dict:
    def sch(noeud):
        if isinstance(noeud, E):
            props, req = {}, []
            for enf in noeud.enfants:
                s = sch(enf)
                if enf.max != 1:
                    s = {'type': 'array', 'items': s, **({'minItems': enf.min} if enf.min else {})}
                props[enf.nom] = s
                if enf.min:
                    req.append(enf.nom)
            return {'type': 'object', 'description': noeud.description, 'properties': props, 'required': req,
                    'additionalProperties': False}
        if noeud.type in ENUMS:
            return {'enum': ENUMS[noeud.type], 'description': noeud.description}
        return {'type': JSON_TYPES[noeud.type], 'description': noeud.description + (f' ({noeud.unite})' if noeud.unite else '')}
    s = sch(RACINE)
    return {'$schema': 'https://json-schema.org/draft/2020-12/schema', '$id': 'https://normatys.org/opennat/rsnat.schema.json',
            'title': 'RSNat, récapitulatif standardisé de l\'étude nature OpenNAT', 'type': 'object',
            'properties': {'RSNat': s}, 'required': ['RSNat'], 'additionalProperties': False}


def ecrire_schemas():
    construire_xsd().write(XSD, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    with open(SCHEMA_JSON, 'w', encoding='utf-8') as f:
        json.dump(construire_schema_json(), f, ensure_ascii=False, indent=1)


# ------------------------------------------------------------------ sérialisation

def _texte(noeud: F, v) -> str:
    if noeud.type == 'booleen':
        return 'true' if v else 'false'
    if noeud.type == 'entier':
        return str(int(round(nm.scalaire(v))))
    if noeud.type == 'decimal':
        x = nm.scalaire(v)
        d = 1 if noeud.unite in UNE_DECIMALE else 4
        return f'{round(x, d):.{d}f}'
    return str(v)


def _json(noeud: F, v):
    if noeud.type == 'booleen':
        return bool(v)
    if noeud.type == 'entier':
        return int(round(nm.scalaire(v)))
    if noeud.type == 'decimal':
        x = nm.scalaire(v)
        d = 1 if noeud.unite in UNE_DECIMALE else 4
        return round(x, d)
    return str(v)


def vers_xml(donnees: dict) -> etree._Element:
    def construire(noeud, valeur, parent):
        valeurs = valeur if noeud.max != 1 else [valeur]
        for v in valeurs:
            el = etree.SubElement(parent, noeud.nom) if parent is not None else etree.Element(noeud.nom)
            if isinstance(noeud, E):
                for enf in noeud.enfants:
                    if enf.nom in v and v[enf.nom] is not None:
                        construire(enf, v[enf.nom], el)
                    elif enf.min:
                        raise ErreurRSNat(f'élément obligatoire absent : {noeud.nom}/{enf.nom}')
            else:
                el.text = _texte(noeud, v)
            if parent is None:
                return el
    return construire(RACINE, donnees, None)


def vers_json(donnees: dict) -> dict:
    def conv(noeud, valeur):
        if isinstance(noeud, E):
            def un(v):
                return {enf.nom: conv(enf, v[enf.nom]) for enf in noeud.enfants if v.get(enf.nom) is not None}
            return [un(v) for v in valeur] if noeud.max != 1 else un(valeur)
        return [_json(noeud, v) for v in valeur] if noeud.max != 1 else _json(noeud, valeur)
    return {'RSNat': conv(RACINE, donnees)}


def valider_xml(el: etree._Element) -> list[str]:
    schema = etree.XMLSchema(etree.parse(XSD))
    if schema.validate(etree.ElementTree(el)):
        return []
    return [f'ligne {e.line} : {e.message}' for e in schema.error_log]


def valider_json(doc: dict) -> list[str]:
    from . import schema
    with open(SCHEMA_JSON, encoding='utf-8') as f:
        return schema.erreurs(doc, json.load(f))


def empreinte_element(el) -> str:
    return hashlib.sha256(etree.tostring(el, method='c14n')).hexdigest()
