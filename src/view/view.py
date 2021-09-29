#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 2:42 下午
# Author: chonmb
# Software: PyCharm
import networkx as nx
import matplotlib.pyplot as plt


class View:
    def __init__(self, manager):
        self.manager = manager

    def show_network(self):
        graph = nx.Graph()
        graph.add_nodes_from([b for b in self.manager.bridges.keys()])
        graph.add_nodes_from([c for c in self.manager.clients.keys()])
        for lan in self.manager.lans.values():
            graph.add_node(lan.name)
            graph.add_edges_from([(lan.name, node.name) for node in lan.spread_nodes.values()])
        nx.draw(graph, with_labels=True)
        plt.show()

    def show_frame(self, frame_name):
        pass  # display the frame

    def show_relay_table(self, bridge_name):
        pass  # display the relay table
