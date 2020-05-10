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
    import matplotlib.pyplot as plt
    from ssd.config import cfg

    img = cv2.imread('../../../datasets/008591.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = np.array([[33, 44, 123, 210]])

    model = Expand(cfg.INPUT.PIXEL_MEAN)

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
            res, res_boxes, _ = model(img.astype(np.float32), boxes, None)
            plt.imshow(res.astype(np.uint8)), plt.axis('off')
            print('{}-{} : {}'.format(i, j, res_boxes))
    plt.show()
