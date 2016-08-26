# -*- coding:utf-8 -*-
import unittest 
import requests
from dianRongQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from dianRongQa.log.log import Log
import pdb
from dianRongQa.utils.webDriver import WebDriver
from projectHelper.webElements.importAll import *
from dianRongQa.utils.tools import  Tools

class AdminConsoleTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("adminMainSite.ymal")
        self.env = Tools.get_test_suit_env()
     
    @unittest.skipUnless(Tools.runCaseIn("admin","ui"),"skip case if not in tags") 
    def test_login_main_page(self):
        WebDriver.start_driver()
        WebDriver.go_to_url(self.config['Login'][self.env])
        login.UserNameTextInput().wait_element_present()
        account_list= self.config['Account'][self.env]['Member0'].strip().split(",")
        login.UserNameTextInput().input(account_list[0])
        login.PasswordTextInput().input(account_list[1])
        login.LoginButton().click()
        WebDriver.switch_to_frame("center-frame")
        commonElement.H1SmallText("Welcome").wait_element_present()