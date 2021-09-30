#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 10:30 上午
# Author: chonmb
# Software: PyCharm
import time
from threading import Thread
from src.manager.SManager import SManager
from src.view.view import View
from src.data.SFrame import SFrame


class SConsole(Thread):
    def __init__(self):
        super().__init__()
        self.banner_template = '\033[36;1m{}\033[0m'
        self.banner = self.__load_banner()
        self.s_manager = SManager()
        self.view = View(self.s_manager)
        self.command_help = {
            "show_network": "show the network graph",
            "help": "show command help",
            "quit": "quit system",
            "send_frame_example": "send example frame(based on default network config)",
            "clear": "clear network memory",
            "show_bridge_table": "[bridge_name] show bridge relay table"
        }
        self.command_map = {
            "show_network": lambda args: self.view.show_network(),
            "help": lambda args: print("\n".join(["%-20s:%5s" % (k, v) for (k, v) in self.command_help.items()])),
            "send_frame_example": lambda args: self.send_frame_example(),
            "clear": lambda args: self.s_manager.clear_network(),
            "trace_frame": lambda args: None,
            "show_bridge_table": lambda args: self.s_manager.bridges[args].show_table() if self.s_manager.bridges.get(
                args) is not None else None
        }

    def parse_command(self, command):
        args = None
        if len(command.split(" ")) == 2:
            func, args = command.split(" ")
        else:
            func = command
        func_o = self.command_map[func]
        if func_o is not None:
            func_o(args)

    def __load_banner(self):
        with open("resource/banner.txt") as banner_file:
            banner_data = ''.join(banner_file.readlines())
        return self.banner_template.format(banner_data)

    def send_frame_example(self):
        """
        ATTENTION: this function can be executed on default net
        send frame from client2 to client3
        the steps at intervals of 0.5 seconds
        will show the branch log of each step
        """
        f = SFrame()
        f.build_frame("test", self.s_manager.clients["client2"], self.s_manager.clients["client3"])
        while not f.death:
            time.sleep(0.5)
            f.next_step()
            print(' '.join([b.node.name for b in f.branches]))

    def run(self) -> None:
        print(self.banner)
        while True:
            command = input('&snb < ')
            if command == "quit":
                break
            self.parse_command(command)
