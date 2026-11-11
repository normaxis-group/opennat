# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Construit donnees/sols.csv : coefficients de nature de surface (module S, Bnat).

Règle (convention C-S1, point P12 de l'audit) : pour chaque nature de surface, valeur
centrale = médiane des coefficients publiés par les grilles de coefficient de biotope
relevées ci-dessous ; plage d'incertitude = valeur la plus basse et la plus haute.

RELEVES : transcription, ligne par ligne, des grilles lues dans les documents conservés
dans sources/grilles/ (lecture du 18/10/2026). Une grille qui ne traite pas une nature
n'y figure pas ; une grille qui distingue plusieurs cas pour une même nature y figure
par chacun de ses cas.
"""
import csv
import os
import statistics

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

G = {
    'berlin': ('Berlin, Biotopflächenfaktor, facteurs des plans fixés après décembre 2019',
               'https://www.berlin.de/sen/uvk/natur-und-gruen/landschaftsplanung/bff-biotopflaechenfaktor/bff-berechnung/',
               'texte administratif public'),
    'londres': ('London Plan Guidance, Urban Greening Factor, février 2023, Table 3.1 p. 8 et 9',
                'https://www.london.gov.uk/sites/default/files/2023-02/London%20Plan%20Guidance%20-%20Urban%20Greening%20Factor.pdf',
                'Open Government Licence v3.0'),
    'strasbourg': ('PLU de l\'Eurométropole de Strasbourg, règlement écrit, dispositions toutes zones, '
                   'modification n° 4 (mai 2024), article 9.2, p. 33 et 34',
                   'https://sig.strasbourg.eu/datastrasbourg/plu_media/reglement_actuel.pdf',
                   'document d\'urbanisme public'),
    'annecy': ('PLUi-HMB du Grand Annecy, fiche d\'aide à l\'instruction des coefficients de biotope et '
               'de pleine terre, § 1.2',
               'https://plui-hmb-approuve-ga.grandannecy.fr/04_REGLEMENT/FICHE_AIDE_instruction_CBS.pdf',
               'document d\'urbanisme public'),
    'paris': ('Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, '
              'règle UG.4, indice de végétalisation du bâti, p. 63 (coefficients sur 10 ramenés sur 1)',
              'https://cdn.paris.fr/paris/2025/07/17/250715_guideenvironnemental-tfz6.pdf',
              'document d\'urbanisme public'),
    'lille': ('PLU de la Métropole européenne de Lille, tableau du CBS (Livre 1, p. 16), extrait du '
              'Pacte Lille Bas Carbone, version du 18/10/2022',
              'https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-06/Lille_CBS_calcul_tableau.pdf',
              'document d\'urbanisme public'),
}

# (nature, grille, valeur, cas relevé)
RELEVES = [
    ('S01', 'berlin', 0.0, 'Versiegelte Flächen'),
    ('S01', 'londres', 0.0, 'Sealed surfaces'),
    ('S01', 'strasbourg', 0.0, 'Surface minérale imperméable'),
    ('S01', 'annecy', 0.0, 'Surfaces imperméables'),
    ('S01', 'lille', 0.0, 'Surface imperméable'),
    ('S02', 'berlin', 0.1, 'Teilversiegelte Flächen (pavés, stabilisé, wassergebundene Decke)'),
    ('S02', 'berlin', 0.2, 'Durchlässige Belagsflächen (dalles drainantes, sable, gravier)'),
    ('S02', 'londres', 0.1, 'Permeable paving'),
    ('S02', 'strasbourg', 0.2, 'Surface minérale perméable'),
    ('S02', 'annecy', 0.3, 'Surfaces semi-perméables'),
    ('S02', 'lille', 0.25, 'Surface perméable non végétalisée'),
    ('S03', 'berlin', 0.4, 'Begrünte Belagsflächen (Rasengitter, pavés à joints engazonnés)'),
    ('S03', 'strasbourg', 0.2, 'Surface minérale perméable (pavés joints gazon)'),
    ('S03', 'annecy', 0.5, 'Surfaces semi-ouvertes'),
    ('S03', 'lille', 0.5, 'Surface perméable végétalisée'),
    ('S04', 'berlin', 0.5, 'Extensive Dachbegrünung (moins de 20 cm)'),
    ('S04', 'londres', 0.7, 'Extensive green roof, au moins 80 mm (GRO Code 2014)'),
    ('S04', 'londres', 0.3, 'Extensive green roof of sedum mat'),
    ('S04', 'strasbourg', 0.5, 'Toiture végétalisée extensive de moins de 10 cm'),
    ('S04', 'strasbourg', 0.6, 'Toiture extensive ou semi-intensive de 30 cm au plus'),
    ('S04', 'annecy', 0.5, 'Espaces verts sur dalle 1 (moins de 80 cm)'),
    ('S04', 'lille', 0.5, 'Toiture extensive et dalle de 15 à 20 cm, gazon ou mousse'),
    ('S04', 'lille', 0.7, 'Toiture extensive et dalle de 15 à 20 cm, végétation hors gazon et mousse'),
    ('S05', 'berlin', 0.5, 'Unterbaute Vegetationsfläche, 20 à 40 cm'),
    ('S05', 'berlin', 0.7, 'Einfach-intensive Dachbegrünung, 15 à 50 cm'),
    ('S05', 'londres', 0.8, 'Intensive green roof or vegetation over structure, au moins 150 mm'),
    ('S05', 'strasbourg', 0.6, 'Toiture extensive ou semi-intensive de 30 cm au plus'),
    ('S05', 'annecy', 0.5, 'Espaces verts sur dalle 1 (moins de 80 cm)'),
    ('S05', 'paris', 0.6, 'S3, substrat d\'au moins 25 cm'),
    ('S05', 'lille', 0.6, 'Toiture semi-intensive ou intensive et dalle de plus de 20 cm'),
    ('S06', 'berlin', 0.6, 'Unterbaute Vegetationsfläche, 41 à 80 cm'),
    ('S06', 'berlin', 0.8, 'Intensive Dachbegrünung, plus de 50 cm'),
    ('S06', 'londres', 0.8, 'Intensive green roof or vegetation over structure, au moins 150 mm'),
    ('S06', 'strasbourg', 0.7, 'Plantations sur dalle ou toiture intensive, plus de 30 cm'),
    ('S06', 'annecy', 0.5, 'Espaces verts sur dalle 1 (moins de 80 cm)'),
    ('S06', 'paris', 0.8, 'S2, substrat de 50 à 80 cm'),
    ('S06', 'lille', 0.6, 'Toiture semi-intensive ou intensive et dalle de plus de 20 cm'),
    ('S07', 'berlin', 0.7, 'Unterbaute Vegetationsfläche, 81 à 150 cm'),
    ('S07', 'berlin', 0.9, 'Unterbaute Vegetationsfläche, plus de 150 cm'),
    ('S07', 'londres', 0.8, 'Intensive green roof or vegetation over structure'),
    ('S07', 'strasbourg', 0.9, 'Plantations sur dalle ou toiture, 80 cm et plus'),
    ('S07', 'annecy', 0.7, 'Espaces verts sur dalle 2 (plus de 80 cm)'),
    ('S07', 'paris', 1.0, 'S1, substrat de 80 cm et plus'),
    ('S07', 'lille', 1.0, 'Espace vert sur dalle d\'au moins 1 m'),
    ('S08', 'berlin', 1.0, 'Vegetationsfläche mit Bodenanschluss'),
    ('S08', 'londres', 1.0, 'Semi-natural vegetation'),
    ('S08', 'strasbourg', 1.0, 'Espaces plantés en pleine terre'),
    ('S08', 'annecy', 1.0, 'Espaces verts en pleine terre'),
    ('S08', 'lille', 1.0, 'Espace vert en continuité avec la terre naturelle'),
    ('S09', 'berlin', 0.5, 'Bodengebundene Vertikalbegrünung (10 m au plus)'),
    ('S09', 'londres', 0.6, 'Green wall, climbers rooted in soil'),
    ('S09', 'strasbourg', 0.4, 'Aménagement végétalisé en surface verticale'),
    ('S09', 'paris', 0.2, 'S5, surfaces verticales végétalisées (15 m au plus)'),
    ('S09', 'lille', 0.4, 'Végétalisation des murs aveugles (10 m au plus)'),
    ('S10', 'berlin', 0.7, 'Wandgebundene Vertikalbegrünung (10 m imputés au plus)'),
    ('S10', 'londres', 0.6, 'Green wall, modular system'),
    ('S10', 'strasbourg', 0.4, 'Aménagement végétalisé en surface verticale'),
    ('S10', 'lille', 0.4, 'Végétalisation des murs aveugles'),
    ('S11', 'berlin', 0.5, 'Wasserfläche, alimentée par l\'eau de pluie'),
    ('S11', 'berlin', 0.6, 'Wasserfläche avec végétation établie (+0,1)'),
    ('S11', 'londres', 1.0, 'Wetland or open water (semi-natural; not chlorinated)'),
    ('S12', 'londres', 0.2, 'Water features (chlorinated) or unplanted detention basins'),
    ('S13', 'berlin', 0.2, 'Versickerungsfläche, par m² de surface extérieure infiltrée'),
]

NATURES = {
    'S01': 'Surface scellée (bâti, enrobé, béton, dallage à joints étanches)',
    'S02': 'Revêtement perméable non végétalisé (stabilisé, gravier, pavés à joints sablés)',
    'S03': 'Revêtement perméable végétalisé (dalles alvéolées, pavés à joints engazonnés)',
    'S04': 'Végétation sur dalle ou toiture, substrat de moins de 15 cm',
    'S05': 'Végétation sur dalle ou toiture, substrat de 15 à 30 cm',
    'S06': 'Végétation sur dalle ou toiture, substrat de plus de 30 cm et de moins de 80 cm',
    'S07': 'Végétation sur dalle ou toiture, substrat de 80 cm et plus',
    'S08': 'Pleine terre',
    'S09': 'Façade végétalisée enracinée au sol (par m² de façade, 10 m de hauteur au plus)',
    'S10': 'Façade végétalisée hors sol (par m² de façade, 10 m de hauteur au plus)',
    'S11': 'Eau à ciel ouvert alimentée par la pluie, berges naturelles',
    'S12': 'Bassin à eau traitée ou bassin de rétention nu',
    'S13': 'Bonus d\'infiltration à ciel ouvert, par m² de surface extérieure dont l\'eau est infiltrée',
}

COLONNES = ['cle', 'parametre', 'valeur', 'unite', 'incertitude_min', 'incertitude_max',
            'source', 'reference_precise', 'url', 'licence', 'type', 'convention',
            'justification']


def main():
    lignes = []
    for nat, libelle in NATURES.items():
        rel = [r for r in RELEVES if r[0] == nat]
        vals = [r[2] for r in rel]
        med = statistics.median(vals)
        grilles = sorted({r[1] for r in rel})
        typ = 'convention' if len(grilles) > 1 else 'transposition'
        detail = ' ; '.join(f'{G[r[1]][0].split(",")[0]} {r[2]:g} ({r[3]})' for r in rel)
        lignes.append({
            'cle': nat, 'parametre': 'coefficient_sol', 'valeur': round(med, 3),
            'unite': 'sans unité', 'incertitude_min': min(vals), 'incertitude_max': max(vals),
            'source': ' ; '.join(G[g][0] for g in grilles),
            'reference_precise': detail,
            'url': ' ; '.join(G[g][1] for g in grilles),
            'licence': ' ; '.join(sorted({G[g][2] for g in grilles})),
            'type': typ, 'convention': 'C-S1',
            'justification': f'{libelle}. Médiane de {len(vals)} valeurs publiées par '
                             f'{len(grilles)} grille(s) ; plage = étendue des valeurs.'})
    with open(os.path.join(RACINE, 'donnees', 'sols.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    for l in lignes:
        print(l['cle'], l['valeur'], l['incertitude_min'], l['incertitude_max'])


if __name__ == '__main__':
    main()
