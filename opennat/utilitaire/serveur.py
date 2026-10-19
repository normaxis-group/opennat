# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 IRICE
"""Utilitaire de calcul OpenNAT : serveur local, sans dépendance hors bibliothèque standard et moteur.

    python -m opennat.utilitaire [--port 8770] [--dossier resultats] [--sans-navigateur]

Le serveur n'écoute que sur la machine (127.0.0.1). Pas de compte : les projets sont des fichiers JSON que
l'utilisateur ouvre et enregistre depuis son navigateur ; les résultats s'écrivent dans le dossier de travail.

Mode public (variable d'environnement OPENNAT_PUBLIC=1, version en ligne) : chaque calcul porte un identifiant
aléatoire et non un numéro, les chemins du serveur ne sortent pas, la taille des envois, le nombre de tirages et le
nombre de calculs simultanés sont bornés, les résultats sont effacés après CONSERVATION_HEURES, les réponses portent
des en-têtes de sécurité, et la page dit ce que deviennent les projets envoyés.

Points d'accès (JSON sauf mention) :
    GET  /                          la page de l'utilitaire
    GET  /api/referentiel           nomenclature, grilles d'état et leurs critères, énumérations, versions
    POST /api/valider               contrôle du fichier projet (schéma, fermeture des surfaces, saisie)
    POST /api/rsee                  corps : un RSEE (XML) ; réponse : les données reprises (fiche A05)
    POST /api/materiaux             corps : un tableur CSV ; réponse : les matériaux d'une variante
    POST /api/calcul                corps : {projet, tirages, reprendre} ; lance le calcul en arrière-plan
    GET  /api/calcul/<n>            avancement du calcul n
    POST /api/calcul/<n>/arret      arrêt entre deux blocs de tirages (le calcul reste reprenable)
    GET  /api/resultats/<n>         résultats pour l'affichage
    GET  /api/fichiers/<n>          fichiers du dossier de résultats ; /api/fichier/<n>?chemin=... : un fichier
    GET  /api/rsnat/<n>.xml|.json   RSNat
    GET  /api/fiche/<n>.docx|.pdf   fiche de synthèse
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import mimetypes
import os
import secrets
import shutil
import tempfile
import threading
import time
import traceback
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from .. import VERSION_METHODE, VERSION_MOTEUR
from .. import calcul as moteur
from .. import pretraitement, projet as mprojet, rsee, schema
from ..donnees import Parametres, Tables
from ..habitats import ErreurSaisie, criteres_de, indicateurs_de
from . import fiche, resume

STATIQUE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'statique')
_TABLES: Tables | None = None
_CALCULS: dict[str, dict] = {}
_VERROU = threading.Lock()
DOSSIER = os.path.abspath('resultats')

PUBLIC = os.environ.get('OPENNAT_PUBLIC') == '1'
TAILLE_MAX_ENVOI = int(os.environ.get('OPENNAT_TAILLE_MAX_MO', '25')) * 1024 * 1024
TIRAGES_MAX = int(os.environ.get('OPENNAT_TIRAGES_MAX', '1000'))
CALCULS_SIMULTANES = int(os.environ.get('OPENNAT_CALCULS_SIMULTANES', '2'))
CONSERVATION_HEURES = float(os.environ.get('OPENNAT_CONSERVATION_HEURES', '24'))
EN_TETES_PUBLICS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Referrer-Policy': 'same-origin',
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
    'Content-Security-Policy': "default-src 'self'; img-src 'self' data: blob:; style-src 'self' 'unsafe-inline'; "
                               "script-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; "
                               "form-action 'self'",
}
MENTION_PUBLIQUE = (
    '<p class="edition">Version en ligne : les projets envoyés sont calculés sur un serveur d\'IRICE, sans compte ni '
    'cookie, et effacés avec leurs résultats au plus tard 24 heures après le calcul. Enregistrez votre fichier projet '
    'et vos résultats sur votre poste. Pour des projets confidentiels, installez l\'outil sur votre poste : '
    '<a href="https://github.com/normaxis-group/opennat" target="_blank" rel="noopener">dépôt OpenNAT</a>. '
    '<a href="https://irice-certification.com/mentions-legales" target="_blank" rel="noopener">Mentions légales</a>.</p>')


class EnvoiTropGros(ValueError):
    """Corps de requête au-delà de TAILLE_MAX_ENVOI."""


class ServeurOccupe(RuntimeError):
    """Trop de calculs en cours (mode public)."""


def tables() -> Tables:
    global _TABLES
    if _TABLES is None:
        _TABLES = Tables()
    return _TABLES


# ------------------------------------------------------------------ services

def referentiel() -> dict:
    T = tables()
    libelles = {}
    for (cle, par), l in T.lignes.items():
        if l.table == 'etat_criteres.csv':
            libelles[(cle, par)] = l
    grilles = {}
    for g in sorted({n['grille_etat'] for n in T.nomenclature.values() if n['grille_etat']}):
        P = Parametres(T)
        crit = [dict(code=c, essentiel=e, libelle=_libelle(T, g, c, e)) for c, e in criteres_de(P, g).items()]
        indic = [dict(code=i, libelle=_libelle_indic(T, g, i)) for i in indicateurs_de(P, g)]
        grilles[g] = dict(criteres=crit, indicateurs=indic)
    with open(mprojet.SCHEMA, encoding='utf-8') as f:
        sch = json.load(f)
    unite = sch['$defs']['unite']['properties']
    enums = {k: v['enum'] for k, v in unite.items() if 'enum' in v}
    enums.update({k: v['enum'] for k, v in sch['properties']['contexte']['properties'].items() if 'enum' in v})
    enums['texture'] = sch['properties']['contexte']['properties']['sol']['properties']['texture']['enum']
    enums['regime'] = sch['$defs']['variante']['properties']['materiaux']['properties']['bois']['items']['properties']['regime']['enum']
    enums['connexion'] = sch['$defs']['tache']['properties']['connexion']['enum']
    enums['cloture'] = sch['$defs']['tache']['properties']['cloture']['enum']
    habitats = [dict(code=c, libelle=n['libelle_fr'], position=n['position'], grille=n['grille_etat'] or None)
                for c, n in T.nomenclature.items()]
    return dict(version_methode=VERSION_METHODE, version_moteur=VERSION_MOTEUR, version_donnees=T.empreinte,
                habitats=habitats, grilles=grilles, enums=enums,
                tirages_defaut=int(T.lignes[('incertitude', 'tirages_defaut')].valeur),
                fiche_pdf=bool(fiche.soffice()), public=PUBLIC, tirages_max=TIRAGES_MAX if PUBLIC else None)


def exemple() -> dict:
    """Projet de l'exemple de l'annexe C de la méthode (banc de validation), avec les options par défaut."""
    from ..donnees import RACINE
    with open(os.path.join(RACINE, 'banc', 'cas', 'exemple_de_l_annexe_c.json'), encoding='utf-8') as f:
        p = json.load(f)
    p['options'] = {'tirages': int(tables().lignes[('incertitude', 'tirages_defaut')].valeur)}
    p['projet'].update(identifiant='exemple-annexe-c', nom='Exemple de l\'annexe C : résidence sur friche urbaine')
    return p


def _libelle(T, g, c, e):
    l = T.lignes.get((g, f'critere_{c}{"_essentiel" if e else ""}'))
    return l and _justif(T, l)


def _libelle_indic(T, g, i):
    l = T.lignes.get((g, f'indicateur_{i}'))
    return l and _justif(T, l)


def _justif(T, l):
    with open(os.path.join(T.dossier, l.table), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['cle'] == l.cle and r['parametre'] == l.parametre:
                return r['justification']
    return ''


def valider(p: dict) -> dict:
    """Contrôles en direct : schéma, saisie de chaque unité, fermeture des surfaces de chaque état (fiche A03)."""
    err = mprojet.valider(p)
    res = dict(erreurs=err, fermeture={}, unites={}, avertissements=[])
    T = tables()
    P = Parametres(T)
    sp = (p.get('parcelle') or {}).get('surface')
    etats = [('initial', p.get('etat_initial') or [])] + \
            [(f'variante {i}', v.get('unites') or []) for i, v in enumerate(p.get('variantes') or [], 1)]
    for nom, unites in etats:
        classees = []
        for u in unites:
            try:
                classees.append(pretraitement.classer(P, u, []))
            except (ErreurSaisie, KeyError, TypeError) as x:
                res['unites'].setdefault(nom, []).append(f'{u.get("id", "?")} : {x}')
        if sp:
            f = pretraitement.fermeture(P, classees, sp)
            res['fermeture'][nom] = f
    ids = {u.get('id') for u in p.get('etat_initial') or []}
    for i, v in enumerate(p.get('variantes') or [], 1):
        for u in v.get('unites') or []:
            if u.get('statut') in ('conservee', 'amelioree') and u.get('liee') not in ids:
                res['avertissements'].append(f'variante {i}, unité {u.get("id")} : unité initiale liée introuvable')
    return res


def lire_rsee(contenu: bytes) -> dict:
    with tempfile.NamedTemporaryFile(suffix='.xml', delete=False) as f:
        f.write(contenu)
        chemin = f.name
    try:
        return rsee.lire(chemin)
    finally:
        os.unlink(chemin)                                   # le RSEE n'est pas conservé


def lire_materiaux(texte: str) -> dict:
    """Tableur des matériaux (CSV, séparateur « ; ») : categorie;regime;quantite;remplacements;justification.

    categorie = bois (quantité en m³, régime forestier) ou granulats (quantité en t). Les lignes de même catégorie et
    de même régime s'additionnent."""
    bois, gran, err = {}, None, []
    lec = csv.DictReader(io.StringIO(texte.lstrip('﻿')), delimiter=';')
    for i, r in enumerate(lec, 2):
        try:
            cat = (r.get('categorie') or '').strip().lower()
            q = float((r.get('quantite') or '0').replace(',', '.'))
            n = int(r.get('remplacements') or 0)
            if cat == 'bois':
                reg = (r.get('regime') or 'coupe_rase').strip() or 'coupe_rase'
                b = bois.setdefault((reg, n), dict(regime=reg, volume=0.0, remplacements=n))
                b['volume'] += q
                if (r.get('justification') or '').strip():
                    b['justification'] = r['justification'].strip()
            elif cat == 'granulats':
                gran = gran or dict(masse=0.0, remplacements=n)
                gran['masse'] += q
            else:
                err.append(f'ligne {i} : catégorie « {cat} » inconnue (bois ou granulats)')
        except ValueError:
            err.append(f'ligne {i} : quantité ou remplacements illisibles')
    m = {}
    if bois:
        m['bois'] = list(bois.values())
    if gran:
        m['granulats'] = gran
    return dict(materiaux=m, erreurs=err)


