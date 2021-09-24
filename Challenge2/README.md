# Challenge 2 : Detection of risky situations on port

## Objectives

The goal of this challenge is to analyse video streams or images to detect risky situations on the port. 

## Dataset 

In this challenge, several danger situation datasets collected in port are provided. The Danger Crossing is a mandatory dataset, and you must choose at least one more from the rest datasets. The dataset () contains:
 * Danger Crossing: Detect the vehicle at the crossing to avoid traffic accidents.
 * Operation on Train： Detect the container operation on train.
 * Operators on Track/Dock: Recognize operators working on track/dock.
 * Train: Recognize train moving, operating and approaching in port.

## Technical description 

We recommend YOLOv5 as the object detection architecture and you can also select the method you want. The following link shows how to build your own object detection model based on YOLOv5.

https://github.com/ultralytics/yolov5

It will be better to create a new Python environment to train the object detection model. Duo to the fact that sometimes the new Python packages will lead to dependency conflicts. The following commands show how to use Python environment:

 * Create environment
conda create -n Hackathon
 * Check the environment
conda info --env
 * Delete the environment (be careful)
conda remove -n Hackathon --all
 * Active environment
conda activate Hackathon
 * Exit environment
conda deactivate

