import detectron2
from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode
from detectron2.data import DatasetCatalog
from detectron2 import data
from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg
import os
import cv2
import random
import time
import numpy as np
import torch, gc

#torch.set_grad_enabled(False)
torch.cuda.empty_cache()

DETECTRON2_ROOT = "/home/user"

register_coco_instances("Speed", {}, DETECTRON2_ROOT + "/detectron2/datasets/custom_coco/annotations/new_speed-18.json", DETECTRON2_ROOT + "/detectron2/datasets/custom_coco/images")

Speed_metadata = MetadataCatalog.get("Speed")
dataset_dicts = DatasetCatalog.get("Speed")
i = 0
for d in random.sample(dataset_dicts, 1):
    i = i +1
    img = cv2.imread(d["file_name"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=Speed_metadata, scale=0.5)
    vis = visualizer.draw_dataset_dict(d)
    cv2.imshow("test" + str(i), vis.get_image()[:, :, ::-1])


cfg = get_cfg()
cfg.merge_from_file(
    "configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
)

cfg.DATASETS.TRAIN = ("Speed",)
cfg.DATASETS.TEST = ()  # no metrics implemented for this dataset
cfg.DATALOADER.NUM_WORKERS = 2
cfg.MODEL.WEIGHTS = "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"  # initialize from model zoo
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.01 * 2 / 16
cfg.SOLVER.MAX_ITER = (
    300
)  # 300 iterations seems good enough, but you can certainly train longer
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = (
    128
)  # faster, and good enough for this toy dataset
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 5  # 3 classes (train, contenaire, quad, portique)

os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
trainer = DefaultTrainer(cfg)
trainer.resume_or_load(resume=False)
trainer.train()

cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
cfg.DATASETS.TEST = ("Speed", )
predictor = DefaultPredictor(cfg)

for d in random.sample(dataset_dicts, 3): 
    i = i +1   
    im = cv2.imread(d["file_name"])
    imS = cv2.resize(im,(1920, 1080))
    outputs = predictor(imS)
    v = Visualizer(imS[:, :, ::-1],
                   metadata=Speed_metadata, 
                   scale=0.8, 
                   instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
    )
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    cv2.imshow("test" + str(i), v.get_image()[:, :, ::-1])

times = []
for i in range(20):
    start_time = time.time()
    outputs = predictor(imS)
    delta = time.time() - start_time
    times.append(delta)
mean_delta = np.array(times).mean()
fps = 1 / mean_delta
print("Average(sec):{:.2f},fps:{:.2f}".format(mean_delta, fps))

#(this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)  
#closing all open windows  
cv2.destroyAllWindows()
