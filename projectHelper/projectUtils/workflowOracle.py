# -*- coding:utf-8 -*-
from pyQa.utils.tools import  Tools
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.database.mysqlUtil import MysqlUtil
from pyQa.database.oracleUtil import OracleUtil
import pdb

class WorkflowOracle(object):
    def __init__(self):
        self.config = PUtils.get_project_config("database.yml")
        self.env = Tools.get_test_suit_env()
        self.db_info= self.config['WorkflowOracle'][ self.env]
#         database_str = "%s:%s/%s"%(self.db_info['host'], self.db_info['port'], self.db_info['db'])
#         _(self, host, port, db, user, password):
        self.instance  = OracleUtil(self.db_info['host'], self.db_info['port'], self.db_info['db'], self.db_info['user'],  self.db_info['password'])
        self.instance .connect()
     
        
     #查询数据库操作
    def query(self,  sql):
        return self.instance.query(sql) 
    
    def do_no_query_action(self, sql):
        self.instance.do_no_query_action(sql) 
       
    def get_acotor_info(self, actor_id):
        pass
    
    def get_loan_inf(self, actor_id):
        pass