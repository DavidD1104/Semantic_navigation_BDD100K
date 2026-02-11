# src/config.py

YOLO_MODEL = "yolov8n.pt"

CRITICAL_CLASSES = [
    "person",
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle"
]


CRITICAL_REGION_Y_RATIO = 0.4  # bottom 60% considered critical
