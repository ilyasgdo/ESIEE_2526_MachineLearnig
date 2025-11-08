#!/usr/bin/env python3
import json, re, sys, os
from pathlib import Path

NB_PATH = r"C:\Users\ilyas\Documents\COURS\ESIEE_2526_MachineLearnig\tp5\TD_spam.ipynb"

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_txt(path, txt):
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)

def apply_fixes_to_line(line):
    orig = line
    # VS Code matplotlib
    line = re.sub(r'%matplotlib\s+notebook', '%matplotlib inline', line)
    # scikit-learn deprecated modules
    line = re.sub(r'\bfrom\s+sklearn\.cross_validation\s+import\b', 'from sklearn.model_selection import', line)
    line = re.sub(r'\bsklearn\.cross_validation\b', 'sklearn.model_selection', line)
    line = re.sub(r'\bfrom\s+sklearn\.grid_search\s+import\b', 'from sklearn.model_selection import', line)
    # typos
    line = line.replace('disctionnaire', 'dictionnaire')
    # temp variable fixes
    line = re.sub(r'\bXXX\b', 'X2', line)
    line = re.sub(r'\bXX\b', 'X3', line)
    changed = (line != orig)
    return line, changed

def main():
    nb_path = NB_PATH
    if not os.path.exists(nb_path):
        print("Notebook introuvable:", nb_path)
        sys.exit(2)
    original_txt = load_txt(nb_path)
    try:
        data = json.loads(original_txt)
    except Exception as e:
        print("Erreur lecture JSON:", e)
        sys.exit(3)

    cells_changed = 0
    replacements = 0

    for cell in data.get("cells", []):
        src = cell.get("source", [])
        if not isinstance(src, list):
            continue
        new_src = []
        cell_modified = False
        for line in src:
            new_line, changed = apply_fixes_to_line(line)
            new_src.append(new_line)
            if changed:
                replacements += 1
                cell_modified = True
        if cell_modified:
            cell["source"] = new_src
            cells_changed += 1

    if cells_changed > 0:
        backup_path = nb_path + ".bak"
        save_txt(backup_path, original_txt)
        save_txt(nb_path, json.dumps(data, ensure_ascii=False, indent=1))
        print(f"Cells changed: {cells_changed}, replacements: {replacements}")
        print("Backup saved to:", backup_path)
    else:
        print("Aucune modification n'a été nécessaire.")

if __name__ == "__main__":
    main()