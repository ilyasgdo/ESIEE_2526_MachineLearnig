3. Datasets disponibles
3.1 ImageNet VID
Description
ImageNet VID (Video Object Detection from ImageNet) constitue le benchmark standard de référence pour évaluer les performances des algorithmes de détection d'objets en vidéo. Dérivé du célèbre dataset ImageNet utilisé pour la classification d'images, ImageNet VID étend ce corpus aux séquences vidéo avec annotations temporelles cohérentes.​

Caractéristiques
Le dataset comprend approximativement 4000 séquences vidéo réparties en ensembles d'entraînement et de validation. Les vidéos couvrent 30 catégories d'objets issues de la taxonomie ImageNet, incluant notamment différentes espèces animales (chien, chat, hamster, etc.), véhicules, et objets du quotidien.​

Les annotations fournissent des bounding boxes avec labels de classe pour chaque objet visible dans les frames sélectionnées. Les vidéos présentent des résolutions variables et capturent des scènes naturelles avec mouvements de caméra, changements d'échelle, occlusions partielles et variations d'éclairage - conditions représentatives des défis réels de détection vidéo.​

ImageNet VID est particulièrement utilisé pour évaluer les algorithmes gérant la cohérence temporelle, comme démontré par les résultats de référence: TGBFormer atteint 86.5% mAP à 41 FPS, ClipVID 84.7% mAP à 39.3 FPS sur ce benchmark.​

Forces
Standard industrie reconnu: ImageNet VID bénéficie d'une adoption massive par la communauté recherche, permettant des comparaisons directes et objectives entre différentes approches. Pratiquement tous les articles sur la détection vidéo rapportent des résultats sur ce dataset.​

Annotations haute qualité: Les bounding boxes et labels sont vérifiés manuellement, garantissant une ground truth fiable pour l'entraînement et l'évaluation.​

Défis vidéo réalistes: Les séquences capturent authentiquement les difficultés de la détection vidéo: mouvement rapide, flou de mouvement, occlusions temporaires, changements d'apparence.​

Diversité temporelle: Contrairement aux datasets d'images statiques, ImageNet VID permet d'évaluer explicitement la capacité des modèles à exploiter l'information temporelle pour améliorer la détection.​

Biais identifiés
Échelle limitée: Avec environ 4000 vidéos, ImageNet VID est significativement plus petit que les datasets d'images statiques modernes. Cette échelle limitée peut restreindre la diversité des scènes et situations capturées.​

Surreprésentation de certaines catégories: Comme dans ImageNet classification, certaines catégories (notamment différentes races de chiens) sont sur-représentées tandis que d'autres objets courants sont absents. Ce déséquilibre peut biaiser les modèles vers une meilleure performance sur les catégories majoritaires.​

Longueur des séquences: Les vidéos sont relativement courtes, limitant l'évaluation des capacités de modélisation temporelle à très long terme.​

Résolution variable: La variabilité des résolutions, bien que reflétant la diversité réelle, peut compliquer l'entraînement et nécessiter un prétraitement soigneux.​

Utilisation recommandée
ImageNet VID est idéal pour le benchmarking et la comparaison de performances entre différentes architectures de détection vidéo. Son statut de standard industrie en fait une référence incontournable pour toute publication scientifique dans le domaine.​

Pour un projet industriel, ImageNet VID peut servir de dataset de validation pour vérifier que les performances d'un modèle sont alignées avec l'état de l'art publié, avant de l'appliquer à des données spécifiques au domaine cible.

3.2 YouTube-VOS
Description
YouTube-VOS (YouTube Video Object Segmentation) est un dataset à large échelle spécifiquement conçu pour l'apprentissage spatial-temporel dans les tâches de segmentation vidéo. La version 2018 originale contient 4,453 clips vidéo YouTube couvrant 78 catégories d'objets, incluant objets courants, animaux et activités humaines. La version 2021 étendue comprend 3,859 vidéos avec des améliorations de catégorisation.​

