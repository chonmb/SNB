#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 11:15 上午
# Author: chonmb
# Software: PyCharm
import json
from src.spreader.SLan import SLan
from src.nodes.SClient import SClient
from src.nodes.SBridge import SBridge
from src.utils.Util import Util

def parse_network_config():
    with open("resource/network.json", encoding='utf-8') as network:
        network_map = json.load(network)
    return network_map

class SManager:
    def __init__(self):
        self.bridges = {}
        self.clients = {}
        self.lans = {}
        self.frames = {}
        self.network = parse_network_config()
        self.check_network()
        self.init_network()

    def init_network(self):
        """
        load network from network.json(it is the default network)
        """
        for lan in self.network["lans"]:
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

    def check_network(self):
        """
        check some basic network config errors such as repeated client name.
        """ 
        bridge_names = [bridge['name'] for bridge in self.network["bridges"]]
        res = Util.check_repeated_elements(bridge_names)
        if res is not None:
            self.init_failed(res + " already existed!")

        lan_names = [lan['name'] for lan in self.network["lans"]]
        res = Util.check_repeated_elements(lan_names)
        if res is not None:
            self.init_failed(res + " already existed!")
        
        client_names = [client['name'] for client in self.network["clients"]]
        res = Util.check_repeated_elements(client_names)
        if res is not None:
            self.init_failed(res + " already existed!")

        for bridge in self.network["bridges"]:
            for lan_name in bridge["lans"]:
                if lan_name not in lan_names:
                    self.init_failed(lan_name+' is not defiend')

        for client in self.network["clients"]:
            if client["lan"] not in lan_names:
                    self.init_failed(client["lan"]+' is not defiend')

    def init_failed(self,reason):
        error_prefix = 'snb quit because of incorrect network config:'
        print(error_prefix+reason)
        exit(0)

    def clear_network(self):
        self.frames.clear()
        for b in self.bridges:
            b.clear()
