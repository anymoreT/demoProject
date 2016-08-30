# -*- coding:utf-8 -*-
import unittest 
from dianRongQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from dianRongQa.log.log import Log
import pdb
from dianRongQa.utils.tools import  Tools

class TestApis(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("lender_config.ymal")
        self.env = Tools.get_test_suit_env()
     
     #注册主站用户，并设置登陆密码和交易密码   
    def test_regsiter_lender_user(self):
        phone_or_email = None
        password = "Cdu_dianron123"
        trade_key = "111111"
        http_handle = HttpHandle()
        http_handle.do_get(self.config["captcha_url"][self.env])
        response= http_handle.do_get(self.config["auto_captcha_url"][self.env])
        if response.status_code != 200:
            Log.log_error_info("status code is error after send auto_captcha_url request")  
        captcha = http_handle.get_response_struct()['content']['result']
        if phone_or_email is None:
            phone_or_email = Tools.get_random_phone_number()
            
        form_data = {"emailOrPhone":  phone_or_email,
                "type": "create",
                "attempt": 0,
                "captcha": captcha
            }
        http_handle.do_post(self.config["user_fetchverifycode_url"][self.env], form_data) 
        if http_handle.get_response_status_code() != 200:
            Log.log_error_info("status code is error after send user_fetchverifycode_url")

        verify_code = http_handle.get_response_struct()["content"]["response"]
        form_data = {"regPhone": phone_or_email,
                "regPhoneResponseCode": verify_code,
                "regPassword": password,
                "regPasswordConfirm": password,
                "acceptAgreement": "on",
                "referralName": '',
                "promotionCode": '',
                "captcha": captcha
        }
        response = http_handle.do_post(self.config["user_create_url"][self.env], form_data)
        if  http_handle.get_response_status_code()  != 200:
            Log.log_error_info("meet error after send user_create_url")

        user_id = http_handle.get_response_struct()["content"]["userId"]
        http_handle.do_get(self.config["tradekey_fetchverifycode_url"][self.env])
        if http_handle.get_response_status_code() != 200:
            Log.log_error_info("meet error meet error after tradekey_fetchverifycode_url")
        trade_key_verify_code = http_handle.get_response_struct()["content"]["confCode"]
        form_data = {"confCode": trade_key_verify_code,
                "tradeKey": trade_key,
                "confirmTradeKey": trade_key
        }
        response = http_handle.do_post(self.config["user_tradekey_url"][self.env],  form_data)
        if http_handle.get_response_status_code() != 200:
            Log.log_error_info("meet error after send user_tradekey_url")
        print( phone_or_email,user_id,password,trade_key)