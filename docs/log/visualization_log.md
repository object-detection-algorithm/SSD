
# 可视化日志

参考：

[[PyTorch]Tensorboard可视化实现](https://blog.zhujian.life/posts/eb6f2b71.html)

[[PyTorch]Tensorboard使用实践](https://blog.zhujian.life/posts/f793688d.html)

使用`TensorboardX`进行训练过程可视化，记录了训练过程中**损失值**和**学习率**的变化，并且记录每个阶段的**测试结果（AP）**

新建了一个`MetricLogger`类，用于平滑损失值，预防单个极大损失值影响损失值可视化

## 相关文件

* `py/ssd/engine/trainer.py`
* `py/ssd/utils/metric_logger.py`