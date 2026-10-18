# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Cas de l'exemple de l'annexe C et huit cas de validation du cahier des charges (§ 7)."""

def U(id, code, position, surface, **k):
    return dict(id=id, code=code, position=position, surface=surface, **k)


# Zone climatique RE2020 (station de référence des fichiers prospectifs) retenue pour chaque zone
# biogéographique dans les cas : continentale, Trappes ; atlantique, Rennes ; méditerranéenne, Marignane ;
# alpine, Mâcon à 900 m d'altitude
CLIMAT = {'continentale': dict(zone_climatique='H1a'), 'atlantique': dict(zone_climatique='H2a'),
          'mediterraneenne': dict(zone_climatique='H3'), 'alpine': dict(zone_climatique='H1c', altitude=900)}


def ctx(zone, typologie, **k):
    return dict(zone=zone, typologie=typologie, **CLIMAT[zone], **k)


# Données des modules dynamiques communes aux cas : chantier commencé en septembre 2027 (abattages et
# défrichements hors période sensible), plan de gestion écologique de dix ans, sol limoneux d'un mètre
DYN = dict(annee_debut=2027, mois_debut=9, plan_gestion_annees=10, sol={'texture': 'limon', 'profondeur': 1.0})

PT = 'sol_pleine_terre'

ANNEXE_C = dict(
    nom='Exemple de l\'annexe C', parcelle=2000, emprise=700, duree_chantier_mois=18, sref=1400,
    contexte=ctx('continentale', 'logement'), **DYN,
    taches={'P1': {}, 'P2': {}, 'P3': {}},
    initial=[U('U0-1', 'VB.8', PT, 1200, tache='P1', criteres=(3, 4, True)), U('U0-2', 'VB.2', PT, 600),
             U('U0-3', 'VB.9', PT, 200, tache='P1', criteres=(2, 5, False)),
             U('U0-4', 'VB.18a', 'arbre', 100, tache='P1', stade='M', criteres=(5, 6, False))],
    projet=[U('U1-1', 'VB.1', PT, 700), U('U1-2', 'VB.2', PT, 300), U('U1-3', 'VB.3', PT, 150),
            U('U1-4', 'VB.26', PT, 450, tache='P2', criteres=(4, 6, False), eclairage='L1'),
            U('U1-5', 'VB.7', PT, 320, tache='P2', criteres=(2, 3, False)),
            U('U1-6', 'FA.3', 'lineaire', 80, tache='P2', stade='M', criteres=(6, 8, False)),
            U('U1-7', 'VB.18a', 'arbre', 100, tache='P2', stade='M', criteres=(5, 6, False), statut='conservee',
              liee='U0-4', protection=True),
            U('U1-8', 'VB.12', 'hors_sol_toiture', 500, tache='P3', epaisseur=15, criteres=(4, 4, False))],
    ges={'phase_A1_A5': 470, 'phase_B': 400, 'phase_C': 55, 'phase_D': -40},
    bois=[('coupe_rase', 30, 0)], granulats=1800)

# Cas 1 : friche urbaine imperméabilisée devenue résidence avec jardin (gain attendu)
CAS1 = dict(
    nom='Cas 1. Friche urbaine imperméabilisée devenue résidence avec jardin',
    attendu='gain : Cnat négatif', parcelle=3000, emprise=900, duree_chantier_mois=20, sref=2200,
    contexte=ctx('atlantique', 'logement'), **DYN,
    taches={'F': {}, 'J': {'connexion': 'moyenne'}, 'T': {}},
    initial=[U('I1', 'VB.2', PT, 2400), U('I2', 'VB.1', PT, 300),
             U('I3', 'VB.8', PT, 300, tache='F', criteres=(1, 4, True))],
    projet=[U('P1', 'VB.1', PT, 900), U('P2', 'VB.2', PT, 300), U('P3', 'VB.3', PT, 200),
            U('P4', 'VB.6', PT, 300, tache='J', criteres=(2, 3, False)),
            U('P5', 'VB.26', PT, 600, tache='J', criteres=(5, 6, False)),
            U('P6', 'VB.7', PT, 400, tache='J', criteres=(2, 3, False)),
            U('P7', 'VB.19', 'eau', 200, tache='J', criteres=(4, 5, False)),
            U('P8', 'FA.3', 'lineaire', 100, tache='J', stade='M', criteres=(6, 8, False)),
            U('P9', 'VB.18a', 'arbre', 977, tache='J', stade='M', criteres=(4, 6, False)),
            U('P10', 'VB.11', 'hors_sol_toiture', 600, tache='T', epaisseur=10, criteres=(2, 3, False))],
    ges={'phase_A1_A5': 520, 'phase_B': 380, 'phase_C': 60}, bois=[('coupe_rase', 40, 0)], granulats=3200,
    infiltration=700)

