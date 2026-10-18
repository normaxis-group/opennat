# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 5 bis : exemples chiffrés des fiches d'application, calculés par le carnet de référence.

Chaque exemple compare deux à quatre variantes d'une même situation, qui ne diffèrent que par le point traité
par la fiche, pour montrer son effet sur les indicateurs.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import carnet_reference as C  # noqa: E402
from cas_validation import U  # noqa: E402
from commun import ecrire, nombre, tableau  # noqa: E402

PT = 'sol_pleine_terre'


def base(nom, initial, projet, parcelle=2000, emprise=600, mois=12, typo='logement', taches=None, **k):
    d = dict(nom=nom, parcelle=parcelle, emprise=emprise, duree_chantier_mois=mois,
             contexte=dict(zone='continentale', typologie=typo), taches=taches or {}, initial=initial,
             projet=projet, ges=k.pop('ges', {}), bois=k.pop('bois', []), granulats=k.pop('granulats', 0),
             sref=k.pop('sref', 0))
    d.update(k)
    return d


def prairie(id_, surf, ok=4, tache='T', **k):
    return U(id_, 'VB.26', PT, surf, tache=tache, criteres=(ok, 6, False), **k)


EXEMPLES = []


def ex(fiche, titre, texte, variantes):
    EXEMPLES.append((fiche, titre, texte, variantes))


# F01 réhabilitation : cour désimperméabilisée ou non
ini = [U('I1', 'VB.1', PT, 600), U('I2', 'VB.2', PT, 1400)]
ex('F01', 'Réhabilitation : cour laissée en enrobé ou désimperméabilisée',
   'Un immeuble de 600 m² d\'emprise sur une parcelle de 2 000 m² entièrement revêtue est réhabilité. Variante A : '
   'la cour reste en enrobé. Variante B : 900 m² de cour deviennent jardin commun et prairie.',
   [base('A', ini, [U('P1', 'VB.1', PT, 600, statut='conservee', liee='I1'), U('P2', 'VB.2', PT, 1400)]),
    base('B', ini, [U('P1', 'VB.1', PT, 600, statut='conservee', liee='I1'), U('P2', 'VB.2', PT, 500),
                    U('P3', 'VB.7', PT, 500, tache='T', criteres=(2, 3, False)), prairie('P4', 400)])])

# F02 extension
ini = [U('I1', 'VB.1', PT, 400), U('I2', 'E2.2', PT, 1600, tache='T', criteres=(4, 6, False))]
ex('F02', 'Extension sur une prairie de fauche',
   'Une maison de 400 m² d\'emprise sur une parcelle de 2 000 m² de prairie de fauche s\'agrandit de 200 m². '
   'Variante A : extension au sol. Variante B : surélévation, sans emprise nouvelle, avec toiture extensive.',
   [base('A', ini, [U('P1', 'VB.1', PT, 400, statut='conservee', liee='I1'), U('P2', 'VB.1', PT, 200),
                    U('P3', 'E2.2', PT, 1400, tache='T', criteres=(4, 6, False), statut='conservee', liee='I2')],
         emprise=600),
    base('B', ini, [U('P1', 'VB.1', PT, 400, statut='conservee', liee='I1'),
                    U('P3', 'E2.2', PT, 1600, tache='T', criteres=(4, 6, False), statut='conservee', liee='I2',
                      protection=True),
                    U('P4', 'VB.11', 'hors_sol_toiture', 400, tache='R', epaisseur=10, criteres=(2, 3, False))],
         emprise=400)])

# F04 terres agricoles
ex('F04', 'Culture ou prairie permanente à l\'état initial',
   'Le même lotissement de 2 000 m² est construit sur une culture intensive (variante A) ou sur une prairie '
   'permanente pâturée en état moyen (variante B). Le projet est identique.',
   [base('A', [U('I1', 'I1.1', PT, 2000)], [U('P1', 'VB.1', PT, 600), U('P2', 'VB.2', PT, 400),
                                            U('P3', 'VB.7', PT, 1000, tache='J', criteres=(2, 3, False))]),
    base('B', [U('I1', 'E2.1', PT, 2000, tache='T', criteres=(4, 6, False))],
         [U('P1', 'VB.1', PT, 600), U('P2', 'VB.2', PT, 400), U('P3', 'VB.7', PT, 1000, tache='J',
                                                                criteres=(2, 3, False))])])

# F07 friches
proj = [U('P1', 'VB.1', PT, 800), U('P2', 'VB.2', PT, 400), U('P3', 'VB.7', PT, 800, tache='J', criteres=(2, 3, False))]
ex('F07', 'Friche riche ou terrain vague',
   'Une friche urbaine de 2 000 m² est construite. Variante A : friche en mosaïque riche (critère D satisfait, '
   'aucune espèce envahissante). Variante B : terrain vague envahi par une espèce exotique (critère C essentiel '
   'échoué).',
   [base('A', [U('I1', 'VB.8', PT, 2000, tache='F', criteres=(4, 4, False))], proj),
    base('B', [U('I1', 'VB.8', PT, 2000, tache='F', criteres=(2, 4, True))], proj)])

