8. Recommandations et faisabilité
8.1 Matrice décisionnelle par cas d’usage
Cas d’usage	Architecture recommandée	Datasets	Métriques prioritaires	Conformité RGPD
Surveillance temps réel	YOLOv11 (mode nano à média)	ImageNet VID, OD-VIRAT	Rappel élevé, mAP@0.50, FPS ≥ 25	Intérêt légitime, DPIA obligatoire
Analyse retail	TGBFormer	YouTube-VOS, COCO	Précision, mAP@0.50:0.95, F1-Score	Intérêt légitime, panneaux informatifs
Conduite autonome	YOLO + agrégation de features	Datasets spécialisés (KITTI, BDD)	mAP@0.50:0.95, FPS ≥ 30, Latence < 50 ms	Obligation légale ou mission publique
8.2 Roadmap d’implémentation
Phase 1 (0–3 mois)

Proof of Concept (POC) avec YOLOv11 sur ImageNet VID et OD-VIRAT en mode skip-frame.

Évaluation des performances baseline (mAP, rappel, FPS).

Réalisation de la première DPIA pour cadrer obligations RGPD.

Phase 2 (3–6 mois)

Collecte et annotation interne de 500–1 000 vidéos spécifiques (skip-frame 1 FPS).

Fine-tuning du modèle sur données internes.

Intégration progressive de mesures Privacy by Design (anonymisation, chiffrement).

Phase 3 (6–12 mois)

Déploiement en production sur environnement restreint (edge ou cloud).

Monitoring continu des performances (tableaux de bord mAP/FPS) et audit RGPD.

Ajustements de seuils opérationnels et optimisation des pipelines d’inférence.

Phase 4 (12+ mois)

Optimisation des modèles (pruning, quantification) pour edge deployment.

Exploration de l’apprentissage faiblement supervisé (PointSR) et auto-supervisé (DOtA).

Scalabilité du système à de nouveaux sites et nouveaux cas d’usage.

8.3 Estimation des ressources
Humaines

1–2 Data Engineers pour collecte, annotation et pipelines de données.

1 Machine Learning Engineer pour fine-tuning, optimisation et déploiement.

1 Expert conformité RGPD pour DPIA, audits et procédures.

Techniques

GPU NVIDIA A100/V100 (ou cluster cloud équivalent) pour entraînement et inférence.

Stockage 5–10 TB pour datasets vidéo et enregistrements temporaires.

Infrastructure cloud ou on-premise Kubernetes pour scalabilité.

Financières

Licences pour datasets commerciaux éventuels (surveillance privée).

Coût annotation externe: $10–$25 par heure annotateur (selon scénario).

Dépenses d’infrastructure cloud : ~$5 000–$10 000/mois selon charge.

Formation et ateliers RGPD: $20 000–$30 000 initial.

Temporelles

6–12 mois pour déploiement complet et stabilisation en production.

Itérations trimestrielles pour revue performance et conformité.

8.4 Risques et mitigation
Risque technique: Performances insuffisantes sur cas réels (petits objets, flou).
– Mitigation : validation POC sur données internes, ajustement architecture (agrégation).

Risque conformité: Violations RGPD (surveillance illégale).
– Mitigation : DPIA rigoureuse, consultation DPO, mise en place Privacy by Design.

Risque budget: Dépassement coûts annotation et infrastructure.
– Mitigation : phases incrémentales avec KPI clairs, basculement partiel vers supervision faible.

Risque adoption: Résistance utilisateurs internes (sécurité, IT).
– Mitigation : ateliers de sensibilisation, documentation des bénéfices, support technique dédié.

8.5 Conclusion sur la faisabilité
Les technologies de détection d’objets vidéo sont désormais matures et accessibles, offrant des solutions adaptées à divers cas d’usage. La combinaison d’architectures éprouvées (YOLOv11, TGBFormer) et de datasets standard garantit une intégration rapide.
La conformité RGPD est réalisable grâce à une DPIA initiale, des mesures Privacy by Design et un suivi continu.
Un déploiement phasé permet de maîtriser les coûts et les risques, tout en assurant un ROI positif dès la phase POC.
Recommandation : lancer un projet pilote supervisé, puis migrer progressivement vers des approches hybrides pour étendre le système à grande échelle