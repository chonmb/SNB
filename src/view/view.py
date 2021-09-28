#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 2:42 下午
# Author: chonmb
# Software: PyCharm

class View:
    def __init__(self, manager):
        self.manager = manager

    def show_network(self):
        pass  # display the network

    def show_frame(self, frame_name):
        pass  # display the frame

    def show_relay_table(self, bridge_name):
        pass  # display the relay table
