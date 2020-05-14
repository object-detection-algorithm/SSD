
# 文本日志

参考：

[python logging - 初级](https://blog.csdn.net/u012005313/article/details/51581442)

[python logging - 高级](https://blog.csdn.net/u012005313/article/details/51588317)

在`logger.py`的函数`setup_logger`中定义了一个日志记录器，同时打印日志到**命令行窗口**和**文本文件**。同时在训练过程中可以新建`logging`对象，打印训练/测试过程

## 相关文件

* `py/ssd/utils/logger.py`