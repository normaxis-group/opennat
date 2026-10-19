# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 NORMATYS
"""Remplissage du RSNat à partir des entrées et des résultats (partie 1, chapitre 11 ; partie 7)."""
from __future__ import annotations

import hashlib
import os

from . import VERSION_METHODE
from . import numerique as nm
from . import rsnat

CLASSES = {'bon': 'bon', 'moyen': 'moyen', 'mauvais': 'mauvais', 'sans état': 'sans_etat'}


def _sans_vide(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}


def _serie(x, d=1) -> str:
    return ' '.join(f'{nm.scalaire(v):.{d}f}' for v in x)


def unite_entree(u: dict) -> dict:
    ecl = u.get('eclairage')
    d = dict(identifiant=u['id'], code_habitat=u['code'], position=u.get('position'), surface=u.get('surface'),
             epaisseur_substrat=u.get('epaisseur'), hauteur_facade=u.get('hauteur'), longueur=u.get('longueur'),
             largeur=u.get('largeur'), nombre_arbres=u.get('nombre_arbres'), classe_diametre=u.get('classe_diametre'),
             stade={'jeune': 'J', 'moyen': 'M', 'age': 'A'}.get(u.get('stade'), u.get('stade')),
             situation=u.get('situation'), tache=u.get('tache'),
             eclairage=ecl if isinstance(ecl, str) else None,
             Eclairage_Horaire=_sans_vide(dict(extinction=ecl.get('extinction'), rallumage=ecl.get('rallumage'),
                                               temperature_couleur=ecl.get('cct'),
                                               part_detection=ecl.get('taux_detection'))) if isinstance(ecl, dict) else None,
             distance_lumiere=ecl.get('distance') if isinstance(ecl, dict) else None,
             arrose=u.get('arrose'), texture_sol=u.get('texture'), profondeur_sol=u.get('profondeur_sol'),
             bassin_versant_impermeable=u.get('bassin_versant'), bassin_versant_permeable=u.get('bassin_versant_permeable'),
             profondeur_mare=u.get('profondeur'), fond_mare=u.get('fond'), gites=u.get('gites'),
             regime_gestion=u.get('gestion'), regime_apres_plan=u.get('apres_plan'),
             plan_gestion_annees=u.get('plan_gestion_annees'), niveau_sonore=u.get('niveau_sonore'),
             exposition_vitrage=u.get('exposition_vitrage'), alimentation_eau=u.get('alimentation'),
             statut=u.get('statut'), unite_liee=u.get('liee'), protection_chantier=u.get('protection'),
             alimentation_humide=u.get('alimentation_humide'))
    if u.get('criteres') or u.get('notes'):
        crit = [dict(code=k, reponse=v) for k, v in u.get('criteres', {}).items()]
        crit += [dict(code=f'indicateur_{k}', note=v) for k, v in u.get('notes', {}).items()]
        d['Critere_Collection'] = dict(Critere=crit)
    if u.get('score'):
        d['Score_Declare'] = _sans_vide(dict(u['score']))
    if u.get('renouvellements'):
        d['Renouvellement_Collection'] = dict(annee=list(u['renouvellements']))
    return _sans_vide(d)


