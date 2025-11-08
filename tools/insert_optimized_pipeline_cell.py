#!/usr/bin/env python3
import json, os, sys

NB_PATH = r"C:\Users\ilyas\Documents\COURS\ESIEE_2526_MachineLearnig\tp5\TD_spam.ipynb"

# We'll insert after the marker cell used previously
CELL_MARKER = 'print("//////////////// 1 ///////////////////")'

NEW_SOURCE = [
    'print("//////////////// OPTIMISATION //////////////////")\n',
    'from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV\n',
    'from sklearn.pipeline import Pipeline\n',
    'from sklearn.feature_extraction.text import TfidfVectorizer\n',
    'from sklearn.linear_model import LogisticRegression\n',
    'from sklearn.metrics import classification_report, confusion_matrix, accuracy_score\n',
    '\n',
    '# Use raw text to avoid any data leakage\n',
    "X_text = sms_dataset['text']\n",
    "y = sms_dataset['label']\n",
    'X_train, X_test, y_train, y_test = train_test_split(\n',
    "    X_text, y, test_size=0.2, random_state=42, stratify=y\n",
    ')\n',
    '\n',
    "pipe = Pipeline([\n",
    "    ('vect', TfidfVectorizer(stop_words='english', sublinear_tf=True)),\n",
    "    ('clf', LogisticRegression(class_weight='balanced', max_iter=2000, solver='liblinear'))\n",
    "])\n",
    '\n',
    'param_grid = {\n',
    "    'vect__min_df': [0.001, 0.005, 0.01],\n",
    "    'vect__ngram_range': [(1,1), (1,2)],\n",
    "    'vect__max_df': [0.9, 1.0],\n",
    "    'vect__max_features': [None, 10000, 20000],\n",
    "    'clf__C': [0.5, 1, 2, 5, 10],\n",
    '}\n',
    '\n',
    'cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n',
    "grid = GridSearchCV(pipe, param_grid, cv=cv, n_jobs=-1, scoring='f1_macro', verbose=0)\n",
    'grid.fit(X_train, y_train)\n',
    'print("Best params:", grid.best_params_)\n',
    'best_model = grid.best_estimator_\n',
    '\n',
    'y_pred = best_model.predict(X_test)\n',
    'print(classification_report(y_test, y_pred))\n',
    'print(confusion_matrix(y_test, y_pred))\n',
    'print("Accuracy:", accuracy_score(y_test, y_pred))\n',
]


def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_txt(path, txt):
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)


def main():
    if not os.path.exists(NB_PATH):
        print("Notebook introuvable:", NB_PATH)
        sys.exit(2)
    original_txt = load_txt(NB_PATH)
    try:
        data = json.loads(original_txt)
    except Exception as e:
        print("Erreur lecture JSON:", e)
        sys.exit(3)

    insert_index = None
    for idx, cell in enumerate(data.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if not isinstance(src, list):
            continue
        cell_text = "".join(src)
        if CELL_MARKER in cell_text:
            insert_index = idx + 1
            break

    if insert_index is None:
        print("Cellule repere non trouvee; insertion en fin de notebook.")
        insert_index = len(data.get("cells", []))

    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": NEW_SOURCE,
    }

    data["cells"].insert(insert_index, new_cell)

    backup_path = NB_PATH + ".bak"
    save_txt(backup_path, original_txt)
    save_txt(NB_PATH, json.dumps(data, ensure_ascii=False, indent=1))
    print("Inserted optimized pipeline cell at index", insert_index)
    print("Backup saved to:", backup_path)


if __name__ == "__main__":
    main()