# F08 sols reconstitués
ini = [U('I1', 'VB.2', PT, 2000)]
ex('F08', 'Jardin en pleine terre ou sur dalle de parking',
   'Un jardin commun de 800 m² est aménagé. Variante A : en pleine terre. Variantes B, C et D : sur la dalle d\'un '
   'parking souterrain, avec 30, 60 et 100 cm de substrat.',
   [base('A', ini, [U('P1', 'VB.1', PT, 800), U('P2', 'VB.2', PT, 400), U('P3', 'VB.7', PT, 800, tache='J',
                                                                       criteres=(2, 3, False))]),
    *[base(lettre, ini, [U('P1', 'VB.1', PT, 800), U('P2', 'VB.2', PT, 400),
                         U('P3', 'VB.7', 'sol_sur_dalle', 800, tache='J', epaisseur=e, criteres=(2, 3, False))])
      for lettre, e in (('B', 30), ('C', 60), ('D', 100))]])

# F09 protection en chantier
ini = [U('I1', 'E2.2', PT, 1200, tache='T', criteres=(5, 6, False)), U('I2', 'VB.2', PT, 800)]
ex('F09', 'Prairie conservée avec ou sans protection en chantier',
   'Une prairie de fauche de 1 200 m² est conservée pendant un chantier de 24 mois. Variante A : clôturée et '
   'protégée. Variante B : sans protection (convention C-T4).',
   [base('A', ini, [U('P1', 'E2.2', PT, 1200, tache='T', criteres=(5, 6, False), statut='conservee', liee='I1',
                      protection=True), U('P2', 'VB.1', PT, 800)], mois=24),
    base('B', ini, [U('P1', 'E2.2', PT, 1200, tache='T', criteres=(5, 6, False), statut='conservee', liee='I1'),
                    U('P2', 'VB.1', PT, 800)], mois=24)])

# F10 arbres
ini = [U('I1', 'VB.5', PT, 2000, tache='T', criteres=(3, 7, False)),
       U('I2', 'VB.18a', 'arbre', 733, tache='T', stade='A', criteres=(5, 6, False))]
ex('F10', 'Deux grands arbres conservés, abattus ou transplantés',
   'Deux chênes indigènes de grand diamètre (houppier de 733 m² par défaut) se trouvent sur une pelouse de 2 000 m² '
   'construite pour moitié. Variante A : conservés et protégés. Variante B : abattus. Variante C : transplantés '
   '(unité créée de stade jeune, fiche F10).',
   [base('A', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.5', PT, 1000, tache='T', criteres=(3, 7, False)),
                    U('P3', 'VB.18a', 'arbre', 733, tache='T', stade='A', criteres=(5, 6, False),
                      statut='conservee', liee='I2', protection=True)]),
    base('B', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.5', PT, 1000, tache='T', criteres=(3, 7, False))]),
    base('C', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.5', PT, 1000, tache='T', criteres=(3, 7, False)),
                    U('P3', 'VB.18a', 'arbre', 733, tache='T', stade='J', criteres=(4, 6, False))])])

# F11 haies
ini = [U('I1', 'FA.4', 'lineaire', 300, tache='H', stade='J', criteres=(4, 8, False)), U('I2', 'I1.1', PT, 1700)]
ex('F11', 'Haie existante renforcée ou remplacée',
   'Une haie indigène pauvre de 150 m sur 2 m borde une culture. Variante A : haie laissée en l\'état. Variante B : '
   'haie renforcée (amélioration, état mauvais vers bon). Variante C : haie arrachée et replantée en haie riche '
   '(création).',
   [base('A', ini, [U('P1', 'FA.4', 'lineaire', 300, tache='H', stade='J', criteres=(4, 8, False),
                      statut='conservee', liee='I1', protection=True), U('P2', 'I1.1', PT, 1700, statut='conservee', liee='I2', protection=True)], emprise=0),
    base('B', ini, [U('P1', 'FA.4', 'lineaire', 300, tache='H', stade='J', criteres=(8, 8, False),
                      statut='amelioree', liee='I1', protection=True), U('P2', 'I1.1', PT, 1700, statut='conservee', liee='I2', protection=True)], emprise=0),
    base('C', ini, [U('P1', 'FA.3', 'lineaire', 300, tache='H', stade='M', criteres=(7, 8, False)),
                    U('P2', 'I1.1', PT, 1700, statut='conservee', liee='I2', protection=True)], emprise=0)])

