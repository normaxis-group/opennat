# Bibliographie de la méthode OpenNAT v1

Sources dont une valeur entre dans `donnees/` ou dont une règle fonde une équation. Les documents ont été lus le 18 octobre 2026 ; leurs copies de travail sont conservées hors dépôt (`sources/`). Les sources de l'audit du lot 0 qui ne fournissent aucune valeur à la v1 restent décrites dans `audit/audit.md` et `audit/fiches/`.

## Textes réglementaires et documents officiels

| Référence | Ce qui en est tiré | Lien | Licence |
|---|---|---|---|
| Verordnung über die Vermeidung und die Kompensation von Eingriffen in Natur und Landschaft im Zuständigkeitsbereich der Bundesverwaltung (BKompV), 14 juin 2020, BGBl. I 2020, 1088, annexe 2 (Biotopwertliste) | 668 valeurs de biotopes de 0 à 24, extraites dans `sources/biotopwert_de/bkompv_anlage2.csv` | https://www.gesetze-im-internet.de/bkompv/anlage_2.html | texte réglementaire, § 5 UrhG |
| Defra et Natural England, The Statutory Biodiversity Metric, calculation tool 1.0.4 (version sans macro) | distinctivités (G-1), difficultés et multiplicateurs (G-3), délais de maturité (G-4), haies (G-6), surfaces des arbres (G-3) | https://assets.publishing.service.gov.uk/media/6867e62810d550c668de3b4e/The_Statutory_Metric_Macro_Disabled_1.0.4.xlsx | Open Government Licence v3.0 |
| Defra et Natural England, Statutory Biodiversity Metric Condition Assessments, juillet 2025 | grilles d'état 4A à 24A | https://assets.publishing.service.gov.uk/media/689c5f19d2a1b0d5d1bb1254/Statutory_Biodiversity_Metric_Condition_Assessments_-_July_2025.xlsx | Open Government Licence v3.0 |
| Environment Act 2021, Schedule 14 (Schedule 7A du Town and Country Planning Act 1990), paragraphes 2(3) et 9(3) | gain net de 10 %, durée de 30 ans | https://www.legislation.gov.uk/ukpga/2021/30/schedule/14 | Open Government Licence v3.0 |
| Arrêté du 4 août 2021 relatif aux exigences de performance énergétique et environnementale des constructions de bâtiments, annexe II | période d'étude de référence de 50 ans, liste et ordre des indicateurs de l'ACV | https://rt-re-batiment.developpement-durable.gouv.fr/IMG/pdf/annexeii_arrete_4_aout_2021.pdf | Licence Ouverte 2.0 |
| Arrêté du 27 décembre 2018 relatif à la prévention, à la réduction et à la limitation des nuisances lumineuses, modifié | définition de l'éclairage conforme (classe L1) | https://aida.ineris.fr/reglementation/arrete-271218-relatif-a-prevention-a-reduction-a-limitation-nuisances-lumineuses | Licence Ouverte 2.0 |
| Senatsverwaltung Berlin, Biotopflächenfaktor, BFF-Berechnung | coefficients de sol, bonus d'infiltration, eau de pluie | https://www.berlin.de/sen/uvk/natur-und-gruen/landschaftsplanung/bff-biotopflaechenfaktor/bff-berechnung/ | texte administratif public |
| Greater London Authority, London Plan Guidance, Urban Greening Factor, février 2023, table 3.1 | coefficients de sol, eau | https://www.london.gov.uk/sites/default/files/2023-02/London%20Plan%20Guidance%20-%20Urban%20Greening%20Factor.pdf | Open Government Licence v3.0 |
| Eurométropole de Strasbourg, PLU, règlement écrit, dispositions applicables à toutes les zones, modification n° 4 (mai 2024), article 9 | coefficients de sol | https://sig.strasbourg.eu/datastrasbourg/plu_media/reglement_actuel.pdf | document d'urbanisme public |
| Grand Annecy, PLUi-HMB, fiche d'aide à l'instruction des coefficients de biotope et de pleine terre | coefficients de sol | https://plui-hmb-approuve-ga.grandannecy.fr/04_REGLEMENT/FICHE_AIDE_instruction_CBS.pdf | document d'urbanisme public |
| Ville de Paris, guide des règles environnementales du PLU bioclimatique, juillet 2025, règle UG.4 (p. 63) | coefficients de l'indice de végétalisation du bâti | https://cdn.paris.fr/paris/2025/07/17/250715_guideenvironnemental-tfz6.pdf | document d'urbanisme public |
| Métropole européenne de Lille, PLU, tableau du coefficient de biotope par surface (extrait du Pacte Lille Bas Carbone, 18/10/2022) | coefficients de sol | https://www.nature-en-ville.com/sites/nature-en-ville/files/document/2025-06/Lille_CBS_calcul_tableau.pdf | document d'urbanisme public |
| NORMATYS, référentiel Effinature 8.1, critère SOL 01.2.5 | seuils du coefficient de biotope et de la pleine terre | non public | propriété de NORMATYS |

