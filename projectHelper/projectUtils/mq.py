# -*- coding:utf-8 -*-
from dianRongQa.httpHander.httpHandler import HttpHandle
from dianRongQa.utils.tools import  Tools
import base64
from projectHelper.projectUtils.pUtils  import PUtils
import time
import json
import pdb

class MqHttpHelper(object):
    def __init__(self):
            self.env = Tools.get_test_suit_env()
            self.http_hander = None
            self.config_hash = PUtils.get_project_config("mq.ymal")
            self.form_data = None
    
    def login_mq(self):
            self.http_hander =  HttpHandle()
            user,password = self.config_hash['Account'][self.env].split(",")
         
            account_str =  "%s:%s"%(user.strip(),password.strip())
            account_bytes = account_str.encode()
            account_base64 = base64.b64encode(account_bytes)
            self.http_hander.update_header({'Content-Type':'application/json', 
                                                                    'authorization': 'Basic %s' %(account_base64.decode())})

            self.http_hander.do_get(self.config_hash['login'][self.env])
           
    
    
    def set_mq_data(self,  **kwargs):
        self.form_data =  {"vhost":"/msgbus",
                      "name": "amq.default",
                      "properties":{"delivery_mode":1,"headers":{}},
                      "routing_key": None,
                      "delivery_mode":"1",
                      "payload": None,
                      "headers":{},
                      "props":{},
                      "payload_encoding":"string"}
        self.form_data.update(kwargs)
       

        #发送新注册用户信息          
    def create_lender_user(self,  offset_day = 0, referid=None):
        offset_time = offset_day * 24 * 60 * 60 * 1000
        regiser_time = int(time.time()*1000) - offset_time 
        playload = {"idNo": "","flags":128,"borrowerStatus":"NONE","lenderStatus":"CONFIRMED",
                       "id":Tools.get_random_actor_id(),
                       "lenderStatusDate":regiser_time,
                       "email": Tools.get_random_email(),
                       "cellphone": Tools.get_random_phone_number(),
                       "name":"","recommendChannel":"m_boappxiaomi1",
                       "createDate":regiser_time,
                       "borrowerStatusDate":regiser_time,
                       "referrerId":referid,
                       "channel":""}
        
        #特别注意，json格式必须是双引号，单引号发送http请求会报错
        self.form_data['payload'] = json.dumps(playload)
        self.http_hander.do_post(self.config_hash['create_user'][self.env], data = json.dumps(self.form_data))
        self.http_hander.response_code_status_should_be(200)
        self.http_hander.response_string_should_include('{"routed":true}')
        print("cellphone:",  playload['cellphone'])
        print("id:",  playload['id'])
        print("referrerId:",playload['referrerId'])
        return  playload