def lancer(corps: dict, client: str = '') -> str:
    """Lance un calcul et rend son identifiant. « reprendre » : l'identifiant d'un calcul interrompu (hors mode public,
    le chemin de son dossier est aussi accepté)."""
    reprise = corps.get('reprendre')
    if reprise:
        if reprise in _CALCULS:
            reprise = _CALCULS[reprise]['dossier']
        elif PUBLIC:
            raise KeyError(reprise)
    tirages = corps.get('tirages')
    if PUBLIC and tirages is not None:
        tirages = max(0, min(int(tirages), TIRAGES_MAX))
    with _VERROU:
        if PUBLIC:
            en_cours = [e for e in _CALCULS.values() if e['etat'] == 'en_cours']
            if len(en_cours) >= CALCULS_SIMULTANES or any(e.get('client') == client for e in en_cours):
                raise ServeurOccupe("le serveur calcule déjà pour vous ou pour d'autres : réessayez dans quelques "
                                    "minutes, ou installez l'outil sur votre poste (voir le dépôt OpenNAT)")
        n = secrets.token_urlsafe(12)
        etat = dict(etat='en_cours', messages=[], etapes={}, e4=None, debut=time.time(), dossier=None, erreur=None,
                    arret=False, resultat=None, client=client)
        _CALCULS[n] = etat
    p = corps['projet']
    os.makedirs(DOSSIER, exist_ok=True)
    chemin = os.path.join(DOSSIER, f'_projet_calcul_{n}.json')
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False)

    def suivi(variante, et, av):
        if et == 'E4':
            etat['e4'] = av
        etat['etapes'][f'{variante or 0}:{et}'] = time.time()
        etat['courante'] = dict(variante=variante, etape=et)

    def tache():
        try:
            r = moteur.calculer(chemin, DOSSIER, tirages, None, reprise,
                                dire=lambda s: etat['messages'].append(s), suivi=suivi, arret=lambda: etat['arret'])
            etat['dossier'] = r['dossier']
            etat['resultat'] = resume.resumer(r)
            etat['etat'] = 'termine'
        except moteur.CalculInterrompu as x:
            etat['dossier'] = str(x)
            etat['etat'] = 'interrompu'
        except Exception as x:                               # message montré à l'utilisateur
            etat['erreur'] = str(x)
            etat['trace'] = traceback.format_exc(limit=3)
            etat['etat'] = 'erreur'
        finally:
            etat['fin'] = time.time()
            try:
                os.unlink(chemin)
            except OSError:
                pass
    threading.Thread(target=tache, daemon=True).start()
    return n


