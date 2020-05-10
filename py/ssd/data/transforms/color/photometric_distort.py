# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:14
@file: photometric_distort.py
@author: zj
@description: 
"""

from numpy import random

import ssd.data.transforms.color as color
import ssd.data.transforms as transforms


class PhotometricDistort(object):
    def __init__(self):
        self.pd = [
            color.RandomContrast(),  # RGB
            color.ConvertColor(current="RGB", transform='HSV'),  # HSV
            color.RandomSaturation(),  # HSV
            color.RandomHue(),  # HSV
            color.ConvertColor(current='HSV', transform='RGB'),  # RGB
            color.RandomContrast()  # RGB
        ]
        self.rand_brightness = color.RandomBrightness()
        self.rand_light_noise = color.RandomLightingNoise()

    def __call__(self, image, boxes, labels):
        im = image.copy()
        im, boxes, labels = self.rand_brightness(im, boxes, labels)
        if random.randint(2):
            distort = transforms.Compose(self.pd[:-1])
        else:
            distort = transforms.Compose(self.pd[1:])
        im, boxes, labels = distort(im, boxes, labels)
        return self.rand_light_noise(im, boxes, labels)


if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    img = cv2.imread('../../../../datasets/008591.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    model = PhotometricDistort()

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
            res, _, _ = model(img.astype(np.float32), None, None)
            plt.imshow(res.astype(np.uint8)), plt.axis('off')
    plt.show()
