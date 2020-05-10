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


if __name__ == '__main__':
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    img = cv2.imread('../../../datasets/003123.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = np.array([[33, 44, 123, 210]])
    labels = np.array([3])

    model = RandomMirror()

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
            res, res_boxes, _ = model(img.astype(np.float32), boxes, labels)
            plt.imshow(res.astype(np.uint8)), plt.axis('off')
            print('{}-{} : {} - {}'.format(i, j, res_boxes, labels))
    plt.show()
