Résumé exécutif
La reconnaissance d'objets en temps réel dans les flux vidéo est un enjeu majeur pour de nombreux secteurs industriels, notamment la surveillance, la conduite autonome, le retail et la sécurité publique. Ce problème consiste à détecter et localiser rapidement des objets d’intérêt dans des séquences vidéo tout en garantissant précision et faible latence.

Ce rapport analyse les principales méthodes de pointe à fin 2025 pour aborder cette problématique, en se concentrant notamment sur des architectures issues du Machine Learning telles que YOLO (You Only Look Once), les Transformers adaptés à la vidéo, et les modèles DETR et leurs variantes récentes. Ces approches offrent un compromis entre rapidité d'exécution, précision de détection et robustesse aux conditions complexes (occlusions, petits objets, variations d’éclairage).

Les conclusions clés indiquent que YOLO est particulièrement adapté aux applications temps réel grâce à sa rapidité, tandis que les Transformers et DETR permettent une meilleure compréhension temporelle et une plus grande précision, au prix d’une complexité et de besoins en ressources supérieurs. L’intégration d’agrégation temporelle et les approches faiblement supervisées émergent pour améliorer la performance et réduire la dépendance aux annotations coûteuses.

En termes de faisabilité, l’entreprise peut déployer une solution efficace en combinant un modèle performant (type YOLO ou transformer selon usage), des datasets publics adaptés (ImageNet VID, YouTube-VOS) et en s’engageant à assurer la conformité avec la réglementation RGPD au travers de mesures de protection des données robustes. Une implantation progressive, avec proof-of-concept sur des cas d’usage ciblés, suivie d’itérations d’amélioration, est recommandée pour maîtriser les coûts et les risques techniques.

1. Introduction et contexte
1.1 Mise en contexte du projet
La reconnaissance d’objets dans les vidéos est un défi crucial pour de nombreuses applications industrielles aujourd’hui. En surveillance, elle permet d’identifier en temps réel des intrusions, des comportements anormaux ou des objets abandonnés, contribuant ainsi à la prévention proactive des risques. Dans les véhicules autonomes, la détection dynamique des piétons, panneaux ou obstacles assure une navigation sécurisée et réactive. Le retail profite également de cette technologie pour analyser les comportements clients, optimiser l’agencement des rayons et limiter les pertes dues au vol.

Cette évolution est renforcée par la montée en puissance de la vision par ordinateur grâce à l’intelligence artificielle, qui transforme les systèmes traditionnels en plateformes intelligentes capables de décisions automatiques.

1.2 Objectifs du rapport
Ce rapport vise à :

Explorer exhaustivement les méthodes de Machine Learning existantes et émergentes pour la reconnaissance d’objets vidéo.

Comparer leurs performances techniques (précision, vitesse, robustesse) et leur applicabilité aux cas d’usage industriels.

Identifier les défis techniques, biais potentiels dans les données et limites des approches actuelles.

Formuler des recommandations concrètes orientant le choix des technologies et des datasets, ainsi que les modalités de conformité vie privée.

1.3 Méthodologie de recherche
La recherche bibliographique s’est appuyée sur des bases spécialisées telles que Google Scholar, IEEE Xplore et arXiv pour accéder aux publications scientifiques récentes, ainsi que sur des ressources techniques industrielles actualisées en 2025 (blogs reconnus, documentations GitHub, rapports d’experts). Les méthodes ont été sélectionnées en fonction de leur popularité, leur performance démontrée sur des benchmarks standards (ImageNet VID, COCO), et leur pertinence pour les besoins temps réel ou haute précision.

L’approche adoptée est comparative, analysant tant les aspects quantitatifs (métriques, complexité) que qualitatifs (robustesse, biais, besoins en données), pour fournir une synthèse critique permettant une prise de décision éclairée par l’entreprise.
