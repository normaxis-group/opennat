# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Partie 8 de l'édition complète : cas de validation déroulés par le carnet de référence."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import carnet_reference as C  # noqa: E402
from cas_validation import CAS, ANNEXE_C  # noqa: E402
from cas_complementaires import CAS_SUPP  # noqa: E402
from cas_dynamiques import CAS_DYN  # noqa: E402
from commun import ecrire, nombre, tableau  # noqa: E402

ANNEES = (1, 2, 3, 5, 10, 15, 20, 30, 40, 50)
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre',
        'décembre']
NIV = ('2_0', '2_7', '4_0')


def table_dynamique(unites, projet=False):
    """Facteurs des modules dynamiques par unité : bilan hydrique (A47 à A50), éclairage (A53), départ de la
    maturation (A58) et facteur de gestion de la dernière année (A56)."""
    ent = ['Unité', 'Groupe', 'RU (mm)', 'IS +2', 'IS +2,7', 'IS +4', 'k_W +2', 'k_W +2,7', 'k_W +4', 'k_lum']
    if projet:
        ent += ['Départ (rang)', 'f_g an 50']
    rows = []
    for u in unites:
        b = u.get('bilan', {})
        b0 = b.get('2_0') or {}
        l = [u['id'], (b0.get('groupe') or 'sans bilan').replace('_', ' '), n(b0.get('RU'), 0) if 'RU' in b0 else '']
        l += [n(b[k]['IS'], 1) if b.get(k) and 'IS' in b[k] else '' for k in NIV]
        l += [n(u['kW_niveaux'][k], 3) for k in NIV]
        l.append(n(u.get('kL', 1.0), 3))
        if projet:
            l += [str(u.get('mois_depart', '')), n(u['f_gestion'][-1], 3)]
        rows.append(l)
    return tableau(ent, rows)


def n(x, d=2):
    return '' if x is None else nombre(x, d)


