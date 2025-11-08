7. Défis et limites
7.1 Défis techniques
La reconnaissance d’objets en vidéo repose sur des modèles complexes confrontés à des conditions de prise de vue et de scène variées. Plusieurs défis techniques majeurs se dégagent :

– Objets petits ou fortement occultés
Les objets de très petite taille (moins de 32×32 pixels) ou partiellement cachés derrière d’autres éléments posent un problème de résolution et de visibilité. Les petits objets génèrent peu de pixels utiles pour l’extraction de features discriminantes, réduisant la fiabilité de la détection, tandis que l’occultation partielle rend difficile la distinction de l’objet de l’arrière-plan.​

– Variations d’éclairage et conditions météo
Les changements brusques d’éclairage (passage du soleil à l’ombre, contrejour) et les conditions météorologiques extrêmes (pluie, brouillard, neige) altèrent la qualité d’image et dégradent les performances des modèles formés sur des images claires et stables. Ces variations requièrent des stratégies d’augmentation de données sophistiquées et des réglages dynamiques de prétraitement (normalisation adaptative).​

– Mouvement rapide et flou de mouvement
Les objets se déplaçant rapidement ou la caméra elle-même en mouvement génèrent du flou cinétique, diluant les contours et rendant la localisation approximative. Les architectures à une seule passe (YOLO) sont particulièrement sensibles au flou, tandis que les transformers bénéficient de l’agrégation temporelle mais souffrent d’une latence accrue pour traiter la séquence entière.​

– Arrière-plans complexes et scenes encombrées
Dans des environnements urbains ou industriels très chargés, les objets cibles peuvent se confondre avec des éléments de décor similaires (panneaux, machines, mobilier). Les modèles doivent alors apprendre à distinguer les objets pertinents malgré un grand nombre de distracteurs et de textures variées, ce qui nécessite des capacités de contextualisation globale avancées.​

– Trade-off précision vs vitesse pour temps réel
Les applications critiques de surveillance et de conduite autonome requièrent à la fois une haute précision et un faible temps de latence. Les modèles CNN comme YOLO offrent une vitesse élevée (>88 FPS pour YOLOv11) mais peuvent sacrifier de la précision sur objets petits ou scènes complexes, tandis que les transformers vidéo (TGBFormer, ViViT) améliorent la précision multicadre au prix d’un throughput réduit (25–40 FPS) et d’une forte consommation mémoire. Trouver l’équilibre adéquat reste un défi permanent.​

7.2 Biais des datasets
Les datasets publics présentent divers biais pouvant limiter la généralisabilité et l’équité des modèles :

– Déséquilibre de classes
Un nombre disproportionné d’images pour quelques catégories (personne, véhicule, chien) entraîne des modèles surspécialisés sur ces classes, au détriment d’objets moins fréquents. Par exemple, ImageNet VID et COCO surreprésentent certaines races de chiens et types de véhicules, biaisant les performances selon la classe.​

– Biais géographiques et culturels
La majorité des vidéos provient de pays industrialisés (États-Unis, Europe, Asie de l’Est), exposant peu les modèles à des architectures, vêtements, véhicules ou scènes propres à d’autres régions. Les systèmes entraînés sur ces données peuvent mal détecter des objets ou comportements spécifiques à des cultures et environnements différents.

– Biais temporels
Beaucoup de datasets datent de plus de cinq ans. Les objets et scènes évoluent rapidement (design de véhicules, styles de vêtements, nouveaux dispositifs urbains). Les modèles risquent de manquer de sensibilité aux objets récents ou aux évolutions de l’infrastructure urbaine, affectant leur pertinence en production.

– Impact sur généralisation et équité
Ces biais mènent à une généralisation limitée et à des inégalités de performance selon les contextes et les populations filmées. Un détecteur peut fonctionner parfaitement sur des scènes diurnes occidentales mais échouer sur des environnements nocturnes ou ruraux, créant des zones de non-couverture ou d’erreur systématique.

– Mitigation des biais
- Augmentation de données : Simuler conditions d’éclairage, flou, perspective et objets rares pour enrichir le spectre d’exemples.
- Ré-échantillonnage : Équilibrer les classes en sur-échantillonnant les catégories sous-représentées ou en sous-échantillonnant les classes dominantes.
- Datasets diversifiés : Combiner plusieurs sources (ImageNet VID, YouTube-VOS, OD-VIRAT, datasets locaux) couvrant variétés géographiques, culturelles et temporelles.
- Validation sur sets out-of-distribution : Tester la robustesse sur des vidéos non issues du même domaine d’entraînement pour mesurer la généralisation et détecter les zones de faiblesse.

La prise en compte proactive de ces biais est essentielle pour développer des solutions fiables, équitables et robustes dans des contextes réels variés.