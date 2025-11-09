# Détection de feu et fumée (YOLOv8)

Ce dossier contient tout le nécessaire pour entraîner et tester un modèle de détection du feu et de la fumée en milieu urbain avec Ultralytics YOLO.

## Arborescence attendue

```
fire/
├── fire.yaml               # config dataset YOLO (déjà créé)
├── train_fire.py           # script d’entraînement
├── infer_fire.py           # script d’inférence (webcam ou vidéo)
├── check_dataset.py        # vérifie cohérence annotations/images (à exécuter avant train)
├── images/
│   ├── train/              # images .jpg/.png d’entraînement
│   ├── val/                # images de validation
│   └── test/               # images de test
└── labels/
    ├── train/              # annotations YOLO pour train
    ├── val/                # annotations pour val
    └── test/               # annotations pour test
```

## Format des annotations (YOLO)

- Un fichier `.txt` par image, même nom que l’image (ex: `img_001.jpg` → `img_001.txt`).
- Chaque ligne: `class x_center y_center width height` en coordonnées normalisées [0,1].
- Classes dans `fire.yaml`: `0 = fire`, `1 = smoke`.

Exemple de ligne (un feu détecté au centre):
```
0 0.50 0.50 0.30 0.30
```

## Installation

- Prérequis: Python 3.8+.
- Installer Ultralytics (Torch est installé automatiquement si nécessaire):
```
python -m pip install -U ultralytics
```
Si `python` n’est pas reconnu, essayer:
```
py -m pip install -U ultralytics
```

## Vérification du dataset

Avant d’entraîner, lancez:
```
python check_dataset.py
```
Ce script vérifie la présence des paires image/label et la validité des annotations (classes et valeurs dans [0,1]).

## Entraînement

- Adapter les chemins du dataset si besoin dans `fire.yaml`.
- Lancer l’entraînement (par défaut sur `yolov8m.pt`, 100 epochs):
```
python train_fire.py
```
Vous pouvez ajuster `epochs`, `batch`, `imgsz`, etc. dans le script.

## Inférence

Tester la webcam (caméra par défaut `0`):
```
python infer_fire.py 0
```
Tester une vidéo:
```
python infer_fire.py path\to\video.mp4
```
Paramètres utiles: `--conf 0.35` pour le seuil de confiance, `--iou 0.5` pour le NMS.

## Conseils dataset

- Inclure des « négatifs » (images sans feu/fumée) pour limiter les faux positifs.
- Varier les conditions: jour/nuit, pluie, brouillard, différentes caméras, distances.
- Annoter systématiquement la fumée (`smoke`) en plus des flammes (`fire`).

## Évaluation

- Sur le split `val` et `test`: mAP@50-95, précision, rappel.
- Sur cas réels: taux d’alertes vraies/fausses, latence d’inférence.

## Déploiement (idées)

- Exposition d’événements via HTTP/MQTT, horodatage, tracking multi-caméras.
- Filtrage temporel (séquence d’images) pour éviter éclats lumineux ponctuels.