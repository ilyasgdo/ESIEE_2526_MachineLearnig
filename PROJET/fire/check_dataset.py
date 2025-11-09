import os
import sys
from pathlib import Path

CLASSES = {0: "fire", 1: "smoke"}
VALID_SPLITS = ["train", "val", "test"]

ROOT = Path(__file__).resolve().parent
IMAGES_DIR = ROOT / "images"
LABELS_DIR = ROOT / "labels"


def check_label_line(line: str, img_w: int = 1, img_h: int = 1, fname: str = ""):
    parts = line.strip().split()
    if len(parts) != 5:
        return f"{fname}: ligne mal formée (attendu 5 éléments)."
    try:
        cls = int(parts[0])
        x, y, w, h = map(float, parts[1:])
    except Exception:
        return f"{fname}: types invalides (class int, x y w h float)."

    if cls not in CLASSES:
        return f"{fname}: classe {cls} inconnue (attendu {list(CLASSES.keys())})."
    for name, v in zip(["x", "y", "w", "h"], [x, y, w, h]):
        if not (0.0 <= v <= 1.0):
            return f"{fname}: valeur {name}={v} hors [0,1]."
    if w <= 0 or h <= 0:
        return f"{fname}: largeur/hauteur doivent être > 0."
    return None


def gather_images(split_dir: Path):
    return [p for p in split_dir.glob("*.*") if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]


def main():
    errors = []

    # Vérif existences dossiers
    for base, name in [(IMAGES_DIR, "images"), (LABELS_DIR, "labels")]:
        if not base.exists():
            errors.append(f"Dossier manquant: {name} → {base}")

    for split in VALID_SPLITS:
        img_split = IMAGES_DIR / split
        lab_split = LABELS_DIR / split
        if not img_split.exists():
            errors.append(f"Dossier images {split} manquant: {img_split}")
        if not lab_split.exists():
            errors.append(f"Dossier labels {split} manquant: {lab_split}")

    if errors:
        print("Erreurs d’arborescence:")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    # Vérif paires image/label
    total_imgs = 0
    total_labels = 0
    for split in VALID_SPLITS:
        img_split = IMAGES_DIR / split
        lab_split = LABELS_DIR / split

        images = gather_images(img_split)
        total_imgs += len(images)
        for img in images:
            txt = lab_split / (img.stem + ".txt")
            if not txt.exists():
                errors.append(f"Label manquant pour {split}: {img.name} → {txt}")
            else:
                total_labels += 1
                try:
                    lines = txt.read_text(encoding="utf-8").strip().splitlines()
                except Exception:
                    errors.append(f"Lecture impossible: {txt}")
                    continue
                for i, line in enumerate(lines, 1):
                    msg = check_label_line(line, fname=f"{txt}:{i}")
                    if msg:
                        errors.append(msg)

    # Résumé
    print(f"Images trouvées: {total_imgs}")
    print(f"Fichiers labels trouvés: {total_labels}")

    if errors:
        print("\nProblèmes détectés:")
        for e in errors[:200]:  # limite affichage
            print(" -", e)
        print(f"\nTotal problèmes: {len(errors)}")
        sys.exit(2)
    else:
        print("\nDataset OK: structure et annotations valides.")
        sys.exit(0)


if __name__ == "__main__":
    main()