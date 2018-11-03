#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Cosmos_corepro.mqtt_pub_sub import mqtt_client_connect
import sys
class run(object):
    def __init__(self,broker,port,username,password,client_id,ProductKey,DeviceName,flag=1):
        self.broker=broker
        self.port=port
        self.username=username
        self.password=password
        self.client_id=client_id
        self.ProductKey=ProductKey
        self.DeviceName=DeviceName
        self.flag=flag
    def main(self):
        #Corepro MQTT broker
        proxymqttClient1=mqtt_client_connect(broker=self.broker,port=int(self.port),username=self.username,password=self.password,client_id=self.client_id)
        # Corepro MQTT device Topic
        proxymqttClient1.mqttc.subscribe(topic="/"+self.ProductKey+"/"+self.DeviceName+"/property/post/reply",qos=1)
        while True:
            if self.flag==1:
                timestamp = str(round(time.time() * 1000))
                load={}
                load["id"]=timestamp
                load["msg_ver"] =proxymqttClient1.num
                load["params"]={'ip':timestamp,'status':'run'}
                payload = json.dumps(load)
                proxymqttClient1.mqttc.publish(topic="/" + self.ProductKey + "/" + self.DeviceName + "/property/post",payload=payload, qos=1)
                proxymqttClient1.num=proxymqttClient1.num+1
                time.sleep(3)
            else:
                proxymqttClient1.mqttc.disconnect()
                break
            # return proxymqttClient1.num





