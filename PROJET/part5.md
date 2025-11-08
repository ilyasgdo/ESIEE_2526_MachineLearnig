5. Types d'apprentissage
Le choix du paradigme d'apprentissage conditionne fortement les coûts de développement, les performances atteignables, et la scalabilité des systèmes de détection d'objets vidéo. Cette section examine les trois catégories principales d'apprentissage et leurs implications pratiques pour le déploiement industriel.

5.1 Apprentissage supervisé
Principe
L'apprentissage supervisé pour la détection d'objets vidéo repose sur des données étiquetées exhaustivement avec bounding boxes et labels de classe pour chaque objet dans chaque frame annotée. Le modèle apprend une fonction de correspondance entre les pixels d'entrée et les annotations de sortie par optimisation d'une fonction de perte combinant erreur de localisation spatiale et erreur de classification sémantique.​

Pour les vidéos, deux stratégies d'annotation prévalent:

Annotation dense: Chaque frame est annotée indépendamment, maximisant la supervision mais générant des coûts prohibitifs. Une vidéo de 1 minute à 30 FPS contient 1800 frames - annoter exhaustivement est irréaliste.​

Annotation skip-frame: Seules des frames échantillonnées à intervalles réguliers sont annotées (typiquement 1 FPS pour vidéos 30 FPS), réduisant les coûts de 97% tout en exploitant la forte corrélation temporelle. Les frames intermédiaires peuvent être interpolées ou apprises par propagation temporelle.​

Méthodes concernées
Pratiquement toutes les architectures state-of-the-art utilisent l'apprentissage supervisé comme paradigme principal:​

Famille YOLO (YOLOv1 à YOLOv11): Entraînement supervisé avec bounding boxes et labels sur COCO, ImageNet VID​

Transformers vidéo (TGBFormer, VideoGLaMM, ViViT): Supervision via annotations denses temporelles​

DETR et variants (MI-DETR, RF-DETR): Supervision avec appariement bipartite entre prédictions et ground truths​

Méthodes d'agrégation (ClipVID, YOLOV+Agrégation): Supervision frame-level avec propagation d'identités​

L'entraînement typique suit un schéma en deux étapes: pré-entraînement sur un vaste dataset générique (COCO, ImageNet), puis fine-tuning sur le dataset cible spécifique au domaine.​

Avantages
Précision élevée: L'apprentissage supervisé atteint les meilleures performances absolues sur les benchmarks standard. YOLOv11x culmine à 54.7% mAP, MI-DETR à 52.4% mAP sur COCO. Cette précision maximale est essentielle pour applications critiques (conduite autonome, médical).​

Performance prédictible: Avec données étiquetées suffisantes et qualitatives, les modèles supervisés convergent vers des performances stables et reproductibles. Les courbes d'apprentissage sont bien comprises, facilitant la planification projet.​

Transfert learning efficace: Les représentations apprises sur datasets génériques se transfèrent remarquablement bien à des domaines spécifiques avec fine-tuning sur quelques centaines d'exemples étiquetés.​

Outillage mature: Frameworks (PyTorch, TensorFlow), plateformes d'annotation (CVAT, Labelbox, V7), et pipelines d'entraînement sont extrêmement matures et documentés.​

Inconvénients
Coût d'annotation prohibitif: L'annotation manuelle de vidéos est extrêmement coûteuse en temps humain et budget.​

Estimation des coûts pour 1000 vidéos:​

Pour 1000 vidéos de 1 minute annotées à 1 FPS (stratégie skip-frame courante):

60,000 frames à annoter au total

Scénario modéré: 4 objets par frame en moyenne

Type: Bounding box + classe

Résumé des coûts:

Coût plateforme: $8,640 (frais AWS Sagemaker ou équivalent)

Temps humain: 1,500 heures (~90 minutes par vidéo)

Coût main d'œuvre @$10/heure: $15,000

COÛT TOTAL: $23,640 soit $23.64 par vidéo

Pour des applications industrielles nécessitant 10,000-100,000 vidéos, les coûts deviennent rapidement prohibitifs ($236K - $2.36M).​