Caractéristiques
Clips de 3-6 secondes: Chaque vidéo est soigneusement sélectionnée pour éviter les transitions de scène, crédits, ou conditions visuelles dégradées (trop sombre, flou excessif). Cette durée courte mais ciblée assure un contenu dense et pertinent.​

Annotations pixel-level: Contrairement aux bounding boxes approximatives, YouTube-VOS fournit des masques de segmentation précis traçant les contours exacts des objets. Les annotations sont effectuées tous les 5 frames dans des vidéos capturées à 30 FPS, résultant en un taux d'échantillonnage de 6 FPS. Cette stratégie skip-frame réduit considérablement l'effort d'annotation tout en exploitant la forte corrélation temporelle entre frames successives.​

Objets multiples par vidéo: Les annotateurs sont instruits de labelliser jusqu'à 5 objets de tailles appropriées par clip. Pour les vidéos d'activités, tant le sujet humain que les objets avec lesquels il interagit sont annotés (par exemple, personne et skateboard dans une vidéo de skateboarding).​

133,886 annotations dans la version 2018, soit 33 fois plus que les meilleurs datasets vidéo existants à l'époque. La version 2021 atteint 232k annotations sur 8,171 instances vidéo uniques.​

Forces
Large échelle sans précédent: YouTube-VOS offre un volume de données 33 fois supérieur aux datasets de segmentation vidéo précédents, permettant un entraînement profond sans surapprentissage rapide.​

Diversité des scènes et objets: Provenant de YouTube, les vidéos capturent une immense variété de scènes du monde réel, conditions d'éclairage, mouvements de caméra, et contextes d'apparition des objets.​

Catégories de validation unique pour la généralisation: 26 catégories dans l'ensemble de validation n'apparaissent pas dans l'entraînement, permettant d'évaluer explicitement la capacité de généralisation des modèles à des objets non vus.​

Annotations pixel-level de haute qualité: Les contours précis sont tracés manuellement plutôt qu'approximés par polygones grossiers, fournissant une supervision fine pour l'apprentissage.​

Scénarios réalistes: Les vidéos YouTube reflètent authentiquement la diversité visuelle rencontrée dans les applications réelles, avec occlusions naturelles, changements d'apparence, et déformations non linéaires.​

Limites
Vidéos courtes (3-6 secondes): Cette durée limite l'évaluation des capacités de modélisation temporelle à très long terme ou de tracking persistant sur des minutes. Les modèles peuvent ne pas être testés sur leur robustesse à des changements d'apparence drastiques survenant sur de longues durées.​

Annotations skip-frame: Avec annotations tous les 5 frames seulement, les modèles doivent interpoler ou propager l'information sur les frames intermédiaires. Cette stratégie réduit certes les coûts mais peut manquer des événements rapides se produisant entre frames annotées.​

Complexité variable: La difficulté des vidéos YouTube varie considérablement - certaines scènes sont simples avec arrière-plans statiques, d'autres extrêmement complexes avec multiples objets en mouvement rapide. Cette variabilité peut compliquer l'analyse des forces/faiblesses des modèles.​

Biais de popularité YouTube: Les vidéos proviennent de contenus populaires YouTube, potentiellement sur-représentant certains types de scènes (sports, animaux mignons, événements spectaculaires) au détriment de scènes quotidiennes plus banales.​

Utilisation recommandée
YouTube-VOS est idéal pour l'entraînement de modèles génériques de détection et segmentation vidéo nécessitant robustesse et généralisation à des scènes variées. Sa large échelle et diversité en font un excellent choix pour le pré-entraînement avant fine-tuning sur datasets spécifiques.​

Pour des applications nécessitant segmentation précise au niveau pixel (édition vidéo, effets spéciaux, réalité augmentée), YouTube-VOS fournit la supervision détaillée requise.​

3.3 COCO (Common Objects in Context)
Description
COCO est un dataset à très large échelle pour la reconnaissance d'objets, contenant 330,000 images dont 200,000 avec annotations pour détection, segmentation et captioning. Bien que conçu pour images statiques, COCO est massivement utilisé pour pré-entraîner les modèles de détection vidéo avant application aux séquences temporelles.​

