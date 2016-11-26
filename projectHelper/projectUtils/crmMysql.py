# -*- coding:utf-8 -*-
from pyQa.utils.tools import  Tools
from projectHelper.projectUtils.pUtils  import PUtils
from pyQa.database.mysqlUtil import MysqlUtil
from pyQa.database.oracleUtil import OracleUtil
import pdb

class CrmMysql(object):
    def __init__(self):
        self.config = PUtils.get_project_config("database.yml")
        self.env = Tools.get_test_suit_env()
        self.db_info= self.config['CrmMysql'][ self.env]
        self.mysql_instance = MysqlUtil(self.db_info['host'],self.db_info['user'],
                                                  self.db_info['password'],self.db_info['db'],
                                                  self.db_info['port'])
            
    def user_is_exist_by_phone(self, phone):
        pass
      
    def query(self,  sql):
        return self.mysql_instance.query(sql) 
    
    def do_no_query_action(self,sql):
        self.mysql_instance.do_no_query_action(sql)
    