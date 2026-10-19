// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2026 IRICE
// Utilitaire OpenNAT : saisie du fichier projet, contrôles en direct, calcul, résultats, fiche et RSNat.
'use strict';

const S = { projet: null, ref: null, onglet: 'projet', vc: 0, sel: null, controle: null, calcul: null, etatCalcul: null,
  resultats: null, rv: 0, modifie: false, minuterie: null };
const ONGLETS = [
  { groupe: 'Saisie' },
  { id: 'projet', n: 1, nom: 'Projet et contexte' }, { id: 'initial', n: 2, nom: 'État initial' },
  { id: 'etatProjet', n: 3, nom: 'État projet' }, { id: 'sol', n: 4, nom: 'Sol' },
  { id: 'connectivite', n: 5, nom: 'Connectivité' }, { id: 'nuisances', n: 6, nom: 'Nuisances' },
  { id: 'eau', n: 7, nom: 'Eau' }, { id: 'materiaux', n: 8, nom: 'Matériaux' }, { id: 'variantes', n: 9, nom: 'Variantes' },
  { groupe: 'Calcul et résultats' },
  { id: 'calcul', nom: 'Calcul' }, { id: 'resultats', nom: 'Résultats' }, { id: 'comparaison', nom: 'Comparaison des variantes' },
  { id: 'fichiers', nom: 'Résultats intermédiaires' }, { id: 'fiche', nom: 'Fiche et RSNat' },
];
const ETAPES = ['E1', 'E2', 'S', 'H', 'C', 'N', 'E', 'W', 'T', 'G', 'E3', 'E5'];
const NOMS_ETAPES = { E1: 'E1 contexte', E2: 'E2 prétraitement', S: 'S sol', H: 'H habitats', C: 'C connectivité',
  N: 'N nuisances', E: 'E eau', W: 'W bilan hydrique', T: 'T temps', G: 'G biodiversité grise', E3: 'E3 agrégation',
  E5: 'E5 conformité', E4: 'E4 incertitude', RSNat: 'RSNat' };
const NIVEAUX = { 0: 'perte nette', 1: 'absence de perte nette', 2: 'gain net' };
const MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
const LIB = {
  sol_pleine_terre: 'sol, pleine terre', sol_sur_dalle: 'sol sur dalle', hors_sol_toiture: 'toiture', hors_sol_facade: 'façade',
  eau: 'eau', arbre: 'arbre', lineaire: 'linéaire', reservoir: 'réservoir', corridor: 'corridor', hors_trame: 'hors trame',
  conservee: 'conservée', creee: 'créée', amelioree: 'améliorée', naturelle: 'naturelle', artificielle: 'artificielle',
  etanche: 'étanche', argile: 'argileux', naturel: 'naturel', courante: 'gestion courante', abandon: 'abandon',
  plan: 'plan de gestion', petit: 'petit', moyen: 'moyen', grand: 'grand', tres_grand: 'très grand', J: 'jeune', M: 'moyen',
  A: 'âgé', continentale: 'continentale', atlantique: 'atlantique', mediterraneenne: 'méditerranéenne', alpine: 'alpine',
  logement: 'logement', tertiaire: 'tertiaire', industrie: 'industrie', amenagement: 'aménagement', forte: 'forte',
  moyenne: 'moyenne', faible: 'faible', aucune: 'aucune', permeable: 'perméable', nappe: 'nappe ou cours d\'eau', pluie: 'pluie',
  plantation: 'plantation', coupe_rase: 'coupe rase', coupe_selective: 'coupe sélective', faible_impact: 'faible impact',
  limon: 'limon', sable: 'sable', sable_limoneux: 'sable limoneux', limon_sableux: 'limon sableux', limon_silteux: 'limon silteux',
  silt: 'silt', limon_argilo_silteux: 'limon argilo-silteux', argile_silteuse: 'argile silteuse',
};

// ------------------------------------------------------------------ outils
const LARGEURS = { text: 90, number: 90, int: 70, select: 120, bool: 60 };
const $ = (s, r = document) => r.querySelector(s);
function el(tag, attrs = {}, ...enfants) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === undefined || v === null || v === false) continue;
    if (k === 'class') e.className = v;
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else if (k === 'html') e.innerHTML = v;
    else e.setAttribute(k, v === true ? '' : v);
  }
  for (const c of enfants.flat()) if (c !== null && c !== undefined && c !== false) e.append(c instanceof Node ? c : document.createTextNode(c));
  return e;
}
const nb = (x, d = 1) => {
  if (x === null || x === undefined || Number.isNaN(x)) return 'n. d.';
  const v = Math.abs(x) < 0.5 * Math.pow(10, -d) ? 0 : Number(x);
  return v.toLocaleString('fr-FR', { minimumFractionDigits: d, maximumFractionDigits: d });
};
const pct = (x, d = 1) => (x === null || x === undefined) ? 'n. d.' : nb(100 * x, d) + ' %';
const lib = v => LIB[v] || v;
const copie = x => JSON.parse(JSON.stringify(x));
async function api(chemin, options = {}) {
  const r = await fetch(chemin, options);
  const t = r.headers.get('Content-Type') || '';
  const corps = t.includes('json') ? await r.json() : await r.text();
  if (!r.ok) throw new Error((corps && corps.erreur) || r.statusText);
  return corps;
}
const post = (chemin, corps, brut = false) => api(chemin, { method: 'POST', body: brut ? corps : JSON.stringify(corps),
  headers: brut ? {} : { 'Content-Type': 'application/json' } });
function telecharger(nom, contenu, type = 'application/json') {
  const a = el('a', { href: URL.createObjectURL(new Blob([contenu], { type })), download: nom });
  document.body.append(a); a.click(); a.remove();
}

// ------------------------------------------------------------------ projet
function projetVide() {
  const aujourdhui = new Date().toISOString().slice(0, 10);
  return { format: 'OpenNAT projet 1', projet: { identifiant: 'nouveau-projet', nom: 'Nouveau projet', date_etude: aujourdhui },
    contexte: { zone_biogeographique: 'continentale', typologie: 'logement', zone_climatique: 'H1a', sol: { texture: 'limon', profondeur: 1 } },
    parcelle: { surface: 1000 }, chantier: { annee_debut: 2027, mois_debut: 9 }, gestion: { plan_annees: 10 }, taches: {},
    batiments: [], etat_initial: [], variantes: [{ nom: 'Projet', reference: true, unites: [] }], options: { tirages: S.ref ? S.ref.tirages_defaut : 1000 } };
}
function charger(p) {
  S.projet = p; S.vc = 0; S.sel = null; S.resultats = null; S.calcul = null; S.etatCalcul = null; S.modifie = false;
  p.contexte = p.contexte || {}; p.contexte.sol = p.contexte.sol || {}; p.taches = p.taches || {};
  p.batiments = p.batiments || []; p.chantier = p.chantier || {}; p.gestion = p.gestion || {}; p.options = p.options || {};
  fermerTiroir(); afficher(); valider();
}
function modifie() {
  S.modifie = true;
  $('#nomProjet').textContent = (S.projet.projet.nom || S.projet.projet.identifiant) + ' (modifié)';
  clearTimeout(S.minuterie); S.minuterie = setTimeout(valider, 350);
}
async function valider() {
  try { S.controle = await post('/api/valider', S.projet); } catch (x) { S.controle = { erreurs: [String(x.message)], fermeture: {}, unites: {}, avertissements: [] }; }
  afficherControles();
  if (S.onglet === 'calcul' && !S.calcul) afficher();
}
const variante = () => S.projet.variantes[Math.min(S.vc, S.projet.variantes.length - 1)];
function habitat(code) { return S.ref.habitats.find(h => h.code === code); }
function controlesOk() {
  const c = S.controle; if (!c) return false;
  return !c.erreurs.length && !Object.keys(c.unites).length && Object.values(c.fermeture).every(f => f.conforme);
}

// ------------------------------------------------------------------ champs liés
function setVal(obj, cle, v) {
  if (v === '' || v === null || v === undefined || (typeof v === 'number' && Number.isNaN(v))) delete obj[cle]; else obj[cle] = v;
}
function entree(obj, cle, type, opts = {}) {
  const val = obj[cle];
  let e;
  const changer = v => { setVal(obj, cle, v); if (opts.apres) opts.apres(v); modifie(); if (opts.reafficher) afficher(); };
  if (type === 'select') {
    e = el('select', { onchange: ev => changer(ev.target.value) },
      opts.vide !== false ? el('option', { value: '' }, opts.vide || '') : null,
      (opts.options || []).map(o => el('option', { value: o, selected: String(val) === String(o) }, opts.libelles ? opts.libelles(o) : lib(o))));
  } else if (type === 'bool') {
    e = el('input', { type: 'checkbox', checked: !!val, onchange: ev => changer(ev.target.checked ? true : undefined) });
  } else if (type === 'number' || type === 'int') {
    e = el('input', { type: 'number', step: opts.step || (type === 'int' ? 1 : 'any'), min: opts.min, max: opts.max, value: val ?? '',
      placeholder: opts.placeholder || '', onchange: ev => changer(ev.target.value === '' ? undefined : (type === 'int' ? parseInt(ev.target.value, 10) : parseFloat(ev.target.value))) });
  } else {
    e = el('input', { type: 'text', value: val ?? '', list: opts.liste, placeholder: opts.placeholder || '',
      onchange: ev => changer(ev.target.value.trim()) });
  }
  return e;
}
function champ(obj, cle, libelle, type = 'text', opts = {}) {
  return el('div', { class: 'champ' }, el('label', {}, libelle), entree(obj, cle, type, opts), opts.aide ? el('div', { class: 'aide' }, opts.aide) : null);
}

