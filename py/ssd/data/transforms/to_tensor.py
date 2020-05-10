# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:29
@file: to_tensor.py
@author: zj
@description: 
"""

import torch
import numpy as np


class ToTensor(object):
    def __call__(self, cvimage, boxes=None, labels=None):
        return torch.from_numpy(cvimage.astype(np.float32)).permute(2, 0, 1), boxes, labels
