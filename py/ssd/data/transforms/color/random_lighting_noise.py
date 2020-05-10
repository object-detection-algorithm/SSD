# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:17
@file: random_lighting_noise.py
@author: zj
@description: 
"""

from numpy import random
import ssd.data.transforms.color as color


class RandomLightingNoise(object):
    def __init__(self):
        self.perms = ((0, 1, 2), (0, 2, 1),
                      (1, 0, 2), (1, 2, 0),
                      (2, 0, 1), (2, 1, 0))

    def __call__(self, image, boxes=None, labels=None):
        if random.randint(2):
            swap = self.perms[random.randint(len(self.perms))]
            shuffle = color.SwapChannels(swap)  # shuffle channels
            image = shuffle(image)
        return image, boxes, labels


if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    img = cv2.imread('../../../../datasets/008591.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    model = RandomLightingNoise()

    f = plt.figure()
    rows = 3
    cols = 3

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
