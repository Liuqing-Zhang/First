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
                self.mydb = self.myclient["userinfo"]
                self.mycol = self.mydb["B5"]
                break
            except:
                print("mongodb server not found")
                continue


    def insert_db(self,str):

        data=str.replace('\r','').replace('\n','').replace("m-mode",'mmode')
        data=json.loads(data)
        self.mycol.insert_one(data)
        print("insert one document successful ",self.Num)
        self.Num=self.Num+1
