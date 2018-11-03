#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Cosmos_corepro.auth_corepro import auth_corepro
from Cosmos_corepro.mqtt_pub_sub import mqtt_client_connect


if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    device1 = auth_corepro(
        ProductKey='240185199697063936',
        DeviceName='Gatway1',
        DeviceSecret='b5a776deb0fc47415980556c92cb2c00e0ad267c5cf07362d75317a16b48189d',
        auth_url='http://10.132.37.177:8088/auth/device/'
    )
    #Corepro MQTT broker
    proxymqttClient1=mqtt_client_connect(broker=device1.mqtthost,port=device1.mqttport,username=device1.username,password=device1.password,client_id=device1.username)
    # Corepro MQTT device Topic
    proxymqttClient1.mqttc.subscribe(topic="/"+device1.ProductKey+"/"+device1.DeviceName+"/property/post/reply",qos=1)
    while True:
        timestamp = str(round(time.time() * 1000))
        load={}
        load["id"]=timestamp
        load["msg_ver"] =proxymqttClient1.num
        load["params"]={'ip':"10.167.198.111",'status':'run'}
        payload = json.dumps(load)
        proxymqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)
        proxymqttClient1.num=proxymqttClient1.num+1
        time.sleep(3)





