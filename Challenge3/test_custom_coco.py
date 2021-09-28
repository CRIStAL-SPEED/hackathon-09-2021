from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultPredictor, DefaultTrainer
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.utils.visualizer import ColorMode
import cv2
import random
import numpy as np
import os
import time

DETECTRON2_ROOT = "/home/user"

register_coco_instances("Speed", {}, DETECTRON2_ROOT + "/detectron2/datasets/custom_coco/annotations/new_speed-18.json", "/home/cristal/detectron2/datasets/custom_coco/images")

img_path = DETECTRON2_ROOT + "/Images/img_speed/test_img/container_5.JPG"

Speed_metadata = MetadataCatalog.get("Speed")
dataset_dicts = DatasetCatalog.get("Speed")

cfg = get_cfg()
cfg.merge_from_file(
    "configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
)

cfg.MODEL.WEIGHTS = DETECTRON2_ROOT + "/detectron2/output/model_final.pth"
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 5  # 3 classes (Comforme, NonComforme, Imature)
cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
predictor = DefaultPredictor(cfg)

im = cv2.imread(img_path)
outputs = predictor(im)
v = Visualizer(im[:, :, ::-1],
               metadata=Speed_metadata, 
               scale=0.8, 
               instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
img = v.get_image()[:, :, ::-1]
print(img.shape)
cv2.imshow("test",  cv2.resize(img,  ( int( img.shape[0] /2), int(img.shape[1] /2)) ) )

times = []
for i in range(20):
    start_time = time.time()
    outputs = predictor(im)
    delta = time.time() - start_time
    times.append(delta)
mean_delta = np.array(times).mean()
fps = 1 / mean_delta
print("Average(sec):{:.2f},fps:{:.2f}".format(mean_delta, fps))

#(this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)  
#closing all open windows  
cv2.destroyAllWindows()
