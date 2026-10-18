# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Vérification arithmétique de l'exemple de l'annexe C de la méthode OpenNAT.

Ce script n'est pas le moteur (lot 2). Il refait, équation par équation, le calcul que
l'annexe C déroule à la main, en lisant les coefficients dans donnees/, pour que les
nombres imprimés dans le texte de la méthode soient exacts. Il imprime chaque résultat
intermédiaire dans l'ordre de l'annexe.
"""
import csv
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def table(nom):
    with open(os.path.join(RACINE, 'donnees', nom), encoding='utf-8') as f:
        return {(r['cle'], r['parametre']): float(r['valeur'])
                for r in csv.DictReader(f, delimiter=';')}


H, SOL, CTX, CON, NUI, MAT = (table(n) for n in ('habitats.csv', 'sols.csv', 'contexte.csv',
                                                  'connectivite.csv', 'nuisances.csv',
                                                  'materiaux.csv'))
N = int(CTX[('*', 'periode_reference')])
S_P = 2000.0


def k_taille(a):                                                       # équation C2
    z, aref = CON[('*', 'exposant_aire_especes')], CON[('*', 'surface_reference')]
    kmin = CON[('*', 'facteur_taille_minimum')]
    return min(1.0, max(kmin, (a / aref) ** z))


def f_etat(ok, n, essentiel_echoue=False):                             # équations H2 et H3
    s = ok / n
    if essentiel_echoue:
        s = min(s, 0.5)
    return s, 0.5 + 0.5 * s


def classe(s):
    return 'bon' if s >= 0.85 else ('moyen' if s >= 0.65 else 'mauvais')


print('== Étape E2 : fermeture')
print('initial', 1200 + 600 + 200, 'projet', 700 + 300 + 150 + 450 + 320 + 80)

print('\n== État initial, modules H et C')
kt1 = k_taille(1400)
print(f'k_taille(1400 m²) = {kt1:.4f}')
ini = []
s, f = f_etat(3, 4, essentiel_echoue=True)
ini.append(('U0-1 VB.8 friche herbacée', 1200, H[('VB.8', 'valeur_intrinseque')], s, f, kt1))
ini.append(('U0-2 VB.2 enrobé', 600, H[('VB.2', 'valeur_intrinseque')], None, 1.0, 1.0))
s, f = f_etat(2, 5)
ini.append(('U0-3 VB.9 friche arbustive', 200, H[('VB.9', 'valeur_intrinseque')], s, f, kt1))
s, f = f_etat(5, 6)
ini.append(('U0-4 VB.18a deux arbres', 100, H[('VB.18a', 'valeur_intrinseque_stade_M')], s, f, kt1))
v0 = 0
for nom, a, v, s, f, k in ini:
    vh = a * v * f                                                     # équation H4 (f_sol = m_sit = 1)
    vu = vh * k                                                        # équation H5 (k_N = k_E = 1)
    v0 += vu
    print(f'{nom:30} A={a:6.0f} v={v:.4f} S={s if s is None else round(s, 3)} f={f:.4f} '
          f'VH={vh:8.2f} kC={k:.4f} V={vu:8.2f}')
print(f'V0 site = {v0:.2f} m²HE, I0 = {N} x V0 = {N * v0:.1f} m²HE·an')

print('\n== État projet, modules H, C, N')
kt2, kt3 = k_taille(850), k_taille(500)
print(f'k_taille(850 m²) = {kt2:.4f}   k_taille(500 m²) = {kt3:.4f}')
klum = NUI[('lumiere_conforme', 'facteur_lumiere')]
pro = []
#            nom, A, v, S, f, kC, kN, statut, délai, difficulté
pro.append(('U1-3 VB.3 stabilisé', 150, H[('VB.3', 'valeur_intrinseque')], None, 1.0, 1.0, 1.0,
            'cree', 0.0, 1.0))
s, f = f_etat(4, 6)
pro.append(('U1-4 VB.26 prairie', 450, H[('VB.26', 'valeur_intrinseque')], s, f, kt2, klum,
            'cree', H[('VB.26', f'delai_maturite_{classe(s)}')], H[('VB.26', 'difficulte_creation')]))
s, f = f_etat(2, 3)
pro.append(('U1-5 VB.7 jardins', 320, H[('VB.7', 'valeur_intrinseque')], s, f, kt2, 1.0,
            'cree', H[('VB.7', 'delai_maturite_sans_etat')], H[('VB.7', 'difficulte_creation')]))
s, f = f_etat(6, 8)
pro.append(('U1-6 FA.3 haie', 80, H[('FA.3', 'valeur_intrinseque_stade_M')], s, f, kt2, 1.0,
            'cree', H[('FA.3', f'delai_maturite_{classe(s)}')], H[('FA.3', 'difficulte_creation')]))
s, f = f_etat(5, 6)
pro.append(('U1-7 VB.18a arbres conservés', 100, H[('VB.18a', 'valeur_intrinseque_stade_M')], s, f,
            kt2, 1.0, 'conserve', 0.0, 1.0))
s, f = f_etat(4, 4)
pro.append(('U1-8 VB.12 toiture biodiverse', 500, H[('VB.12', 'valeur_intrinseque')], s, f, kt3,
            1.0, 'cree', H[('VB.12', f'delai_maturite_{classe(s)}')],
            H[('VB.12', 'difficulte_creation')]))
cible = {}
for nom, a, v, s, f, kc, kn, statut, d, D in pro:
    vu = a * v * f * kc * kn
    cible[nom] = (vu, statut, d, D)
    print(f'{nom:30} A={a:5.0f} v={v:.4f} S={s if s is None else round(s, 3)} f={f:.4f} '
          f'kC={kc:.4f} kN={kn:.2f} V={vu:8.2f} statut={statut} d={d:g} D={D:g}')

print('\n== Module T')
d_ch = 1.5
traj = []
for t in range(1, N + 1):
    phi = min(1.0, max(0.0, d_ch - (t - 1)))                          # équation T1
    tau = t - d_ch                                                     # années depuis la fin du chantier
    tot = 0.0
    for nom, (vu, statut, d, D) in cible.items():
        if statut == 'conserve':
            tot += vu                                                  # équation T2, protection prévue
        else:
            g = 0.0 if tau <= 0 else (1.0 if d == 0 else min(1.0, tau / d))   # équation T3
            tot += D * vu * g
    traj.append(tot)
for t in (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 20, 30, 50):
    print(f'année {t:2d} : V1 = {traj[t - 1]:8.2f}')
i1, i1_30 = sum(traj), sum(traj[:30])
print(f'I1 = {i1:.1f}   I1(30 ans) = {i1_30:.1f}')
v_cible = sum(D * vu for vu, statut, d, D in cible.values())
dette = sum(v_cible - x for x in traj)
print(f'valeur projet à maturité = {v_cible:.2f}, dette de maturité = {dette:.1f}')
cnat = N * v0 - i1                                                     # équation A1
print(f'Cnat = {N * v0:.1f} - {i1:.1f} = {cnat:.1f} m²HE·an, Cnat moyen = {cnat / N:.2f} m²HE')
print(f'Cnat(30 ans) = {30 * v0 - i1_30:.1f}')
print(f'Cnat relatif = {cnat / (N * v0):.3f}')

print('\n== Module G')
cf = MAT[('climat', 'facteur_caracterisation')]
cf_calc = (MAT[('climat', 'surface_terres_emergees_hors_glaces')]
           * (1 - MAT[('climat', 'part_cultures_infrastructures')])
           * MAT[('climat', 'perte_msa_par_degre')] / MAT[('climat', 'facteur_retard_reponse')]
           * MAT[('climat', 'tcre')])
print(f'CF recalculé = {cf_calc:.4e} (table : {cf:.4e})')
sref = 1400.0
ges = {'phase_A1_A5': 350.0 + 120.0, 'phase_B': 400.0, 'phase_C': 55.0, 'phase_D': -40.0}
somme = sum(g * MAT[(p, 'annees_persistance')] for p, g in ges.items())
inat_clim = cf * sref * somme                                          # équation G2
print(f'somme GES x années = {somme:.0f} kg·an/m², Inat climat = {inat_clim:.1f}')
q_bois = 30.0
occ = 10000 / MAT[('foret', 'production_biologique')] * MAT[('foret', 'rapport_bois_rond_produit')]
inat_bois = q_bois * occ * (1 - MAT[('foret_coupe_rase', 'msa_usage')])   # équation G3
print(f'occupation bois = {occ:.1f} m²·an/m³, Inat bois = {inat_bois:.1f}')
m_gran = 1800.0
inat_carr = m_gran * MAT[('carriere', 'occupation_par_tonne')] * (1 - MAT[('carriere', 'msa_usage')])
print(f'Inat granulats = {inat_carr:.1f}')
inat = inat_clim + inat_bois + inat_carr
print(f'Inat = {inat:.1f} m²HE·an, par m² de Sref = {inat / sref:.2f}')
snat = -(cnat + inat)
print(f'Snat = {snat:.1f} m²HE·an')

print('\n== Bnat')
c = {k[0]: v for k, v in SOL.items()}
num = 700 * c['S01'] + 300 * c['S01'] + 150 * c['S02'] + 850 * c['S08'] + 500 * c['S05']
print(f'numérateur = {num:.1f}, Bnat = {100 * num / S_P:.1f}, pleine terre = {850 / S_P:.3f}, '
      f'emprise = {700 / S_P:.2f}')
