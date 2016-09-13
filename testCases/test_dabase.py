# -*- coding:utf-8 -*-
import unittest 
from dianRongQa.httpHander.httpHandler import HttpHandle
# from dianRongQa.database.mysqlUtil import MysqlUtil
# from dianRongQa.database.oracleUtil import OracleUtil
from projectHelper.projectUtils.pUtils  import PUtils
from projectHelper.projectUtils.workflowOracle import WorkflowOracle
from projectHelper.projectUtils.crmMysql import CrmMysql
from projectHelper.projectUtils.mongo import Mongo
from dianRongQa.utils.tools import  Tools
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

    def  test_mongo_db(self):
        mongo_instance = Mongo().get_db_instance()
        table = mongo_instance['neo.merchant.OrderStatisticsResult']
        print(table.find_one())
        uc_time = datetime.datetime.utcnow()
        row_data = {
            "_class" : "com.dianrong.neo.merchant.model.entity.OrderStatisticsResult",
            "cellphone" : "18699999999",
            "platform" : "eBay",
            "account" : "wandon-49",
            "applyTime" : uc_time,
            "registerTime" : uc_time,
            "totalAmount" : 21302.97,
            "totalCount" : 6,
            "data" : [ 
                      {
                       "year" : 2016,
                       "month" : 8,
                       "count" : 3,
                       "amount" : 300.0,
                       "currencyID" : "GBP"
                       }, 
                      {
                       "year" : 2016,
                       "month" : 7,
                       "count" : 1,
                       "amount" : 5000.99,
                       "currencyID" : "GBP"
                       }, 
                      {
                       "year" : 2016,
                       "month" : 6,
                       "count" : 2,
                       "amount" : 16001.98,
                       "currencyID" : "GBP"
                       }
                      ],
                    "createTime" : uc_time,
                    "updateTime" : uc_time
}
        table.insert(row_data)

        
        