# -*- coding:utf-8 -*-
from frameWork.utils.tools import Tools
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
    
    @staticmethod
    #获取运行环境，Demo, Dev
    def get_project_evn():  
        return  sys.argv[1].strip()
    
    @staticmethod
    #获取运行的测试集，smoke, regression
    def get_project_testSuit():  
            if len(sys.argv) > 2:
                return  sys.argv[2].strip() 
            else:
                return "regression"   
     
    @staticmethod        
    #url = "http://sina.com/{0}/new/{1}?{2}"
    #用传入参数,替换{0},{1},{2}
    def replace_paramter(url, *paramters):
        request_str = ""
        if len(paramters) == 1:
            request_str = url.format(paramters[0])
        elif  len(paramters) == 2:
            request_str = url.format(paramters[0],paramters[1])
        elif  len(paramters) == 3:
            request_str = url.format(paramters[0],paramters[1],paramters[2])    
        else:
            return request_str
        return request_str
               
#用于保证case在指定测试集里面运行 
    
def runTagIn(*tags):
        run_testSuit =  PUtils.get_project_testSuit()
        if run_testSuit in tags:
            return True
        else:
            return False           