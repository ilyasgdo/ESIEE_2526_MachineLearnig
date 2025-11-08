# TD – Recherche de minimum et descente de gradient

Ce cours synthétise et structure le notebook `4I_SI2_TD2_correction.ipynb` pour offrir une vue claire, rigoureuse et pratique de la recherche de minimum d’une fonction, via la méthode du nombre d’or et la descente de gradient.

## Objectifs
- Comprendre la convexité et les polynômes quadratiques.
- Implémenter la méthode du nombre d’or pour une fonction unimodale 1D.
- Maîtriser la descente de gradient (1D et 2D), ses conditions de convergence et ses limites.
- Visualiser et analyser le comportement des algorithmes.

## Prérequis
- Bases de Python et NumPy.
- Calcul différentiel (dérivées, gradient).
- Connaissances élémentaires de Matplotlib.

## Environnement
- Utiliser `%matplotlib inline` sous VS Code et Colab.
- Bibliothèques: `numpy`, `math`, `matplotlib`.

## Rappel: Convexité & Quadratique
- Fonction quadratique: `f(x) = a x^2 + b x + c`, convexe si `a > 0`.
- Minimum analytique: `x_opt = -b/(2a)`.

## Méthode du nombre d’or (Golden-section search)
- Problème: trouver le minimum d’une fonction unimodale sur `[x1, x3]`.
- Idée: sonder la fonction avec deux points `x2` et `x4` définis via `\varphi = (1+\sqrt{5})/2`.
- Mise à jour de l’intervalle selon la comparaison `f(x2)` vs `f(x4)` jusqu’à `|x2 - x4| < \epsilon`.
- Points clés:
  - Choisir un intervalle initial contenant le minimum.
  - Assurer l’unimodalité sur l’intervalle.

```python
import math

def mno(f, x1, x3, epsilon):
    phi = (math.sqrt(5) + 1) / 2
    x2 = x3 - (x3 - x1) / phi
    x4 = x1 + (x3 - x1) / phi
    while abs(x2 - x4) > epsilon:
        if f(x2) < f(x4):
            x3 = x4
        else:
            x1 = x2
        x2 = x3 - (x3 - x1) / phi
        x4 = x1 + (x3 - x1) / phi
    return (x3 + x1) / 2
```

## Descente de gradient (1D)
- Mise à jour: `x_{t+1} = x_t - \mu * df(x_t)` avec `\mu` le pas d’apprentissage.
- Conditions de convergence (quadratique): `0 < \mu < 1/L` où `L` est la Lipschitzianité de `df`.
- Effets du pas:
  - Trop petit: convergence lente.
  - Trop grand: oscillations ou divergence.

```python
def compute_f(x):
    a, b, c = 2, -4, 5
    return a*x**2 + b*x + c

def compute_df(x):
    a, b = 2, -4
    return 2*a*x + b

def algo_gradient1(df, mu, x0, n):
    x = x0
    hist = [x0]
    for _ in range(n):
        x = x - mu * df(x)
        hist.append(x)
    return hist
```

## Descente de gradient (2D)
- Mise à jour: `x_{t+1} = x_t - \mu * \nabla f(x_t)`.
- Visualisation 3D: utile pour comprendre les vallées et la condition du problème.
- Bonnes pratiques: normaliser les variables, ajuster `\mu`, utiliser arrêt par tolérance.

## Exercices guidés (recommandés)
- Choisir `a > 0`, `b`, `c` et calculer `x_opt`.
- Compléter `compute_f` et `compute_df`, valider numériquement `x_opt`.
- Implémenter `mno` et tester différentes `\epsilon`.
- Comparer la descente de gradient pour `\mu ∈ {0.0001, 0.1, 0.4, 0.5, 0.6}`.
- Visualiser et commenter les trajectoires (2D/3D).

## Bonnes pratiques
- Vérifier la convexité avant d’appliquer la descente de gradient.
- Choisir prudemment `\mu` (line search, décroissance, ou Bornes par Lipschitz).
- Utiliser des critères d’arrêt robustes (`|x_{t+1} - x_t|`, variation de `f`, nombre d’itérations).
- Tracer pour diagnostiquer (2D/3D, trajectoire, valeur de `f`).

## Les bonnes parties du cours (points forts)
- Rappel clair sur convexité et minimum analytique des quadratiques.
- Exposé didactique de la méthode du nombre d’or avec `\varphi` et mise à jour d’intervalle.
- Implémentations propres et minimalistes (`mno`, `algo_gradient1`).
- Visualisations 2D/3D pour comprendre convergence et oscillations.
- Exercices progressifs: compléter les fonctions, tester différents pas, analyser la convergence.
- Comparaison des méthodes (analytique vs numérique), apports et limites.

## Références utiles
- Golden-section search: Wikipedia (EN/FR).
- Gradient descent: articles et notes de cours standards.
- Convexité: rappels d’analyse réelle.

## Code minimal (exemple d’usage)
```python
# Minimum du polynôme par nombre d’or
x_opt_num = mno(compute_f, -100, 100, 1e-8)

# Gradient 1D avec pas fixe
traj = algo_gradient1(compute_df, mu=0.4, x0=10, n=50)
# Analyse: convergence/oscillation selon mu
```