La segmentation pixel-level est 3× plus coûteuse ($30K main d'œuvre pour 1000 vidéos vs $15K pour bounding boxes).​

Risque de biais d'annotations: Les annotateurs humains introduisent inévitablement des biais cognitifs, inconsistances, et erreurs. Différents annotateurs peuvent dessiner des bounding boxes significativement différentes pour un même objet, particulièrement pour objets partiellement occultés ou aux contours ambigus.​

Généralisation limitée: Les modèles supervisés excellent sur des distributions similaires aux données d'entraînement mais peuvent échouer dramatiquement sur des scénarios non vus: nouvelles poses d'objets, conditions d'éclairage extrêmes, occlusions inhabituelles. Un détecteur entraîné sur vidéos diurnes performera médiocrement la nuit sans données nocturnes étiquetées.​

Dépendance aux distributions d'entraînement: Tout changement dans le domaine cible (nouveaux types d'objets, nouvelles catégories, nouveau contexte visuel) nécessite collecte et annotation de nouvelles données, créant un cycle perpétuel coûteux.​

5.2 Apprentissage non supervisé
Principe
L'apprentissage non supervisé vise à découvrir automatiquement des structures, patterns et représentations dans des données vidéo brutes sans aucune étiquette manuelle. Pour la détection d'objets, l'approche repose sur l'exploitation de signaux naturels présents dans les vidéos: cohérence temporelle, continuité spatiale, co-occurrence d'objets.​

Applications en détection vidéo
Tracking visuel comme supervision: Les vidéos fournissent une supervision "gratuite" via le tracking naturel des objets. Deux patches d'image connectés par une trajectoire de tracking cohérente devraient avoir des représentations features similaires. Cette contrainte de cohérence temporelle peut entraîner des encodeurs visuels sans labels explicites.​

Segmentation d'objets auto-supervisée: Des méthodes comme SOLV (Self-supervised Object-Centric Learning for Videos) découvrent et segmentent automatiquement plusieurs objets dans des vidéos réelles en utilisant des slots attention spatio-temporels et reconstruction de features masquées. SOLV atteint des performances state-of-the-art sur MOVi-E et compétitives sur DAVIS 2017 sans aucune annotation manuelle.​

Apprentissage par marches aléatoires sur graphes: Une approche construit un graphe pondéré connectant des séquences vidéo selon les similarités entre objets contenus, puis échantillonne des triplets (similar, dissimilar) via random walks pour entraîner un réseau siamois. Cette méthode améliore significativement le clustering d'objets inconnus sans supervision.​

Détection égocentrique auto-supervisée: Pour vidéos first-person, des systèmes auto-supervisés exploitent les mouvements de caméra et interactions naturelles pour apprendre à détecter objets manipulés sans labels.​

Avantages
Pas d'annotations nécessaires: Élimination complète du coût d'annotation humaine, permettant d'exploiter des millions de vidéos web disponibles gratuitement (YouTube, datasets publics). Cet avantage est décisif pour domaines où obtenir annotations est impossible (espèces animales rares, environnements dangereux).​

Exploitation de vastes données web: Les méthodes non supervisées peuvent s'entraîner sur l'intégralité de YouTube (>500 millions de vidéos), capturant une diversité visuelle inaccessible aux approches supervisées limitées par les budgets d'annotation.​

Découverte de patterns cachés: L'apprentissage non supervisé peut révéler des structures visuelles, co-occurrences d'objets, ou patterns temporels que les annotateurs humains n'auraient pas explicitement labellisés.​

Robustesse aux changements de domaine: Les représentations apprises sans biais d'annotations humaines tendent à mieux généraliser à des distributions visuelles nouvelles.​

Inconvénients
Moins précis que supervisé: Les performances absolues restent systématiquement inférieures aux méthodes supervisées. SOLV atteint des résultats "compétitifs" mais non supérieurs sur DAVIS 2017. Pour applications critiques nécessitant précision maximale (conduite autonome), cette limitation est rédhibitoire.​

Complexe à entraîner: L'apprentissage non supervisé nécessite conception soigneuse de tâches proxy (prédiction frame future, reconstruction, clustering) qui corrèlent bien avec la tâche finale de détection. Trouver les bonnes fonctions de perte, architectures, et hyperparamètres est plus art que science.​

Validation difficile: Sans ground truth, évaluer la qualité des représentations apprises pendant l'entraînement est problématique. Faut-il visualiser manuellement les segmentations? Tester sur un petit ensemble étiqueté externe? L'incertitude ralentit l'itération expérimentale.​

Dépendance aux biais des données: En l'absence de supervision humaine, les modèles amplifient les biais statistiques présents dans les données (objets fréquents dominants, contextes sur-représentés). Un système entraîné sur YouTube peut sur-apprendre des patterns de vidéos "virales" non représentatifs du monde réel.​

