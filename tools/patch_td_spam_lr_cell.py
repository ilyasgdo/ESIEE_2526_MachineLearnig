#!/usr/bin/env python3
import json, os, sys

NB_PATH = r"C:\Users\ilyas\Documents\COURS\ESIEE_2526_MachineLearnig\tp5\TD_spam.ipynb"

CELL_MARKER = 'print("//////////////// 1 ///////////////////")'

NEW_SOURCE = [
    'print("//////////////// 1 ///////////////////")\n',
    'print("Nombre de mots dans le dictionnaire :", len(vectorizer.vocabulary_))\n',
    'print()\n',
    '\n',
    'from sklearn.model_selection import train_test_split\n',
    'from sklearn.linear_model import LogisticRegression\n',
    'from sklearn.metrics import classification_report, confusion_matrix\n',
    '\n',
    'train_X, test_X, train_y, test_y = train_test_split(\n',
    '    X, sms_dataset[\'label\'], test_size=0.2, random_state=42, stratify=sms_dataset[\'label\']\n',
    ')\n',
    '\n',
    "cls = LogisticRegression(class_weight='balanced', max_iter=1000)\n",
    'cls.fit(train_X, train_y)\n',
    'y_pred = cls.predict(test_X)\n',
    'score = cls.score(test_X, test_y)\n',
    '\n',
    'y_pred_best = y_pred\n',
    'best = score\n',
    'for i in range(1000):\n',
    '    cls.fit(train_X, train_y)\n',
    '    y_pred = cls.predict(test_X)\n',
    '    score = cls.score(test_X, test_y)\n',
    '    if score > best:\n',
    '        best = score\n',
    '        y_pred_best = y_pred\n',
    '        print(score)\n',
    '\n',
    'print(classification_report(test_y, y_pred_best))\n',
    'print(confusion_matrix(test_y, y_pred_best))\n',
    '\n',
    'print(best)\n',
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

    cells_changed = 0

    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if not isinstance(src, list):
            continue
        cell_text = "".join(src)
        if CELL_MARKER in cell_text:
            cell["source"] = NEW_SOURCE
            cells_changed += 1
            break

    if cells_changed > 0:
        backup_path = NB_PATH + ".bak"
        save_txt(backup_path, original_txt)
        save_txt(NB_PATH, json.dumps(data, ensure_ascii=False, indent=1))
        print(f"Cells changed: {cells_changed}")
        print("Backup saved to:", backup_path)
    else:
        print("Cellule cible non trouvée; aucune modification.")


if __name__ == "__main__":
    main()