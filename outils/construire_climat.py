# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit donnees/climat.csv : stations de référence des zones climatiques, normales mensuelles de pluie
1991-2020 et ETP Penman annuelle de Météo-France (contrôle de l'évapotranspiration calculée).

Sources dans sources/meteo/ (hors dépôt) :
- mensuel/MENSQ_<département>_previous-1950-2024.csv.gz : données climatologiques de base mensuelles de
  Météo-France, Licence Ouverte 2.0 ;
- prospectif_FR_<niveau>.csv : fichiers climatiques prospectifs ADEME, Météo-France, CSTB, DHUP (2025),
  Licence Ouverte 2.0, recopiés sous forme réduite dans donnees/climat/.
"""
import csv
import gzip
import os
import statistics

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RACINE, 'sources', 'meteo', 'mensuel')
COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max', 'source',
            'reference_precise', 'url', 'licence', 'type', 'convention', 'justification']
# zone : (station du fichier prospectif, département, numéro de poste Météo-France, latitude, longitude, altitude)
STATIONS = {
    'H1a': ('TRAPPES', '78', '78621001', 48.7743, 2.0098, 167),
    'H1b': ('NANCY', '54', '54526001', 48.6878, 6.2215, 212),
    'H1c': ('MACON', '71', '71105001', 46.2945, 4.7943, 219),
    'H2a': ('RENNES', '35', '35281001', 48.0688, -1.7640, 36),
    'H2b': ('TOURS', '37', '37179001', 47.4445, 0.7273, 108),
    'H2c': ('AGEN', '47', '47091001', 44.1721, 0.5946, 58),
    'H2d': ('CARPENTRAS', '84', '84031001', 44.0836, 5.2160, 98),
    'H3': ('MARIGNANE', '13', '13054001', 43.4376, 5.2160, 9),
}
URL_MENS = 'https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-mensuelles'
URL_PROSP = 'https://data.ademe.fr/datasets/donnees-climatologiques-prospectives-france-2c'
LO = 'Licence Ouverte 2.0'


def nombre(x):
    return f'{x:.4f}'.rstrip('0').rstrip('.')


def normales(dep, poste):
    rr = {m: [] for m in range(1, 13)}
    etp = {m: [] for m in range(1, 13)}
    with gzip.open(os.path.join(SRC, f'MENSQ_{dep}_previous-1950-2024.csv.gz'), 'rt', encoding='latin-1') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['NUM_POSTE'] != poste:
                continue
            a, m = int(r['AAAAMM'][:4]), int(r['AAAAMM'][4:])
            if not 1991 <= a <= 2020:
                continue
            if r['RR'] and r['QRR'] in ('1', '9'):
                rr[m].append(float(r['RR']))
            if r.get('ETP'):
                etp[m].append(float(r['ETP']))
    return ({m: statistics.mean(v) for m, v in rr.items()}, {m: len(v) for m, v in rr.items()},
            sum(statistics.mean(v) for v in etp.values() if v))


def main():
    lignes = []
    for zone, (nom, dep, poste, lat, lon, alt) in STATIONS.items():
        base = dict(incertitude_min='', incertitude_max='', url=URL_PROSP, licence=LO, type='primaire',
                    convention='C-W1')
        ref = f'note technique Météo-France, ADEME (version 3.0 du 23 mai 2025), tableau des stations de référence'
        for p, v, u in (('latitude', lat, 'degré'), ('longitude', lon, 'degré'), ('altitude', alt, 'm')):
            lignes.append(dict(base, cle=zone, parametre=f'station_{p}', valeur=nombre(v), unite=u,
                               incertitude_min=nombre(v), incertitude_max=nombre(v),
                               source='ADEME, Météo-France, CSTB, DHUP, fichiers climatiques prospectifs (2025)',
                               reference_precise=f'{ref}, station {nom}',
                               justification=f'Station de référence de la zone {zone} ({nom})'))
        rr, n, etp = normales(dep, poste)
        for m in range(1, 13):
            lignes.append(dict(cle=zone, parametre=f'pluie_normale_m{m:02d}', valeur=nombre(round(rr[m], 1)),
                               unite='mm/mois', incertitude_min=nombre(round(rr[m] * 0.5, 1)),
                               incertitude_max=nombre(round(rr[m] * 1.5, 1)),
                               source='Météo-France, données climatologiques de base mensuelles',
                               reference_precise=f'fichier MENSQ_{dep}, poste {poste}, champ RR, moyenne 1991-2020 '
                                                 f'({n[m]} années valides)',
                               url=URL_MENS, licence=LO, type='primaire', convention='C-W3',
                               justification='Normale mensuelle de pluie de la station de référence, sur laquelle '
                                             'les pluies horaires des années types sont recalées'))
        lignes.append(dict(cle=zone, parametre='etp_penman_normale', valeur=nombre(round(etp)), unite='mm/an',
                           incertitude_min=nombre(round(etp * 0.9)), incertitude_max=nombre(round(etp * 1.1)),
                           source='Météo-France, données climatologiques de base mensuelles',
                           reference_precise=f'fichier MENSQ_{dep}, poste {poste}, champ ETP, somme des moyennes '
                                             f'mensuelles 1991-2020',
                           url=URL_MENS, licence=LO, type='primaire', convention='C-W2',
                           justification="Contrôle de l'évapotranspiration de référence calculée (fiche A44), "
                                         "sans entrer dans le calcul"))
    with open(os.path.join(RACINE, 'donnees', 'climat.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    print(len(lignes), 'lignes')


if __name__ == '__main__':
    main()
