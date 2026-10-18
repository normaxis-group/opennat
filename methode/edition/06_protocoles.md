## Partie 6. Protocoles de relevé des grilles d'état

Les grilles d'état (`etat_criteres.csv`) disent quoi observer ; cette partie dit comment le relever pour que deux écologues aboutissent au même score. Les protocoles transposent les règles et les notes de bas de page des fiches d'évaluation de la métrique statutaire anglaise (juillet 2025, Open Government Licence v3.0), adaptées au contexte français. Ils valent pour l'état initial (critères constatés) comme pour l'état projet (critères visés).

### 6.1 Règles communes

#### Unité de relevé

Le relevé se fait par unité d'habitat : une surface homogène d'un seul type, d'une seule position et d'un seul état. Quand une partie d'une unité diffère nettement (une moitié de prairie surpâturée, l'autre non), l'unité se scinde en deux unités, chacune avec sa grille.

#### Période

Le relevé de la végétation se fait pendant la période où les espèces caractéristiques sont identifiables : en plaine, d'avril à juillet pour les prairies et les pelouses, de mai à septembre pour les zones humides et les mégaphorbiaies, toute l'année pour les critères de structure (hauteur, couvert, bois mort). Un relevé hors période est signalé au RSNat et ses critères floristiques sont répondus « non » sauf preuve contraire (convention C-R1).

#### Réponses

Chaque critère reçoit « oui », « non » ou « sans objet ». « Sans objet » n'est admis que pour les critères qui ne visent qu'un sous-ensemble de types (grilles EU1 et EH1, fiche A10). Un critère non relevé vaut « non ».

#### Preuves

Chaque réponse « oui » s'appuie sur une pièce : relevé floristique daté, photographie géolocalisée, mesure (hauteur, couvert, épaisseur), plan. Pour un habitat créé, la pièce est un engagement écrit : clause du cahier des clauses techniques particulières, plan de gestion, palette végétale. L'attestation à l'achèvement vérifie les critères constatés sur les unités réalisées.

#### Espèces exotiques envahissantes

Les critères qui portent sur les espèces exotiques envahissantes se jugent sur la liste de l'Union (section 6.14), la liste nationale et les listes régionales des conservatoires botaniques nationaux (convention C-H8).

#### Couverts et pourcentages

Les couverts s'estiment en projection verticale, à 5 % près, sur toute l'unité ou par quadrats représentatifs : au moins 5 quadrats de 1 m² par hectare de prairie, répartis sur un transect en W, et au moins 3 par unité de moins d'un hectare (convention C-R2).

### 6.2 Grille EP1 : prairies de faible valeur

