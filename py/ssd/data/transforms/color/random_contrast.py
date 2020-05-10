# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:15
@file: random_contrast.py
@author: zj
@description: 
"""

from numpy import random


class RandomContrast(object):
    def __init__(self, lower=0.5, upper=1.5):
        self.lower = lower
        self.upper = upper
        assert self.upper >= self.lower, "contrast upper must be >= lower."
        assert self.lower >= 0, "contrast lower must be non-negative."

    # expects float image
    def __call__(self, image, boxes=None, labels=None):
        if random.randint(2):
            alpha = random.uniform(self.lower, self.upper)
            image *= alpha
        return image, boxes, labels


if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    img = cv2.imread('../../../../datasets/008591.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    model = RandomContrast()

    f = plt.figure()
    rows = 2
    cols = 2

    plt.subplot(rows, cols, 1)
    plt.title('src')
    plt.imshow(img), plt.axis('off')
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            plt.subplot(rows, cols, i * cols + j + 1)
            res, _, _ = model(img.astype(np.float32))
            plt.imshow(res.astype(np.uint8)), plt.axis('off')
    plt.show()