def _sans_chemins(texte):
    """Mode public : retire des messages le dossier de travail du serveur."""
    if not PUBLIC or not isinstance(texte, str):
        return texte
    return texte.replace(DOSSIER + os.sep, '').replace(DOSSIER, '')


def purger():
    """Mode public : efface les calculs finis depuis plus de CONSERVATION_HEURES, puis les dossiers orphelins."""
    limite = time.time() - CONSERVATION_HEURES * 3600
    racine_ok = os.path.realpath(DOSSIER) + os.sep
    with _VERROU:
        vieux = [n for n, e in _CALCULS.items() if e['etat'] != 'en_cours' and (e.get('fin') or e['debut']) < limite]
        for n in vieux:
            d = _CALCULS.pop(n).get('dossier')
            if d and os.path.isdir(d) and os.path.realpath(d).startswith(racine_ok):
                shutil.rmtree(d, ignore_errors=True)
        gardes = {os.path.realpath(e['dossier']) for e in _CALCULS.values() if e.get('dossier')}
    if not os.path.isdir(DOSSIER):
        return
    for racine, dossiers, fichiers in os.walk(DOSSIER, topdown=False):
        for x in dossiers:
            c = os.path.realpath(os.path.join(racine, x))
            if c in gardes or any(g.startswith(c + os.sep) for g in gardes):
                continue
            if os.path.getmtime(c) < limite:
                shutil.rmtree(c, ignore_errors=True)
        for x in fichiers:
            c = os.path.join(racine, x)
            if os.path.getmtime(c) < limite and os.path.realpath(racine) == os.path.realpath(DOSSIER):
                os.unlink(c)


