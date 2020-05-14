
# 数据集路径解析

定义了数据集路径解析类`DatasetCatalog`

默认保存路径为当前路径下的`datasets`文件夹，可设置环境变量进行调整

* 对于`voc`数据集，设置环境变量`VOC_ROOT`
* 对于`coco`数据集，设置环境变量`COCO_ROOT`

## 相关文件

* `py/ssd/data/datasets/path_catalog.py`