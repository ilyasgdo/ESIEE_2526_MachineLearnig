#!/usr/bin/env python3
import json, os, sys

NB_PATH = r"C:\Users\ilyas\Documents\COURS\ESIEE_2526_MachineLearnig\tp5\TD_spam.ipynb"


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
    replacements = 0

    for cell in data.get("cells", []):
        src = cell.get("source", [])
        if not isinstance(src, list):
            continue
        new_src = []
        cell_modified = False
        for line in src:
            new_line = line
            if "min_df=0.003" in new_line:
                new_line = new_line.replace("min_df=0.003", "min_df=0.001")
            if "min_df = 0.003" in new_line:
                new_line = new_line.replace("min_df = 0.003", "min_df = 0.001")
            if new_line != line:
                replacements += 1
                cell_modified = True
            new_src.append(new_line)
        if cell_modified:
            cell["source"] = new_src
            cells_changed += 1

    if cells_changed > 0:
        backup_path = NB_PATH + ".bak"
        save_txt(backup_path, original_txt)
        save_txt(NB_PATH, json.dumps(data, ensure_ascii=False, indent=1))
        print(f"Cells changed: {cells_changed}, replacements: {replacements}")
        print("Backup saved to:", backup_path)
    else:
        print("Aucune modification n'a été nécessaire.")


if __name__ == "__main__":
    main()