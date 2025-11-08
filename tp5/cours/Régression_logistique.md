# Cours — Régression logistique (TP5)

Objectifs
- Comprendre la sigmoïde, le logit, les odds et log-odds.
- Mettre en œuvre une régression logistique binaire en pratique (scikit-learn).
- Gérer le déséquilibre de classes, choisir le seuil, évaluer via ROC/PR.

Prérequis
- Python, pandas, numpy, matplotlib, scikit-learn.
- Bases de classification binaire, métriques (accuracy, precision, recall, F1, ROC-AUC).

Sigmoïde et logit
```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.linspace(-8, 8, 400)
curves = [(0, 1), (1, 2), (-1, 4), (0, -2)]  # (beta0, beta1)
plt.figure(figsize=(6,4))
for b0, b1 in curves:
    plt.plot(x, sigmoid(b0 + b1 * x), label=f"β0={b0}, β1={b1}")
plt.title("Sigmoïde composée avec une affine β0 + β1 x")
plt.grid(True)
plt.legend()
plt.show()
```
- Odds: `odds = p / (1 - p)`; Logit: `logit(p) = log(odds)`.
- La régression logistique modèle `logit(p(y=1|x)) = β0 + βᵀx`.

Données d’exemple (Défaut bancaire)
- Fichier `Default.csv` (fourni) avec colonnes typiques: `default` (Yes/No), `student` (Yes/No), `balance`, `income`.

Pipeline régression logistique (sklearn)
```python
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt

# Chargement (adapter au chemin si besoin)
df = pd.read_csv('Default.csv')
print(df.head())

# Cible binaire robuste (Yes/No → 1/0)
y = df['default'].astype(str).str.lower().isin(['yes', '1', 'true']).astype(int)

# Variables explicatives (adapter selon colonnes disponibles)
import numpy as np
X = pd.DataFrame()
for col in ['balance', 'income']:
    if col in df.columns:
        X[col] = df[col]
# Étudiant (variable catégorielle binaire si présente)
if 'student' in df.columns:
    X['student'] = df['student'].astype(str).str.lower().isin(['yes','1','true']).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=400, class_weight='balanced', solver='liblinear'))
])

param_grid = {
    'clf__C': [0.1, 0.5, 1.0, 2.0, 5.0],
    'clf__penalty': ['l2', 'l1']  # liblinear supporte l1/l2 en binaire
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(pipe, param_grid=param_grid, scoring='f1', cv=cv, n_jobs=-1)
grid.fit(X_train, y_train)

best = grid.best_estimator_
print('Meilleurs hyperparamètres:', grid.best_params_)
print('Score CV (F1):', grid.best_score_)

# Évaluation standard
y_pred = best.predict(X_test)
print('\nClassification report (test):\n', classification_report(y_test, y_pred, digits=4))
print('Matrice de confusion (test):\n', confusion_matrix(y_test, y_pred))

# Probabilités & ROC-AUC
import numpy as np
if hasattr(best.named_steps['clf'], 'predict_proba'):
    y_proba = best.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_proba)
    print(f'ROC-AUC (test): {auc:.4f}')
    from sklearn.metrics import RocCurveDisplay, PrecisionRecallDisplay
    RocCurveDisplay.from_estimator(best, X_test, y_test)
    plt.grid(True); plt.show()
    PrecisionRecallDisplay.from_estimator(best, X_test, y_test)
    plt.grid(True); plt.show()
```

Ajustement du seuil (policy/risque)
```python
# Choisir un seuil selon un compromis précision/rappel
thresholds = np.linspace(0.1, 0.9, 9)
from sklearn.metrics import precision_score, recall_score, f1_score
if 'y_proba' in locals():
    for t in thresholds:
        y_hat = (y_proba >= t).astype(int)
        p = precision_score(y_test, y_hat, zero_division=0)
        r = recall_score(y_test, y_hat, zero_division=0)
        f1 = f1_score(y_test, y_hat, zero_division=0)
        print(f't={t:.2f}  precision={p:.3f}  recall={r:.3f}  f1={f1:.3f}')
```
- En présence de classes déséquilibrées, `class_weight='balanced'` et le réglage du seuil sont souvent cruciaux.

Interprétation des coefficients
```python
# Coefficients (log-odds par unité): signe et magnitude
coef = best.named_steps['clf'].coef_.ravel()
for name, c in zip(X.columns, coef):
    print(f'{name:>12}: {c:+.4f}')
```
- `exp(coef)` donne le multiplicateur d’odds par unité (si features standardisées, interprétation relative).

Bonnes pratiques
- Standardiser les variables numériques (pipeline) avant la régression logistique.
- Utiliser `StratifiedKFold` et un `random_state` fixe pour comparabilité.
- Penser au prétraitement des catégories (OneHot) si nécessaires.
- Ajuster le seuil selon le contexte métier (coût FP/FN).

Exercices guidés
- Ajouter `OneHotEncoder` si des catégories existent; comparer performances.
- Tester `solver='lbfgs'` (L2) et comparer vitesse/score vs `liblinear`.
- Implémenter une courbe coût (FP/FN) et choisir un seuil optimal selon une matrice de coûts.

Références
- scikit-learn: LogisticRegression, GridSearchCV, RocCurveDisplay, PrecisionRecallDisplay.
- Notes de cours “Régression logistique”.