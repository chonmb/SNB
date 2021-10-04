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
from pynput.keyboard import Listener, Key


class SConsole(Thread):
    def __init__(self):
        super().__init__()
        self.banner_template = '\033[36;1m{}\033[0m'
        self.s_manager = SManager()
        self.banner = self.__load_banner()
        self.view = View(self.s_manager)
        self.keyboard_listener = None
        self.command_help = {
            "show_network": "show the network graph",
            "help": "show command help",
            "quit": "quit system",
            "send_frame_example": "send example frame(based on default network config)",
            "send_frame": "[source] [target] send an frame from a client to another(input client name)",
            "clear": "clear network memory",
            "show_bridge_table": "[bridge_name] show bridge relay table(print all relay table when bridge is not specified)",
            "show_frame_trace": "(-optional)[frame_name] show history of frame relay",
            "rollback": "(-optional)[clock_index] rollback the simulation",
            "reload_network": "update network"
        }
        self.command_map = {
            "show_network": lambda args: self.view.show_network(),
            "help": lambda args: self.help(),
            "send_frame_example": lambda args: self.send_frame_example(),
            "send_frame": lambda args: self.send_frame(args),
            "clear": lambda args: self.s_manager.clear_network(),
            "show_frame_trace": lambda args: self.trace_path(args) if args is not None else self.trace_path(
                "client2_client3"),
            "reload_network": lambda args: self.s_manager.reload_network(),
            "show_bridge_table": lambda args: self.show_bridge_table(args),
            "rollback": lambda args: self.s_manager.rollback() if args is None else self.s_manager.rollback(int(args))
        }

    def parse_command(self, command):
        args = None
        if len(command.split(" ")) == 2:
            func, args = command.split(" ")
        elif len(command.split(" ")) == 3:
            func, args1, args2 = command.split(" ")
            args = [args1, args2]
        else:
            func = command
        if not func in self.command_map.keys():
            print("wrong command!please check your spelling or use 'help' to know supported commands.")
        else:
            func_o = self.command_map[func]
            if func_o is not None:
                func_o(args)

    def __load_banner(self):
        with open(self.s_manager.env["path"]["banner"], encoding='utf-8') as banner_file:
            banner_data = ''.join(banner_file.readlines())
        return self.banner_template.format(banner_data)

    def help(self):
        """
        show help list
        """
        print('\n'.join(["%-20s:%5s" % (k, v) for (k, v) in self.command_help.items()]))

    def trace_path(self, args):
        if self.s_manager.frames.get(args) is None:
            return None
        else:
            return self.s_manager.frames[args].trace_path()

    def send_frame_example(self):
        """
        ATTENTION: this function can be executed on default net
        send frame from client2 to client3
        the steps at intervals of 0.5 seconds
        will show the branch log of each step
        """
        self.send_frame(["client2", "client3"])

    def send_frame(self, args):
        """
        send a frame from a client to another
        """
        if args is None or len(args) != 2:
            print("send_frame exactly need 2 arguments,one is source client,another is target client")
            return
        if self.s_manager.clients.get(args[0]) is None or self.s_manager.clients.get(args[1]) is None:
            print("wrong client name,please check again!")
            return
        frame_name = args[0] + '_' + args[1]
        f = SFrame(self.s_manager)
        f.build_frame(frame_name, self.s_manager.clients[args[0]], self.s_manager.clients[args[1]])
        if self.s_manager.env["step"]["auto"] == "True":
            while not f.death:
                print("clock - %d:" % self.s_manager.global_clock.current_clock)
                time.sleep(float(self.s_manager.env["step"]["interval"]))
                self.s_manager.global_clock.next()
        else:
            with Listener(on_press=self.press_listen) as listener:
                self.keyboard_listener = listener
                print("press key 'down' to continue and press key 'up' to rollback.")
                self.keyboard_listener.join()

    def press_listen(self, key):
        if not self.s_manager.is_frames_alive():
            self.keyboard_listener.stop()
            self.keyboard_listener = None
            return
        print("clock - %d:" % self.s_manager.global_clock.current_clock)
        if key == Key.down:
            self.s_manager.global_clock.next()
        if key == Key.up:
            print("rollback to ", self.s_manager.global_clock.current_clock - 1)
            self.s_manager.rollback()

    def show_bridge_table(self, bridge_name=None):
        # print all bridge relay table when bridge name is not specified
        if bridge_name is None:
            for bridge in self.s_manager.bridges.values():
                bridge.show_table()
        else:
            if self.s_manager.bridges.get(bridge_name) is not None:
                self.s_manager.bridges[bridge_name].show_table()
            else:
                print(bridge_name + " is not founded.")

    def run(self):
        print(self.banner)
        # self.view.show_network(is_output=True)
        while True:
            command = input('&snb < ')
            if command == "quit":
                break
            self.parse_command(command)