Types concernés : prairies de distinctivité anglaise 2 au plus (E2.6 prairies améliorées, E1.E et E2.8 pelouses piétinées, VB.5 pelouse d'agrément).

| Critère | Comment le relever |
|---|---|
| A (essentiel) | Compter les espèces de plantes vasculaires dans chaque quadrat de 1 m² ; le critère est satisfait si la moyenne atteint 6, dont au moins 2 dicotylédones autres que les espèces nitrophiles listées (chardons, rumex, ortie, renoncule rampante, grand plantain, trèfle rampant, cerfeuil sauvage). Si les espèces relevées sont caractéristiques d'une prairie de valeur moyenne ou plus, ou si 9 espèces ou plus sont présentes par m², l'unité relève de la grille EP2 et d'un autre type. |
| B | Estimer la part de la surface en herbe rase (moins de 7 cm) et en herbe haute (plus de 7 cm) : chacune doit atteindre 20 %. |
| C | Estimer le couvert des fourrés (ronce comprise) : moins de 20 % de la surface. Un fourré continu à plus de 90 % de couvert forme une unité séparée. |
| D | Repérer les dégradations physiques (ornières, piétinement, stockage, érosion) : moins de 5 % de la surface. |
| E | Estimer le sol nu : entre 1 % et 10 %. |
| F | Estimer le couvert de fougère aigle : moins de 20 %. |
| G | Rechercher les espèces exotiques envahissantes : aucune. |

Résultat anglais, pour mémoire : bon avec 6 ou 7 critères dont A, moyen avec 4 ou 5 dont A, mauvais sinon. OpenNAT calcule S = critères satisfaits / 7, plafonné à 0,5 si A échoue.

### 6.3 Grille EP2 : prairies de valeur moyenne à très haute

Types concernés : prairies et pelouses de distinctivité 4 et plus (E1, E2.1 à E2.3, E2.7, E3, E4, E5.2, E5.4, E5.5, VB.26).

| Critère | Comment le relever |
|---|---|
| A (essentiel) | Comparer la composition aux espèces caractéristiques du type (fiche habitat de la partie 4) : l'unité en est un bon exemple si ces espèces sont régulièrement présentes dans les quadrats et si les espèces d'un état dégradé restent minoritaires. |
| B | Hauteur variée : au moins 20 % sous 7 cm et 20 % au-dessus. |
| C | Sol nu entre 1 % et 5 %. |
| D | Fougère aigle sous 20 % et fourrés (ronce comprise) sous 5 %. |
| E | Espèces d'un état dégradé et dégradations physiques cumulées sous 5 % de la surface. |
| F (essentiel pour le bon état) | Au moins 10 espèces vasculaires par m² en moyenne, dont des dicotylédones caractéristiques du type ; les espèces nitrophiles et d'un état dégradé ne comptent pas. |

### 6.4 Grille EL1 : landes

Types concernés : landes (F4, F6, F7, F2.2) et lignes anglaises « heathland ».

| Critère | Comment le relever |
|---|---|
| A (essentiel) | Composition conforme au type, espèces indicatrices vasculaires et non vasculaires régulièrement présentes. |
| B (essentiel) | Au moins deux espèces d'arbrisseaux (callune, bruyères, myrtilles, ajoncs nains) fréquentes ; couvert d'arbrisseaux de 25 à 75 % en plaine. |
| C | Toutes les classes d'âge de la callune (pionnière, mûre, dégénérescente) présentes, dont au moins 10 % de stade pionnier en plaine. |
| D | Sol nu non ombragé de 1 à 10 %. |
| E | Aucune espèce exotique envahissante. |
| F | Aucune perturbation des zones sensibles (brûlage, passage d'engins). |
| G | Au plus un tiers des pousses de callune récemment broutées, ou callune fleurie fréquente à l'automne. |
| H | Arbres et fourrés épars (ajoncs exclus) sous 15 % en lande sèche de plaine, 10 % en lande humide, 20 % en montagne. |
| I | Ajoncs sous 50 %, ajonc d'Europe sous 25 %. |
| J | Fougère aigle sous 5 %. |
| K | Aucun drainage, extraction, dépôt, lixiviat ni eutrophisation. |

### 6.5 Grille EF1 : fourrés

Types concernés : fourrés (F3, F5, F9, F2.1, F2.3, F2.4, VB.9).

| Critère | Comment le relever |
|---|---|
| A | Fourré conforme au type, au moins 80 % d'essences indigènes. |
| B | Semis, jeunes plants, arbustes jeunes et mûrs tous présents. |
| C | Aucune espèce exotique envahissante ; espèces d'un état dégradé sous 5 % du sol. |
| D | Lisière étagée : arbustes épars et ourlet herbacé haut entre le fourré et l'habitat voisin. |
| E | Clairières, layons ou trouées qui ménagent des lisières abritées. |

### 6.6 Grille EM1 : mares et plans d'eau

Types concernés : C1, C2 (par la convention C-H4), VB.20, VB.21, VB.24.

| Critère | Comment le relever |
|---|---|
| A | Eau claire, sans signe de pollution (irisations, mousses, odeurs). Une turbidité due au bétail est admise. |
| B | Habitat semi-naturel (prairie, fourré, boisement indigènes) sur au moins 10 m tout autour. |
| C | Lentilles d'eau ou algues filamenteuses sur moins de 10 % de la surface. |
| D | Aucun raccordement artificiel à d'autres eaux (fossé agricole, canalisation). |
| E | Niveau libre de fluctuer naturellement, sans barrage, pompe ni canalisation. |
| F | Aucune espèce végétale ou animale exotique envahissante. |
| G | Pas d'empoissonnement. |
| H | Végétation aquatique (émergée, immergée, flottante, lentilles exclues) sur au moins 50 % de la partie de moins de 3 m de profondeur. |
| I | Surface ombragée à 50 % au plus. |

Période : de mai à août, en dehors d'une crue ou d'un assec exceptionnel. Résultat anglais pour mémoire : bon avec 9 critères, moyen avec 6 à 8.

### 6.7 Grille ER1 : milieux peu végétalisés

Types concernés : éboulis, falaises, dalles rocheuses, moraines, berges nues (H2, H3, H5, C3.6, C3.7, E1.1).

| Critère | Comment le relever |
|---|---|
| A | Milieu conforme au type, espèces indicatrices régulièrement présentes. |
| B | Fougère aigle, fourrés et arbres sous 25 %. |
| C | Aucune espèce exotique envahissante ; espèces d'un état dégradé sous 5 % de la surface végétalisée. |
| D | Recouvrement végétal entre 5 et 50 %. |

### 6.8 Grille EU1 : milieux urbains

Types concernés : types VB végétalisés, E5.1, et lignes anglaises « urban ».

| Critère | Applicable à | Comment le relever |
|---|---|---|
| A | tous | Aucune strate (herbacée, arbustive, arborée) ni aucun type de végétation ne dépasse 80 % de la surface. |
| B | tous | Présence d'espèces favorables à la faune, notamment de plantes à fleurs nectarifères dont les floraisons s'étalent du printemps à l'automne (palette végétale à l'appui). |
| C (essentiel) | tous | Espèces exotiques envahissantes sous 5 % de la surface végétalisée ; leur absence totale est exigée pour le bon état. |
| D | VB.8 friches | Mosaïque de substrat nu et d'au moins quatre communautés pionnières (annuelles, mousses, lichens, rudérales, espèces des sols inondables, pelouse ouverte, prairie fleurie, lande, mares temporaires). |
| E1 | VB.19, VB.24 | Plantes majoritairement indigènes. |
| E2 | VB.19, VB.24 | Végétation d'espèces de milieux humides ou riverains. |
| F | VB.13 | Au moins 50 % de plantes à fleurs ; 70 % de la toiture en sol et végétation, eau comprise. |
| G | VB.12 | Substrat d'épaisseur variée de 8 à 15 cm, au moins 50 % à 15 cm, semé de plantes sauvages et d'orpins ; tas de sable, pierres ou bois pour le bon état. |

Les jardins privatifs (VB.7) se relèvent sur l'ensemble des jardins d'une même opération, par échantillon d'au moins un jardin sur cinq (convention C-R4).

### 6.9 Grille EZ1 : zones humides

Types concernés : D, E3 (par leur ligne anglaise), C3.1 à C3.5, D6, E6.1.

| Critère | Comment le relever |
|---|---|
| A (essentiel) | Nappe à la surface ou proche de la surface toute l'année (eau libre ou sol saturé), sans drainage. Relevé au printemps et en fin d'été, ou par piézomètre. |
| B | Zone humide conforme au type, espèces indicatrices régulièrement présentes. |
| C | Eaux d'alimentation claires, sans signe de pollution. |
| D | Fourrés et arbres épars sous 10 %. |
| E | Sol nu sous 5 %. |
| F | Aucune espèce exotique envahissante ; espèces d'un état dégradé sous 5 %. |
| G | Litière continue sur 25 % au plus de la surface. |

La délimitation d'une zone humide au sens de l'article L. 211-1 du code de l'environnement (critères de sol et de végétation) précède le relevé de la grille ; elle n'en tient pas lieu.

### 6.10 Grille EB1 : boisements

Types concernés : boisements, parcs boisés, coupes (G, E7, G5.8).

Chacun des 13 indicateurs est noté de 1 à 3 (fiche A11) : âge des arbres, dégâts d'herbivores, espèces envahissantes, nombre d'essences indigènes, couvert indigène, espaces ouverts, régénération, santé des arbres, flore du sol, structure verticale, arbres vétérans, bois mort, perturbations. Les seuils de chaque note sont ceux de la fiche 24A de la métrique anglaise ; le relevé se fait sur placettes de 10 m de rayon, au moins une par hectare et au moins trois par unité (convention C-R3).

### 6.11 Grille EA1 : arbres

Types concernés : VB.18a, VB.18b, G5.1.

| Critère | Comment le relever |
|---|---|
| A | Essence indigène (au moins 70 % des arbres d'un groupe). |
| B | Couvert continu pour un groupe (trouées sous 10 %, aucune de plus de 5 m) ; réputé satisfait pour un arbre isolé. |
| C | Arbre mûr (plus de 50 % des arbres d'un groupe). |
| D | Pas d'atteinte humaine à la santé de l'arbre ni de taille régulière ; plus de 75 % du houppier naturel conservé. |
| E | Microhabitats présents : bois mort, cavités, lierre, écorce décollée. |
| F | Plus de 20 % du houppier au-dessus d'une végétation, et non d'un sol revêtu. |

Chaque arbre ou groupe se relève séparément ; le diamètre se mesure à 1,30 m.

### 6.12 Grille EH1 : haies

Types concernés : FA.1 à FA.4.

| Attribut | Comment le relever |
|---|---|
| A1 | Hauteur moyenne de la partie ligneuse supérieure à 1,5 m. |
| A2 | Largeur moyenne supérieure à 1,5 m. |
| B1 | Espace entre le sol et le feuillage inférieur à 0,5 m sur plus de 90 % de la longueur. |
| B2 | Trouées sur moins de 10 % de la longueur, aucune de plus de 5 m. |
| C1 | Bande d'au moins 1 m de sol non perturbé à végétation herbacée vivace, sur au moins un côté et plus de 90 % de la longueur. |
| C2 | Espèces nitrophiles (ortie, gaillet gratteron, rumex) sur moins de 20 % de cette bande. |
| D1 | Plus de 90 % de la haie et de sa bande exempts d'espèces exotiques envahissantes. |
| D2 | Plus de 90 % exempts de dégradations d'origine humaine. |
| E1 (haies avec arbres) | Plusieurs classes d'âge d'arbres et au moins un arbre mûr tous les 20 à 50 m. |
| E2 (haies avec arbres) | Au moins 95 % des arbres de la haie en bonne santé. |

Le relevé se fait par tronçons homogènes de 100 m au plus (convention C-R4).

### 6.13 Grille EV1 : vergers

Types concernés : G1.D, G2.9 (vergers traditionnels).

| Critère | Comment le relever |
|---|---|
| A (essentiel pour le bon état) | Arbres anciens ou vétérans présents. |
| B (essentiel pour le bon état) | Bois mort pour au moins 20 % des arbres mûrs. |
| C | Moins de 5 % des fruitiers étouffés par les fourrés ; fourrés sur moins de 10 % du sol. |
| D | Taille de formation ou de restauration qui prolonge la vie des arbres. |
| E | Au moins 95 % des arbres sans dégâts (abroutissement, écorçage, liens). |
| F | Prairie non surpâturée, piétinement sous 10 % des houppiers au plus. |
| G | Prairie d'une richesse équivalente à une prairie de valeur moyenne ou plus. |
| H | Aucune espèce exotique envahissante ; espèces d'un état dégradé sous 10 % du sol. |

### 6.14 Espèces exotiques envahissantes préoccupantes pour l'Union

Liste au 19 juillet 2022 (règlement d'exécution (UE) 2016/1141 modifié par les règlements d'exécution 2017/1263, 2019/1262 et 2022/1203), d'après le Centre de ressources espèces exotiques envahissantes. Une mise à jour a été adoptée par le règlement d'exécution (UE) 2025/1422 du 17 juillet 2025 ; son contenu n'a pas été relu pour cette édition et doit être intégré avant la validation.

| Groupe | Espèces |
|---|---|
| Plantes aquatiques | Cabomba caroliniana, Eichhornia crassipes, Elodea nuttalii, Gymnocoronis spilanthoides, Hydrocotyle ranunculoides, Lagarosiphon major, Ludwigia grandiflora, Ludwigia peploides, Myriophyllum aquaticum, Myriophyllum heterophyllum, Pistia stratiotes, Salvinia molesta |
| Plantes terrestres | Acacia saligna, Ailanthus altissima, Alternanthera philoxeroides, Andropogon virginicus, Asclepias syriaca, Baccharis halimifolia, Cardiospermum grandiflorum, Celastrus orbiculatus, Cortaderia jubata, Ehrharta calycina, Gunnera tinctoria, Hakea sericea, Heracleum mantegazzianum, Heracleum persicum, Heracleum sosnowskyi, Humulus scandens, Impatiens glandulifera, Koenigia polystachya, Lespedeza cuneata, Lygodium japonicum, Lysichiton americanus, Microstegium vimineum, Parthenium hysterophorus, Pennisetum setaceum, Polygonum perfoliatum, Prosopis juliflora, Pueraria montana var. lobata, Triadica sebifera |
| Invertébrés | Arthurdendyus triangulatus, Eriocheir sinensis, Faxonius rusticus, Limnoperna fortunei, Orconectes limosus, Orconectes virilis, Pacifastacus leniusculus, Procambarus fallax f. virginalis, Procambarus clarkii, Solenopsis geminata, Solenopsis invicta, Solenopsis richteri, Vespa velutina nigrithorax, Wasmannia auropunctata |
| Poissons | Ameiurus melas, Channa argus, Fundulus heteroclitus, Gambusia affinis, Gambusia holbrooki, Lepomis gibbosus, Morone americana, Perccottus glenii, Plotosus lineatus, Pseudorasbora parva |
| Reptiles et amphibiens | Lampropeltis getula, Lithobates catesbeianus, Trachemys scripta, Xenopus laevis |
| Oiseaux | Acridotheres tristis, Alopochen aegyptiaca, Corvus splendens, Oxyura jamaicensis, Pycnonotus cafer, Threskiornis aethiopicus |
| Mammifères | Axis axis, Callosciurus erythraeus, Callosciurus finlaysonii, Herpestes javanicus, Muntiacus reevesi, Myocastor coypus, Nasua nasua, Nyctereutes procyonoides, Ondatra zibethicus, Procyon lotor, Sciurus carolinensis, Sciurus niger, Tamias sibiricus |
| Algues marines | Rugulopteryx okamurae |

L'orthographe de quelques noms scientifiques de la liste source a été rectifiée (Arthurdendyus, Asclepias, Alopochen aegyptiaca, Nyctereutes procyonoides). Source : Centre de ressources espèces exotiques envahissantes, liste au 19 juillet 2022, https://especes-exotiques-envahissantes.fr/wp-content/uploads/2024/07/220719_liste_rue_eee.pdf.
