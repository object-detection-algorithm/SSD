# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:27
@file: expand.py
@author: zj
@description: 
"""

from numpy import random
import numpy as np


class Expand(object):
    def __init__(self, mean):
        self.mean = mean

    def __call__(self, image, boxes, labels):
        if random.randint(2):
            return image, boxes, labels

        height, width, depth = image.shape
        ratio = random.uniform(1, 4)
        left = random.uniform(0, width * ratio - width)
        top = random.uniform(0, height * ratio - height)

        expand_image = np.zeros(
            (int(height * ratio), int(width * ratio), depth),
            dtype=image.dtype)
        expand_image[:, :, :] = self.mean
        expand_image[int(top):int(top + height),
        int(left):int(left + width)] = image
        image = expand_image

        boxes = boxes.copy()
        boxes[:, :2] += (int(left), int(top))
        boxes[:, 2:] += (int(left), int(top))

        return image, boxes, labels


if __name__ == '__main__':
    import cv2
    import numpy as np
    import torch
    from ssd.config import cfg

    img = cv2.imread('/home/zj/test/TEST/data/003123.jpg').astype(np.float32)
    cv2.imshow('img', img.astype(np.uint8))

    model = Expand(cfg.INPUT.PIXEL_MEAN)
    print(model)

    outputs, _, _ = model(img, None, None)

    outputs = outputs.astype(np.uint8)
    cv2.imshow('out', outputs)
    cv2.waitKey(0)
