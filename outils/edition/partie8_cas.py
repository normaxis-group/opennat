# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 8 de l'édition complète : cas de validation déroulés par le carnet de référence."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import carnet_reference as C  # noqa: E402
from cas_validation import CAS, ANNEXE_C  # noqa: E402
from commun import ecrire, nombre, tableau  # noqa: E402

ANNEES = (1, 2, 3, 5, 10, 15, 20, 30, 40, 50)


def n(x, d=2):
    return '' if x is None else nombre(x, d)


def table_unites(unites, projet=False):
    ent = ['Unité', 'Type', 'Position', 'A (m²)', 'Nature', 'c', 'f_sol', 'v', 'S', 'f', 'm', 'k_C', 'k_N',
           'k_E', 'V (m²HE)']
    if projet:
        ent += ['Statut', 'd (an)', 'D']
    lignes = []
    for u in unites:
        l = [u['id'], u['code'], u['position'].replace('_', ' '), n(u['surface'], 0), u['nature'] or '',
             n(u['c']), n(u['f_sol']), n(u['v'], 4), n(u['S'], 4), n(u['f'], 4), n(u['m']), n(u['kC'], 4),
             n(u['kN'], 3), n(u['kE']), n(u['V'], 2)]
        if projet:
            l += [u.get('statut', 'creee').replace('creee', 'créée').replace('conservee', 'conservée')
                  .replace('amelioree', 'améliorée'), n(u.get('d'), 1), n(u.get('D'))]
        lignes.append(l)
    return tableau(ent, lignes)


def table_taches(kc):
    if not kc:
        return 'Aucune tache.'
    return tableau(['Tache', 'A_k (m²)', 'k_taille', 'm_conn', 'k_clot', 'k_C'],
                   [[t, n(a, 0), n(kt, 4), n(m), n(kcl), n(k, 4)] for t, (a, kt, m, kcl, k) in sorted(kc.items())])


def derouler(cas, r):
    out = [f'### {cas["nom"]}', '', f'**Résultat attendu** : {cas.get("attendu", "")}.', '',
           '**Hypothèses**', '',
           tableau(['Donnée', 'Valeur'], [
               ['Parcelle', f'{n(cas["parcelle"], 0)} m²'], ['Emprise du bâti', f'{n(cas.get("emprise", 0), 0)} m²'],
               ['Zone biogéographique', cas['contexte']['zone']], ['Typologie', cas['contexte']['typologie']],
               ['Durée du chantier', f'{cas["duree_chantier_mois"]} mois (d_ch = {n(r["d_ch"], 3)} an)'],
               ['Surface de référence', f'{n(cas.get("sref", 0), 0)} m²'],
               ['Émissions des composants et du chantier', ', '.join(
                   f'{p.replace("phase_", "").replace("_", "-")} : {n(g, 0)}' for p, g in cas.get('ges', {}).items())
                or 'aucun bâtiment'],
               ['Bois', ', '.join(f'{n(q, 0)} m³ ({reg.replace("_", " ")})' for reg, q, _ in cas.get('bois', []))
                or 'aucun'],
               ['Granulats', f'{n(cas.get("granulats", 0), 0)} t'],
               ['Surface infiltrée en surface', f'{n(cas.get("infiltration", 0), 0)} m²']]), '',
           '**Étape E2, fermeture (fiche A03)**', '',
           tableau(['État', 'Somme au sol (m²)', 'Écart (m²)', 'Contrôle'],
                   [[k, n(s, 0), n(e, 0), 'satisfait' if ok else 'échoué'] for k, (s, e, ok) in r['fermeture'].items()]),
           '', '**État initial (fiches A06 à A25)**', '', table_unites(r['initial']), '',
           'Taches de l\'état initial (fiches A17 à A19) :', '', table_taches(r['kc0']), '',
           f'Valeur du site sans projet V_0 = {n(r["v0"])} m²HE ; I_0 = {n(r["i0"], 1)} m²HE·an.', '',
           '**État projet (fiches A06 à A30)**', '', table_unites(r['projet'], projet=True), '',
           'Taches de l\'état projet :', '', table_taches(r['kc1']), '',
           '**Trajectoire du site (fiche A31)**', '',
           tableau(['Année'] + [str(a) for a in ANNEES], [['V_1(t), m²HE'] + [n(r['site'][a - 1], 1) for a in ANNEES]]),
           '', '**Indicateurs (fiches A33 à A38)**', '']
    m = r['mat']
    lignes = [['I_0', n(r['i0'], 1), 'm²HE·an'], ['I_1', n(r['i1'], 1), 'm²HE·an'],
              ['Cnat', n(r['cnat'], 1), 'm²HE·an'],
              ['Cnat relatif', n(r['cnat_rel'], 3) if r['cnat_rel'] is not None else 'non défini', ''],
              ['Cnat sur 30 ans', n(r['cnat_30'], 1), 'm²HE·an'], ['Dette de maturité', n(r['dm'], 1), 'm²HE·an'],
              ['Inat climat', n(m['inat_clim'], 1), 'm²HE·an'], ['Inat bois', n(m['inat_bois'], 1), 'm²HE·an'],
              ['Inat carrières', n(m['inat_carr'], 1), 'm²HE·an'], ['Inat', n(r['inat'], 1), 'm²HE·an'],
              ['Snat', n(r['snat'], 1), 'm²HE·an'], ['Bnat', n(r['bnat'], 1), 'points'],
              ['Pleine terre', n(r['pt'], 3), ''], ['Imperméabilisation nette', n(r['aimp1'] - r['aimp0'], 0), 'm²']]
    out += [tableau(['Indicateur', 'Valeur', 'Unité'], lignes), '']
    bmin = r['bnat_min']
    conf = []
    if bmin is not None:
        conf.append(f'Bnat {n(r["bnat"], 1)} pour un seuil de {n(bmin, 0)} : '
                    f'{"atteint" if r["bnat"] >= bmin else "non atteint"}')
    else:
        conf.append('pas de seuil de Bnat pour cette typologie')
    conf.append(f'pleine terre {n(r["pt"] * 100, 1)} % pour un seuil de 15 % : '
                f'{"atteint" if r["pt"] >= r["pt_min"] else "non atteint"}')
    conf.append(f'niveau du site : {r["niveau"]}')
    out += ['**Conformité (fiche A40)** : ' + ' ; '.join(conf) + '.', '']
    return out


