#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from B5_corepro.auth_corepro import auth_corepro
from B5_corepro.mqtt_pub_sub import mqtt_client_connect

class local_mqtt_client_connect(mqtt_client_connect):

    def on_message(self,client, userdata, msg):

        strcurtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        data=str(msg.payload,encoding="utf-8")
        data = json.loads(data)
        if data["devlist"][0]["deviceid"]=="P10XXK370":
            data1=data["devlist"][0]["varlist"][0]
            # data={"feed_rate":data1["feed_rate"],"spindle_speed":data1["spindle_speed"]}
            timestamp = str(round(time.time() * 1000))
            load = {}
            load["id"] = timestamp
            load["msg_ver"] = 1
            load["params"] = data1
            payload = json.dumps(load)
            # print(payload)
            yunmqttClient.mqttc.publish(topic="/" + device.ProductKey + "/" + device.DeviceName + "/property/post",payload=payload, qos=1)
        elif data["devlist"][0]["deviceid"] == "P115XK828":
            data1 = data["devlist"][0]["varlist"][0]
            # print(len(data1))
            # data = {"feed_rate": data1["feed_rate"], "spindle_speed": data1["spindle_speed"]}
            timestamp = str(round(time.time() * 1000))
            load = {}
            load["id"] = timestamp
            load["msg_ver"] = 1
            load["params"] = data1
            payload = json.dumps(load,ensure_ascii=False)
            # print(payload)
            yunmqttClient1.mqttc.publish(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post",payload=payload, qos=1)

if __name__ == "__main__":

    try:

        device=auth_corepro(
            ProductKey='242692703488307200',
            DeviceName='P10XXK370',
            DeviceSecret='dc56d128c8e0763f62b6d7711a6c3005e9e1a6dcc7a1ae16dd36a49b76b88aee',
            auth_url='http://110.139.136.146:8088/auth/device/'
        )
        device1 = auth_corepro(
            ProductKey='242692703488307200',
            DeviceName='P115XK828',
            DeviceSecret='ae943ecfbc060da828210b0ddf3e9b7708813240cbb2c2d626b07cb84fc76a7b',
            auth_url='http://110.139.136.146:8088/auth/device/'
        )
        timestamp = str(round(time.time() * 1000))
        # Corepro MQTT broker
        yunmqttClient=mqtt_client_connect(broker=device.mqtthost,port=device.mqttport,username=device.username,password=device.password,client_id=device.username)
        # Corepro MQTT device Topic
        yunmqttClient.mqttc.subscribe(topic="/"+device.ProductKey+"/"+device.DeviceName+"/property/post/reply",qos=1)
        # local MQTT broker

        # Corepro MQTT broker
        yunmqttClient1 = mqtt_client_connect(broker=device1.mqtthost, port=device1.mqttport, username=device1.username,password=device1.password, client_id=device1.username)
        # Corepro MQTT device Topic
        yunmqttClient1.mqttc.subscribe(topic="/" + device1.ProductKey + "/" + device1.DeviceName + "/property/post/reply",qos=1)
        # local MQTT broker
        localmqttClient = local_mqtt_client_connect(broker="10.132.44.123", port=1883, username="admin",password="password",client_id=timestamp)
        # local MQTT data Topic
        localmqttClient.mqttc.subscribe(topic="st/ftg18tl", qos=1)
        while True:
            pass
    except Exception as err:
        print(err)
        time.sleep(3)

