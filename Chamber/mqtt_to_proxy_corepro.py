#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang

import time
import json
from Chamber_corepro.auth_corepro import auth_corepro
from Chamber_corepro.mqtt_pub_sub import mqtt_client_connect
from Chamber_corepro.serial_data import Ser

if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    device1 = auth_corepro(
        ProductKey='240917282203627520',
        DeviceName='Chamber01',
        DeviceSecret='facfae00ab8d669ce0a36790fb633f18fb50713527786a62fb465cf5aa3bf48e',
        auth_url='http://10.132.37.177:8088/auth/device/'
    )
    #Corepro MQTT broker
    proxymqttClient1=mqtt_client_connect(broker=device1.mqtthost,port=device1.mqttport,username=device1.username,password=device1.password,client_id=device1.username)
    # Corepro MQTT device Topic
    proxymqttClient1.mqttc.subscribe(topic="/"+device1.ProductKey+"/"+device1.DeviceName+"/property/post/reply",qos=1)
    while True:
        ser=Ser("COM7")
        ser.run()
        data={"C1_temperature":ser.C1,"C1_set_value":ser.SP1}
        timestamp = str(round(time.time() * 1000))
        load={}
        load["id"]=timestamp
        load["msg_ver"] =proxymqttClient1.num
        load["params"]=data
        payload = json.dumps(load)
        proxymqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)
        proxymqttClient1.num=proxymqttClient1.num+1
        time.sleep(3)





