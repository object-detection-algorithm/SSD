
# 检查点读写

* 定义：`py/ssd/utils/checkpoint.py`
* 声明：`py/train.py`
* 使用：`py/ssd/engine/trainer.py`

## 保存

每次保存两个文件，一个用于保存训练参数；另一个固定命名为`last_checkpoint.txt`，里面给出了当前保存的模型路径

```
$ cat last_checkpoint.txt 
outputs/vgg_ssd300_voc0712/model_final.pth
```

保存以下训练参数：

1. 模型参数
2. 优化器参数
3. 学习率调度器参数
4. 已迭代次数：`arguments = {"iteration": 0}`

## 加载

可重新启动之前被打断的训练过程，通过检索文件`last_checkpoint.txt`找到最新的训练结果，重新开始训练

```
2020-05-11 15:34:19,907 SSD.trainer INFO: Loading checkpoint from outputs/vgg_ssd300_voc0712/model_002500.pth
2020-05-11 15:34:19,988 SSD.trainer INFO: Loading optimizer from outputs/vgg_ssd300_voc0712/model_002500.pth
2020-05-11 15:34:20,033 SSD.trainer INFO: Loading scheduler from outputs/vgg_ssd300_voc0712/model_002500.pth
2020-05-11 15:34:20,061 SSD.trainer INFO: Start training ...
2020-05-11 15:34:32,532 SSD.trainer INFO: iter: 002510, lr: 0.00100, total_loss: 4.547 (4.547), reg_loss: 1.361 (1.361), cls_loss: 3.186 (3.186), time: 1.241 (1.241), eta: 1 day, 16:29:26, mem: 8391M
2020-05-11 15:34:38,424 SSD.trainer INFO: iter: 002520, lr: 0.00100, total_loss: 4.717 (4.632), reg_loss: 1.373 (1.367), cls_loss: 3.344 (3.265), time: 0.589 (0.915), eta: 1 day, 5:51:26, mem: 8391M
2020-05-11 15:34:44,299 SSD.trainer INFO: iter: 002530, lr: 0.00100, total_loss: 4.998 (4.754), reg_loss: 1.488 (1.407), cls_loss: 3.510 (3.347), time: 0.587 (0.806), eta: 1 day, 2:17:34, mem: 8391M
```