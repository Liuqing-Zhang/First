#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 8:09
# @Author  : userzhang
import time

import pymongo
import json
import datetime
from paho.mqtt.client import Client
from b5_mongodb import python_mongodb

class mqtt_client_connect():

    def __init__(self,broker,port,username,password):
        self.broker=broker
        self.port=port
        self.username=username
        self.password=password
        self.payload=None
        self.mqttc=Client(clean_session=False,client_id="12345")
        self.mqttc.on_connect=self.on_connect
        self.mqttc.on_publish=self.on_publish
        self.mqttc.on_subscribe=self.on_subscribe

        self.mqttc.username_pw_set(self.username,self.password)
        self.mqttc.connect(self.broker)
        self.mqttc.loop_start()
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
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

        self.mqttc.on_message = self.on_message

    def on_message(self,client, userdata, msg):
        curtime = datetime.datetime.now()
        strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        self.payload=msg.payload
        self.insert_to_mongo()

        # print(type(self.payload))
    def insert_to_mongo(self):
        if not self.payload==None:
            data=str(self.payload,encoding="utf-8")
            pymo.insert_db(data)
        else:
            print("Waitting......")
        # =====================================================



if __name__=="__main__":
    pymo = python_mongodb()
    mqttClient=mqtt_client_connect("10.129.7.199",'1883','iot','iot123!')
    mqttClient.mqttc.subscribe("st/ftg18tl",qos=1)
    print("订阅成功")

    while True:
       pass





