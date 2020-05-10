# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:14
@file: convert_from_ints.py
@author: zj
@description: 
"""

import numpy as np


class ConvertFromInts(object):
    def __call__(self, image, boxes=None, labels=None):
        return image.astype(np.float32), boxes, labels
