#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 11:11
# @Author  : userzhang
import time
from B5_corepro.for_mongodb import python_mongodb
from B5_corepro.mqtt_pub_sub import mqtt_client_connect

# 重寫 on_message 函數
def on_message(client, userdata, msg):
    strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    payload=msg.payload
    if not payload==None:
        data = str(payload, encoding="GBK")
        pymo.insert_db(data)
    else:
        print("Waitting......")

if __name__ == "__main__":
    """
       通過本地mqtt服務器 訂閱到主題消息
       存儲在mongodb數據庫
    """
    mqttClient = mqtt_client_connect(
        broker="10.129.7.199",
        port=1883,
        username="iot",
        password="iot123!")

    pymo=python_mongodb(
        host="localhost",
        port=27017,
        db="B5",
        col="Data"
    )
    mqttClient.on_message = on_message
    mqttClient.mqttc.subscribe(
        topic="st/ftg18tl",
        qos=1)

    while True:
        pass




