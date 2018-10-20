# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 18:31
# @Author  : userzhang
import re
import pymysql
with open("9-27-16.sta","r+") as target:
    lines=target.readlines()
    data = {}
    dic = []
    n=0
    for line in lines:
        if re.match("日期",line):
            n = n + 1
            data[str(n)]={}
            line=line.replace("\n", '')
            line=line.replace(" ",'')
            data[str(n)]["日期"]=line.split("时间:")[0][3:]
            # data["日期"]=
            data[str(n)]["时间"]=line.split("时间:")[1]
        else:
            line=line.replace(" ",'').replace("\n",'')
            line=line.split(":")
            data[str(n)][line[0]]=line[1]
            if re.search("设定值",line[1]):
                value = line[1].replace("设定值", ",").replace("实际值", ",").replace("温区状态", ",")
                value = value.split(",")
                dic.append(value[0])
                dic.append(value[1])
                dic.append(value[2])
                dic.append(value[3])
print

db=pymysql.connect(host='10.167.198.187',user='root',password='admin',charset="utf8mb4",db='9-27-16')
cursor=db.cursor()
print("創建游標成功")
try:
    sql1="delete from 9_27_16"
    sql3="delete from 9_27_16_state"
    cursor.execute(sql1)
    cursor.execute(sql3)
    db.commit()
    print("delete successful")
except:
    print("rollback")
    db.rollback()

for i in range(1,len(data)+1):
    i=str(i)
    sql1='insert into 9_27_16 values("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}")'.format(data[i]["日期"],data[i]["时间"],data[i]["设备状态"],data[i]["供电状况"],data[i]["热风马达"],data[i]["运输马达"],data[i]["掉板状况"],data[i]["盖子"],data[i]["紧急制"],data[i]["后备电源"])
    try:
        cursor.execute(sql1)
        db.commit()
        print("commit 9_27_16")
    except:
        print("rollback")
        db.rollback()
i=0
n=1
for j in range(0,len(dic),4):
    if i%(24*4)==0:
        n=n+1
    sql2='insert into 9_27_16_state values("{0}","{1}","{2}","{3}","{4}","{5}")'.format(dic[j],dic[j+1],dic[j+2],dic[j+3],data[str(n)]["日期"],data[str(n)]["时间"])
    try:
        cursor.execute(sql2)
        db.commit()
        print("commit 9_27_16_state")
        i=i+1
    except:
        print("rollback")
        db.rollback()
cursor.close()







