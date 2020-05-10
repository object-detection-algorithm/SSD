# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:16
@file: random_hue.py
@author: zj
@description: 
"""

from numpy import random


class RandomHue(object):
    def __init__(self, delta=18.0):
        assert delta >= 0.0 and delta <= 360.0
        self.delta = delta

    def __call__(self, image, boxes=None, labels=None):
        if random.randint(2):
            image[:, :, 0] += random.uniform(-self.delta, self.delta)
            image[:, :, 0][image[:, :, 0] > 360.0] -= 360.0
            image[:, :, 0][image[:, :, 0] < 0.0] += 360.0
        return image, boxes, labels


if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    img = cv2.imread('../../../../datasets/003123.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    model = RandomHue()

    f = plt.figure()
    rows = 2
    cols = 2

    plt.subplot(rows, cols, 1)
    plt.title('src')
    plt.imshow(img), plt.axis('off')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            plt.subplot(rows, cols, i * cols + j + 1)
            res, _, _ = model(img.astype(np.float32))
            res = cv2.cvtColor(res.astype(np.uint8), cv2.COLOR_HSV2RGB)
            plt.imshow(res), plt.axis('off')
    plt.show()
