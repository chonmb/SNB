#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 3:10 下午
# Author: chonmb
# Software: PyCharm
# this is simulation for client, we presume that a client stands for PC

from src.core.AbstractNode import AbstractNode


class SClient(AbstractNode):
    def __init__(self, name, mac='', lan=None):
        super().__init__(name)
        self.mac = mac
        self.lan = lan

    def set_lan(self, lan):
        self.lan = lan

    def deliver(self, frame, node_from):
        if frame.source_mac == self.mac:
            return [self.lan]
        return None