def _purge_periodique():
    while True:
        time.sleep(600)
        try:
            purger()
        except OSError:
            pass


def _dans(dossier: str, chemin: str) -> str:
    """Chemin sûr à l'intérieur du dossier de résultats."""
    complet = os.path.realpath(os.path.join(dossier, chemin))
    if not complet.startswith(os.path.realpath(dossier) + os.sep):
        raise PermissionError(chemin)
    return complet


# ------------------------------------------------------------------ HTTP

class Gestionnaire(BaseHTTPRequestHandler):
    server_version = f'OpenNAT/{VERSION_MOTEUR}'

    def log_message(self, fmt, *args):
        pass

    def _envoyer(self, code, corps: bytes, mime='application/json; charset=utf-8', nom=None):
        self.send_response(code)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(corps)))
        self.send_header('Cache-Control', 'no-store')
        if PUBLIC:
            for k, v in EN_TETES_PUBLICS.items():
                self.send_header(k, v)
        if nom:
            self.send_header('Content-Disposition', f'attachment; filename="{nom}"')
        self.end_headers()
        self.wfile.write(corps)

    def _json(self, x, code=200):
        self._envoyer(code, json.dumps(x, ensure_ascii=False, default=_serialiser).encode('utf-8'))

    def _corps(self) -> bytes:
        n = int(self.headers.get('Content-Length') or 0)
        if n > TAILLE_MAX_ENVOI:
            raise EnvoiTropGros(f'envoi de plus de {TAILLE_MAX_ENVOI // (1024 * 1024)} Mo')
        return self.rfile.read(n) if n else b''

    def _client(self) -> str:
        """Adresse du visiteur : première adresse transmise par le proxy, sinon celle de la connexion."""
        transmis = (self.headers.get('X-Forwarded-For') or '').split(',')[0].strip()
        return transmis or self.client_address[0]

    def do_GET(self):
        u = urlparse(self.path)
        ch = unquote(u.path)
        try:
            if ch in ('/', '/index.html'):
                return self._page()
            if ch.startswith('/statique/'):
                return self._statique(ch[len('/statique/'):])
            if ch == '/api/referentiel':
                return self._json(referentiel())
            if ch == '/api/exemple':
                return self._json(exemple())
            parts = ch.strip('/').split('/')
            if parts[:2] == ['api', 'calcul'] and len(parts) == 3:
                e = _CALCULS[parts[2]]
                caches = ('resultat', 'trace', 'client') + (('dossier',) if PUBLIC else ())
                vue = {k: v for k, v in e.items() if k not in caches}
                vue['messages'] = [_sans_chemins(m) for m in e['messages']]
                vue['erreur'] = _sans_chemins(e['erreur'])
                return self._json(vue | dict(duree=round((e.get('fin') or time.time()) - e['debut'], 1)))
            if parts[:2] == ['api', 'resultats']:
                r = _CALCULS[parts[2]]['resultat']
                if PUBLIC and r:
                    journal = [_sans_chemins(x) for x in r.get('journal', [])]
                    r = {k: v for k, v in r.items() if k != 'dossier'} | dict(journal=journal)
                return self._json(r)
            if parts[:2] == ['api', 'fichiers']:
                d = _CALCULS[parts[2]]['dossier']
                liste = []
                for racine, dossiers, fichiers in os.walk(d):
                    dossiers[:] = [x for x in dossiers if not x.startswith('.')]
                    for f in sorted(fichiers):
                        c = os.path.relpath(os.path.join(racine, f), d).replace('\\', '/')
                        liste.append(dict(chemin=c, taille=os.path.getsize(os.path.join(racine, f))))
                return self._json(sorted(liste, key=lambda x: x['chemin']))
            if parts[:2] == ['api', 'fichier']:
                d = _CALCULS[parts[2]]['dossier']
                c = _dans(d, parse_qs(u.query)['chemin'][0])
                with open(c, 'rb') as f:
                    return self._envoyer(200, f.read(), 'text/plain; charset=utf-8')
            if parts[:2] == ['api', 'rsnat']:
                n, ext = parts[2].split('.')
                if ext not in ('xml', 'json'):
                    raise KeyError(ext)
                d = _CALCULS[n]['dossier']
                with open(os.path.join(d, f'rsnat.{ext}'), 'rb') as f:
                    mime = 'application/xml' if ext == 'xml' else 'application/json'
                    return self._envoyer(200, f.read(), mime, f'rsnat.{ext}')
            if parts[:2] == ['api', 'fiche']:
                n, ext = parts[2].split('.')
                if ext not in ('docx', 'pdf'):
                    raise KeyError(ext)
                e = _CALCULS[n]
                chemin = fiche.produire(e['resultat'], e['dossier'], ext)
                with open(chemin, 'rb') as f:
                    mime = 'application/pdf' if ext == 'pdf' else \
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                    return self._envoyer(200, f.read(), mime, os.path.basename(chemin))
            self._json(dict(erreur='introuvable'), 404)
        except (KeyError, IndexError, ValueError, FileNotFoundError) as x:
            self._json(dict(erreur=f'introuvable : {x}'), 404)
        except PermissionError:
            self._json(dict(erreur='chemin refusé'), 403)
        except fiche.ErreurFiche as x:
            self._json(dict(erreur=str(x)), 503)

    def do_POST(self):
        ch = urlparse(self.path).path
        try:
            if ch == '/api/valider':
                return self._json(valider(json.loads(self._corps() or b'{}')))
            if ch == '/api/rsee':
                return self._json(lire_rsee(self._corps()))
            if ch == '/api/materiaux':
                return self._json(lire_materiaux(self._corps().decode('utf-8', errors='replace')))
            if ch == '/api/calcul':
                return self._json(dict(calcul=lancer(json.loads(self._corps()), self._client())))
            parts = ch.strip('/').split('/')
            if parts[:2] == ['api', 'calcul'] and parts[-1] == 'arret':
                _CALCULS[parts[2]]['arret'] = True
                return self._json(dict(arret=True))
            self._json(dict(erreur='introuvable'), 404)
        except json.JSONDecodeError as x:
            self._json(dict(erreur=f'JSON illisible : {x}'), 400)
        except EnvoiTropGros as x:
            self._json(dict(erreur=str(x)), 413)
        except ServeurOccupe as x:
            self._json(dict(erreur=str(x)), 429)
        except KeyError as x:
            self._json(dict(erreur=f'introuvable : {x}'), 404)
        except Exception as x:
            self._json(dict(erreur=_sans_chemins(str(x))), 400)

    def _page(self):
        """Page de l'utilitaire. Le logo OpenNAT, quand il est déposé dans statique/opennat.svg, remplace le nom écrit."""
        with open(os.path.join(STATIQUE, 'index.html'), encoding='utf-8') as f:
            html = f.read()
        if PUBLIC:
            html = html.replace('<!--MENTION_PUBLIQUE-->', MENTION_PUBLIQUE)
        if os.path.exists(os.path.join(STATIQUE, 'opennat.svg')):
            html = html.replace('<!--MARQUE_OPENNAT--><span class="nom-opennat">OpenNAT</span>',
                                '<img class="logo-opennat" src="/statique/opennat.svg" alt="OpenNAT">')
        self._envoyer(200, html.encode('utf-8'), 'text/html; charset=utf-8')

    def _statique(self, nom):
        c = _dans(STATIQUE, nom)
        with open(c, 'rb') as f:
            mime = mimetypes.guess_type(c)[0] or 'application/octet-stream'
            if mime.startswith('text/') or mime in ('application/javascript',):
                mime += '; charset=utf-8'
            self._envoyer(200, f.read(), mime)


