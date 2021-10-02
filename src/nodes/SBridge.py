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
        self.data = {}

    def add_spreader(self, spreader):
        self.spreaders[spreader.name] = spreader

    def remove_spreader(self, spreader_name):
        self.spreaders.pop(spreader_name)

    def set_lan(self, lan):
        self.add_spreader(lan)

    def deliver(self, frame, node_from):
        self.data[frame.source_mac] = node_from.name
        if self.data.get(frame.dist_mac) is not None:
            return [self.spreaders[self.data[frame.dist_mac]]]
        if self.data.get(frame.dist_mac) == node_from.name:
            return None
        node_list = []
        for spreader in self.spreaders.values():
            if node_from.name == spreader.name:
                continue
            else:
                node_list.append(spreader)
        return node_list

    def clear(self):
        super().clear()
        self.data.clear()

    def show_table(self):
        print(self.name)
        print("-------------------------")
        print("%-20s%-10s" % ("mac", "port"))
        print("-------------------------")
        print('\n'.join(["%-20s%-10s" % (k, v) for k, v in self.data.items()]))
        print('\n')
