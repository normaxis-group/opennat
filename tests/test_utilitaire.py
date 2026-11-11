# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Tests de l'utilitaire (lot 3) : services HTTP, contrôles en direct, imports, calcul de bout en bout, sécurité."""
import json
import threading
import time
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from opennat.utilitaire import fiche, serveur
from test_calcul import RSEE_FABRIQUE


@pytest.fixture(scope='module')
def url(tmp_path_factory):
    serveur.DOSSIER = str(tmp_path_factory.mktemp('resultats'))
    srv = ThreadingHTTPServer(('127.0.0.1', 0), serveur.Gestionnaire)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f'http://127.0.0.1:{srv.server_address[1]}'
    srv.shutdown()


def appel(url, chemin, corps=None, brut=False):
    data = None if corps is None else (corps if brut else json.dumps(corps).encode())
    req = urllib.request.Request(url + chemin, data=data, method='POST' if data is not None else 'GET')
    with urllib.request.urlopen(req, timeout=120) as r:
        contenu = r.read()
        return json.loads(contenu) if 'json' in r.headers.get('Content-Type', '') else contenu


def test_page_et_referentiel(url):
    assert b'OpenNAT' in appel(url, '/')
    r = appel(url, '/api/referentiel')
    assert len(r['habitats']) == 191 and 'EU1' in r['grilles']
    c = r['grilles']['EU1']['criteres']
    assert any(x['code'] == 'C' and x['essentiel'] and x['libelle'] for x in c)


def test_controles_en_direct(url):
    p = appel(url, '/api/exemple')
    r = appel(url, '/api/valider', p)
    assert not r['erreurs'] and all(f['conforme'] for f in r['fermeture'].values())
    p['etat_initial'][0]['surface'] = 1000
    p['etat_initial'][1]['code'] = 'ZZ.9'
    r = appel(url, '/api/valider', p)
    assert not r['fermeture']['initial']['conforme'] or r['unites']
    assert any('ZZ.9' in x for x in r['unites']['initial'])


def test_imports(url):
    m = appel(url, '/api/materiaux', 'categorie;regime;quantite;remplacements;justification\nbois;coupe_selective;12,5;0;PEFC\n'
                                     'bois;coupe_selective;7,5;0;\ngranulats;;100;1;\nacier;;3;0;\n'.encode(), brut=True)
    assert m['materiaux']['bois'][0]['volume'] == 20 and m['materiaux']['granulats']['masse'] == 100
    assert len(m['erreurs']) == 1
    r = appel(url, '/api/rsee', RSEE_FABRIQUE.encode(), brut=True)
    assert r['zone_climatique'] == 'H1a' and r['batiments'][0]['sref'] == 1400


def test_calcul_de_bout_en_bout(url):
    p = appel(url, '/api/exemple')
    n = appel(url, '/api/calcul', dict(projet=p, tirages=0))['calcul']
    for _ in range(240):
        e = appel(url, f'/api/calcul/{n}')
        if e['etat'] != 'en_cours':
            break
        time.sleep(0.5)
    assert e['etat'] == 'termine', e.get('erreur')
    assert '1:W' in e['etapes'] and '1:E5' in e['etapes']
    r = appel(url, f'/api/resultats/{n}')
    v = r['variantes'][0]
    assert v['indicateurs']['cnat'] == pytest.approx(3217.2, abs=0.1) and len(v['trajectoire']['site']) == 50
    fichiers = [f['chemin'] for f in appel(url, f'/api/fichiers/{n}')]
    assert 'variante_1/08_W_hydrique.json' in fichiers and 'rsnat.xml' in fichiers
    assert b'<RSNat>' in appel(url, f'/api/rsnat/{n}.xml')
    assert appel(url, f'/api/fiche/{n}.docx')[:2] == b'PK'
    if fiche.soffice():
        assert appel(url, f'/api/fiche/{n}.pdf')[:4] == b'%PDF'
    with pytest.raises(urllib.error.HTTPError) as x:
        appel(url, f'/api/fichier/{n}?chemin=../../../../etc/passwd')
    assert x.value.code == 403
