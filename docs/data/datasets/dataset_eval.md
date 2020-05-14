
# 数据集评估

## voc评估

* `py/ssd/data/datasets/evaluation/voc/build.py`
* `py/ssd/data/datasets/evaluation/voc/eval_detection_voc.py`

评估`VOC`数据集目标检测的`mAP`

## coco评估

* `py/ssd/data/datasets/evaluation/coco`

调用了`pycocotools`库的评估函数`COCOeval`

## 封装评估函数

* `py/ssd/data/datasets/evaluation/build.py`

定义函数`evaluate`，根据数据集的类型调用不同的评估函数