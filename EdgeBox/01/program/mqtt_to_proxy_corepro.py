#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Cosmos_corepro.mqtt_pub_sub import mqtt_client_connect
import sys

if __name__ == "__main__":
    for i in sys.argv:
        print(i)
    #Corepro MQTT broker
    proxymqttClient1=mqtt_client_connect(broker=sys.argv[1],port=int(sys.argv[2]),username=sys.argv[3],password=sys.argv[4],client_id=sys.argv[3])
    # Corepro MQTT device Topic
    proxymqttClient1.mqttc.subscribe(topic="/"+sys.argv[5]+"/"+sys.argv[6]+"/property/post/reply",qos=1)
    while True:
        timestamp = str(round(time.time() * 1000))
        load={}
        load["id"]=timestamp
        load["msg_ver"] =proxymqttClient1.num
        load["params"]={'ip':timestamp,'status':'run'}
        payload = json.dumps(load)
        proxymqttClient1.mqttc.publish(topic="/" + sys.argv[5] + "/" + sys.argv[6] + "/property/post",payload=payload, qos=1)
        proxymqttClient1.num=proxymqttClient1.num+1
        time.sleep(3)





