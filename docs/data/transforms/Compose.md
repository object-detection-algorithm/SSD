
# Compose

* `py/ssd/data/transforms/compose.py`

一方面，级联图像预处理操作。另一方面，在每次执行完成后，去除空边界框（也就是长宽为`0`的情况）