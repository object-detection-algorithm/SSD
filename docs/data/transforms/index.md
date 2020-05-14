
# 图像预处理

## 预处理操作

对于目标检测算法，常用以下预处理操作进行数据扩充

1. 格式转换
      1. `ConvertFromInts`
      2. `ToPercentCoords`
      3. `ToTensor`
2. 光度扭曲：`PhotometricDistort`
3. 图像扩展：`Expand`
4. 随机裁剪：`RandomSampleCrop`
5. 随机镜像：`RandomMirror`
6. 图像缩放：`Resize`
7. 数据标准化：`SubtractMeans`

## 构建转换器

定义函数`build_transforms`，调用上述预处理操作

* `py/ssd/data/transforms/build.py`

## `__init__.py`

所有图像预处理操作可通过模块文件调用

* `py/ssd/data/transforms/__init__.py`