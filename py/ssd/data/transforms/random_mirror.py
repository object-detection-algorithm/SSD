# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:26
@file: random_mirror.py
@author: zj
@description: 
"""

from numpy import random


class RandomMirror(object):
    def __call__(self, image, boxes, classes):
        _, width, _ = image.shape
        if random.randint(2):
            image = image[:, ::-1]
            boxes = boxes.copy()
            boxes[:, 0::2] = width - boxes[:, 2::-2]
        return image, boxes, classes
