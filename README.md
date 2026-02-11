# Semantic_navigation_BDD100K

Hybrid Perception System using YOLO and Vision-Language Models (LLaVA)

## Overview

This project implements a hybrid perception system for autonomous ground navigation by combining:

- **Structured object detection** using YOLOv8
- **Semantic reasoning** using a Vision-Language Model (LLaVA via Ollama)
- A rule-based fusion layer for decision-making

The system evaluates urban driving scenes (BDD100K dataset) and produces navigation-oriented decisions:

- SAFE
- CAUTION
- STOP

The objective is not to replace object detection with a VLM, but to explore how structured perception and semantic reasoning can complement each other in robotics applications.

---


## System Architecture
### Pipeline:

Input Image → YOLOv8 Object Detection → LLaVA Scene Reasoning → Fusion Logic → Navigation Decision

### 1. Object Detection (YOLOv8n)

- YOLO without previous training
- Filters navigation-relevant classes:
  - person
  - car
  - truck
  - bus
  - motorcycle
  - bicycle

Outputs:
- Bounding boxes
- Class labels
- Confidence scores
- Inference latency


### 2. Vision-Language Reasoning (LLaVA via Ollama)

The VLM is prompted as a perception module for a mobile robot.

Example prompt:

        You are a perception module for a mobile ground robot.

        Analyze the image and answer:

        1. Is it safe to move forward?
        2. Are there pedestrians directly ahead?
        3. Are there obstacles or cars blocking the path?

        Respond strictly in this format:

        Decision: SAFE / CAUTION / STOP
        Reason: <short explanation>

Outputs:
- Semantic decision
- Inference latency


### 3. Fusion Logic

A rule-based module combines:

- Spatial analysis of detected bounding boxes
- VLM semantic output

Decision strategy:

- Person in critical region → STOP
- Large object in lower-central region → CAUTION
- No relevant obstacle → SAFE

This allows structured perception to dominate safety-critical decisions, while the VLM provides contextual reinforcement.


---


## Example Outputs

<p align="center">
  YOLO detection examples
</p>

<p align="center">
  <img src="results/output5.1.jpg" width="45%" />
  <img src="results/output2.jpg" width="45%" />
</p>

<p align="center">
  <img src="results/output3.jpg" width="45%" />
  <img src="results/output4.jpg" width="45%" />
</p>


<p align="center">
  Logs and metrics
</p>

The system logs structured outputs in JSON format:



---

## Technologies
- OpenCV
- YOLO
- Ollama (Llava:7b model) 

---


## Results


---


## Dataset

The system is dataset-agnostic and operates on any image source.

I used the following one:
- BDD100K: https://bair.berkeley.edu/blog/2018/05/30/bdd/


## Future Work
