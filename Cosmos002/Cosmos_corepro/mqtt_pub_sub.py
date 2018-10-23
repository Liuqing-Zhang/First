#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 8:09
# @Author  : userzhang

import time
from paho.mqtt.client import Client


class mqtt_client_connect():

    def __init__(self,broker="10.129.7.199",port=1883,username="iot",password="iot123!",client_id="12345"):
        self.broker=broker
        self.port=port
        self.username=username
        self.password=password
        self.payload=None
        self.client_id=client_id
        self.num=1
        while True:
            try:
                # self.mqttc=Client(clean_session=False,client_id="12345")
                self.mqttc = Client(client_id=self.client_id)
                self.mqttc.on_connect=self.on_connect
                self.mqttc.on_publish=self.on_publish
                self.mqttc.on_subscribe=self.on_subscribe
                self.mqttc.username_pw_set(self.username,self.password)
                self.mqttc.connect(self.broker)
                self.mqttc.loop_start()
                break
            except:
                print("mqtt_client_connect error: mqttc connect failed Please check Broker and Port....")
                continue
    # ======================================================
    def on_connect(self,client, userdata, flags, rc):
        #rc为0 返回连接成功
        if rc==0:
            print("OnConnetc, rc: " + str(rc), 'successful  '+str(client._username).split("_")[1][:-1])
        else:
            print("OnConnetc, rc: " + str(rc), 'unsuccessful  '+str(client._username).split("_")[1][:-1])

    def on_disconnect(self,client, userdata, rc):
        if rc != 0:
            print("Unexpected MQTT disconnection. Will auto-reconnect")

    def on_publish(self,client, userdata, mid):
        print("OnPublish, mid: " + str(mid)+" "+str(client._username).split("_")[1][:-1])

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + "   " + str(granted_qos)+"  订阅成功 "+str(client._username).split("_")[1][:-1])
        self.mqttc.on_message = self.on_message

    def on_message(self,client, userdata, msg):
        strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload)+str(client._username).split("_")[1][:-1])









