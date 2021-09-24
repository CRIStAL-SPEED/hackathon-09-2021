# Challenge 3 : Intruders detection on the port

## Objectives

TODO : complete

## Resources

We will descibe here a first version of algortihm using Detectron2 deep learning framework to detect objects on the port. 
This has been processed to a physical twin of a port (a demonstrator @1/87th scale).  

### Database for training

Coco-annotator : 
TODO : describe the tool or put links to tutorials, manuals

Link to database: 
Structure: 
  - images
  - annotations

### Dependencies for detectron2

Before using the example provided after, it is necessary to install the correct software environment on your machine. 

1. CUDA installation 

```
sudo sh cuda_11.1.0_455.23.05_linux.run --toolkit --silent --override
```

2. Pytorch installation:

As explained here : https://detectron2.readthedocs.io/en/latest/tutorials/install.html#requirements
via https://pytorch.org/ click install button and configure your settings in the window.  

Example with pytorch 1.9, on Linux, with pip and CUDA 11.1, the resulting command is:
```
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

3. Detectron2 installation:

Get detectron2 from git repository: 
```
git clone https://github.com/facebookresearch/detectron2.git
```
put *.ipynb in detectron2 root folder
put *.py files in tools folder
copy the dataset here in datasets


4. Training with detectron

``` cd detectron2 ``` 
Then
``` python3 tools/train_custom_coco.py ```
Before launching the program make sure you are loading the good dataset and image directory at this line ``` register_coco_instances ```
5. Testing with detectron
``` cd detectron2 ```
Then
``` python3 tools/test_custom_coco.py ```
You should have a result like this : ![result](https://i.imgur.com/wHownzJ.jpg)
