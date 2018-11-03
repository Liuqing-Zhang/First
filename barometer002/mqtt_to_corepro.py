#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Barometer_corepro.auth_corepro import auth_corepro
from Barometer_corepro.mqtt_pub_sub import mqtt_client_connect


if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    device1 = auth_corepro(
        ProductKey='6461014146573972956',
        DeviceName='barometer001',
        DeviceSecret='33aaf6a78765c03c17040ce808fd4e97d66d3123fac087c95ecb165988e3e7e3bda3575c115607b747386cc64cc772dcf3a75ffc20a4ee6ad7c1fd22cba28ca7'
    )
    #Corepro MQTT broker
    yunmqttClient1=mqtt_client_connect(broker=device1.mqtthost,port=device1.mqttport,username=device1.username,password=device1.password,client_id=device1.username)
    # Corepro MQTT device Topic
    yunmqttClient1.mqttc.subscribe(topic="/"+device1.ProductKey+"/"+device1.DeviceName+"/event/DeviceLogion/post/reply",qos=1)

    while True:
        timestamp = str(round(time.time() * 1000))
        load = {}
        load["id"] = timestamp
        load["msg_ver"] =yunmqttClient1.num
        load["params"]={"Controller":"","Vers":"","Type":"","EquipmentID":"","RebootEvent":"","Time":"","IPNUM":"","MACS":"","RSSID":""}
        payload = json.dumps(load)
        # print(payload)
        # yunmqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/event/DeviceLogion/post",payload=payload, qos=1)
        yunmqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)
        yunmqttClient1.num=yunmqttClient1.num+1
        time.sleep(3)
                #




