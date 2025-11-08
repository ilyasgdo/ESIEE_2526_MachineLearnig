4. Métriques de performance
L'évaluation rigoureuse des modèles de détection d'objets vidéo nécessite un ensemble de métriques complémentaires capturant différentes dimensions de la performance: précision de localisation spatiale, exactitude de classification, et vitesse d'exécution. Cette section détaille les métriques standard de l'industrie et leur application selon les contextes.

4.1 Métriques de précision spatiale
IoU (Intersection over Union)
Définition: L'Intersection over Union, également appelé indice de Jaccard, quantifie le degré de chevauchement entre une bounding box prédite et la vérité terrain (ground truth). Cette métrique fondamentale évalue la précision de localisation des objets détectés.​

Formule mathématique:​

IoU
=
Aire d’Intersection
Aire d’Union
=
Box
pr
e
ˊ
dite
∩
Box
ground truth
Box
pr
e
ˊ
dite
∪
Box
ground truth
IoU= 
Aire d’Union
Aire d’Intersection
 = 
Box 
pr 
e
ˊ
 dite
 ∪Box 
ground truth
 
Box 
pr 
e
ˊ
 dite
 ∩Box 
ground truth
 
 
Plus concrètement, pour deux bounding boxes:

IoU
=
Aire
(
Box
pred
∩
Box
gt
)
Aire
(
Box
pred
)
+
Aire
(
Box
gt
)
−
Aire
(
Box
pred
∩
Box
gt
)
IoU= 
Aire(Box 
pred
 )+Aire(Box 
gt
 )−Aire(Box 
pred
 ∩Box 
gt
 )
Aire(Box 
pred
 ∩Box 
gt
 )
 
Le dénominateur soustrait l'intersection une fois car elle est comptée dans les deux aires individuelles.​

Pour la classification binaire (détection présence/absence), IoU s'exprime via la matrice de confusion:​

IoU
=
TP
TP
+
FN
+
FP
IoU= 
TP+FN+FP
TP
 
où TP = Vrais Positifs, FN = Faux Négatifs, FP = Faux Positifs.

Interprétation (0-1):​

IoU = 0: Aucun chevauchement entre prédiction et ground truth, pire cas possible

0 < IoU < 0.5: Chevauchement faible, localisation imprécise

IoU ≥ 0.5: Chevauchement significatif, généralement considéré comme détection valide

IoU ≥ 0.75: Chevauchement élevé, localisation précise

IoU = 1: Correspondance parfaite, prédiction exacte

Seuil standard 0.50: Par convention, une détection est considérée comme Vrai Positif si IoU ≥ 0.50 et Faux Positif si IoU < 0.50. Ce seuil représente un équilibre entre tolérance aux petites erreurs de localisation et exigence de précision raisonnable.​

Pertinence: IoU est la métrique fondamentale pour évaluer la précision de localisation spatiale des détecteurs. Elle pénalise équitablement deux types d'erreurs:​

Sous-détection: La prédiction ne couvre pas toute la zone de l'objet réel (numérateur faible)

Sur-détection: La prédiction déborde largement sur l'arrière-plan (dénominateur élevé)

Cette double pénalité rend IoU plus robuste qu'une simple mesure de chevauchement.​

Limites:​

Sensibilité aux petits objets: Pour des objets de très petite taille (< 32×32 pixels), un décalage de quelques pixels peut drastiquement réduire l'IoU même si la détection est visuellement correcte. Un décalage de 5 pixels sur un objet de 10×10 pixels peut faire chuter l'IoU en dessous de 0.5, classant la détection comme échec alors qu'elle reste utile.​

Absence de capture des erreurs de classification: IoU mesure uniquement la qualité géométrique de localisation, ignorant complètement si la classe prédite est correcte. Une voiture parfaitement localisée mais classée comme "camion" obtiendra IoU = 1.0 malgré l'erreur sémantique.​

Insensibilité à la forme de l'erreur: Un IoU de 0.6 peut résulter d'un léger décalage global ou d'une déformation importante - IoU ne distingue pas ces situations.​

Précision et Rappel
Définitions et formules:​

Précision (Precision): Proportion de détections correctes parmi toutes les détections effectuées par le modèle. Elle mesure la capacité à éviter les faux positifs.

Pr
e
ˊ
cision
=
TP
TP
+
FP
=
Vrais Positifs
Toutes les pr
e
ˊ
dictions positives
Pr 
e
ˊ
 cision= 
TP+FP
TP
 = 
Toutes les pr 
e
ˊ
 dictions positives
Vrais Positifs
 
Une précision élevée signifie que lorsque le modèle détecte un objet, il a probablement raison.​

