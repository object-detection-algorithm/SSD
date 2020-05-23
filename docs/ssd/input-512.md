
# 输入设置为512

## 调整

当使用`512`输入大小时，额外增加了一个`Conv12_2`特征图用于检测，同时设置$s_{min}=0.1$，特征层`Conv4_3`的尺度设置为`0.04`

具体修改参考：`py/configs/vgg_ssd512_voc0712.yaml`

## 训练结果

```
2020-05-23 06:14:05,597 SSD.inference INFO: mAP: 0.8036
aeroplane       : 0.8450
bicycle         : 0.8690
bird            : 0.8148
boat            : 0.7590
bottle          : 0.6156
bus             : 0.8720
car             : 0.8860
cat             : 0.8896
chair           : 0.6619
cow             : 0.8651
diningtable     : 0.7361
dog             : 0.8686
horse           : 0.8757
motorbike       : 0.8545
person          : 0.8226
pottedplant     : 0.5503
sheep           : 0.8234
sofa            : 0.7870
train           : 0.8748
tvmonitor       : 0.8013
```