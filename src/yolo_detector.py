# src/yolo_detector.py

from ultralytics import YOLO
from src.config import YOLO_MODEL, CRITICAL_CLASSES

class YoloDetector:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL)

    def detect(self, image):
        results = self.model(image, verbose=False)[0]

        detections = []

        for box in results.boxes:
            cls_id = int(box.cls[0])
            cls_name = self.model.names[cls_id]

            if cls_name in CRITICAL_CLASSES:
                detections.append({
                    "class": cls_name,
                    "confidence": float(box.conf[0]),
                    "bbox": box.xyxy[0].tolist()
                })

        return detections
