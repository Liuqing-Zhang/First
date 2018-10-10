#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 8:09
# @Author  : userzhang

import time
import pymongo
import json
import datetime
from paho.mqtt.client import Client
from auth_corepro import auth_corepro
# from b5_mongodb import  python_mongodb

class mqtt_client_connect():

    def __init__(self,broker,port,username,password):
        self.broker=broker
        self.port=port
        self.username=username
        self.password=password
        self.payload=None
        while True:
            try:
                # self.mqttc=Client(clean_session=False,client_id="12345")
                self.mqttc = Client()
                self.mqttc.on_connect=self.on_connect
                self.mqttc.on_publish=self.on_publish
                self.mqttc.on_subscribe=self.on_subscribe
                self.mqttc.username_pw_set(self.username,self.password)
                self.mqttc.connect(self.broker)
                self.mqttc.loop_start()
                break
            except:
                print("mqtt_client_connect error: mqttc connect failed Please check Broker and Port....")
                time.sleep(3)
                continue
    # ======================================================
    def on_connect(self,client, userdata, flags, rc):
        #rc为0 返回连接成功
        if rc==0:
            print("OnConnetc, rc: " + str(rc), 'successful')
        else:
            print("OnConnetc, rc: " + str(rc), 'unsuccessful')


    def on_publish(self,client, userdata, mid):
        print("OnPublish, mid: " + str(mid))

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("订阅成功")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        self.mqttc.on_message = self.on_message

    def on_message(self,client, userdata, msg):
        curtime = datetime.datetime.now()
        strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #     self.payload=msg.payload
    #     self.insert_to_mongo()
    #
    #     # print(type(self.payload))
    # def insert_to_mongo(self):
    #     if not self.payload==None:
    #         data=str(self.payload,encoding="GBK")
    #
    #         pymo.insert_db(data)
    #     else:
    #         print("Waitting......")
    #     # =====================================================


if __name__ == "__main__":

    B5device=auth_corepro(
        ProductKey='6453668283668082833',
        DeviceName='P10XXK370',
        DeviceSecret='ff99aaa845774651edeebcad72a7b6810b8fa0f237bece49001476ab20f09fe4f0b648747b924999a3f5c3ba2ee31880463cff2f376c7df55fff31b917a85acc'
    )
    mqttClient=mqtt_client_connect(B5device.mqtthost,B5device.mqttport,B5device.username,B5device.password)
    mqttClient.mqttc.subscribe("/"+B5device.ProductKey+"/"+B5device.DeviceName+"/property/post/reply",qos=1)
    while True:
        mqttClient.mqttc.publish(
            topic="/" + B5device.ProductKey + "/" + B5device.DeviceName + "/property/post",
            payload='{"msg_ver":null,"id":"123456","params":[{"name":"userzhang","action":"test"}]}',
            qos=1)
        time.sleep(3)