## Modèles et données scientifiques

| Référence | Ce qui en est tiré | Lien | Licence |
|---|---|---|---|
| PBL Netherlands Environmental Assessment Agency, 2016, GLOBIO 3.5 Technical model description, publication 2369 | MSA par usage des sols (table 2.2), perte de MSA par °C (table 3.1) et facteur de retard (§ 3.3), fragmentation (table 6.1) | https://www.pbl.nl/downloads/pbl-publication-2369pdf | reproduction autorisée avec mention de la source |
| GIEC, 2021, Climate Change 2021, The Physical Science Basis, résumé à l'intention des décideurs, D.1.1 | réponse transitoire du climat aux émissions cumulées (0,45 °C par 1 000 GtCO2) | https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf | citation de valeur |
| GIEC, 2019, Climate Change and Land, résumé à l'intention des décideurs, figure SPM.1 | surface terrestre libre de glace (130 Mkm²), parts des cultures et des infrastructures | https://www.ipcc.ch/site/assets/uploads/sites/4/2022/11/SRCCL_SPM.pdf | citation de valeur |
| IGN, Mémento de l'inventaire forestier, édition 2024, p. 38 et 39 | production biologique des forêts françaises (5,4 m³/ha/an) | https://www.ign.fr/publications-de-l-ign/institut/kiosque/publications/docs_thematiques/memento-2024.pdf | publication publique |
| Beninde J., Veith M., Hochkirch A., 2015, Biodiversity in cities needs space, Ecology Letters 18, 581-592 | seuil de 4,4 ha pour les espèces adaptées à la ville | https://www.uni-trier.de/fileadmin/fb6/prof/BIO/Hochkirch/Beninde_et_al-2015-Ecology_Letters.pdf | article, citation |
| PatriNat, HabRef v7 (07/08/2025) | libellés français et présence en France des habitats EUNIS 2012 de niveau 3 | https://assets.patrinat.fr/files/referentiel/HABREF.zip | licence non lue (serveurs de l'INPN hors service) |

## Sources secondaires à remplacer par la source primaire

Valeurs lues au lot 0 dans l'audit et non relues au lot 1 ; chacune est marquée « secondaire » dans les tables.

| Référence | Valeur | Raison |
|---|---|---|
| Matthews T. J. et al., 2016, On the form of species-area relationships in habitat islands and true islands, Global Ecology and Biogeography 25 | exposant z = 0,22 (îles d'habitat) | dépôt de l'université de Birmingham refusé (erreur 403) le 18/10/2026 |
| Azam C. et al., 2018, et Rowse E. G. et al., 2018 (via EUROBATS) | distances d'évitement des chiroptères | articles non téléchargés |
| Reijnen R. et al., 1997, Disturbance by traffic of breeding birds | seuils de bruit, baisse de densité | article non téléchargé |
| Dossiers d'enquête publique de quatre carrières (Pouzilhac, Valliguières, Montreuil-au-Houlme, Saint-Colomban) | occupation par tonne | lus dans des extraits de recherche |
| FCBA, Mémento 2025-2026 | borne haute du rapport bois rond / produit | lu dans un extrait de recherche |

## Sources écartées pour leur licence

Global Biodiversity Score (CC BY-NC), grille CBSh du CSTB (usage commercial interdit), webservice INIES (interdiction de tout classement ou notation des déclarations). Voir l'audit, § 5, point P14.
