# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:28
@file: resize.py
@author: zj
@description: 
"""

import cv2


class Resize(object):
    def __init__(self, size=300):
        self.size = size

    def __call__(self, image, boxes=None, labels=None):
        image = cv2.resize(image, (self.size,
                                   self.size))
        return image, boxes, labels
