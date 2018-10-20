#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:45
# @Author  : userzhang
import pymongo
import json
import time


class python_mongodb():
    def __init__(self,host="localhost",port=27017,db="None",col="None"):
        self.Num=0
        self.host=host
        self.port=port
        self.db=db
        self.col=col
        while True:
            try:
                self.myclient = pymongo.MongoClient(self.host,self.port)
                # self.mydb = self.myclient[self.db]
                # self.mycol = self.mydb[self.col]
                break
            except:
                print("pymongo.MongoClient error: mongodb server not found pleas check host or port")
                time.sleep(3)
                continue

    def insert_db(self,str):
        # data=str.replace('\r','').replace('\n','').replace("m-mode",'m mode').replace("run","run info").replace("_",' ').replace("aut","aut info").replace("des","des info")
        data=json.loads(str)

        # 按網關名為數據庫名稱 電錶名為表名稱
        self.db=data["Gateway"]
        self.col=data["Port"]
        self.mydb = self.myclient[self.db]
        self.mycol = self.mydb[self.col]

        self.mycol.insert_one(data)
        self.Num=self.Num+1
        print("insert one document successful ",self.Num)

    def select_db(self,find):
        self.data =self.mycol.find(find)
        print("select data successful")


# pymo=python_mongodb()
# find={'devlist.0.varlist.0.readtime':{"$gt":"2018-10-04 00:00:00"}}
# pymo.select_db(find=find)
#
# for data in pymo.data:
#     data=data["devlist"][0]["varlist"][0]
#     data.pop("status")
#     data.pop("varid")
#     print(data)
# print(pymo.data.count())