# F12 biosourcés et réemploi
ini = [U('I1', 'VB.2', PT, 2000)]
proj = [U('P1', 'VB.1', PT, 800), U('P2', 'VB.2', PT, 400), U('P3', 'VB.7', PT, 800, tache='J', criteres=(2, 3, False))]
ex('F12', 'Isolant biosourcé, bois d\'œuvre et réemploi',
   'Même bâtiment de 1 500 m² de S_ref. Variante A : isolation minérale. Variante B : isolation en fibre de bois '
   '(40 m³ de bois de plus, régime non justifié, et 30 kg CO2 éq./m² de moins en production). Variante C : '
   'structure de réemploi (60 kg CO2 éq./m² de moins, 1 000 t de granulats de moins).',
   [base('A', ini, proj, sref=1500, ges={'phase_A1_A5': 480, 'phase_B': 320, 'phase_C': 50},
         bois=[('coupe_rase', 30, 0)], granulats=4000),
    base('B', ini, proj, sref=1500, ges={'phase_A1_A5': 450, 'phase_B': 320, 'phase_C': 50},
         bois=[('coupe_rase', 70, 0)], granulats=4000),
    base('C', ini, proj, sref=1500, ges={'phase_A1_A5': 420, 'phase_B': 320, 'phase_C': 50},
         bois=[('coupe_rase', 30, 0)], granulats=3000)])

# F13 toitures
ini = [U('I1', 'VB.2', PT, 2000)]
ex('F13', 'Toiture : nue, extensive, biodiverse, intensive, biosolaire',
   'Une toiture de 1 000 m² sur un bâtiment de 1 000 m² d\'emprise. Variante A : toiture nue. B : extensive de '
   '8 cm. C : biodiverse de 20 cm. D : intensive de 40 cm. E : biosolaire, 600 m² végétalisés en extensif hors '
   'emprise des panneaux.',
   [base('A', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000)], emprise=1000),
    base('B', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.11', 'hors_sol_toiture', 1000, tache='R', epaisseur=8, criteres=(2, 3, False))],
         emprise=1000),
    base('C', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.12', 'hors_sol_toiture', 1000, tache='R', epaisseur=20, criteres=(4, 4, False))],
         emprise=1000),
    base('D', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.13', 'hors_sol_toiture', 1000, tache='R', epaisseur=40, criteres=(4, 4, False))],
         emprise=1000),
    base('E', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.11', 'hors_sol_toiture', 600, tache='R', epaisseur=10, criteres=(2, 3, False))],
         emprise=1000)])

# F14 façades
ex('F14', 'Façade enracinée ou hors sol',
   'Une façade de 40 m de long est végétalisée sur 10 m de haut (400 m²). Variante A : sans végétalisation. '
   'Variante B : plantes grimpantes enracinées au sol. Variante C : mur végétalisé hors sol.',
   [base('A', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000)], emprise=1000),
    base('B', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.15', 'hors_sol_facade', 400, tache='F', criteres=(2, 3, False))], emprise=1000),
    base('C', ini, [U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 1000),
                    U('P3', 'VB.16', 'hors_sol_facade', 400, tache='F', criteres=(2, 3, False))], emprise=1000)])

# F15 mares
ini = [U('I1', 'VB.5', PT, 2000, tache='T', criteres=(3, 7, False))]
ex('F15', 'Mare naturelle, mare alimentée par le réseau, bassin',
   'Un plan d\'eau de 200 m² est créé dans une pelouse de 2 000 m². Variante A : mare à berges naturelles alimentée '
   'par la pluie. Variante B : même mare remplie par le réseau d\'eau potable (convention C-E4). Variante C : bassin '
   'à eau traitée (VB.21).',
   [base('A', ini, [U('P1', 'VB.5', PT, 1800, tache='T', criteres=(3, 7, False), statut='conservee', liee='I1', protection=True),
                    U('P2', 'VB.20', 'eau', 200, tache='T', criteres=(7, 9, False))], emprise=0),
    base('B', ini, [U('P1', 'VB.5', PT, 1800, tache='T', criteres=(3, 7, False), statut='conservee', liee='I1', protection=True),
                    U('P2', 'VB.20', 'eau', 200, tache='T', criteres=(7, 9, False), alimentation='artificielle')],
         emprise=0),
    base('C', ini, [U('P1', 'VB.5', PT, 1800, tache='T', criteres=(3, 7, False), statut='conservee', liee='I1', protection=True),
                    U('P2', 'VB.21', 'eau', 200, tache='T', criteres=(2, 9, False))], emprise=0)])

# F16 éclairage
ini = [U('I1', 'I1.1', PT, 2000)]
ex('F16', 'Éclairage de la prairie : aucun, conforme, permanent',
   'Une prairie urbaine de 1 200 m² est créée à côté d\'un stationnement éclairé. Variantes A, B et C : classes '
   'd\'éclairage L0, L1 et L2 (fiche A20).',
   [base(lettre, ini, [U('P1', 'VB.2', PT, 800), prairie('P2', 1200, eclairage=cl)], emprise=0)
    for lettre, cl in (('A', 'L0'), ('B', 'L1'), ('C', 'L2'))])

