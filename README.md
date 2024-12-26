# Setup 

## Conda environment
I suggest you create a conda environment for this project. 

If you don't have conda please see first:
- [Installing conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
Once conda --version gives an output similar to 
``` shell 
conda 24.11.2
```
It is now safely installed. 

Note that (at time of writing) it must be version between 3.8 to 3.12 (inclusive). I chose the most recent 3.12 for this project and also installed ipython so I can send code from my scripts to an interactive python terminal easily. You do not have to install ipython and can change *birds* to whatever name you wish.
```
conda create -n "birds" python=3.12 ipython
conda activate "birds"
```
## Installing dependenciemport cv2
from ultralytics import YOLO
# Load a pretrained YOLO model (recommended for training)
model = YOLO("models/yolo11n.pt")
s
Make sure you are in the *birds* environment before this. 
``` shell 
pip install ultralytics
```

I aim to setup a Dockerfile for this image soon so that it can be made more accessible.
