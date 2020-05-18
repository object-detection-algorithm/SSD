
# 命令行操作

执行训练、测试、检测命令如下

## 相关参数

* 数据集：`PASCAL VOC 07+12`
* 基础网络：`VGG16`
* 输入大小：$300\times 300$
* `GPU: Nvidia GTX 1080Ti`

## 训练

```
# 单GPU训练
$ python train.py --config-file configs/vgg_ssd300_voc0712.yaml
```

## 测试

```
# 单GPU测试
python test.py --config-file configs/vgg_ssd300_voc0712.yaml
```

## 检测

```
$ python demo.py --config-file configs/vgg_ssd300_voc0712.yaml --images_dir demo --ckpt outputs/vgg_ssd300_voc0712/model_final.pth
```