# src/fusion_logic.py

from src.config import CRITICAL_REGION_Y_RATIO

def evaluate_decision(detections, image_height):

    critical_y = image_height * CRITICAL_REGION_Y_RATIO

    for det in detections:
        x1, y1, x2, y2 = det["bbox"]

        if y2 > critical_y:
            if det["class"] == "person":
                return "STOP"
            else:
                return "CAUTION"

    return "SAFE"
