
# 损失函数

分为两个部分：

1. 定位损失（`localization loss`）
2. 置信度损失（`confidence loss`）

## 定位损失

$$
L_{loc}(x, l, g) = \sum_{i\in Pos}^{N} \sum_{m\in \{cx, cy, w, h\}} x_{i,j}^{k} smooth_{L1}(L_{i}^{m} - \hat{g}_{j}^{m})
$$

$$
\hat{g}_{j}^{cx} = (g_{j}^{cx} - d_{i}^{cx}) / d_{i}^{w}\ \ \ 
\hat{g}_{j}^{cy} = (g_{j}^{cy} - d_{i}^{cy}) / d_{i}^{h}\\ 
\hat{g}_{j}^{w} = \log (\frac {g_{j}^{w}}{d_{i}^{w}})\ \ \ 
\hat{g}_{j}^{h} = \log (\frac {g_{j}^{h}}{d_{i}^{h}})
$$

定位损失计算的是预测框$l$和标注框$g$之间的$Smooth\ L1$损失。其中，

* $N$表示匹配的先验框的数目
* $x_{i,j}^{p}=\{1, 0\}$：指示器，表示第$i$个先验框是否和类别$p$的第$j$个标注框匹配
* $\{cx, cy, w, h\}$表示先验框$d$的预测偏移

## 置信度损失

置信度损失计算的是交叉熵损失

$$
L_{conf}(x, c) = -\sum_{i\in Pos}^{N} x_{ij}^{p} \log (\hat{c}_{i}^{p}) - \sum_{i\in N_{eg}} \log (\hat{c}_{i}^{0})
$$

其中

$$
\hat{c}_{i}^{p} = \frac {exp(c_{i}^{p})}{\sum_{ p} \exp(c_{i}^{p})}
$$

## 整体损失

整体的损失函数是定位损失和置信度损失的加权求和

$$
L(x, y, l, g) = \frac {1}{N} (L_{conf}(x, c) + \alpha L_{loc}(x, l, g))
$$

其中，$N$是指和标注框匹配的先验框的个数。如果$N=0$，那么设置损失值为$0$

*加权因子$\alpha$通过交叉验证设置为$1$*

## 实现文件

* `py/ssd/models/box_head/loss.py`