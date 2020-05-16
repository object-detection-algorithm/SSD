
# Hard Negative Mining

在单个图像的先验框中，属于负样本（背景类别）的数目远远大于属于正样本的数目，所以论文通过`HNM`的方式进一步降低负样本的比例

## 实现策略

* 给定正负样本比率$a=\frac {1}{3}$
* 计算正样本数目$N_{p}$，计算保留的负样本数目$N_{n}=3\times N_{p}$
* 计算预测得到的边界框的置信度损失
* 根据背景类别的置信度损失对负样本预测框从大到小排序，保留前$N_{n}$个

## 具体实现

* `py/ssd/utils/box_utils.py`

```
def hard_negative_mining(loss, labels, neg_pos_ratio):
。。。
```