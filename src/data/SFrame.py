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
    def __init__(self, manager, name='', s_mac='', dist_mac='', ):
        super().__init__(manager.global_clock)
        self.name = name
        self.source_mac = s_mac
        self.dist_mac = dist_mac
        self.manager = manager
        self.current_node = None
        self.branches = []
        self.next_branches = []
        self.death = False
        self.history_branches = {}
        self.history_next_branches = {}
        self.history_current_node = {}
        self.history_death = {}

    def trace_path(self):
        print("frame name: %s\npath_trace: " % self.name)
        trace_branches = [self.data]
        path = []
        while len(trace_branches) > 0:
            path.append(', '.join([t_b.node.name for t_b in trace_branches]))
            next_trace_branches = []
            for b in trace_branches:
                for b_child in b.children:
                    next_trace_branches.append(b_child)
            trace_branches = next_trace_branches
        print(' -> '.join(path))

    def build_frame(self, name, source_node, dist_node):
        self.name = name
        self.source_mac = source_node.mac
        self.dist_mac = dist_node.mac
        self.data = FrameTraceNode(source_node)
        self.next_branches.append(self.data)
        self.manager.frames[self.name] = self

    def record_data(self):
        self.next_clock()
        self.history_branches[self.clock.current_clock] = self.branches
        self.history_next_branches[self.clock.current_clock] = self.next_branches
        self.history_current_node[self.clock.current_clock] = self.current_node
        self.history_death[self.clock.current_clock] = self.death

    def recover(self, clock_stamp):
        if clock_stamp in self.history.keys():
            super().recover(clock_stamp)
            self.branches = self.history_branches.get(clock_stamp)
            self.current_node = self.history_current_node.get(clock_stamp)
            self.death = self.history_death.get(clock_stamp)
            self.next_branches = self.history_next_branches.get(clock_stamp)

    def next_step(self):
        if len(self.next_branches) == 0:
            self.death = True
            return
        self.record_data()
        self.branches = self.next_branches
        self.next_branches = []
        for branch in self.branches:
            self.current_node = branch.node
            next_nodes = self.current_node.deliver(self, branch.parent.node if branch.parent is not None else None)
            if next_nodes is not None and len(next_nodes) != 0:
                for n in next_nodes:
                    trace_node = FrameTraceNode(n)
                    branch.add_children(trace_node)
                    self.next_branches.append(trace_node)
