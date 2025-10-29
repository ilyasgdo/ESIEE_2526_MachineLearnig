Page de titre (1 page)
Titre du projet: "Reconnaissance d'objets en vidéos: État de l'art et solutions Machine Learning"

Nom de l'entreprise (fictive)

Membres du groupe

Date

Logo ESIEE Paris

Résumé exécutif (0.5-1 page)
Synthèse du problème adressé (détection d'objets en temps réel dans flux vidéo)

Principales méthodes analysées (YOLO, Transformers, DETR)

Conclusions clés et recommandations principales

Faisabilité technique et business pour l'entreprise

1. Introduction et contexte (1-1.5 pages)
1.1 Mise en contexte du projet

Présentation de la problématique entreprise (surveillance, conduite autonome, retail analytics, etc.)

Importance de la détection d'objets vidéo dans l'industrie actuelle

Enjeux business: sécurité, optimisation, automatisation

1.2 Objectifs du rapport

Explorer les solutions ML existantes

Comparer performances et applicabilité

Identifier défis, biais et limites

Formuler recommandations pour implémentation

1.3 Méthodologie de recherche

Sources consultées (Google Scholar, arXiv, IEEE Xplore, GitHub)

Critères de sélection des méthodes analysées

Approche comparative adoptée

2. État de l'art des méthodes (4-5 pages)
2.1 Famille YOLO (You Only Look Once) (1 page)

Principe de fonctionnement: détection en une seule passe

Évolution: YOLOv1 → YOLOv11

Performance: 45+ FPS avec GPU, mAP jusqu'à 92.9% sur datasets standard​

Avantages: vitesse exceptionnelle, précision élevée, moins de faux positifs​

Limites: performance réduite sur petits objets, ressources GPU importantes​

Applications typiques: surveillance temps réel, véhicules autonomes​

Type d'apprentissage: supervisé avec bounding boxes​

2.2 Architectures Transformer pour vidéo (1.5 pages)

TGBFormer: 86.5% mAP à 41 FPS sur ImageNet VID​

Combinaison Transformer + GraphFormer pour relations spatio-temporelles

Capture dépendances à long terme dans séquences vidéo

VideoGLaMM: approche multimodale avec alignement pixel-niveau​

Vision Transformers (ViT): adaptation pour compréhension vidéo​

Avantages: modélisation temporelle supérieure, performance sur objets en mouvement rapide​

Limites: complexité computationnelle élevée, besoins importants en données d'entraînement​

Type d'apprentissage: principalement supervisé, émergence d'approches auto-supervisées​

2.3 DETR et variants (1 page)

MI-DETR (Multi-time Inquiries DETR): requêtes multiples parallèles​

RF-DETR: détection et segmentation temps réel​

Architecture end-to-end sans post-traitement NMS

Avantages: élégance architecturale, performance sur objets complexes/occultés​

Limites: convergence lente, coût inférence élevé​

Type d'apprentissage: supervisé​

2.4 Méthodes d'agrégation temporelle (0.75 page)

ClipVID: agrégation cohérente d'identité, 84.7% mAP à 39.3 FPS​

YOLOV avec agrégation: 92.9% AP50 à 30+ FPS​

Exploitation de l'information inter-frames

Avantages: performance exceptionnelle sur mouvement rapide​

Limites: coût mémoire, sensibilité variations d'apparence​

2.5 Approches émergentes (0.75 page)

Spiking Neural Networks: Multi-scale Spiking Detector pour efficacité énergétique​

Approches faiblement supervisées: DOtA (détection 3D non supervisée), PointSR (supervision point-level)​

Potentiel futur: réduction coûts annotation, déploiement embarqué

Tableau comparatif synthétique (inclus dans cette section)

Comparaison des 5-7 méthodes principales

Colonnes: Méthode, mAP (%), FPS, Complexité, Ressources requises, Cas d'usage optimal

3. Datasets disponibles (1.5-2 pages)
3.1 ImageNet VID (0.4 page)

Description: benchmark standard pour détection vidéo​

Caractéristiques: vidéos annotées, multiples catégories d'objets

Forces: standard industrie, annotations haute qualité​

Biais identifiés: échelle limitée, surreprésentation certaines catégories​

Utilisation recommandée: benchmarking performances

3.2 YouTube-VOS (0.4 page)

Description: 4,453 clips, 94 catégories, annotations pixel-level​

Caractéristiques: 3-6 secondes par clip, objets multiples​

Forces: large échelle, diversité, 26 catégories validation pour généralisation​

Limites: vidéos courtes, complexité variable​

Utilisation recommandée: entraînement modèles génériques

3.3 COCO (Common Objects in Context) (0.3 page)

Description: 200K+ images, 80 catégories​

Usage: pré-entraînement pour modèles vidéo​

Forces: très large échelle, intégration facile​

Limites: images statiques, nécessite adaptation vidéo​

3.4 DAVIS (0.3 page)

Description: 50 séquences HD avec annotations pixel-level tous frames​

Forces: annotations précises, qualité HD, benchmark segmentation​

Limites: échelle limitée (90 clips DAVIS 2016)​

3.5 OD-VIRAT (0.3 page)

Description: 8.7M instances pour surveillance réaliste​

Caractéristiques: 10 scènes surveillance, objets petite échelle​

Forces: conditions réalistes, arrière-plans complexes​

Limites: spécialisé surveillance, généralisation limitée​

Tableau comparatif datasets (inclus)

Colonnes: Dataset, Taille, Type annotations, Domaine, Biais principaux, Recommandation usage

4. Métriques de performance (1.5-2 pages)
4.1 Métriques de précision spatiale (0.75 page)

IoU (Intersection over Union): mesure chevauchement bounding boxes​

Formule et interprétation (0-1)

Seuil standard: 0.50​

Pertinence: précision localisation

Limites: sensibilité petits objets, pas de capture erreurs classification​

Précision et Rappel​

Définitions et formules

Trade-off inhérent

Application selon contexte (surveillance vs retail)

4.2 Métriques agrégées (0.5 page)

F1-Score: moyenne harmonique précision/rappel​

AP et mAP: standard industrie​

mAP@0.50 vs mAP@0.50:0.95

Pertinence: comparaison inter-modèles

Limites: peut masquer faiblesses spécifiques, biais si classes faciles surreprésentées​

4.3 Métriques de vitesse (0.25 page)

FPS (Frames Per Second): critique temps réel​

Latence: temps capture-détection​

Importance égale à précision pour applications temps réel

Limites: variabilité selon matériel​

4.4 Choix métriques selon cas d'usage (0.25 page)

Surveillance: rappel élevé prioritaire (éviter faux négatifs)

Conduite autonome: précision + vitesse critiques

Retail analytics: équilibre précision/rappel

Tableau: Cas d'usage → Métriques prioritaires

5. Types d'apprentissage (1-1.5 pages)
5.1 Apprentissage supervisé (0.5 page)

Principe: données étiquetées avec bounding boxes et classes​

Méthodes concernées: YOLO, DETR, la plupart transformers​

Avantages: précision élevée, performance prédictible​

Inconvénients: coût annotation (dizaines milliers à millions points), risque biais annotations, généralisation limitée​

Estimation coûts: temps humain pour annotation 1000 vidéos

5.2 Apprentissage non supervisé (0.3 page)

Principe: découverte structures sans étiquettes​

Applications: tracking visuel, représentations via trajectoires​

Avantages: pas d'annotations, exploitation vastes données web​

Inconvénients: moins précis, complexe à entraîner, validation difficile​

5.3 Apprentissages hybrides (0.4 page)

Faiblement supervisé: PointSR (supervision point-level au lieu de bounding boxes)​

Auto-supervisé: DOtA (détection 3D multi-agents sans annotations)​

Tendance 2025: réduction dépendance annotations manuelles​

Avantages: réduction drastique coûts, performances compétitives​

Limites: encore en développement pour production​

5.4 Recommandation stratégique (0.2 page)

Court terme: supervisé pour déploiement rapide

Moyen terme: exploration faiblement supervisé pour scalabilité

Arbitrage coût annotation vs performance requise

6. Vie privée et sécurité (1.5-2 pages)
6.1 Cadre réglementaire RGPD (0.75 page)

Surveillance vidéo = traitement données personnelles​

6 bases légales du traitement​

Intérêt légitime vs consentement pour surveillance​

Objectifs légitimes: protection propriété, préservation preuves​

Droits des personnes: information, accès, effacement, opposition

6.2 Évaluation d'impact (DPIA) (0.3 page)

Quand requise: risque élevé, zones publiques, Article 35(3) RGPD​

Contenu DPIA: description traitement, nécessité/proportionnalité, risques libertés, mesures protection

Consultation autorité protection données si nécessaire

6.3 Mesures techniques de protection (0.5 page)

Privacy by design: intégration dès conception​

Vidéos masquées: entraînement sur identités masquées (YOLOv4/v5)​

Technologies alternatives: LiDAR pour approche privacy-first​

Chiffrement données (repos et transit)

Contrôles d'accès stricts, pseudonymisation/anonymisation​

Limitation durée conservation

6.4 Données sensibles (0.25 page)

Types révélables: santé, orientation sexuelle, opinions politiques​

Protection renforcée requise

Minimisation données: collecter uniquement nécessaire

6.5 Checklist conformité pour l'entreprise (0.2 page)

DPIA complétée avant démarrage

Documentation traitement

Mesures techniques implémentées

Formation équipes

Procédure réponse demandes exercice droits

7. Défis et limites (0.75-1 page)
7.1 Défis techniques (0.4 page)

Objets petits ou fortement occultés​

Variations d'éclairage et conditions météo

Mouvement rapide et flou de mouvement

Arrière-plans complexes et encombrement scènes​

Trade-off précision/vitesse pour temps réel​

7.2 Biais des datasets (0.35 page)

Déséquilibre classes: surreprésentation certaines catégories​

Biais géographiques et culturels

Biais temporels: datasets anciens vs évolution objets

Impact sur généralisation et équité modèles

Mitigation: augmentation données, ré-échantillonnage, datasets diversifiés

8. Recommandations et faisabilité (1-1.5 pages)
8.1 Matrice décisionnelle par cas d'usage (0.4 page)
Tableau structuré:

Cas d'usage 1 (Surveillance temps réel): YOLO11, ImageNet VID + datasets surveillance, mAP + Rappel + FPS

Cas d'usage 2 (Analyse retail): TGBFormer, YouTube-VOS, mAP + Précision

Cas d'usage 3 (Conduite autonome): YOLO + agrégation, Datasets spécialisés, mAP + FPS + Latence

Colonnes: Cas d'usage, Architecture recommandée, Datasets, Métriques prioritaires, Conformité RGPD

8.2 Roadmap implémentation (0.35 page)

Phase 1 (0-3 mois): Proof of concept avec YOLO sur dataset public, évaluation performances baseline, DPIA initiale

Phase 2 (3-6 mois): Collection/annotation données internes, fine-tuning modèle, mesures privacy by design

Phase 3 (6-12 mois): Déploiement production, monitoring performances, conformité continue

Phase 4 (12+ mois): Optimisation, exploration approches faiblement supervisées, scalabilité

8.3 Estimation ressources (0.3 page)

Humaines: 1-2 data engineers, 1 ML engineer, 1 expert conformité

Techniques: GPU NVIDIA A100/V100, stockage 5-10 TB, infrastructure cloud/on-premise

Financières: licences datasets commerciaux, annotation (si externe), infrastructure, formation

Temporelles: 6-12 mois pour déploiement production complet

8.4 Risques et mitigation (0.25 page)

Risque technique: performances insuffisantes → POC validation

Risque conformité: violations RGPD → DPIA rigoureuse + expert juridique

Risque budget: dépassements → phases incrémentales

Risque adoption: résistance utilisateurs → accompagnement changement

8.5 Conclusion sur faisabilité (0.2 page)

Technologie mature et accessible

Solutions adaptables multiples cas d'usage

Conformité RGPD réalisable avec mesures appropriées

ROI attendu selon application

Recommandation: GO avec approche phasée et pilote

9. Conclusion (0.5 page)
Récapitulatif: panorama solutions ML pour reconnaissance objets vidéo

État de l'art 2025: YOLO pour vitesse, Transformers pour précision, hybrides émergents

Datasets riches et diversifiés disponibles

Métriques standards permettant comparaison rigoureuse

Impératif conformité RGPD réalisable

Faisabilité confirmée pour entreprise avec ressources adéquates

Perspectives: évolution vers faiblement supervisé, edge computing, temps réel amélioré

Bibliographie (0.5-1 page)
Articles scientifiques (arXiv, IEEE, CVPR)

Documentation technique (Ultralytics, Roboflow, V7 Labs)

Ressources RGPD (EDPB, CNIL)

Datasets officiels

Blogs techniques reconnus

Format: IEEE ou APA selon préférence ESIEE

Annexes (optionnel, hors comptage pages)
Annexe A: Détails techniques architectures (diagrammes)

Annexe B: Exemples résultats visuels détections

Annexe C: Code snippets configuration YOLO/DETR

Annexe D: Template DPIA pour surveillance vidéo

Annexe E: Glossaire termes techniques

Répartition suggérée des pages
Version courte (7 pages):

Titre + Résumé: 1 page

Introduction: 1 page

État de l'art: 2.5 pages

Datasets + Métriques: 1.5 pages

Type apprentissage + Privacy: 1.5 pages

Recommandations + Conclusion: 1 page

Version complète (15 pages):

Titre + Résumé: 1.5 pages

Introduction: 1.5 pages

État de l'art: 5 pages

Datasets: 2 pages

Métriques: 2 pages

Type apprentissage: 1.5 pages

Privacy: 2 pages

Défis: 1 page

Recommandations: 1.5 pages

Conclusion + Biblio: 1 page

Cette structure couvre tous les éléments requis par le cahier des charges tout en permettant flexibilité selon contrainte pages.