def main():
    out = ['## Partie 8. Cas de validation', '',
           'Les huit situations types du cahier des charges (§ 7) sont calculées ci-dessous par le carnet de calcul '
           'de référence (`outils/carnet_reference.py`), qui applique les fiches algorithmes de la partie 3 sans '
           'Monte-Carlo et sans rien partager avec le futur moteur. Chaque cas donne ses hypothèses, toutes les '
           'grandeurs intermédiaires et les indicateurs : le moteur devra les retrouver à 0,1 % près (exigence E10). '
           'Les cas 7 et 8 se déclinent en variantes.', '',
           'Le carnet a d\'abord été contrôlé sur l\'exemple de l\'annexe C de la partie 1, qu\'il retrouve à '
           'l\'identique : V_0 = 270,39 ; I_0 = 13 519,3 ; I_1 = 12 847,4 ; Cnat = 671,9 ; dette de maturité 876,5 ; '
           'Inat = 141 842,9 ; Bnat = 59,0.', '']
    res = {}
    for cas in CAS:
        r = C.calculer(cas)
        res[cas['nom']] = r
        out += derouler(cas, r)
    # synthèse
    out += ['### Synthèse et propriétés vérifiées', '',
            tableau(['Cas', 'Attendu', 'Cnat', 'Inat', 'Snat', 'Bnat', 'Niveau'],
                    [[c['nom'], c.get('attendu', ''), n(res[c['nom']]['cnat'], 0), n(res[c['nom']]['inat'], 0),
                      n(res[c['nom']]['snat'], 0), n(res[c['nom']]['bnat'], 1), str(res[c['nom']]['niveau'])]
                     for c in CAS]), '']
    r2, r5 = res[CAS[1]['nom']], res[CAS[4]['nom']]
    r7 = [res[c['nom']] for c in CAS[6:9]]
    r8 = [res[c['nom']] for c in CAS[9:12]]
    out += ['Propriétés vérifiées par ces cas :', '',
            f'- Une friche imperméabilisée transformée en résidence avec jardin gagne de la nature : Cnat = '
            f'{n(res[CAS[0]["nom"]]["cnat"], 0)} m²HE·an (cas 1).',
            f'- La construction d\'une prairie riche fait perdre l\'essentiel de sa valeur au site : Cnat relatif = '
            f'{n(r2["cnat_rel"], 3)} (cas 2).',
            f'- La même opération en réservoir perd davantage : {n(r5["cnat"], 0)} contre {n(r2["cnat"], 0)} '
            f'm²HE·an, soit le rapport du multiplicateur de situation (cas 5).',
            f'- Les bureaux sur dalle atteignent le seuil de Bnat du tertiaire grâce à la dalle et à la toiture, '
            f'mais pas celui de la pleine terre, nulle (cas 3).',
            f'- La réhabilitation gagne un peu de nature par la cour désimperméabilisée et le jardin amélioré (cas 4).',
            f'- La mare, les haies et le boisement créés sur une culture laissent une dette de maturité de '
            f'{n(res[CAS[5]["nom"]]["dm"], 0)} m²HE·an (cas 6).',
            f'- Bois et béton (cas 7) : Inat vaut {n(r7[0]["inat"], 0)} pour le béton, {n(r7[1]["inat"], 0)} pour le '
            f'bois d\'origine non justifiée et {n(r7[2]["inat"], 0)} pour le bois de coupe sélective justifiée.',
            f'- Zone méditerranéenne (cas 8) : sans différence en v1 ; avec des délais allongés de 25 %, Cnat passe de '
            f'{n(r8[0]["cnat"], 0)} à {n(r8[2]["cnat"], 0)} m²HE·an.', '',
            '### Lecture du cas 7', '',
            'Avec les conventions de la v1, le bâtiment en bois a une biodiversité grise plusieurs fois plus forte que '
            'le même bâtiment en béton. Le climat est plus faible pour le bois, mais l\'occupation des forêts, '
            'comptée en surface et en durée à la perte de MSA du régime d\'exploitation, l\'emporte largement. Le sens '
            'de l\'écart est celui de la littérature citée par l\'audit (Christiansson et Roos 2023 ; Carbone 4, 2026, '
            'pour qui une substitution par du bois de provenance non maîtrisée triple la pression de changement '
            'd\'usage des sols) ; son ampleur dépend de trois conventions à soumettre au Biodiversity Standard '
            'Council : le rapport de 2 m³ de bois rond par m³ de produit (C-G4), le choix d\'une approche '
            'attributionnelle qui compte toute la forêt de production comme une perte par rapport à la forêt '
            'naturelle (C-G5), et l\'absence de prise en compte de l\'occupation des usines et des carrières de '
            'ciment pour les autres matériaux (C-G7), qui avantage le béton. Ce cas est le premier à recalibrer.', '']
    print(ecrire('08_cas_validation.md', '\n'.join(out)))


if __name__ == '__main__':
    main()
