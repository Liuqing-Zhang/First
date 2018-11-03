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
    Thermocouple = auth_corepro(
        ProductKey='6461078598027932362',
        DeviceName='Thermostat01',
        DeviceSecret='b7d2e34f9afa525d21c5992a684d35ea9a5f46877f69d5e9568011594f3876c4b6079bb4e446eda254d4b81b286391fcc7ac857b31f0f647181fa66fe3e9b675'
    )
    #Corepro MQTT broker
    yunmqttClient1=mqtt_client_connect(broker=Thermocouple.mqtthost,port=Thermocouple.mqttport,username=Thermocouple.username,password=Thermocouple.password,client_id=Thermocouple.username)
    # Corepro MQTT device Topic
    yunmqttClient1.mqttc.subscribe(topic="/"+Thermocouple.ProductKey+"/"+Thermocouple.DeviceName+"/property/post/reply",qos=1)

    while True:
        ser = Ser("COM7")
        ser.run()
        data = {"C1_temperature": ser.C1, "C1_set_value": ser.SP1}
        timestamp = str(round(time.time() * 1000))
        load = {}
        load["id"] = timestamp
        load["msg_ver"] ="null"
        # load["msg_ver"] = yunmqttClient1.num
        load["params"] = data
        payload = json.dumps(load)
        yunmqttClient1.mqttc.publish(topic="/" + Thermocouple.ProductKey + "/" + Thermocouple.DeviceName + "/property/post",payload=payload, qos=1)
        yunmqttClient1.num=yunmqttClient1.num+1
        time.sleep(3)





