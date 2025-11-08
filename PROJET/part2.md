2. État de l'art des méthodes
2.1 Famille YOLO (You Only Look Once)
Principe de fonctionnement
YOLO (You Only Look Once) révolutionne la détection d'objets en la transformant en un problème de régression unique. Contrairement aux méthodes traditionnelles à deux étapes qui génèrent d'abord des propositions de régions puis les classifient, YOLO traite l'image en une seule passe à travers le réseau de neurones. L'image d'entrée est divisée en une grille, et chaque cellule prédit directement les boîtes englobantes et les probabilités de classe des objets présents. Cette approche unifiée permet une inférence extrêmement rapide, rendant YOLO particulièrement adapté aux applications temps réel.​

Évolution de YOLOv1 à YOLOv11
L'évolution de YOLO sur près d'une décennie illustre les progrès constants en détection d'objets:​

YOLOv1 (2016) a introduit le concept de détection unifiée en une seule étape, utilisant un backbone inspiré de GoogLeNet. Bien que révolutionnaire, cette version initiale souffrait de limitations sur les petits objets et les objets rapprochés.​

YOLOv2 (2017), aussi appelé YOLO9000, a apporté des innovations majeures: normalisation par batch pour un entraînement plus stable, introduction des anchor boxes inspirées de Faster R-CNN, et entraînement multi-échelle permettant de gérer des objets de tailles variées. Cette version pouvait détecter jusqu'à 9000 classes d'objets.​

YOLOv3 (2018) a introduit Darknet-53, un backbone résiduel profond, et des prédictions multi-échelles permettant de détecter objets petits, moyens et grands avec une précision améliorée. Cette version a établi YOLO comme référence pour la surveillance en temps réel.​

YOLOv4 (2020) a intégré des techniques d'augmentation de données avancées (Mosaic, CutMix), CSPNet (Cross-Stage Partial Network) pour une meilleure efficacité, et SAT (Self-Adversarial Training). Elle a atteint 43.5% mAP sur COCO tout en maintenant plus de 100 FPS sur GPU.​

YOLOv5 (2020) a marqué la transition vers PyTorch et a introduit l'optimisation automatique des hyperparamètres, la sélection automatique d'ancres, et des fonctionnalités d'exportation facilitées. Cette version a démocratisé l'utilisation de YOLO grâce à sa facilité d'implémentation.​

YOLOv6 (2022) a introduit des têtes de détection découplées et le RepOptimizer pour optimiser l'entraînement. Cette version, open-source par Meituan, alimente notamment les robots de livraison autonomes.​

YOLOv7 (2022) a apporté E-ELAN (Extended Efficient Layer Aggregation Network) et des "bag-of-freebies" entraînables, ainsi que l'estimation de pose sur le dataset COCO Keypoints.​

YOLOv8 (2023), développée par Ultralytics, a introduit une tête sans ancres (anchor-free), unifié plusieurs tâches (détection, segmentation, suivi, classification) dans une seule architecture, et utilisé Distribution Focal Loss (DFL).​

YOLOv9 (2024) a intégré GELAN (Generalized Efficient Layer Aggregation Network), DFL v2, et Programmable Gradient Information (PGI) pour améliorer l'apprentissage.​

YOLOv10 (2024), développée à l'Université Tsinghua, a éliminé le besoin de Non-Maximum Suppression (NMS) grâce à un entraînement avec assignations doubles cohérentes, réduisant significativement la latence d'inférence. YOLOv10-S est 1.8× plus rapide que RT-DETR-R18 avec une précision similaire.​

YOLOv11 (2024), dernière version d'Ultralytics, améliore l'extraction de caractéristiques avec des composants comme le bloc C3k2 et SPPF (Spatial Pyramid Pooling - Fast). YOLOv11m atteint un mAP supérieur sur COCO avec moins de paramètres que YOLOv8m. Elle supporte une gamme étendue de tâches: détection d'objets, segmentation d'instances, classification, estimation de pose, et détection d'objets orientés.​