// ------------------------------------------------------------------ affichage général
function afficherOnglets() {
  const nav = $('#onglets'); nav.innerHTML = '';
  for (const o of ONGLETS) {
    if (o.groupe) { nav.append(el('div', { class: 'groupe' }, o.groupe)); continue; }
    nav.append(el('a', { href: '#' + o.id, class: S.onglet === o.id ? 'actif' : '', onclick: ev => { ev.preventDefault(); aller(o.id); } },
      o.n ? el('span', { class: 'num' }, String(o.n)) : null, o.nom));
  }
}
function aller(id) { S.onglet = id; fermerTiroir(); afficher(); }
function afficher() {
  afficherOnglets();
  $('#nomProjet').textContent = (S.projet.projet.nom || S.projet.projet.identifiant) + (S.modifie ? ' (modifié)' : '');
  const m = $('#contenu'); m.innerHTML = '';
  const f = { projet: ongletProjet, initial: () => ongletUnites('initial'), etatProjet: () => ongletUnites('projet'),
    sol: ongletSol, connectivite: ongletConnectivite, nuisances: ongletNuisances, eau: ongletEau, materiaux: ongletMateriaux,
    variantes: ongletVariantes, calcul: ongletCalcul, resultats: ongletResultats, comparaison: ongletComparaison,
    fichiers: ongletFichiers, fiche: ongletFiche }[S.onglet];
  m.append(...[].concat(f()).filter(x => x !== null && x !== undefined && x !== false));
}
function afficherControles() {
  const z = $('#etatControles'); z.innerHTML = ''; const c = S.controle; if (!c) return;
  const ferm = Object.entries(c.fermeture);
  z.append(el('h4', {}, 'Fermeture des surfaces (fiche A03)'));
  if (!ferm.length) z.append(el('div', { class: 'note' }, 'Surface de parcelle à saisir.'));
  for (const [nom, f] of ferm)
    z.append(el('div', { class: 'ligne' }, el('span', { class: 'pastille ' + (f.conforme ? 'ok' : 'ko') }, f.conforme ? 'fermé' : 'écart'),
      `${nom} : ${nb(f.somme, 0)} m² au sol, écart ${nb(f.ecart, 0)} m²` + (f.conforme ? '' : ` (tolérance ${nb(f.tolerance, 0)} m²)`)));
  const err = [...c.erreurs, ...Object.entries(c.unites).flatMap(([k, l]) => l.map(x => `${k}, ${x}`))];
  z.append(el('h4', {}, 'Saisie'));
  z.append(err.length ? el('ul', { class: 'erreurs' }, err.slice(0, 40).map(x => el('li', {}, traduire(x)))) :
    el('div', {}, el('span', { class: 'pastille ok' }, 'complète'), ' champs obligatoires et unités valides'));
  if (c.avertissements.length) z.append(el('ul', { class: 'erreurs avert' }, c.avertissements.map(x => el('li', {}, x))));
  z.append(el('h4', {}, 'Calcul'), el('div', {}, el('span', { class: 'pastille ' + (controlesOk() ? 'ok' : 'neutre') },
    controlesOk() ? 'prêt' : 'à compléter')));
}
const traduire = x => x.replace(/^\$\.?/, '').replace(/\$\./g, '');

// ------------------------------------------------------------------ onglet 1 : projet et contexte
function ongletProjet() {
  const p = S.projet, c = p.contexte, ch = p.chantier;
  const enums = S.ref.enums;
  return [
    el('h2', {}, 'Projet et contexte'),
    el('div', { class: 'carte' }, el('h3', {}, 'Identification'), el('div', { class: 'grille' },
      champ(p.projet, 'identifiant', 'Identifiant du projet'), champ(p.projet, 'nom', 'Nom de l\'opération'),
      champ(p.projet, 'adresse', 'Adresse'), champ(p.projet, 'commune_insee', 'Code INSEE de la commune'),
      champ(p.projet, 'date_etude', 'Date de l\'étude', 'text', { placeholder: 'AAAA-MM-JJ' }))),
    el('div', { class: 'carte' }, el('h3', {}, 'Reprise d\'un RSEE (fiche A05)'),
      el('p', { class: 'note' }, 'Le RSEE de l\'étude RE2020 fournit la parcelle, les bâtiments (S_ref, emprise, durée du chantier), les indicateurs d\'ACV des composants et du chantier, la zone climatique, le département et l\'altitude. Le fichier est lu puis oublié : rien n\'est conservé.'),
      el('input', { type: 'file', accept: '.xml', onchange: ev => importerRsee(ev.target.files[0]) }), el('div', { id: 'rseeRetour', class: 'note' })),
    el('div', { class: 'carte' }, el('h3', {}, 'Contexte'), el('div', { class: 'grille' },
      champ(c, 'zone_biogeographique', 'Zone biogéographique', 'select', { options: enums.zone_biogeographique, vide: false }),
      champ(c, 'typologie', 'Typologie', 'select', { options: enums.typologie, vide: false }),
      champ(c, 'zone_climatique', 'Zone climatique RE2020', 'select', { options: enums.zone_climatique, vide: false, libelles: o => o }),
      champ(c, 'departement', 'Département'), champ(c, 'altitude', 'Altitude du site (m)', 'number'),
      champ(c, 'cbs_plu', 'Coefficient de biotope du PLU', 'number', { step: 0.01, aide: 'facultatif, de 0 à 1' }),
      champ(c, 'pleine_terre_plu', 'Pleine terre imposée par le PLU', 'number', { step: 0.01, aide: 'facultatif, de 0 à 1' }),
      champ(c, 'k_delai_etude', 'Étude de sensibilité : multiplicateur des délais', 'number', { step: 0.05, aide: 'facultatif ; 1 par défaut (cas 8c du banc)' }))),
    el('div', { class: 'carte' }, el('h3', {}, 'Parcelle'), el('div', { class: 'grille' },
      champ(p.parcelle, 'surface', 'Surface de la parcelle (m²)', 'number'),
      champ(p.parcelle, 'emprise', 'Emprise du bâti (m²)', 'number', { aide: 'quand aucun bâtiment n\'est décrit' }))),
    el('div', { class: 'carte' }, el('h3', {}, 'Chantier et gestion (fiches A55 à A58)'), el('div', { class: 'grille' },
      champ(ch, 'annee_debut', 'Année de début du chantier', 'int'),
      champ(ch, 'mois_debut', 'Mois de début', 'select', { options: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], libelles: m => MOIS[m - 1], vide: false, apres: v => ch.mois_debut = parseInt(v, 10) }),
      champ(ch, 'duree_mois', 'Durée du chantier (mois)', 'number', { aide: 'à défaut, celle des bâtiments' }),
      champ(ch, 'mois_destruction', 'Mois des défrichements et abattages', 'select', { options: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], libelles: m => MOIS[m - 1], vide: 'premier mois du chantier', apres: v => { if (v) ch.mois_destruction = parseInt(v, 10); } }),
      champ(p.gestion, 'plan_annees', 'Plan de gestion écologique (années)', 'number', { aide: '0 : gestion courante dès la livraison (C-M3)' }))),
    el('div', { class: 'carte' }, el('h3', {}, 'Bâtiments et indicateurs d\'ACV (fiches A05, A32)'),
      el('p', { class: 'note' }, 'Indicateur 101 des contributeurs composants et chantier, en kg CO2 éq. par m² de S_ref.'),
      tableau(p.batiments, [
        { cle: 'nom', lib: 'Bâtiment', type: 'text' }, { cle: 'sref', lib: 'S_ref (m²)', type: 'number' },
        { cle: 'emprise_au_sol', lib: 'Emprise (m²)', type: 'number' }, { cle: 'duree_chantier', lib: 'Chantier (mois)', type: 'number' },
        ...['A1-A3', 'A4-A5', 'B', 'C', 'D'].map(ph => ({ lib: ph, type: 'number', get: b => (b.ges || {})[ph], set: (b, v) => { b.ges = b.ges || {}; setVal(b.ges, ph, v); } })),
      ], { ajouter: () => ({ nom: 'Bâtiment ' + (p.batiments.length + 1), sref: 0, emprise_au_sol: 0, duree_chantier: 12, ges: {} }) })),
  ];
}
async function importerRsee(f) {
  if (!f) return;
  const z = $('#rseeRetour');
  try {
    const r = await post('/api/rsee', await f.arrayBuffer(), true);
    const p = S.projet, faits = [];
    if (r.parcelle.surface) { p.parcelle.surface = r.parcelle.surface; faits.push(`parcelle ${nb(r.parcelle.surface, 0)} m²`); }
    for (const k of ['surface_vegetalisee_rsee', 'surface_impermeable_rsee', 'surface_arrosee_rsee']) if (r.parcelle[k] !== undefined) p.parcelle[k] = r.parcelle[k];
    if (r.batiments.length) { p.batiments = r.batiments; faits.push(`${r.batiments.length} bâtiment(s)`); }
    for (const k of ['zone_climatique', 'departement', 'altitude']) if (r[k] !== undefined && r[k] !== null) { p.contexte[k] = r[k]; faits.push(`${k.replace('_', ' ')} ${r[k]}`); }
    if (r.date_etude) p.projet.date_etude = r.date_etude;
    modifie(); afficher();
    $('#rseeRetour').textContent = (r.rsenv ? 'RSEE repris : ' : 'RSEE sans branche RSEnv : ') + (faits.join(', ') || 'aucune donnée utilisable');
  } catch (x) { z.textContent = 'RSEE illisible : ' + x.message; }
}

