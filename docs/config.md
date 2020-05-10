
# 配置

相关文件目录：

* `py/ssd/config`

## YAML

使用`YAML`文件保存工程的整体配置，其读取和设置参考[[yacs][pytohn]YAML文件读取](https://zj-image-processing.readthedocs.io/zh_CN/latest/python/[yacs][pytohn]YAML%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96/)

其默认设置位于

* `py/ssd/config/defaults.py`

### 数据相关

```
# 输入大小及图像均值
# -----------------------------------------------------------------------------
# INPUT
# -----------------------------------------------------------------------------
_C.INPUT = CN()
# Image size
_C.INPUT.IMAGE_SIZE = 300
# Values to be used for image normalization, RGB layout
_C.INPUT.PIXEL_MEAN = [123, 117, 104]
# 数据集
# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------
_C.DATASETS = CN()
# List of the dataset names for training, as present in paths_catalog.py
_C.DATASETS.TRAIN = ("voc_2007_trainval", "voc_2012_trainval")  # ()
# List of the dataset names for testing, as present in paths_catalog.py
_C.DATASETS.TEST = ("voc_2007_test",)  # ()
# 数据加载器
# -----------------------------------------------------------------------------
# DataLoader
# -----------------------------------------------------------------------------
_C.DATA_LOADER = CN()
# Number of data loading threads
_C.DATA_LOADER.NUM_WORKERS = 8
_C.DATA_LOADER.PIN_MEMORY = True
```

### 数据路径

定义了数据集路径解析类`DatasetCatalog`

* `py/ssd/config/path_catelog.py`

默认保存路径为当前路径下的`datasets`文件夹，可设置环境变量进行调整

* 对于`voc`数据集，设置环境变量`VOC_ROOT`
* 对于`coco`数据集，设置环境变量`COCO_ROOT`