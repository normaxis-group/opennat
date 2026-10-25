# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Commande `opennat credits` : calcule un fichier crédits et écrit `resultats/<identifiant>/credits-<horodatage>/`
avec `rsnatc.json`, `rsnatc.xml`, `journal.txt` et `empreinte.txt`."""
from __future__ import annotations

import datetime as dt
import os

from . import calcul, rsnatc


def executer(chemin: str, sortie: str | None = None, tirages: int | None = None, graine: int | None = None,
             date: str | None = None, dire=print) -> dict:
    def prog(a, b):
        dire(f'  tirages {a} sur {b}')
    res = calcul.calculer(chemin, tirages, graine, prog)
    date = date or dt.date.today().isoformat()
    d = rsnatc.construire(res, date)
    ident = d['Projet']['Identifiant']
    dossier = os.path.join(sortie or 'resultats', ident, 'credits-' + dt.datetime.now().strftime('%Y%m%d-%H%M%S'))
    err = rsnatc.ecrire(d, dossier)
    with open(os.path.join(dossier, 'journal.txt'), 'w', encoding='utf-8') as f:
        f.write(f'{d["Versions"]["Methode_Credits"]}, {d["Versions"]["Methode"]}, moteur {d["Versions"]["Moteur"]}, '
                f'calcul du {date}\n\n' + '\n'.join(d['Journal']) + '\n')
    with open(os.path.join(dossier, 'empreinte.txt'), 'w', encoding='utf-8') as f:
        f.write(f'entrees : {d["Empreinte"]["Entrees"]}\nsorties : {d["Empreinte"]["Sorties"]}\n')
    p = d['Prevision']
    dire(f'gain prévu {p["Gain"]["Retenu"]:.1f} m²HE·an (valeur retenue), {p["Unites_Previsionnelles"]} unités '
         f'prévisionnelles, plafond {p["Plafond"]} crédits, réserve {d["Risque"]["Taux_Reserve"]:.0%}')
    for v in d['Verifications']:
        dire(f'vérification de l\'année {v["Annee"]} : gain {v["Gain"]["Retenu"]:.1f}, émission {v["Emission"]}, '
             f'cumul {v["Credits_Emis_Cumul"]}, réserve {v["Reserve_Cumul"]}, inversion {v["Inversion"]}')
    if not d['Eligibilite']['Eligible'] or d['Eligibilite']['Motifs']:
        dire('éligibilité : ' + ('oui' if d['Eligibilite']['Eligible'] else 'non') + ' ; ' + ' ; '.join(d['Eligibilite']['Motifs']))
    dire(f'résultats : {dossier}')
    return dict(dossier=dossier, rsnatc=d, erreurs_schema=err, resultat=res)