def unite_resultat(u: dict, etat: str, taches: dict) -> dict:
    t = taches.get(u.get('tache'), {})
    bilans = []
    for n, b in (u.get('bilan') or {}).items():
        if b is None:
            continue
        bilans.append(_sans_vide(dict(niveau=n, indice_stress=b.get('IS'), indice_stress_reference=b.get('IS_ref'),
                                      facteur_hydrique=u['kW_niveaux'][n], arrosage=b.get('arrosage_mm'),
                                      assec_printemps=b.get('assec_precoce'))))
    d = dict(identifiant=u['id'], etat=etat, type=u['code'], nature_surface=u['nature'], coefficient_sol=u['c'],
             facteur_support=u['f_sol'], valeur_intrinseque=u['v'], score_etat=u['S'], facteur_etat=u['f'],
             classe_etat=CLASSES[u['classe']], multiplicateur_situation=u['m'], facteur_taille=t.get('k_taille'),
             facteur_connectivite=u['kC'], facteur_eclairage=u['kL'],
             fraction_nuit_eclairee=(u.get('lumiere') or {}).get('fraction'), facteur_nuisances=u['kN'],
             facteur_eau=u['kE'], valeur_habitat=u['VH'], valeur_maturite=u['V'], delai=u.get('d'),
             difficulte=u.get('D'), groupe_hydrique=u.get('groupe_hydrique'), reserve_utile=u.get('RU'),
             Bilan_Hydrique=bilans or None, mois_depart_maturation=u.get('mois_depart'),
             facteurs_hydriques=_serie(u['kW'], 4) if 'kW' in u else None,
             facteurs_gestion=_serie(u['f_gestion'], 4) if 'f_gestion' in u else None,
             trajectoire=_serie(u['traj']) if 'traj' in u else None,
             valeur_integree=sum(u['traj']) if 'traj' in u else None)
    return _sans_vide(d)


