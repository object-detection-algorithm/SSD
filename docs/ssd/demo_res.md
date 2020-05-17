
# 使用日志

测试检测结果，计算`FPS`

## 使用日志

```
$ python demo.py --config-file configs/vgg_ssd300_voc0712.yaml --images_dir demo --ckpt outputs/vgg_ssd300_voc0712/model_final.pth 
Namespace(ckpt='outputs/vgg_ssd300_voc0712/model_final.pth', config_file='configs/vgg_ssd300_voc0712.yaml', dataset_type='voc', images_dir='demo', opts=[], output_dir='demo/result', score_threshold=0.7)
Loaded configuration file configs/vgg_ssd300_voc0712.yaml

MODEL:
  NUM_CLASSES: 21
INPUT:
  IMAGE_SIZE: 300
DATASETS:
  TRAIN: ("voc_2007_trainval", "voc_2012_trainval")
  TEST: ("voc_2007_test", )
SOLVER:
  MAX_ITER: 120000
  LR_STEPS: [80000, 100000]
  GAMMA: 0.1
  BATCH_SIZE: 32
  LR: 1e-3

OUTPUT_DIR: 'outputs/vgg_ssd300_voc0712'
Running with config:
DATASETS:
  TEST: ('voc_2007_test',)
  TRAIN: ('voc_2007_trainval', 'voc_2012_trainval')
DATA_LOADER:
  NUM_WORKERS: 8
  PIN_MEMORY: True
INPUT:
  IMAGE_SIZE: 300
  PIXEL_MEAN: [123, 117, 104]
MODEL:
  BACKBONE:
    NAME: vgg
    OUT_CHANNELS: (512, 1024, 512, 256, 256, 256)
    PRETRAINED: True
  BOX_HEAD:
    NAME: SSDBoxHead
    PREDICTOR: SSDBoxPredictor
  CENTER_VARIANCE: 0.1
  DEVICE: cuda
  META_ARCHITECTURE: SSDDetector
  NEG_POS_RATIO: 3
  NUM_CLASSES: 21
  PRIORS:
    ASPECT_RATIOS: [[2], [2, 3], [2, 3], [2, 3], [2], [2]]
    BOXES_PER_LOCATION: [4, 6, 6, 6, 4, 4]
    CLIP: True
    FEATURE_MAPS: [38, 19, 10, 5, 3, 1]
    MAX_SIZES: [60, 111, 162, 213, 264, 315]
    MIN_SIZES: [30, 60, 111, 162, 213, 264]
    STRIDES: [8, 16, 32, 64, 100, 300]
  SIZE_VARIANCE: 0.2
  THRESHOLD: 0.5
OUTPUT_DIR: outputs/vgg_ssd300_voc0712
SOLVER:
  BATCH_SIZE: 32
  GAMMA: 0.1
  LR: 0.001
  LR_STEPS: [80000, 100000]
  MAX_ITER: 120000
  MOMENTUM: 0.9
  WARMUP_FACTOR: 0.3333333333333333
  WARMUP_ITERS: 500
  WEIGHT_DECAY: 0.0005
TEST:
  BATCH_SIZE: 10
  CONFIDENCE_THRESHOLD: 0.01
  MAX_PER_CLASS: -1
  MAX_PER_IMAGE: 100
  NMS_THRESHOLD: 0.45
Loaded weights from outputs/vgg_ssd300_voc0712/model_final.pth
/opt/conda/conda-bld/pytorch_1587428266983/work/torch/csrc/utils/python_arg_parser.cpp:756: UserWarning: This overload of nonzero is deprecated:
	nonzero(Tensor input, *, Tensor out)
Consider using one of the following signatures instead:
	nonzero(Tensor input, *, bool as_tuple)
(0001/0005) 004101.jpg: objects 01 | load 004ms | inference 170ms | FPS 6
(0002/0005) 000542.jpg: objects 01 | load 006ms | inference 014ms | FPS 73
(0003/0005) 003123.jpg: objects 08 | load 004ms | inference 012ms | FPS 81
(0004/0005) 000342.jpg: objects 02 | load 003ms | inference 013ms | FPS 79
(0005/0005) 008591.jpg: objects 02 | load 004ms | inference 013ms | FPS 77
```

## 分析

第一次推导时间（`inference 170ms`）大大超过后续的推导时间（`inference 014ms`）

相关文件

* `py/ssd/models/box_head/box_head.py`

第一次推导需要额外计算先验框，所以需要更多的推导时间

```
@registry.BOX_HEADS.register('SSDBoxHead')
class SSDBoxHead(nn.Module):
    def __init__(self, cfg):
        。。。
        。。。
        self.priors = None

    def _forward_test(self, cls_logits, bbox_pred):
        if self.priors is None:
            self.priors = PriorBox(self.cfg)().to(bbox_pred.device)
        。。。
        。。。
```