Caractéristiques
80 catégories d'objets: COCO couvre des objets courants comme personnes, véhicules, animaux, mobilier, ustensiles, nourriture, équipements sportifs et électroniques. Cette sélection reflète les objets fréquemment rencontrés dans la vie quotidienne.​

1.5 millions d'instances annotées: En moyenne ~47 objets par image, significativement plus dense que ImageNet (~1.46 objets/image). Cette densité élevée force les modèles à gérer des scènes encombrées avec multiples objets se chevauchant.​

Annotations riches multi-tâches:​

Bounding boxes pour détection d'objets

Masques de segmentation instance-level

Annotations keypoint pour 250,000+ personnes (pose humaine)

Segmentation stuff pour 91 catégories d'arrière-plans amorphes

5 captions textuelles par image décrivant la scène

Ensembles standardisés: Train2017 (118K images), Val2017 (5K images), Test2017 (20K images). Les labels test ne sont pas publics, nécessitant soumission au serveur d'évaluation COCO pour obtenir les scores officiels.​

Usage pour la vidéo
COCO sert principalement au pré-entraînement des backbones (ResNet, EfficientNet, transformers) avant leur utilisation dans les architectures de détection vidéo. Les modèles YOLO, par exemple, sont systématiquement pré-entraînés sur COCO avant adaptation aux séquences vidéo.​

Les performances sur COCO sont devenues un indicateur de qualité pour les détecteurs: YOLOv11x atteint 54.7% mAP, MI-DETR 52.4% mAP en seulement 12 epochs. Ces résultats sur images statiques prédisent généralement bien les capacités sur vidéos.​

Forces
Très large échelle: 330K images permettent un pré-entraînement robuste sans surapprentissage, fournissant des features visuelles génériques transférables.​

Intégration facilitée: Support natif dans tous les frameworks modernes (PyTorch, TensorFlow, Ultralytics). Scripts de téléchargement et d'évaluation standardisés largement adoptés par la communauté.​

Métriques standardisées: mAP à différents seuils IoU (50, 75, 50:95) permettant comparaisons rigoureuses et objectives.​

Objets en contexte: Contrairement à ImageNet centré sur objets isolés, COCO capture des scènes naturelles complexes avec multiples objets interagissant dans leur contexte environnemental. Cette propriété améliore la compréhension contextuelle des modèles.​

Limites
Images statiques uniquement: COCO ne contient aucune information temporelle, limitant son utilité directe pour la détection vidéo. Les modèles pré-entraînés sur COCO doivent être adaptés pour exploiter la dimension temporelle.​

Biais vers objets moyens et grands: Les objets très petits (< 32×32 pixels) sont sous-représentés comparés aux tailles moyennes et grandes. Les modèles entraînés sur COCO peuvent donc sous-performer sur détection de petits objets dans vidéos de surveillance ou aériennes.​

Distribution de catégories déséquilibrée: Certaines catégories (personne, voiture, chaise) dominent largement, tandis que d'autres sont rares. Ce déséquilibre peut biaiser les modèles vers les catégories fréquentes.​

Annotations statiques: Les bounding boxes et masques sont optimisés pour images figées et peuvent ne pas capturer adéquatement les trajectoires et dynamiques d'objets en mouvement.​

Utilisation recommandée
COCO est incontournable pour le pré-entraînement de tout modèle de détection, que la cible finale soit images ou vidéos. Ses features visuelles bas-niveau (contours, textures, formes) se transfèrent excellemment aux tâches vidéo.​

Pour des applications de détection générique où les 80 catégories COCO correspondent aux besoins, utiliser des modèles pré-entraînés COCO puis fine-tuner sur un petit dataset vidéo spécifique peut suffire.​

