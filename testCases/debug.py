# -*- coding:utf-8 -*-
import unittest 
import requests
from frameWork.httpHander.httpHandler import HttpHandle
from projectHelper.projectUtils.pUtils  import PUtils
from frameWork.log.log import Log
import pdb

class AdminConsoleTest(unittest.TestCase):
    def setUp(self):
        self.config = PUtils.get_project_config("adminConsle.ymal")
        self.env = PUtils.get_project_evn()
        
    
     #https://drac-demo.dianrong.com/adminconsole/api/actor/{actorId}/transactions
    def test_transactions(self):
        actor = "11335844"
        url = self.config["Url"]["transactions"]
        url = PUtils.replace_paramter(url, actor)
        http_hander = HttpHandle()
        http_hander.do_get(url)
        http_hander.reponse_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.response_dictionary_should_have_key("content")
        http_hander.response_string_should_include('{"content":{"transactions":[{"createDate":"2016-07-06 17:07"')
        http_hander.response_string_should_include('{"createDate":"2016-07-06 17:07","type":11,"typeName":"每月还款"')
        
    #https://drac-demo.dianrong.com/adminconsole/api/actor/{actorId}/transactions
    #测试无效id
    def test_transactions_with_invalid_actor(self):
        actor = "999911335844"
        url = self.config["Url"]["transactions"]
        url = PUtils.replace_paramter(url, actor)
        http_hander = HttpHandle()
        http_hander.do_get(url)  
        http_hander.reponse_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.response_dictionary_should_have_key("errMsg")
        http_hander.response_dictionary_should_have_key_value("errMsg", "actor not found")
     
    #测试投资者过滤    
    #POST /api/investment/filterInvestment
    def test_filterInvestment(self):
        url = self.config["Url"]["filterInvestment"]
        http_hander = HttpHandle()
        http_hander.update_header({'Accept': 'application/json', 'Content-Type':'application/json'})
        payload = '{"actorList": [11335844],"endDate": "2016-02-05","page": 1,"pageSize": 100,"prdList": [102801, 145201, 26760168201, 340401,304201], "singleton": true,"startDate": "2016-02-02"}'
        #http_hander.do_post_with_json_payload(url, payload)  
        http_hander.do_post_with_json_string_payload(url, payload)  
        http_hander.reponse_code_status_should_be(200)  
        http_hander.print_response_body()
        http_hander.response_dictionary_should_have_key("content")
        http_hander.response_string_should_include('"start":1,"count":100,"total":2')
        http_hander.response_string_should_include('"rows":[{"registDate":"2015-12-25"')
        http_hander.response_string_should_include('{"registDate":"2015-12-25","investDate":"2016-02-03","actorId":11335844,"actorName":"黄勇","loanId":340401,"loanType":"group","investType":"正常投资","investAmount":666.66}')

     
    #https://drac-demo.dianrong.com/adminconsole/api/actor/{parameter}/investSummary
    def test_investSummary(self):
        url = self.config["Url"]["investSummary"]
        actor = '11335844'
        url = PUtils.replace_paramter(url, actor)
        http_hander = HttpHandle()
        http_hander.do_get(url)  
        http_hander.reponse_code_status_should_be(200)
        http_hander.response_body_should_be_dictionary_struct()
        http_hander.print_response_body()
        http_hander.response_string_should_include('"verified":"失效"')
        http_hander.response_dictionary_should_have_keys(["content", "errMsg", "code", "errName"])

     