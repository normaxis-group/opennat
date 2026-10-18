# Lot 0 - Inventaire des sources : relations pression-réponse et paramètres écologiques (méthode Vi-BCN, outil OpenNat)

Date de l'inventaire : 17 octobre 2026.

Conventions de vérification employées dans ce document :
- « page ouverte avec WebFetch » : le contenu de la page ou du PDF a été lu par l'outil de lecture de pages ; les valeurs relevées proviennent de ce contenu, avec l'emplacement indiqué quand il est connu.
- « PDF téléchargé et lu intégralement » : le fichier a été téléchargé dans l'espace de travail et son texte extrait (pdftotext) ; les numéros de page cités sont ceux du PDF.
- « vu dans les résultats de recherche » : seule la référence (titre, revue) a été vue dans une liste de résultats WebSearch ; aucune valeur n'en est tirée.
- « métadonnées Crossref ou Europe PMC » : la référence bibliographique et, le cas échéant, le résumé ont été vérifiés par l'API Crossref (api.crossref.org) ou Europe PMC (ebi.ac.uk) ; les valeurs citées viennent alors du résumé seulement.
- « non vérifié » : la valeur est demandée dans la commande mais n'a pas pu être lue dans une source ouverte ; elle n'est pas à utiliser.

Limite générale de la session : le quota de recherches web a été atteint en fin de travail ; les thèmes G (guides Cerema eaux pluviales) et F (FLL, DESTISOL en texte intégral) restent partiellement documentés, voir le résumé final.

Rappel pour l'usage par la méthode : la quasi-totalité des sources ci-dessous sont établies à l'échelle du paysage ou de la région (mailles de 0,5 degré pour GLOBIO, taches de 1 à 140 ha pour Beninde et al., corridors routiers de plusieurs kilomètres pour Benítez-López et al.). Leur transposition à l'échelle de la parcelle (0,1 à 5 ha) est une extrapolation qui doit être explicitée dans la méthode.

---

## Thème A. Relation aire-espèces et taille des taches

## Fiche : Drakare, Lennon, Hillebrand 2006, méta-analyse des relations aire-espèces
- Objet : méta-analyse quantitative de 794 relations aire-espèces (SAR) couvrant organismes, habitats et localisations variés ; test des facteurs qui modifient la pente (z) et la force de la SAR.
- Référence complète (revue, volume, pages, DOI) : Drakare S., Lennon J.J., Hillebrand H. (2006). The imprint of the geographical, evolutionary and ecological context on species-area relationships. Ecology Letters 9 (2) : 215-227. DOI 10.1111/j.1461-0248.2005.00848.x.
- URL (préciser) : https://doi.org/10.1111/j.1461-0248.2005.00848.x ; la page éditeur (Wiley) et PubMed n'ont pas pu être ouvertes (erreur de chargement et contrôle anti-robot). Référence et résumé vérifiés par métadonnées Crossref et Europe PMC.
- Contenu et valeurs disponibles : d'après le résumé, 794 SAR ; la pente et l'ajustement dépendent du schéma d'échantillonnage (emboîté ou indépendant), de l'échelle spatiale, du type d'organisme et d'habitat ; pentes plus fortes aux basses latitudes et pour les organismes de grande taille ; pas de différence générale entre domaines terrestre et aquatique. Aucune valeur numérique de z n'est donnée dans le résumé.
- Licence et accessibilité : article payant (Wiley) ; pas de version PMC repérée ; Europe PMC indique « OA : N ».
- Limites pour une méthode à l'échelle de la parcelle : la méta-analyse porte sur des SAR de toutes échelles, y compris des échantillonnages emboîtés qui ne correspondent pas à des « îlots » d'habitat isolés ; la valeur moyenne agrège des contextes très hétérogènes ; le texte intégral (tableaux de z par type) n'a pas pu être lu.
- Nature : méta-analyse.
- Valeurs clés relevées :
  - 794 SAR analysées (résumé, Crossref et Europe PMC).
  - z moyen : non vérifié directement dans l'article. Une valeur de z moyen de 0,24 attribuée à Drakare et al. 2006 (plage 0 à environ 1) est rapportée dans le tableau 4 de Matthews et al. 2016 (voir fiche suivante, page ouverte avec WebFetch), avec la réserve que cette moyenne inclut des SAR emboîtées.
  - Valeurs par type d'habitat ou par échelle : non vérifié.

