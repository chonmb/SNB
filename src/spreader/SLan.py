#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 10:41 下午
# Author: chonmb
# Software: PyCharm
# this is simulation for lan, which will tell the nodes registered the frame data

class SLan:
    def __init__(self, name=''):
        self.name = name
        self.spread_nodes = {}

    def notify_all(self, frame):
        pass  # notified other registered nodes to deliver message
