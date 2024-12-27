from ultralytics import YOLO
import cv2
import os
import kagglehub

# Download latest version
path = kagglehub.dataset_download("davemahony/20-uk-garden-birds")
print("Path to dataset files:", path)

# Initialise model
model = YOLO('model/yolo11n.pt')

# Train the model with MPS (for apple silicon - change this on other devices)
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device="mps")
