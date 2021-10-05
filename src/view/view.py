#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 2:42 下午
# Author: chonmb
# Software: PyCharm
import networkx as nx
import matplotlib.pyplot as plt
import os
import platform


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
        if platform.system() != "Windows":
            if self.manager.env["path"]["network_pic_output"] != "":
                self.save_network_pic(plt)
            else:
                print("please config the 'network_pic_output' in 'env.json")
        else:
            plt.show()

    def save_network_pic(self, plt):
        pic = self.manager.env["path"]["network_pic_output"]
        if os.path.exists(pic):
            os.remove(pic)
        plt.savefig(pic)
        print("the picture of network have saved to {}".format(pic))

    def show_frame(self, frame_name):
        print(self.manager.frames[frame_name].trace_path())

    def show_relay_table(self, bridge_name):
        print(self.manager.bridges[bridge_name].data)