Performance actuelle
Les performances de YOLOv11 en 2025 sont remarquables:​

YOLOv11n (nano): 39.5% mAP, 1.5 ms sur GPU T4, 2.6M paramètres

YOLOv11s (small): 47.0% mAP, 2.5 ms sur GPU T4, 9.4M paramètres

YOLOv11m (medium): 51.5% mAP, 4.7 ms sur GPU T4, 20.1M paramètres

YOLOv11l (large): 53.4% mAP, 6.2 ms sur GPU T4, 25.3M paramètres

YOLOv11x (extra-large): 54.7% mAP, 11.3 ms sur GPU T4, 56.9M paramètres

Ces modèles peuvent traiter entre 88 et 200+ images par seconde selon la taille du modèle, dépassant largement le seuil de 30 FPS nécessaire pour la vidéo temps réel.​

Dans des tests comparatifs sur vidéos de trafic, YOLOv11 a démontré sa supériorité en détectant des véhicules larges (camions) manqués par YOLOv10, tout en maintenant une vitesse de traitement entre 10 et 20 millisecondes par frame. La performance sur objets distants ou de petite taille reste un défi, bien que YOLOv11 montre des améliorations notables par rapport aux versions précédentes.​

Sur des datasets spécialisés, les résultats confirment la robustesse de YOLO11: sur la détection de panneaux de signalisation, YOLO11m atteint 79.5% mAP50-95 avec une inférence de 2.4 ms et seulement 38.8 MB de taille de modèle. Les familles YOLO11 et YOLOv10 surpassent significativement les générations précédentes en équilibrant précision et vitesse.​

Avantages de YOLO
Vitesse exceptionnelle: L'architecture en une seule passe permet un traitement ultra-rapide, essentiel pour les applications temps réel comme la surveillance, les véhicules autonomes, et l'analyse vidéo en direct.​

Précision élevée: Les dernières versions atteignent des mAP compétitifs avec des méthodes plus complexes, tout en maintenant une vitesse supérieure.​

Moins de faux positifs: En analysant l'image globalement plutôt que région par région, YOLO comprend mieux le contexte et génère moins de fausses détections.​

Polyvalence: Support natif de multiples tâches (détection, segmentation, classification, pose) dans une architecture unifiée.​

Facilité de déploiement: Optimisations pour différentes plateformes (CPU, GPU, edge devices), exportation vers ONNX, TensorRT, CoreML.​

Limites
Performance réduite sur petits objets: Malgré les améliorations, la détection d'objets très petits ou fortement occultés reste un défi, particulièrement dans les versions légères (nano, small).​

Ressources GPU importantes: Les versions les plus précises (large, extra-large) nécessitent des GPU modernes (NVIDIA T4, A100, V100) pour maintenir les performances temps réel.​

Sensibilité aux conditions extrêmes: Variations importantes d'éclairage, flou de mouvement, ou occlusions sévères peuvent dégrader les performances.​

Trade-off précision/vitesse: Les versions rapides sacrifient de la précision, tandis que les versions précises réduisent la vitesse.​

Applications typiques
Surveillance temps réel: Détection d'intrusions, comptage de personnes, identification de comportements anormaux dans les systèmes de sécurité.​

Véhicules autonomes: Détection de piétons, panneaux de signalisation, véhicules, obstacles pour la navigation sécurisée.​

Retail analytics: Analyse du comportement client, détection de vols, gestion d'inventaire automatique.​

Systèmes industriels: Contrôle qualité automatisé, détection de défauts, suivi d'objets sur chaînes de production.​

Type d'apprentissage
YOLO utilise un apprentissage supervisé nécessitant des données étiquetées avec bounding boxes et labels de classes. L'entraînement repose sur des fonctions de perte combinant erreur de localisation (régression des coordonnées), erreur de classification (probabilités de classes), et erreur de confiance (probabilité de présence d'objet).​

