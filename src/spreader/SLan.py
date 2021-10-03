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

    def add_node(self, node):
        self.spread_nodes[node.name] = node
        node.set_lan(self)

    def deliver(self, frame, node_from):
        node_list = []
        for node in self.spread_nodes.values():
            if node.name == node_from.name:
                continue
            print("[%s] received Frame[name:%s] from [%s]:spread to [%s]" % (
                self.name, frame.name, node_from.name, node.name))
            node_list.append(node)
        return node_list
