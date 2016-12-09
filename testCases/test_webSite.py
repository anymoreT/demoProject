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
# from selenium import webdriver
# from pyQa.globalFactory.globalVars import GlobalFactory

class WebSiteTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("project.ymal")
        self.env = Tools.get_test_suit_env()
     
    @unittest.skipUnless(Tools.runCaseIn("smoke"),"skip case if not in tags") 
    def test_TC001(self):
        Log.log_case_desc("测试进入百度页面，输入搜索内容，点击搜索，然后进行检查.如果不能成功进行，则报错。如果成功，久不管")

        # driver = webdriver.Chrome()
        # GlobalFactory.set_driver(driver)
        WebDriver.start_driver()
        WebDriver.go_to_url(self.config['Login'][self.env])
        PageTextInputElement(BaiduHomePage.SearchTextInput).wait_element_present()
        PageTextInputElement(BaiduHomePage.SearchTextInput).input("测试一下")
        PageTextInputElement(BaiduHomePage.SearchButton).click()


    @unittest.skipUnless(Tools.runCaseIn("smoke"), "skip case if not in tags")
    def test_TC002(self):
      Log.log_case_desc("测试进入百度页面，输入搜索内容，点击搜索，然后进行检查.如果不能成功进行，则报错。如果成功，久不管")
      Log.log_error_info("meet error")
