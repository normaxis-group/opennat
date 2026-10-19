# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 IRICE
"""Résumé des résultats d'un calcul pour l'utilitaire et la fiche de synthèse (valeurs centrales, intervalles)."""
from __future__ import annotations

from .. import VERSION_METHODE, VERSION_MOTEUR
from .. import numerique as nm

ETAPES = ('E1', 'E2', 'S', 'H', 'C', 'N', 'E', 'W', 'T', 'G', 'E3', 'E5')


def _f(x):
    return None if x is None else nm.scalaire(x)


def resumer(r: dict) -> dict:
    e = r['entrees']
    variantes = []
    for v, res in zip(e['variantes'], r['resultats']):
        et = res['etapes']
        it, ind, bn, g = et['E3']['integration'], et['E3']['indicateurs'], et['E3']['bnat'], et['G']
        a0, a1 = et['T']['annees']
        unites = []
        for etat, liste in (('initial', res['initial']), ('projet', res['projet'])):
            for u in liste:
                kw = u.get('kW') or []
                unites.append(dict(
                    etat=etat, id=u['id'], code=u['code'], position=u['position'], surface=_f(u['surface']),
                    nature=u['nature'], classe=u['classe'], S=_f(u['S']), f=_f(u['f']), v=_f(u['v']), kC=_f(u['kC']),
                    kL=_f(u['kL']), kN=_f(u['kN']), kE=_f(u['kE']), V=_f(u['V']),
                    groupe=u.get('groupe_hydrique'), RU=_f(u.get('RU')),
                    kW={n: _f(k) for n, k in u['kW_niveaux'].items()},
                    kW_moyen=_f(sum(kw) / len(kw)) if kw else None,
                    f_gestion_fin=_f(u['f_gestion'][-1]) if 'f_gestion' in u else None,
                    statut=u.get('statut', 'creee') if etat == 'projet' else None,
                    delai=_f(u.get('d')) if etat == 'projet' else None,
                    depart=_f(u.get('mois_depart')) if etat == 'projet' else None,
                    integree=_f(sum(u['traj'])) if 'traj' in u else _f(u['V'] * len(it['ref']))))
        variantes.append(dict(
            index=v['index'], nom=v['nom'], reference=bool(v.get('reference')),
            indicateurs=dict(bnat=_f(bn['bnat']), cbs=_f(bn['cbs']), pleine_terre=_f(et['S']['pleine_terre']),
                             cnat=_f(ind['cnat']), cnat_relatif=_f(ind['cnat_relatif']), cnat_30=_f(ind['cnat_30']),
                             cnat_moyen=_f(ind['cnat_moyen']), inat=_f(ind['inat']), snat=_f(ind['snat']),
                             niveau=int(nm.scalaire(et['E5']['niveau_cnat']))),
            seuils=dict(bnat_min=_f(et['E1']['bnat_min']), pleine_terre_min=_f(et['E1']['pleine_terre_min']),
                        bnat_conforme=et['E5']['bnat_conforme'], pleine_terre_conforme=et['E5']['pleine_terre_conforme'],
                        plu_conforme=et['E5']['plu_conforme'], permis=et['E5']['attestation_permis_conforme'],
                        part_emprise=_f(et['E1']['part_emprise']), classe=et['E1']['classe_seuil']),
            site=dict(v0=_f(it['v0']), i0=_f(it['i0']), i1=_f(it['i1']), dette=_f(it['dm']),
                      destruction=_f(et['T']['supplement_destruction']), detail_destruction=et['T']['destruction'],
                      arrosage=_f(et['E3']['arrosage_m3_an']), impermeabilisation=_f(et['S']['impermeabilisation_nette']),
                      a_inf=_f(et['E']['a_inf']), rang_plantation=_f(et['T']['rang_plantation']),
                      chantier=et['T']['chantier'], plan=et['T']['plan_gestion_annees']),
            materiaux=dict(sref=_f(g['sref']), CF=_f(g['CF']), inat_clim=_f(g['inat_clim']), inat_bois=_f(g['inat_bois']),
                           inat_carr=_f(g['inat_carr']), inat_pol=_f(g['inat_pol']), par_phase={p: _f(x) for p, x in g['inat_clim_phase'].items()},
                           pollution={c: _f(x) for c, x in g['pollution'].items()}),
            trajectoire=dict(annees=list(range(a0, a1 + 1)), site=[_f(x) for x in it['site']],
                             reference=[_f(x) for x in it['ref']]),
            unites=unites,
            incertitude=(r.get('incertitude') or {}).get(v['index'])))
    d = r['rsnat']
    return dict(projet=dict(identifiant=e['projet']['identifiant'], nom=e['projet'].get('nom'),
                            zone_climatique=e['contexte']['zone_climatique'], typologie=e['contexte']['typologie'],
                            zone_biogeographique=e['contexte']['zone_biogeographique'],
                            parcelle=e['parcelle']['surface']),
                versions=dict(methode=VERSION_METHODE, moteur=VERSION_MOTEUR, donnees=d['version_donnees'],
                              graine=d['graine'], date=d['date_calcul']),
                empreinte=d['Empreinte'], dossier=r['dossier'], journal=r['journal'],
                erreurs_schema=r['erreurs_schema'], variantes=variantes)
