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
            print("[%s] send Frame[name:%s] from Port[%s]" % (self.name,frame.name,self.lan.name))
            return [self.lan]
        if frame.dist_mac == self.mac:
            print("[%s] received Frame[name:%s]:Accepted!!!" % (self.name,frame.name))
        else:
            print("[%s] received Frame[name:%s]:Declined!!!" % (self.name,frame.name))
        return None
