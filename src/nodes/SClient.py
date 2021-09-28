#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 3:10 下午
# Author: chonmb
# Software: PyCharm
# this is simulation for client, we presume that a client stands for PC

from ..core.AbstractNode import AbstractNode


class SClient(AbstractNode):
    def __init__(self, name):
        super().__init__(name)
        self.mac = ''
        self.eth = None

    def set_eth(self, eth):
        self.eth = eth