5.3 Apprentissages hybrides
Les approches hybrides émergent comme compromis optimal entre coût d'annotation et performance, réduisant drastiquement la supervision manuelle tout en maintenant une précision compétitive avec l'apprentissage supervisé complet.​

Apprentissage faiblement supervisé
Principe: Utiliser des annotations simplifiées et moins coûteuses que les bounding boxes complètes, tout en atteignant des performances proches du supervisé complet.​

PointSR (Point-level Supervision): Au lieu de dessiner des bounding boxes précises, les annotateurs cliquent simplement sur le centre approximatif de chaque objet. Cette annotation point-level réduit le temps d'annotation de 80-90% tout en permettant au modèle d'inférer l'étendue complète de l'objet. PointSR atteint des performances remarquables sur détection d'objets dans images de drones où dessiner des boxes précises pour objets minuscules est extrêmement laborieux.​

Supervision image-level uniquement: Les méthodes WSOD (Weakly Supervised Object Detection) utilisent uniquement des labels de présence/absence de classes sans localisation. Par exemple, une image étiquetée "contient: chat, chien" sans indiquer où. Le modèle apprend à localiser via Multiple Instance Learning.​

Récemment, W2N (Weakly-supervision to Noisy-supervision) transforme les prédictions d'un détecteur WSOD en pseudo-labels bruités, puis les raffine itérativement via localisation adaptative et apprentissage semi-supervisé. W2N surpasse tous les précédents WSOD purs sur PASCAL VOC.​

Collaboration segmentation-détection: Des architectures comme SDCN exploitent la complémentarité entre tâches de segmentation (rappel pixel-level élevé) et détection (précision élevée) en les entraînant conjointement avec supervision faible. La segmentation génère des cartes de réponse guidant la détection, tandis que les détections affinent la segmentation.​

Apprentissage auto-supervisé
Principe: Créer des tâches de pré-texte où la supervision est générée automatiquement depuis les données elles-mêmes, sans intervention humaine.​

DOtA (Detection of 3D Objects from multi-Agent viewpoints): Cette approche révolutionnaire élimine complètement l'annotation pour détection 3D en exploitant des viewpoints multi-agents. Plusieurs caméras observant une scène depuis différentes positions génèrent une cohérence géométrique multi-vues qui contraint les objets 3D détectables sans labels explicites. DOtA a démontré une détection 3D compétitive sur des scènes complexes sans aucune bounding box annotée manuellement.​

Adaptation de scène auto-supervisée: Des méthodes comme celle de Zhang et al. améliorent un détecteur pré-entraîné sur des scènes spécifiques à caméra fixe via auto-enseignement. Le détecteur génère des pseudo-labels sur frames passées, un tracker les valide, et ces pseudo-labels auto-générés ré-entraînent le détecteur en boucle. L'approche exploite l'équivariance d'arrière-plan et augmentation d'objets pour améliorer progressivement la précision sans nouvelle annotation humaine.​

Reconstruction de features masquées: SOLV entraîne un réseau à reconstruire des features de haut niveau de la frame centrale depuis un contexte temporel, après avoir masqué une portion significative des tokens. Cette tâche force le modèle à apprendre des représentations robustes capturant l'essence des objets sans labels explicites.​

Tendance 2025: Réduction dépendance annotations
L'industrie et la recherche convergent vers la minimisation de la supervision manuelle:​

Acceptation croissante des pseudo-labels: Les pseudo-labels bien filtrés atteignent maintenant des performances à 95-98% du supervisé complet, rendant le surcoût du full-supervision injustifiable pour de nombreuses applications.​

Combinaison supervision faible + auto-supervision: Les approches hybrides combinant labels image-level + pré-entraînement auto-supervisé + raffinement semi-supervisé deviennent dominantes.​

Foundation models et zero-shot: L'émergence de modèles fondations (SAM, CLIP) pré-entraînés sur milliards d'images permet détection zero-shot ou few-shot avec minimal fine-tuning.​

Avantages
Réduction drastique des coûts: Annotation point-level ou image-level réduit les coûts de 80-95% comparé aux bounding boxes complètes. Pour 1000 vidéos, cela représente une économie de $18K-$22K (de $23.6K à $1K-$5K).​

Performances compétitives: Les méthodes récentes atteignent 85-95% de la performance supervisée sur benchmarks standard. Cette légère perte est largement compensée par le gain coût/scalabilité pour la plupart des applications industrielles non-critiques.​

