
# variance变量

## 边界框回归

参考：[[R-CNN]边界框回归](https://blog.zhujian.life/posts/dd3aa53a.html)

已知先验框$P=(P_{x}, P_{y}, P_{w}, P_{h})$和标注框坐标$G=(G_{x}, G_{y}, G_{w}, G_{h})$，计算回归目标$t$

$$
t_{x} = (G_{x} - P_{x}) / P_{w} \\
t_{y} = (G_{y} - P_{y}) / P_{h} \\
t_{w} = \log(G_{w} / P_{w}) \\
t_{h} = \log(G_{h} / P_{h})
$$

## variance使用

不过在`SSD`算法实现中，额外增加了一个`variance`变量

$$
t_{x} = (G_{x} - P_{x}) / P_{w} /center\_variance\\
t_{y} = (G_{y} - P_{y}) / P_{h} /center\_variance\\
t_{w} = \log(G_{w} / P_{w}) /size\_variance\\
t_{h} = \log(G_{h} / P_{h}) /size\_variance
$$

其中

$$
center\_variance = 0.1 \ \ 
size\_variance=0.2
$$

参考：

[[question] What is the purpose of the variances?](https://github.com/rykov8/ssd_keras/issues/53)

[variance in priorbox layer #155](https://github.com/weiliu89/caffe/issues/155)

[Bounding Box Encoding and Decoding in Object Detection](https://leimao.github.io/blog/Bounding-Box-Encoding-Decoding/)

`variance`的作用在于对回归目标$t$进行了一次归一化操作，从而实现更好的训练精度

$$
{t}' = \frac {t - mean}{variance} = \frac {t - 0}{0.1或者0.2}
$$

`variance`表示的其实是标准方差（`standard variance`）

当然最后预测时，同样需要使用`variance`变量

$$
Pred_{x} = {t}'_{x} * center\_variance * P_{w} + P_{x}\\ 
Pred_{y} = {t}'_{y} * center\_variance * P_{h} + P_{y}\\ 
Pred_{w} = \exp ({t}'_{w} * size\_variance) * P_{w}\\
Pred_{h} = \exp ({t}'_{h} * size\_variance) * P_{h}
$$

## 具体实现

* `py/ssd/utils/box_utils.py`

```
def convert_locations_to_boxes(locations, priors, center_variance, size_variance):
。。。
def convert_boxes_to_locations(center_form_boxes, center_form_priors, center_variance, size_variance):
。。。
```