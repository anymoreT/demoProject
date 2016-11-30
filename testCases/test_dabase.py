# -*- coding:utf-8 -*-
import unittest 
from pyQa.httpHander.httpHandler import HttpHandle
# from pyQa.database.mysqlUtil import MysqlUtil
# from pyQa.database.oracleUtil import OracleUtil
from projectHelper.projectUtils.pUtils  import PUtils
from projectHelper.projectUtils.workflowOracle import WorkflowOracle
from projectHelper.projectUtils.crmMysql import CrmMysql
from pyQa.utils.tools import  Tools
import pdb
import datetime


class DbTest(unittest.TestCase):
    def setUp(self):
        pass
    
     #查询数据库sl$loan_app,的数据
    @unittest.skipUnless(Tools.runCaseIn("smoke"),"skip case if not in tags") 
    def test_query_loan_id_from_loanApp(self):
        loan_id = 14801
        oracel_instance = WorkflowOracle()
        sql = "select * from sl$loan_app where loan_id=%d"%(loan_id)
        result = oracel_instance.query(sql)
        print("loan_app status is : ",result[0][4])
     
    @unittest.skipUnless(Tools.runCaseIn("smoke"),"skip case if not in tags")    
    def test_mysql(self):        
        mysql_instance = CrmMysql()
        sql = 'SELECT * FROM wfcrm.actor where actor_id=11335844'
        res = mysql_instance.query(sql)
        sql = 'update wfcrm.actor  set recommend_actor_id="1234567" where crm_customer_id=24943'
        res = mysql_instance.do_no_query_action(sql)
        sql = 'SELECT * FROM wfcrm.actor where crm_customer_id=24943'
        res = mysql_instance.query(sql)
        print("mysql test finished %s"%(res))

   
        
        