# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午9:00
@file: test_data.py
@author: zj
@description: 
"""

from ssd.data.build import make_data_loader
from ssd.config import cfg


def train_data():
    max_iter = 12000
    train_loader = make_data_loader(cfg, is_train=True, distributed=False, max_iter=max_iter,
                                    start_iter=0)
    for iteration, (images, targets, _) in enumerate(train_loader, 0):
        print(iteration)
        print(images.shape)
        print(targets.shape)
        exit(0)


def test_data():
    data_loaders_val = make_data_loader(cfg, is_train=False, distributed=False)
    for dataset_name, data_loader in zip(cfg.DATASETS.TEST, data_loaders_val):
        print(dataset_name)
        print(data_loader)
        exit(0)


if __name__ == '__main__':
    train_data()
