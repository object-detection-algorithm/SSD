# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:52
@file: ssd_target_transform.py
@author: zj
@description: 
"""

import torch
import numpy as np
from ssd.utils import box_utils


class SSDTargetTransform:
    def __init__(self, center_form_priors, center_variance, size_variance, iou_threshold):
        self.center_form_priors = center_form_priors
        self.corner_form_priors = box_utils.center_form_to_corner_form(center_form_priors)
        self.center_variance = center_variance
        self.size_variance = size_variance
        self.iou_threshold = iou_threshold

    def __call__(self, gt_boxes, gt_labels):
        if type(gt_boxes) is np.ndarray:
            gt_boxes = torch.from_numpy(gt_boxes)
        if type(gt_labels) is np.ndarray:
            gt_labels = torch.from_numpy(gt_labels)
        # boxes: [num_priors, 4] 每个先验框对应的标注框坐标
        # labels: [num_priors] 每个先验框对应标签
        boxes, labels = box_utils.assign_priors(gt_boxes, gt_labels, self.corner_form_priors, self.iou_threshold)
        boxes = box_utils.corner_form_to_center_form(boxes)
        locations = box_utils.convert_boxes_to_locations(boxes, self.center_form_priors, self.center_variance,
                                                         self.size_variance)

        return locations, labels