Rappel (Recall): Proportion d'objets réels correctement détectés parmi tous les objets présents. Il mesure la capacité à éviter les faux négatifs.

Rappel
=
TP
TP
+
FN
=
Vrais Positifs
Tous les objets r
e
ˊ
els
Rappel= 
TP+FN
TP
 = 
Tous les objets r 
e
ˊ
 els
Vrais Positifs
 
Un rappel élevé signifie que le modèle détecte la plupart des objets présents, même s'il génère quelques fausses alarmes.​

Trade-off inhérent:​

Précision et rappel sont inversement corrélés via le seuil de confiance du modèle:

Seuil élevé (modèle conservateur): Seules les détections très confiantes sont retenues → Précision haute, Rappel bas (peu de faux positifs, mais beaucoup d'objets manqués)

Seuil bas (modèle permissif): Presque toutes les détections candidates sont acceptées → Précision basse, Rappel haut (peu d'objets manqués, mais nombreux faux positifs)

Ce trade-off fondamental nécessite de choisir un point d'opération sur la courbe précision-rappel selon les priorités de l'application.​

Application selon contexte:

Surveillance sécurité: Rappel élevé prioritaire. Manquer une intrusion réelle (faux négatif) est inacceptable, tandis que quelques fausses alarmes (faux positifs) peuvent être tolérées et vérifiées par opérateurs humains. Objectif typique: Rappel > 0.95, Précision > 0.70.​

Retail analytics: Équilibre précision/rappel. Les faux positifs (compter des clients inexistants) et faux négatifs (manquer des clients réels) biaisent tous deux les statistiques de trafic et analyses comportementales. Un F1-Score élevé (voir section 4.2) est recherché, typiquement > 0.85.​

Conduite autonome: Précision ET Rappel élevés critiques. Les faux positifs (freiner pour un piéton inexistant) créent des arrêts intempestifs perturbant le trafic, tandis que les faux négatifs (ne pas détecter un piéton réel) sont potentiellement fatals. Exigence: Précision > 0.98, Rappel > 0.98.​

4.2 Métriques agrégées
F1-Score
Le F1-Score est la moyenne harmonique de la précision et du rappel, fournissant une métrique unique équilibrant ces deux aspects:​

F1-Score
=
2
×
Pr
e
ˊ
cision
×
Rappel
Pr
e
ˊ
cision
+
Rappel
=
2
×
TP
2
×
TP
+
FP
+
FN
F1-Score=2× 
Pr 
e
ˊ
 cision+Rappel
Pr 
e
ˊ
 cision×Rappel
 = 
2×TP+FP+FN
2×TP
 
Le F1-Score varie de 0 (pire) à 1 (parfait).​

Pourquoi moyenne harmonique? La moyenne arithmétique simple favoriserait les modèles déséquilibrés (ex: Précision = 1.0, Rappel = 0.1 donnerait moyenne = 0.55, trompeur). La moyenne harmonique pénalise sévèrement les valeurs extrêmes, forçant Précision ET Rappel à être élevés pour obtenir un bon F1-Score.​

Pertinence: Le F1-Score est particulièrement utile pour datasets déséquilibrés où une classe domine largement. Il est également précieux lorsque précision et rappel ont une importance approximativement égale, comme en retail analytics ou analyse médicale non critique.​

Average Precision (AP) et Mean Average Precision (mAP)
Average Precision (AP): L'AP résume la courbe précision-rappel en un nombre unique représentant l'aire sous la courbe. Elle capture la performance du modèle à tous les niveaux de seuil de confiance.​

Calcul de l'AP (méthode VOC interpolée):​

Générer des détections avec scores de confiance pour une classe

Trier les détections par confiance décroissante

Pour chaque seuil de confiance, calculer Précision et Rappel

Tracer la courbe Précision-Rappel

Interpoler la précision: pour chaque point de rappel 
r
r, la précision est le maximum des précisions à tous les rappels ≥ 
r
r

Calculer l'AP comme somme pondérée:

AP
=
∑
i
=
1
n
(
R
i
−
R
i
−
1
)
×
P
i
AP= 
i=1
∑
n
 (R 
i
 −R 
i−1
 )×P 
i
 
où 
R
i
R 
i
  est le rappel au point 
i
i, 
P
i
P 
i
  la précision interpolée correspondante.​

Mean Average Precision (mAP): La mAP est simplement la moyenne des AP sur toutes les classes:​

mAP
=
1
N
∑
i
=
1
N
AP
i
mAP= 
N
1
  
i=1
∑
N
 AP 
i
 
où 
N
N est le nombre de classes.​

mAP@0.50 vs mAP@0.50:0.95:​

mAP@0.50 (ou mAP@IoU=0.5): Calcule la mAP en considérant une détection comme correcte si IoU ≥ 0.50. Standard PASCAL VOC, relativement indulgent sur la précision de localisation.​

mAP@0.50:0.95 (ou mAP@[0.5:0.95]): Calcule la mAP pour des seuils IoU de 0.50, 0.55, 0.60, ..., 0.95 (10 seuils), puis moyenne ces valeurs. Standard COCO, beaucoup plus exigeant sur la qualité de localisation.​

Typiquement, mAP@0.50:0.95 est ~15-20 points inférieur à mAP@0.50 pour un même modèle. Par exemple, YOLOv11x atteint 54.7% mAP@0.50:0.95 mais dépasserait 70% mAP@0.50.​

Pertinence: La mAP est devenue le standard industrie pour comparer les détecteurs d'objets. Elle permet des comparaisons objectives et reproductibles entre différentes architectures, indépendamment des choix d'hyperparamètres de seuil. Les leaderboards académiques (COCO, ImageNet VID) utilisent exclusivement mAP comme métrique primaire.​

Limites:​

Peut masquer faiblesses spécifiques: Une mAP globale élevée peut cacher des performances médiocres sur certaines classes minoritaires. Un modèle avec AP = 0.90 sur 9 classes fréquentes et AP = 0.10 sur 1 classe rare obtiendra mAP = 0.82, semblant excellent malgré l'échec complet sur la classe rare.​

Biais si classes faciles surreprésentées: Si le dataset contient majoritairement des objets faciles à détecter (grands, bien contrastés, vues canoniques) et peu d'objets difficiles (petits, occultés, angles inhabituels), la mAP sera artificiellement gonflée. Le modèle performera bien sur le benchmark mais échouera en déploiement réel rencontrant plus de cas difficiles.​

Ne capture pas la performance temporelle: Pour les vidéos, mAP est généralement calculé frame par frame indépendamment, ignorant la consistance temporelle des détections. Un modèle avec mAP élevé mais détections flickering (apparaissant/disparaissant aléatoirement) sera problématique en pratique.​

Insensibilité aux coûts différenciés: mAP traite tous les types d'erreurs également. En réalité, certaines erreurs peuvent être plus coûteuses (ne pas détecter un piéton en conduite autonome) que d'autres (faux positif sur objet bénin).​

4.3 Métriques de vitesse
FPS (Frames Per Second)
Définition: Le FPS mesure le nombre d'images traitées par seconde par le modèle de détection. C'est la métrique primaire pour évaluer la viabilité temps réel d'un système.​

Seuils critiques:​

< 15 FPS: Trop lent pour vidéo fluide, utilisation limitée à l'analyse offline ou applications non critiques

15-25 FPS: Acceptable pour applications tolérantes (analytics retail, inspection qualité non temps réel)

25-30 FPS: Minimum pour perception humaine de fluidité, standard vidéo cinématographique

30-60 FPS: Idéal pour applications temps réel (surveillance, conduite autonome, robotique)

> 60 FPS: Excellent, permet marge de sécurité et traitement additionnel (tracking, post-traitement)

Importance égale à la précision pour applications temps réel: Dans les systèmes de surveillance, conduite autonome, ou robotique interactive, un détecteur avec 60% mAP à 40 FPS peut être plus utile qu'un détecteur avec 70% mAP à 10 FPS. La latence excessive rend les détections obsolètes avant utilisation, compromettant la réactivité du système.​

Par exemple, TGBFormer atteint 86.5% mAP à 41 FPS, un équilibre remarquable permettant haute précision ET temps réel viable.​

Latence
Définition: La latence mesure le délai entre capture d'une frame et disponibilité de la détection. Elle inclut temps de prétraitement, inférence réseau, et post-traitement (NMS, etc.).​

Latence
=
t
d
e
ˊ
tection disponible
−
t
capture frame
Latence=t 
d 
e
ˊ
 tection disponible
 −t 
capture frame
 
Typiquement exprimée en millisecondes (ms).​

Relation avec FPS: La latence et le FPS sont liés mais non identiques. FPS mesure le throughput (débit), tandis que latence mesure la réactivité. Pour un modèle traitant frames en pipeline, FPS peut être élevé (sortie chaque 25 ms = 40 FPS) tandis que latence reste élevée (100 ms de délai frame-à-détection).​

Criticité selon application:

Conduite autonome: Latence < 50 ms cruciale pour réaction rapide aux événements soudains (piéton surgissant)​

Drone autonome: Latence < 30 ms pour éviter obstacles à haute vitesse

Surveillance: Latence < 200 ms généralement acceptable

Analytics offline: Latence non critique

Limites: variabilité selon matériel:​

Les FPS et latence dépendent fortement du matériel d'inférence:

GPU haute performance (NVIDIA A100, V100): YOLOv11x atteint 88 FPS sur GPU T4​

GPU consommateur (NVIDIA RTX 3060): ~30-50 FPS pour mêmes modèles

CPU moderne (Intel i9): ~5-15 FPS, souvent insuffisant pour temps réel

Edge devices (Jetson Nano, mobile): ~10-20 FPS avec modèles compressés

Cette variabilité rend les comparaisons inter-études difficiles si le matériel diffère. Les publications doivent systématiquement spécifier la plateforme d'évaluation (GPU exact, batch size, résolution input) pour reproductibilité.​

Optimisations courantes: Quantification (FP32 → INT8), pruning, distillation, exportation vers TensorRT/ONNX peuvent améliorer FPS de 2-5× au prix d'une légère perte de mAP (~1-3 points).​

4.4 Choix des métriques selon cas d'usage
Le choix des métriques prioritaires doit refléter les contraintes opérationnelles et coûts relatifs des erreurs de chaque application.

Surveillance sécurité
Métriques prioritaires: Rappel élevé, mAP@0.50, FPS ≥ 25

Justification: Dans la surveillance, manquer une menace réelle (intrusion, comportement suspect, objet abandonné) est inacceptable et peut avoir des conséquences graves. Le rappel doit donc être maximisé, même au prix de quelques faux positifs. Les opérateurs humains peuvent filtrer les fausses alarmes, mais ne peuvent compenser les événements manqués. Un seuil IoU modéré (0.50) suffit car la localisation exacte est moins critique que la détection elle-même. Le temps réel est obligatoire pour réaction rapide.​

Conduite autonome
Métriques prioritaires: mAP@0.50:0.95, FPS ≥ 30, Latence < 50 ms

Justification: La conduite autonome exige précision de localisation maximale (d'où mAP@0.50:0.95) pour navigation sûre et décisions de trajectoire précises. Les faux positifs (freiner pour obstacle inexistant) perturbent le trafic et irritent passagers. Les faux négatifs (ne pas détecter piéton ou véhicule) sont potentiellement fatals. Précision ET Rappel doivent être simultanément élevés (> 0.98). La réactivité est critique: latence excessive rend détections obsolètes à haute vitesse.​

Retail analytics
Métriques prioritaires: Précision, Rappel, F1-Score

Justification: Les analytics retail (comptage clients, heatmaps, analyse comportementale) nécessitent statistiques précises. Les faux positifs surestiment le trafic, gonflant artificiellement les taux de conversion. Les faux négatifs sous-estiment le trafic, masquant des opportunités. Un équilibre (F1-Score élevé) assure des données fiables pour décisions business. Le temps réel strict n'est pas critique - traitement à 15-20 FPS suffit généralement.​

Inspection industrielle
Métriques prioritaires: Précision élevée, mAP@0.75, IoU

Justification: Détecter des défauts de fabrication nécessite localisation précise (d'où IoU et mAP@0.75 élevés) pour permettre intervention robotique ciblée ou rejet pièce. Les faux positifs génèrent des rejets coûteux de pièces conformes, impactant rentabilité. Les faux négatifs laissent passer des défauts, compromettant qualité et satisfaction client. La précision est donc prioritaire, avec rappel secondaire mais important. Le temps réel complet n'est pas toujours requis (10-20 FPS acceptable).

Analyse sportive
Métriques prioritaires: mAP@0.50, FPS ≥ 30, F1-Score

Justification: L'analyse sportive (tracking joueurs, détection ballon, statistiques jeu) nécessite fluidité visuelle (≥ 30 FPS) pour suivi perceptuellement agréable. Une précision modérée est acceptable car erreurs occasionnelles peuvent être corrigées manuellement en post-production. Les faux positifs/négatifs sporadiques sont tolérables si consistance temporelle générale est maintenue.

Santé/Médical
Métriques prioritaires: Précision très élevée, IoU, mAP@0.75

Justification: Les applications médicales (détection tumeurs, lésions, anomalies) exigent précision diagnostique maximale. Les faux positifs causent anxiété patient et procédures invasives inutiles. Les faux négatifs retardent traitement de pathologies graves, potentiellement fatals. La localisation exacte (IoU, mAP@0.75) est cruciale pour biopsies guidées ou planification chirurgicale. Le temps réel n'est généralement pas requis (5-15 FPS acceptable pour analyse offline).

Tableau récapitulatif: Métriques par cas d'usage
Ce tableau guide le choix des métriques d'évaluation et des seuils d'acceptabilité selon le contexte d'application, assurant que les modèles déployés répondent aux exigences opérationnelles réelles plutôt qu'aux seuls benchmarks académiques.