# Cas 2 : prairie naturelle en périphérie construite en logements (forte perte)
CAS2 = dict(
    nom='Cas 2. Prairie naturelle en périphérie construite en logements',
    attendu='forte perte : Cnat positif et élevé', parcelle=10000, emprise=3000, duree_chantier_mois=24,
    sref=6000, contexte=ctx('continentale', 'logement'), **DYN,
    taches={'PR': {'connexion': 'forte', 'exterieur': 20000}, 'H': {'connexion': 'forte'},
            'JA': {'connexion': 'moyenne'}},
    initial=[U('I1', 'E2.2', PT, 9700, tache='PR', criteres=(5, 6, False)),
             U('I2', 'FA.3', 'lineaire', 300, tache='PR', stade='A', criteres=(8, 10, False))],
    projet=[U('P1', 'VB.1', PT, 3000), U('P2', 'VB.2', PT, 2000),
            U('P3', 'VB.7', PT, 4000, tache='JA', criteres=(2, 3, False)),
            U('P4', 'VB.5', PT, 700, tache='JA', criteres=(3, 7, False)),
            U('P5', 'FA.3', 'lineaire', 300, tache='JA', stade='A', criteres=(8, 10, False), statut='conservee',
              liee='I2', protection=True)],
    ges={'phase_A1_A5': 480, 'phase_B': 350, 'phase_C': 50}, bois=[('coupe_rase', 120, 0)], granulats=9000)

# Cas 3 : bureaux sur dalle avec toiture végétalisée
CAS3 = dict(
    nom='Cas 3. Bureaux sur dalle avec toiture végétalisée',
    attendu='Bnat porté par la dalle et la toiture ; Cnat négatif sur un site déjà imperméable',
    parcelle=4000, emprise=2400, duree_chantier_mois=22, sref=9000,
    contexte=ctx('continentale', 'tertiaire'), **DYN,
    taches={'D': {}, 'T': {}, 'A': {}},
    initial=[U('I1', 'VB.2', PT, 3600), U('I2', 'VB.5', PT, 400, tache='A', criteres=(1, 7, True)),
             U('I3', 'VB.18b', 'arbre', 326, tache='A', stade='M', criteres=(2, 6, False))],
    projet=[U('P1', 'VB.1', PT, 2400), U('P2', 'VB.3', PT, 400),
            U('P3', 'VB.6', 'sol_sur_dalle', 800, tache='D', epaisseur=40, criteres=(2, 3, False)),
            U('P4', 'VB.5', 'sol_sur_dalle', 400, tache='D', epaisseur=30, criteres=(3, 7, False)),
            U('P5', 'VB.13', 'hors_sol_toiture', 1200, tache='T', epaisseur=40, criteres=(4, 4, False)),
            U('P6', 'VB.15', 'hors_sol_facade', 300, tache='D', criteres=(2, 3, False))],
    ges={'phase_A1_A5': 560, 'phase_B': 420, 'phase_C': 45}, bois=[], granulats=11000)

# Cas 4 : réhabilitation sans emprise nouvelle
CAS4 = dict(
    nom='Cas 4. Réhabilitation sans emprise nouvelle',
    attendu="petit gain par la désimperméabilisation de la cour et l'amélioration du jardin",
    parcelle=1500, emprise=900, duree_chantier_mois=14, sref=1600,
    contexte=ctx('continentale', 'logement'), **DYN,
    taches={'J': {}},
    initial=[U('I1', 'VB.1', PT, 900), U('I2', 'VB.2', PT, 400),
             U('I3', 'VB.7', PT, 200, tache='J', criteres=(1, 3, False))],
    projet=[U('P1', 'VB.1', PT, 900, statut='conservee', liee='I1'), U('P2', 'VB.3', PT, 150),
            U('P3', 'VB.7', PT, 250, tache='J', criteres=(2, 3, False)),
            U('P4', 'VB.7', PT, 200, tache='J', criteres=(2, 3, False), statut='amelioree', liee='I3',
              protection=True)],
    ges={'phase_A1_A5': 180, 'phase_B': 260, 'phase_C': 30}, bois=[('coupe_selective', 15, 0)], granulats=300)