Scalabilité améliorée: Annoter 100,000 vidéos avec supervision complète est irréaliste ($2.36M). Avec supervision faible, le même corpus devient accessible ($200K-$500K), démocratisant les applications de détection vidéo à grande échelle.​

Limites
Encore en développement pour production: Bien que prometteurs académiquement, les systèmes faiblement/auto-supervisés nécessitent encore expertise technique significative pour déploiement production. Les frameworks et outils ne sont pas aussi matures que pour le supervisé classique.​

Performance légèrement inférieure: Le gap de 5-15% avec le supervisé complet peut être inacceptable pour applications critiques (conduite autonome, médical, sécurité). Ces domaines continueront de requérir supervision complète.​

Sensibilité aux hyperparamètres: Les méthodes hybrides introduisent des hyperparamètres supplémentaires (seuils de confiance pour pseudo-labels, pondération des pertes multiples) nécessitant tuning soigneux.​

5.4 Recommandation stratégique
Court terme (0-6 mois): Supervisé pour déploiement rapide
Pour un proof-of-concept et déploiement initial, l'apprentissage supervisé reste la voie la plus sûre:​

Avantages immédiats:

Utiliser des modèles pré-entraînés state-of-the-art (YOLOv11, MI-DETR) disponibles immédiatement

Fine-tuning sur 500-2000 vidéos étiquetées ($12K-$48K) pour adapter au domaine cible

Performance prédictible et reproductible

Outillage mature minimisant risques techniques

Stratégie d'annotation optimale:

Annotation skip-frame à 1 FPS (réduction 97% coûts vs annotation dense)

Prioriser la qualité sur la quantité: 1000 vidéos excellemment annotées > 10000 médiocrement annotées

Utiliser SAM ou pré-annotation automatique pour accélérer le travail humain (gain 30-50%)​

Moyen terme (6-18 mois): Exploration faiblement supervisé
Une fois le système initial déployé et ROI démontré, investir dans l'exploration de méthodes hybrides:​

Expérimentations recommandées:

Tester PointSR ou supervision image-level sur un subset de nouvelles données

Comparer performances vs supervisé complet sur métriques critiques

Évaluer l'économie totale: coût annotation réduit vs coût éventuel de performance inférieure

Scalabilité progressive:

Si les résultats sont satisfaisants (≥90% performance supervisée), migrer progressivement vers annotation faible pour expansion du dataset

Utiliser le supervisé complet sur catégories/scénarios critiques, faible supervision sur cas secondaires

Combiner données supervisées complètes (10-20%) + faiblement supervisées (80-90%) pour équilibre optimal​

Long terme (18+ mois): Auto-supervision et foundation models
Veille technologique active sur les avancées en auto-supervision et foundation models:​

Évaluer régulièrement les nouveaux modèles fondations (SAM, CLIP successeurs)

Tester capacités zero-shot/few-shot sur nouveaux domaines

Participer à la recherche collaborative (open-source, publications)

Arbitrage coût annotation vs performance requise
Matrice décisionnelle:

Application	Performance minimum	Type supervision recommandé	Justification
Conduite autonome	>98% précision/rappel	Supervisé complet	Criticité sécurité, aucun compromis acceptable
Surveillance sécurité	>95% rappel	Supervisé complet (critique) + Faible (secondaire)	Événements critiques nécessitent supervision maximale
Retail analytics	>85% F1-Score	Faiblement supervisé	Erreurs tolérables, scalabilité prioritaire
Médical diagnostic	>97% précision	Supervisé complet	Conséquences erreurs graves, réglementation stricte
Analyse sportive	>80% mAP	Faiblement supervisé ou Auto-supervisé	Précision modérée acceptable, volume élevé
Inspection qualité	>90% précision	Supervisé (défauts critiques) + Faible (défauts mineurs)	Hybride selon sévérité défauts
Formule ROI simplifiée:

ROI
=
(
Valeur business
×
Performance
)
−
Co
u
ˆ
t annotation
Co
u
ˆ
t annotation
ROI= 
Co 
u
ˆ
 t annotation
(Valeur business×Performance)−Co 
u
ˆ
 t annotation
 
Si réduire coût annotation de 80% (supervisé → faible) ne réduit performance que de 10%, le ROI s'améliore significativement pour applications non-critiques.​

Recommandation finale: Commencer supervisé pour validation concept, puis migrer progressivement vers hybride pour scalabilité, en maintenant supervision complète sur composantes critiques. Cette approche pragmatique équilibre rapidité de déploiement, contrôle qualité, et optimisation coûts à long terme.