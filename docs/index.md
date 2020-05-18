# SSD

在`Github`上找到一个`SSD`目标检测算法实现 - [lufficc/SSD](https://github.com/lufficc/SSD)，这个工程不仅完美的实现了`SSD`算法，而且整体结构清晰，具有高可扩展性。所以新建了一个仓库，一方面是学习`SSD`算法，另一方面是研究整个训练框架，以便于其他算法的实现

## 训练框架

整个目标检测训练框架可分为以下几个部分：

1. 配置模块
2. 日志模块
3. 数据模块
4. 检测器模块
5. 优化器模块
6. 辅助模块

![](./imgs/arch.png)

## SSD算法

* 引言
* 原理解析
    * 基础网络
    * 先验框
    * 匹配策略
    * 损失函数
    * `Hard Negative Mining`
    * `variance`变量
    * `300 vs. 512`
* 具体实现
    * 命令行操作
    * 训练
        * 训练流程
        * 训练日志
    * 测试
        * 测试流程
        * 测试日志
    * 使用
        * 使用示例
        * 使用日志

## 相关文档

* [学习 SSD: Single Shot MultiBox Detector](https://blog.zhujian.life/posts/4adff177.html)
* [目标检测训练框架](https://blog.zhujian.life/posts/902134ce.html)