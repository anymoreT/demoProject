# -*- coding:utf-8 -*-
from dianRongQa.utils.tools import  Tools
from  pymongo import MongoClient
class Mongo(object):
    def __init__(self,host,port,user,password):
        client = MongoClient('localhost', 8000)  
        db = client["matrix_db"]
        db.authenticate("neo", "6c7cb51c-2f70-11e5-958a-001f16377cc4")
        db.collection_names()
        collection = db['neo.merchant.wish.WishSales']