Les versions récentes intègrent des stratégies d'entraînement sophistiquées: augmentation de données (Mosaic, CutMix, MixUp), entraînement multi-échelle, sélection automatique d'hyperparamètres, et assignation dynamique d'étiquettes. Ces techniques améliorent la robustesse et la généralisation sans nécessiter de données étiquetées supplémentaires.​

2.2 Architectures Transformer pour vidéo
Contexte: De ViT à la vidéo
Les Transformers, initialement développés pour le traitement du langage naturel, ont été adaptés à la vision par ordinateur avec Vision Transformer (ViT). ViT divise les images en patches (segments de 16×16 pixels typiquement) traités comme tokens pour les Transformers. Le mécanisme d'auto-attention permet de capturer les dépendances à longue portée dans l'image.​​

L'extension aux vidéos ajoute une dimension temporelle cruciale: au-delà des informations spatiales dans chaque frame, les Transformers vidéo doivent modéliser l'évolution temporelle des objets et les relations entre frames successives. Cette double modélisation spatio-temporelle est essentielle pour comprendre les mouvements, actions et dynamiques dans les séquences vidéo.​

TGBFormer: Fusion Transformer-GraphFormer
TGBFormer (Transformer-GraphFormer Blender Network) représente l'état de l'art en 2025 pour la détection d'objets vidéo avec 86.5% mAP à 41 FPS sur ImageNet VID. Cette architecture innovante combine deux paradigmes complémentaires:​

Composante Transformer: Capture les dépendances globales à long terme dans les séquences vidéo grâce au mécanisme d'auto-attention. Les Transformers excellent à modéliser les relations entre frames distantes, permettant de suivre des objets sur de longues séquences même en cas d'occlusions temporaires.​

Composante GraphFormer: Modélise les relations locales spatio-temporelles via des graphes où les nœuds représentent des patches d'image ou des caractéristiques d'objets, et les arêtes encodent les relations de proximité spatiale et de continuité temporelle. Cette représentation graphique est particulièrement efficace pour capturer les interactions locales entre objets proches.​

La fusion de ces deux approches permet à TGBFormer d'exploiter simultanément le contexte global (Transformer) et les structures locales (GraphFormer), résultant en une compréhension riche et robuste des scènes vidéo dynamiques. Cette architecture atteint un équilibre remarquable entre précision (86.5% mAP) et vitesse (41 FPS), la rendant viable pour des applications nécessitant haute précision avec contraintes temps réel modérées.​

VideoGLaMM: Alignement multimodal
VideoGLaMM introduit une approche multimodale révolutionnaire pour l'alignement au niveau pixel dans les vidéos. Cette architecture connecte un modèle de langage avec des encodeurs visuels duaux et un décodeur spatio-temporel spécialisé.​

