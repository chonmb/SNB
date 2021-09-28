#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 2:48 下午
# Author: chonmb
# Software: PyCharm
# simulation for frame
from src.core.AbstractClock import AbstractClock


class SFrame(AbstractClock):
    def __init__(self):
        super().__init__()
        self.dist = ''
