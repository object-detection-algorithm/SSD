# -*- coding: utf-8 -*-

"""
@date: 2020/5/14 下午3:37
@file: build.py
@author: zj
@description: 
"""

from ssd.models import registry
from .box_head import SSDBoxHead


def build_box_head(cfg):
    return registry.BOX_HEADS[cfg.MODEL.BOX_HEAD.NAME](cfg)
