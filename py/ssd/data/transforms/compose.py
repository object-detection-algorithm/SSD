# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:18
@file: compose.py
@author: zj
@description: 
"""

import numpy as np


def remove_empty_boxes(boxes, labels):
    """Removes bounding boxes of W or H equal to 0 and its labels

    Args:
        boxes   (ndarray): NP Array with bounding boxes as lines
                           * BBOX[x1, y1, x2, y2]
        labels  (labels): Corresponding labels with boxes

    Returns:
        ndarray: Valid bounding boxes
        ndarray: Corresponding labels
    """
    del_boxes = []
    for idx, box in enumerate(boxes):
        if box[0] == box[2] or box[1] == box[3]:
            del_boxes.append(idx)

    return np.delete(boxes, del_boxes, 0), np.delete(labels, del_boxes)


class Compose(object):
    """Composes several augmentations together.
    Args:
        transforms (List[Transform]): list of transforms to compose.
    Example:
        >>> augmentations.Compose([
        >>>     transforms.CenterCrop(10),
        >>>     transforms.ToTensor(),
        >>> ])
    """

    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, img, boxes=None, labels=None):
        for t in self.transforms:
            img, boxes, labels = t(img, boxes, labels)
            if boxes is not None:
                boxes, labels = remove_empty_boxes(boxes, labels)
        return img, boxes, labels
