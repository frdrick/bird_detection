## Setup conda environment (optional)
I suggest you create a conda environment for this project to avoid issues with these packages messing with other projects. 

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
## Installing dependencies

[See ultralytics quickstart](https://docs.ultralytics.com/quickstart/#__tabbed_1_1)
Make sure you are in the *birds* environment before this. 
``` shell 
pip install ultralytics
```
## Training
There are a few different options for training object detection models - both the data itself or alternatively software to actually label images yourself. Labelling data yourself - especially when the context of the data you're labelling matches the context of your final application can be extremely useful. I believe this following [Jeff Pi In the Sky's][jeff-yt] youtube series detecting birds in his back garden. Training his model with images of birds from his webcam significantly improved performance when identifying birds from this same webcam. 

1. Getting labelled data.

There are loads of options for this:
- Kaggle datasets (particularly for bird detection outside of the UK - I do not want to train my model on birds that don't come to the UK so I will be careful using large kaggle datasets)
- Labelling data yourself. Some of the options for this I've found so far include:
    - [Roboflow][roboflow]
    - [Label studio][label-studio]
    - [Datatorch][datatorch], also [see here](https://medium.com/datatorch/automating-data-annotation-5eb828789cbd) for a medium article using it.

2. Using a pretrained model.

Ultralytics has made it's model work out of the box with some significant datasets - [see here.](https://docs.ultralytics.com/modes/train/#why-choose-ultralytics-yolo-for-training)
<!--NOTE: subject to change-->
I opted for a combination of Label Studio, a pretrained object detection model. My idea is that if any birds that I lack training data for the pretrained model will at least recognise them as a birds so that they can be labelled and added as training data later.
```shell
pip install label-studio
```
## Next:

- [ ] Identify good datasets to use for pretraining 
- [ ] Label additional data specific to my context (the view from my camera)
- [ ] Train and compare yolo models (and perhaps others depending on performance)
- [ ] Setup a Dockerfile soon so that it can be made more accessible.

[jeff-yt]: https://www.youtube.com/@jeffs_piinthesky/videos
[label-studio]: https://labelstud.io/
[roboflow]: https://app.roboflow.com/
[datatorch]: https://datatorch.io/
