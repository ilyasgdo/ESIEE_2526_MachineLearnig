# TD — Régression (Flu Surveillance)

Objectifs
- Modéliser l’incidence de la grippe (`ILI`) à partir des requêtes web (`Queries`).
- Préparer des données temporelles et éviter la fuite d’information.
- Évaluer une régression linéaire, proposer des améliorations.

Prérequis
- Python, pandas, numpy, matplotlib, scikit-learn.
- Bases de régression (MSE, RMSE, R²), corrélation, log-transform.

Jeu de données
- Fichiers `FluTrain.csv` (2004–2011) et `FluTest.csv` (2012).
- Colonnes typiques : `Week` (date), `ILI` (incidence grippale), `Queries` (volume de requêtes). 

Imports et chargement
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Chargement
flu_train = pd.read_csv('FluTrain.csv')
flu_test = pd.read_csv('FluTest.csv')

# Parse des dates si nécessaire
flu_train['Week'] = pd.to_datetime(flu_train['Week'])
flu_test['Week'] = pd.to_datetime(flu_test['Week'])

print(flu_train.head())
print(flu_train.describe())
```

Exploration et corrélation
```python
plt.figure(figsize=(6,4))
plt.scatter(flu_train['Queries'], flu_train['ILI'], alpha=0.5)
plt.xlabel('Queries')
plt.ylabel('ILI')
plt.title('ILI vs Queries (train)')
plt.grid(True)
plt.show()

print('Corrélation ILI-Queries =', flu_train[['ILI','Queries']].corr().iloc[0,1])
```

Log-transform pour linéariser
```python
flu_train['log_ILI'] = np.log(flu_train['ILI'])
flu_test['log_ILI'] = np.log(flu_test['ILI'])

plt.figure(figsize=(6,4))
plt.scatter(flu_train['Queries'], flu_train['log_ILI'], alpha=0.5, color='tab:orange')
plt.xlabel('Queries')
plt.ylabel('log(ILI)')
plt.title('log(ILI) vs Queries (train)')
plt.grid(True)
plt.show()
```

Modèle de base (régression linéaire)
```python
X_train = flu_train[['Queries']].values
y_train = flu_train['log_ILI'].values
X_test = flu_test[['Queries']].values
y_test = flu_test['log_ILI'].values

linreg = LinearRegression()
linreg.fit(X_train, y_train)

print('Coef:', linreg.coef_, 'Intercept:', linreg.intercept_)

y_pred_log = linreg.predict(X_test)
# Revenir dans l’espace original
y_pred = np.exp(y_pred_log)
y_true = np.exp(y_test)

rmse = mean_squared_error(y_true, y_pred, squared=False)
r2 = r2_score(y_true, y_pred)
print(f'RMSE (test): {rmse:.4f}, R² (test): {r2:.4f}')

plt.figure(figsize=(6,4))
plt.scatter(y_true, y_pred, alpha=0.5)
plt.xlabel('ILI vrai')
plt.ylabel('ILI prédit')
plt.title('Prédictions vs Valeurs vraies (test)')
plt.grid(True)
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
plt.show()
```

Améliorations rapides
- Caractéristiques temporelles : moyenne mobile des `Queries` pour lisser.
- Interaction ou polynomial léger si courbure résiduelle.
- Validation temporelle (éviter mélange train/test).

Exemple de moyenne mobile
```python
# Ajouter moyenne mobile sur 3 semaines dans train et test (attention aux bords)
flu_train = flu_train.sort_values('Week')
flu_test = flu_test.sort_values('Week')

flu_train['Queries_ma3'] = flu_train['Queries'].rolling(window=3, min_periods=1).mean()
flu_test['Queries_ma3'] = flu_test['Queries'].rolling(window=3, min_periods=1).mean()

X_train2 = flu_train[['Queries','Queries_ma3']].values
X_test2 = flu_test[['Queries','Queries_ma3']].values

linreg2 = LinearRegression().fit(X_train2, flu_train['log_ILI'].values)
y_pred_log2 = linreg2.predict(X_test2)
y_pred2 = np.exp(y_pred_log2)

rmse2 = mean_squared_error(y_true, y_pred2, squared=False)
r22 = r2_score(y_true, y_pred2)
print(f'RMSE amélioré: {rmse2:.4f}, R² amélioré: {r22:.4f}')
```

Bonnes pratiques
- Découper par temps (ex.: train < 2012, test = 2012), pas de mélange.
- Tester la log-transform si l’hétéroscédasticité est forte.
- Visualiser résidus vs prédictions pour diagnostiquer (courbure, variance, outliers).
- Comparer plusieurs variantes simples, garder celle la plus robuste.

Exercices guidés
- Ajouter `Queries_ma5` et comparer RMSE/R².
- Tester un polynôme degré 2 sur `Queries` (sur log(ILI)).
- Tracer résidus sur test et interpréter.

Références
- Introduction à la régression linéaire (scikit-learn).