def table_unites(unites, projet=False):
    """Deux tableaux : identification de l'unité, puis facteurs de calcul."""
    ent1 = ['Unité', 'Type', 'Position', 'A (m²)', 'Nature']
    if projet:
        ent1 += ['Statut', 'd (an)', 'D']
    l1, l2 = [], []
    for u in unites:
        l = [u['id'], u['code'], u['position'].replace('_', ' '), n(u['surface'], 0), u['nature'] or '']
        if projet:
            l += [u.get('statut', 'creee').replace('creee', 'créée').replace('conservee', 'conservée')
                  .replace('amelioree', 'améliorée'), n(u.get('d'), 1), n(u.get('D'))]
        l1.append(l)
        l2.append([u['id'], n(u['c']), n(u['f_sol']), n(u['v'], 4), n(u['S'], 4), n(u['f'], 4), n(u['m']),
                   n(u['kC'], 4), n(u['kN'], 3), n(u['kE']), n(u['V'], 2)])
    return (tableau(ent1, l1) + '\n\nFacteurs de calcul :\n\n' +
            tableau(['Unité', 'c', 'f_sol', 'v', 'S', 'f', 'm', 'k_C', 'k_N', 'k_E', 'V (m²HE)'], l2))


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
               ['Zone climatique, altitude', f'{r["contexte"]["zone_climatique"]}, '
                + (f'{n(r["contexte"]["altitude"], 0)} m' if r['contexte'].get('altitude') else 'altitude de la station')],
               ['Sol du site', ', '.join(f'{k} {v}' for k, v in cas.get('sol', {}).items()) or 'limon, 1 m (défaut)'],
               ['Début du chantier', f'{MOIS[cas.get("mois_debut", 1) - 1]} {cas.get("annee_debut", 2027)} ; '
                f'période {r["annees"][0]} à {r["annees"][-1]}'],
               ['Mois de destruction', MOIS[cas.get('mois_destruction', cas.get('mois_debut', 1)) - 1]],
               ['Plan de gestion écologique', f'{cas.get("plan_gestion_annees", 0)} ans'],
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
           '**Modules dynamiques, état initial (fiches A47 à A53)**', '', table_dynamique(r['initial']), '',
           '**Modules dynamiques, état projet (fiches A47 à A58)**', '', table_dynamique(r['projet'], True), '',
           '**Trajectoire du site (fiche A31)**', '',
           tableau(['Année'] + [str(a) for a in ANNEES], [['V_1(t), m²HE'] + [n(r['site'][a - 1], 1) for a in ANNEES],
                                                          ['V_0 x k_W, m²HE'] + [n(r['ref'][a - 1], 1) for a in ANNEES]]),
           '', '**Indicateurs (fiches A33 à A38)**', '']
    m = r['mat']
    lignes = [['I_0', n(r['i0'], 1), 'm²HE·an'], ['I_1', n(r['i1'], 1), 'm²HE·an'],
              ['Cnat', n(r['cnat'], 1), 'm²HE·an'],
              ['Cnat relatif', n(r['cnat_rel'], 3) if r['cnat_rel'] is not None else 'non défini', ''],
              ['Cnat sur 30 ans', n(r['cnat_30'], 1), 'm²HE·an'], ['Dette de maturité', n(r['dm'], 1), 'm²HE·an'],
              ['Supplément pour destruction en période sensible', n(r['faune'], 1), 'm²HE·an'],
              ['Arrosage annuel moyen', n(r['arrosage_m3_an'], 1), 'm³'],
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


RC = C.calculer(ANNEXE_C)


def main():
    out = ['## Partie 8. Cas de validation', '',
           'Les huit situations types du cahier des charges (§ 7) sont calculées ci-dessous par le carnet de calcul '
           'de référence (`outils/carnet_reference.py`), qui applique les fiches algorithmes de la partie 3 sans '
           'Monte-Carlo et sans rien partager avec le futur moteur. Chaque cas donne ses hypothèses, toutes les '
           'grandeurs intermédiaires et les indicateurs : le moteur devra les retrouver à 0,1 % près (exigence E10). '
           'Les cas 7 et 8 se déclinent en variantes.', '',
           f'Le carnet a d\'abord été contrôlé sur l\'exemple de l\'annexe C de la partie 1, qu\'il retrouve à '
           f'l\'identique : V_0 = {n(RC["v0"])} ; I_0 = {n(RC["i0"], 1)} ; I_1 = {n(RC["i1"], 1)} ; Cnat = '
           f'{n(RC["cnat"], 1)} ; dette de maturité {n(RC["dm"], 1)} ; Inat = {n(RC["inat"], 1)} ; Bnat = '
           f'{n(RC["bnat"], 1)}. Les grandeurs des modules dynamiques (bilan hydrique horaire, éclairage horaire, '
           f'maturation, gestion, calendrier) sont données par unité dans chaque cas.', '']
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
            f'- Zone méditerranéenne (cas 8) : les délais sont les mêmes (C-E2), mais la mare non raccordée s\'assèche '
            f'au printemps sous le climat de Marignane ; Cnat passe de {n(r8[0]["cnat"], 0)} à {n(r8[1]["cnat"], 0)} '
            f'm²HE·an, et à {n(r8[2]["cnat"], 0)} avec des délais allongés de 25 %.', '',
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
    out += ['### Cas complémentaires', '',
            "Trente et un cas complémentaires déclinent une même opération type (part d'emprise bâtie, 15 % de "
            "voirie, jardins, prairie urbaine et haie sur le reste, toiture extensive sur la moitié de l'emprise, "
            "arbres plantés) sur cinq sites initiaux, trois tailles de parcelle, trois emprises, deux typologies, "
            "trois durées de chantier, trois situations, trois éclairages et quatre zones. Ils forment, avec les huit "
            "cas précédents, le jeu de référence du banc de validation du moteur (lot 4).", '']
    rs = [(cas, C.calculer(cas)) for cas in CAS_SUPP]
    out += ['#### Synthèse des cas complémentaires', '',
            tableau(['Cas', 'V_0', 'Cnat', 'Cnat relatif', 'Dette', 'Inat', 'Snat', 'Bnat', 'Niveau'],
                    [[c['nom'].split('. ')[0], n(r['v0'], 1), n(r['cnat'], 0),
                      n(r['cnat_rel'], 3) if r['cnat_rel'] is not None else 'non défini', n(r['dm'], 0),
                      n(r['inat'], 0), n(r['snat'], 0), n(r['bnat'], 1), str(r['niveau'])] for c, r in rs]), '',
            'Lecture :', '',
            "- La taille de la parcelle change peu la consommation relative (C04 à C06 : 0,63 à 0,64) : l'effet de "
            "taille des taches touche l'état initial comme l'état projet.",
            "- La prairie de fauche et la chênaie-charmaie de stade moyen donnent les mêmes résultats (C04 à C06 et "
            "C10 à C12) : leurs valeurs de biotope allemandes sont égales (20 sur 24) et leurs grilles d'état sont "
            "remplies de la même façon. La méthode ne distingue ici un boisement d'une prairie que par son stade.",
            "- Plus l'emprise augmente, plus Cnat et Inat augmentent et plus Bnat baisse (C05, C16, C17).",
            "- Un chantier plus long creuse la perte (C19, C08, C20 : 6, 18 et 36 mois).",
            "- La situation en corridor ou en réservoir augmente la perte dans le rapport des multiplicateurs "
            "(C05, C21, C22).",
            "- L'éclairage de la prairie créée réduit le gain (C02, C23, C24).",
            "- La zone biogéographique ne change pas les délais (C-E2) ; les écarts entre C02 et C25 à C27 viennent "
            "du climat de la station de référence (Trappes, Rennes, Marignane, Mâcon à 900 m) et restent faibles, "
            "le facteur hydrique ne comptant que l'écart au climat local.",
            "- Un parking revêtu transformé en résidence avec jardins gagne toujours de la nature (C13 à C15, C30, "
            "C31) ; sa valeur initiale nulle laisse Cnat relatif non défini et le niveau 2 se juge sur Cnat < 0.", '']
    for cas, r in rs:
        out += derouler(cas, r)
    # cas dynamiques
    r6 = C.calculer(next(c for c in CAS if c['nom'].startswith('Cas 6')))
    rd = [(cas, C.calculer(cas)) for cas in CAS_DYN]

    def ref(cas):
        return r6 if 'Cas 6' in cas['nom'] else RC
    out += ['### Cas dynamiques', '',
            "Vingt-neuf cas reprennent l'exemple de l'annexe C (et le cas 6 pour la mare) en ne changeant qu'une "
            "donnée des modules dynamiques : calendrier du chantier, substrat de la toiture, sol, arrosage, zone "
            "climatique, éclairage, plan de gestion, année de début, raccordement et fond de la mare, abattage "
            "d'arbres à gîtes. L'écart se lit par rapport à l'exemple de l'annexe C (Cnat = "
            f"{n(RC['cnat'], 1)}) ou au cas 6 en zone H3 pour D25 à D27 (Cnat du cas 6 en zone H1a : "
            f"{n(r6['cnat'], 1)}).", '',
            '#### Synthèse des cas dynamiques', '',
            tableau(['Cas', 'Donnée changée', 'I_1', 'Cnat', 'Écart', 'ΔI_ch', 'Arrosage (m³/an)'],
                    [[c['nom'].split('. ')[0], c['nom'].split('. ', 1)[1], n(r['i1'], 0), n(r['cnat'], 0),
                      n(r['cnat'] - ref(c)['cnat'], 0), n(r['faune'], 1), n(r['arrosage_m3_an'], 1)]
                     for c, r in rd]), '',
            'Lecture :', '']
    d = {c['nom'].split('. ')[0]: r for c, r in rd}
    e = lambda k: n(d[k]['cnat'] - RC['cnat'], 0)
    out += [f"- Calendrier : un défrichement en mai ajoute {n(d['Cas D01']['faune'], 1)} m²HE·an pour la "
            f"nidification ; un début en janvier reporte les plantations à novembre et coûte {e('Cas D02')} m²HE·an ; "
            f"l'abattage d'arbres âgés à gîtes en janvier ajoute {n(d['Cas D28']['faune'], 1)} m²HE·an que l'abattage "
            "en octobre évite.",
            f"- Substrat : la toiture de 8 cm coûte {e('Cas D03')} m²HE·an, celle de 30 cm en rend "
            f"{n(-(d['Cas D04']['cnat'] - RC['cnat']), 0)}.",
            f"- Sol : sur un sable, Cnat baisse de {n(-(d['Cas D07']['cnat'] - RC['cnat']), 0)} m²HE·an. L'état "
            "initial, sur le même sol, perd lui aussi, et davantage : la friche herbacée initiale est plus étendue "
            "que les milieux créés. Le sol pauvre pénalise le projet dans l'absolu (I_1 plus faible), pas face à "
            "l'état initial.",
            f"- Éclairage : la prairie éclairée toute la nuit en 4 000 K coûte {e('Cas D17')} m²HE·an ; éteinte à 23 h, "
            f"en 2 700 K, à 20 m, elle en rend {n(-(d['Cas D18']['cnat'] - RC['cnat']), 0)}.",
            f"- Gestion : sans plan, Cnat monte de {e('Cas D20')} ; un plan de trente ans le baisse de "
            f"{n(-(d['Cas D21']['cnat'] - RC['cnat']), 0)}, un plan de cinquante ans de "
            f"{n(-(d['Cas D22']['cnat'] - RC['cnat']), 0)}. L'abandon après le plan vaut mieux que la tonte d'une "
            "pelouse : la friche abandonnée garde plus de valeur que la pelouse (BKompV).",
            f"- Climat : d'une zone à l'autre, l'écart reste sous {n(max(abs(d[f'Cas D{i}']['cnat'] - RC['cnat']) for i in range(10, 17)), 0)} "
            "m²HE·an, parce que la végétation de chaque zone est jugée sur son propre climat ; un début en 2045 "
            f"décale la période vers un climat plus chaud et baisse Cnat de {n(-(d['Cas D24']['cnat'] - RC['cnat']), 0)} "
            "m²HE·an, l'état initial perdant davantage que le projet.",
            f"- Mare en zone H3 : sans bassin versant, elle s'assèche au printemps ; raccordée à 3 000 m² de prairie, "
            f"elle tient mieux (Cnat {n(d['Cas D26']['cnat'], 0)}) ; avec un fond étanche, elle reste en eau "
            f"(Cnat {n(d['Cas D27']['cnat'], 0)}, contre {n(d['Cas D25']['cnat'], 0)}).", '']
    for cas, r in rd:
        out += derouler(cas, r)
    print(ecrire('08_cas_validation.md', '\n'.join(out)))


if __name__ == '__main__':
    main()
