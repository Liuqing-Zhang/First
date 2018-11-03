#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 8:17
# @Author  : userzhang
import pymysql
db=pymysql.connect('127.0.0.1','root','123456','chamber')
cursor=db.cursor()
sql="""select * from chamber_info """
try:
    cursor.execute(sql)
    #獲取所有記錄列表
    results=cursor.fetchall()
    for row in results:
        Cone_set_value=row[0]
        Cone_temperature=row[1]
        #打印結果
        print('Cone_set_value=%s,Cone_temperature=%s'%(Cone_set_value,Cone_temperature))
except Exception as err:
    print(err)

db.close()
