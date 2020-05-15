
# 匹配策略

在训练过程中，需要先确定先验框对应于哪个标注框

## 匹配步骤

实现步骤如下：

* 首先计算每个标注框和先验框的`IoU`
    * 找出对于每个先验框而言，对应`IoU`最大的标注框 - `best_target_per_prior`
    * 找出对于每个标注框而言，对应`IoU`最大的先验框 - `best_prior_per_target`
* 从标注框（`gt_boxes`）和标签（`gt_labels`）中提取出每个先验框对应的标注框坐标和类别
* 同时为了确保每个标注框都有一个对应的先验框，设置对应先验框`IoU`大于阈值
* 判断每个先验框的最高`IoU`是否超过阈值（`0.5`）。如果没有，则设置该标签为`0`（背景类别）

## 具体实现

* `py/ssd/utils/box_utils.py`

```
def assign_priors(gt_boxes, gt_labels, corner_form_priors,
                  iou_threshold):
    """Assign ground truth boxes and targets to priors.

    Args:
        gt_boxes (num_targets, 4): ground truth boxes.
        gt_labels (num_targets): labels of targets.
        priors (num_priors, 4): corner form priors
    Returns:
        boxes (num_priors, 4): real values for priors.
        labels (num_priros): labels for priors.
    """
    # size: [num_priors, num_targets]
    # 每行表示单个先验框与各个标注框的IoU
    # 每列表示单个标注框与各个先验框的IoU
    ious = iou_of(gt_boxes.unsqueeze(0), corner_form_priors.unsqueeze(1))
    # size: [num_priors]
    # best_target_per_prior：每个先验框计算得到的最高IoU
    # best_target_per_prior_index：每个先验框对应最高IoU的标注框下标
    best_target_per_prior, best_target_per_prior_index = ious.max(1)
    # size: [num_targets]
    # best_prior_per_target：每个标注框计算得到的最高IoU
    # best_prior_per_target_index：每个标注框对应最高IoU的先验框下标
    best_prior_per_target, best_prior_per_target_index = ious.max(0)

    # 再一次确保标注框与最高IoU的先验框匹配
    for target_index, prior_index in enumerate(best_prior_per_target_index):
        best_target_per_prior_index[prior_index] = target_index

    # size: [num_priors]
    # 得到每个先验框对应标注框的标签/类别
    labels = gt_labels[best_target_per_prior_index]
    # size: [num_priors, 4]
    # 得到每个先验框对应标注框的坐标
    boxes = gt_boxes[best_target_per_prior_index]

    # 2.0 is used to make sure every target has a prior assigned
    # 确保每个标注框对应IoU最高的先验框的阈值大于iou_threshold
    best_target_per_prior.index_fill_(0, best_prior_per_target_index, 2)
    # IoU小于iou_threshold的先验框设置为背景类别
    labels[best_target_per_prior < iou_threshold] = 0  # the backgournd id

    return boxes, labels
```