3.4 DAVIS (Densely Annotated VIdeo Segmentation)
Description
DAVIS est un benchmark de haute qualité spécifiquement conçu pour évaluer la segmentation vidéo d'objets. DAVIS 2016 contient 50 séquences Full HD (1080p) capturées à 24 FPS, chacune accompagnée d'annotations pixel-accurate sur tous les frames. DAVIS 2017 étend le dataset à 90 séquences avec support multi-objets.​

Caractéristiques
Séquences courtes de haute qualité: Chaque vidéo dure environ 2-4 secondes, couvrant 3,455 frames annotés dans DAVIS 2016. Malgré leur brièveté, ces séquences capturent l'ensemble des défis majeurs de la segmentation vidéo: occlusions, flou de mouvement, changements d'apparence, déformations non linéaires, mouvement rapide.​

Annotations pixel-level exhaustives: Contrairement aux approches skip-frame, chaque frame dispose d'un masque de segmentation binaire tracé manuellement avec précision pixel. Cette densité d'annotation extrême garantit une ground truth parfaite mais explique l'échelle limitée du dataset.​

Attributs de défis annotés: Chaque vidéo est étiquetée avec ses défis spécifiques (occlusion, mouvement rapide, déformation, flou), permettant une analyse fine des forces/faiblesses des algorithmes selon le type de difficulté.​

Métriques d'évaluation complètes: DAVIS fournit trois métriques complémentaires mesurant l'étendue spatiale de la segmentation (region similarity J), la précision des contours de silhouette (contour accuracy F), et la cohérence temporelle (temporal stability T).​

Forces
Annotations pixel-perfect: La précision maximale des masques manuels sur tous les frames fournit la meilleure supervision possible pour entraînement et la ground truth la plus fiable pour évaluation.​

Qualité vidéo Full HD: La résolution 1080p préserve les détails fins essentiels pour une segmentation précise, reflétant les standards vidéo modernes.​

Benchmark reconnu pour segmentation: DAVIS est devenu la référence standard pour comparer les méthodes de segmentation vidéo, avec des leaderboards actifs et workshops dédiés.​

Couverture exhaustive des défis: Malgré seulement 50 séquences, DAVIS capture systématiquement tous les cas difficiles majeurs rencontrés en segmentation vidéo réelle.​

Limites
Échelle très limitée: 50 séquences dans DAVIS 2016 (90 dans DAVIS 2017) est minuscule comparé aux milliers de vidéos de YouTube-VOS ou millions d'images de COCO. Cette petite taille limite sévèrement l'entraînement de modèles deep learning modernes, qui nécessitent de vastes données.​

Performances saturées: Les algorithmes state-of-the-art atteignent maintenant environ 80% de performance sur DAVIS 2016, approchant de la saturation. Le dataset commence à manquer de pouvoir discriminant entre méthodes avancées.​

Coût d'annotation prohibitif: L'annotation pixel-level exhaustive de tous les frames explique pourquoi DAVIS ne peut être étendu facilement à plus grande échelle.​

Focus segmentation, pas détection: DAVIS cible la segmentation binaire (objet vs arrière-plan) plutôt que la détection multi-classe avec classification. Son utilité est donc limitée pour les tâches de détection d'objets typiques.​

Utilisation recommandée
DAVIS est idéal pour benchmark et recherche en segmentation vidéo, particulièrement pour valider que de nouvelles méthodes atteignent des performances compétitives avec l'état de l'art.​

Pour des projets industriels nécessitant segmentation très précise d'objets spécifiques (par exemple, effets spéciaux cinématographiques, chirurgie assistée par ordinateur), DAVIS peut servir de dataset de validation qualité, mais son échelle limitée nécessite complémentation par des données domaine-spécifiques.​

3.5 OD-VIRAT
Description
OD-VIRAT (Object Detection VIRAT) est un benchmark à large échelle spécifiquement conçu pour évaluer la détection d'objets dans des conditions de surveillance réalistes. Dérivé du dataset VIRAT Ground 2.0 pour reconnaissance d'événements vidéo, OD-VIRAT se décline en deux variantes: OD-VIRAT Large avec 8.7 millions d'instances annotées dans 599,996 images, et OD-VIRAT Tiny avec 288,901 instances dans 19,860 images.​

