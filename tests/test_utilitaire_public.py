# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 IRICE
"""Tests du mode public de l'utilitaire (version en ligne, OPENNAT_PUBLIC=1) : identifiants de calcul aléatoires,
chemins du serveur masqués, reprise par chemin refusée, envois bornés, calculs simultanés bornés, en-têtes de
sécurité, purge des résultats, analyseur XML sans résolution d'entités."""
import json
import os
import threading
import time
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from opennat import rsee
from opennat.utilitaire import serveur


@pytest.fixture(scope='module')
def url(tmp_path_factory):
    anciens = serveur.PUBLIC, serveur.DOSSIER
    serveur.PUBLIC = True
    serveur.DOSSIER = str(tmp_path_factory.mktemp('resultats_publics'))
    srv = ThreadingHTTPServer(('127.0.0.1', 0), serveur.Gestionnaire)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f'http://127.0.0.1:{srv.server_address[1]}'
    srv.shutdown()
    serveur.PUBLIC, serveur.DOSSIER = anciens


def requete(url, chemin, corps=None, entetes=None):
    data = None if corps is None else (corps if isinstance(corps, bytes) else json.dumps(corps).encode())
    req = urllib.request.Request(url + chemin, data=data, method='POST' if data is not None else 'GET',
                                 headers=entetes or {})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, dict(r.headers), r.read()


def appel(url, chemin, corps=None, entetes=None):
    return json.loads(requete(url, chemin, corps, entetes)[2])


def statut(url, chemin, corps=None, entetes=None):
    try:
        return requete(url, chemin, corps, entetes)[0]
    except urllib.error.HTTPError as x:
        return x.code


def test_page_et_en_tetes_de_securite(url):
    code, entetes, corps = requete(url, '/')
    assert code == 200
    assert "default-src 'self'" in entetes['Content-Security-Policy']
    assert entetes['X-Frame-Options'] == 'DENY' and entetes['X-Content-Type-Options'] == 'nosniff'
    page = corps.decode('utf-8')
    assert 'Version en ligne' in page and '24 heures' in page
    ref = appel(url, '/api/referentiel')
    assert ref['public'] is True and ref['tirages_max'] == serveur.TIRAGES_MAX


def test_calcul_identifiant_aleatoire_et_chemins_masques(url):
    p = appel(url, '/api/exemple')
    n = appel(url, '/api/calcul', dict(projet=p, tirages=0), {'X-Forwarded-For': '203.0.113.10'})['calcul']
    assert isinstance(n, str) and len(n) >= 16 and not n.isdigit()
    for _ in range(240):
        e = appel(url, f'/api/calcul/{n}')
        if e['etat'] != 'en_cours':
            break
        time.sleep(0.5)
    assert e['etat'] == 'termine', e.get('erreur')
    assert 'dossier' not in e and 'client' not in e
    assert not any(serveur.DOSSIER in m for m in e['messages'])
    r = appel(url, f'/api/resultats/{n}')
    assert 'dossier' not in r and not any(serveur.DOSSIER in x for x in r['journal'])
    assert statut(url, '/api/calcul/1') == 404
    assert statut(url, f'/api/rsnat/{n}.txt') == 404
    assert statut(url, f'/api/fichier/{n}?chemin=../../../../etc/passwd') == 403


def test_reprise_par_chemin_refusee(url):
    p = appel(url, '/api/exemple')
    assert statut(url, '/api/calcul', dict(projet=p, tirages=0, reprendre=serveur.DOSSIER)) == 404


def test_envoi_trop_gros(url, monkeypatch):
    """La taille annoncée suffit au refus : le serveur répond 413 sans lire le corps."""
    import http.client
    monkeypatch.setattr(serveur, 'TAILLE_MAX_ENVOI', 1000)
    hote, port = url.rsplit('/', 1)[1].split(':')
    c = http.client.HTTPConnection(hote, int(port), timeout=30)
    c.putrequest('POST', '/api/rsee')
    c.putheader('Content-Length', '2000')
    c.endheaders()
    assert c.getresponse().status == 413
    c.close()


def test_serveur_occupe(url, monkeypatch):
    monkeypatch.setattr(serveur, 'CALCULS_SIMULTANES', 1)
    serveur._CALCULS['occupe'] = dict(etat='en_cours', debut=time.time(), client='198.51.100.7', dossier=None)
    try:
        p = appel(url, '/api/exemple')
        assert statut(url, '/api/calcul', dict(projet=p, tirages=0)) == 429
    finally:
        serveur._CALCULS.pop('occupe')


def test_purge_des_resultats_anciens(url, monkeypatch):
    d = os.path.join(serveur.DOSSIER, 'ancien_projet', '20260101-000000')
    os.makedirs(d)
    with open(os.path.join(d, 'rsnat.json'), 'w') as f:
        f.write('{}')
    serveur._CALCULS['ancien'] = dict(etat='termine', debut=0, fin=1, dossier=d)
    monkeypatch.setattr(serveur, 'CONSERVATION_HEURES', 0.0001)
    time.sleep(1)
    serveur.purger()
    assert 'ancien' not in serveur._CALCULS and not os.path.exists(d)


def test_analyseur_xml_sans_resolution_d_entites(tmp_path):
    xml = ('<?xml version="1.0"?><!DOCTYPE r [<!ENTITY e "H2b">]>'
           '<RSEE><zone_climatique>&e;</zone_climatique></RSEE>')
    c = tmp_path / 'entite.xml'
    c.write_text(xml, encoding='utf-8')
    assert rsee.lire(str(c)).get('zone_climatique') != 'H2b'
