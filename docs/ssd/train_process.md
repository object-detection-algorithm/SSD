
# 训练流程

* `py/train.py`

## 训练参数

* 数据集
    * 训练：`PASCAL VOC 07+12 trainval`
    * 测试：`PASCAL VOC 07 test`
* 数据
    * 输入大小：`300`
    * 批量大小：`32`
* 优化器：`SGD`
    * `lr: 1e-3`
    * `weight_decay: 5e-4`
    * 动量：`0.9`
* 衰减器：`WarmupMultiStepLR`（自定义，`warmup + stepLR`）
    * 起始学习率（`warmup_factor`）：`1/3.0`
    * `warmup`迭代次数（`warmup_iters`）：`500`
    * 衰减时刻：第`8`万次和第`10`万次迭代
    * 迭代总数：`12`万次
* 模型
    * 基础网络：`VGG16`
    * 损失函数：`SmoothL1 Loss + Softmax Loss`
* 目标检测：
    * 中心坐标的标准方差（`CENTER_VARIANCE`）：`0.1`
    * 长宽的标准方差（`SIZE_VARIANCE`）：`0.2`

## 训练流程

* 批量载入图像
* 图像预处理
    * 针对图像进行操作
    * 针对边界框进行操作：计算先验框；匹配先验框和标注框，转换边界框坐标格式
* 模型计算
* 损失计算
* 梯度更新
* 学习率更新