# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Module H : habitats (fiches A09 à A13 ; A14 à A16 sont appliquées au prétraitement)."""
from __future__ import annotations

from . import numerique as nm
from .donnees import Parametres

REPONSES = ('oui', 'non', 'sans_objet')


class ErreurSaisie(ValueError):
    """Entrée du projet incohérente avec la méthode."""


def valeur_intrinseque(P: Parametres, u: dict):
    """Fiche A09-1 [H1] : valeur du stade pour un type ligneux, valeur du type sinon."""
    st = u.get('stade')
    if st and P.existe(u['code'], f'valeur_intrinseque_stade_{st}'):
        return P(u['code'], f'valeur_intrinseque_stade_{st}')
    return P(u['code'], 'valeur_intrinseque')


def criteres_de(P: Parametres, grille: str) -> dict[str, bool]:
    """Fiche A10 : critères d'une grille et leur caractère essentiel (`etat_criteres.csv`)."""
    res = {}
    for (cle, par), l in P.tables.lignes.items():
        if cle == grille and par.startswith('critere_'):
            code = par[len('critere_'):]
            ess = code.endswith('_essentiel')
            res[code[:-len('_essentiel')] if ess else code] = ess
    return res


def indicateurs_de(P: Parametres, grille: str) -> list[str]:
    """Fiche A11 : indicateurs notés de 1 à 3 d'une grille de boisement."""
    return [par[len('indicateur_'):] for (cle, par) in P.tables.lignes if cle == grille and par.startswith('indicateur_')]


def score(P: Parametres, u: dict, grille: str | None, journal: list) -> float | None:
    """Fiches A10 et A11 : score d'état S_u ; None si le type n'a pas de grille."""
    if not grille:
        return None
    plafond = P('*', 'plafond_score_si_essentiel_echoue')
    if 'score' in u:                                       # résumé de grille : satisfaits, applicables, essentiel
        s = u['score']
        val = s['satisfaits'] / s['applicables'] if s['applicables'] else 0.0
        return nm.mini(val, plafond) if s.get('essentiel_echoue') else val
    indic = indicateurs_de(P, grille)
    if indic:                                              # fiche A11 : grille des boisements, notes de 1 à 3
        notes = u.get('notes', {})
        inconnus = set(notes) - set(indic)
        if inconnus:
            raise ErreurSaisie(f'unité {u["id"]} : indicateurs inconnus de la grille {grille} : {sorted(inconnus)}')
        q_min, q_max = P.central('boisement', 'note_minimale'), P.central('boisement', 'note_maximale')
        n = len(indic)
        q = sum(notes.get(k, q_min) for k in indic)                                           # (A11-1)
        if not notes:
            journal.append(f'unité {u["id"]} : grille {grille} non renseignée, toutes les notes à {q_min:g}')
        return (q - n * q_min) / (n * (q_max - q_min))                                        # (A11-2)
    crit = criteres_de(P, grille)
    rep = u.get('criteres', {})
    inconnus = set(rep) - set(crit)
    if inconnus:
        raise ErreurSaisie(f'unité {u["id"]} : critères inconnus de la grille {grille} : {sorted(inconnus)}')
    for k, x in rep.items():
        if x not in REPONSES:
            raise ErreurSaisie(f'unité {u["id"]} : réponse « {x} » au critère {k} (attendu : oui, non, sans_objet)')
    if not rep:
        journal.append(f'unité {u["id"]} : grille {grille} non renseignée, tous les critères à « non » (fiche A10)')
    applicables = [k for k in crit if rep.get(k, 'non') != 'sans_objet']                      # (A10-1)
    ok = sum(1 for k in applicables if rep.get(k) == 'oui')                                   # (A10-2)
    s = ok / len(applicables) if applicables else 0.0                                         # (A10-3) [H2]
    if any(crit[k] and rep.get(k, 'non') == 'non' for k in applicables):
        s = nm.mini(s, plafond)                                                                # (A10-4)
    return s


def etat(P: Parametres, s) -> tuple:
    """Fiche A12 [H3] : facteur d'état et classe (la classe se lit sur les seuils centraux : elle choisit un délai)."""
    if s is None:
        return 1.0, 'sans état'
    fmin = P('*', 'facteur_etat_minimum')
    f = fmin + (1 - fmin) * s                                                                  # (A12-1)
    sc = nm.scalaire(s)
    cl = ('bon' if sc >= P.central('*', 'seuil_classe_bon') else
          'moyen' if sc >= P.central('*', 'seuil_classe_moyen') else 'mauvais')               # (A12-2)
    return f, cl


def multiplicateur_situation(P: Parametres, situation: str | None):
    """Fiche A02-1 [1]."""
    return P(f'situation_{situation or "hors_trame"}', 'multiplicateur_situation')


def valeur_habitat(u: dict):
    """Fiche A13-1 [H4] : V^H = A x v x f x f_sol x m."""
    return u['surface'] * u['v'] * u['f'] * u['f_sol'] * u['m']
