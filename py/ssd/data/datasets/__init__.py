# -*- coding: utf-8 -*-

"""
@date: 2020/5/9 下午8:54
@file: __init__.py.py
@author: zj
@description: 
"""

from .voc import VOCDataset
from .coco import COCODataset

from .build import build_dataset
from .evaluation import evaluate
