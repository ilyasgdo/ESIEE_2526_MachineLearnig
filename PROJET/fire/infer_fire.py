from ultralytics import YOLO
import sys

MODEL_PATH = r'runs/detect/train_fire/weights/best.pt'

if __name__ == '__main__':
    source = sys.argv[1] if len(sys.argv) > 1 else '0'  # webcam by default
    model = YOLO(MODEL_PATH)
    # Adjust conf for urban false positives (traffic lights, headlights)
    model.predict(
        source=source,
        conf=0.35,
        iou=0.5,
        imgsz=640,
        stream=True,
        save=True,
        project='runs/infer',
        name='fire_demo'
    )