// ------------------------------------------------------------------ tableau générique
function tableau(lignes, colonnes, opts = {}) {
  const corps = el('tbody');
  lignes.forEach((l, i) => {
    const tr = el('tr', { class: opts.selection && opts.selection(l) ? 'sel' : '' });
    for (const c of colonnes) {
      let td;
      const style = `min-width:${c.largeur || LARGEURS[c.type] || 90}px`;
      if (c.calc) td = el('td', { class: c.n ? 'n' : '', style }, c.calc(l));
      else if (c.get) {
        const tmp = { v: c.get(l) };
        const e = entree(tmp, 'v', c.type, Object.assign({}, c, { apres: v => { c.set(l, tmp.v); if (c.apres) c.apres(l, v); } }));
        td = el('td', { style }, e);
      } else td = el('td', { style }, entree(l, c.cle, c.type, Object.assign({}, c, { apres: v => c.apres && c.apres(l, v) })));
      tr.append(td);
    }
    const act = el('td', { class: 'n actes' });
    if (opts.ouvrir) act.append(el('button', { title: 'Détail', onclick: () => opts.ouvrir(l) }, 'Détail'), ' ');
    if (opts.ajouter) act.append(el('button', { title: 'Dupliquer', onclick: () => { const d = copie(l); if (d.id) d.id = d.id + '-copie'; lignes.splice(i + 1, 0, d); modifie(); afficher(); } }, 'Copier'), ' ',
      el('button', { class: 'danger', title: 'Supprimer', onclick: () => { lignes.splice(i, 1); modifie(); afficher(); } }, 'Suppr.'));
    if (opts.ouvrir || opts.ajouter) tr.append(act);
    corps.append(tr);
  });
  const t = el('table', { class: 't' }, el('thead', {}, el('tr', {}, colonnes.map(c => el('th', { class: c.n ? 'n' : '' }, c.lib)),
    (opts.ouvrir || opts.ajouter) ? el('th', {}, '') : null)), corps);
  const bloc = el('div', {}, el('div', { class: 'defile' }, t));
  if (!lignes.length) bloc.append(el('div', { class: 'vide' }, opts.vide || 'Aucune ligne.'));
  if (opts.ajouter) bloc.append(el('div', { class: 'ligne', style: 'margin-top:8px' },
    el('button', { onclick: () => { lignes.push(opts.ajouter()); modifie(); afficher(); } }, '+ Ajouter')));
  return bloc;
}

// ------------------------------------------------------------------ onglets 2 et 3 : unités
function selecteurVariante() {
  return el('div', { class: 'ligne' }, el('label', {}, 'Variante : '),
    el('select', { onchange: ev => { S.vc = parseInt(ev.target.value, 10); afficher(); } },
      S.projet.variantes.map((v, i) => el('option', { value: i, selected: i === S.vc }, `${i + 1}. ${v.nom}${v.reference ? ' (référence)' : ''}`))));
}
function apercuEtat(u) {
  const h = habitat(u.code); if (!h) return '';
  if (!h.grille) return 'sans grille';
  const g = S.ref.grilles[h.grille];
  if (u.score) { let s = u.score.applicables ? u.score.satisfaits / u.score.applicables : 0; if (u.score.essentiel_echoue) s = Math.min(s, 0.5); return `${h.grille} · S ${nb(s, 2)}`; }
  if (g.indicateurs.length) {
    const n = g.indicateurs.length, q = g.indicateurs.reduce((a, i) => a + ((u.notes || {})[i.code] || 1), 0);
    return `${h.grille} · S ${nb((q - n) / (2 * n), 2)}`;
  }
  const r = u.criteres || {}; const app = g.criteres.filter(c => r[c.code] !== 'sans_objet');
  let s = app.length ? app.filter(c => r[c.code] === 'oui').length / app.length : 0;
  if (app.some(c => c.essentiel && (r[c.code] || 'non') === 'non')) s = Math.min(s, 0.5);
  return `${h.grille} · S ${nb(s, 2)}` + (Object.keys(r).length ? '' : ' (non renseignée)');
}
function colonnesUnites(mode) {
  const enums = S.ref.enums;
  const cols = [
    { cle: 'id', lib: 'Unité', type: 'text', largeur: 80 },
    { cle: 'code', lib: 'Type', type: 'text', liste: 'listeHabitats', reafficher: true, largeur: 85 },
    { lib: 'Libellé', calc: u => (habitat(u.code) || { libelle: 'type inconnu' }).libelle, largeur: 190 },
    { cle: 'position', lib: 'Position', type: 'select', options: enums.position, vide: 'du type', largeur: 140 },
    { cle: 'surface', lib: 'Surface (m²)', type: 'number' },
    { cle: 'epaisseur', lib: 'Substrat (cm)', type: 'number' },
    { cle: 'stade', lib: 'Stade', type: 'select', options: ['J', 'M', 'A'] },
    { cle: 'situation', lib: 'Situation', type: 'select', options: enums.situation, vide: 'hors trame' },
    { cle: 'tache', lib: 'Tache', type: 'text', liste: 'listeTaches' },
  ];
  if (mode === 'projet') cols.push(
    { cle: 'statut', lib: 'Statut', type: 'select', options: enums.statut, vide: 'créée', reafficher: true },
    { cle: 'liee', lib: 'Unité initiale', type: 'select', options: S.projet.etat_initial.map(u => u.id), libelles: x => x },
    { cle: 'protection', lib: 'Protégée', type: 'bool' });
  cols.push({ lib: 'État', calc: u => el('span', { class: 'lien', onclick: () => ouvrirUnite(u, mode) }, apercuEtat(u) || 'à renseigner') });
  return cols;
}
function listes() {
  const taches = new Set(Object.keys(S.projet.taches));
  for (const u of [...S.projet.etat_initial, ...S.projet.variantes.flatMap(v => v.unites)]) if (u.tache) taches.add(u.tache);
  return [el('datalist', { id: 'listeHabitats' }, S.ref.habitats.map(h => el('option', { value: h.code }, `${h.code} ${h.libelle}`))),
    el('datalist', { id: 'listeTaches' }, [...taches].map(t => el('option', { value: t })))];
}
function ongletUnites(mode) {
  const liste = mode === 'initial' ? S.projet.etat_initial : variante().unites;
  const prefixe = mode === 'initial' ? 'U0-' : `U${S.vc + 1}-`;
  return [el('h2', {}, mode === 'initial' ? 'État initial' : 'État projet'),
    mode === 'projet' ? selecteurVariante() : null,
    el('p', { class: 'note' }, mode === 'initial'
      ? 'Les unités d\'habitat du site avant le projet, relevées par l\'écologue. Les unités au sol, en eau et linéaires doivent couvrir toute la parcelle ; les arbres, toitures et façades s\'y ajoutent.'
      : 'Les unités de l\'état projet de la variante. Une unité conservée ou améliorée se rattache à son unité initiale. Le lien « État » ouvre la grille de critères et le détail de l\'unité.'),
    ...listes(),
    tableau(liste, colonnesUnites(mode), { ouvrir: u => ouvrirUnite(u, mode), selection: u => S.sel === u,
      ajouter: () => ({ id: prefixe + (liste.length + 1), code: 'VB.26', surface: 0 }) })];
}

