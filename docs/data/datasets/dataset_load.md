
# 数据集加载

## 定义数据集

* `py/ssd/data/datasets/voc.py`
* `py/ssd/data/datasets/coco.py`

为不同数据集创建相应的类，加载图像并解析相应的边界框坐标

## 加载数据集

* `py/ssd/data/datasets/build.py`

定义函数`build_dataset`，创建指定的数据集类并返回