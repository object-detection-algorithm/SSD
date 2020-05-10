# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:29
@file: subtract_means.py
@author: zj
@description: 
"""

import numpy as np


class SubtractMeans(object):
    def __init__(self, mean):
        self.mean = np.array(mean, dtype=np.float32)

    def __call__(self, image, boxes=None, labels=None):
        image = image.astype(np.float32)
        image -= self.mean
        return image.astype(np.float32), boxes, labels