// ------------------------------------------------------------------ tiroir de l'unité
function fermerTiroir() { const t = $('#tiroir'); t.hidden = true; t.innerHTML = ''; S.sel = null; }
function ouvrirUnite(u, mode) {
  S.sel = u;
  const t = $('#tiroir'); t.hidden = false; t.innerHTML = '';
  const h = habitat(u.code), enums = S.ref.enums;
  const rafraichir = () => { ouvrirUnite(u, mode); afficher(); S.sel = u; };
  t.append(el('button', { class: 'fermer', onclick: () => { fermerTiroir(); afficher(); } }, 'Fermer'),
    el('h2', {}, `Unité ${u.id}`), el('div', { class: 'note' }, h ? `${h.code} ${h.libelle} · position par défaut : ${lib(h.position)}` : 'Type inconnu'),
    el('h3', {}, 'Identification et surface (fiches A04, A14 à A16)'),
    el('div', { class: 'grille' }, champ(u, 'surface', 'Surface (m²)', 'number', { aide: 'vide : déduite pour un arbre, une haie ou une façade' }),
      champ(u, 'nombre_arbres', 'Nombre d\'arbres', 'int'), champ(u, 'classe_diametre', 'Classe de diamètre', 'select', { options: enums.classe_diametre }),
      champ(u, 'longueur', 'Longueur (m)', 'number'), champ(u, 'largeur', 'Largeur (m)', 'number'), champ(u, 'hauteur', 'Hauteur de façade (m)', 'number'),
      champ(u, 'epaisseur', 'Épaisseur de substrat (cm)', 'number'))),
  t.append(editeurEtat(u, h, rafraichir));
  t.append(el('h3', {}, 'Nuisances (fiches A20 à A22, A51 à A53)'), editeurEclairage(u, rafraichir),
    el('div', { class: 'grille' }, champ(u, 'niveau_sonore', 'Niveau sonore (dB(A))', 'number'),
      champ(u, 'exposition_vitrage', 'À moins de 15 m d\'un vitrage non traité de plus de 10 m²', 'bool')));
  t.append(el('h3', {}, 'Eau et sol (fiches A23, A47 à A49)'), el('div', { class: 'grille' },
    champ(u, 'alimentation', 'Alimentation d\'une unité en eau', 'select', { options: enums.alimentation }),
    champ(u, 'alimentation_humide', 'Milieu humide alimenté par', 'select', { options: enums.alimentation_humide }),
    champ(u, 'arrose', 'Arrosage automatique', 'bool'),
    champ(u, 'texture', 'Texture du sol', 'select', { options: enums.texture, vide: 'celle du site' }),
    champ(u, 'profondeur_sol', 'Profondeur de sol (m)', 'number'),
    champ(u, 'bassin_versant', 'Surface imperméable raccordée (m²)', 'number'),
    champ(u, 'bassin_versant_permeable', 'Surface perméable raccordée (m²)', 'number'),
    champ(u, 'profondeur', 'Profondeur de la mare (m)', 'number'), champ(u, 'fond', 'Fond de la mare', 'select', { options: enums.fond })));
  const g = el('div', { class: 'grille' }, champ(u, 'gestion', 'Régime imposé', 'select', { options: enums.gestion, vide: 'plan du projet' }),
    champ(u, 'apres_plan', 'Après le plan de gestion', 'select', { options: enums.apres_plan, vide: 'gestion courante' }),
    champ(u, 'plan_gestion_annees', 'Plan propre à l\'unité (années)', 'number'), champ(u, 'gites', 'Gîtes de chiroptères', 'bool'));
  const renouv = { v: (u.renouvellements || []).join(' ') };
  g.append(el('div', { class: 'champ' }, el('label', {}, 'Années de réfection (fiche A30)'),
    el('input', { type: 'text', value: renouv.v, placeholder: 'ex. 25 40', onchange: ev => {
      const l = ev.target.value.split(/[\s,;]+/).map(x => parseInt(x, 10)).filter(x => x >= 1 && x <= 50);
      setVal(u, 'renouvellements', l.length ? l : undefined); modifie(); } })));
  t.append(el('h3', {}, 'Gestion et chantier (fiches A30, A55 à A57)'), g);
  if (mode === 'projet') t.append(el('div', { class: 'grille' },
    champ(u, 'statut', 'Statut', 'select', { options: enums.statut, vide: 'créée' }),
    champ(u, 'liee', 'Unité initiale liée', 'select', { options: S.projet.etat_initial.map(x => x.id), libelles: x => x }),
    champ(u, 'protection', 'Protection pendant le chantier', 'bool')));
}
function editeurEtat(u, h, rafraichir) {
  const bloc = el('div', {}, el('h3', {}, 'État (fiches A10 à A12)'));
  if (!h || !h.grille) { bloc.append(el('div', { class: 'note' }, 'Ce type n\'a pas de grille d\'état : facteur d\'état 1.')); return bloc; }
  const g = S.ref.grilles[h.grille];
  bloc.append(el('div', { class: 'ligne' }, el('span', { class: 'pastille neutre' }, `grille ${h.grille}`), el('strong', {}, apercuEtat(u)),
    el('label', {}, el('input', { type: 'checkbox', checked: !!u.score, onchange: ev => {
      if (ev.target.checked) { u.score = { satisfaits: 0, applicables: g.criteres.length || 1 }; delete u.criteres; delete u.notes; } else delete u.score;
      modifie(); rafraichir(); } }), ' résumé de grille')));
  if (u.score) {
    bloc.append(el('div', { class: 'grille' }, champ(u.score, 'satisfaits', 'Critères satisfaits', 'int', { apres: rafraichir }),
      champ(u.score, 'applicables', 'Critères applicables', 'int', { apres: rafraichir }),
      champ(u.score, 'essentiel_echoue', 'Un critère essentiel a échoué', 'bool', { apres: rafraichir })),
      el('p', { class: 'note' }, 'Résumé admis quand le détail de la grille n\'est pas transmis ; il est écrit tel quel dans le RSNat.'));
    return bloc;
  }
  if (g.indicateurs.length) {
    u.notes = u.notes || {};
    for (const i of g.indicateurs) bloc.append(el('div', { class: 'crit' }, el('span', { class: 'code' }, ''), el('span', {}, i.libelle || i.code),
      el('select', { onchange: ev => { u.notes[i.code] = parseInt(ev.target.value, 10); modifie(); rafraichir(); } },
        [1, 2, 3].map(n => el('option', { value: n, selected: (u.notes[i.code] || 1) === n }, `note ${n}`)))));
    return bloc;
  }
  u.criteres = u.criteres || {};
  for (const c of g.criteres) {
    const nom = `c-${u.id}-${c.code}`;
    bloc.append(el('div', { class: 'crit' }, el('span', { class: 'code' }, c.code),
      el('span', {}, c.libelle || '', c.essentiel ? el('div', { class: 'ess' }, 'critère essentiel') : null),
      el('div', { class: 'radios' }, ['oui', 'non', 'sans_objet'].map(r => el('label', {}, el('input', { type: 'radio', name: nom, checked: (u.criteres[c.code] || '') === r,
        onchange: () => { u.criteres[c.code] = r; modifie(); rafraichir(); } }), r === 'sans_objet' ? 'sans objet' : r)))));
  }
  return bloc;
}
function modeEclairage(u) { const e = u.eclairage; return !e ? 'aucun' : (typeof e === 'string' ? (e === 'L0' ? 'aucun' : e) : 'horaire'); }
function editeurEclairage(u, rafraichir) {
  const m = modeEclairage(u);
  const bloc = el('div', {}, el('div', { class: 'champ' }, el('label', {}, 'Éclairage nocturne'),
    el('select', { onchange: ev => { const v = ev.target.value;
      if (v === 'aucun') delete u.eclairage; else if (v === 'horaire') u.eclairage = { extinction: 23, cct: 3000, distance: 0 }; else u.eclairage = v;
      modifie(); rafraichir(); } },
      [['aucun', 'aucun'], ['L1', 'raccourci L1 : conforme, éteint à 1 h, 3 000 K'], ['L2', 'raccourci L2 : toute la nuit, 4 000 K'], ['horaire', 'déclaré : horaires, température, distance']]
        .map(([v, l]) => el('option', { value: v, selected: v === m }, l)))));
  if (m === 'horaire') {
    const e = u.eclairage;
    bloc.append(el('div', { class: 'grille' },
      champ(e, 'extinction', 'Extinction (heure légale)', 'int', { min: 0, max: 23, aide: 'vide : toute la nuit' }),
      champ(e, 'rallumage', 'Rallumage du matin', 'int', { min: 0, max: 23 }),
      champ(e, 'cct', 'Température de couleur (K)', 'number'), champ(e, 'distance', 'Distance au luminaire (m)', 'number'),
      champ(e, 'taux_detection', 'Part de temps allumé (détection)', 'number', { step: 0.05, aide: 'de 0 à 1 ; 1 sans détection' })));
  }
  return bloc;
}

