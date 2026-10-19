# Contrôle d'ordre de grandeur du module G face à l'étude Carbone 4

Méthode OpenNAT 1, moteur 0.2.0, données 1.2.1. Note du lot 4 (cahier des charges, § 7), 19 octobre 2026. Méthode en attente de validation du Biodiversity Standard Council.

Le cahier des charges demande de situer la biodiversité grise calculée par OpenNAT (module G, indicateur Inat) face à l'étude de Carbone 4 et d'expliquer les écarts. Sur le périmètre que les deux calculs partagent, OpenNAT donne 54 m²HE·an par m² de plancher là où Carbone 4 donne 44 PDF.m².yr : même ordre de grandeur, rapport de 1,0 à 1,5 selon l'empreinte carbone supposée. Deux écarts de structure subsistent : OpenNAT ne compte pas la pollution, qui fait la moitié du résultat de Carbone 4, et pénalise le bois nettement plus fort.

## L'étude de référence

Carbone 4, « La biodiversité grise dans le bâtiment : comment estimer l'impact des matériaux de construction sur la nature ? », position paper de 30 pages, octobre 2026, étude financée par Altarea et Nexity, modélisation par la plateforme Darwin selon la méthode IMPACT World+. Les fiches INIES fournissent le climat, l'acidification et l'eutrophisation ; l'occupation et la transformation des sols et l'écotoxicité viennent de jeux ecoinvent mis à l'échelle de l'empreinte carbone de chaque fiche.

| Grandeur lue | Valeur |
|---|---|
| Bâtiment type | 50 logements collectifs, 3 000 m², R+4, structure béton, phases A1-A3, environ 80 % de l'empreinte carbone des matériaux modélisée |
| Biodiversité grise | 272 000 PDF.m².yr, soit 91 par m² de plancher |
| Répartition par pression | pollution 51 %, changement climatique 38 %, changement d'usage des sols 11 % |
| Variante biosourcée (façade ossature bois, fenêtres bois, parquet massif) | 314 000 PDF.m².yr (+15 %), dont usage des sols 27 % |
| Impact in situ, terrain naturel intact | 58 000 PDF.m².yr pour 1 250 m² sur 50 ans, 40 % de conversion et 60 % d'occupation |

Carbone 4 ne publie ni l'empreinte carbone du bâtiment type, ni ses quantités de matériaux, ni ses valeurs par matériau (graphiques seulement). Les auteurs écrivent que leurs incertitudes sont importantes, que leurs facteurs sont pour la plupart mondiaux et que l'usage des sols est probablement sous-estimé, le modèle prenant par défaut une prairie comme écosystème de départ.

## Ce qui se compare

Les deux métriques ne sont pas commensurables. Le PDF d'IMPACT World+ est une fraction d'espèces potentiellement disparues ; le m²HE d'OpenNAT est une surface d'habitat de qualité 1, fondée sur la MSA de GLOBIO. L'audit n'a trouvé aucune conversion publiée de l'une vers l'autre. Le contrôle les rapproche à 1 pour 1 : une fraction d'espèces perdue sur un m² pendant un an compte comme un m²HE·an. Ce rapprochement ne vaut que pour juger d'un ordre de grandeur.

Les périmètres diffèrent aussi :

| Point | Carbone 4 | OpenNAT, module G |
|---|---|---|
| Pressions | pollution, climat, usage des sols, eau | climat, usage des sols (forêts pour le bois, carrières pour les granulats) ; pollution affichée à part, non convertie (point P19) |
| Phases | A1-A3 | A1-A5, B, C (D exclu) |
| Matériaux | environ 80 % de l'empreinte carbone | toutes les émissions du RSEE ; usage des sols limité au bois et aux granulats (convention C-G7) |
| Usage des sols du bois | facteurs mondiaux de forêt exploitée, prairie comme état de départ | toute la forêt nécessaire à la pousse, comptée à la perte de MSA du régime d'exploitation (conventions C-G4 et C-G5) |

