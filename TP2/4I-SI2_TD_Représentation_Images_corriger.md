# TD — Représentation d’images par histogrammes couleur (Holidays)

## Objectifs
- Construire une représentation robuste des images via histogrammes couleur.
- Mesurer la similarité et effectuer la recherche par requête (retrieval).
- Évaluer les performances et adopter de bonnes pratiques de vision.

## Prérequis
- Python, `numpy`, `matplotlib`, `imageio`.
- Notions d’histogrammes et distances (euclidienne, chi‑carré, intersection).

## Dataset Holidays
- Base d’environ 1491 images regroupées en ~500 scènes. La première image de chaque groupe sert de requête.
- Noms encodent groupe et indice: `1 005 02.jpg` → groupe 6, image 3; `…00.jpg` → requête.

## Mise en place
```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

import glob, os
from imageio import imread

images_dir = './Holidays_dataset'
image_file_names = sorted([os.path.split(f)[1]
                           for f in glob.glob(os.path.join(images_dir, '*.jpg'))])
N = len(image_file_names)
print('Nombre d\'images:', N)

# Chargement simple (liste)
images = [imread(os.path.join(images_dir, fn)) for fn in image_file_names]
```

## Histogrammes couleur (RGB/HSV)
- Choisir l’espace couleur: RGB (simple), HSV (teinte/saturation/valeur).
- Binning: nombre de classes par canal (p.ex. 8×8×8).
- Normalisation: somme = 1 (probabilités) pour comparaisons cohérentes.

```python
def rgb_to_hsv(I):
    # Utilise matplotlib pour rester léger
    return (plt.colors.rgb_to_hsv(I/255.0) if I.dtype != np.float32 else plt.colors.rgb_to_hsv(I))

def color_histogram(I, space='HSV', bins=(8,8,8), norm=True):
    if space.upper() == 'HSV':
        import matplotlib.colors as mcolors
        I_f = I.astype(np.float32)/255.0
        Ic = mcolors.rgb_to_hsv(I_f)
        ranges = [(0,1),(0,1),(0,1)]
    else:  # RGB
        Ic = I.astype(np.float32)
        ranges = [(0,255),(0,255),(0,255)]
    X = Ic.reshape(-1, 3)
    H, _ = np.histogramdd(X, bins=bins, range=ranges)
    H = H.astype(np.float32)
    if norm:
        s = H.sum()
        if s > 0: H /= s
    return H.ravel()
```

## Mesures de similarité
- Euclidienne (L2): simple mais sensible aux pics.
- Intersection d’histogrammes: robuste aux occlusions.
- Chi‑carré: standard pour histogrammes (évite division par zéro).

```python
def chi2_distance(h1, h2, eps=1e-10):
    num = (h1 - h2) ** 2
    den = h1 + h2 + eps
    return 0.5 * np.sum(num / den)

def hist_intersection(h1, h2):
    return np.sum(np.minimum(h1, h2))  # plus grand = plus proche
```

## Pipeline de recherche par requête
1. Pré‑calculer les histogrammes de toutes les images.
2. Choisir une image requête; calculer distances aux autres.
3. Trier et afficher Top‑K résultats.

```python
# 1) Pré-calcul des descripteurs
H_all = [color_histogram(I, space='HSV', bins=(8,8,8)) for I in images]
H_all = np.vstack(H_all)

# 2) Choisir une requête (ex.: première image d\'un groupe)
q_idx = 0
h_q = H_all[q_idx]

# 3) Distances Chi‑carré
D = np.array([chi2_distance(h_q, h) for h in H_all])
order = np.argsort(D)  # petit = plus proche

# Visualiser Top‑5
K = 5
fig, axes = plt.subplots(1, K, figsize=(12,3))
for i, ax in enumerate(axes):
    idx = order[i]
    ax.imshow(images[idx])
    ax.set_title(f"#{i} d={D[idx]:.3f}")
    ax.axis('off')
plt.show()
```

## Évaluation
- `précision@K`: part d’images du même groupe dans les K premiers.
- `rappel@K`: proportion d’images pertinentes retrouvées.
- `mAP`: pertinent pour tri global (optionnel).

## Bonnes pratiques
- Normaliser systématiquement les histogrammes.
- Tester plusieurs espaces (HSV souvent supérieur à RGB) et tailles de bins.
- Pré‑calculer et sérialiser les descripteurs pour accélérer.
- Choisir la mesure selon l’application (Chi‑carré vs intersection).

## Exercices guidés
- Implémentez `precision_at_k(order, y, q_idx, K)` avec `y` (labels de groupe).
- Comparez RGB vs HSV et 8×8×8 vs 16×16×16.
- Ajoutez l’intersection comme score et combinez (moyenne pondérée).

## Références
- Color histogram: Wikipedia, vision classique.
- Scikit‑image (optionnel) pour conversions couleur avancées.