# Challenge 3 : Intruders detection on the port

## Problematic

The production rate on a port is a critical data of the activity and of course, stopping the containers tranfer for any reasons is not acceptable. For this challenge, we focus on the detection of intruders that can interrupt the normal operating tasks. Detecting these intruders as soon as possible could be a key feature for the service in charge of security. We define intruders as objects, animals or people not allowed to enter in the port area. The objects may be vehicles with no authorization for example. People not allowed may be identified easily if they are not equipped with personal protective equipment (helmet, yellow jacket,...)

## Objective

The objective of this challenge is to detect intruders on the port, it may be animals, unauthorized humans or vehicles. 

## Resources

We will descibe here a first version of an algortihm using Detectron2 deep learning framework to detect objects on the port. 
This has been processed to a physical twin of a port (a demonstrator @1/87th scale).  

### Database for training

Coco-annotator : 
https://github.com/jsbroks/coco-annotator/wiki/Getting-Started#Prerequisites

Link to database used to train the model at samll scale (1/87th): https://nextcloud.univ-lille.fr/index.php/s/ccMMadg76YpMHXr
This database is provided only for tests. 
For the challenge, we want to detect objects on a real environment so you can use the database of challenge 2. See the link [here, section dataset](Challenge2)

Structure of custom_coco (folder to put in the dataset directory of detectron2) : 
  - images : contains the photos dataset. Warning, all the images have not been used to train the model, you can have a look in the JSON file to know which images can be used to test the model (choose images not used during the training).
  - annotations : contain a JSON file used during the training session (see [train_custom_coco.py](Challenge3/train_custom_coco.py)). The JSON file was generated with coco-annotator.

### Dependencies for detectron2

Before using the example provided after, it is necessary to install the correct software environment on your machine. 

#### 1. CUDA installation 

As referenced here for Linux Ubuntu 20.04: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=runfile_local 

```
wget https://developer.download.nvidia.com/compute/cuda/11.4.2/local_installers/cuda_11.4.2_470.57.02_linux.run
sudo sh cuda_11.4.2_470.57.02_linux.run --toolkit --silent --override
```

#### 2. Pytorch installation:

As explained here : https://detectron2.readthedocs.io/en/latest/tutorials/install.html#requirements
via https://pytorch.org/ click install button and configure your settings in the window.  

Example with pytorch 1.9, on Linux, with pip and CUDA 11.1, the resulting command is:
```
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

#### 3. Detectron2 installation:

Get detectron2 from git repository: 
```
git clone https://github.com/facebookresearch/detectron2.git
```
From this repository in the folder Challenge3, copy the [python and jupyter notebooks](Challenge3) in the corresponding paths: 
- put *.ipynb in detectron2 root folder
- put *.py files in tools folder
- copy the dataset here in datasets

#### 4. Training with detectron

``` cd detectron2 ``` 

Then

``` python3 tools/train_custom_coco.py ```

Before launching the program make sure you are loading the good dataset and image directory at this line ``` register_coco_instances ```

#### 5. Testing with detectron

``` cd detectron2 ```

Then

``` python3 tools/test_custom_coco.py ```

You should have a result like this : ![result](https://i.imgur.com/wHownzJ.jpg)