Le contrôle se fait donc sur le périmètre commun : climat et usage des sols, phases A1-A3, par m² de plancher.

## Hypothèses du contrôle

Faute de métrés publiés, le bâtiment type est décrit dans OpenNAT par des hypothèses déclarées. `python -m banc.carbone4` recalcule chaque nombre de cette note avec le module G du moteur et l'écrit dans `banc/carbone4.json` ; les valeurs de Carbone 4 sont celles que l'audit du lot 0 (§ 2.4) a lues dans le document fourni le 17 octobre 2026.

| Hypothèse | Valeur | Origine |
|---|---|---|
| S_ref | 3 000 m² | surface du bâtiment type de Carbone 4 |
| Émissions A1-A3 | 470 kg CO2 éq./m², plage étudiée de 350 à 600 | exemple de l'annexe C de la méthode |
| Granulats | 2,4 t par m² | rapport du cas 7a (bâtiment béton) |
| Bois dans le bâtiment béton | 5 litres par m², soit 15 m³, coupe rase | rapport du cas 7a |
| Parquet massif de la variante biosourcée | 2 400 m² en lames de 14 à 20 mm, soit 34 à 48 m³ | surface habitable d'environ 80 % des 3 000 m² |

## Résultats

| Par m² de plancher | Carbone 4 (PDF.m².yr) | OpenNAT (m²HE·an) | Rapport |
|---|---|---|---|
| Changement climatique | 34,5 | 42,5 | 1,23 |
| Usage des sols | 10,0 | 11,3 (bois 9,3 ; carrières 2,0) | 1,13 |
| Périmètre commun | 44,4 | 53,8 | 1,21 |
| Pollution | 46,2 | non comptée | |
| Total publié | 90,7 | 53,8 | 0,59 |

Avec des émissions A1-A3 de 350 puis 600 kg CO2 éq./m², le total OpenNAT passe de 42,9 à 65,5 m²HE·an par m², soit un rapport de 0,97 à 1,47 au périmètre commun.

## Lecture des écarts

### Climat

OpenNAT compte 0,0904 m²HE·an par kg CO2 éq. émis en A1-A3 (facteur de 1,807 × 10⁻³ m²HE par kg, subi pendant les 50 ans de persistance, convention C-G2). Le climat des deux calculs coïncide si le bâtiment type émet 381 kg CO2 éq./m² sur ses éléments modélisés, soit 477 kg CO2 éq./m² ramenés à la totalité des matériaux, puisque Carbone 4 en modélise 80 %. Cette valeur est celle que l'exemple de l'annexe C suppose (470). Carbone 4 ne publiant pas son empreinte carbone, la coïncidence ne démontre pas que les deux facteurs sont égaux ; elle montre qu'ils ne divergent pas d'un ordre de grandeur. Les deux voies sont pourtant indépendantes : OpenNAT passe par la réponse du climat aux émissions cumulées (TCRE du GIEC) et la perte de MSA par degré de GLOBIO ; IMPACT World+ par ses propres facteurs d'effet sur les écosystèmes.

### Usage des sols du bâtiment béton

Les deux valeurs sont proches (11,3 contre 10,0), mais pour des raisons différentes. Chez OpenNAT, 82 % de l'usage des sols vient des 15 m³ de bois supposés ; les carrières ne pèsent que 2 m²HE·an par m², et les usines (cimenteries, aciéries) ne sont pas comptées (C-G7). Chez Carbone 4, l'usage des sols couvre l'extraction et la transformation de tous les matériaux, par les jeux ecoinvent. OpenNAT sous-estime donc l'usage des sols des matériaux minéraux et métalliques ; l'égalité des totaux est en partie fortuite.

### Bois

