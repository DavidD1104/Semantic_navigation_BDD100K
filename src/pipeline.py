# src/pipeline.py

import cv2
import time

from src.yolo_detector import YoloDetector
from src.vlm_reasoner import VLMReasoner
from src.fusion_logic import evaluate_decision
from src.config import CRITICAL_REGION_Y_RATIO

def draw_overlay(image, detections, decision):
        h, w, _ = image.shape
        critical_y = int(h * CRITICAL_REGION_Y_RATIO)

        # Draw critical region
        cv2.rectangle(image, (0, critical_y), (w, h), (0, 0, 255), 2)

        for det in detections:
            x1, y1, x2, y2 = map(int, det["bbox"])
            label = det["class"]

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.putText(image, f"Decision: {decision}",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    3)

        return image

class NavigationPipeline:

    def __init__(self):
        self.detector = YoloDetector()
        self.vlm = VLMReasoner()


    def run_on_image(self, image_path):

        image = cv2.imread(image_path)
        h, w, _ = image.shape

        start = time.time()
        detections = self.detector.detect(image)
        yolo_time = time.time() - start

        start = time.time()
        vlm_response = self.vlm.query(image_path)
        vlm_time = time.time() - start

        rule_decision = evaluate_decision(detections, h)

        annotated = draw_overlay(image.copy(), detections, rule_decision)
        cv2.imwrite("results/output.jpg", annotated)

        return {
            "detections": detections,
            "vlm_response": vlm_response,
            "rule_decision": rule_decision,
            "yolo_time": yolo_time,
            "vlm_time": vlm_time
        }
    
    
