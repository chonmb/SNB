#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 11:15 上午
# Author: chonmb
# Software: PyCharm
import json
from src.spreader.SLan import SLan
from src.nodes.SClient import SClient
from src.nodes.SBridge import SBridge


def parse_network_config():
    with open("resource/network.json") as network:
        network_map = json.load(network)
    return network_map


class SManager:
    def __init__(self):
        self.bridges = {}
        self.clients = {}
        self.lans = {}
        self.network = parse_network_config()
        self.init_network()

    def init_network(self):
        for lan in self.network["lan"]:
            self.lans[lan["name"]] = SLan(lan["name"])
        for client in self.network["clients"]:
            c = SClient(client["name"], client["mac"])
            self.clients[client["name"]] = c
            self.lans[client["lan"]].add_node(c)
        for bridge in self.network["bridges"]:
            b = SBridge(bridge["name"])
            self.bridges[bridge["name"]] = b
            for lan_name in bridge["lans"]:
                self.lans[lan_name].add_node(b)
