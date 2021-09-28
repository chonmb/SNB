#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 2:51 下午
# Author: chonmb
# Software: PyCharm

class AbstractPart:
    def __init__(self, name):
        self.name = name

    def rollback(self, index):
        pass  # overwrite this function to implement rollback

    def next_step(self):
        pass  # overwrite this function to implement next_step
