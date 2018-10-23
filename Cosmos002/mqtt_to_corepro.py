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
        ProductKey='6459976247993086025',
        DeviceName='Cosmosdevice01',
        DeviceSecret='62ffdeddf56ad0df75efc7f29813885dda84d1d068fe60413ce922493355f4916e72378ac7548558d14ddc9db513bc5b1e8e2aa40196aa1118fb4e0acda49d12'
    )
    device2 = auth_corepro(
        ProductKey='6459976247993086025',
        DeviceName='Cosmosdevice02',
        DeviceSecret='6d893b235fa853e74802b86105d00e4bbd80dcf9cfb00dcf24a63f7c491bd1c3d0b9c33ca076ab77b1f24bbdec0d97bdbf57afb7df7cefcdfdfa1cd0b65aa984'
    )
    # device1 = auth_corepro(
    #     ProductKey='6453668283668082833',
    #     DeviceName='P10XXK370',
    #     DeviceSecret='ff99aaa845774651edeebcad72a7b6810b8fa0f237bece49001476ab20f09fe4f0b648747b924999a3f5c3ba2ee31880463cff2f376c7df55fff31b917a85acc'
    # )
    # device2 = auth_corepro(
    #     ProductKey='6453668283668082833',
    #     DeviceName='P115XK828',
    #     DeviceSecret='188c8a493e14354ed0ae164db678ff55446f97a13abfd3430f2e6f98f8d3b6dfe7b48efae725977c15af5f1207efd7b462ab4d8a3e556e15c856cc940b0c2a6e'
    # )
    #Corepro MQTT broker
    yunmqttClient1=mqtt_client_connect(broker=device1.mqtthost,port=device1.mqttport,username=device1.username,password=device1.password,client_id=device1.username)
    # Corepro MQTT device Topic
    yunmqttClient1.mqttc.subscribe(topic="/"+device1.ProductKey+"/"+device1.DeviceName+"/property/post/reply",qos=1)
    # Corepro MQTT broker
    yunmqttClient2 = mqtt_client_connect(broker=device2.mqtthost, port=device2.mqttport, username=device2.username,password=device2.password, client_id=device2.username)
    # Corepro MQTT device Topic
    yunmqttClient2.mqttc.subscribe(topic="/" + device2.ProductKey + "/" + device2.DeviceName + "/property/post/reply",qos=1)


    while True:
        with open("CPUstationlog.txt", "r+") as target:
            lines = target.readlines()
            for line in lines:
                strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
                line=line.replace("\n","").replace("_","").replace("seq","seqNum").replace("'","\"")
                line=json.loads(line)
                line["rectime"]=strcurtime
                payload = json.dumps(line)
                # print(payload)
                yunmqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)
                yunmqttClient2.mqttc.publish(topic="/" + device2.ProductKey + "/" + device2.DeviceName + "/property/post",payload=payload, qos=1)
                time.sleep(3)




