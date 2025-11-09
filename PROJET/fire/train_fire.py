from ultralytics import YOLO
import torch

# Choose model size: 'yolov8n.pt' (fast), 'yolov8s.pt', 'yolov8m.pt' (balanced), 'yolov8l.pt' (accurate)
MODEL = 'yolov8m.pt'
DATA = r'C:/Users/ilyas/Documents/COURS/ESIEE_2526_MachineLearnig/PROJET/fire/fire.yaml'

if __name__ == '__main__':
    device = 0 if torch.cuda.is_available() else 'cpu'
    model = YOLO(MODEL)
    results = model.train(
        data=DATA,
        epochs=100,
        batch=16,
        imgsz=640,
        device=device,
        workers=4,
        patience=20,
        cos_lr=True,
        optimizer='AdamW',
        lr0=1e-3,
        weight_decay=5e-4,
        amp=True,
        project='runs/detect',
        name='train_fire'
    )
    print('Training complete. Best weights at:', results.save_dir)