Caractéristiques
10 scènes de surveillance diversifiées: Les vidéos couvrent chantiers de construction, parkings, rues, et espaces extérieurs ouverts, capturées par caméras statiques montées à hauteur significative (généralement au sommet de bâtiments).​

Objets à petite échelle: La distance et hauteur de capture résultent en objets de très petite taille à l'image, représentant un défi majeur pour les détecteurs. Cette caractéristique reflète fidèlement les conditions réelles de surveillance où les sujets d'intérêt apparaissent souvent minuscules.​

5 catégories spécialisées surveillance: Bike/Bicycle, Car, Carrying_object (personne portant un objet), Person, Vehicle. Cette sélection ciblée correspond aux besoins typiques de systèmes de surveillance sécuritaire.​

Arrière-plans complexes: Les scènes présentent des arrière-plans encombrés, variations d'éclairage, et occlusions fréquentes - conditions rendant la détection particulièrement difficile.​

Stratégies de sampling différenciées: OD-VIRAT Large extrait tous les frames (0 frame-skip) pour créer un dataset gigantesque, tandis qu'OD-VIRAT Tiny utilise un sampling tous les 30 frames pour fournir un subset plus maniable pour prototypage rapide.​

Forces
Conditions de surveillance authentiques: Contrairement aux datasets génériques, OD-VIRAT capture spécifiquement les défis réels de la vidéosurveillance: vue plongeante, objets distants et petits, scènes encombrées.​

Échelle massive (Large): 8.7 millions d'instances représentent l'un des plus grands datasets de détection d'objets existants, permettant entraînement robuste de modèles complexes sans surapprentissage.​

Benchmarking spécialisé: OD-VIRAT permet d'évaluer les performances sur des cas d'usage surveillance que COCO ou ImageNet VID ne couvrent pas adéquatement.​

Résolutions HD: Vidéos capturées en 1920×1080 ou 1280×720 pixels à 25-30 FPS, reflétant les standards modernes de vidéosurveillance.​

Limites
Spécialisé surveillance uniquement: Les 10 scènes et 5 catégories sont optimisées pour applications de sécurité, limitant sévèrement la généralisation à d'autres domaines (retail, conduite autonome, analyse sportive). Un modèle entraîné sur OD-VIRAT performera probablement mal sur objets hors de ces catégories ou scènes non-surveillance.​

Très petits objets challengeants: La prédominance d'objets de taille inférieure à 32×32 pixels rend le dataset extrêmement difficile, potentiellement décourageant pour établir des baselines initiales.​

Diversité limitée des catégories: Seulement 5 catégories comparées aux 80 de COCO ou 78 de YouTube-VOS restreint l'utilité pour applications multi-catégories.​

Biais géographique et temporel: Toutes les vidéos proviennent du dataset VIRAT original capturé dans des contextes et périodes spécifiques, pouvant ne pas représenter la diversité mondiale des systèmes de surveillance.​

Utilisation recommandée
OD-VIRAT Large est optimal pour développer des systèmes de surveillance haute performance nécessitant robustesse aux objets petits et distants dans des environnements complexes. Les entreprises de sécurité, smart cities, ou gestion de flux de foule bénéficieraient grandement de ce dataset.​

OD-VIRAT Tiny est idéal pour prototypage rapide et tests avant engagement sur l'entraînement complet avec Large. Son échelle réduite (19,860 images) permet itérations rapides d'expérimentation.​

Pour benchmarking d'algorithmes spécialisés dans la détection de petits objets, OD-VIRAT fournit un test rigoureux que les datasets génériques ne peuvent offrir.​

Tableau comparatif des datasets
Ce tableau synthétique permet de sélectionner rapidement le ou les datasets les plus appropriés selon les contraintes du projet (échelle, type d'annotations, domaine d'application, biais acceptables).​