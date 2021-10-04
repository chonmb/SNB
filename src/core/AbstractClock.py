#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 10:47 下午
# Author: chonmb
# Software: PyCharm
# definition of clock, which will be used for record time and data that needed recover


class AbstractClock:
    def __init__(self, clock):
        # current time
        self.clock = clock
        self.clock.add_listener(self)
        # history data
        self.history = {}
        # current data
        self.data = None

    def get_history(self, clock_stamp):
        return self.history[clock_stamp] if self.history.get(clock_stamp) is not None else None

    def recover(self, clock_stamp):
        self.data = self.get_history(clock_stamp)

    def next_clock(self):
        self.history[self.clock.current_clock] = self.data

    def clear(self):
        self.history.clear()
        self.data = None

    def next_step(self):
        self.next_clock()


class Clock:
    def __init__(self):
        self.current_clock = 0
        self.clock_listeners = []

    def next(self):
        self.current_clock += 1
        for listener in self.clock_listeners:
            listener.next_step()

    def clear(self):
        self.current_clock = 0
        for listener in self.clock_listeners:
            listener.clear()

    def rollback(self, clock_index):
        self.current_clock = clock_index
        for listener in self.clock_listeners:
            listener.recover(clock_index)

    def add_listener(self, listener: AbstractClock):
        if isinstance(listener, AbstractClock):
            self.clock_listeners.append(listener)
