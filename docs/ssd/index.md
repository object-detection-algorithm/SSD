
# SSD

[SSD(Single Shot MultiBox Detector)](https://arxiv.org/abs/1512.02325)是一个`One-Stage`目标检测算法。其相对于之前的检测算法（`YOLOv1、Faster RCNN`）而言，关键的区别在于

1. 使用多个**不同尺度**的特征图进行边界框预测
2. 定义了一组**多个尺度、多个长宽比**的先验框
2. 利用**小卷积滤波器**计算特征图，以得到先验框偏移和分类成绩

## 章节安排

分两部分研究`SSD`算法：

1. 原理解析
2. 具体实现

## 相关阅读

* [【SSD算法】史上最全代码解析-核心篇](https://zhuanlan.zhihu.com/p/79854543?from_voters_page=true)
* [目标检测|SSD原理与实现](https://zhuanlan.zhihu.com/p/33544892)