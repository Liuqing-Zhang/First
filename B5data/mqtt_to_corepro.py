#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from B5_corepro.auth_corepro import auth_corepro
from B5_corepro.mqtt_pub_sub import mqtt_client_connect
from B5_corepro.for_mongodb import python_mongodb

def select_data(year=2018,month=10,day=11,hour=00,minute=00,second=00):

    lefttime = time.strftime("%Y-%m-%d %H:%M:%S", (year, month, day, hour, minute, second, 0, 0, 0))
    righttime=time.strftime("%Y-%m-%d %H:%M:%S", (year, month, day+1, hour, minute, second, 0, 0, 0))
    find = {'devlist.0.varlist.0.readtime': {"$gte": lefttime,"$lte":righttime}}
    pymo.select_db(find=find)
    print("Count: ", pymo.data.count()," time zones",lefttime,"--",righttime)
    return pymo.data


if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    數據為本地mongodb數據庫   
    """
    device=auth_corepro(
        ProductKey='6453668283668082833',
        DeviceName='P10XXK370',
        DeviceSecret='ff99aaa845774651edeebcad72a7b6810b8fa0f237bece49001476ab20f09fe4f0b648747b924999a3f5c3ba2ee31880463cff2f376c7df55fff31b917a85acc'
    )

    mqttClient=mqtt_client_connect(
        broker=device.mqtthost,
        port=device.mqttport,
        username=device.username,
        password=device.password)

    pymo = python_mongodb(
        host="localhost",
        port=27017,
        db="B5",
        col="Data"
    )

    mqttClient.mqttc.subscribe(
        topic="/"+device.ProductKey+"/"+device.DeviceName+"/property/post/reply",
        qos=1)

    load={}
    load["id"]="12345"
    load["msg_ver"]=None

    nmonth=10
    nday = 11
    while True:
        datas=select_data(year=2018,month=nmonth,day=nday,hour=8,minute=0)
        for data in datas:
            data = data["devlist"][0]["varlist"][0]
            # data.pop("status")
            # data.pop("varid")
            load["params"] = data
            payload = json.dumps(load)
            mqttClient.mqttc.publish(
                topic="/" + device.ProductKey + "/" + device.DeviceName + "/property/post",
                payload=payload,
                qos=1)
            time.sleep(3)

        nday=nday+1
        if nday>31:
            nmonth=nmonth+1
            nday=1

