# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:28
@file: to_percent_coords.py
@author: zj
@description: 
"""


class ToPercentCoords(object):
    def __call__(self, image, boxes=None, labels=None):
        height, width, channels = image.shape
        boxes[:, 0] /= width
        boxes[:, 2] /= width
        boxes[:, 1] /= height
        boxes[:, 3] /= height

        return image, boxes, labels
