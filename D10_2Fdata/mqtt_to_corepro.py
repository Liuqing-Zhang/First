#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from D10_corepro.auth_corepro import auth_corepro
from D10_corepro.mqtt_pub_sub import mqtt_client_connect
from D10_corepro.format_three_phase import format_three_phase

class local_mqtt_client_connect(mqtt_client_connect):

    def on_message(self,client, userdata, msg):

        strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        payload=str(msg.payload,encoding="GBK")
        payload = json.loads(payload)
        data=format_three_phase(payload)
        # print(data)
        timestamp = str(round(time.time() * 1000))
        load = {}
        load["id"] = timestamp
        load["msg_ver"] = "null"
        load["params"] = data
        # print(load)
        payload = json.dumps(load)
        yunmqttClient.mqttc.publish(topic="/" + device.ProductKey + "/" + device.DeviceName + "/property/post",payload=payload, qos=1)
        # self.num=self.num+1

if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    device=auth_corepro(
        ProductKey='6447904538381752188',
        DeviceName='D10-2F-WG1',
        DeviceSecret='ab0bfe30f7218535aa41577c9ed81091b042dc7f7a2c5bb6edd6c496059eba34ebb97ac09f202389cf136a39675c6bbcf492df1745741a9c99c588034caff7a3'
    )
    # device = auth_corepro(
    #     ProductKey='6459976247993086025',
    #     DeviceName='Cosmosdevice01',
    #     DeviceSecret='62ffdeddf56ad0df75efc7f29813885dda84d1d068fe60413ce922493355f4916e72378ac7548558d14ddc9db513bc5b1e8e2aa40196aa1118fb4e0acda49d12'
    # )
    # device = auth_corepro(
    #     ProductKey='6459976247993086025',
    #     DeviceName='Cosmosdevice02',
    #     DeviceSecret='6d893b235fa853e74802b86105d00e4bbd80dcf9cfb00dcf24a63f7c491bd1c3d0b9c33ca076ab77b1f24bbdec0d97bdbf57afb7df7cefcdfdfa1cd0b65aa984'
    # )
    #Corepro MQTT broker
    yunmqttClient=mqtt_client_connect(broker=device.mqtthost,port=device.mqttport,username=device.username,password=device.password,client_id=device.username)
    # Corepro MQTT device Topic
    yunmqttClient.mqttc.subscribe(topic="/"+device.ProductKey+"/"+device.DeviceName+"/property/post/reply",qos=1)
    # local MQTT broker
    localmqttClient = local_mqtt_client_connect(broker="10.129.7.199", port=1883, username="iot",password="iot123!",client_id="123456789")
    # local MQTT data Topic
    localmqttClient.mqttc.subscribe(topic="nsd1/meter", qos=1)
    while True:
        pass