OpenNAT compte 1 852 m²HE·an par m³ de bois de coupe rase (1 111 en coupe sélective justifiée) : 10 000 m² par hectare divisés par une production de 5,4 m³ par hectare et par an, multipliés par 2 m³ de bois rond par m³ de produit et par une perte de MSA de 0,5. Pour la variante biosourcée, Carbone 4 trouve une hausse de l'usage des sols de 54 860 PDF.m².yr. OpenNAT l'atteint avec 30 m³ de bois de coupe rase ; le parquet massif seul en représente déjà 34 à 48, et la façade ossature bois et les fenêtres s'y ajoutent. À métrés égaux, OpenNAT pénalise le bois plusieurs fois plus que Carbone 4. Le parquet seul ajouterait 21 à 30 m²HE·an par m², soit +38 % à +55 % sur le bâtiment béton, quand Carbone 4 trouve +15 % pour toute la variante. Le cas 7 de la méthode (structure entière en bois, 900 m³) en donne la forme extrême : Inat six fois plus fort que pour le béton.

Trois conventions expliquent cet écart, et ce sont celles que la partie 8 désigne déjà comme les premières à recalibrer :

- C-G5, approche attributionnelle : toute la forêt de production est comptée comme une perte par rapport à la forêt naturelle, au prorata de la perte de MSA du régime ; IMPACT World+ compare l'occupation forestière à un état de référence moins exigeant, et Carbone 4 écrit que l'usage des sols est probablement sous-estimé chez lui ;
- C-G4, rapport de 2 m³ de bois rond par m³ de produit, qui double l'occupation ;
- C-G7, absence d'occupation des usines et des carrières de ciment, qui avantage le béton par comparaison.

Une observation va dans le même sens chez Carbone 4 : la part du climat de la variante biosourcée (35 % de 314 000, soit 110 000) n'est pas inférieure à celle du bâtiment béton (38 % de 272 000, soit 103 000). Le gain carbone que le module G accorde au bois (cas 7 : émissions A1-A3 de 400 au lieu de 560 kg CO2 éq./m²) n'apparaît pas dans cette variante partielle.

### Pollution

C'est le plus grand écart : 46 PDF.m².yr par m², la moitié du résultat de Carbone 4, « très largement due aux produits en béton » selon l'étude. OpenNAT reprend les indicateurs de pollution du RSEE (acidification, eutrophisation, écotoxicité, formation d'ozone) et les affiche à part, sans les convertir, faute de facteur de passage sourcé vers la MSA (convention C-G8, point P19 de l'audit). Inat mesure donc environ la moitié de ce que Carbone 4 appelle biodiversité grise, et la part manquante pèse surtout sur le béton. Combler cet écart rapprocherait aussi le bois et le béton.

### Impact in situ

Carbone 4 compte 46 PDF.m².yr par m² de terrain naturel intact sur 50 ans ; OpenNAT, sur le cas 2 (prairie riche construite en logements), 33 m²HE·an par m² de parcelle. Même ordre de grandeur, avec un état initial moins favorable chez OpenNAT, qui part de l'état relevé et non d'un écosystème intact. La part du site dans l'impact total est de 18 % chez Carbone 4 et de 36 % pour le cas 2 d'OpenNAT ; en doublant Inat pour y ajouter une pollution de même poids que chez Carbone 4, elle tombe à 22 %. L'écart de part tient donc à la pollution, pas au calcul du site.

## Conséquences pour la méthode

1. Le module G est dans l'ordre de grandeur de l'étude Carbone 4 sur le périmètre commun ; rien n'impose de revoir le facteur climat.
2. Les seuils d'Inat et de Snat ne doivent pas être fixés avant que la pollution soit traitée : sans elle, Inat compte environ la moitié de l'impact selon Carbone 4.
3. Le bois est le premier point à soumettre au Biodiversity Standard Council : conventions C-G4, C-G5 et C-G7, déjà désignées par la lecture du cas 7.
4. Le contrôle est à refaire dès qu'une étude publie à la fois ses métrés, son empreinte carbone et sa biodiversité grise, ou qu'un second bâtiment type est modélisé par les deux méthodes.
