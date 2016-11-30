# -*- coding:utf-8 -*-
import unittest 
import requests
from pyQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.log.log import Log
import pdb
from pyQa.utils.webDriver import WebDriver
from projectHelper.webElements.login import BaiduHomePage
from pyQa.utils.tools import  Tools
from pyQa.web.PageElement import *

class WebSiteTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("project.ymal")
        self.env = Tools.get_test_suit_env()
     
    @unittest.skipUnless(Tools.runCaseIn("smoke"),"skip case if not in tags") 
    def test_goto_baidu_page(self):
        WebDriver.start_driver()
        WebDriver.go_to_url(self.config['Login'][self.env])
        PageTextInputElement(BaiduHomePage.SearchTextInput).wait_element_present()
        PageTextInputElement(BaiduHomePage.SearchTextInput).input("测试一下")
        PageTextInputElement(BaiduHomePage.SearchButton).click()

       
        