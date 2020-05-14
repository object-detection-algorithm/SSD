
# 学习率调度

## 自定义

* `py/ssd/optim/lr_scheduler/`

可以调用`PyTorch`提供的学习率调度器，对于自定义的学习率调度器放置于`lr_scheduler`目录下

## 封装

* `py/ssd/optim/build.py`

定义辅助函数`make_lr_scheduler`，根据配置要求生成优化器

```
def make_lr_scheduler(cfg, optimizer, milestones=None):
    return WarmupMultiStepLR(optimizer=optimizer,
                             milestones=cfg.SOLVER.LR_STEPS if milestones is None else milestones,
                             gamma=cfg.SOLVER.GAMMA,
                             warmup_factor=cfg.SOLVER.WARMUP_FACTOR,
                             warmup_iters=cfg.SOLVER.WARMUP_ITERS)
```