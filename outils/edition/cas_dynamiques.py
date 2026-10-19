# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Cas dynamiques du banc de validation : l'exemple de l'annexe C (et le cas 6 pour la mare) décliné en ne
faisant varier qu'une donnée des modules dynamiques à la fois (calendrier du chantier, substrat, sol,
arrosage, zone climatique, éclairage, gestion, année de début, mare, abattage d'arbres à gîtes)."""
from cas_validation import ANNEXE_C, CAS6, U, ctx


def variante(num, libelle, attendu, base=ANNEXE_C, projet=None, initial=None, **k):
    c = dict(base, nom=f'Cas D{num:02d}. {libelle}', attendu=attendu, **k)
    if projet:
        c['projet'] = [projet.get(u['id'], lambda x: x)(dict(u)) for u in base['projet']]
    if initial:
        c['initial'] = [initial.get(u['id'], lambda x: x)(dict(u)) for u in base['initial']]
    return c


def maj(**k):
    return lambda u: dict(u, **k)


CAS_DYN = [
    variante(1, 'Chantier commencé en mai : défrichement pendant la nidification',
             'supplément de Cnat pour la friche et le fourré détruits en période sensible (fiche A57)', mois_debut=5),
    variante(2, 'Chantier commencé en janvier : plantations reportées à novembre de l\'année suivante',
             'maturation plus tardive, Cnat plus élevé que l\'exemple (fiche A58)', mois_debut=1),
    variante(3, 'Toiture extensive de 8 cm au lieu de 15 cm', 'valeur et facteur hydrique plus faibles (fiche A48)',
             projet={'U1-8': maj(code='VB.11', epaisseur=8)}),
    variante(4, 'Toiture semi-intensive de 30 cm', 'moins de stress hydrique (fiche A48)',
             projet={'U1-8': maj(epaisseur=30)}),
    variante(5, 'Toiture intensive de 50 cm (gazon et massifs, type VB.13)',
             'facteur hydrique de 1 mais valeur intrinsèque plus faible que la toiture biodiverse (distinctivité '
             'faible de la métrique anglaise)',
             projet={'U1-8': maj(code='VB.13', epaisseur=50)}),
    variante(6, 'Prairie urbaine arrosée', 'facteur hydrique de 1, consommation d\'eau d\'arrosage affichée (fiche A49)',
             projet={'U1-4': maj(arrose=True)}),
    variante(7, 'Sol sableux', 'réserve utile plus faible, stress hydrique accru (fiche A48)',
             sol={'texture': 'sable', 'profondeur': 1.0}),
    variante(8, 'Sol argileux', 'réserve utile plus forte', sol={'texture': 'argile', 'profondeur': 1.0}),
    variante(9, 'Sol limoneux de 40 cm sur dalle rocheuse', 'réserve utile bornée par la profondeur de sol',
             sol={'texture': 'limon', 'profondeur': 0.4}),
]
n = 9
for zone, nom in (('H1b', 'Nancy'), ('H1c', 'Mâcon'), ('H2a', 'Rennes'), ('H2b', 'Tours'), ('H2c', 'Agen'),
                  ('H2d', 'Carpentras'), ('H3', 'Marignane')):
    n += 1
    CAS_DYN.append(variante(n, f'Zone climatique {zone} ({nom})', 'effet du climat local et de son évolution',
                            contexte=dict(ANNEXE_C['contexte'], zone_climatique=zone)))
CAS_DYN += [
    variante(17, 'Prairie éclairée toute la nuit en 4 000 K', 'facteur d\'éclairage de 0,75 (fiche A53)',
             projet={'U1-4': maj(eclairage='L2')}),
    variante(18, 'Prairie éclairée jusqu\'à 23 h en 2 700 K, luminaires à 20 m',
             'facteur d\'éclairage proche de 1 (fiche A53)',
             projet={'U1-4': maj(eclairage=dict(extinction=23, rallumage=None, cct=2700, distance=20))}),
    variante(19, 'Prairie éclairée toute la nuit en ambre avec détection de présence (30 % du temps)',
             'facteur d\'éclairage intermédiaire',
             projet={'U1-4': maj(eclairage=dict(extinction=None, rallumage=None, cct=1800, distance=0,
                                                taux_detection=0.3))}),
    variante(20, 'Sans plan de gestion écologique', 'gestion courante dès la livraison (fiche A55, C-M3)',
             plan_gestion_annees=0),
    variante(21, 'Plan de gestion de trente ans', 'gestion courante après trente ans', plan_gestion_annees=30),
    variante(22, 'Plan de gestion couvrant les cinquante ans', 'aucune perte de gestion', plan_gestion_annees=50),
    variante(23, 'Abandon de l\'entretien à la fin du plan de dix ans', 'friche puis embroussaillement des '
             'milieux herbacés (fiche A56, C-M2)', projet={k: maj(apres_plan='abandon') for k in ('U1-4', 'U1-5')}),
    variante(24, 'Chantier commencé en 2045', 'climat plus chaud sur la période : facteurs hydriques plus faibles '
             '(fiche A46)', annee_debut=2045),
    variante(25, 'Cas 6 en zone H3, mare sans bassin versant', 'assec de printemps (fiche A49, C-W12)', base=CAS6,
             contexte=ctx('mediterraneenne', 'amenagement')),
    variante(26, 'Cas 6 en zone H3, mare raccordée à 3 000 m² de prairie', 'mare en eau au printemps', base=CAS6,
             contexte=ctx('mediterraneenne', 'amenagement'),
             projet={'P1': maj(bassin_versant_permeable=3000)}),
    variante(27, 'Cas 6 en zone H3, mare à fond étanche raccordée à 3 000 m² de prairie', 'mare en eau toute l\'année',
             base=CAS6, contexte=ctx('mediterraneenne', 'amenagement'),
             projet={'P1': maj(bassin_versant_permeable=3000, fond='etanche')}),
    variante(28, 'Arbres âgés à gîtes abattus en janvier', 'supplément de Cnat pour les chiroptères en hibernation '
             '(fiche A57)', mois_debut=1,
             initial={'U0-4': maj(stade='A')},
             projet={'U1-7': lambda u: dict(U('U1-7', 'VB.18a', 'arbre', 100, tache='P2', stade='M',
                                                criteres=(5, 6, False)))}),
    variante(30, 'Indicateurs de pollution médians de neuf bâtiments réels',
             'biodiversité grise accrue de la pollution convertie (fiche A36-2, C-G8)',
             pollution={'106': 0.207, '107': 0.00805, '108': 0.0369, '109': 0.383, '116': 2.37}),
    variante(29, 'Arbres âgés à gîtes abattus en octobre', 'pas de supplément : période favorable', mois_debut=10,
             initial={'U0-4': maj(stade='A')},
             projet={'U1-7': lambda u: dict(U('U1-7', 'VB.18a', 'arbre', 100, tache='P2', stade='M',
                                                criteres=(5, 6, False)))}),
]
