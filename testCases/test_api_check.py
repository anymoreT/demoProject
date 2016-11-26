# -*- coding:utf-8 -*-
import unittest 
import requests
from pyQa.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.log.log import Log
from pyQa.utils.tools import  Tools

import pdb

class AdminConsoleCrmTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("adminConsle.ymal")
        self.env = Tools.get_test_suit_env()
        
    
    @unittest.skipUnless(Tools.runCaseIn("admin"),"skip case if not in tags")
    def test_transactions(self):    
        actor = "11335844"
        url = self.config["Url"]["transactions"]
        http_hander = HttpHandle()
        url = http_hander.replace_paramter_for_url(url, actor)

        http_hander.do_get(url)
        http_hander.response_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.response_dictionary_should_have_key("content")
        http_hander.response_string_should_include('{"content":{"transactions":[{"createDate":')
        http_hander.response_string_should_include('{"createDate":"2016-07-06 17:07","type":11,"typeName":"每月还款"')
       
    #https://drac-demo.pyQa.com/adminconsole/api/actor/{actorId}/transactions
    #测试无效id
    @unittest.skipUnless(Tools.runCaseIn("admin"),"skip case if not in tags") 
    def test_transactions_with_invalid_actor(self):
        actor = "999911335844"
        url = self.config["Url"]["transactions"]
        http_hander = HttpHandle()
        url = http_hander.replace_paramter_for_url(url, actor)
        http_hander.do_get(url)  
        http_hander.response_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.response_dictionary_should_have_key("errMsg")
        http_hander.response_dictionary_should_have_key_value("errMsg", "actor not found")
     
    #测试投资者过滤    
    #POST /api/investment/filterInvestment
    @unittest.skipUnless(Tools.runCaseIn("sm"),"skip case if not in tags") 
    def test_filterInvestment(self):
        url = self.config["Url"]["filterInvestment"]
        http_hander = HttpHandle()
        http_hander.update_header({'Accept': 'application/json', 'Content-Type':'application/json'})
        payload = '{"actorList": [11335844],"endDate": "2016-02-05","page": 1,"pageSize": 100,"prdList": [102801, 145201, 26760168201, 340401,304201], "singleton": true,"startDate": "2016-02-02"}'
        #http_hander.do_post_with_json_payload(url, payload)  
        http_hander.do_post_with_json_string_payload(url, payload)  
        http_hander.response_code_status_should_be(200)  
        http_hander.print_response_body()
        http_hander.response_dictionary_should_have_key("content")
        http_hander.response_string_should_include('"start":1,"count":100,"total":')
        http_hander.response_string_should_include('"rows":[{"registDate":"2015-12-25"')
        http_hander.response_string_should_include('{"registDate":"2015-12-25","investDate":"2016-02-03","actorId":11335844,"actorName":"黄勇","loanId":340401,"loanType":"group","investType":"正常投资","investAmount":666.66}')

     
    #https://drac-demo.pyQa.com/adminconsole/api/actor/{parameter}/investSummary
    @unittest.skipUnless(Tools.runCaseIn("admin"),"skip case if not in tags") 
    def test_investSummary(self):
        url = self.config["Url"]["investSummary"]
        actor = '11335844'
        http_hander = HttpHandle()
        url = http_hander.replace_paramter_for_url(url, actor)
        http_hander.do_get(url)  
        http_hander.response_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.print_response_body()
        http_hander.response_string_should_include('"verified":"失效"')
        http_hander.response_dictionary_should_have_keys(["content", "errMsg", "code", "errName"])

    # https://drac-demo.pyQa.com/api/actor/lender/{0}
    @unittest.skipUnless(Tools.runCaseIn("admin"),"skip case if not in tags") 
    def test_lender(self): 
        url = self.config["Url"]["lender"]
        actor = '11335844'
        http_hander = HttpHandle()
        url = http_hander.replace_paramter_for_url(url, actor)
        http_hander.do_get(url)  
        http_hander.response_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.print_response_body()
        http_hander.response_string_should_include('"actor":{"id":"11335844","name":"yong.huangv15"')
        http_hander.response_deep_key_is_struct("content","actor",target_struct={"birthday":"STRING", "cellphone":"STRING", "country":"STRING", "countryCode":"STRING", "createD":"STRING"})

     

        