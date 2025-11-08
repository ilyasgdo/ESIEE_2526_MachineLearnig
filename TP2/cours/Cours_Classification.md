# Cours — Classification de messages (NLP, BOW, TF‑IDF, K‑Means)

## Objectifs
- Transformer du texte en vecteurs exploitables (sac‑de‑mots, TF‑IDF).
- Réduire le vocabulaire (stopwords, min_df/max_df, stemming).
- Regrouper des messages par similarité avec K‑Means et évaluer.

## Prérequis
- Python, `numpy`, `scikit‑learn`, `nltk` (stopwords).
- Concepts: distance/similarité, clustering non supervisé.

## Représentation en sac‑de‑mots (CountVectorizer)
```python
corpus = [
    'Vous êtes excellents',
    'Les étudiants sont souvent excellents',
    'Les étudiants aiment bien rigoler',
    'Rigoler est excellent pour la santé',
    'étudier est excellent'
]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print('Vocabulaire:', vectorizer.vocabulary_)
print(X.toarray())
```

## Réduction du vocabulaire
- `stopwords` (fr/en): retirer articles, auxiliaires, liaisons.
- `min_df`, `max_df`: filtrer termes trop rares/usuel.
- Stemming/Lemmatisation: ramener les mots à la racine/lemme.

```python
import nltk
# nltk.download('stopwords')  # à lancer une fois
from nltk.corpus import stopwords
stwf = stopwords.words('french')

vectorizer = CountVectorizer(stop_words=stwf, min_df=1, max_df=1.0)
X = vectorizer.fit_transform(corpus)
```

### Stemming (Snowball, français)
```python
from nltk.stem.snowball import FrenchStemmer
stemmer = FrenchStemmer()

def stem_tokenizer(doc):
    import re
    tokens = re.findall(r"\b\w+\b", doc.lower())
    return [stemmer.stem(t) for t in tokens]

vectorizer = CountVectorizer(tokenizer=stem_tokenizer,
                             stop_words=stwf, min_df=1)
X = vectorizer.fit_transform(corpus)
```

## TF‑IDF (pondérer par fréquence inverse du document)
```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words=stwf, min_df=1)
X = tfidf.fit_transform(corpus)
print('Dim:', X.shape)
```

## Clustering K‑Means (K‑moyennes)
- Initialisation `k‑means++` recommandée.
- Choix de K: méthode du coude (inertie) + silhouette.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

K = 2
kmeans = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=42)
labels = kmeans.fit_predict(X)
print('Inertie:', kmeans.inertia_)
if X.shape[0] > K:
    print('Silhouette:', silhouette_score(X, labels, metric='cosine'))
```

### Méthode du coude
```python
Ks = range(2, 8)
Inertia = []
for k in Ks:
    km = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    km.fit(X)
    Inertia.append(km.inertia_)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(list(Ks), Inertia, '-o'); plt.xlabel('K'); plt.ylabel('Inertie');
```

## Pipeline scikit‑learn
- Enchaîner vectorisation et clustering proprement.
```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stwf, min_df=1)),
    ('km', KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42))
])
labels = pipe.fit_predict(corpus)
print(labels)
```

## Évaluation (si vérité de terrain)
- Silhouette (non supervisé), Homogénéité/Complétude/V‑mesure si labels connus.
```python
from sklearn.metrics import homogeneity_score, completeness_score, v_measure_score
# y_true: labels si disponibles
# print(homogeneity_score(y_true, labels), completeness_score(y_true, labels), v_measure_score(y_true, labels))
```

## Bonnes pratiques
- Nettoyer le texte: minuscules, ponctuation, accents, emojis si besoin.
- Ajuster `min_df`/`max_df`, `ngram_range` et stemming selon la langue.
- Préférer TF‑IDF pour réduire l’impact des mots fréquents.
- Fixer `random_state` pour reproductibilité; tester plusieurs `n_init`.

## Exercices guidés
- Comparez CountVectorizer vs TfidfVectorizer (silhouette, cohérence des clusters).
- Ajoutez `ngram_range=(1,2)` et observez l’impact.
- Testez K dans [2..10] et discutez le coude; ajoutez silhouette.

## Références
- Scikit‑learn: `feature_extraction.text`, `cluster.KMeans`.
- NLTK: stopwords, SnowballStemmer.