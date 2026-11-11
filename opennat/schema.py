# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Validation JSON Schema réduite aux mots-clés employés par `schemas/projet.schema.json` et
`schemas/rsnat.schema.json` (type, const, enum, required, properties, additionalProperties, items, minItems,
minLength, minimum, maximum, exclusiveMinimum, oneOf, $ref vers $defs). Évite une dépendance de plus."""
from __future__ import annotations

TYPES = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}


def _type_ok(x, t) -> bool:
    if t == 'number':
        return isinstance(x, (int, float)) and not isinstance(x, bool)
    if t == 'integer':
        return (isinstance(x, int) and not isinstance(x, bool)) or (isinstance(x, float) and x.is_integer())
    return isinstance(x, TYPES[t])


def erreurs(x, schema: dict, racine: dict | None = None, chemin: str = '$') -> list[str]:
    racine = racine or schema
    if '$ref' in schema:
        nom = schema['$ref'].split('/')[-1]
        return erreurs(x, racine['$defs'][nom], racine, chemin)
    err = []
    if 'oneOf' in schema:
        n_ok = sum(1 for s in schema['oneOf'] if not erreurs(x, s, racine, chemin))
        if n_ok != 1:
            err.append(f'{chemin} : ne correspond à aucune des formes admises')
        return err
    if 'const' in schema and x != schema['const']:
        err.append(f'{chemin} : attendu « {schema["const"]} »')
    if 'enum' in schema and x not in schema['enum']:
        err.append(f'{chemin} : « {x} » n\'est pas parmi {schema["enum"]}')
    if 'type' in schema:
        types = schema['type'] if isinstance(schema['type'], list) else [schema['type']]
        if not any(_type_ok(x, t) for t in types):
            return err + [f'{chemin} : type {type(x).__name__}, attendu {" ou ".join(types)}']
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        if 'minimum' in schema and x < schema['minimum']:
            err.append(f'{chemin} : {x} inférieur au minimum {schema["minimum"]}')
        if 'maximum' in schema and x > schema['maximum']:
            err.append(f'{chemin} : {x} supérieur au maximum {schema["maximum"]}')
        if 'exclusiveMinimum' in schema and x <= schema['exclusiveMinimum']:
            err.append(f'{chemin} : {x} doit dépasser {schema["exclusiveMinimum"]}')
    if isinstance(x, str) and 'minLength' in schema and len(x) < schema['minLength']:
        err.append(f'{chemin} : texte vide')
    if isinstance(x, list):
        if 'minItems' in schema and len(x) < schema['minItems']:
            err.append(f'{chemin} : au moins {schema["minItems"]} élément(s)')
        if 'items' in schema:
            for i, y in enumerate(x):
                err += erreurs(y, schema['items'], racine, f'{chemin}[{i}]')
    if isinstance(x, dict):
        for k in schema.get('required', []):
            if k not in x:
                err.append(f'{chemin} : champ obligatoire « {k} » absent')
        props = schema.get('properties', {})
        add = schema.get('additionalProperties', True)
        for k, y in x.items():
            if k in props:
                err += erreurs(y, props[k], racine, f'{chemin}.{k}')
            elif add is False:
                err.append(f'{chemin} : champ « {k} » inconnu')
            elif isinstance(add, dict):
                err += erreurs(y, add, racine, f'{chemin}.{k}')
    return err
