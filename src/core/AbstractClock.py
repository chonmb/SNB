#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 10:47 下午
# Author: chonmb
# Software: PyCharm
# definition of clock, which will be used for record time and data that needed recover


class AbstractClock:
    def __init__(self):
        # current time
        self.current_clock = 0
        # history data
        self.history = {}
        # current data
        self.data = None

    def get_history(self, clock_stamp):
        return self.history[clock_stamp]

    def next_clock(self):
        self.history[self.current_clock] = self.data
        self.current_clock += 1

    def clear(self):
        self.history.clear()
        self.data = None
        self.current_clock = 0
