#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 3:04 下午
# Author: chonmb
# Software: PyCharm
# this is simulation for network bridge

from src.core.AbstractNode import AbstractNode


class SBridge(AbstractNode):
    def __init__(self, name):
        super().__init__(name)
        self.spreaders = {}

    def add_spreader(self, spreader):
        self.spreaders[spreader.name] = spreader

    def remove_spreader(self, spreader_name):
        self.spreaders.pop(spreader_name)

    def set_lan(self, lan):
        self.add_spreader(lan)