def construire(e: dict, resultats: list[dict], incertitude: dict | None, empreinte_tables: str, date: str,
               empreinte_rsee: str | None = None) -> dict:
    """Dictionnaire du RSNat ; `resultats` : un élément par variante (sortie de chaine.calculer)."""
    ctx, pa, ch = e['contexte'], e['parcelle'], e['chantier']
    projet = _sans_vide(dict(
        identifiant=e['projet']['identifiant'], nom=e['projet'].get('nom', e['projet']['identifiant']),
        adresse=e['projet'].get('adresse'), commune_insee=e['projet'].get('commune_insee'),
        zone_biogeographique=ctx['zone_biogeographique'], departement=ctx.get('departement'),
        altitude=ctx.get('altitude'), zone_climatique=ctx['zone_climatique'], texture_sol=ctx['sol']['texture'],
        profondeur_sol=ctx['sol']['profondeur'], annee_debut_chantier=ch['annee_debut'],
        mois_debut_chantier=ch['mois_debut'], mois_destruction=ch.get('mois_destruction'),
        plan_gestion_annees=e['gestion'].get('plan_annees'), typologie=ctx['typologie'],
        rsee_empreinte=empreinte_rsee, date_etude=e['projet'].get('date_etude', date)))
    batiments = []
    for i, b in enumerate(e['batiments'], 1):
        ges = [dict(phase=p, valeur=v) for p, v in b.get('ges', {}).items()]
        pol = [dict(code=int(c), phase=p, valeur=v) for c, par in b.get('pollution', {}).items() for p, v in par.items()]
        batiments.append(_sans_vide(dict(index=i, nom=b.get('nom'), sref=b.get('sref', 0.0),
                                         emprise_au_sol=b.get('emprise_au_sol', 0.0),
                                         duree_chantier=b.get('duree_chantier', 0.0),
                                         Ges_Collection=dict(Ges=ges or [dict(phase='A1-A3', valeur=0.0)]),
                                         Pollution_Collection=dict(Pollution=pol) if pol else None)))
    taches = [_sans_vide(dict(identifiant=t, surface_exterieure=i.get('exterieur'), connexion=i.get('connexion'),
                              distance_espace_naturel=i.get('distance_espace_naturel'),
                              surface_espace_naturel=i.get('surface_espace_naturel'), cloture=i.get('cloture')))
              for t, i in e['taches'].items()]
    variantes = []
    for v in e['variantes']:
        mat = v.get('materiaux', {})
        variantes.append(_sans_vide(dict(
            index=v['index'], nom=v['nom'], reference=bool(v.get('reference')),
            Unite_Collection=dict(Unite=[unite_entree(u) for u in v['unites']]),
            Bois_Collection=dict(Bois=[_sans_vide(dict(regime=b.get('regime', 'coupe_rase'), volume=b['volume'],
                                                       remplacements=b.get('remplacements'),
                                                       justification=b.get('justification')))
                                       for b in mat['bois']]) if mat.get('bois') else None,
            Granulats=_sans_vide(dict(mat['granulats'])) if mat.get('granulats') else None,
            Ouvrage_Pluvial_Collection=dict(Ouvrage_Pluvial=[dict(surface_drainee=o['surface_drainee'],
                                                                  infiltration_surface=bool(o.get('infiltration_surface')))
                                                             for o in v['ouvrages_pluviaux']]) if v.get('ouvrages_pluviaux') else None,
            Facade_Vitree_Collection=dict(Facade_Vitree=[dict(surface=f['surface'], traitee=bool(f.get('traitee')))
                                                         for f in v['facades_vitrees']]) if v.get('facades_vitrees') else None)))
    entree = _sans_vide(dict(
        Projet=projet,
        Parcelle=_sans_vide(dict(surface=pa['surface'], surface_vegetalisee_rsee=pa.get('surface_vegetalisee_rsee'),
                                 surface_impermeable_rsee=pa.get('surface_impermeable_rsee'),
                                 cbs_plu=ctx.get('cbs_plu'), pleine_terre_plu=ctx.get('pleine_terre_plu'))),
        Batiment_Collection=dict(Batiment=batiments) if batiments else None,
        Tache_Collection=dict(Tache=taches) if taches else None,
        Etat_Initial=dict(Unite_Collection=dict(Unite=[unite_entree(u) for u in e['etat_initial']])),
        Variante_Collection=dict(Variante=variantes)))
    sorties = []
    for v, r in zip(e['variantes'], resultats):
        et = r['etapes']
        it, ind, bn = et['E3']['integration'], et['E3']['indicateurs'], et['E3']['bnat']
        taches_res = dict(et['C']['taches_initiales'], **et['C']['taches_projet'])
        unites = [unite_resultat(u, 'initial', et['C']['taches_initiales']) for u in r['initial']] + \
                 [unite_resultat(u, 'projet', et['C']['taches_projet']) for u in r['projet']]
        g = et['G']
        inc = (incertitude or {}).get(v['index'])
        sorties.append(_sans_vide(dict(
            index=v['index'],
            Contexte=_sans_vide(dict(part_emprise=et['E1']['part_emprise'], bnat_min=et['E1']['bnat_min'],
                                     pleine_terre_min=et['E1']['pleine_terre_min'],
                                     multiplicateur_delai=et['E1']['k_delai'])),
            Fermeture_Collection=dict(Fermeture=[dict(etat=k, somme=f['somme'], ecart=f['ecart'], conforme=f['conforme'])
                                                 for k, f in et['E2']['fermeture'].items()]),
            Unite_Resultat_Collection=dict(Unite_Resultat=unites),
            Site=_sans_vide(dict(
                valeur_initiale=it['v0'], i0=it['i0'], i1=it['i1'], i0_30=it['i0_30'], i1_30=it['i1_30'],
                dette_maturite=it['dm'], supplement_destruction=et['T']['supplement_destruction'],
                arrosage_annuel=et['E3']['arrosage_m3_an'], rang_plantation=et['T']['rang_plantation'],
                annees_periode=f'{et["T"]["annees"][0]} {et["T"]["annees"][1]}',
                trajectoire_reference=_serie(it['ref']), trajectoire_site=_serie(it['site']),
                pleine_terre=et['S']['pleine_terre'], pleine_terre_initiale=et['S']['pleine_terre_initiale'],
                impermeable_initial=et['S']['impermeable_initial'], impermeable_projet=et['S']['impermeable_projet'],
                impermeabilisation_nette=et['S']['impermeabilisation_nette'], part_pluvial_infiltre=et['E']['p_inf'],
                surface_vitree_non_traitee=et['N']['surface_vitree_non_traitee'])),
            Materiaux=_sans_vide(dict(
                facteur_climat=g['CF'], inat_climat=g['inat_clim'],
                Inat_Climat_Phase=[dict(phase=p, valeur=x) for p, x in g['inat_clim_phase'].items()] or None,
                inat_bois=g['inat_bois'], inat_carrieres=g['inat_carr'], inat_pollution=g['inat_pol'],
                Pollution_Resultat=[dict(code=int(c), valeur=x, valeur_convertie=g['inat_pol_detail'][c])
                                    for c, x in g['pollution'].items() if nm.scalaire(x)] or None)),
            Indicateurs=_sans_vide(dict(
                cnat=ind['cnat'], cnat_moyen=ind['cnat_moyen'], cnat_relatif=ind['cnat_relatif'], cnat_30=ind['cnat_30'],
                inat=ind['inat'], snat=ind['snat'], bnat=bn['bnat'], cbs=bn['cbs'],
                cnat_par_m2_parcelle=ind['cnat_par_m2_parcelle'], inat_par_m2_sref=ind['inat_par_m2_sref'])),
            Incertitude=inc,
            Conformite=_sans_vide(dict(bnat_conforme=et['E5']['bnat_conforme'],
                                       pleine_terre_conforme=et['E5']['pleine_terre_conforme'],
                                       plu_conforme=et['E5']['plu_conforme'], niveau_cnat=et['E5']['niveau_cnat'])))))
    ref = next(i for i, v in enumerate(e['variantes']) if v.get('reference'))
    rr = resultats[ref]['etapes']
    mention = None
    if rr['E5']['plu_conforme'] is False:
        mention = (f'Le projet ne respecte pas le minimum du PLU (coefficient de biotope {ctx.get("cbs_plu")}, pleine '
                   f'terre {ctx.get("pleine_terre_plu")}) : l\'attestation ne conclut pas à la conformité (convention C-P1).')
    permis = _sans_vide(dict(variante=e['variantes'][ref]['index'], bnat=rr['E3']['bnat']['bnat'],
                             bnat_min=rr['E1']['bnat_min'], pleine_terre=rr['S']['pleine_terre'],
                             pleine_terre_min=rr['E1']['pleine_terre_min'], cbs_plu=ctx.get('cbs_plu'),
                             pleine_terre_plu=ctx.get('pleine_terre_plu'),
                             conforme=rr['E5']['attestation_permis_conforme'], mention=mention))
    d = dict(version_methode=VERSION_METHODE, version_donnees=empreinte_tables,
             graine=e['options']['graine'], date_calcul=date, Entree_Projet=entree,
             Sortie_Projet=dict(Variante_Resultat=sorties), Attestation_Permis=permis)
    el_e = rsnat.vers_xml(dict(d, Empreinte=dict(entrees='', sorties='')))
    d['Empreinte'] = dict(entrees=rsnat.empreinte_element(el_e.find('Entree_Projet')),
                          sorties=rsnat.empreinte_element(el_e.find('Sortie_Projet')))
    return d


def empreinte_fichier(chemin: str) -> str:
    h = hashlib.sha256()
    with open(chemin, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def ecrire(d: dict, dossier: str) -> dict:
    """Écrit `rsnat.xml` et `rsnat.json` et les valide contre leurs schémas (exigence E9)."""
    import json
    from lxml import etree
    el = rsnat.vers_xml(d)
    err_x = rsnat.valider_xml(el)
    doc = rsnat.vers_json(d)
    err_j = rsnat.valider_json(doc)
    etree.ElementTree(el).write(os.path.join(dossier, 'rsnat.xml'), pretty_print=True, xml_declaration=True,
                                encoding='UTF-8')
    with open(os.path.join(dossier, 'rsnat.json'), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    return dict(xml=err_x, json=err_j)