## Fiche : Matthews, Guilhaumon, Triantis, Borregaard, Whittaker 2016, SAR des îles d'habitat et des vraies îles
- Objet : comparaison de 20 modèles de SAR sur 207 jeux de données d'îles d'habitat (fragments terrestres, dont îlots urbains) et 601 jeux de vraies îles (Triantis et al. 2012) ; valeurs de z du modèle puissance par type de système.
- Référence complète : Matthews T.J., Guilhaumon F., Triantis K.A., Borregaard M.K., Whittaker R.J. (2016). On the form of species-area relationships in habitat islands and true islands. Global Ecology and Biogeography 25 (7) : 847-858. DOI 10.1111/geb.12269.
- URL : https://research.birmingham.ac.uk/files/46558191/Matthews_et_al_On_the_form_of_species_area_relationships_Global_Ecology_and_Biogeography.pdf (dépôt institutionnel de l'université de Birmingham ; PDF ouvert avec WebFetch).
- Contenu et valeurs disponibles : 207 jeux d'îles d'habitat (182 retenus pour la comparaison de modèles, au moins 7 îles chacun) ; 601 jeux de vraies îles (193 océaniques, 353 de plateau continental, 55 puis 66 de plans d'eau intérieurs) ; médianes et quartiles de z ; comparaison par type d'habitat (forêt, urbain, sommets) ; effet de l'échelle (z décroît quand le rapport des aires augmente) ; tableau 4 comparant les z de la littérature.
- Licence et accessibilité : article Wiley ; version auteur en accès libre sur le dépôt de Birmingham.
- Limites pour une méthode à l'échelle de la parcelle : les « îles d'habitat » sont des fragments de taille très variable, le plus souvent bien supérieurs à une parcelle ; z décroît avec l'étendue d'échelle, donc une valeur unique de z n'est pas transposable sans calibration ; les auteurs recommandent explicitement de calibrer z au contexte plutôt que d'utiliser 0,25.
- Nature : source primaire (analyse de synthèse de jeux de données).
- Valeurs clés relevées (page ouverte avec WebFetch) :
  - z médian des îles d'habitat : 0,22 (Q1-Q3 : 0,16-0,32), sur 135 jeux avec z significatif.
  - z médian des vraies îles : 0,29 (Q1-Q3 : 0,20-0,40) ; par type : océaniques 0,35, plateau continental 0,28, plans d'eau intérieurs 0,28.
  - z médian par type d'île d'habitat : forêt 0,20 ; urbain 0,27 ; sommets 0,30 (seule la différence forêt-urbain est significative).
  - Pas de différence significative de z entre plantes, vertébrés et invertébrés.
  - Modèle puissance meilleur modèle pour 24 % des 182 jeux (N = 44), premier au classement général.
  - Tableau 4 : z moyen de 0,24 pour Drakare et al. 2006 ; z moyen de 0,32 (plage 0,06 à 1,31) pour Triantis et al. 2012.

## Fiche : Triantis, Guilhaumon, Whittaker 2012, SAR insulaire : biologie et statistique
- Objet : comparaison de 20 modèles de SAR insulaire sur 601 jeux de données d'îles terrestres ; forme dominante de la relation et variation des paramètres z et c.
- Référence complète : Triantis K.A., Guilhaumon F., Whittaker R.J. (2012). The island species-area relationship: biology and statistics. Journal of Biogeography 39 (2) : 215-231. DOI 10.1111/j.1365-2699.2011.02652.x.
- URL : https://repositorio.uac.pt/handle/10400.3/1807 (notice du dépôt de l'université des Açores, page ouverte avec WebFetch ; PDF en accès restreint). Référence confirmée par Crossref.
- Contenu et valeurs disponibles : 601 jeux, 465 ajustements adéquats ; le modèle puissance est premier ; forme le plus souvent convexe sans asymptote ; z et c varient avec le type de système insulaire et le taxon (résumé). Les valeurs de z par type ne sont pas dans la notice.
- Licence et accessibilité : article payant (Wiley) ; dépôt en accès restreint (demande de copie).
- Limites pour une méthode à l'échelle de la parcelle : vraies îles, donc matrice totalement hostile ; z plus élevé que pour les îles d'habitat (Matthews et al. 2016) ; non transposable tel quel aux parcelles urbaines insérées dans une matrice partiellement perméable.
- Nature : source primaire (analyse de synthèse).
- Valeurs clés relevées :
  - 601 jeux de données, 465 ajustements adéquats (notice du dépôt, page ouverte).
  - z moyen du modèle puissance 0,32, plage 0,06 à 1,31 : valeur rapportée par Matthews et al. 2016 (tableau 4, page ouverte), non lue dans l'article original lui-même.

## Fiche : Beninde, Veith, Hochkirch 2015, la biodiversité en ville a besoin d'espace
- Objet : première méta-analyse mondiale des facteurs de variation intra-urbaine de la biodiversité (75 villes) ; effets de la surface des taches, des corridors, de la structure de la végétation et des autres variables locales et paysagères ; seuils de surface rapportés par la littérature.
- Référence complète : Beninde J., Veith M., Hochkirch A. (2015). Biodiversity in cities needs space: a meta-analysis of factors determining intra-urban biodiversity variation. Ecology Letters 18 (6) : 581-592. DOI 10.1111/ele.12427.
- URL : https://www.uni-trier.de/fileadmin/fb6/prof/BIO/Hochkirch/Beninde_et_al-2015-Ecology_Letters.pdf (PDF du dépôt de l'université de Trèves, page ouverte avec WebFetch). Référence confirmée par Crossref.
- Contenu et valeurs disponibles : 3 956 publications examinées, 87 retenues ; 2 021 combinaisons facteur x mesure x taxon x ville ; jeu « détaillé » de 331 combinaisons (24 publications) et jeu « généralisé » de 1 690 entrées (87 publications) ; 938 combinaisons sur les oiseaux ; modèles à effets aléatoires sur 27 facteurs pour la richesse spécifique ; coefficients de corrélation résumés ; seuils de surface relevés dans les études sources ; hétérogénéité (I²).
- Licence et accessibilité : article Wiley sous copyright (© 2015 John Wiley & Sons Ltd/CNRS) ; copie en accès libre sur le dépôt de Trèves ; pas de licence ouverte indiquée.
- Limites pour une méthode à l'échelle de la parcelle : jeu de données biaisé vers les oiseaux des régions tempérées ; les seuils de surface (4,4 ha, 26,7 ha, 53,3 ha) dépassent la taille d'une parcelle ordinaire, ce qui signifie qu'à l'échelle d'un projet la contribution à la richesse passe surtout par la connexion à des taches plus grandes ; les corrélations résumées ne sont pas des fonctions dose-réponse continues.
- Nature : méta-analyse.
- Valeurs clés relevées (page ouverte avec WebFetch) :
  - Surface de la tache et corridors : effets résumés les plus forts, coefficients de corrélation supérieurs à 0,6 dans les deux cas.
  - Surface (richesse spécifique) : n = 22 entrées, 6 niveaux taxonomiques, I² = 86,65 %, Tau² = 0,19.
  - Corridors (richesse) : n = 5, I² = 0 %.
  - Effets de la surface par taxon : oiseaux 0,76 (n = 10), insectes 0,62 (n = 6), plantes 0,52 (n = 4).
  - Structure de la végétation : n = 10 (richesse), I² = 41,21 % ; pas de r résumé chiffré dans le texte extrait.
  - « % sealed » (imperméabilisation) : n = 17, I² = 85,25 %, sans r résumé chiffré dans le texte extrait.
  - Seuils de surface rapportés par les études sources : plage 1 à 140 ha ; moyenne 26,7 ha (± 7,4 ET, n = 24) ; seuils « hauts » pour les espèces sensibles à la surface 53,3 ha (± 12,1, n = 11) ; seuils « bas » pour les espèces adaptées à la ville 4,4 ha (± 0,85, n = 13) ; différence significative (W = 143, p < 0,001).
  - Recommandation : sites de plus de 50 ha nécessaires pour éviter la perte rapide des espèces sensibles à la surface (résumé, confirmé par Crossref).
  - 15 effets résumés significativement positifs, aucun négatif ; variables biotiques, locales et de gestion plus importantes que paysagères, abiotiques ou de conception.
  - Chiffres paysagers cités d'autres sources : déclin rapide de la richesse sous 10 % de couvert végétal (Radford et al. 2005) ; couvert d'espaces verts des villes européennes 2 à 46 % (Fuller et Gaston 2009).

---

## Thème B. Infrastructures, routes, clôtures

## Fiche : Benítez-López, Alkemade, Verweij 2010, méta-analyse des effets des infrastructures sur mammifères et oiseaux
- Objet : méta-analyse des effets de la proximité des routes et autres infrastructures sur l'abondance des oiseaux et des mammifères, exprimés en abondance moyenne des espèces (MSA) relative aux distances non perturbées ; fonctions distance-effet.
- Référence complète : Benítez-López A., Alkemade R., Verweij P.A. (2010). The impacts of roads and other infrastructure on mammal and bird populations: a meta-analysis. Biological Conservation 143 (6) : 1307-1316. DOI 10.1016/j.biocon.2010.02.009.
- URL : https://dspace.library.uu.nl/bitstream/handle/1874/203524/verweij-impacts_2010.pdf?sequence=2 (PDF du dépôt de l'université d'Utrecht, page ouverte avec WebFetch) ; page de présentation GLOBIO https://www.globio.info/the-impacts-of-roads-and-other-infrastructure-on-mammal-and-bird-populations (ouverte avec WebFetch). Référence et résumé confirmés par Europe PMC.
- Contenu et valeurs disponibles : 49 études (27 oiseaux, 22 mammifères), 90 jeux de données, 2 107 points, 201 espèces d'oiseaux et 33 de mammifères ; MSA groupées par classes de distance avec IC 95 % ; méta-régressions (log-distance pour les oiseaux ; distance + couvert forestier pour les mammifères) ; hétérogénéité et biais de publication.
- Licence et accessibilité : article Elsevier payant ; version en accès libre sur le dépôt d'Utrecht.
- Limites pour une méthode à l'échelle de la parcelle : les distances d'effet (centaines de mètres à kilomètres) dépassent l'emprise d'un projet, donc l'effet route doit être traité comme une pression externe appliquée à la parcelle et non comme un paramètre interne ; forte hétérogénéité (I² 96,6 % oiseaux, 90,7 % mammifères) et biais de publication détecté ; biais géographique Europe-Amérique du Nord ; pas d'effet détectable de l'intensité du trafic sur un petit sous-ensemble (10 jeux).
- Nature : méta-analyse.
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Oiseaux : MSA groupée 0,678 (IC 95 % 0,636-0,720) dans une zone d'environ 2 600 m ; déclin de 28 à 36 %.
  - Mammifères : MSA groupée 0,675 (IC 0,608-0,742) dans une zone d'environ 17 000 m ; déclin de 25 à 38 %.
  - Distances d'effet : oiseaux jusqu'à environ 1 km ; mammifères jusqu'à environ 5 km ; petits mammifères quelques mètres ; grands mammifères jusqu'à plusieurs centaines de mètres (plusieurs km pour le renne).
  - MSA oiseaux par classe de distance : moins de 10 m 0,398 (0,146-0,651) ; 15-35 m 0,486 (0,311-0,661) ; 90-100 m 0,622 (0,480-0,763) ; 1 000-1 075 m 0,836 (0,681-0,991) ; 1 800-2 000 m 1,000 (0,905-1,095).
  - MSA mammifères par classe : 10-25 m 0,711 ; 30-50 m 0,565 ; 75-100 m 0,396 ; 110-180 m 0,837 ; 1 050-2 200 m 0,579 ; 4 500-5 000 m 0,867 ; 9 500-11 000 m 1,000 (séquence non monotone, les auteurs s'appuient sur les courbes de régression).
  - Effets plus étendus en milieu ouvert qu'en forêt (visibilité de l'infrastructure).
  - Rapaces (Accipitriformes, Falconiformes) non affectés ou plus abondants près des infrastructures.
  - Usage dans GLOBIO 3.5 : MSA moyenne de 0,66 pour oiseaux et mammifères dans une zone d'impact de 1 km, convertie en MSA infrastructure de 0,78 pour l'ensemble des groupes (voir fiche GLOBIO 3.5, thème I).

## Fiche : Forman & Alexander 1998, les routes et leurs effets écologiques majeurs
- Objet : revue de synthèse des effets écologiques des routes ; concept de « road-effect zone » ; distances d'effet sur les oiseaux selon le trafic (études néerlandaises de Reijnen et al.) ; seuils de bruit ; seuils de densité routière.
- Référence complète : Forman R.T.T., Alexander L.E. (1998). Roads and their major ecological effects. Annual Review of Ecology and Systematics 29 : 207-231. DOI 10.1146/annurev.ecolsys.29.1.207.
- URL : https://www.leg.mn.gov/docs/2015/other/150681/PFEISref_1/Forman%20and%20Alexander%201998.pdf (copie déposée par la législature du Minnesota, page ouverte avec WebFetch). Référence et résumé confirmés par Crossref.
- Contenu et valeurs disponibles : largeur de la zone d'effet (dizaines à centaines de mètres), distances d'effet sur les oiseaux pour 10 000 et 50 000 véhicules/jour en bois et en prairie, seuils de bruit en dB, densités routières seuils, proportion de territoire affecté, dimensions d'ouvrages de franchissement, distances d'effet des polluants.
- Licence et accessibilité : article Annual Reviews payant ; copie en accès libre sur le site de la législature du Minnesota.
- Limites pour une méthode à l'échelle de la parcelle : valeurs issues de quelques études pionnières (Pays-Bas) et souvent exprimées en dB non pondérés ; synthèse de 1998, antérieure aux méta-analyses ; les seuils de densité routière sont des indicateurs de paysage.
- Nature : revue de synthèse (source secondaire).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Zones d'effet des routes : « dizaines ou centaines de mètres », asymétriques ; 15 à 20 % du territoire des États-Unis écologiquement affecté ; 10 à 20 % des Pays-Bas.
  - Distances d'effet sur les oiseaux (espèces les plus sensibles, vitesse 120 km/h) : bois 305 m à 10 000 véh./jour et 810 m à 50 000 ; prairie 365 m et 930 m.
  - Déclin de la plupart des espèces de prairie dès 5 000 véh./jour ou moins ; densité totale d'oiseaux réduite d'environ un tiers dans la zone affectée ; 60 % des espèces à densité réduite près des autoroutes.
  - Seuils de bruit : début du déclin des oiseaux forestiers à 42 dB en moyenne, des oiseaux de prairie à 48 dB ; espèce forestière la plus sensible (coucou) 35 dB ; espèce de prairie la plus sensible (barge à queue noire) 43 dB.
  - Densité routière : environ 0,6 km/km² comme maximum apparent pour un paysage fonctionnel avec grands prédateurs ; effets hydrologiques dès 2 à 3 km/km².
  - Barrières : routes peu circulées de 6 à 15 m de large réduisent le franchissement des petits mammifères à moins de 10 % des mouvements internes ; routes de 2,5 m bloquent carabes et lycoses.
  - Grands mammifères souvent moins denses à 100-200 m des routes.
  - Ouvrages : passages supérieurs 30-50 m au centre et 50-80 m aux extrémités (140 et 200 m en Suisse) ; passages inférieurs 8-30 m de large et au moins 2,5 m de haut ; tunnels à amphibiens 30-100 cm.

## Fiche : Jakes, Jones, Paige, Seidler, Huijser 2018, « A fence runs through it »
- Objet : essai de perspective appelant à une « écologie des clôtures » ; état des connaissances sur les effets des clôtures sur la faune (mortalité, barrière, fragmentation) et sur leur rôle de conservation.
- Référence complète : Jakes A.F., Jones P.F., Paige L.C., Seidler R.G., Huijser M.P. (2018). A fence runs through it: a call for greater attention to the influence of fences on wildlife and ecosystems. Biological Conservation 227 : 310-318. DOI 10.1016/j.biocon.2018.09.026.
- URL : https://jhwildlife.org/wp-content/uploads/2019/01/Fence-paper-by-Paige-et-al-1.pdf (copie déposée par Jackson Hole Wildlife Foundation, page ouverte avec WebFetch). Référence confirmée par Crossref.
- Contenu et valeurs disponibles : article de perspective, non systématique ; pas de taux de mortalité par km, pas de hauteurs ou d'espacements de fils recommandés chiffrés ; tableau 1 des types de clôtures (barbelé 3 à 5 fils ; clôtures de conservation grillagées d'environ 2 m de haut, souvent électrifiées) ; comparaison de linéaire dans le sud de l'Alberta.
- Licence et accessibilité : article Elsevier payant ; copie en accès libre sur le site de la fondation.
- Limites pour une méthode à l'échelle de la parcelle : aucune relation dose-réponse ; les auteurs disent eux-mêmes que les taux de mortalité sont « largement inconnus » ; utile seulement pour justifier qualitativement un facteur « obstacle » dans la méthode, pas pour le chiffrer.
- Nature : essai de synthèse (source secondaire, non systématique).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Clôtures du sud de l'Alberta : linéaire environ 2 fois celui de toutes les routes, 16 fois celui des routes revêtues, 7 fois les chemins à deux ornières, 4 fois les routes en gravier.
  - Cartographie des clôtures par imagerie avec environ 94 % de précision (Seward et al. 2012).
  - Clôtures de conservation : grillage d'environ 2 m de haut (tableau 1).
  - Mortalité par km de clôture : non vérifié (non fourni par l'article).
  - Hauteur maximale et espacement des fils pour une clôture « perméable à la faune » : non vérifié (non fourni par l'article).

---

## Thème C. Lumière artificielle nocturne

## Fiche : Sanders, Frago, Kehoe, Patterson, Gaston 2021, méta-analyse des impacts biologiques de l'ALAN
- Objet : méta-analyse multi-niveaux (MCMCglmm) de 126 études et 1 304 tailles d'effet sur les impacts de la lumière artificielle nocturne sur la physiologie, la phénologie, l'activité journalière, les traits d'histoire de vie et les populations/communautés ; test d'une relation dose-réponse avec l'éclairement.
- Référence complète : Sanders D., Frago E., Kehoe R., Patterson C., Gaston K.J. (2021). A meta-analysis of biological impacts of artificial light at night. Nature Ecology & Evolution 5 (1) : 74-81. DOI 10.1038/s41559-020-01322-x.
- URL : manuscrit accepté https://ore.exeter.ac.uk/rest/bitstreams/169056/retrieve (dépôt ORE de l'université d'Exeter, PDF ouvert avec WebFetch) ; notice https://ore.exeter.ac.uk/repository/handle/10871/123068 (ouverte) ; notice Durham https://durham-repository.worktribe.com/output/1223651/... (ouverte) ; page éditeur Nature non ouverte (erreur), page miroir Springer ouverte mais aperçu seulement ; données Dryad https://datadryad.org/dataset/doi:10.5061/dryad.wpzgmsbjn (ouverte). Volume et pages confirmés par Crossref.
- Contenu et valeurs disponibles : effectifs par catégorie, direction et significativité des effets par sous-catégorie (les valeurs numériques de Hedges' d sont dans les figures 2 et 3, non lisibles dans le texte extrait) ; méta-régression sur l'intensité lumineuse ; biais de publication.
- Licence et accessibilité : article payant chez Nature (« exclusive licence to Springer Nature ») ; manuscrit accepté en libre accès sur ORE Exeter après embargo (mai 2021) ; données et code sur Dryad.
- Limites pour une méthode à l'échelle de la parcelle : pas de relation dose-réponse générale avec l'éclairement (donc impossible de dériver une fonction effet = f(lux) de cette source) ; spectre non testé comme modérateur ; études de terrain surtout européennes et nord-américaines ; les effets sur les fonctions écosystémiques n'ont pas pu être analysés.
- Nature : méta-analyse.
- Valeurs clés relevées (manuscrit ouvert avec WebFetch) :
  - 126 études, 1 304 tailles d'effet ; vertébrés 746, invertébrés 388, plantes 143, communautés microbiennes 24 ; 82 études de terrain, 42 de laboratoire ; terrain : Europe 46, Amérique du Nord 17, Australie 7.
  - Observations par catégorie : physiologie 338 (35 études), phénologie 35 (7), histoire de vie 411 (58), activité journalière 139 (27), population/communauté 381 (42).
  - Effets significatifs (IC de crédibilité 95 % excluant 0) : niveaux hormonaux (mélatonine surtout, n = 145) nettement réduits ; début d'activité (n = 52) avancé ; fin d'activité (n = 23) retardée ; cognition (n = 30) négative ; prédation (n = 23) positive ; nombre de descendants (n = 14) négatif ; orientation vers la mer des tortues (n = 79) fortement négative.
  - Pas d'effet net : réponse immunitaire, stress, phénologie (effets dans les deux sens), abondance (n = 256, très large dispersion), activité des chauves-souris (n = 99), diversité des communautés (n = 7).
  - Intensités testées : environ 0 à 100 lux, concentrées vers 1 à 2 lux ; aucune relation entre intensité et taille d'effet dans la méta-régression toutes catégories confondues ; impact possiblement marqué même à faible intensité.
  - Effets d'histoire de vie et d'activité plus négatifs chez les espèces nocturnes ; effets physiologiques plus négatifs chez les diurnes.

## Fiche : Gaston, Bennie, Davies, Hopkins 2013, impacts écologiques de la pollution lumineuse : cadre mécaniste
- Objet : revue conceptuelle proposant un cadre mécaniste croisant les modes d'altération des régimes lumineux (espace, temps, spectre) et les modes d'action de la lumière (ressource, information) ; identification des lacunes (seuils d'intensité, étendue spatiale).
- Référence complète : Gaston K.J., Bennie J., Davies T.W., Hopkins J. (2013). The ecological impacts of nighttime light pollution: a mechanistic appraisal. Biological Reviews 88 (4) : 912-927. DOI 10.1111/brv.12036.
- URL : notice https://research.bangor.ac.uk/en/publications/the-ecological-impacts-of-nighttime-light-pollution-a-mechanistic/ (page ouverte avec WebFetch) ; référence et résumé confirmés par Crossref. Texte intégral non ouvert.
- Contenu et valeurs disponibles : d'après le résumé, cadre conceptuel ; effets à tous les niveaux d'organisation ; effets possibles à faible niveau de lumière ; lacunes sur les seuils d'intensité et l'extension spatiale autour des luminaires. Aucune valeur numérique dans le résumé.
- Licence et accessibilité : la notice de Bangor indique une licence CC BY (accès libre).
- Limites pour une méthode à l'échelle de la parcelle : source conceptuelle, sans relation dose-réponse ; sert à structurer les mécanismes (lumière ressource / lumière information), pas à chiffrer.
- Nature : revue de synthèse.
- Valeurs clés relevées : aucune valeur numérique dans le résumé (page ouverte) ; valeurs du texte intégral non vérifiées.

## Fiche : Gaston, Davies, Bennie, Hopkins 2012, réduire les conséquences écologiques de la pollution lumineuse : options
- Objet : revue des options de réduction (maintien de zones sombres, limitation de la durée, de l'intensité et du spectre) ; ordres de grandeur des éclairements naturels et artificiels ; exemples de seuils de réponse biologique.
- Référence complète : Gaston K.J., Davies T.W., Bennie J., Hopkins J. (2012). Reducing the ecological consequences of night-time light pollution: options and developments. Journal of Applied Ecology 49 (6) : 1256-1266. DOI 10.1111/j.1365-2664.2012.02212.x. PMCID PMC3546378.
- URL : https://pmc.ncbi.nlm.nih.gov/articles/PMC3546378 (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : éclairements naturels (pleine lune, ciel étoilé, ciel couvert), éclairement sous éclairage public, exemples de réponses à faible éclairement, tableau 1 des températures de couleur par type de lampe, sensibilités visuelles comparées (tableau 2), croissance de la pollution lumineuse.
- Licence et accessibilité : accès libre (Wiley Open Access, article en PMC).
- Limites pour une méthode à l'échelle de la parcelle : les auteurs indiquent que peu d'études ont quantifié des seuils d'intensité ou de surface, probablement variables selon les espèces ; les exemples de seuils sont ponctuels (une espèce, une réponse).
- Nature : revue de synthèse.
- Valeurs clés relevées (page PMC ouverte avec WebFetch) :
  - Éclairement naturel : pleine lune ciel clair environ 0,1-0,3 lux ; ciel étoilé clair environ 0,001 lux ; ciel nocturne couvert environ 0,00003-0,0001 lux.
  - Éclairage public (incandescent, fluorescent, décharge) : 10 à 60 lux au niveau de la rue, décroissance rapide avec la distance au mât.
  - Réponses à faible éclairement : floraison de plantes ornementales modifiée et croissance végétative accrue vers 10 lux ; chant matinal du merle d'Amérique avancé sous 4 lux.
  - Croissance de la pollution lumineuse : environ 6 % par an (Hölker et al. 2010).
  - Halo lumineux (skyglow) perceptible à des dizaines, voire des centaines de km ; au-delà d'environ 10 km les grandes longueurs d'onde contribuent davantage au halo.
  - Tableau 1 (CCT en K) : sodium basse pression 1 807 ; sodium haute pression 2 005-2 108 ; fluorescent 2 766-5 193 ; iodures métalliques 2 874-4 160 ; LED 1 739-8 357.
  - Exemple de géométrie : mâts de 8 m espacés de 30 m (iodures métalliques) ; LED directionnelles à 10 m espacées de 25 m.
  - Aucune relation dose-réponse quantitative générale fournie.

## Fiche : Sordello, Paquier, Daloz 2021, guide OFB « Trame noire »
- Objet : guide méthodologique de l'OFB pour identifier et mettre en oeuvre une trame noire (réseau écologique nocturne) : concepts, méthodes de cartographie de la pollution lumineuse et des zones sensibles, outils (réglementation, caractéristiques des points lumineux, organisation spatiale et temporelle), annexes (modèle de cahier des charges, modèle d'arrêté d'extinction).
- Référence complète : Sordello R., Paquier F., Daloz A. (2021). Trame noire : méthodes d'élaboration et outils pour sa mise en oeuvre. Office français de la biodiversité, collection Comprendre pour agir, 112 p. ISBN web 978-2-38170-084-7 ; ISBN imprimé 978-2-38170-085-4 ; référence documentaire DOC00083892. Édition mars 2021.
- URL : notice https://ofb.gouv.fr/doc/trame-noire-methodes-elaboration-et-outils-pour-sa-mise-en-oeuvre (page ouverte avec WebFetch) ; PDF https://oai-gem.ofb.fr/exl-php/document-affiche/ofb_recherche_oai/OUVRE_DOC/60520?fic=PUBLI/R20/47.pdf (ouverture refusée : robots.txt) ; traduction anglaise de synthèse « Dark Infrastructure: an ecological network for night-time wildlife » (septembre 2021) https://trameverteetbleue.fr/sites/default/files/references_bibliographiques/dark_infrastructure_an_ecological_network_september_2021.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : le PDF français n'a pas pu être lu ; les valeurs ci-dessous proviennent de la synthèse anglaise des mêmes auteurs (29 références citées), qui reprend les ordres de grandeur du guide.
- Licence et accessibilité : publication OFB gratuite ; le site ofb.gouv.fr indique une licence etalab-2.0 par défaut, non confirmée pour ce guide précis.
- Limites pour une méthode à l'échelle de la parcelle : guide d'échelle territoriale (commune, intercommunalité, parc) ; les seuils de sensibilité par espèce sont qualifiés par les auteurs eux-mêmes de lacunaires et disponibles pour quelques espèces seulement ; la partie « outils » donne des recommandations techniques (température de couleur, extinction) transposables à un projet, mais sans fonction dose-réponse.
- Nature : guide technique.
- Valeurs clés relevées (synthèse anglaise ouverte avec WebFetch ; pagination du guide français non vérifiée) :
  - Croissance de la surface éclairée : environ 2,2 % par an (2012-2016), radiance + 1,8 % par an (Kyba et al. 2017) ; environ 6 % par an dans d'autres études.
  - Plus de 80 % de la population mondiale et 99 % des Européens sous un ciel pollué (Falchi et al. 2016).
  - Visites nocturnes d'insectes aux plantes réduites d'environ 60 %, fructification réduite de 10 % (Knop et al. 2017).
  - Églises éclairées : 2 à 3 fois moins de colonies de chauves-souris (Rydell et al. 2017).
  - Évitement des lampadaires par certaines chauves-souris jusqu'à 50 m (Azam et al. 2018).
  - Chute des feuilles perturbée dès 10 lux (Matzke 1936) ; bornes solaires de moins de 1 lux à quelques lux agissant comme pièges à insectes (Eccard et al. 2018).
  - Température de couleur recommandée : LED blanc chaud 2 400 K ou moins ; LED ambre/orange 2 000 K ou moins comme compromis (efficacité énergétique environ moitié d'une LED 3 000 K).
  - Bandes spectrales : UV < 380 nm ; violet 380-450 ; bleu 450-500 ; vert 500-550 ; jaune 550-600 ; orange 600-650 ; rouge 650-750 nm ; bleu, vert et rouge apparaissent comme les plus impactants.
  - Hauteur des mâts, espacement, réflectance : non chiffrés dans la synthèse.

## Fiche : Sordello et al. 2022, plaidoyer pour une « dark infrastructure » mondiale
- Objet : article de synthèse et de position (22 auteurs) sur l'intégration de la pollution lumineuse dans les réseaux écologiques, avec exemples pratiques et pistes de développement.
- Référence complète : Sordello R., Busson S., Cornuau J.H., Deverchère P., Faure B., Guetté A., Hölker F., Kerbiriou C., Lengagne T., Le Viol I., Longcore T., Moeschler P., Ranzoni J., Ray N., Reyjol Y., Roulet Y., Schroer S., Secondi J., Valet N., Vanpeene S., Vauclair S. (2022). A plea for a worldwide development of dark infrastructure for biodiversity - Practical examples and ways to go forward. Landscape and Urban Planning 219 : 104332. DOI 10.1016/j.landurbplan.2021.104332.
- URL : notice UCLA IoES https://www.ioes.ucla.edu/publication/considering-light-pollution-in-ecological-networks-... (page ouverte avec WebFetch, métadonnées seulement) ; page ScienceDirect refusée (robots.txt) ; notice eScholarship vide. Titre, volume et numéro d'article confirmés par Crossref (le titre Crossref diffère du titre de travail « Considering light pollution in ecological networks » affiché par UCLA).
- Contenu et valeurs disponibles : résumé non lu ; aucune valeur relevée.
- Licence et accessibilité : Elsevier (licence TDM Elsevier selon Crossref) ; statut d'accès non vérifié.
- Limites pour une méthode à l'échelle de la parcelle : article de cadrage territorial.
- Nature : revue de synthèse / position.
- Valeurs clés relevées : aucune (non vérifié).

## Fiche : Azam et al. 2018, seuils de distance et d'éclairement des effets de l'éclairage sur l'activité des chauves-souris
- Objet : étude de terrain (France) des effets des lampadaires sur l'activité de plusieurs espèces de chauves-souris en fonction de la distance et de l'éclairement ; seuils par espèce ; recommandation de distance aux corridors.
- Référence complète : Azam C., Le Viol I., Bas Y., Zissis G., Vernet A., Julien J.-F., Kerbiriou C. (2018). Evidence for distance and illuminance thresholds in the effects of artificial lighting on bat activity. Landscape and Urban Planning 175 : 123-135. DOI 10.1016/j.landurbplan.2018.02.011.
- URL : notice HAL https://hal-univ-tlse3.archives-ouvertes.fr/hal-02532626 (accès refusé par protection anti-robot) ; page ScienceDirect refusée (robots.txt). Référence confirmée par Crossref. Valeurs relevées via le rapport EUROBATS AC24.6 (2019) https://www.eurobats.org/sites/default/files/documents/pdf/Advisory_Committee/Doc.AC24.6.Rev_.1_IWG_Bats_LightPollution.pdf (page ouverte avec WebFetch), qui résume cette étude.
- Contenu et valeurs disponibles (via EUROBATS) : effets d'attraction limités à environ 10 m pour Pipistrellus et Nyctalus ; évitement jusqu'à 25 m pour Myotis et 50 m pour Eptesicus serotinus ; plage d'éclairement mesurée 0,1-30,2 lux ; effet négatif sur Myotis sous 1 lux ; pic d'activité de P. pipistrellus et N. leisleri entre 1 et 5 lux ; recommandation : séparer les lampadaires des corridors d'au moins 50 m et limiter la lumière intrusive verticale à 0,1 lux.
- Licence et accessibilité : article Elsevier payant ; version HAL existante mais non ouverte dans cette session.
- Limites pour une méthode à l'échelle de la parcelle : une région et un contexte (France rurale/périurbaine) ; les seuils sont spécifiques aux groupes d'espèces ; valeurs lues dans une source secondaire, à confirmer dans l'article.
- Nature : source primaire (lue via source secondaire).
- Valeurs clés relevées (rapport EUROBATS ouvert avec WebFetch, citant Azam et al. 2018) : 10 m (Pipistrellus, Nyctalus) ; 25 m (Myotis) ; 50 m (E. serotinus) ; 0,1-30,2 lux ; moins de 1 lux (effet négatif Myotis) ; 1 à 5 lux (pic P. pipistrellus, N. leisleri) ; recul minimal de 50 m des corridors ; 0,1 lux de lumière intrusive maximale. Le même rapport cite Rowse et al. 2018 (Royal Society Open Science 5 : 180205) : à 25 % du flux initial, pas d'effet significatif sur P. pipistrellus ni Myotis par rapport au noir ; à 50 et 100 %, baisse de l'activité de Myotis.

## Fiche : Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses (France)
- Objet : texte réglementaire fixant les horaires d'extinction, les caractéristiques photométriques (ULR, code flux CIE n°3), les températures de couleur maximales et les densités surfaciques de flux lumineux par catégorie d'installation et par zone (agglomération, hors agglomération, espaces protégés, sites d'observation astronomique).
- Référence complète : Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, NOR TREP1831126A, JORF n°0300 du 28 décembre 2018.
- URL : page Légifrance https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037864346 (non ouverte : erreur de chargement) ; copie du texte Légifrance https://www.ville-ballancourt.fr/wp-content/uploads/sites/76/koba-documents/Arrete-du-27-decembre-2018-...-Legifrance.pdf (page ouverte avec WebFetch) ; tableau de synthèse Signify https://www.assets.signify.com/is/content/Signify/Assets/philips-lighting/france/20201119-tableau-arretes-nuisances-lumineuses.pdf (ouvert) ; page ministère https://www.ecologie.gouv.fr/arrete-du-27-decembre-2018-... (ouverte, texte partiel).
- Contenu et valeurs disponibles : articles 2 (horaires), 3 (prescriptions techniques), 4 (cours d'eau, plans d'eau, DPM, canons à lumière, lasers), 8 (dates d'application), lus dans la copie du texte.
- Licence et accessibilité : texte officiel, libre de réutilisation (Légifrance).
- Limites pour une méthode à l'échelle de la parcelle : il s'agit de prescriptions réglementaires minimales, pas de seuils écologiques ; la méthode peut s'en servir comme niveau « conformité » et graduer au-dessus (par exemple 2 400 K, extinction coeur de nuit, 0 ULR) en s'appuyant sur le guide Trame noire.
- Nature : texte réglementaire (guide technique au sens de la grille).
- Valeurs clés relevées (copie du texte ouverte avec WebFetch) :
  - Article 2 : extinction au plus tard 1 h après la fin d'activité et rallumage au plus tôt à 7 h (ou 1 h avant l'activité) pour les installations liées à une activité ; patrimoine, parcs et jardins : du coucher du soleil à 1 h au plus tard (ou 1 h après la fermeture) ; bâtiments non résidentiels et vitrines : extinction à 1 h au plus tard (ou 1 h après la fin d'activité) ; parkings annexés à une zone d'activité : extinction 2 h après la cessation de l'activité ; chantiers : du coucher du soleil à 1 h après la fin des travaux.
  - Article 3 : ULR nominal strictement inférieur à 1 % ; ULR installé strictement inférieur à 4 % ; part du flux dans le cône de 75,5° supérieure à 95 % du flux de l'hémisphère inférieur (code flux CIE n°3) ; température de couleur maximale 3 000 K (catégories a, d, e) ; densité surfacique de flux installé (lm/m², agglomération / hors agglomération) : éclairage extérieur (a) moins de 35 / 25 ; parcs et jardins (b) moins de 25 / 10 ; bâtiments non résidentiels (d) moins de 25 / 20 ; parkings (e) moins de 25 / 20 ; cheminements PMR : éclairement maximal 20 lux.
  - Espaces protégés : réserves naturelles et périmètres de protection 2 400 K (catégories a à f), 3 000 K pour les chantiers ; coeurs de parcs nationaux 2 700 K en agglomération et 2 400 K hors agglomération ; sites d'observation astronomique : chantiers 3 000 K ; ULR installé 0 % (aucun flux vers le haut) dans ces zones selon le tableau Signify.
  - Article 4 : interdiction d'éclairer directement les cours d'eau, le domaine public fluvial, lacs, étangs et domaine public maritime (sauf exceptions) ; canons à lumière de plus de 100 000 lm et lasers interdits dans les espaces naturels et sites astronomiques.
  - Hors champ : luminaires de moins de 100 lm (balisage) ; sanction jusqu'à 750 euros par installation irrégulière (page ministère).
  - Article 8 : installations nouvelles au 1er janvier 2020 ; la plupart des horaires pour l'existant au 1er janvier 2021 ; remplacement des luminaires émettant plus de 50 % du flux au-dessus de l'horizontale au 1er janvier 2025.

---

## Thème D. Bruit

## Fiche : Shannon et al. 2016, synthèse de deux décennies de recherche sur les effets du bruit sur la faune
- Objet : revue systématique et standardisée (1990-2013) des effets du bruit anthropique sur la faune terrestre et aquatique ; distribution des niveaux sonores auxquels des réponses sont documentées ; courbes cumulées « poids de la preuve ».
- Référence complète : Shannon G., McKenna M.F., Angeloni L.M., Crooks K.R., Fristrup K.M., Brown E., Warner K.A., Nelson M.D., White C., Briggs J., McFarland S., Wittemyer G. (2016). A synthesis of two decades of research documenting the effects of noise on wildlife. Biological Reviews 91 (4) : 982-1005. DOI 10.1111/brv.12207.
- URL : https://sites.warnercnr.colostate.edu/wp-content/uploads/sites/146/2020/11/biologicalreviews2015.pdf (PDF du site de Colorado State University, page ouverte avec WebFetch). Référence et résumé confirmés par Europe PMC.
- Contenu et valeurs disponibles : 2 205 articles identifiés, 242 études empiriques retenues, sous-ensemble de 131 études (69 terrestres, 62 aquatiques) avec réponse significative et niveau acoustique ; répartition taxonomique ; niveaux de réponse ; types de réponses ; qualité du reporting acoustique.
- Licence et accessibilité : article Wiley payant ; copie en accès libre sur le site de l'université.
- Limites pour une méthode à l'échelle de la parcelle : les auteurs précisent que les courbes cumulées ne sont pas des relations dose-réponse (elles comptent des études, pas des proportions d'espèces répondant) ; métriques acoustiques hétérogènes (30 % sans niveau reçu, 51 % sans pression de référence) ; biais vers oiseaux chanteurs et mammifères marins ; la médiane terrestre de 60 dB est jugée gonflée par les métriques de pic.
- Nature : revue systématique (synthèse).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Réponses de la faune terrestre dès environ 40 dBA ; 14 études terrestres (environ 20 %) rapportent des effets sous 50 dBA (résumé et texte).
  - Exemples terrestres : changements chez les oiseaux à 45 dBA et plus ; stress et reproduction réduite chez les mammifères terrestres à 52-68 dBA ; trafic au-dessus de 60 dBA affectant la vocalisation des anoures ; trafic au-dessus de 80 dBA réduisant la chasse des chauves-souris glaneuses.
  - Médiane terrestre des niveaux à effet : 60 dB (jugée surestimée par les auteurs).
  - Aquatique : 50 % des études rapportent des réponses à 125 dB re 1 µPa ou moins ; plage 67 à 195 dB.
  - Oiseaux 37 % et mammifères aquatiques 28 % du jeu de données ; poissons 15 % ; mammifères terrestres 11 % ; reptiles/amphibiens 4 % ; invertébrés 4 % ; 81 % des travaux terrestres en Amérique du Nord ou Europe.
  - Réponses terrestres : vocales 44 %, population 16 %, mouvement 15 %, physiologie 10 %, vigilance 6 %.
  - Comparaison humaine : risque d'hypertension lié à un LAeq supérieur à 55 dB ; la courbe faune terrestre s'accumule à des niveaux plus bas que la courbe de gêne rurale humaine, avec des pentes similaires.

## Fiche : Francis & Barber 2013, cadre pour comprendre les impacts du bruit sur la faune
- Objet : revue et cadre conceptuel : distinction entre bruit chronique/fréquent (masquage) et bruit intermittent/imprévisible (perçu comme menace) ; coûts de fitness directs et indirects ; appel à des métriques acoustiques appropriées pour fixer des limites.
- Référence complète : Francis C.D., Barber J.R. (2013). A framework for understanding noise impacts on wildlife: an urgent conservation priority. Frontiers in Ecology and the Environment 11 (6) : 305-313. DOI 10.1890/120183.
- URL : notice ScholarWorks Boise State https://scholarworks.boisestate.edu/bio_facpubs/385 (page ouverte avec WebFetch ; PDF d'environ 1,1 Mo disponible, non lu). Référence et résumé confirmés par Crossref.
- Contenu et valeurs disponibles : résumé et cadre conceptuel ; aucune valeur de seuil ni de distance dans la notice ou le résumé.
- Licence et accessibilité : article ESA/Wiley ; copie en dépôt institutionnel (restrictions de copyright signalées).
- Limites pour une méthode à l'échelle de la parcelle : source conceptuelle ; utile pour distinguer les types de bruit (chantier intermittent, trafic continu) dans la structure de la méthode, pas pour chiffrer.
- Nature : revue de synthèse.
- Valeurs clés relevées : aucune valeur numérique (page ouverte, résumé Crossref) ; texte intégral non vérifié.

## Fiche : Kleist, Guralnick, Cruz, Lowry, Francis 2018, bruit chronique, corticostérone et fitness chez une communauté d'oiseaux
- Objet : étude de terrain pluriannuelle (2011-2014, Nouveau-Mexique, compresseurs de gaz) sur 240 nichoirs et 3 espèces cavicoles ; effets du niveau sonore continu (Leq) sur la corticostérone, le succès d'éclosion et la croissance des oisillons ; relation non linéaire pour la croissance.
- Référence complète : Kleist N.J., Guralnick R.P., Cruz A., Lowry C.A., Francis C.D. (2018). Chronic anthropogenic noise disrupts glucocorticoid signaling and has multiple effects on fitness in an avian community. PNAS 115 (4) : E648-E657. DOI 10.1073/pnas.1709200115. PMCID PMC5789909.
- URL : https://www.greatoldbroads.org/wp-content/uploads/formidable/44/Kleist-et-al.-2018-....pdf (copie de l'« Early Edition », page ouverte avec WebFetch) ; page PMC non ouverte (contrôle anti-robot). Volume, numéro et pages confirmés par Europe PMC.
- Contenu et valeurs disponibles : design (240 nichoirs, 12 paires de sites traités/témoins, 10 nichoirs par site ; espèces : merlebleu de l'Ouest, merlebleu azuré, tyran à gorge cendrée) ; niveaux Leq en dB(F), axes des figures d'environ 50 à 85 dB(F) ; coefficients standardisés (prédicteurs centrés-réduits, IC 85 %) ; relations quadratiques pour la croissance.
- Licence et accessibilité : PNAS, licence éditeur ; données et code sur Dryad (doi:10.5061/dryad.bt45d) ; version PMC existante (OA : N selon Europe PMC, mais disponible en PMC).
- Limites pour une méthode à l'échelle de la parcelle : un système d'étude (bruit industriel continu, milieu semi-aride), niveaux en dB(F) et non dB(A), coefficients par écart-type et non par dB, donc pas de pente directement transposable ; relation non monotone (optimum apparent vers 70 dB(F)) qui interdit une fonction linéaire simple.
- Nature : source primaire.
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Corticostérone basale des femelles adultes : β = -1,120 (IC 85 % -1,966 à -0,279) ; des oisillons : β = -0,660 (-1,243 à -0,080) ; corticostérone induite par le stress chez les oisillons : β = +1,297 (0,067 à 2,538).
  - Succès d'éclosion du merlebleu de l'Ouest : β = -0,483 (-0,892 à -0,075) ; pas d'effet net pour les deux autres espèces.
  - Croissance des plumes et taille corporelle : relation quadratique, maximum vers 70 dB(F), fortement réduites au-dessus (IC 85 % -5,410 à -2,184 pour les plumes ; -2,589 à -0,499 pour la taille).
  - Pente par dB(A) : non vérifié (non fournie sous cette forme).

---

## Thème E. Collisions avec les vitrages

## Fiche : Loss, Will, Loss, Marra 2014, collisions oiseaux-bâtiments aux États-Unis
- Objet : estimation systématique de la mortalité annuelle par collision avec les bâtiments aux États-Unis à partir de 23 jeux de données, par classe de hauteur de bâtiment ; vulnérabilité spécifique à partir de plus de 92 000 cadavres.
- Référence complète : Loss S.R., Will T., Loss S.S., Marra P.P. (2014). Bird-building collisions in the United States: estimates of annual mortality and species vulnerability. The Condor: Ornithological Applications 116 (1) : 8-23. DOI 10.1650/CONDOR-13-090.1.
- URL : https://media.audubon.org/documents/loss_et_al_bird-building_collisons_condor_2014.pdf (copie Audubon, page ouverte avec WebFetch). Référence et résumé confirmés par Crossref.
- Contenu et valeurs disponibles : mortalité totale (médiane et IC 95 %), taux médian par bâtiment et par an pour 3 classes de hauteur, nombre de bâtiments par classe, parts de mortalité, espèces vulnérables, facteurs (surface vitrée, végétation, éclairage), limites.
- Licence et accessibilité : article de la Cooper Ornithological Society (BioOne), copie en accès libre sur le site d'Audubon.
- Limites pour une méthode à l'échelle de la parcelle : contexte nord-américain (migrateurs néotropicaux) ; données concentrées à l'est du Mississippi ; échantillonnage surtout en migration ; incertitude maximale sur les bâtiments de 4 à 11 étages ; les taux par bâtiment sont des médianes nationales non ajustées à la surface vitrée ou à l'environnement du site.
- Nature : méta-analyse / estimation nationale (synthèse quantitative).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Mortalité annuelle : médiane 599 millions, IC 95 % 365-988 millions ; jusqu'à environ 1,3 milliard avec l'estimation « toute l'année » pour les bâtiments bas.
  - Taux médian par bâtiment et par an (IC 95 %) : résidences (1-3 étages) 2,1 (1,3-3,1) ; bâtiments bas (4-11 étages) 21,7 (5,9-55) ; tours (12 étages et plus) 24,3 (5-76).
  - Nombre de bâtiments : environ 122,9 millions de résidences, 15,1 millions de bâtiments bas, 20 900 tours.
  - Parts : bâtiments bas environ 56 %, résidences environ 44 %, tours moins de 1 %.
  - 23 jeux de données pour la mortalité, 26 pour la vulnérabilité ; 92 869 cadavres.
  - Facteurs : mortalité croissante avec le pourcentage et la surface de vitrage, la présence et la hauteur de la végétation proche, la lumière émise par les fenêtres la nuit.

## Fiche : Klem & Saenger 2013, évaluation de signaux visuels pour prévenir les collisions
- Objet : expériences de terrain (fenêtres de 1,2 x 0,9 m, mangeoire à 10 m) comparant verre clair, verre à motifs UV (ORNILUX Mikado) et cordes verticales espacées de 10,8 cm et 8,9 cm ; comparaison avec les tests en tunnel.
- Référence complète : Klem D. Jr., Saenger P.G. (2013). Evaluating the effectiveness of select visual signals to prevent bird-window collisions. The Wilson Journal of Ornithology 125 (2) : 406-411.
- URL : https://www.birdsavers.com/product_images/WilsonJournalOfOrnithology-KlemAndSaenger.pdf (copie commerciale, page ouverte avec WebFetch). DOI non vu.
- Contenu et valeurs disponibles : nombres de collisions par traitement, pourcentages, comportements d'évitement, réflectance UV du verre testé, recommandations sur le seuil de réflectance UV.
- Licence et accessibilité : article payant (BioOne) ; copie hébergée par un fabricant de dispositifs anticollision (conflit d'intérêt potentiel de l'hébergeur, pas des auteurs).
- Limites pour une méthode à l'échelle de la parcelle : une station expérimentale, un contexte ; les auteurs soulignent que les tests en tunnel ne reproduisent pas les fenêtres installées ; pas de « règle 2 x 4 » formulée dans cet article (l'affirmation porte sur les bandes verticales à 10 cm ou moins).
- Nature : source primaire.
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Verre clair témoin : 69 collisions (62 %) ; ORNILUX Mikado sur intérieur sombre : 31 collisions, réduction de 55 % ; cordes verticales à 10,8 cm : 7 collisions (6 %) ; cordes à 8,9 cm : 5 collisions (4 %).
  - Les bandes verticales espacées de 10 cm ou moins sont efficaces (confirmation d'études antérieures).
  - Signaux UV efficaces : réflectance d'au moins 20 à 40 % entre 300 et 400 nm, adjacente à des zones absorbant l'UV ; ORNILUX ne réfléchissait que 7 % (300-380 nm) et 7-22 % (380-400 nm).
  - Traitements les plus efficaces en face externe (surface 1).
  - Durées : expérience 1 sur 75 jours, expérience 2 sur 68 jours, 63,5 h d'observation.

## Fiche : Klem 2009, prévenir les collisions oiseaux-fenêtres (travail fondateur)
- Objet : article de synthèse des travaux de Klem sur la prévention des collisions, à l'origine de la « règle 2 x 4 » (espacement des marquages).
- Référence complète : Klem D. Jr. (2009). Preventing bird-window collisions. The Wilson Journal of Ornithology 121 (2) : 314-321. DOI 10.1676/08-118.1.
- URL : https://bioone.org/doi/abs/10.1676/08-118.1 (non ouverte : protection anti-robot Incapsula). Référence confirmée par Crossref.
- Contenu et valeurs disponibles : non lu.
- Licence et accessibilité : payant (BioOne).
- Limites pour une méthode à l'échelle de la parcelle : non évaluables ici.
- Nature : source primaire / synthèse d'auteur.
- Valeurs clés relevées : règle 2 x 4 (5 cm horizontal, 10 cm vertical) : non vérifié dans cet article. La règle est documentée dans le guide ABC (fiche suivante) sous la forme « espaces horizontaux de 2 pouces ou moins et verticaux de 4 pouces ou moins ».

## Fiche : American Bird Conservancy, « Bird-Friendly Building Design » (guide, édition vers 2011)
- Objet : guide de conception de bâtiments pour réduire les collisions : mécanismes, zones à risque, règle 2 x 4, facteurs de menace des matériaux, éclairage.
- Référence complète : American Bird Conservancy. Bird-Friendly Building Design. Guide, édition non datée dans le texte lu (événements cités jusqu'en octobre 2011), au moins 57 pages. Auteurs non indiqués dans le texte (Christine Sheppard apparaît comme contact).
- URL : https://theiwrc.org/wp-content/uploads/2011/05/BirdFriendlyBuildingDesign1.pdf (copie hébergée par IWRC, page ouverte avec WebFetch) ; page « Threat Factor » ABC https://abcbirds.org/?p=24327 (ouverte) ; page LEED ABC https://abcbirds.org/strategies/leed-innovation-credit/ (ouverte) ; Model Bird-Friendly Building Guidelines ABC mars 2025 (.docx) https://abcbirds.org/wp-content/uploads/2025/10/American-Bird-Conservancy-Model-Bird-Friendly-Building-Guidelines-March-2025.docx (ouvert).
- Contenu et valeurs disponibles : estimations de mortalité, règle 2 x 4, zone de collision primaire, exigences de couverture de façade, relation surface vitrée / collisions (Klem 2009), efficacité des motifs, recommandations d'éclairage ; la page « Threat Factor » donne l'échelle ; les Model Guidelines 2025 donnent le seuil de matériau et la zone 0-100 pieds.
- Licence et accessibilité : documents gratuits de l'ONG ; copyright ABC.
- Limites pour une méthode à l'échelle de la parcelle : contexte nord-américain ; les Threat Factors par matériau ne figurent pas dans le texte lu (tableau séparé) ; les règles sont prescriptives (conformité), pas des fonctions dose-réponse ; les pourcentages de réduction sont expérimentaux.
- Nature : guide technique.
- Valeurs clés relevées :
  - Guide (PDF ouvert) : mortalité 100 millions à 1 milliard d'oiseaux par an aux États-Unis (p. 7) ; Klem 1990 : 1 à 10 oiseaux par bâtiment et par an (p. 37) ; Dunn 1993 : 0,65 à 7,7 morts par maison et par an (p. 37).
  - Règle 2 x 4 : espaces horizontaux de 2 pouces (5 cm) ou moins et verticaux de 4 pouces (10 cm) ou moins (p. 17, 51) ; largeur de ligne d'au moins 1/4 de pouce (p. 51) ; motifs couvrant environ 5 % du vitrage dissuadant environ 90 % des collisions en conditions expérimentales (p. 17).
  - Zone de collision primaire : du sol à 40 pieds (environ 12 m) (p. 11) ; exigence de 90 % des matériaux exposés conformes dans cette zone et 60 % au-dessus pour dissuader 70 % ou plus des collisions (p. 10).
  - Klem 2009 : chaque hausse de 10 % de surface vitrée réfléchissante/transparente associée à + 19 % de collisions mortelles au printemps et + 32 % en automne (p. 12, 38).
  - Éclairage : extinction intérieure nocturne, orientation vers le bas, lumières bleues et vertes moins nocives que blanches ou rouges (p. 31, 40) ; ampoule « Clear Sky » : réduction de 50 à 90 % des oiseaux tournant autour d'une plateforme (p. 40).
  - Échelle des Threat Factors : 1 à 100 (page ABC ouverte) ; New York Local Law 15 de 2020 : Threat Factor de 25 ou moins pour la plupart des vitrages neufs à partir du 1er janvier 2021.
  - Model Guidelines mars 2025 (.docx ouvert) : matériau « bird-friendly » = Threat Factor de 30 ou moins ; Bird Activity Zone de 0 à 100 pieds ; rénovation majeure dès 25 % du vitrage remplacé ; grilles de protection extérieure à mailles de 12 pouces maximum.

## Fiche : USGBC, LEED Pilot Credit SSpc55 « Bird Collision Deterrence »
- Objet : crédit pilote LEED (ajouté 2011, révisé 2015, versé au catalogue Innovation en 2022, pilote fermé en août 2022) : calcul du Bird Collision Threat Rating (BCTR) de la façade, zones de façade, exigences d'éclairage extérieur et plan de suivi post-construction sur 3 ans.
- Référence complète : U.S. Green Building Council. LEED Pilot Credit SSpc55, Bird collision deterrence (Sustainable Sites). Repris comme Innovation Credit « Bird Collision Deterrence » dans LEED BD+C.
- URL : https://leeduser.buildinggreen.com/credit/Pilot-Credits/SSpc55 (page ouverte avec WebFetch) ; page ABC sur le crédit (ouverte) ; standard Cornell « 016010 Bird-Friendly Design for New Construction » (04/03/2024) https://fcs.cornell.edu/sites/default/files/2024-03/016010_Bird-Friendly%20Design%20For%20New%20Construction.pdf (ouverte), qui applique l'Innovation Credit.
- Contenu et valeurs disponibles : formules du BCTR, définitions des zones, seuils de Threat Factor, règle d'éclairage (extinction de minuit à 6 h, limites d'uplight par zone d'éclairage MLO), plan de suivi ; la page Cornell donne les seuils de la version Innovation Credit (zone 1 à 40 pieds, Threat Factor 30, règle 2 x 2 et 2 x 4).
- Licence et accessibilité : documentation USGBC (certaines parties sur abonnement LEEDuser) ; standard Cornell public.
- Limites pour une méthode à l'échelle de la parcelle : système prescriptif conçu pour la certification, dépend d'un tableau de Threat Factors propriétaire (ABC) non lu ; pas de validation épidémiologique du seuil 15 dans les pages consultées.
- Nature : guide technique / référentiel de certification.
- Valeurs clés relevées (page LEEDuser ouverte, sauf mention) :
  - Zone 1 : 36 premiers pieds (environ 11 m) au-dessus du sol, plus 12 pieds au-dessus de toute toiture végétalisée ; zone 2 : au-dessus de 36 pieds. (Cornell, version Innovation : zone 1 = 40 premiers pieds + 12 pieds au-dessus des toitures végétalisées ; zone 2 = 40 à 100 pieds.)
  - Exemption de calcul si tous les matériaux de façade ont un Threat Factor de 15 ou moins ; structures de site (garde-corps, abris, écrans) entièrement en matériaux de Threat Factor 15 ou moins.
  - Threat Factor maximal 25 pour les angles vitrés et configurations traversantes ; au plus 15 % de la zone 1 en matériaux de Threat Factor supérieur à 75 (« Hazardous Glazing Factor »).
  - Formules : Zone Factored Area = somme (Threat Factor x surface) ; Adjusted Building Façade Area = 2 x surface zone 1 + surface zone 2 ; BCTR total = (zone 1 pondérée + zone 2 pondérée) / surface ajustée ; conformité si BCTR total de 15 ou moins.
  - Éclairage extérieur non lié à la sécurité éteint automatiquement de minuit à 6 h ; limites d'uplight U0 à U4 selon la zone d'éclairage LZ0 à LZ4 (IES TM-15-11 addendum A).
  - Suivi post-construction sur 3 ans.
  - Cornell 2024 : Threat Factor de 30 ou moins ; au plus 5 % de la zone 1 au-dessus de 30 ; marquages espacés de 2 x 2 ou 2 x 4 pouces, ou lignes frittées de 1/8 de pouce espacées de 2 pouces ; points d'au moins 1/4 de pouce.

## Fiche : Rössler, Doppler, Furrer, Haupt, Schmid, Schneider, Steiof, Wegworth 2023, « Bird-friendly building with glass and light » (Station ornithologique suisse)
- Objet : brochure de référence (3e édition révisée) de la Station ornithologique suisse de Sempach sur la construction respectueuse des oiseaux : mécanismes (transparence, réflexion), facteurs de risque, règles de marquage (dimensions et écartements), classes d'efficacité des vitrages testés (Hohenau), lumière.
- Référence complète : Rössler M., Doppler W., Furrer R., Haupt H., Schmid H., Schneider A., Steiof K., Wegworth C. (2023). Bird-friendly building with glass and light. 3rd, revised edition. Swiss Ornithological Institute, Sempach. ISBN 978-3-85949-037-2. Édition allemande « Vogelfreundliches Bauen mit Glas und Licht » 2022 (fichier Glasbroschuere_2022_D.pdf sur vogelglas.vogelwarte.ch). Première édition : Schmid, Doppler, Heynen, Rössler 2012 (vu dans les résultats de recherche, non ouvert).
- URL : https://www.nabu.de/imperia/md/content/nabude/vogelschutz/231205-broschuere-englisch-bird-friendly-building.pdf (copie NABU de l'édition anglaise, page ouverte avec WebFetch) ; portail https://vogelglas.vogelwarte.ch/ (ouvert, liens de téléchargement) ; page vogelwarte.ch non ouverte (erreur).
- Contenu et valeurs disponibles : section 3.2.4 (p. 31) règles de marquage ; p. 31-32 couverture et contraste ; tableau 2 (p. 30) classes d'efficacité ; p. 6 mortalité en Allemagne ; p. 12-14 végétation et étages ; p. 9-10 réflexions. Le chapitre 5 (lumière, p. 50) était tronqué dans le texte lu.
- Licence et accessibilité : brochure gratuite ; copyright Station ornithologique suisse.
- Limites pour une méthode à l'échelle de la parcelle : règles de conception et tests en tunnel (Hohenau) ; les classes d'efficacité portent sur des produits ; la brochure ne donne pas de taux de mortalité par bâtiment pour la Suisse ; les règles « main » (règle de la main), « 2 x 4 » et « 25 % de couverture » demandées dans la commande ne figurent pas dans le texte lu (voir ci-dessous les valeurs réellement données).
- Nature : guide technique.
- Valeurs clés relevées (PDF ouvert avec WebFetch, pagination de l'édition anglaise) :
  - Bandes horizontales : largeur d'au moins 3 mm, écart bord à bord maximal 50 mm ; bandes verticales : au moins 5 mm, écart maximal 100 mm ; points : diamètre d'au moins 9 mm, écart maximal 90 mm (p. 31) ; exemple de grille de points 9-12 mm espacés de 90-100 mm (p. 33).
  - Couverture minimale : marquages dépolis semi-transparents au moins 11 % ; films semi-transparents au moins 20 % ; marquages métalliques efficaces sous 1 % grâce au contraste (p. 31-32). Pas de valeur de 25 % dans le texte lu.
  - Grilles denses de très petits points (3 mm à 14 mm) non reconnues comme obstacle.
  - Classes d'efficacité (tableau 2, p. 30, schéma de Hohenau) : A très efficace (0-10 % des oiseaux volent vers la vitre test), recommandé ; B (plus de 10 à 20 %) en général non recommandé ; C (plus de 20 à 42 %) et D (plus de 42 %) non recommandés ; seuil statistique de recommandation jusqu'à 12 %.
  - Mortalité : Allemagne environ 100 à 115 millions d'oiseaux par an, plus de 5 % des oiseaux présents (p. 6) ; États-Unis 365 à 988 millions.
  - Végétation : risque 3,6 fois plus élevé avec des arbres de plus de deux étages à proximité qu'en milieu sans arbres ; corrélation positive démontrée jusqu'à 100 m entre façades vitrées et arbres (p. 12) ; la plupart des collisions diurnes jusqu'à la hauteur de la cime (environ 6 étages) (p. 14).
  - Réflexion : vitrage peu réfléchissant seul non protecteur (p. 10) ; films solaires réfléchissant 25 à 60 % de la lumière ; 3 fois plus de vols vers un miroir argenté que vers un verre flotté non marqué (p. 10).
  - Règle de la main, règle 2 x 4, couverture 25 % : non vérifié (absentes du texte lu).

## Fiche : LPO France 2019, fiche « Chocs contre les vitres »
- Objet : fiche technique grand public de la LPO (rédaction Solène Bornier, mise à jour février 2019) sur les collisions et leur prévention.
- Référence complète : LPO France (2019). Atteintes à la petite faune : chocs contre les vitres (1/2). Fiche technique, dernière mise à jour février 2019.
- URL : https://wp.aveyron.lpo.fr/wp-content/uploads/2019/08/FicheChocsContreLesVitres2019_Web.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : statistiques des centres de sauvegarde LPO 2018, règles d'espacement des marquages, inefficacité des silhouettes de rapaces, renvoi au site vogelglas.vogelwarte.ch.
- Licence et accessibilité : document gratuit, copyright LPO.
- Limites pour une méthode à l'échelle de la parcelle : fiche de vulgarisation, pas de taux de mortalité ni de tests contrôlés ; les espacements recommandés (une paume, environ 15 cm) sont plus larges que ceux de la Station ornithologique suisse 2023 (50 mm horizontal, 100 mm vertical).
- Nature : guide technique (vulgarisation).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - 2018 : 479 oiseaux recueillis après collision avec une vitre ; 771 avec hématomes évoquant un choc indéterminé ; 328 appels et courriels sur ce sujet.
  - Autocollants espacés d'au plus une paume de main, soit environ 15 cm ; fils de nylon verticaux espacés de 5 à 8 cm ; marquage sur toute la surface, plus efficace à l'extérieur.
  - Une seule silhouette par vitre inefficace ; silhouettes de rapaces non reconnues comme prédateurs.
  - Lésions internes une fois sur deux chez les oiseaux apparemment indemnes.

---

## Thème F. Sol et substrat

## Fiche : Madre, Vergnes, Machon, Clergeau 2014, toitures végétalisées comme habitats pour la flore sauvage (115 toitures, nord de la France)
- Objet : échantillonnage à grande échelle de la flore spontanée de 115 toitures végétalisées du nord de la France ; effet de l'épaisseur de substrat, de l'âge, de la surface, de la hauteur et de l'entretien ; proposition d'une classification par strates.
- Référence complète : Madre F., Vergnes A., Machon N., Clergeau P. (2014). Green roofs as habitats for wild plant species in urban landscapes: first insights from a large-scale sampling. Landscape and Urban Planning 122 : 100-107. DOI 10.1016/j.landurbplan.2013.11.012.
- URL : notice https://esploro.umontpellier.fr/esploro/outputs/journalArticle/Green-roofs-as-habitats-for-wild/99163728709311 (page ouverte avec WebFetch, résumé) ; version HAL https://hal.sorbonne-universite.fr/hal-01489469v1/document (accès refusé par protection anti-robot).
- Contenu et valeurs disponibles (résumé) : 115 toitures, 176 espèces vasculaires colonisatrices dont 86 % indigènes ; l'épaisseur de substrat est le premier facteur de diversité ; composition aussi liée à l'âge, la surface, la hauteur et l'intensité d'entretien ; pas d'effet détectable du paysage environnant ; traits fonctionnels de milieux ouverts, secs et chauds. Les classes d'épaisseur en cm et les effets chiffrés ne figurent pas dans le résumé.
- Licence et accessibilité : article Elsevier payant ; dépôt HAL existant (non ouvert ici).
- Limites pour une méthode à l'échelle de la parcelle : flore seulement ; les valeurs de richesse par classe d'épaisseur n'ont pas été lues ; une région (nord de la France).
- Nature : source primaire.
- Valeurs clés relevées (résumé, page ouverte) : 115 toitures ; 176 espèces ; 86 % d'indigènes ; épaisseur de substrat premier facteur. Classes d'épaisseur et richesse associée : non vérifié.

## Fiche : ARB Île-de-France (Barra, Hemminki) 2021, programme GROOVES, Note rapide n° 890
- Objet : synthèse des résultats du programme GROOVES (36 toitures végétalisées de Paris et petite couronne, 2017-2019) : flore, invertébrés, sol, eau, évapotranspiration ; relations entre épaisseur de substrat et richesse ; recommandations de conception.
- Référence complète : Barra M., Hemminki J. (2021). Les toitures végétalisées : une évaluation des bénéfices écologiques en Île-de-France. Note rapide n° 890, Institut Paris Region / Agence régionale de la biodiversité en Île-de-France, mai 2021.
- URL : https://data.iau-idf.fr/fileadmin/DataStorage/user_upload/NR_890_web_1_.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : effectifs par catégorie de toiture, richesse floristique et entomologique, seuils d'épaisseur, texture optimale, rétention d'eau, évapotranspiration, biomasse microbienne, recommandations.
- Licence et accessibilité : publication gratuite de l'Institut Paris Region.
- Limites pour une méthode à l'échelle de la parcelle : 36 toitures d'une seule région, note de synthèse (les rapports détaillés ne sont pas lus ici) ; relations décrites qualitativement (« jusqu'à environ 25 cm ») plutôt que par équations.
- Nature : source primaire (programme régional) présentée en synthèse.
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - 36 toitures : 18 extensives (0-15 cm de substrat), 6 semi-intensives (15-30 cm), 8 intensives (plus de 30 cm), 4 « Wildroof » (non plantées).
  - Flore : environ 400 espèces au total ; 292 espèces vasculaires dans le suivi Vigie-Flore, environ 70 % spontanées ; invertébrés : 611 espèces.
  - Richesse végétale croissante avec l'épaisseur de substrat jusqu'à environ 25 cm ; diversité des pollinisateurs croissant encore au-delà de 25 cm.
  - Hauteur du bâtiment : effet positif sur la richesse végétale jusqu'à environ 10 m (3 étages), sans gain au-delà.
  - Texture optimale : environ 10 % d'argile et 60 % de sable.
  - Rétention d'eau (laboratoire) : 6 L/m² (3,5 cm) à 532 L/m² (100 cm) ; rétention annuelle modélisée environ 200-500 L/m²/an (26 toitures) ; abattement par événement 4 à 92 L/m² ; seules 5 toitures sur 26 régulent une pluie décennale de 48 mm en 4 h (sols agricoles d'environ 30 cm).
  - Évapotranspiration (14 toitures) : 7 à 190 W/m², 6 sur 14 au-dessus de 100 W/m².
  - Biomasse microbienne : 129,4 µg ADN/g sur toitures contre 59,2 dans la référence RMQS.
  - Toitures extensives environ 50 % moins performantes que semi-intensives et intensives sur les services évalués.
  - Recommandations : environ 30 cm de substrat ; au moins 10 % d'argile et environ 60 % de sable ; hétérogénéité des épaisseurs ; micro-habitats (bois mort, pierres, zones sableuses nues).

## Fiche : Brenneisen 2006, de l'espace pour la faune urbaine : toitures végétalisées en Suisse
- Objet : article de synthèse d'un chercheur suisse sur les toitures conçues comme habitats (Bâle, Zurich) : inventaires d'invertébrés, épaisseurs testées, réglementation bâloise (sols naturels régionaux, épaisseurs variées).
- Référence complète : Brenneisen S. (2006). Space for urban wildlife: designing green roofs as habitats in Switzerland. Urban Habitats 4 (1). Pagination non indiquée dans le texte lu.
- URL : https://www.eaglehill.us/urban-habitats/Vol%204/Urban Habitats -- Space for Urban Wildlife  Designing Green Roofs as Habitats in Switzerland.html (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : effectifs d'araignées et de coléoptères, espèces menacées, épaisseurs testées (6, 12, 20 cm), toitures de Wollishofen (15 cm de terre végétale sur 5 cm de gravier, 175 espèces végétales dont 9 orchidées), règle bâloise (toitures de plus de 500 m²), limites des substrats minces (vers de terre).
- Licence et accessibilité : revue en ligne en accès libre.
- Limites pour une méthode à l'échelle de la parcelle : article descriptif, nombre de toitures non indiqué ; pas de relation épaisseur-richesse chiffrée ; pas de seuil minimal d'épaisseur réglementaire dans le texte.
- Nature : source primaire / synthèse d'auteur.
- Valeurs clés relevées (page ouverte avec WebFetch) :
  - 12 500 araignées collectées ; toiture Rhypark : 79 espèces de coléoptères et 40 d'araignées, dont 13 et 7 sur listes rouges.
  - Épaisseurs testées à l'hôpital cantonal de Bâle : 6, 12 et 20 cm.
  - Bâle : sur les toitures de plus de 500 m², substrats en sols naturels de la région et d'épaisseur variable (pas de minimum chiffré dans le texte).
  - Wollishofen (Zurich, 1914) : 15 cm de terre sur 5 cm de gravier ; 175 espèces végétales dont 9 orchidées (3 menacées).
  - Vers de terre incapables de survivre sur substrats minces (chaleur estivale).
  - Mounds de 15-20 cm pour les oiseaux : non vérifié (absent du texte).

## Fiche : Williams, Lundholm, MacIvor 2014, les toitures végétalisées aident-elles la conservation de la biodiversité urbaine ?
- Objet : article de synthèse (« letter ») évaluant 6 hypothèses sur les bénéfices des toitures végétalisées pour la biodiversité.
- Référence complète : Williams N.S.G., Lundholm J., MacIvor J.S. (2014). Do green roofs help urban biodiversity conservation? Journal of Applied Ecology 51 (6) : 1643-1649. DOI 10.1111/1365-2664.12333.
- URL : notice AGRIS https://agris.fao.org/search/en/records/65dfd095b766d82b180334aa (page ouverte avec WebFetch, résumé) ; billet The Applied Ecologist https://appliedecologistsblog.com/2014/09/23/do-green-roofs-enhance-urban-conservation/ (ouvert) ; page Wiley non ouverte (erreur). Référence et résumé confirmés par Europe PMC.
- Contenu et valeurs disponibles : conclusion qualitative : les toitures soutiennent surtout des généralistes (insectes) ; valeur pour les taxons rares et les vertébrés mal documentée ; réplication des communautés du sol et connectivité largement non testées ; appel à la retenue dans les revendications et à ne pas traiter les toitures comme équivalentes aux habitats au sol. Aucune valeur numérique dans le résumé.
- Licence et accessibilité : article Wiley (OA : N selon Europe PMC).
- Limites pour une méthode à l'échelle de la parcelle : source conceptuelle utile pour plafonner la valeur attribuée aux toitures par rapport à la pleine terre, mais sans coefficient chiffré.
- Nature : revue de synthèse.
- Valeurs clés relevées : aucune valeur numérique (résumé, pages ouvertes) ; seuils d'épaisseur : non vérifié.

## Fiche : FLL 2018, Dachbegrünungsrichtlinien (directives allemandes pour la végétalisation des toitures)
- Objet : directives techniques de la Forschungsgesellschaft Landschaftsentwicklung Landschaftsbau (FLL) pour la planification, l'exécution et l'entretien des toitures végétalisées ; épaisseurs de substrat par forme de végétation.
- Référence complète : FLL (2018). Dachbegrünungsrichtlinien : Richtlinien für Planung, Bau und Instandhaltung von Dachbegrünungen. Bonn. (Référence vue dans la bibliographie des pages Baunetz Wissen ouvertes ; la directive elle-même n'a pas été ouverte, c'est un document payant.)
- URL : pages de vulgarisation Baunetz Wissen https://www.baunetzwissen.de/stadt--und-dachbegruenung/fachwissen/vegetation/pflanzen-extensive-dachbegruenungen-8277145 et .../pflanzen-intensive-dachbegruenungen-8277148 (pages ouvertes avec WebFetch).
- Contenu et valeurs disponibles (via Baunetz Wissen) : extensif : couche de substrat de 5 à 15 cm, liste de plantes pour 8 à 15 cm ; intensif : substrat à partir de 15 cm, liste de plantes pour 25 à 40 cm, arbres à partir de 80 cm. Le tableau FLL des épaisseurs par forme de végétation (Moos-Sedum, Sedum-Kraut-Gras, Gras-Kraut, etc.) n'a pas été lu.
- Licence et accessibilité : directive payante (FLL) ; pages Baunetz gratuites.
- Limites pour une méthode à l'échelle de la parcelle : valeurs lues dans une source secondaire ; la FLL vise la pérennité technique de la végétation, pas la biodiversité.
- Nature : guide technique (lu via source secondaire).
- Valeurs clés relevées (pages Baunetz ouvertes) : extensif 5-15 cm (plantes 8-15 cm) ; intensif à partir de 15 cm (plantes 25-40 cm ; arbres 80 cm et plus). Tableau FLL par forme de végétation : non vérifié.

## Fiche : Ville de Paris 2012, cahier technique des toitures végétalisées (15 fiches)
- Objet : cahier technique municipal : classification des toitures (extensive, semi-intensive, intensive) avec épaisseurs et charges, recommandations de conception (épaisseur minimale, hétérogénéité, nombre d'espèces).
- Référence complète : Ville de Paris (2012). Toitures végétalisées : cahier technique, 15 fiches pratiques. Rédaction DEVE, DPA, DU, DPE, DLH. Septembre 2012, 30 p.
- URL : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2022-01/cahier-technique-des-toitures-vegetalisees-15-fiches-pratiques-ville-de-paris1.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : fiches 1 à 3 (p. 7-9), recommandations p. 5 et p. 30.
- Licence et accessibilité : document public gratuit.
- Limites pour une méthode à l'échelle de la parcelle : document de 2012 sans référence scientifique nommée ; valeurs de conception, pas de relation épaisseur-biodiversité mesurée.
- Nature : guide technique.
- Valeurs clés relevées (PDF ouvert avec WebFetch) : extensive : végétation basse, substrat 10 cm (minimum 8 cm), 100-150 kg/m² (p. 7) ; semi-intensive : herbacée, 10-30 cm, 150-350 kg/m² (p. 8) ; intensive : arbustive, 30-80 cm, plus de 350 kg/m² (p. 9) ; épaisseur minimale recommandée 10 cm, ou 8 cm si la structure l'impose ; bénéfices pour la biodiversité croissant avec l'épaisseur (p. 5) ; une dizaine d'espèces de genres différents (p. 5, 11) ; varier les épaisseurs et les strates (p. 30). La fiche pratique de la Région Bretagne (ouverte, non datée) donne d'autres bornes : extensive moins de 8 cm (environ 100 kg/m²), semi-intensive moins de 30 cm (150-350 kg/m²), intensive plus de 30 cm (plus de 600 kg/m²).

## Fiche : Cerema / ADEME 2022, projet MUSE : fonctions des sols et multifonctionnalité (rapport et fiches)
- Objet : méthode MUSE (projet ADEME 2017-2021, Cerema avec INRAE, IRSTV, BRGM, Chambre d'agriculture de l'Indre, Aix-Marseille Université) pour cartographier la multifonctionnalité des sols à l'échelle des PLUi : 4 fonctions notées de 1 à 5 (source de biomasse, régulation du cycle de l'eau, réservoir de carbone, réservoir de biodiversité), approche rurale sur Référentiels régionaux pédologiques au 1/250 000 et approche urbaine par proxy d'occupation du sol (pleine terre, imperméabilisation, couvert arboré).
- Référence complète : Branchu P., Marseille F. et al. (2022). MUSE : intégrer la multifonctionnalité des sols dans les documents d'urbanisme. Rapport et annexes. ADEME, collection Expertises, mars 2022, 184 p. (librairie ADEME, fiche 5415). Fiches fonctions Cerema (mai 2022, biomasse avril 2023) et Note Pleine Terre (Vigneron F., 2022, environ 18 p.). Suite : projet CartoMUSE (2023-2025), fiches techniques rurales décembre 2025 (CeremaDoc 606996).
- URL : https://www.cerema.fr/fr/actualites/prendre-compte-multifonctionnalite-sols-amenagement (page ouverte avec WebFetch, liste des livrables) ; https://www.cerema.fr/fr/actualites/determiner-fonctions-que-remplissent-sols (ouverte) ; https://www.cerema.fr/fr/actualites/fiches-synthetiques-presentation-fonctions-sols-retenues (ouverte) ; fiche biodiversité https://www.cerema.fr/fr/system/files?file=documents/2022/05/3.4_fiche_fonction_reservoir_biodiversite.pdf (ouverte) ; fiche eau https://www.cerema.fr/fr/system/files?file=documents/2022/05/3.2_fiche_fonction_regulation_eau.pdf (ouverte) ; Note Pleine Terre https://www.cerema.fr/fr/system/files?file=documents/2022/05/3.5_note_pleine_terre.pdf (ouverte) ; fiche milieu urbain https://www.cerema.fr/fr/system/files?file=documents/2022/05/2.6_fiche_multifonctionnalite_urbain_0.pdf (ouverte) ; rapport ADEME https://librairie.ademe.fr/urbanisme-et-batiment/5415-muse-... (notice ouverte, PDF derrière formulaire, non lu).
- Contenu et valeurs disponibles : règles de notation complètes des indicateurs infiltration et biodiversité ; approche urbaine à 3 classes ; définition de la pleine terre et épaisseurs associées ; analyse de 15 PLU.
- Licence et accessibilité : documents gratuits (ADEME, Cerema) ; licence non précisée sur la notice ADEME.
- Limites pour une méthode à l'échelle de la parcelle : méthode conçue pour le 1/250 000 (rural) et pour l'occupation du sol à 10 m (urbain) ; les auteurs déclarent la validité limitée à l'échelle source et l'absence de données de profondeur en milieu urbain ; les indicateurs reposent sur des moyennes nationales (vers de terre) ; la transposition à la parcelle suppose des mesures de terrain (profondeur, texture, tassement) que MUSE ne prévoit pas.
- Nature : guide technique / méthode (recherche appliquée).
- Valeurs clés relevées (fiches ouvertes avec WebFetch) :
  - Indicateur biodiversité (fiche 3.4) : vers de terre, données ONB/EcoBioSoil, 731 sites (abondance) et 629 (richesse), 2006-2015 ; moyennes par occupation : espaces verts urbains 280 ind/m² et 6 taxons ; cultures 223 et 5 ; vignes et vergers 163 et 3 ; prairies 421 et 9 ; forêts et milieux semi-naturels 149 et 6 ; classes d'abondance : moins de 25 = 1 ; 25-150 = 2 ; 150-300 = 3 ; 300-600 = 4 ; plus de 600 = 5 ; classes de richesse : moins de 1 = 1 ; 1-2 = 2 ; 3-4 = 3 ; 5-7 = 4 ; 8 et plus = 5 ; somme reclassée 2 = 1, 3-4 = 2, 5-6 = 3, 7-8 = 4, plus de 8 = 5.
  - Indicateur infiltration (fiche 3.2) : 4 critères notés 0 à 3 : plancher imperméable (moins de 25 cm = 0 ; 25-50 = 1 ; 50-100 = 2 ; plus de 100 cm ou absent = 3) ; texture (argileuse 0, limoneuse 1, équilibrée 2, sableuse 3) ; perméabilité Ks (moins de 0,86 cm/j = 0 ; 0,86-8,6 = 1 ; 8,6-86 = 2 ; plus de 86 cm/j = 3) ; hydromorphie (aucune = 3 ; 25-80 cm = 1 ; 0-25 cm ou histosol = 0) ; un 0 est éliminatoire (classe 1) ; somme : moins de 4 = classe 2, 4 à 7 = 3, plus de 7 à 10 = 4, plus de 10 = 5 ; pente supérieure à 10 % éliminatoire ; à échelle fine, pente 0-2 % = 3, 2-5 % = 2, 5-10 % = 1, plus de 10 % = 0.
  - Approche urbaine (fiche 2.6 et page Cerema) : profondeur du sol comme proxy de multifonctionnalité potentielle ; couvert arboré dominant = capacité optimale ; imperméabilisé (bâti, routes) = capacité nulle ; autres = intermédiaire ; données Copernicus (imperméabilisation et densité de couvert arboré, 10 m) ; notation 0 (scellé), 1 (perméable végétalisé non arboré), 2 (arboré) dans la Note Pleine Terre.
  - Note Pleine Terre : pleine terre = sol urbain capable d'exercer tout ou partie des fonctions d'un sol naturel ; optimum associé à une épaisseur d'environ 1 à 1,2 m ; sols sur dalle exclus (continuité sol / sous-sol requise) ; épaisseurs retenues selon la végétation : herbacée 0 à 0,4 m, arbustive 0 à 0,8 m, arborée 0 à 1,2 m ; biodiversité et carbone concentrés dans les 25 premiers cm ; décapage de la couche de surface : baisse de 88 à 94 % du stock de carbone (Geissen et al. 2013) ; 15 PLU analysés, profondeurs de référence variables (10 m à Nantes et Cadaujac, 3 m à Nogent-sur-Marne et Grand Chambéry) ; aires de stationnement et dalles généralement exclues.
  - Indice de multifonctionnalité = somme non pondérée des 4 notes, classé de « très faible » à « très forte » (page Cerema).

## Fiche : Séré et al. 2024, DESTISOL, outil d'aide à la décision sur les services écosystémiques des sols urbains
- Objet : modèle DESTISOL (Université de Lorraine / LSE, Cerema, SCE ; programme ADEME 2013-2017) : 20 indicateurs physico-chimico-biologiques transformés en scores de 15 fonctions du sol, puis en compatibilité avec 13 types de couverture, puis en 18 services écosystémiques ; appliqué à 37 sols urbains.
- Référence complète : Séré G., Lothode M., Blanchart A., Chirol C., Tribotte A., Schwartz C. (2024). Destisol: a decision-support tool to assess the ecosystem services provided by urban soils for better urban planning. European Journal of Soil Science 75 (5) : e13557. DOI 10.1111/ejss.13557.
- URL : notice HAL https://hal.inrae.fr/hal-04804531v1 (accès refusé par protection anti-robot) ; page Wiley non ouverte (erreur). Référence et résumé vérifiés par métadonnées Crossref. Compléments lus dans le recueil ADEME 5e RNR SSP atelier 5A https://recherche.ademe.fr/sites/default/files/2025-05/5eRNR_SSP_Recueil_Atelier5A.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : résumé (architecture du modèle, effectifs) ; recueil ADEME : scores de fonctions de 0 à 3, 13 couvertures, 4 catégories de confiance des données, résultats d'un cas (circulation de l'eau supérieure à 2 ; fertilité 0,68 à 2 ; stockage de carbone surtout sous 2 ; rétention des polluants sous 1,29). Aucun seuil d'épaisseur de sol ou de pleine terre dans les textes lus.
- Licence et accessibilité : article Wiley (licence éditeur selon Crossref) ; dépôt HAL existant.
- Limites pour une méthode à l'échelle de la parcelle : c'est la seule source de ce thème conçue à l'échelle opérationnelle du projet, mais ses règles de décision (indicateurs vers fonctions) ne sont pas lues ici et supposent des analyses de sol de terrain et de laboratoire ; pas de sortie « biodiversité » directe au-delà des fonctions.
- Nature : source primaire (outil de recherche appliquée).
- Valeurs clés relevées : 20 indicateurs, 15 fonctions, 13 couvertures, 18 services, 37 sols testés (résumé Crossref) ; notation 0 à 3 par fonction (recueil ADEME, p. 4) ; seuils d'épaisseur : non vérifié.

## Fiche : Agence de l'eau Seine-Normandie / DRIEAT 2024, guide ERC imperméabilisation (disposition 3.2.2 du SDAGE)
- Objet : guide d'application d'une disposition du SDAGE Seine-Normandie sur l'imperméabilisation nouvelle planifiée dans les documents d'urbanisme ; définitions (imperméabilisation, pleine terre), coefficients d'équivalence par type de surface, ratios de compensation.
- Référence complète : Agence de l'eau Seine-Normandie, DRIEAT Île-de-France (2024). « Éviter, réduire et compenser » : l'imperméabilisation nouvelle des sols planifiée dans les documents d'urbanisme. Guide d'application de la disposition 3.2.2 du SDAGE Seine-Normandie, janvier 2024, 42 p. (avec conseils du Cerema et de l'Institut Paris Region).
- URL : https://www.drieat.ile-de-france.developpement-durable.gouv.fr/IMG/pdf/guide-erc-impermeabilisation-des-sols.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : définitions, seuil de profondeur pour la pleine terre, coefficients d'équivalence, ratios de compensation, pondérations.
- Licence et accessibilité : document public gratuit.
- Limites pour une méthode à l'échelle de la parcelle : logique hydraulique (infiltration), pas écologique ; coefficients fixés par convention de bassin (Seine-Normandie) ; aucun coefficient pour les dalles ; pas de taux d'infiltration.
- Nature : guide technique (réglementaire de bassin).
- Valeurs clés relevées (PDF ouvert avec WebFetch) :
  - Pleine terre : espace libre sans construction en surélévation ni en sous-sol permettant une infiltration totale ; profondeur supérieure à 1 m (hors végétation en pot) ; « perméable végétalisé » : profondeur inférieure à 1 m.
  - Coefficients d'équivalence : pleine terre (parc, jardin de pluie, noue) 1 ; perméable déconnecté et végétalisé (toiture végétalisée) 0,5 ; perméable déconnecté non végétalisé (enrobé poreux) 0,1 ; dispositifs déconnectés végétalisés gérant la pluie cinquantennale 0,7 à 0,8 ; réfections de trottoirs ou toitures 0.
  - Compensation : 150 % de la surface impactée en commune urbaine, 100 % en commune rurale.
  - Pondérations : P_ZR 0,8 (zéro rejet pluie trentennale), 1 (neutralité hydraulique), 1,1 (absence de règle) ; c_perm conseillé 0,9.

## Fiche : ISO 19204:2017, évaluation écologique des risques spécifique au site (approche TRIAD)
- Objet : norme décrivant l'application de l'approche TRIAD (chimie, écotoxicologie, écologie) à l'évaluation écologique des risques des sols contaminés ; pas une norme de fonctionnalité des sols non pollués.
- Référence complète : ISO 19204:2017. Qualité du sol : procédure pour l'évaluation écologique des risques spécifique au site de la contamination des sols (approche TRIAD de la qualité du sol). ISO/TC 190/SC 4, 27 p. Publiée le 24 février 2017, confirmée en 2022, révision ISO/DIS 19204 en cours.
- URL : https://www.iso.org/standard/63989.html (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : domaine d'application seulement ; aucune classe de fonctionnalité ni seuil.
- Licence et accessibilité : norme payante (159 CHF).
- Limites pour une méthode à l'échelle de la parcelle : hors sujet pour la fonctionnalité des sols sains ; pertinente seulement si la méthode traite des sites pollués. ISO 18504 (remédiation durable) : non vérifié (recherche non effectuée, quota atteint).
- Nature : norme (guide technique).
- Valeurs clés relevées : aucune valeur de fonctionnalité ; 3 lignes de preuve (page ouverte).

---

## Thème G. Eau

## Fiche : OFB 2023, Méthode nationale d'évaluation des fonctions des zones humides, version 2
- Objet : méthode nationale (collectif Patrinat, Biotope, Cerema, OFB, INRAE, Tour du Valat, université de Tours) pour évaluer les fonctions hydrologiques, biogéochimiques et d'accomplissement du cycle biologique des espèces sur un site impacté et un site de compensation, indicateur par indicateur ; interface de dimensionnement (ratio fonctionnel) intégrant le risque d'échec et le délai des gains.
- Référence complète : Collectif (2023). Le guide de la méthode nationale d'évaluation des fonctions des zones humides, version 2. OFB, collection Guides et protocoles, septembre 2023, 154 p. ISBN web 978-2-38170-116-5 ; imprimé 978-2-38170-117-2 ; DOC00084433. Version 1 : Gayet G. et al. (2016), OFB/MNHN (vue dans les résultats de recherche : « 2016_Guide_ZH_OFB.pdf », non ouverte). Note d'information DEB du 16 novembre 2023 (dossier suivi par G. Gayet et P. Caessteker).
- URL : https://ofb.gouv.fr/doc/le-guide-de-la-methode-nationale-evaluation-des-fonctions-des-zones-humides-version-2 (page ouverte avec WebFetch) ; note d'information https://www.zones-humides.org/sites/default/files/pdf/Note%20d'information%20MNEFZH%20V2.pdf (ouverte).
- Contenu et valeurs disponibles : structure de la méthode, nouveautés de la v2 (zones humides littorales et marais, nouvelles fonctions : soutien d'étiage et atténuation des pics de crue aval ; interface de dimensionnement ; tableur xlsx ; extension QGIS Cerema) ; testée sur environ 400 sites. Les valeurs des indicateurs ne sont pas dans les pages lues.
- Licence et accessibilité : gratuit ; licence etalab-2.0 par défaut sur ofb.gouv.fr (non confirmée pour le guide) ; PDF du guide sur oai-gem.ofb.fr (domaine refusant les robots dans cette session).
- Limites pour une méthode à l'échelle de la parcelle : méthode conçue pour la compensation réglementaire des zones humides (comparaison impact / compensation), pas pour noter une parcelle isolée ; nécessite des relevés de terrain et des données environnementales (zone contributive, zone tampon, paysage).
- Nature : guide technique / méthode nationale.
- Valeurs clés relevées (pages ouvertes) : 154 p. ; 3 familles de fonctions ; 3 diagnostics (contexte, dimensionnement, fonctionnel) ; environ 400 sites de test ; pas d'augmentation de la collecte de données par rapport à la v1 ; valeurs d'indicateurs et ratios : non vérifié.

## Fiche : Williams, Whitfield, Biggs 2008, comment rendre les nouvelles mares riches en biodiversité ? Pinkhill Meadow, 7 ans
- Objet : suivi sur 7 ans d'un complexe d'environ 40 mares créées sur 3,2 ha en bordure de Tamise (Pinkhill Meadow) ; colonisation par la flore, les macroinvertébrés et les oiseaux ; comparaison avec d'autres mares nouvelles et des mares de référence.
- Référence complète : Williams P., Whitfield M., Biggs J. (2008). How can we make new ponds biodiverse? A case study monitored over 7 years. Hydrobiologia 597 (1) : 137-148. DOI 10.1007/s10750-007-9224-9.
- URL : https://link.springer.com/article/10.1007/s10750-007-9224-9 (page ouverte avec WebFetch, résumé). Référence confirmée par Crossref.
- Contenu et valeurs disponibles (résumé) : proportion du pool national colonisant le site, espèces rares, oiseaux, comparaison avec les références ; les comptes d'espèces et le rythme annuel de colonisation sont dans le texte intégral, non lu.
- Licence et accessibilité : article Springer payant.
- Limites pour une méthode à l'échelle de la parcelle : un site, contexte très favorable (eau propre, paysage riche en zones humides) ; résultats de type « potentiel maximal », pas valeur attendue moyenne.
- Nature : source primaire.
- Valeurs clés relevées (résumé, page ouverte) : environ 40 mares et mares temporaires sur 3,2 ha ; environ 20 % de toutes les espèces britanniques de plantes de zones humides et de macroinvertébrés ont colonisé le site pendant le suivi ; 8 invertébrés « Nationally Scarce » ; 3 espèces de limicoles nicheuses et 54 autres espèces d'oiseaux de zones humides ; conductivité significativement plus basse que les autres mares ; les 4 mares suivies en détail plus riches que les mares de référence peu altérées. Délai de colonisation par année : non vérifié.

## Fiche : Williams, Biggs, Crowe, Murphy, Nicolet, Weatherby, Dunbar 2010, Countryside Survey : Ponds Report from 2007
- Objet : rapport technique national (Grande-Bretagne) sur l'état des mares en 2007 ; comparaison des mares nouvelles (0-9 ans) et anciennes.
- Référence complète : Williams P., Biggs J., Crowe A., Murphy J., Nicolet P., Weatherby A., Dunbar M. (2010). Countryside Survey: Ponds Report from 2007. Technical Report No. 7/07, Pond Conservation et Centre for Ecology & Hydrology, janvier 2010.
- URL : https://nora.nerc.ac.uk/id/eprint/9622/1/N009622CR.pdf (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : richesse végétale des mares nouvelles contre anciennes, part de mares de bonne qualité, nutriments, effectifs.
- Licence et accessibilité : rapport public en accès libre (NORA).
- Limites pour une méthode à l'échelle de la parcelle : 16 mares nouvelles seulement ; contexte britannique ; pas de courbe temporelle.
- Nature : source primaire (rapport technique).
- Valeurs clés relevées (PDF ouvert avec WebFetch) : mares de 0-9 ans : 10,2 espèces de plantes de zones humides en moyenne contre 7,9 pour les mares plus anciennes ; 24 % des mares nouvelles de « bonne qualité » (Priority Ponds) contre environ 6 % des anciennes ; 259 mares étudiées en 2007 dont 16 créées depuis 1998 ; 18 % des mares nouvelles au-dessus du seuil de phosphore (0,12 mg/l PO4-P) contre 26 % de l'ensemble ; environ 70 600 mares créées entre 1998 et 2007 contre environ 18 000 perdues.

## Fiche : Williams, Biggs, Stoate, Szczur, Brown, Bonney 2020, mesures fondées sur la nature et biodiversité d'eau douce dans les bassins agricoles
- Objet : suivi annuel sur 9 ans de la richesse en macrophytes de ruisseaux, mares et fossés dans 3 bassins agricoles anglais ; effet de mares d'eau propre créées pour la biodiversité et de dispositifs multifonctionnels.
- Référence complète : Williams P., Biggs J., Stoate C., Szczur J., Brown C.D., Bonney S. (2020). Nature based measures increase freshwater biodiversity in agricultural catchments. Biological Conservation 244 : 108515 (volume non affiché sur la notice ; numéro d'article 108515 confirmé par la notice). DOI de la version bioRxiv 10.1101/672915 indiqué sur la notice.
- URL : https://eprints.whiterose.ac.uk/id/eprint/158373/ (notice White Rose, page ouverte avec WebFetch ; manuscrit accepté CC BY-NC-ND).
- Contenu et valeurs disponibles : variation de richesse à l'échelle du bassin, espèces rares, tendance de fond, comparaison des mesures ; évaluation 5 ans après la création.
- Licence et accessibilité : manuscrit accepté en libre accès (CC BY-NC-ND 2.5) ; article Elsevier payant.
- Limites pour une méthode à l'échelle de la parcelle : échelle du bassin versant et contexte agricole ; le nombre de mares créées n'est pas sur la notice.
- Nature : source primaire.
- Valeurs clés relevées (notice ouverte) : mares d'eau propre : + 26 % de richesse totale du bassin et + 181 % du nombre d'espèces rares, 5 ans après création ; sans mesure : perte d'environ 1 % des espèces par an et 2 % des espèces rares par an ; dispositifs « services écosystémiques » compensant la perte générale sans restaurer les espèces rares ; embâcles sans effet détectable.

## Fiche : Cerema 2023, « L'eau de pluie, une amie qui refait surface » (collection Les essentiels) et guides associés
- Objet : plaquette de synthèse du Cerema sur la gestion intégrée des eaux pluviales et la désimperméabilisation ; renvoie aux guides Cerema de la période 2018-2023.
- Référence complète : Cerema (2023). L'eau de pluie, une amie qui refait surface. Collection Les essentiels, mai 2023 (contributeur Cyril Pajot). Guides cités : Zonage pluvial : de son élaboration à sa mise en oeuvre (Cerema, 2020) ; Zonage pluvial : pour une gestion intégrée de l'eau (Cerema, 2021) ; série de fiches « Gestion intégrée de l'eau en milieu urbain » (Cerema, 2020-2023) ; Sobriété foncière (Les essentiels, 2022).
- URL : https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2023-07/ville-permeable%5B1%5D.pdf (page ouverte avec WebFetch) ; catalogue GRAIE « Eau dans la ville » https://www.graie.org/graie/graiedoc/doc_telech/GRAIE_OutilsSupportsPedagogiques_EauxPluvialesAmenagement.pdf (ouvert) ; pages Cerema https://www.cerema.fr/fr/print/pdf/node/15253 et /node/2960 (ouvertes : page projet « ville perméable » Nice Côte d'Azur 2024-2025 et offre de service, sans valeur).
- Contenu et valeurs disponibles : ordres de grandeur de ruissellement et d'artificialisation ; aucune valeur de perméabilité, de dimensionnement ni de biodiversité dans les pages lues.
- Licence et accessibilité : documents publics gratuits.
- Limites pour une méthode à l'échelle de la parcelle : les guides Cerema techniques (zonage pluvial 2020-2021, fiches 2020-2023) n'ont pas pu être ouverts avant la fin du quota de recherche ; aucune relation « gestion intégrée des eaux pluviales vers biodiversité » chiffrée n'a été trouvée dans les sources ouvertes.
- Nature : guide technique (plaquette de synthèse).
- Valeurs clés relevées (plaquette ouverte) : ruissellement d'environ 55 % de la pluie en zone urbaine dense contre environ 10 % en zone naturelle (ministère, 2017) ; surfaces imperméabilisées croissant environ 3 fois plus vite que la population depuis 1980 (CGDD 2017) ; objectif de la métropole de Lyon : 400 ha désimperméabilisés ou déconnectés d'ici 2026. Taux d'infiltration, seuils de perméabilité, dimensions de noues : non vérifié.

---

## Thème H. Délais de maturation et risque d'échec des habitats créés

## Fiche : Natural England 2023, Biodiversity Metric 4.0, Technical Annex 2 (Technical Information)
- Objet : annexe technique de la métrique de biodiversité anglaise (base de la Statutory Biodiversity Metric de 2024) : justification et valeurs des « time to target condition » (années) par habitat et par condition visée, multiplicateurs d'actualisation temporelle, catégories de difficulté de création et de restauration et multiplicateurs de risque associés.
- Référence complète : Natural England (2023). The Biodiversity Metric 4.0, User Guide, Technical Annex 2 : Technical Information. Natural England Joint Publication JP039, mars 2023. ISBN 978-1-7393362-3-3. Licence Open Government Licence v3.0.
- URL : https://publications.naturalengland.org.uk/file/5749350878412800 (PDF téléchargé et lu intégralement, 79 pages). La page d'accueil des documents de la métrique statutaire (https://publications.naturalengland.org.uk/publication/6049804846366720, ouverte) indique qu'une annexe technique spécifique à la métrique statutaire « sera publiée prochainement » ; le User Guide statutaire (Defra, février 2024, mis à jour juin 2026, https://assets.publishing.service.gov.uk/media/689c5ee17b2e384441636196/The_Statutory_Biodiversity_Metric_-_User_Guide_-_July_2025.pdf, ouvert) ne reproduit pas les tables de temps mais renvoie à l'onglet « G-4 Temporal multipliers » de l'outil et donne les multiplicateurs spatiaux.
- Contenu et valeurs disponibles : section 5 (p. 51-55) : méthode des temps vers la condition cible (estimations « largement fondées sur l'avis d'experts », complétées par l'expérience de terrain), taux d'actualisation, Technical Table 5-1 (multiplicateurs par année), exemples (tables 5-2 et 5-3) ; section 6 (p. 56 et suivantes) : 4 catégories de difficulté (Low, Medium, High, Very High) ; Data Table 1 (p. 69) : distinctivité et multiplicateurs de difficulté par habitat ; Data Table 3 « Habitat creation matrix » (p. 73) : années vers chaque condition cible par habitat créé ; Data Table 3 (sic) « Habitat enhancement matrix » (p. 75) ; Data Table 5 (p. 76) : haies.
- Licence et accessibilité : accès libre, Open Government Licence v3.0 (sauf classification UKHab sous licence propre).
- Limites pour une méthode à l'échelle de la parcelle : valeurs expertes calibrées pour l'Angleterre et pour la classification UKHab ; « saut » de qualité supposé à l'échéance (pas de trajectoire continue) ; les temps ne distinguent pas la taille de la parcelle ni la distance aux sources de colonisation (facteurs cités en 5.2.1 mais non paramétrés) ; transposition française à justifier habitat par habitat.
- Nature : guide technique (référentiel réglementaire).
- Valeurs clés relevées (PDF lu intégralement ; pages du PDF) :
  - Taux d'actualisation 3,5 % par an (Treasury Green Book), 5.3.2, p. 52.
  - Technical Table 5-1 (p. 52-53), multiplicateurs par temps vers la condition cible : 0 an 1,000 ; 1 an 0,965 ; 2 ans 0,931 ; 3 ans 0,899 ; 4 ans 0,867 ; 5 ans 0,837 ; 6 ans 0,808 ; 7 ans 0,779 ; 8 ans 0,752 ; 9 ans 0,726 ; 10 ans 0,700 ; 11 ans 0,676 ; 12 ans 0,652 ; 13 ans 0,629 ; 14 ans 0,607 ; 15 ans 0,586 ; 16 ans 0,566 ; 17 ans 0,546 ; 18 ans 0,527 ; 19 ans 0,508 ; 20 ans 0,490 ; 21 ans 0,473 ; 22 ans 0,457 ; 23 ans 0,441 ; 24 ans 0,425 ; 25 ans 0,410 ; 26 ans 0,396 ; 27 ans 0,382 ; 28 ans 0,369 ; 29 ans 0,356 ; 30 ans 0,343 ; 30 ans et plus 0,320.
  - Multiplicateurs de difficulté (Data Table 1, p. 69) : Low 1 ; Medium 0,67 ; High 0,33 ; Very High 0,1. Exemples : modified grassland Low/Low (1/1) ; other neutral grassland Low/Low ; lowland meadows création High 0,33, restauration Medium 0,67 ; lowland calcareous grassland High/High (0,33/0,33) ; lowland mixed deciduous woodland High/High ; ponds (priority habitat) Medium/Medium (0,67/0,67) ; ponds (non-priority) Low/Medium ; reedbeds Medium/Medium ; biodiverse green roof Medium/Medium ; intensive green roof Low/Low ; mixed scrub Low/Low ; introduced shrub Low/Low ; vegetated garden Low/Low ; urban tree Low/Low ; open mosaic habitats on previously developed land Medium/Medium ; aquifer-fed naturally fluctuating water bodies Very High 0,1 (création).
  - Data Table 3, Habitat creation matrix (p. 73-74), années pour atteindre la condition Good / Fairly Good / Moderate / Fairly Poor / Poor : modified grassland 7 / 5 / 4 / 2 / 1 ; other neutral grassland 10 / 7 / 5 / 3 / 2 ; lowland meadows 15 / 12 / 10 / 8 / 5 ; lowland calcareous grassland 20 / 15 / 10 / 8 / 5 ; lowland dry acid grassland 30+ / 25 / 20 / 15 / 10 ; upland calcareous grassland 25 / 20 / 15 / 12 / 10 ; traditional orchards 30 / 25 / 20 / 10 / 5 ; mixed scrub 10 / 7 / 5 / 3 / 1 ; hawthorn et blackthorn scrub 10 / 7 / 5 / 3 / 1 ; hazel scrub 15 / 12 / 10 / 7 / 5 ; bramble scrub 1 an (condition N/A) ; ponds (priority et non-priority) 5 / 4 / 3 / 2 / 1 ; temporary ponds 5 / 4 / 3 / 2 / 1 ; reedbeds 12 / 10 / 7 / 5 / 3 ; purple moor grass and rush pastures 30 / 25 / 20 / 15 / 10 ; lowland raised bog 30+ / 30+ / 30 / 20 / 15 ; lowland mixed deciduous woodland 30+ / 30+ / 30+ / 25 / 10 ; other woodland broadleaved 30+ / 25 / 15 / 7 / 5 ; other woodland mixed 30+ / 30+ / 30 / 10 / 5 ; other coniferous woodland 30+ / 30+ / 30 / 10 / 5 ; wet woodland 30+ / 30 / 15 / 10 / 5 ; wood-pasture and parkland 30+ / 30+ / 30+ / 25 / 10 ; urban tree et rural tree 30+ / 30+ / 27 / 19 / 10 ; intensive green roof 5 / 4 / 3 / 2 / 1 ; biodiverse green roof 10 / 8 / 5 / 3 / 1 ; other green roof 1 an (N/A) ; introduced shrub 1 an (N/A) ; vegetated garden 1 an (N/A) ; allotments 1 ; open mosaic habitats on previously developed land 10 / 7 / 4 / 2 / 0 ; developed land sealed surface et artificial unvegetated unsealed surface 0.
  - Data Table 5, haies (p. 76), années de création vers Poor / Moderate / Good : native hedgerow, species-rich native hedgerow et variantes avec talus ou fossé 1 / 5 / 12 ; haies avec arbres (native hedgerow with trees, species-rich with trees) 1 / 10 / 20 ; lines of trees et ecologically valuable lines of trees 5 / 20 / 30+ ; distinctivité des haies : Very High 8 (species-rich native hedgerow with trees associated with bank or ditch), High 6, Medium 4, Low 2 (native hedgerow, line of trees), Very Low 1 (non-native and ornamental hedgerow).
  - Exemples de la table 5-2 (p. 54) : lowland meadow Good 15 ans ; modified grassland Good 7 ans ; lowland heathland Good 30+ ; artificial littoral coarse sediment Moderate 1 an. Table 5-3 (p. 55) : other broadleaved woodland Moderate 15 ans, Good 30+ ; upland calcareous grassland Good 25 ans.
  - Multiplicateurs spatiaux (User Guide statutaire, table 9, p. 39) : dans le site 1,0 ; voisinage 0,75 ; hors zone 0,5.
  - La version 3.1 (JP039, avril 2022, https://publications.naturalengland.org.uk/file/6059060118683648, ouverte) et la 3.0 (https://images.reading.gov.uk/2021/10/Appendix-6-Biodiversity-Metric-3.0-Technical-Supplement.pdf, ouverte) ont la même structure (temps vers la condition cible p. 68 et p. 61 respectivement) mais leurs tables n'ont pas été lues. La version 2.0 (JP029, 2019, https://publications.naturalengland.org.uk/file/4923683225468928, PDF téléchargé) donne par exemple pour reedbeds : distinctivité High, difficultés Medium/Medium, années 15 / 12 / 10 / 7 / 5.

## Fiche : Fagan, Pywell, Bullock, Marrs 2008, les prairies calcaires restaurées sur anciennes cultures ressemblent-elles aux cibles anciennes ?
- Objet : comparaison multi-sites de 40 prairies calcaires restaurées sur anciennes terres arables avec 40 prairies anciennes de référence appariées ; similarité des communautés, durée du processus, filtres environnementaux (phosphore).
- Référence complète : Fagan K.C., Pywell R.F., Bullock J.M., Marrs R.H. (2008). Do restored calcareous grasslands on former arable fields resemble ancient targets? The effect of time, methods and environment on outcomes. Journal of Applied Ecology 45 (4) : 1293-1303. DOI 10.1111/j.1365-2664.2008.01492.x.
- URL : notice NORA https://nora.nerc.ac.uk/id/eprint/5474/ (page ouverte avec WebFetch, résumé, texte intégral non disponible). Résumé confirmé par Europe PMC.
- Contenu et valeurs disponibles (résumé) : peu de recouvrement entre communautés restaurées et anciennes même après 60 ans ; restauration possible mais lente ; semis à faible diversité délétère ; régénération naturelle efficace seulement à proximité de prairies anciennes ; phosphore élevé défavorable.
- Licence et accessibilité : article Wiley payant ; pas de texte intégral sur NORA.
- Limites pour une méthode à l'échelle de la parcelle : prairies calcaires britanniques ; âge maximal 60 ans ; nombre d'espèces cibles manquantes non lu.
- Nature : source primaire (multi-sites).
- Valeurs clés relevées (résumé) : 40 sites restaurés, 40 références ; pas de convergence après 60 ans ; filtres : phosphore du sol, distance aux prairies anciennes, qualité du semis.

## Fiche : Moreno-Mateos, Power, Comín, Yockteng 2012, pertes structurelles et fonctionnelles des zones humides restaurées
- Objet : méta-analyse de 621 zones humides restaurées ou créées (401 restaurées, 220 créées) comparées à 556 références (124 études, 1 501 points) ; récupération de la structure biologique et des fonctions biogéochimiques selon l'âge, la taille, le climat et l'hydrologie.
- Référence complète : Moreno-Mateos D., Power M.E., Comín F.A., Yockteng R. (2012). Structural and functional loss in restored wetland ecosystems. PLoS Biology 10 (1) : e1001247. DOI 10.1371/journal.pbio.1001247.
- URL : https://journals.plos.org/plosbiology/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001247 (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : déficits moyens à 50-100 ans, délais de récupération par groupe (végétaux, invertébrés, vertébrés), carbone et azote, effets de la taille (plus de 100 ha), du climat (tempéré, froid, tropical) et de l'hydrologie (fluviale, tidale, dépressionnaire, tourbières).
- Licence et accessibilité : accès libre, licence CC BY.
- Limites pour une méthode à l'échelle de la parcelle : les zones humides de petite taille (moins de 0,1 ha à quelques ha, cas des mares de projet) récupèrent plus lentement, mais les valeurs par classe de taille sont dans la figure 3, non lues ; chronoséquences souvent de moins de 30 ans ; incohérence interne relevée entre résumé (structure -26 %, fonction -23 %) et résultats (structure environ 77 %, fonction 74 % de la référence).
- Nature : méta-analyse.
- Valeurs clés relevées (page ouverte avec WebFetch) :
  - 621 sites restaurés ou créés, 556 références, 124 études, 1 501 points.
  - Après 50 à 100 ans : structure biologique environ 77 % et fonctionnement biogéochimique environ 74 % de la référence (résultats) ; résumé : structure 26 % plus basse et fonction 23 % plus basse même environ un siècle après.
  - Végétation : environ 30 ans en moyenne pour devenir statistiquement similaire à la référence, valeurs absolues encore inférieures après 100 ans ; vertébrés environ 5 ans ; macroinvertébrés 5 à 10 ans.
  - Stockage de carbone environ 50 % plus bas après 20 ans (6 études, 21 zones humides) ; matière organique du sol environ 62 % de la référence à 20-30 ans ; azote significativement plus bas pendant environ 30 ans ; phosphore peu affecté.
  - Taille : zones humides de plus de 100 ha récupérant plus vite (13 études, 25 sites).
  - Climat : tempéré, fonction à environ 79 % à 30 ans (83 études, 302 sites) ; froid, environ 53 % à 50 ans (33 études, 311 sites).
  - Hydrologie : fluviales et tidales récupérées après environ 20 et 30 ans (73 études, 210 sites) ; dépressionnaires non récupérées après 50 ans (36 études, 358 sites) ; tourbières : structure immédiate, fonction encore inférieure à 30 ans.

## Fiche : Rey Benayas, Newton, Diaz, Bullock 2009, amélioration de la biodiversité et des services par la restauration écologique
- Objet : méta-analyse de 89 évaluations de restauration dans des écosystèmes variés ; gains de biodiversité et de services par rapport à l'état dégradé et déficit par rapport aux références intactes.
- Référence complète : Rey Benayas J.M., Newton A.C., Diaz A., Bullock J.M. (2009). Enhancement of biodiversity and ecosystem services by ecological restoration: a meta-analysis. Science 325 (5944) : 1121-1124. DOI 10.1126/science.1172460.
- URL : notice NORA https://nora.nerc.ac.uk/id/eprint/8122/ (page ouverte avec WebFetch, résumé, pas de texte intégral). Référence confirmée par Crossref.
- Contenu et valeurs disponibles (résumé et notice) : 89 évaluations ; biodiversité + 44 % et services + 25 % après restauration par rapport à l'état dégradé ; valeurs restant inférieures aux références intactes ; corrélation positive entre gains de biodiversité et de services ; priorité aux biomes tropicaux terrestres. L'ampleur du déficit par rapport aux références n'est pas sur la notice.
- Licence et accessibilité : article Science payant.
- Limites pour une méthode à l'échelle de la parcelle : échelle mondiale et multi-biomes ; pas de délai.
- Nature : méta-analyse.
- Valeurs clés relevées (notice ouverte) : 89 évaluations ; + 44 % de biodiversité ; + 25 % de services ; déficit par rapport aux références : non chiffré (non vérifié).

## Fiche : Jones et al. 2018, restauration et réparation des écosystèmes dégradés de la Terre
- Objet : méta-analyse de 400 études de récupération après perturbations à grande échelle (marées noires, agriculture, exploitation forestière) ; complétude et vitesse de récupération ; comparaison restauration active / récupération passive.
- Référence complète : Jones H.P., Jones P.C., Barbier E.B., Blackburn R.C., Rey Benayas J.M., Holl K.D., McCrackin M., Meli P., Montoya D., Moreno-Mateos D. (2018). Restoration and repair of Earth's damaged ecosystems. Proceedings of the Royal Society B 285 (1873) : 20172577. DOI 10.1098/rspb.2017.2577.
- URL : page éditeur non ouverte (erreur) ; notices HAL et UAH refusées (protection anti-robot) ; résumé vérifié par métadonnées Crossref ; communiqué ScienceDaily https://www.sciencedaily.com/releases/2018/03/180301094834.htm (page ouverte avec WebFetch).
- Contenu et valeurs disponibles : résumé Crossref : 400 études ; récupération en cours mais rarement complète ; ralentissement des taux avec le temps ; restauration active pas plus rapide ni plus complète que l'arrêt des perturbations. ScienceDaily : taux de récupération de 1 à 10 % par an pour la plupart des sites ; moins de 5 % des études comparant actif et passif sur un même site.
- Licence et accessibilité : Royal Society ; statut d'accès non vérifié (dépôts HAL et UAH existent).
- Limites pour une méthode à l'échelle de la parcelle : perturbations à grande échelle, pas des créations d'habitat urbain ; pas de valeur de complétude en pourcentage dans les sources lues.
- Nature : méta-analyse.
- Valeurs clés relevées : 400 études (résumé Crossref) ; 1 à 10 % de récupération par an, ralentissant avec le temps (ScienceDaily, page ouverte) ; pourcentage de récupération finale : non vérifié.

## Fiche : Staley et al. 2015 et Staley et al. 2018 (Defra BD2114), gestion et restauration des haies
- Objet : expérimentation multi-sites de 5 méthodes de rajeunissement des haies (3 ans de suivi) et rapport final du projet Defra BD2114 sur les effets de la gestion et de la restauration des haies sur la biodiversité (cycles de taille, haies expérimentales de Monks Wood plantées en 1961).
- Référence complète : Staley J.T., Amy S.R., Adams N.P., Chapman R.E., Peyton J.M., Pywell R.F. (2015). Re-structuring hedges: rejuvenation management can improve the long term quality of hedgerow habitats for wildlife in the UK. Biological Conservation 186 : 187-196. DOI 10.1016/j.biocon.2015.03.002. Et : Staley J.T., Adams N.P. et al. (2018). Effects of hedgerow management and restoration on biodiversity. Rapport final Defra BD2114, NERC Centre for Ecology and Hydrology.
- URL : résumé 2015 sur Hedgelink https://hedgelink.org.uk/research/re-structuring-hedges-... (page ouverte avec WebFetch) ; rapport 2018 https://nora.nerc.ac.uk/id/eprint/532938/1/N532938CR.pdf (page ouverte avec WebFetch, texte tronqué après la section 4.6). Volume et pages 2015 confirmés par Crossref.
- Contenu et valeurs disponibles : cycles de gestion, réponses des fleurs et baies aux cycles de taille, effets du rajeunissement sur 3 à 4 ans ; aucune valeur de « temps de maturité » d'une haie plantée.
- Licence et accessibilité : article Elsevier payant ; rapport Defra en accès libre (NORA).
- Limites pour une méthode à l'échelle de la parcelle : les sources documentent la gestion de haies existantes, pas le délai d'une haie nouvellement plantée pour atteindre une valeur écologique donnée ; pour ce délai, seule la table haies de la métrique anglaise (fiche Natural England) fournit des années (1 / 5 / 12 ans ; 1 / 10 / 20 ans avec arbres).
- Nature : source primaire (2015) et rapport technique (2018).
- Valeurs clés relevées (rapport 2018 ouvert) : taille d'entretien tous les 1 à 3 ans, rajeunissement (plessage ou recépage) tous les 20 ans et plus (section 1.1.1) ; fleurs d'aubépine cumulées sur 8 ans 1,9 fois plus nombreuses et masse de baies 3,5 fois plus élevée sur parcelles taillées tous les 3 ans que tous les ans (sections 3.1-3.2) ; haie de 1 m atteignant environ 1,6 m après 6 ans de coupes annuelles incrémentales, 1,3 m en cycle de 2 ans, 1,2 m en cycle de 3 ans (section 2.2.1) ; effets du recépage encore visibles 3 à 4 ans après ; richesse des lépidoptères plus élevée en cycle de 3 ans. Délai de maturité d'une haie plantée : non vérifié.

## Fiche : Broughton et al. 2021 et 2022, réensauvagement passif et développement de boisements sur terres agricoles (Monks Wood Wildernesses ; site éloigné des sources de graines)
- Objet : deux études de cas anglaises à long terme sur la colonisation ligneuse de champs abandonnés : (1) deux parcelles adjacentes à une forêt ancienne, suivies 24 et 59 ans ; (2) 25 ha de terres remaniées éloignées des sources de graines, 33 ans.
- Référence complète : Broughton R.K., Bullock J.M., George C., Hill R.A., Hinsley S.A., Maziarz M., Melin M., Mountford J.O., Sparks T.H., Pywell R.F. (2021). Long-term woodland restoration on lowland farmland through passive rewilding. PLoS ONE 16 (6) : e0252466. DOI 10.1371/journal.pone.0252466. Et : Broughton R.K., Bullock J.M., George C., Gerard F., Maziarz M., Payne W.E., Scholefield P.A., Wade D., Pywell R.F. (2022). Slow development of woodland vegetation and bird communities during 33 years of passive rewilding in open farmland. PLoS ONE 17 (11) : e0277545. DOI 10.1371/journal.pone.0277545.
- URL : pages PMC (PMC8208563, PMC9651571) non ouvertes (contrôle anti-robot) ; résumés et licences vérifiés par métadonnées Europe PMC.
- Contenu et valeurs disponibles (résumés) : couvert ligneux, hauteur, densité d'arbres par âge ; dépendance à la distance des sources de graines.
- Licence et accessibilité : accès libre, CC BY (Europe PMC).
- Limites pour une méthode à l'échelle de la parcelle : 3 sites, Angleterre ; mais échelle (2 à 25 ha) et logique (colonisation spontanée) directement comparables à une parcelle de projet.
- Nature : sources primaires.
- Valeurs clés relevées (résumés Europe PMC) :
  - New Wilderness (2,1 ha, abandonnée en 1996, adjacente à une forêt ancienne) : 86 % de couvert ligneux de 2,9 m de haut en moyenne 23 ans après ; 132 arbres vivants/ha (57 % chênes) à 24 ans.
  - Old Wilderness (3,9 ha, abandonnée en 1961) : 100 % de couvert ligneux de 13,1 m en moyenne à 53 ans, canopée de 8 m et plus sur 91 % ; 390 arbres/ha (52 % chênes) à 59 ans ; structure en hauteur approchant celle des forêts anciennes voisines en environ 50 ans ; composition différente (chêne et arbustes à baies, dispersés par les animaux).
  - Site éloigné des sources de graines (25 ha, sols remaniés) : prairie ouverte dominante pendant deux décennies ; après 33 ans, fourrés épineux sur 53 % du site, arbres rares, forêt fermée « perspective lointaine ».

## Fiche : Harmer, Peterken, Kerr, Poulton 2001, 100 ans de développement de deux boisements secondaires sur terres arables abandonnées (Rothamsted)
- Objet : étude des Broadbalk et Geescroft Wildernesses (Rothamsted, abandonnées dans les années 1880) sur un siècle de colonisation.
- Référence complète : Harmer R., Peterken G., Kerr G., Poulton P.R. (2001). Vegetation changes during 100 years of development of two secondary woodlands on abandoned arable land. Biological Conservation 101 (3) : 291-304. DOI 10.1016/S0006-3207(01)00072-6.
- URL : notice du dépôt Rothamsted https://repository.rothamsted.ac.uk/item/88982/... (page ouverte avec WebFetch, sans résumé, texte sous embargo) ; page Forest Research « New native woodlands » https://www.forestresearch.gov.uk/?p=101937 (ouverte, citation et description qualitative). Référence confirmée par Crossref.
- Contenu et valeurs disponibles : aucune valeur chiffrée lue ; description qualitative (Broadbalk dominé par l'aubépine avec quelques chênes, frênes et érables, flore au sol pauvre et riche en lierre ; Geescroft : chêne et frêne en canopée, houx en sous-étage, flore au sol clairsemée).
- Licence et accessibilité : article Elsevier payant, embargo indéfini sur le dépôt.
- Limites pour une méthode à l'échelle de la parcelle : valeurs non lues.
- Nature : source primaire.
- Valeurs clés relevées : délai de fermeture de la canopée, nombre d'espèces, indicatrices de forêt ancienne : non vérifié.

---

## Thème I. Courbe de récupération de la végétation secondaire dans GLOBIO

## Fiche : Schipper, Bakkenes, Meijer, Alkemade, Huijbregts 2016, GLOBIO 3.5 technical model description (PBL)
- Objet : description technique du modèle GLOBIO 3.5 (PBL, Pays-Bas) : valeurs de MSA par classe d'usage du sol, courbe de récupération de la MSA de la végétation secondaire selon les années depuis l'abandon (figure 2.1), zones d'impact des infrastructures, relation MSA / taille de tache (fragmentation), encroachment, azote, climat.
- Référence complète : Schipper A., Bakkenes M., Meijer J., Alkemade R., Huijbregts M. (2016). GLOBIO 3.5 technical model description. PBL Netherlands Environmental Assessment Agency, publication 2369, 1er mars 2016, 36 p.
- URL : notice https://www.pbl.nl/en/publications/globio-35-technical-model-description (page ouverte avec WebFetch) ; PDF https://www.pbl.nl/downloads/pbl-publication-2369pdf (téléchargé et lu intégralement ; page 11 rastérisée et vérifiée visuellement pour la figure 2.1).
- Contenu et valeurs disponibles : table 2.2 (MSA par usage du sol), figure 2.1 (courbe de récupération), section 5.3 (MSA infrastructure), table 6.1 (fragmentation).
- Licence et accessibilité : rapport public du PBL en accès libre.
- Limites pour une méthode à l'échelle de la parcelle : modèle à la maille de 0,5 degré ; la courbe de récupération est une moyenne mondiale par grand type de biome (forestier / non forestier) issue d'études de végétation secondaire après coupe rase ou abandon agricole, sans intervalle de confiance ni équation dans le texte ; la MSA « urbain 0,05 » est un avis d'expert pour des villes denses sans espaces verts ; la MSA infrastructure de 0,78 est une moyenne sur une zone de 1 km, incompatible avec une résolution parcellaire sans réutiliser les courbes distance-MSA de Benítez-López et al. 2010.
- Nature : guide technique (documentation de modèle).
- Valeurs clés relevées (PDF lu intégralement, pages du PDF) :
  - Courbe de récupération (figure 2.1, p. 11), lecture graphique : biomes forestiers : MSA d'environ 0,35 à 0 an, croissant à peu près linéairement jusqu'à environ 0,8 à 60 ans ; biomes non forestiers : environ 0,7 à 0 an, croissant jusqu'à environ 0,95 à 60 ans. Courbe établie « à partir des valeurs de MSA de la végétation secondaire dérivées d'études à nombre variable d'années depuis la coupe rase et/ou l'abandon » ; pas d'équation ni d'intervalle dans le document (valeurs lues sur le graphique, précision d'environ ± 0,05).
  - Table 2.2 (p. 11), MSA_LU : forêt naturelle 1,0 ; plantation forestière 0,30 ; coupe rase 0,50 (note a : moyenne de la végétation secondaire sur un nombre variable d'années) ; coupe sélective 0,70 ; exploitation à impact réduit 0,85 ; prairie naturelle 1,0 ; pâturage modéré à intensif 0,60 ; pâturage artificiel 0,30 ; culture extensive 0,30 ; culture intensive 0,10 ; culture irriguée 0,05 ; biocarburants ligneux 0,30 ; sol nu, neige et glace 1,0 ; zone urbaine 0,05 (note b : villes denses sans espaces verts significatifs, avis d'expert). Sources indiquées : Alkemade et al. 2009, Alkemade et al. 2013, base de référence GLOBIO.
  - Infrastructure (section 5.3, p. 16) : zone d'impact de 1 km ; MSA moyenne de 0,66 pour oiseaux et mammifères (Benítez-López et al. 2010) ; MSA_I = 4/6 x 0,66 + 2/6 x 1 = 0,78 pour l'ensemble des groupes ; 0,90 en aire protégée.
  - Fragmentation (table 6.1, p. 18), MSA_F selon la surface de la tache d'habitat naturel : 0-1 km² 0,35 ; 1-10 km² 0,45 ; 10-100 km² 0,65 ; 100-1 000 km² 0,90 ; 1 000-10 000 km² 0,98 ; plus de 10 000 km² 1,00 ; dérivée des besoins minimaux en surface de 36 espèces d'oiseaux et 80 de mammifères (Verboom et al. 2014).

## Fiche : Alkemade et al. 2009, GLOBIO3 : cadre pour explorer les options de réduction de la perte de biodiversité terrestre
- Objet : article fondateur de GLOBIO3 : MSA par usage du sol (89 jeux de données), zones d'impact des infrastructures, fragmentation, azote, climat.
- Référence complète : Alkemade R., van Oorschot M., Miles L., Nellemann C., Bakkenes M., ten Brink B. (2009). GLOBIO3: a framework to investigate options for reducing global terrestrial biodiversity loss. Ecosystems 12 (3) : 374-390. DOI 10.1007/s10021-009-9229-5.
- URL : https://link.springer.com/article/10.1007/s10021-009-9229-5 (page ouverte avec WebFetch ; article en accès libre, mais les tables 4, 6 et 7 sont des liens séparés refusés par robots.txt et le PDF est protégé par un contrôle anti-robot).
- Contenu et valeurs disponibles : texte principal : 89 jeux de données d'usage du sol ; forte variabilité des forêts secondaires ; urbain 0,05 par avis d'expert ; taches de plus de 10 000 km² suffisantes pour toute espèce. Les valeurs de la table 4 (MSA avec erreurs-types et n) n'ont pas été lues.
- Licence et accessibilité : accès libre (Springer, « Open access »), licence précise non indiquée sur la page.
- Limites pour une méthode à l'échelle de la parcelle : mêmes limites que GLOBIO 3.5 ; pas de courbe de récupération par âge dans l'article de 2009 (seulement une MSA moyenne pour la forêt secondaire).
- Nature : source primaire (documentation de modèle).
- Valeurs clés relevées (page ouverte) : 89 jeux de données ; urbain 0,05 (avis d'expert) ; seuil de 10 000 km² ; table 4 : non vérifié dans l'article (voir table 2.2 de GLOBIO 3.5 et diapositive PBL 2013 ci-dessous).

## Fiche : Schipper et al. 2020, projection de l'intégrité de la biodiversité terrestre avec GLOBIO 4 ; et PBL / ThinkLandscape 2023, documentation technique GLOBIOweb
- Objet : GLOBIO 4 remplace les classes d'usage du sol de GLOBIO 3 par des relations issues de la base PREDICTS (plantes et vertébrés séparément) ; la végétation secondaire reçoit une MSA fixe par groupe ; les routes sont modélisées par une relation MSA / distance (oiseaux et mammifères) ; la fragmentation par la taille des taches avec absence d'impact au-delà de 10 000 ha.
- Référence complète : Schipper A.M., Hilbers J.P., Meijer J.R., Antão L.H., Benítez-López A., de Jonge M.M.J., Leemans L.H., Scheper E., Alkemade R., Doelman J.C., Mylius S., Stehfest E., van Vuuren D.P., van Zeist W.-J., Huijbregts M.A.J. (2020). Projecting terrestrial biodiversity intactness with GLOBIO 4. Global Change Biology 26 (2) : 760-771. DOI 10.1111/gcb.14848. PMCID PMC7028079. Et : Meijer J. (2023). Technical documentation of the GLOBIOweb datasets. ThinkLandscape pour PBL, février 2023.
- URL : https://pmc.ncbi.nlm.nih.gov/articles/PMC7028079 (page ouverte avec WebFetch) ; https://www.globio.info/wp-content/uploads/2023/03/GlobioWeb_technical_documentation_20230219.pdf (page ouverte avec WebFetch) ; diapositives PBL 2013 (van der Esch) https://unstats.un.org/unsd/envaccounting/seeaRev/meeting2013/EG13-2-GLOBIO3.pdf (ouvertes).
- Contenu et valeurs disponibles : licence et structure de GLOBIO 4 (article) ; table 3.1 de la documentation GLOBIOweb avec MSA par classe pour oiseaux et mammifères et pour plantes ; valeurs GLOBIO3 par usage du sol (diapositives 2013).
- Licence et accessibilité : article en accès libre CC BY 4.0 ; documentation PBL publique.
- Limites pour une méthode à l'échelle de la parcelle : GLOBIO 4 n'a plus de courbe de récupération par âge : la végétation secondaire a une valeur unique ; les valeurs urbaines (0,264 et 0,361) sont des moyennes PREDICTS toutes intensités confondues ; mailles mondiales.
- Nature : source primaire (article) et guide technique (documentation).
- Valeurs clés relevées :
  - GLOBIOweb 2023, table 3.1 (page ouverte), MSA oiseaux et mammifères / plantes : urbain 0,264 / 0,361 ; cultures 0,452 / 0,156 (intensif 0,401 / 0,149 ; minimal 0,502 / 0,162) ; mosaïque cultures dominantes 0,671 / 0,493 ; mosaïque végétation naturelle dominante 0,781 / 0,662 ; pâturage 0,452 / 0,156 ; sylviculture 0,589 / 0,259 ; végétation secondaire 0,621 / 0,568 ; classes naturelles 1,0 ; distance maximale du module routes 150 km (annexe 2) ; pas de dépendance à l'âge pour la végétation secondaire.
  - Schipper et al. 2020 (page PMC ouverte) : la végétation secondaire a une MSA plus élevée que les usages agricoles, d'où une restauration partielle lors de l'abandon ; routes de types 1 à 3 (GRIP) seulement ; impact routier appliqué aux vertébrés homéothermes seulement ; fragmentation sans impact au-delà de 10 000 ha ; valeurs numériques par classe seulement dans la figure 2 (non lues).
  - GLOBIO3 (diapositives PBL 2013, ouvertes) : forêts primaires 1,0 ; forêts primaires peu utilisées 0,7 ; forêts secondaires 0,5 ; plantations 0,2 ; agroforesterie 0,5 ; pâturage extensif 0,7 ; pâturages artificiels 0,1 ; agriculture extensive 0,3 ; intensive 0,1 ; bâti 0,05.
  - Kok et al. 2022 : cité comme source des valeurs agricoles de GLOBIOweb ; non ouvert, non vérifié.

Conclusion du thème I : la courbe de récupération de la végétation secondaire existe et a été vérifiée dans la documentation GLOBIO 3.5 (figure 2.1, p. 11) : elle est linéaire par morceaux, de 0,35 à environ 0,8 en 60 ans pour les biomes forestiers et de 0,7 à environ 0,95 pour les autres biomes, sans équation publiée dans ce document. Elle n'apparaît ni dans Alkemade et al. 2009 (MSA moyenne 0,5 pour la forêt secondaire) ni dans GLOBIO 4 (valeur fixe 0,621 / 0,568). Elle ne doit pas être confondue avec le multiplicateur d'actualisation de la métrique anglaise (3,5 % par an), qui est une convention économique et non une courbe écologique.
