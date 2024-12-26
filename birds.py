# See: https://docs.ultralytics.com/quickstart/#install-ultralytics
# conda create -n "birds" python=3.12 ipython
# pip install ultralytics
import cv2
from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("models/yolo11n.pt", "v8")