// ------------------------------------------------------------------ onglets thématiques
function unitesDesDeux() {
  return [...S.projet.etat_initial.map(u => ({ u, etat: 'initial' })), ...variante().unites.map(u => ({ u, etat: 'projet' }))];
}
function tableauThematique(colonnes) {
  const lignes = unitesDesDeux();
  return tableau(lignes, [{ lib: 'État', calc: l => l.etat, largeur: 60 }, { lib: 'Unité', calc: l => l.u.id, largeur: 70 },
    { lib: 'Type', calc: l => `${l.u.code} ${(habitat(l.u.code) || {}).libelle || ''}`, largeur: 230 },
    ...colonnes.map(c => Object.assign({}, c, { get: l => c.get ? c.get(l.u) : l.u[c.cle], set: (l, v) => c.set ? c.set(l.u, v) : setVal(l.u, c.cle, v) }))],
  { ouvrir: l => ouvrirUnite(l.u, l.etat) });
}
function ongletSol() {
  const sol = S.projet.contexte.sol;
  return [el('h2', {}, 'Sol'), selecteurVariante(),
    el('div', { class: 'carte' }, el('h3', {}, 'Sol du site (fiche A48, convention C-W4)'), el('div', { class: 'grille' },
      champ(sol, 'texture', 'Texture', 'select', { options: S.ref.enums.texture, vide: false }),
      champ(sol, 'profondeur', 'Profondeur explorable (m)', 'number'))),
    el('div', { class: 'carte' }, el('h3', {}, 'Natures de surface et sols des unités (fiches A06 à A08)'),
      el('p', { class: 'note' }, 'La nature de surface (S01 à S12) se déduit du type, de la position et de l\'épaisseur de substrat. Texture et profondeur propres à une unité l\'emportent sur celles du site.'),
      tableauThematique([{ cle: 'position', lib: 'Position', type: 'select', options: S.ref.enums.position, vide: 'du type' },
        { cle: 'epaisseur', lib: 'Substrat (cm)', type: 'number' },
        { cle: 'texture', lib: 'Texture', type: 'select', options: S.ref.enums.texture, vide: 'du site' },
        { cle: 'profondeur_sol', lib: 'Profondeur (m)', type: 'number' }]))];
}
function ongletConnectivite() {
  const p = S.projet;
  const ids = new Set(Object.keys(p.taches));
  for (const u of [...p.etat_initial, ...p.variantes.flatMap(v => v.unites)]) if (u.tache) ids.add(u.tache);
  for (const t of ids) p.taches[t] = p.taches[t] || {};
  const lignes = [...ids].sort().map(t => ({ t, info: p.taches[t] }));
  return [el('h2', {}, 'Connectivité'), selecteurVariante(),
    el('div', { class: 'carte' }, el('h3', {}, 'Taches (fiches A17 à A19)'),
      el('p', { class: 'note' }, 'Une tache réunit des unités contiguës. Une unité sans tache forme la sienne. La connexion se déduit de la distance et de la surface de l\'espace naturel le plus proche quand elles sont saisies.'),
      tableau(lignes, [{ lib: 'Tache', calc: l => l.t },
        ...[['connexion', 'Connexion', 'select', S.ref.enums.connexion], ['exterieur', 'Surface extérieure contiguë (m²)', 'number'],
          ['cloture', 'Clôture', 'select', S.ref.enums.cloture], ['distance_espace_naturel', 'Distance à l\'espace naturel (m)', 'number'],
          ['surface_espace_naturel', 'Surface de cet espace (m²)', 'number'], ['trame', 'Contiguë à la trame', 'bool']]
          .map(([cle, libelle, type, options]) => ({ lib: libelle, type, options, get: l => l.info[cle], set: (l, v) => setVal(l.info, cle, v) }))],
      { vide: 'Aucune tache : déclarez-en une dans la colonne « Tache » des unités.' })),
    el('div', { class: 'carte' }, el('h3', {}, 'Rattachement des unités'), ...listes(),
      tableauThematique([{ cle: 'tache', lib: 'Tache', type: 'text', liste: 'listeTaches', reafficher: true },
        { cle: 'situation', lib: 'Situation', type: 'select', options: S.ref.enums.situation, vide: 'hors trame' }]))];
}
function ongletNuisances() {
  const v = variante(); v.facades_vitrees = v.facades_vitrees || [];
  const ecl = (k) => ({ get: u => (u.eclairage && typeof u.eclairage === 'object') ? u.eclairage[k] : undefined,
    set: (u, x) => { if (u.eclairage && typeof u.eclairage === 'object') setVal(u.eclairage, k, x); } });
  return [el('h2', {}, 'Nuisances'), selecteurVariante(),
    el('div', { class: 'mention' }, 'L\'éclairage se calcule heure par heure : heures de nuit éclairées d\'avril à octobre, température de couleur, distance au luminaire (fiches A51 à A53). Le détail d\'une unité permet de choisir un raccourci ou un éclairage déclaré.'),
    el('div', { class: 'carte' }, el('h3', {}, 'Éclairage, bruit, vitrages par unité'),
      tableauThematique([{ lib: 'Éclairage', type: 'select', options: ['aucun', 'L1', 'L2', 'horaire'], vide: false, reafficher: true,
          get: u => modeEclairage(u), set: (u, v) => { if (v === 'aucun') delete u.eclairage; else if (v === 'horaire') u.eclairage = { extinction: 23, cct: 3000, distance: 0 }; else u.eclairage = v; } },
        Object.assign({ lib: 'Extinction', type: 'int' }, ecl('extinction')), Object.assign({ lib: 'K', type: 'number' }, ecl('cct')),
        Object.assign({ lib: 'Distance (m)', type: 'number' }, ecl('distance')),
        { cle: 'niveau_sonore', lib: 'Bruit (dB(A))', type: 'number' }, { cle: 'exposition_vitrage', lib: 'Vitrage', type: 'bool' }])),
    el('div', { class: 'carte' }, el('h3', {}, 'Façades vitrées exposées de la variante (fiche A22)'),
      tableau(v.facades_vitrees, [{ cle: 'surface', lib: 'Surface vitrée (m²)', type: 'number' }, { cle: 'traitee', lib: 'Traitée contre les collisions', type: 'bool' }],
        { ajouter: () => ({ surface: 0, traitee: false }) }))];
}
function ongletEau() {
  const v = variante(); v.ouvrages_pluviaux = v.ouvrages_pluviaux || [];
  return [el('h2', {}, 'Eau'), selecteurVariante(),
    el('div', { class: 'carte' }, el('h3', {}, 'Unités : alimentation, arrosage, raccordements, mares (fiches A23, A47 à A50)'),
      tableauThematique([{ cle: 'alimentation', lib: 'Alimentation', type: 'select', options: S.ref.enums.alimentation },
        { cle: 'alimentation_humide', lib: 'Milieu humide', type: 'select', options: S.ref.enums.alimentation_humide },
        { cle: 'arrose', lib: 'Arrosé', type: 'bool' }, { cle: 'bassin_versant', lib: 'Raccordé imperméable (m²)', type: 'number' },
        { cle: 'bassin_versant_permeable', lib: 'Raccordé perméable (m²)', type: 'number' },
        { cle: 'profondeur', lib: 'Mare : profondeur (m)', type: 'number' }, { cle: 'fond', lib: 'Fond', type: 'select', options: S.ref.enums.fond }])),
    el('div', { class: 'carte' }, el('h3', {}, 'Ouvrages de gestion des eaux pluviales de la variante (fiche A24)'),
      el('p', { class: 'note' }, 'La surface imperméable conduite vers un ouvrage qui infiltre en surface entre dans Bnat (coefficient S13).'),
      tableau(v.ouvrages_pluviaux, [{ cle: 'surface_drainee', lib: 'Surface drainée (m²)', type: 'number' }, { cle: 'infiltration_surface', lib: 'Infiltration en surface', type: 'bool' }],
        { ajouter: () => ({ surface_drainee: 0, infiltration_surface: true }) }))];
}
function ongletMateriaux() {
  const v = variante(); v.materiaux = v.materiaux || {}; const m = v.materiaux; m.bois = m.bois || [];
  const gran = m.granulats || {};
  const modele = 'categorie;regime;quantite;remplacements;justification\nbois;coupe_rase;30;0;\nbois;coupe_selective;12;0;certificat PEFC n° ...\ngranulats;;1800;0;\n';
  return [el('h2', {}, 'Matériaux'), selecteurVariante(),
    el('div', { class: 'carte' }, el('h3', {}, 'Bois (fiche A34)'),
      el('p', { class: 'note' }, 'Un régime autre que la coupe rase n\'est retenu qu\'avec une pièce justificative (convention C-G5).'),
      tableau(m.bois, [{ cle: 'regime', lib: 'Régime forestier', type: 'select', options: S.ref.enums.regime, vide: 'coupe rase' },
        { cle: 'volume', lib: 'Volume (m³)', type: 'number' }, { cle: 'remplacements', lib: 'Remplacements en 50 ans', type: 'int' },
        { cle: 'justification', lib: 'Pièce justificative', type: 'text' }], { ajouter: () => ({ regime: 'coupe_rase', volume: 0 }) })),
    el('div', { class: 'carte' }, el('h3', {}, 'Granulats, sables et roches (fiche A35)'), el('div', { class: 'grille' },
      champ(gran, 'masse', 'Masse (t)', 'number', { apres: () => { if (gran.masse !== undefined) m.granulats = gran; else delete m.granulats; } }),
      champ(gran, 'remplacements', 'Remplacements en 50 ans', 'int', { apres: () => { if (gran.masse !== undefined) m.granulats = gran; } }))),
    el('div', { class: 'carte' }, el('h3', {}, 'Import d\'un tableur de matériaux'),
      el('p', { class: 'note' }, 'Fichier CSV, séparateur point-virgule, colonnes : categorie (bois ou granulats) ; regime (pour le bois) ; quantite (m³ de bois, t de granulats) ; remplacements ; justification. L\'import remplace les matériaux de la variante.'),
      el('div', { class: 'ligne' }, el('input', { type: 'file', accept: '.csv,text/csv', onchange: ev => importerMateriaux(ev.target.files[0]) }),
        el('button', { onclick: () => telecharger('modele_materiaux.csv', modele, 'text/csv') }, 'Télécharger le modèle')),
      el('div', { id: 'matRetour', class: 'note' })),
    el('div', { class: 'carte' }, el('h3', {}, 'Émissions des bâtiments'),
      el('p', { class: 'note' }, 'Les indicateurs d\'ACV des bâtiments se saisissent ou se reprennent du RSEE dans l\'onglet « Projet et contexte ». Une variante qui change la construction (bois contre béton) peut porter ses propres bâtiments. Le RSEE n\'est pas lu lot par lot : la biodiversité grise est donnée par poste (climat, bois, carrières) et par phase.'),
      el('label', {}, el('input', { type: 'checkbox', checked: !!v.batiments, onchange: ev => {
        if (ev.target.checked) v.batiments = copie(S.projet.batiments); else delete v.batiments; modifie(); afficher(); } }), ' bâtiments propres à cette variante'),
      v.batiments ? tableau(v.batiments, [
        { cle: 'nom', lib: 'Bâtiment', type: 'text' }, { cle: 'sref', lib: 'S_ref (m²)', type: 'number' },
        { cle: 'emprise_au_sol', lib: 'Emprise (m²)', type: 'number' }, { cle: 'duree_chantier', lib: 'Chantier (mois)', type: 'number' },
        ...['A1-A3', 'A4-A5', 'B', 'C', 'D'].map(ph => ({ lib: ph, type: 'number', get: b => (b.ges || {})[ph], set: (b, x) => { b.ges = b.ges || {}; setVal(b.ges, ph, x); } })),
      ], { ajouter: () => ({ nom: 'Bâtiment', sref: 0, emprise_au_sol: 0, duree_chantier: 12, ges: {} }) }) : null)];
}
async function importerMateriaux(f) {
  if (!f) return;
  const r = await post('/api/materiaux', await f.text(), true);
  variante().materiaux = r.materiaux; modifie(); afficher();
  $('#matRetour').textContent = r.erreurs.length ? 'Lignes ignorées : ' + r.erreurs.join(' ; ') : 'Matériaux importés.';
}
function ongletVariantes() {
  const p = S.projet;
  return [el('h2', {}, 'Variantes (fiche A41)'),
    el('p', { class: 'note' }, 'Toutes les variantes partagent l\'état initial et le contexte. La variante de référence porte l\'attestation au permis ; les autres se comparent à elle. Un plan de gestion ou un calendrier de chantier propre à une variante remplace celui du projet ; vide, c\'est celui du projet qui s\'applique.'),
    el('div', { class: 'carte' }, tableau(p.variantes, [
      { cle: 'nom', lib: 'Nom', type: 'text' },
      { lib: 'Référence', calc: v => el('input', { type: 'radio', name: 'reference', checked: !!v.reference,
        onchange: () => { p.variantes.forEach(x => delete x.reference); v.reference = true; modifie(); afficher(); } }) },
      { lib: 'Unités', n: true, calc: v => String(v.unites.length) },
      { lib: 'Plan de gestion (années)', type: 'number', get: v => (v.gestion || {}).plan_annees, set: (v, x) => { v.gestion = v.gestion || {}; setVal(v.gestion, 'plan_annees', x); if (!Object.keys(v.gestion).length) delete v.gestion; } },
      ...[['duree_mois', 'Chantier (mois)', 'number'], ['mois_debut', 'Début (mois)', 'int'], ['annee_debut', 'Début (année)', 'int']].map(([k, l, t]) => ({ lib: l, type: t,
        get: v => (v.chantier || {})[k], set: (v, x) => { v.chantier = v.chantier || {}; setVal(v.chantier, k, x); if (!Object.keys(v.chantier).length) delete v.chantier; } })),
      { cle: 'emprise', lib: 'Emprise sans bâtiment (m²)', type: 'number' },
      { lib: 'Édition', calc: v => el('button', { onclick: () => { S.vc = p.variantes.indexOf(v); aller('etatProjet'); } }, 'Ouvrir l\'état projet') },
    ], { ajouter: () => { const d = copie(variante()); d.nom = 'Variante ' + (p.variantes.length + 1); delete d.reference; return d; } }))];
}

