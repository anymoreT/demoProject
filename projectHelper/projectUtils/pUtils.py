# -*- coding:utf-8 -*-
from dianRongQa.utils.tools import Tools
import os
import sys
import pdb

class PUtils(object):
    @staticmethod
    def get_project_config(config_file = "config.ymal"):
        #读取project_config下面的文件夹里面的项目配置数据
        config_path = os.path.dirname(__file__)
        config_path = os.path.join(config_path, "test_config", config_file)
        return Tools.get_config(config_path)
