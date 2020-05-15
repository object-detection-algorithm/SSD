
# 检测器

对于目标检测训练框架而言，检测器模块集成了以下几个部分：

1. 特征提取
2. 分类/检测
3. 损失函数计算
      1. 定位损失
      2. 置信度损失

## 注册器

### 定义

定义了一个注册器`Registry`，其继承自`dict`

* `py/ssd/utils/registry.py`

新增了一个`registry()`函数，用于保存模块名和对应的模块对象

### 声明

在`py/ssd/models/registry.py`中新建了`3`个`Registry`对象，分别保存`BACKBONE、BOX_HEAD、BOX_PREDICTOR`

### 注册

使用装饰器的方式注册相应的模块，比如

* `py/ssd/models/backbone/vgg.py`
* `py/ssd/models/box_head/box_head.py`
* `py/ssd/models/box_head/box_predictor.py`

### 使用

每个`Registry`对象都是一个`dict`，根据配置文件输入相应的键和对应函数的参数即可

* `py/ssd/models/backbone/build.py`
* `py/ssd/moels/box_head/build.py`