#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/9/27 11:09 下午
# Author: chonmb
# Software: PyCharm
# the start of simulation for network bridge. (SNB)
# emmmm, sound like we are simulating nb？🤪
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from src.console.console import SConsole

if __name__ == '__main__':
    console = SConsole()
    console.start()
