# Challenge 2 : Detection of risky situations on port

## Objectives

The goal of this challenge is to analyze video streams or images to detect risky situations on the port. 

## Dataset 

In this challenge, several danger situation datasets collected in port are provided. The Danger Crossing is a mandatory dataset, and you must choose at least one more from the rest datasets. The dataset is available at https://nextcloud.univ-lille.fr/index.php/s/s6Ha4zNPq2T4MkS and contains:
 * Danger Crossing: Detect the vehicle at the crossing to avoid traffic accidents.
 * Operation on Train： Detect the container operation on train.
 * Operators on Track/Dock: Recognize operators working on track/dock.
 * Train: Recognize train moving, operating and approaching in port.

Alternative download link: https://filesender.renater.fr/?s=download&token=091e42b2-0086-4acc-a90f-37eef171ac48

All files and links are protected with password: Hacka7honSp33d

## Python environment

It will be better to create a new Python environment to train the object detection model. Duo to the fact that sometimes the new Python packages will lead to dependency conflicts. The following commands show how to use Python environment in Anaconda:

```
 # Create environment
   conda create -n Hackathon
   
 # Check the environment
   conda info --env
   
 # Delete the environment (be careful)
   conda remove -n Hackathon --all
   
 # Active environment
   conda activate Hackathon
   
 # Exit environment
   conda deactivate
```

## Technical description 

We recommend YOLOv5 as the object detection architecture and you can also select the method you want. The following link shows how to build your own object detection model based on YOLOv5.

https://github.com/ultralytics/yolov5

The following contents are some suggestions when you follow the YOLOv5 guidance.

### Create Labels
The online tool https://makesense.ai is recommended to create labels of objects. No additional software is required to do the annotation.

Notice: You must create labels corresponding to your dataset (the number of the classes), and export annotations in YOLO format.

### Organize Directories
The dataset should follow the structure below:

```
  |----yolov5-master
  |----your dataset(Hackathon)
       |---train
           |---images      
           |---labels        
       |---val     
           |---images         
           |---labels
```