def _serialiser(x):
    try:
        import numpy as np
        if isinstance(x, np.ndarray):
            return x.tolist()
        if isinstance(x, (np.floating, np.integer, np.bool_)):
            return x.item()
    except ImportError:
        pass
    return str(x)


def main(argv=None):
    global DOSSIER
    ap = argparse.ArgumentParser(prog='opennat.utilitaire', description='Utilitaire de calcul OpenNAT')
    ap.add_argument('--port', type=int, default=8770)
    ap.add_argument('--hote', default=os.environ.get('OPENNAT_HOTE', '127.0.0.1'),
                    help="adresse d'écoute (127.0.0.1 par défaut ; 0.0.0.0 dans un conteneur, publié sur la seule machine)")
    ap.add_argument('--dossier', default='resultats', help='dossier de travail des résultats')
    ap.add_argument('--sans-navigateur', action='store_true')
    a = ap.parse_args(argv)
    DOSSIER = os.path.abspath(a.dossier)
    tables()
    if PUBLIC:
        purger()
        threading.Thread(target=_purge_periodique, daemon=True).start()
    srv = ThreadingHTTPServer((a.hote, a.port), Gestionnaire)
    url = f'http://127.0.0.1:{a.port}/'
    print(f'Utilitaire OpenNAT : {url} (résultats dans {DOSSIER}) ; Ctrl+C pour arrêter', flush=True)
    if not a.sans_navigateur:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