// ------------------------------------------------------------------ calcul
function ongletCalcul() {
  const opt = S.projet.options;
  const bloc = [el('h2', {}, 'Calcul'),
    el('div', { class: 'carte' }, el('h3', {}, 'Lancement'),
      el('div', { class: 'grille' }, champ(opt, 'tirages', 'Tirages de l\'analyse d\'incertitude', 'int', { aide: '0 : valeurs centrales seules ; 1 000 par défaut' }),
        champ(opt, 'graine', 'Graine du générateur', 'int', { aide: 'facultative ; à graine égale, résultats identiques' })),
      el('p', { class: 'note' }, 'Le calcul enchaîne, pour chaque variante, les étapes E1, E2, S, H, C, N, E, W, T, G, E3 et E5, puis l\'analyse d\'incertitude E4. Le bilan hydrique horaire prend quelques secondes par variante ; 1 000 tirages prennent environ trois minutes.'),
      el('div', { class: 'ligne' },
        el('button', { class: 'vert', disabled: !controlesOk() || (S.etatCalcul && S.etatCalcul.etat === 'en_cours'), onclick: () => lancer() }, 'Lancer le calcul'),
        controlesOk() ? null : el('span', { class: 'avert' }, 'Contrôles à lever avant le calcul (panneau de droite).')))];
  if (S.etatCalcul) bloc.push(suiviCalcul());
  return bloc;
}
async function lancer(reprendre) {
  try {
    const r = await post('/api/calcul', { projet: S.projet, tirages: S.projet.options.tirages, reprendre });
    S.calcul = r.calcul; S.etatCalcul = { etat: 'en_cours', messages: [], etapes: {} }; S.resultats = null; afficher(); suivre();
  } catch (x) { alert('Calcul refusé : ' + x.message); }
}
async function suivre() {
  if (!S.calcul) return;
  S.etatCalcul = await api('/api/calcul/' + S.calcul);
  if (S.onglet === 'calcul') { const z = $('#suivi'); if (z) z.replaceWith(suiviCalcul()); }
  if (S.etatCalcul.etat === 'en_cours') { setTimeout(suivre, 700); return; }
  if (S.etatCalcul.etat === 'termine') { S.resultats = await api('/api/resultats/' + S.calcul); S.rv = 0; if (S.onglet === 'calcul') aller('resultats'); }
  else if (S.onglet === 'calcul') afficher();
}
function suiviCalcul() {
  const e = S.etatCalcul, nv = S.projet.variantes.length;
  const z = el('div', { class: 'carte', id: 'suivi' }, el('h3', {}, 'Avancement'),
    el('div', { class: 'ligne' }, el('span', { class: 'pastille ' + ({ termine: 'ok', erreur: 'ko', interrompu: 'ko' }[e.etat] || 'neutre') },
      { en_cours: 'en cours', termine: 'terminé', erreur: 'erreur', interrompu: 'interrompu' }[e.etat]), e.duree !== undefined ? `${nb(e.duree, 0)} s` : ''));
  for (let v = 1; v <= nv; v++) {
    const ch = el('div', { class: 'etapes' }, el('strong', {}, `Variante ${v} : `));
    ETAPES.forEach(k => {
      const fait = (`${v}:${k}` in (e.etapes || {}));
      const cours = e.courante && e.courante.variante === v && e.courante.etape === k && e.etat === 'en_cours';
      ch.append(el('span', { class: 'etape ' + (cours ? 'cours' : fait ? 'fait' : '') }, NOMS_ETAPES[k]));
    });
    z.append(ch);
  }
  if (S.projet.options.tirages !== 0) {
    const av = e.e4 || 0;
    z.append(el('div', {}, el('strong', {}, `E4 incertitude : ${nb(100 * av, 0)} %`)), el('div', { class: 'progression' }, el('div', { style: `width:${100 * av}%` })));
  }
  if (e.etat === 'en_cours') z.append(el('div', { class: 'ligne', style: 'margin-top:10px' }, el('button', { class: 'danger', onclick: () => post(`/api/calcul/${S.calcul}/arret`, {}) }, 'Arrêter après le bloc de tirages en cours')));
  if (e.etat === 'interrompu') z.append(el('div', { class: 'ligne', style: 'margin-top:10px' }, el('span', {}, 'Le dossier reste reprenable : '),
    el('button', { class: 'principal', onclick: () => lancer(e.dossier) }, 'Reprendre le calcul')));
  if (e.etat === 'erreur') z.append(el('div', { class: 'erreurs' }, 'Calcul arrêté : ' + e.erreur));
  z.append(el('h4', {}, 'Journal'), el('pre', { class: 'journal' }, (e.messages || []).join('\n')));
  return z;
}

