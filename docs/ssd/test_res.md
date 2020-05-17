
# 测试日志

```
$ python test.py --config-file configs/vgg_ssd300_voc0712.yaml 
2020-05-17 20:17:43,458 SSD INFO: Using 1 GPUs
2020-05-17 20:17:43,458 SSD INFO: Namespace(ckpt=None, config_file='configs/vgg_ssd300_voc0712.yaml', local_rank=0, opts=[], output_dir='eval_results')
2020-05-17 20:17:43,458 SSD INFO: Loaded configuration file configs/vgg_ssd300_voc0712.yaml
2020-05-17 20:17:43,458 SSD INFO: 
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
2020-05-17 20:17:43,458 SSD INFO: Running with config:
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
2020-05-17 20:17:44,736 SSD.inference INFO: Loading checkpoint from outputs/vgg_ssd300_voc0712/model_final.pth
2020-05-17 20:17:44,834 SSD.inference INFO: Evaluating voc_2007_test dataset(4952 images):
  0%|                                                                                                                                                                                      | 0/496 [00:00<?, ?it/s]/opt/conda/conda-bld/pytorch_1587428266983/work/torch/csrc/utils/python_arg_parser.cpp:756: UserWarning: This overload of nonzero is deprecated:
	nonzero(Tensor input, *, Tensor out)
Consider using one of the following signatures instead:
	nonzero(Tensor input, *, bool as_tuple)
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 496/496 [00:41<00:00, 11.90it/s]
2020-05-17 20:18:28,805 SSD.inference INFO: mAP: 0.7740
aeroplane       : 0.8113
bicycle         : 0.8322
bird            : 0.7476
boat            : 0.7160
bottle          : 0.5331
bus             : 0.8619
car             : 0.8669
cat             : 0.8781
chair           : 0.6243
cow             : 0.8297
diningtable     : 0.7607
dog             : 0.8393
horse           : 0.8634
motorbike       : 0.8420
person          : 0.7972
pottedplant     : 0.5075
sheep           : 0.7754
sofa            : 0.7775
train           : 0.8548
tvmonitor       : 0.7622
```