#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:45
# @Author  : userzhang
import pymongo
import json

class python_mongodb():

    def __init__(self):
        self.Num=1
        while True:
            try:
                self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                self.mydb = self.myclient["B5"]
                self.mycol = self.mydb["Data"]
                break
            except:
                print("mongodb server not found")
                continue


    def insert_db(self,str):

        data=str.replace('\r','').replace('\n','').replace("m-mode",'m mode').replace("run","run info").replace("_",' ').replace("aut","aut info").replace("des","des info")
        data=json.loads(data)
        self.mycol.insert_one(data)
        print("insert one document successful ",self.Num)
        self.Num=self.Num+1


    def select_db(self,find):
        self.data =self.mycol.find(find)
        print("select data successful")


# pymo=python_mongodb()
# find={'devlist.0.varlist.0.readtime':{"$gt":"2018-10-04 00:00:00"}}
# pymo.select_db(find=find)
#
#
# for data in pymo.data:
#     data=data["devlist"][0]["varlist"][0]
#     data.pop("status")
#     data.pop("varid")
#     print(data["readtime"])
# print(pymo.data.count())