L'innovation majeure réside dans la capacité à aligner précisément les représentations linguistiques (descriptions textuelles d'objets) avec les localisations pixel-level dans les vidéos. Cet alignement multimodal permet non seulement de détecter des objets, mais aussi de générer des descriptions détaillées, répondre à des requêtes en langage naturel sur le contenu vidéo, et effectuer des tâches de grounding visuel (localisation d'objets décrits textuellement).​

Les encodeurs visuels duaux traitent respectivement les informations spatiales (apparence des objets dans chaque frame) et temporelles (évolution et mouvement des objets). Le décodeur spatio-temporel fusionne ces deux flux d'information pour produire des prédictions cohérentes à travers le temps, maintenant l'identité des objets malgré changements d'apparence ou occlusions partielles.​

VideoGLaMM ouvre la voie à des applications avancées comme la recherche vidéo par requête textuelle, l'annotation automatique de contenu vidéo, et l'assistance intelligente pour l'édition vidéo.​

Vision Transformers (ViViT) pour vidéo
ViViT (Video Vision Transformer) adapte systématiquement les Transformers à la compréhension vidéo en modélisant explicitement les dimensions spatiale et temporelle.​

Tokenization vidéo: Chaque frame est divisée en patches spatiaux, et l'ensemble des patches sur tous les frames forme les tokens d'entrée du Transformer. Pour une vidéo de T frames avec des patches de taille p×p, le nombre total de tokens est proportionnel à T × (H/p) × (W/p), où H et W sont la hauteur et largeur des frames.​

Quatre variantes architecturales:​

Spatio-Temporal Attention (Joint Attention): Applique l'auto-attention simultanément sur tous les tokens spatiaux et temporels. Cette approche capture les interactions complètes mais est computationnellement coûteuse (complexité quadratique en nombre de tokens).

Factorized Encoder: Décompose le traitement en deux Transformers séquentiels - un Transformer spatial traite indépendamment chaque frame, puis un Transformer temporal agrège l'information temporelle. Plus efficace que l'attention jointe avec performance légèrement réduite.

Variante avec réduction temporelle: Réduit la dimension temporelle avant le traitement complet pour diminuer la complexité computationnelle.

Variante avec pooling central: Utilise un token central pour agréger l'information temporelle.

Adaptive Memory Mechanism (AMViT): Une innovation récente introduit un mécanisme de mémoire adaptative pour les vidéos longues. Au lieu de maintenir un cache Key-Value fixe, AMViT utilise une Memory Bank qui retient les embeddings les plus importants basés sur les scores d'attention avec le token CLS. Cette approche dynamique ajuste le champ réceptif temporel en fonction du contenu vidéo, améliorant l'efficacité et les performances sur des tâches de reconnaissance d'actions, anticipation, et détection.​

Memory Consolidation: Pour les vidéos à contexte très long, des techniques de consolidation de mémoire inspirées des neurosciences permettent aux Transformers de maintenir des représentations compactes d'événements passés tout en restant réactifs aux nouveaux contenus.​

Avantages des Transformers vidéo
Modélisation temporelle supérieure: Les Transformers capturent naturellement les dépendances à long terme grâce à l'auto-attention, permettant de suivre des objets sur de longues séquences et de comprendre des actions complexes s'étendant sur plusieurs secondes.​

Performance sur objets en mouvement rapide: La capacité à agréger l'information sur multiple frames aide à gérer le flou de mouvement et à maintenir la détection d'objets se déplaçant rapidement.​

Flexibilité architecturale: Les Transformers s'adaptent facilement à différentes modalités (texte, audio) pour des applications multimodales comme VideoGLaMM.​

Compréhension contextuelle riche: L'attention globale permet de comprendre les relations entre objets distants et le contexte général de la scène.​

Limites
Complexité computationnelle élevée: La complexité quadratique de l'auto-attention par rapport au nombre de tokens rend les Transformers très gourmands en calcul, particulièrement pour les vidéos haute résolution ou longues. TGBFormer, malgré ses 41 FPS, nécessite des GPU haute performance pour maintenir cette vitesse.​

Besoins importants en données d'entraînement: Les Transformers ont typiquement des millions de paramètres et nécessitent de vastes datasets pour un entraînement efficace, risquant le surapprentissage sur datasets limités.​

Latence d'inférence: Le traitement séquentiel de nombreux tokens introduit une latence qui peut être prohibitive pour certaines applications temps réel strict.​

Consommation mémoire: Le cache Key-Value pour l'attention multi-têtes consomme une mémoire GPU substantielle, limitant la longueur des vidéos traitables.​

Type d'apprentissage
Les Transformers vidéo utilisent principalement l'apprentissage supervisé avec annotations denses (bounding boxes, masques de segmentation, labels d'actions). L'entraînement en deux étapes est courant: pré-entraînement sur de vastes datasets d'images (ImageNet) ou vidéos génériques, puis fine-tuning sur la tâche cible.​

Une tendance forte en 2025 est l'émergence d'approches auto-supervisées: pré-entraînement sur vidéos non étiquetées en exploitant des tâches proxy comme la prédiction de frames futurs, le réordonnancement temporel, ou l'apprentissage contrastif entre différentes augmentations d'une même vidéo. Ces méthodes réduisent la dépendance aux annotations coûteuses tout en apprenant des représentations riches exploitant les structures temporelles naturelles des vidéos.​

