# -*- coding:utf-8 -*-
import unittest 
from dianRongQa.httpHander.httpHandler import HttpHandle
from dianRongQa.database.mysqlUtil import MysqlUtil
from dianRongQa.database.oracleUtil import CrmOracle
from projectHelper.projectUtils.pUtils  import PUtils
from dianRongQa.utils.tools import  Tools


class DbTest(unittest.TestCase):
    def setUp(self):
        #读取配置文件
        self.config = PUtils.get_project_config("adminMainSite.ymal")
        self.env = Tools.get_test_suit_env()
    
    #删除数据库sl$loan,的数据
    def test_delete_loanId_from_loan(self):    
        loan_id = 3919342
        oracel_instance = CrmOracle()
        oracel_instance.connect()
        sql = "delete from sl$loan where id=%d"%(loan_id)
        result = oracel_instance.do_insert_del_action(sql)
        print("delete oracle result is: ",result)
     
     #查询数据库sl$loan_app,的数据
    def test_query_loan_id_from_loanApp(self):
        loan_id = 3919342
        oracel_instance = CrmOracle()
        oracel_instance.connect()
        sql = "select * from sl$loan_app where loan_id=%d"%(loan_id)
        result = oracel_instance.ececute(sql)
        print("loan_app status is : ",result[0][4])
        
   #查询数据库sl$loan,的数据
    def test_query_loan_id_from_loan(self):
        loan_id = 3919342
        oracel_instance = CrmOracle()
        oracel_instance.connect()
        sql = "select * from sl$loan where id=%d"%(loan_id)
        result = oracel_instance.ececute(sql)
        print("loan_app status is : ",result[0][4])
             
    def test_make_loan_state_is_create(self,loan_id = 10015081):        
        oracel_instance = CrmOracle()
        oracel_instance.connect()
        #删除loan in sl$loan
        sql = "delete from sl$loan where id=%d"%(loan_id)
        result = oracel_instance.do_no_query_action(sql)
        print("delete loan result:", result)
        
        #更新loan in sl$loan_app
        sql = "update sl$loan_app set status=32  where loan_id=%d"%(loan_id)
        result = oracel_instance.do_no_query_action(sql)
        print("delete loan result:",result)
        
        #更新MYSQL
        #用户资料已完成,状态是32:CREATED
        mysql_instance = MysqlUtil()
        mysql_instance.connect()
        sql = "update loan set status='CREATED'  where loan_id=%d"%(loan_id)
        result = mysql_instance.do_no_query_action(sql)
        print("update loan result in mysql",result)
        