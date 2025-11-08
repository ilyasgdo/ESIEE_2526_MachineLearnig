# Cours — Régression (TP3)

Objectifs
- Comprendre la régression linéaire et ses métriques (MSE, RMSE, R²).
- Explorer variance, covariance, corrélation et vérifier la linéarité.
- Étendre avec régularisation (Ridge/Lasso), polynômes, KNN régression.

Prérequis
- Python, pandas, numpy, matplotlib, scikit-learn.
- Bases d’algèbre linéaire et statistiques.

Données (ex. CIQUAL)
- Fichier `CIQUAL.csv`: valeurs nutritionnelles d’aliments (énergie, lipides, glucides, protides, etc.).
- Sélectionnez les colonnes quantitatives pertinentes.

Imports et chargement
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

ciqual = pd.read_csv('CIQUAL.csv')
num_cols = ['Energie', 'Lipides', 'Glucides', 'Protides']
df = ciqual[num_cols].dropna()
print(df.describe())
```

Exploration: variance, covariance, corrélation
```python
print('Covariance:\n', df.cov())
print('\nCorrélation:\n', df.corr())

plt.figure(figsize=(6,4))
plt.scatter(df['Lipides'], df['Energie'], alpha=0.5)
plt.xlabel('Lipides')
plt.ylabel('Energie')
plt.title('Energie vs Lipides')
plt.grid(True)
plt.show()
```

Régression linéaire (base)
```python
X = df[['Lipides','Protides','Glucides']].values
y = df['Energie'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linreg = LinearRegression().fit(X_train, y_train)
y_pred = linreg.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print(f'RMSE: {rmse:.3f}, R²: {r2:.3f}')
```

Régularisation (Ridge/Lasso)
```python
ridge = Ridge(alpha=1.0).fit(X_train, y_train)
lasso = Lasso(alpha=0.01).fit(X_train, y_train)
print('Ridge R²:', r2_score(y_test, ridge.predict(X_test)))
print('Lasso R²:', r2_score(y_test, lasso.predict(X_test)))
```

Polynômes et pipeline
```python
model_poly = Pipeline([
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('linreg', LinearRegression())
]).fit(X_train, y_train)

y_pred_poly = model_poly.predict(X_test)
print('Poly (deg=2) R²:', r2_score(y_test, y_pred_poly))
```

Régression KNN (option)
```python
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5).fit(X_train, y_train)
print('KNN R²:', r2_score(y_test, knn.predict(X_test)))
```

Visualisation des résidus
```python
import seaborn as sns
res = y_test - y_pred
plt.figure(figsize=(6,4))
sns.histplot(res, kde=True)
plt.title('Distribution des résidus (linéaire)')
plt.grid(True)
plt.show()
```

Bonnes pratiques
- Vérifier la linéarité par visualisation et corrélation.
- Standardiser les variables si régularisation ou KNN.
- Limiter le degré des polynômes pour éviter le sur-apprentissage.
- Utiliser un `random_state` fixe pour comparabilité.

Exercices guidés
- Comparer les performances: linéaire vs Ridge vs Lasso vs Poly.
- Tester `degree=3` avec régularisation (Ridge) et commenter.
- Analyser l’importance des variables (coefficients) et interpréter.

Références
- Documentation scikit-learn: LinearRegression, Ridge, Lasso, PolynomialFeatures.
- Notes de cours Régression (TP3).