2.3 DETR et variants
Architecture DETR originale
DETR (DEtection TRansformer), introduit par Facebook AI en 2020, simplifie radicalement la détection d'objets en la reformulant comme un problème de prédiction d'ensemble (set prediction). Contrairement aux détecteurs traditionnels nécessitant des composants manuels complexes (génération d'ancres, Non-Maximum Suppression), DETR adopte une approche end-to-end élégante.​

Composantes architecturales:​

Backbone CNN: Typiquement ResNet-50 ou ResNet-101, extrait des caractéristiques visuelles de l'image d'entrée. Ces features maps conservent l'information spatiale essentielle pour la localisation d'objets.​

Encodage positionnel: Puisque les Transformers n'ont pas de compréhension spatiale inhérente, DETR ajoute des encodages positionnels aux features pour informer le modèle des relations spatiales.​

Transformer Encoder: Traite les features avec encodages positionnels via l'auto-attention multi-têtes, permettant de capturer les relations globales entre différentes régions de l'image.​

Object Queries: Ensemble de vecteurs apprenables (typiquement 100) représentant des "slots" pour objets potentiels. Ces queries sont indépendantes de l'image et apprises durant l'entraînement.​

Transformer Decoder: Chaque object query "interroge" les features encodées via l'attention croisée (cross-attention) pour extraire l'information pertinente à un objet spécifique.​

Têtes de prédiction: Réseaux feed-forward prédisent pour chaque query la classe de l'objet (ou "pas d'objet") et les coordonnées de la bounding box.​

Bipartite Matching: Durant l'entraînement, un algorithme d'appariement optimal (Hungarian algorithm) associe chaque prédiction à un objet réel, éliminant le besoin de NMS post-traitement.​

DETR original souffrait d'une convergence lente (500 epochs pour 43.3% AP sur COCO), motivant de nombreuses améliorations dans les années suivantes.​

MI-DETR: Multi-time Inquiries
MI-DETR, accepté à CVPR 2025, propose une innovation architecturale majeure pour résoudre les limitations de l'architecture en cascade de DETR.​

Problématique: Les DETR traditionnels utilisent des décodeurs en cascade où les object queries se mettent à jour séquentiellement couche après couche. Cette contrainte limite l'information que chaque query peut extraire, les queries dans les couches tardives dépendant exclusivement des représentations des couches précédentes.​

Mécanisme Multi-time Inquiries (MI): MI-DETR remplace l'architecture cascade par une architecture parallèle où les object queries effectuent simultanément plusieurs interrogations des features d'image via des têtes d'interrogation (inquiry heads) indépendantes.​

Implémentation technique:​

Chaque couche décodeur MI contient M têtes d'interrogation indépendantes, chacune composée de:

Self-Attention (SA): Les queries interagissent entre elles

Cross-Attention (CA): Les queries interrogent les features d'image

Feed-Forward Network (FFN): Transformation non-linéaire

Les sorties des M têtes sont fusionnées par concaténation puis projection linéaire:

Q_i = Linear(Concat(Q_1^i, Q_2^i, ..., Q_M^i))

où Q_k^i représente la sortie de la k-ième tête d'interrogation à la i-ième couche décodeur.

Performances exceptionnelles: MI-DETR atteint 52.4% AP sur COCO en 12 epochs, surpassant DINO (+2.3 AP) et Relation-DETR (+0.7 AP) qui étaient précédemment state-of-the-art. Avec 24 epochs, MI-DETR atteint 52.1% AP. Les améliorations sont particulièrement notables sur les objets petits, fortement occultés, ou confondus avec l'arrière-plan - défis majeurs en détection naturelle.​

Interprétabilité: Des expériences de visualisation démontrent que différentes têtes d'interrogation apprennent à extraire des patterns d'information distincts et complémentaires, validant l'hypothèse de l'apprentissage multi-pattern.​

RF-DETR: Détection et segmentation temps réel
RF-DETR combine détection et segmentation d'objets en temps réel, offrant une alternative moderne à YOLO pour les applications nécessitant des informations de segmentation précises en plus des bounding boxes.​

Cette architecture hérite de l'approche end-to-end de DETR tout en optimisant pour la vitesse: elle maintient plus de 30 FPS sur GPU moderne avec des performances de détection compétitives (environ 50-52% mAP sur COCO). La capacité de segmentation simultanée (masques pixel-level) est particulièrement précieuse pour des applications comme l'édition vidéo automatique, la réalité augmentée, ou l'analyse détaillée de scènes.​

RF-DETR représente une convergence intéressante: performance temps réel proche de YOLO avec l'élégance architecturale et la capacité multi-tâches de DETR.​

Avantages de DETR et variants
Élégance architecturale: Architecture end-to-end sans composants manuels (ancres, NMS), simplifiant considérablement le pipeline de détection.​

Performance sur objets complexes/occultés: L'attention globale permet de mieux gérer les occlusions partielles et objets dans des configurations complexes. MI-DETR excelle particulièrement sur ces cas difficiles.​

Flexibilité: Facilité d'extension à des tâches connexes (segmentation, estimation de pose, tracking) grâce à l'architecture modulaire.​

Pas de post-traitement NMS: Élimine le besoin d'ajuster des seuils de suppression, réduisant les hyperparamètres et la latence.​

Limites
Convergence lente: DETR original nécessite 500 epochs, bien que les variants récents (MI-DETR, DINO) aient réduit ce nombre à 12-24 epochs. L'entraînement reste néanmoins plus long que YOLO.​

Coût d'inférence élevé: Le traitement Transformer de multiples object queries et l'attention croisée génèrent une latence substantielle comparée aux CNNs purs. RF-DETR atténue ce problème mais reste en deçà de YOLO en vitesse pure.​

Complexité d'implémentation: L'appariement bipartite, les object queries, et les multiples mécanismes d'attention rendent DETR plus complexe à implémenter et optimiser que les détecteurs conventionnels.​

Sensibilité aux hyperparamètres: Nombre d'object queries, nombre de couches décodeur, dimensionnalité des embeddings - ces choix architecturaux impactent significativement la performance et nécessitent un tuning soigné.​

Type d'apprentissage
DETR et ses variants utilisent l'apprentissage supervisé avec annotations complètes (bounding boxes et labels). La fonction de perte combine:​

Perte de classification: Cross-entropy sur les prédictions de classe

Perte de localisation: L1 loss et GIoU (Generalized Intersection over Union) sur les coordonnées de boxes

Appariement optimal: Hungarian algorithm pour assigner prédictions aux ground truths

L'entraînement end-to-end optimise simultanément tous les composants du réseau (backbone, encoder, decoder, têtes de prédiction) via backpropagation standard.​

Les variants récents explorent l'intégration de techniques semi-supervisées: utilisation de pseudo-labels sur données non étiquetées, apprentissage contrastif pour améliorer les représentations des object queries, ou distillation de connaissances depuis des modèles enseignants plus larges.​

2.4 Méthodes d'agrégation temporelle
ClipVID: Agrégation cohérente d'identité
ClipVID introduit l'agrégation cohérente d'identité pour maintenir la consistance des objets à travers les frames vidéo. Cette approche atteint 84.7% mAP à 39.3 FPS sur ImageNet VID, démontrant un excellent équilibre entre précision et vitesse.​

Principe clé: Les objets dans une vidéo maintiennent généralement une identité visuelle cohérente malgré les changements de pose, d'échelle ou d'éclairage. ClipVID exploite cette propriété en associant et propageant les identités d'objets détectés entre frames successives.​

Mécanisme d'agrégation: Pour chaque objet détecté, ClipVID maintient un vecteur de features agrégées sur plusieurs frames passées. Lors du traitement d'une nouvelle frame, le système:

Détecte les objets candidats dans la frame courante

Associe chaque détection à une identité existante via similarité de features

Agrège les features de la détection courante avec l'historique de cette identité

Utilise les features agrégées enrichies pour raffiner la prédiction finale

Cette propagation temporelle d'information améliore considérablement la robustesse aux occlusions temporaires, variations d'apparence, et détections manquées ponctuelles.​

YOLOV avec agrégation de features
L'intégration d'agrégation de features à YOLO produit des résultats remarquables: 92.9% AP50 à plus de 30 FPS sur des benchmarks vidéo. Cette performance représente le meilleur compromis actuel entre précision maximale et vitesse temps réel viable.​

Approche: Combine la rapidité inhérente de YOLO avec une sélection et agrégation intelligentes de features sur plusieurs frames:​

Sélection de features: Identifie les features les plus informatives dans chaque frame via mécanismes d'attention ou scores de saillance, évitant d'agréger du bruit ou de l'information redondante.​

Agrégation multi-échelle: Fusionne features de différentes résolutions spatiales et différents timesteps temporels, capturant simultanément détails fins et contexte global.​

Optimisation mémoire: Utilise des stratégies de cache efficaces pour stocker uniquement les features essentielles des frames récentes, permettant l'agrégation sans explosion de la consommation mémoire.​

Les applications typiques incluent l'analyse de vidéos haute résolution où la précision est critique (sécurité, inspection qualité industrielle) mais où un traitement légèrement différé (30 FPS au lieu de 100+ FPS) est acceptable.​

Exploitation de l'information inter-frames
L'exploitation cohérente de l'information temporelle apporte plusieurs bénéfices fondamentaux:

Réduction du bruit: Les détections isolées erronées (faux positifs ponctuels) sont filtrées naturellement car elles ne trouvent pas de correspondance dans les frames adjacentes.

Complétion d'occlusions: Si un objet est temporairement occluté, son identité et ses features agrégées des frames précédentes permettent de maintenir la détection ou de la restaurer rapidement quand l'objet réapparaît.

Amélioration de précision: L'agrégation de multiples observations d'un même objet sous différents angles ou conditions améliore l'estimation de sa bounding box et de sa classe.

Suivi implicite: L'association d'identités entre frames fournit gratuitement un tracking basique sans algorithme de suivi séparé.

Avantages
Performance exceptionnelle sur mouvement rapide: Les méthodes d'agrégation temporelle excellent lorsque les objets se déplacent rapidement ou subissent des changements brusques, car elles intègrent l'information de multiples frames pour stabiliser les prédictions.​

Robustesse accrue: Moins sensibles aux conditions ponctuelles dégradées (flou momentané, éclairage variable, occlusion partielle) grâce à la mémoire temporelle.​

Qualité de tracking améliorée: La cohérence d'identité facilite grandement le suivi multi-objets en aval.​

Limites
Coût mémoire: Maintenir des features agrégées pour de nombreux objets sur plusieurs frames consomme une mémoire GPU significative, limitant le nombre d'objets suivis simultanément ou la longueur de l'historique.​

Sensibilité aux variations d'apparence: Des changements brusques d'apparence (changement d'éclairage dramatique, rotation complète) peuvent rompre l'association d'identité, causant des pertes de tracking.​

Latence légère: L'agrégation sur plusieurs frames introduit un délai minimal (typiquement 2-5 frames), acceptable pour la plupart des applications mais potentiellement problématique pour des systèmes à latence ultra-critique.​

Complexité d'implémentation: L'association d'identités et la gestion du cache de features requièrent une logique supplémentaire par rapport à la détection frame-par-frame isolée.​

2.5 Approches émergentes
Spiking Neural Networks (SNNs)
Multi-scale Spiking Detector (MSD) représente une approche bio-inspirée révolutionnaire pour la détection d'objets économe en énergie. Cette architecture atteint 62.0% mAP sur COCO avec seulement 7.8M paramètres et 6.43 mJ de consommation énergétique.​

Principe des SNNs: Inspirés du fonctionnement des neurones biologiques, les SNNs communiquent via des impulsions binaires (spikes) plutôt que des valeurs continues. Cette approche événementielle présente des avantages intrinsèques d'efficacité énergétique, particulièrement sur des puces neuromorphiques spécialisées.​

Architecture MSD:​

Optic Nerve Nucleus Block (ONNB): Composant central utilisant des neurones convolutifs à impulsions pour l'extraction profonde de features, améliorant significativement les capacités de représentation des SNNs.​

Fusion multi-échelle: Intègre des features de différentes profondeurs du réseau via mécanismes à impulsions, émulant la réponse biologique à des stimuli d'objets de tailles variées.​

Détecteur à impulsions: Prédit les bounding boxes et classes en utilisant uniquement des opérations à impulsions, maintenant l'efficacité énergétique jusqu'à la sortie finale.​

Spiking-YOLO: Une approche antérieure convertissait YOLO en SNN, atteignant jusqu'à 98% de la performance de Tiny YOLO sur PASCAL VOC et MS COCO, tout en consommant environ 280 fois moins d'énergie sur puce neuromorphique. La convergence était également 2.3 à 4 fois plus rapide que les méthodes de conversion SNN précédentes.​

Entraînement direct vs conversion: Les travaux récents privilégient l'entraînement direct des SNNs plutôt que la conversion ANN-to-SNN, permettant de mieux exploiter les dynamiques temporelles uniques des neurones à impulsions. L'entraînement avec valeurs entières pendant l'entraînement et inférence spike-driven avec timesteps virtuels étendus améliore la précision tout en maintenant l'efficacité.​

Approches faiblement supervisées
DOtA (Detection of 3D Objects from multi-Agent viewpoints): Cette méthode révolutionnaire élimine complètement le besoin d'annotations manuelles pour la détection 3D en exploitant les viewpoints multi-agents. En observant une scène depuis plusieurs positions ou agents simultanément, DOtA infère les structures 3D par cohérence géométrique entre vues, sans supervision explicite des positions d'objets.​

PointSR: Réduit drastiquement le coût d'annotation en utilisant uniquement une supervision point-level au lieu de bounding boxes complètes. Pour des images de drones où dessiner des boxes précises est laborieux, PointSR nécessite seulement qu'un annotateur clique sur le centre approximatif de chaque objet. Le modèle apprend ensuite à inférer l'étendue complète de l'objet depuis ce point unique, atteignant des performances compétitives avec supervision complète.​

DViN (Deeply-supervised Vision Network): Framework faiblement supervisé pour la compréhension d'expressions référentielles, où le modèle doit localiser un objet décrit textuellement sans annotations de bounding boxes pendant l'entraînement. DViN exploite la supervision naturelle du langage pour apprendre les correspondances vision-langage.​

Potentiel futur
Réduction des coûts d'annotation: Les approches faiblement supervisées promettent de réduire les coûts d'annotation de 50% à 90%, démocratisant le déploiement de systèmes de détection dans des domaines où obtenir des annotations exhaustives est prohibitif (imagerie médicale, inspection industrielle spécialisée).​

Déploiement embarqué: Les SNNs avec leur efficacité énergétique remarquable sont idéaux pour les systèmes embarqués: drones autonomes, robots mobiles, capteurs IoT, caméras de surveillance sur batterie. La consommation 280 fois inférieure de Spiking-YOLO permet d'envisager des opérations continues sur batteries pendant des jours ou semaines.​

Edge computing: La combinaison de SNNs et de puces neuromorphiques dédiées (Intel Loihi, IBM TrueNorth) permet le traitement intelligent à la périphérie sans cloud, réduisant latence et préoccupations de vie privée.​

Scalabilité: Les méthodes faiblement supervisées facilitent l'extension à de nouvelles catégories d'objets ou domaines avec un minimum d'effort d'annotation, accélérant le cycle développement-déploiement.​

Tableau comparatif synthétique
Ce tableau comparatif permet une vision globale des forces et faiblesses de chaque approche pour guider le choix technologique selon les contraintes spécifiques de l'application ciblée.​