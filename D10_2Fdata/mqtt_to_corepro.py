#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from D10_corepro.auth_corepro import auth_corepro
from D10_corepro.mqtt_pub_sub import mqtt_client_connect

class local_mqtt_client_connect(mqtt_client_connect):

    def on_message(self,client, userdata, msg):

        strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        payload=str(msg.payload,encoding="GBK")
        payload = json.loads(payload)
        payload=payload["devlist"][0]["varlist"][0]
        timestamp = str(round(time.time() * 1000))
        load = {}
        load["id"] = timestamp
        load["msg_ver"] = 1
        load["params"] = payload
        payload = json.dumps(load)
        yunmqttClient.mqttc.publish(topic="/" + device.ProductKey + "/" + device.DeviceName + "/property/post",
                                    payload=payload, qos=1)

if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    數據為本地mongodb數據庫   
    """
    #設備鑒權
    device=auth_corepro(
        ProductKey='6453668283668082833',
        DeviceName='P10XXK370',
        DeviceSecret='ff99aaa845774651edeebcad72a7b6810b8fa0f237bece49001476ab20f09fe4f0b648747b924999a3f5c3ba2ee31880463cff2f376c7df55fff31b917a85acc'
    )
    #Corepro MQTT broker
    yunmqttClient=mqtt_client_connect(broker=device.mqtthost,port=device.mqttport,username=device.username,password=device.password,client_id=device.username)


    # Corepro MQTT device Topic
    yunmqttClient.mqttc.subscribe(topic="/"+device.ProductKey+"/"+device.DeviceName+"/property/post/reply",qos=1)
    # local MQTT broker
    localmqttClient = local_mqtt_client_connect(broker="10.132.44.123", port=1883, username="admin",password="password")
    # local MQTT data Topic
    localmqttClient.mqttc.subscribe(topic="st/ftg18tl", qos=1)
    while True:
        pass
