'''
author : DannyWu
site   : www.idannywu.com
'''
import pymongo
from pymongo import MongoClient
from config import MONGO_HOST,MONGO_PORT,DATABASE

class DB_Utils(object):
    
    #初始化，连接MongoDB
    def __init__(self):
        self.client = MongoClient(MONGO_HOST,MONGO_PORT)
        self.db = self.client[DATABASE]

    #向数据库集合中增加一条数据
    def save_one_to_mongo(self,collection,data):
        table = self.db[collection]
        table.insert_one(data)

    #向数据库集合中增加多条数据
    def save_many_to_mongo(self,collection,data):
        table = self.db[collection]
        table.insert_many(data)

    #条件查询数据库中的数据
    def query_of_arg(self,collection,arg):
        table = self.db[collection]
        result = table.find(arg)
        return result
        #for i in result:
        #    print(i)

    #查询数据库中所有的数据
    def query_all(self,collection):
        table = self.db[collection]
        result = table.find()
        return result
        #for i in result:
        #    print(i)

    #删除数据库
    #def drop_db(self,db_name):
    #    self.db

    #删除集合
    def drop_collection(self,collection):
        table = self.db[collection]
        table.drop()


