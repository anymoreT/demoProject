# -*- coding:utf-8 -*-
import unittest 
import requests
from frameWork.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils,runTagIn
from frameWork.log.log import Log
import pdb
from frameWork.utils.webDriver import WebDriver
from projectHelper.webElements.importAll import *

class AdminConsoleTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("adminMainSite.ymal")
        self.env = PUtils.get_project_evn()
        
    @unittest.skipUnless(runTagIn("admin","ui"),"skip case if not in tags") 
    def test_login_main_page(self):
        WebDriver.start_driver()
        WebDriver.go_to_url(self.config['Login'][self.env])
        login.UserNameTextInput().input("yong.huang@dianrong.com")
        login.PasswordTextInput().input("$cdu1234R")
        login.LoginButton().click()
        WebDriver.switch_to_frame("center-frame")
        commonElement.H1SmallText("Welcome").wait_element_present()