// ------------------------------------------------------------------ résultats
function sansResultats() { return [el('h2', {}, 'Résultats'), el('div', { class: 'vide' }, 'Lancez un calcul dans l\'onglet « Calcul ».')]; }
function selecteurResultat() {
  return el('div', { class: 'ligne' }, el('label', {}, 'Variante : '), el('select', { onchange: ev => { S.rv = parseInt(ev.target.value, 10); afficher(); } },
    S.resultats.variantes.map((v, i) => el('option', { value: i, selected: i === S.rv }, `${v.index}. ${v.nom}${v.reference ? ' (référence)' : ''}`))));
}
function carte(nom, val, sous) { return el('div', { class: 'ind' }, el('div', { class: 'nom' }, nom), el('div', { class: 'val' }, val), sous ? el('div', { class: 'sous' }, sous) : null); }
function pastilleConf(x) { return x === null || x === undefined ? el('span', { class: 'pastille neutre' }, 'sans seuil') : el('span', { class: 'pastille ' + (x ? 'ok' : 'ko') }, x ? 'respecté' : 'non respecté'); }
function intervalle(v, nom) { const i = v.incertitude && v.incertitude.Intervalle.find(x => x.indicateur === nom); return i ? `90 % : ${nb(i.p5, 0)} à ${nb(i.p95, 0)}` : null; }
function ongletResultats() {
  if (!S.resultats) return sansResultats();
  const v = S.resultats.variantes[S.rv], i = v.indicateurs, s = v.seuils, si = v.site, ma = v.materiaux;
  const blocs = [el('h2', {}, 'Résultats'), selecteurResultat(),
    el('div', { class: 'mention' }, 'Méthode, conventions et seuils proposés, en attente de validation du Biodiversity Standard Council : les résultats ne sont pas opposables.'),
    el('div', { class: 'indicateurs' },
      carte('Bnat (points)', nb(i.bnat), el('span', {}, `seuil ${s.bnat_min === null ? 'aucun' : nb(s.bnat_min, 0)} `, pastilleConf(s.bnat_conforme))),
      carte('Pleine terre', pct(i.pleine_terre), el('span', {}, `seuil ${pct(s.pleine_terre_min, 0)} `, pastilleConf(s.pleine_terre_conforme))),
      carte('Cnat (m²HE·an)', nb(i.cnat, 0), [i.cnat_relatif === null ? 'relatif non défini' : `${pct(i.cnat_relatif)} de I_0`, ' · ', NIVEAUX[i.niveau]].join('')),
      carte('Inat (m²HE·an)', nb(i.inat, 0), intervalle(v, 'inat')), carte('Snat (m²HE·an)', nb(i.snat, 0), intervalle(v, 'snat')),
      carte('Cnat sur 30 ans', nb(i.cnat_30, 0), `moyenne annuelle ${nb(i.cnat_moyen)} m²HE`)),
    el('div', { class: 'carte' }, el('h3', {}, 'Attestation au permis de construire (variante de référence)'),
      el('p', {}, s.permis ? 'Le plan masse respecte les seuils proposés.' : 'Le plan masse ne respecte pas tous les seuils proposés ; l\'attestation ne conclut pas à la conformité.'),
      el('div', { class: 'note' }, `Part d'emprise ${pct(s.part_emprise)} ; règles du PLU : ${s.plu_conforme === null ? 'sans objet' : s.plu_conforme ? 'respectées' : 'non respectées'}.`)),
    el('div', { class: 'carte' }, el('h3', {}, 'Trajectoire du site sur 50 ans'), courbe(v.trajectoire)),
    el('div', { class: 'carte' }, el('h3', {}, 'Détail du site (modules S, W, T)'), tableauLecture([
      ['Valeur du site sans projet (m²HE)', nb(si.v0)], ['I_0, valeur intégrée sans projet, même climat (m²HE·an)', nb(si.i0)],
      ['I_1, valeur intégrée avec projet (m²HE·an)', nb(si.i1)], ['Dette de maturité (m²HE·an)', nb(si.dette)],
      ['Destruction en période sensible (m²HE·an)', nb(si.destruction)], ['Arrosage annuel moyen (m³)', nb(si.arrosage)],
      ['Imperméabilisation nette (m²)', nb(si.impermeabilisation, 0)], ['Surface infiltrée en surface (m²)', nb(si.a_inf, 0)],
      ['Premier mois de plantation (rang depuis le début du chantier)', nb(si.rang_plantation, 0)],
      ['Plan de gestion écologique (années)', nb(si.plan, 0)]])),
    el('div', { class: 'carte' }, el('h3', {}, 'Biodiversité grise par poste (module G)'), barres([
      ['Climat (composants et chantier)', ma.inat_clim], ['Bois (occupation des forêts)', ma.inat_bois], ['Carrières', ma.inat_carr]]),
      el('h4', {}, 'Climat par phase'), tableauLecture(Object.entries(ma.par_phase).map(([p, x]) => [p, nb(x, 0)])),
      el('div', { class: 'note' }, `S_ref ${nb(ma.sref, 0)} m² ; facteur climat ${ma.CF.toExponential(3).replace('.', ',').replace('e', ' x 10^')} m²HE par kg CO2 éq. et par an.`))];
  if (v.incertitude) blocs.push(el('div', { class: 'carte' }, el('h3', {}, `Incertitude (${v.incertitude.tirages} tirages, fiche A39)`),
    tableau(v.incertitude.Intervalle, [{ lib: 'Indicateur', calc: x => x.indicateur.replace('ecart_', 'écart à la référence : ') },
      { lib: 'Centile 5', n: true, calc: x => nb(x.p5) }, { lib: 'Médiane', n: true, calc: x => nb(x.p50) }, { lib: 'Centile 95', n: true, calc: x => nb(x.p95) }]),
    el('h4', {}, 'Paramètres les plus influents sur Snat'),
    tableau(v.incertitude.Parametre_Influent, [{ lib: 'Rang', n: true, calc: x => String(x.rang) }, { lib: 'Table', calc: x => x.table },
      { lib: 'Clé', calc: x => x.cle }, { lib: 'Paramètre', calc: x => x.parametre }, { lib: 'Corrélation de rang', n: true, calc: x => nb(x.correlation, 2) }])));
  blocs.push(el('div', { class: 'carte' }, el('h3', {}, 'Unités'), tableau(v.unites, [
    { lib: 'État', calc: u => u.etat }, { lib: 'Unité', calc: u => u.id }, { lib: 'Type', calc: u => u.code },
    { lib: 'Surface', n: true, calc: u => nb(u.surface, 0) }, { lib: 'S', n: true, calc: u => u.S === null ? '' : nb(u.S, 2) },
    { lib: 'f', n: true, calc: u => nb(u.f, 3) }, { lib: 'k_C', n: true, calc: u => nb(u.kC, 3) }, { lib: 'k_lum', n: true, calc: u => nb(u.kL, 3) },
    { lib: 'k_N', n: true, calc: u => nb(u.kN, 3) }, { lib: 'V (m²HE)', n: true, calc: u => nb(u.V) },
    { lib: 'k_W moyen', n: true, calc: u => u.kW_moyen === null ? '' : nb(u.kW_moyen, 3) },
    { lib: 'f_gestion an 50', n: true, calc: u => u.f_gestion_fin === null ? '' : nb(u.f_gestion_fin, 3) },
    { lib: 'Intégrée (m²HE·an)', n: true, calc: u => nb(u.integree, 0) }])));
  blocs.push(el('div', { class: 'carte' }, el('h3', {}, 'Journal du calcul'), el('pre', { class: 'journal' }, S.resultats.journal.join('\n') || 'aucune remarque')));
  return blocs;
}
function tableauLecture(lignes) { return el('table', { class: 't' }, el('tbody', {}, lignes.map(([a, b]) => el('tr', {}, el('td', {}, a), el('td', { class: 'n' }, b))))); }
function barres(lignes) {
  const max = Math.max(...lignes.map(l => Math.abs(l[1] || 0)), 1);
  return el('div', { class: 'barres' }, lignes.map(([n, x]) => el('div', { class: 'b' }, el('span', {}, n),
    el('div', { class: 'piste' }, el('div', { class: 'rempli', style: `width:${100 * Math.abs(x || 0) / max}%` })), el('span', { class: 'n' }, nb(x, 0)))));
}
function courbe(tr) {
  const W = 760, H = 260, g = 46, d = 16, h = 16, b = 30;
  const toutes = [...tr.site, ...tr.reference], ymax = Math.max(...toutes, 1) * 1.08, n = tr.site.length;
  const x = i => g + (W - g - d) * i / (n - 1), y = v => H - b - (H - b - h) * v / ymax;
  const ligne = (s, coul, tiret) => `<polyline fill="none" stroke="${coul}" stroke-width="2.2" ${tiret ? 'stroke-dasharray="6 4"' : ''} points="${s.map((v, i) => `${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(' ')}"/>`;
  let axes = `<line x1="${g}" y1="${H - b}" x2="${W - d}" y2="${H - b}" stroke="#CFD6D9"/>`;
  for (let k = 0; k <= 4; k++) { const v = ymax * k / 4; axes += `<line x1="${g}" y1="${y(v)}" x2="${W - d}" y2="${y(v)}" stroke="#EEF3F6"/><text x="${g - 6}" y="${y(v) + 4}" text-anchor="end">${nb(v, 0)}</text>`; }
  for (let i = 0; i < n; i += 10) axes += `<text x="${x(i)}" y="${H - 10}" text-anchor="middle">${tr.annees[i]}</text>`;
  const svg = `<svg class="courbe" viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Trajectoire du site">${axes}${ligne(tr.reference, '#0FA36A', true)}${ligne(tr.site, '#2871B7')}</svg>`;
  return el('div', {}, el('div', { html: svg }), el('div', { class: 'legende' }, el('span', {}, el('i', { style: 'background:#2871B7' }), 'avec projet (m²HE)'),
    el('span', {}, el('i', { style: 'background:#0FA36A' }), 'site sans projet, même climat')));
}
function ongletComparaison() {
  if (!S.resultats) return sansResultats();
  const vs = S.resultats.variantes, ref = vs.find(v => v.reference);
  const lignes = [['Bnat (points)', v => nb(v.indicateurs.bnat)], ['Pleine terre', v => pct(v.indicateurs.pleine_terre)],
    ['Cnat (m²HE·an)', v => nb(v.indicateurs.cnat, 0)], ['Cnat relatif', v => v.indicateurs.cnat_relatif === null ? 'n. d.' : pct(v.indicateurs.cnat_relatif)],
    ['Niveau du site', v => NIVEAUX[v.indicateurs.niveau]], ['Inat (m²HE·an)', v => nb(v.indicateurs.inat, 0)], ['Snat (m²HE·an)', v => nb(v.indicateurs.snat, 0)],
    ['Dette de maturité', v => nb(v.site.dette, 0)], ['Arrosage (m³/an)', v => nb(v.site.arrosage)],
    ['Écart de Snat à la référence', v => v === ref ? '' : nb(v.indicateurs.snat - ref.indicateurs.snat, 0)],
    ['Intervalle de l\'écart de Snat', v => { const i = v.incertitude && v.incertitude.Intervalle.find(x => x.indicateur === 'ecart_snat'); return i ? `${nb(i.p5, 0)} à ${nb(i.p95, 0)}` : ''; }]];
  return [el('h2', {}, 'Comparaison des variantes'),
    el('p', { class: 'note' }, 'Les écarts se calculent sur les mêmes tirages pour toutes les variantes : leur intervalle est plus étroit que celui de chaque variante (fiche A41).'),
    el('div', { class: 'defile' }, el('table', { class: 't' }, el('thead', {}, el('tr', {}, el('th', {}, 'Indicateur'), vs.map(v => el('th', { class: 'n' }, `${v.nom}${v.reference ? ' (réf.)' : ''}`)))),
      el('tbody', {}, lignes.map(([n, f]) => el('tr', {}, el('td', {}, n), vs.map(v => el('td', { class: 'n' }, f(v))))))))];
}
function ongletFichiers() {
  if (!S.resultats) return sansResultats();
  const z = el('div', { class: 'carte' }, el('div', { class: 'vide' }, 'Chargement…'));
  const vue = el('pre', { class: 'fichier' }, 'Choisissez un fichier.');
  api('/api/fichiers/' + S.calcul).then(l => {
    z.innerHTML = '';
    z.append(tableau(l, [{ lib: 'Fichier', calc: f => el('span', { class: 'lien', onclick: () => voir(f.chemin) }, f.chemin) },
      { lib: 'Taille', n: true, calc: f => `${nb(f.taille / 1024, 1)} ko` }]));
  });
  async function voir(chemin) {
    let t = await api(`/api/fichier/${S.calcul}?chemin=${encodeURIComponent(chemin)}`);
    if (chemin.endsWith('.json')) try { t = JSON.stringify(JSON.parse(t), null, 1); } catch (x) { /* texte brut */ }
    vue.textContent = t.length > 400000 ? t.slice(0, 400000) + '\n[…]' : t;
  }
  return [el('h2', {}, 'Résultats intermédiaires (fiche A42)'),
    el('p', { class: 'note' }, `Dossier : ${S.resultats.dossier}. Chaque variante a un fichier par étape, dans l'ordre du chapitre 6 de la méthode.`), z, vue];
}
function ongletFiche() {
  if (!S.resultats) return sansResultats();
  const r = S.resultats, retour = el('div', { class: 'note' });
  const charger_ = async (url, nom) => {
    retour.textContent = 'Préparation…';
    const rep = await fetch(url);
    if (!rep.ok) { const e = await rep.json().catch(() => ({})); retour.textContent = e.erreur || rep.statusText; return; }
    const a = el('a', { href: URL.createObjectURL(await rep.blob()), download: nom }); document.body.append(a); a.click(); a.remove(); retour.textContent = '';
  };
  const id = r.projet.identifiant;
  return [el('h2', {}, 'Fiche de synthèse et RSNat'),
    el('div', { class: 'carte' }, el('h3', {}, 'Fiche de synthèse'),
      el('p', { class: 'note' }, 'Fiche au papier de l\'éditeur de la méthode : identification, version de la méthode et des données, empreinte de contrôle, attestation au permis, indicateurs, incertitude.'),
      el('div', { class: 'ligne' }, el('button', { class: 'principal', onclick: () => charger_(`/api/fiche/${S.calcul}.pdf`, `fiche_synthese_${id}.pdf`) }, 'Fiche en PDF'),
        el('button', { onclick: () => charger_(`/api/fiche/${S.calcul}.docx`, `fiche_synthese_${id}.docx`) }, 'Fiche en Word')), retour),
    el('div', { class: 'carte' }, el('h3', {}, 'RSNat'),
      el('p', { class: 'note' }, 'Récapitulatif standardisé, validé contre ses schémas XSD et JSON. Le bloc Attestation_Permis est l\'extrait déposé au permis de construire.'),
      el('div', { class: 'ligne' }, el('button', { onclick: () => charger_(`/api/rsnat/${S.calcul}.xml`, `rsnat_${id}.xml`) }, 'RSNat XML'),
        el('button', { onclick: () => charger_(`/api/rsnat/${S.calcul}.json`, `rsnat_${id}.json`) }, 'RSNat JSON')),
      tableauLecture([['Méthode', r.versions.methode], ['Moteur', r.versions.moteur], ['Données (SHA-256)', r.versions.donnees],
        ['Graine', String(r.versions.graine)], ['Empreinte des entrées', r.empreinte.entrees], ['Empreinte des sorties', r.empreinte.sorties],
        ['Conformité aux schémas', Object.values(r.erreurs_schema).every(l => !l.length) ? 'valide (XSD et JSON)' : 'non conforme, voir le journal']]))];
}

// ------------------------------------------------------------------ démarrage
async function demarrer() {
  S.ref = await api('/api/referentiel');
  $('#bNouveau').onclick = () => { if (!S.modifie || confirm('Abandonner les modifications ?')) charger(projetVide()); };
  $('#bOuvrir').onclick = () => $('#fOuvrir').click();
  $('#fOuvrir').onchange = async ev => { const f = ev.target.files[0]; if (!f) return; try { charger(JSON.parse(await f.text())); } catch (x) { alert('Fichier projet illisible : ' + x.message); } ev.target.value = ''; };
  $('#bExemple').onclick = async () => { if (!S.modifie || confirm('Abandonner les modifications ?')) charger(await api('/api/exemple')); };
  $('#bEnregistrer').onclick = () => { telecharger(`${S.projet.projet.identifiant || 'projet'}.opennat.json`, JSON.stringify(S.projet, null, 1)); S.modifie = false; afficher(); };
  window.addEventListener('beforeunload', ev => { if (S.modifie) { ev.preventDefault(); ev.returnValue = ''; } });
  charger(projetVide());
}
demarrer();