# F17 clôtures
ex('F17', 'Jardins clos par une clôture étanche ou perméable',
   'Des jardins de 1 500 m² sont clos. Variante A : clôture perméable (passages de 15 x 15 cm tous les 20 m). '
   'Variante B : clôture étanche (convention C-C3).',
   [base('A', ini, [U('P1', 'VB.1', PT, 500), U('P2', 'VB.7', PT, 1500, tache='J', criteres=(2, 3, False))],
         taches={'J': {'cloture': 'permeable'}}, emprise=500),
    base('B', ini, [U('P1', 'VB.1', PT, 500), U('P2', 'VB.7', PT, 1500, tache='J', criteres=(2, 3, False))],
         taches={'J': {'cloture': 'etanche'}}, emprise=500)])

# F20 stationnements
ini = [U('I1', 'VB.5', PT, 2000, tache='T', criteres=(3, 7, False))]
ex('F20', 'Stationnement en enrobé, en pavés drainants ou en dalles engazonnées',
   'Un stationnement de 1 000 m² est aménagé sur une pelouse de 2 000 m². Variantes A, B et C : enrobé (VB.2), '
   'pavés à joints sablés (VB.3), dalles alvéolées engazonnées (VB.4).',
   [base(lettre, ini, [U('P1', code, PT, 1000), U('P2', 'VB.5', PT, 1000, tache='T', criteres=(3, 7, False), statut='conservee', liee='I1', protection=True)],
         emprise=0) for lettre, code in (('A', 'VB.2'), ('B', 'VB.3'), ('C', 'VB.4'))])

# F22 état initial dégradé
proj = [U('P1', 'VB.1', PT, 600), U('P2', 'VB.2', PT, 400), U('P3', 'VB.7', PT, 1000, tache='J', criteres=(2, 3, False))]
ex('F22', 'État initial après débroussaillage préalable',
   'Une prairie de fauche en bon état a été labourée un an avant le dépôt. Variante A : état initial saisi tel que '
   'constaté (culture). Variante B : état antérieur documenté, comme l\'impose la convention C-R5.',
   [base('A', [U('I1', 'I1.5', PT, 2000)], proj),
    base('B', [U('I1', 'E2.2', PT, 2000, tache='T', criteres=(5, 6, False))], proj)])


def ligne(nom, r):
    return [nom, nombre(r['v0'], 1), nombre(r['i0'], 0), nombre(r['i1'], 0), nombre(r['cnat'], 0),
            nombre(r['dm'], 0), nombre(r['inat'], 0), nombre(r['bnat'], 1), nombre(r['pt'] * 100, 1)]


def main():
    out = ['### 5.6 Exemples chiffrés', '',
           'Chaque fiche d\'application est illustrée ci-dessous par des variantes d\'une même situation, calculées par '
           'le carnet de référence (`outils/carnet_reference.py`). Sauf mention contraire : parcelle de 2 000 m², '
           'zone continentale, chantier de 12 mois, hors trame verte et bleue, sans nuisance, taches de connexion '
           'faible. Les valeurs sont en m²HE, m²HE·an, points et pourcentage.', '']
    for fiche, titre, texte, variantes in EXEMPLES:
        out += [f'#### Exemple de la fiche {fiche}. {titre}', '', texte, '']
        lignes, detail = [], []
        for v in variantes:
            r = C.calculer(v)
            lignes.append(ligne(f'Variante {v["nom"]}', r))
            detail.append((v['nom'], r))
        out += [tableau(['Variante', 'V_0', 'I_0', 'I_1', 'Cnat', 'Dette', 'Inat', 'Bnat', 'Pleine terre (%)'],
                        lignes), '']
        for nom, r in detail:
            out += [f'Variante {nom}, unités de l\'état projet :', '',
                    tableau(['Unité', 'Type', 'A (m²)', 'v', 'f', 'f_sol', 'k_C', 'k_N', 'k_E', 'V', 'd', 'D'],
                            [[u['id'], u['code'], nombre(u['surface'], 0), nombre(u['v'], 4), nombre(u['f'], 4),
                              nombre(u['f_sol'], 2), nombre(u['kC'], 4), nombre(u['kN'], 3), nombre(u['kE'], 2),
                              nombre(u['V'], 2), nombre(u.get('d', 0), 1), nombre(u.get('D', 1), 2)]
                             for u in r['projet']]), '']
    print(ecrire('05b_exemples_application.md', '\n'.join(out)), len(EXEMPLES), 'exemples')


if __name__ == '__main__':
    main()