# Cas 5 : projet en réservoir de biodiversité (même projet que le cas 2, site en réservoir)
CAS5 = dict(CAS2, nom='Cas 5. Projet en réservoir de biodiversité',
            attendu='perte plus forte que le cas 2, du fait du multiplicateur de situation',
            initial=[dict(u, situation='reservoir') for u in CAS2['initial']],
            projet=[dict(u, situation='reservoir') for u in CAS2['projet']])

# Cas 6 : mare et haies créées sur une culture intensive (effet de maturation)
CAS6 = dict(
    nom='Cas 6. Mare et haies créées sur une culture intensive',
    attendu='gain à maturité, dette de maturité élevée', parcelle=5000, emprise=0, duree_chantier_mois=6,
    sref=0, contexte=ctx('continentale', 'amenagement'), **DYN,
    taches={'N': {'connexion': 'moyenne'}},
    initial=[U('I1', 'I1.1', PT, 5000)],
    projet=[U('P1', 'VB.20', 'eau', 300, tache='N', criteres=(7, 9, False)),
            U('P2', 'FA.3', 'lineaire', 600, tache='N', stade='M', criteres=(6, 8, False)),
            U('P3', 'VB.26', PT, 3000, tache='N', criteres=(4, 6, False)),
            U('P4', 'G1.A', PT, 800, tache='N', stade='M', criteres=(4, 6, False)),
            U('P5', 'VB.3', PT, 300)],
    ges={}, bois=[], granulats=200)

# Cas 7 : bâtiment bois face au même bâtiment béton (module G)
_BASE7 = dict(parcelle=3000, emprise=1000, duree_chantier_mois=18, sref=4000,
              contexte=ctx('continentale', 'logement'), **DYN,
              taches={'J': {}},
              initial=[U('I1', 'E2.6', PT, 3000, tache='J', criteres=(4, 7, False))],
              projet=[U('P1', 'VB.1', PT, 1000), U('P2', 'VB.2', PT, 600),
                      U('P3', 'VB.7', PT, 1400, tache='J', criteres=(2, 3, False))])
CAS7_BETON = dict(_BASE7, nom='Cas 7a. Bâtiment en béton', attendu='Inat climat dominant',
                  ges={'phase_A1_A5': 560, 'phase_B': 300, 'phase_C': 60}, bois=[('coupe_rase', 20, 0)],
                  granulats=9500)
CAS7_BOIS = dict(_BASE7, nom='Cas 7b. Même bâtiment en bois, origine non justifiée',
                 attendu='climat plus faible, occupation des forêts plus forte',
                 ges={'phase_A1_A5': 400, 'phase_B': 300, 'phase_C': 70}, bois=[('coupe_rase', 900, 0)],
                 granulats=2500)
CAS7_BOIS_GERE = dict(CAS7_BOIS, nom='Cas 7c. Même bâtiment en bois issu de coupe sélective justifiée',
                      attendu='Inat le plus faible des trois', bois=[('coupe_selective', 900, 0)])

# Cas 8 : même site en zone méditerranéenne et en zone continentale
CAS8_CONT = dict(CAS6, nom='Cas 8a. Aménagement en zone continentale', attendu='référence',
                 contexte=ctx('continentale', 'amenagement'))
CAS8_MED = dict(CAS6, nom='Cas 8b. Même aménagement en zone méditerranéenne',
                attendu='délais identiques (convention C-E2) ; bilan hydrique et tenue de la mare propres au climat '
                        'méditerranéen',
                contexte=ctx('mediterraneenne', 'amenagement'))
CAS8_MED_SENS = dict(CAS6, nom='Cas 8c. Zone méditerranéenne, délais allongés de 25 % (borne haute de C-E2)',
                     attendu='perte de valeur intégrée par allongement des délais',
                     contexte=ctx('mediterraneenne', 'amenagement', k_delai_etude=1.25))

CAS = [CAS1, CAS2, CAS3, CAS4, CAS5, CAS6, CAS7_BETON, CAS7_BOIS, CAS7_BOIS_GERE, CAS8_CONT, CAS8_MED,
       CAS8_MED_SENS]
