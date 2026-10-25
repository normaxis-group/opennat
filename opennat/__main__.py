# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Ligne de commande du moteur OpenNAT.

    opennat calcul projet.json [--sortie DOSSIER] [--tirages N] [--graine G] [--reprendre DOSSIER]
    opennat controle                 contrôle les tables de donnees/ et la cohérence dimensionnelle (E12)
    opennat valider projet.json      valide un fichier projet contre son schéma
    opennat schemas                  régénère les schémas du RSNat et du RSNat-C
    opennat credits fichier.json [--sortie DOSSIER] [--tirages N] [--graine G]
                                     calcule les crédits d'un projet (méthode OpenNAT Crédits) et écrit le RSNat-C
    opennat effinature export.json --sortie DOSSIER [--periode-hve N] [--releves fiche.csv]
                                     importe un dossier Effinature 8.1 : fichier projet, fichier crédits, fiche de relevé
"""
from __future__ import annotations

import argparse
import sys

from . import VERSION_METHODE, VERSION_MOTEUR


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog='opennat', description=f'Moteur de calcul {VERSION_METHODE} ({VERSION_MOTEUR})')
    sp = ap.add_subparsers(dest='commande', required=True)
    c = sp.add_parser('calcul', help='calcule un projet et écrit le dossier de résultats et le RSNat')
    c.add_argument('projet')
    c.add_argument('--sortie', help='dossier racine des résultats (défaut : resultats)')
    c.add_argument('--tirages', type=int, help='nombre de tirages de l\'analyse d\'incertitude (0 : aucune)')
    c.add_argument('--graine', type=int, help='graine du générateur')
    c.add_argument('--reprendre', help='dossier d\'un calcul interrompu à reprendre')
    sp.add_parser('controle', help='contrôle les tables de donnees/ et les dimensions des équations')
    v = sp.add_parser('valider', help='valide un fichier projet')
    v.add_argument('projet')
    sp.add_parser('schemas', help='régénère les schémas du RSNat')
    k = sp.add_parser('credits', help='calcule un fichier crédits (méthode OpenNAT Crédits) et écrit le RSNat-C')
    k.add_argument('fichier')
    k.add_argument('--sortie', help='dossier racine des résultats (défaut : resultats)')
    k.add_argument('--tirages', type=int, help='nombre de tirages (défaut : minimum de la convention C-X9)')
    k.add_argument('--graine', type=int, help='graine du générateur')
    m = sp.add_parser('effinature', help='importe un export de dossier Effinature 8.1')
    m.add_argument('export')
    m.add_argument('--sortie', required=True, help='dossier où écrire les fichiers produits')
    m.add_argument('--periode-hve', type=int, help='années entre deux relevés après le premier contrôle HVE')
    m.add_argument('--releves', help='fiche de relevé remplie à reprendre dans le fichier crédits')
    a = ap.parse_args(argv)
    if a.commande == 'effinature':
        from . import effinature
        try:
            effinature.executer(a.export, a.sortie, a.periode_hve or effinature.PERIODE_HVE, a.releves,
                                dire=lambda s: print(s, file=sys.stderr, flush=True))
        except (effinature.ErreurImport, KeyError) as x:
            print(f'import arrêté : {x}', file=sys.stderr)
            return 2
        return 0
    if a.commande == 'credits':
        from .chaine import ErreurCalcul
        from .credits import commande
        from .credits.calcul import ErreurCredits
        from .donnees import ErreurDonnees
        from .projet import ErreurProjet
        try:
            r = commande.executer(a.fichier, a.sortie, a.tirages, a.graine,
                                  dire=lambda s: print(s, file=sys.stderr, flush=True))
        except (ErreurCredits, ErreurDonnees, ErreurProjet, ErreurCalcul) as x:
            print(f'calcul arrêté : {x}', file=sys.stderr)
            return 2
        if any(r['erreurs_schema'].values()):
            print('RSNat-C non conforme à ses schémas : ' + '; '.join(sum(r['erreurs_schema'].values(), [])),
                  file=sys.stderr)
            return 3
        return 0
    if a.commande == 'controle':
        from .donnees import ErreurDonnees, Tables
        try:
            t = Tables()
        except ErreurDonnees as x:
            print(x, file=sys.stderr)
            return 1
        print(f'{len(t.lignes)} valeurs contrôlées dans {len(t.par_table)} tables ; empreinte {t.empreinte}')
        from . import dimensions
        err = dimensions.verifier(t)
        for x in err:
            print(f'dimension : {x}', file=sys.stderr)
        print(f'contrôle dimensionnel : {len(dimensions.CATALOGUE)} unités, {len(dimensions.EQUATIONS)} équations, '
              + (f'{len(err)} incohérences' if err else 'aucune incohérence'))
        return 1 if err else 0
    if a.commande == 'valider':
        from . import projet
        err = projet.valider(projet.lire(a.projet))
        print('\n'.join(err) if err else 'fichier projet valide')
        return 1 if err else 0
    if a.commande == 'schemas':
        from . import rsnat
        from .credits import rsnatc
        rsnat.ecrire_schemas()
        rsnatc.ecrire_schemas()
        print('schemas/rsnat.xsd, schemas/rsnat.schema.json, schemas/rsnatc.xsd et schemas/rsnatc.schema.json régénérés')
        return 0
    from . import calcul
    from .chaine import ErreurCalcul
    from .donnees import ErreurDonnees
    from .projet import ErreurProjet
    try:
        r = calcul.calculer(a.projet, a.sortie, a.tirages, a.graine, a.reprendre,
                            dire=lambda s: print(s, file=sys.stderr, flush=True))
    except (ErreurDonnees, ErreurProjet, ErreurCalcul, calcul.ErreurReprise) as x:
        print(f'calcul arrêté : {x}', file=sys.stderr)
        return 2
    if any(r['erreurs_schema'].values()):
        print('RSNat non conforme à ses schémas, voir le journal', file=sys.stderr)
        return 3
    return 0


if __name__ == '__main__':
    sys.exit(main())
