# -*- coding: utf-8 -*-

"""
@date: 2020/5/14 下午2:49
@file: build.py
@author: zj
@description: 
"""

from ssd.models import registry

from .vgg import vgg
from .mobilenet import mobilenet_v2
from .efficient_net import efficient_net_b3


def build_backbone(cfg):
    return registry.BACKBONES[cfg.MODEL.BACKBONE.NAME](cfg, cfg.MODEL.BACKBONE.PRETRAINED)
