#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time: 2021/10/3 4:26 下午
# Author: chonmb
# Software: PyCharm
import json


class GlobalConfig:
    def __init__(self):
        self.config_path = "env.json"
        self.configs = self.__config_init__()

    def __config_init__(self):
        with open(self.config_path, encoding="utf-8") as config:
            env_config = json.load(config)
        return env_config
