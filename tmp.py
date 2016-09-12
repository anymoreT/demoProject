import pdb
import  pymongo

client = pymongo.MongoClient('localhost', 8000)  
db = client["matrix_db"]
db.authenticate("neo", "6c7cb51c-2f70-11e5-958a-001f16377cc4")
db.collection_names()
#collection = db['neo.merchant.wish.WishSales']
collection  = db['neo.merchant.OrderStatisticsResult']
print(collection.find_one())
