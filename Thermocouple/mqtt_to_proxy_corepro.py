#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Thermocouple_corepro.serial_data import Ser
from Thermocouple_corepro.auth_corepro import auth_corepro
from Thermocouple_corepro.mqtt_pub_sub import mqtt_client_connect


if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    device1 = auth_corepro(
        ProductKey='241609820149379072',
        DeviceName='Thermostat01',
        DeviceSecret='39362854ede9157905236584d7c147e8c0964e390d21eb67a17ece3a4c49dcd9',
        auth_url='http://10.132.37.177:8088/auth/device/'
    )
    #Corepro MQTT broker
    proxymqttClient1=mqtt_client_connect(broker=device1.mqtthost,port=device1.mqttport,username=device1.username,password=device1.password,client_id=device1.username)
    # Corepro MQTT device Topic
    proxymqttClient1.mqttc.subscribe(topic="/"+device1.ProductKey+"/"+device1.DeviceName+"/property/post/reply",qos=1)
    while True:
        Pxr = Ser(port="COM3", baudrate=9600)
        Pxr.run(data="0x02 0x04 0x03 0xE8 0x00 0x02")
        data = {"Current_temperature": Pxr.PV, "set_value": Pxr.SV}
        timestamp = str(round(time.time() * 1000))
        load = {}
        load["id"] = timestamp
        load["msg_ver"] = "null"
        # load["msg_ver"] = yunmqttClient1.num
        load["params"] = data
        payload = json.dumps(load)
        proxymqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)
        proxymqttClient1.num=proxymqttClient1.num+1
        time.sleep(3)





