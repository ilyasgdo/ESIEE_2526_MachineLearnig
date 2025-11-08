# TD — SMS Spam Classification (TP5)

Objectifs
- Charger et analyser le corpus SMS Spam Collection.
- Vectoriser le texte (Count, TF-IDF) et classifier (LogisticRegression).
- Optimiser via GridSearchCV et évaluer (rapport, confusion, ROC/PR).

Prérequis
- Python, pandas, numpy, scikit-learn, matplotlib.

Données
- Fichier `SMSSpamCollection.txt` (tabulé) avec colonnes: `label` (spam/ham), `text` (contenu).

Chargement et aperçu
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sms = pd.read_csv('SMSSpamCollection.txt', sep='\t', header=None, names=['label','text'])
print(sms.head())
print(sms['label'].value_counts())

# Cible binaire
y = (sms['label'].astype(str).str.lower() == 'spam').astype(int).values
X = sms['text'].values

spam_ratio = y.mean()
print(f"Proportion de spams: {spam_ratio:.3f}")
```

Split stratifié et pipeline TF-IDF + LogisticRegression
```python
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

pipe = Pipeline([
    ('vect', TfidfVectorizer(lowercase=True,
                             stop_words='english',
                             ngram_range=(1,2),
                             min_df=2,
                             max_df=0.9)),
    ('clf', LogisticRegression(max_iter=1000, class_weight='balanced', solver='liblinear'))
])

param_grid = {
    'vect__ngram_range': [(1,1), (1,2)],
    'vect__min_df': [1, 2, 3],
    'vect__max_df': [0.85, 0.90, 1.0],
    'vect__max_features': [None, 5000, 10000],
    'clf__C': [0.5, 1.0, 2.0, 5.0]
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(pipe, param_grid=param_grid, scoring='f1_macro', cv=cv, n_jobs=-1)
grid.fit(X_train, y_train)

best = grid.best_estimator_
print('Meilleurs hyperparamètres:', grid.best_params_)
print('Score CV (F1_macro):', grid.best_score_)

# Évaluation test
y_pred = best.predict(X_test)
print('\nAccuracy (test):', accuracy_score(y_test, y_pred))
print('\nClassification report (test):\n', classification_report(y_test, y_pred, digits=4))
print('Matrice de confusion (test):\n', confusion_matrix(y_test, y_pred))
```

Courbes ROC et PR, seuil de décision
```python
from sklearn.metrics import roc_auc_score, RocCurveDisplay, PrecisionRecallDisplay, precision_score, recall_score, f1_score
import numpy as np

if hasattr(best.named_steps['clf'], 'predict_proba'):
    y_proba = best.predict_proba(X_test)[:, 1]
    print('ROC-AUC (test):', roc_auc_score(y_test, y_proba))
    RocCurveDisplay.from_estimator(best, X_test, y_test)
    plt.grid(True); plt.show()
    PrecisionRecallDisplay.from_estimator(best, X_test, y_test)
    plt.grid(True); plt.show()

    # Essayons quelques seuils
    for t in [0.3, 0.4, 0.5, 0.6]:
        y_hat = (y_proba >= t).astype(int)
        p = precision_score(y_test, y_hat, zero_division=0)
        r = recall_score(y_test, y_hat, zero_division=0)
        f1 = f1_score(y_test, y_hat, zero_division=0)
        print(f't={t:.2f}  precision={p:.3f}  recall={r:.3f}  f1={f1:.3f}')
```

Alternatives utiles
```python
# SVM linéaire (souvent très performant sur TF-IDF)
from sklearn.svm import LinearSVC
pipe_svc = Pipeline([
    ('vect', TfidfVectorizer(lowercase=True, stop_words='english')),
    ('clf', LinearSVC(class_weight='balanced'))
])
pipe_svc.fit(X_train, y_train)
print('LinearSVC Accuracy:', accuracy_score(y_test, pipe_svc.predict(X_test)))

# Naive Bayes (Complément NB pour texte)
from sklearn.naive_bayes import ComplementNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
pipe_nb = Pipeline([
    ('vect', TfidfVectorizer(lowercase=True, stop_words='english')),
    ('clf', ComplementNB())
])
pipe_nb.fit(X_train, y_train)
print('ComplementNB Accuracy:', accuracy_score(y_test, pipe_nb.predict(X_test)))
```

Bonnes pratiques
- Utiliser `StratifiedKFold` et un `random_state` reproductible.
- Activer `class_weight='balanced'` si déséquilibre fort.
- Tester des `ngram_range` et `min_df` pour contrôler bruit vs signal.
- Nettoyer le texte (lowercase, retirer URLs/numéros) selon besoin; attention à la langue (stopwords).

Exercices guidés
- Comparer CountVectorizer vs TfidfVectorizer (F1_macro, ROC-AUC).
- Évaluer l’impact de `ngram_range=(1,2)` vs `(1,3)` et `min_df`.
- Tuner le seuil pour maximiser F1 ou rappel (policy anti-spam stricte).

Références
- scikit-learn: TfidfVectorizer, LogisticRegression, LinearSVC, GridSearchCV.
- Dataset SMS Spam Collection.