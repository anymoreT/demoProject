# -*- coding:utf-8 -*-
from dianRongQa.utils.tools import  Tools
from  pymongo import MongoClient
from projectHelper.projectUtils.pUtils  import PUtils

class Mongo(object):
    def __init__(self):
        '''
        client = MongoClient('localhost', 8000)  
        db = client["matrix_db"]
        db.authenticate("neo", "6c7cb51c-2f70-11e5-958a-001f16377cc4")
        db.collection_names()
        collection = db['neo.merchant.wish.WishSales']
        '''
        self.config = PUtils.get_project_config("database.yml")
        self.env = Tools.get_test_suit_env()
        client = MongoClient(self.config['Mongodb'][self.env]['host'], int(self.config['Mongodb'][self.env]['port'])) 
        self.db = client[self.config['Mongodb'][self.env]['db']]
        self.db .authenticate(self.config['Mongodb'][self.env]['user'], self.config['Mongodb'][self.env]['password'])
        
    def get_db_instance(self):
        return self.db     
        