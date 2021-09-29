#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/28 10:30 上午
# Author: chonmb
# Software: PyCharm
from threading import Thread
from src.manager.SManager import SManager
from src.view.view import View


class SConsole(Thread):
    def __init__(self):
        super().__init__()
        self.banner_template = '\033[36;1m{}\033[0m'
        self.banner = self.__load_banner()
        self.s_manager = SManager()
        self.view = View(self.s_manager)
        self.command_map = {
            "show_network": lambda args: self.view.show_network(),
            "help": lambda args: print("\n".join(self.command_map.keys()))
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

    def run(self) -> None:
        print(self.banner)
        while True:
            command = input('&snb < ')
            if command == "quit":
                break
            self.parse_command(command)
