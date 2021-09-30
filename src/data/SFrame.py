#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 2:48 下午
# Author: chonmb
# Software: PyCharm
# simulation for frame
from src.core.AbstractClock import AbstractClock


class FrameTraceNode:
    def __init__(self, node):
        self.parent = None
        self.children = []
        self.node = node

    def set_parent(self, parent):
        self.parent = parent

    def add_children(self, children_node):
        self.children.append(children_node)
        children_node.set_parent(self)


class SFrame(AbstractClock):
    def __init__(self, name='', s_mac='', dist_mac=''):
        super().__init__()
        self.name = name
        self.source_mac = s_mac
        self.dist_mac = dist_mac
        self.current_node = None
        self.branches = []
        self.death = False

    def trace_path(self):
        pass  # pretty print

    def build_frame(self, name, source_node, dist_node):
        self.__init__(name, source_node.mac, dist_node.mac)
        self.data = FrameTraceNode(source_node)
        self.branches.append(self.data)

    def next_step(self):
        if len(self.branches) == 0:
            self.death = True
            return
        self.next_clock()
        for branch in self.branches:
            next_branches = []
            self.current_node = branch.node
            next_nodes = self.current_node.deliver(self, branch.parent.node if branch.parent is not None else None)
            if next_nodes is not None and len(next_nodes) != 0:
                for n in next_nodes:
                    trace_node = FrameTraceNode(n)
                    branch.add_children(trace_node)
                    next_branches.append(trace_node)
            self.branches = next_branches
