
# 梯度更新

使用`PyTorch`提供的优化器

## 封装

* `py/ssd/optim/build.py`

定义了一个辅助函数`make_optimizer`，可根据配置要求生成优化器

```
def make_optimizer(cfg, model, lr=None):
    lr = cfg.SOLVER.BASE_LR if lr is None else lr
    return torch.optim.SGD(model.parameters(), lr=lr, momentum=cfg.SOLVER.MOMENTUM,
                           weight_decay=cfg.SOLVER.WEIGHT_DECAY)
```