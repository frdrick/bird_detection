# See: https://docs.ultralytics.com/quickstart/#install-ultralytics
# conda create -n "birds" python=3.12 ipython
# pip install ultralytics
from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11n.pt")
