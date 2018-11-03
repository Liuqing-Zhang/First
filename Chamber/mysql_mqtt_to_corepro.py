#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang
import time
import json
from Chamber_corepro.auth_corepro import auth_corepro
from Chamber_corepro.mqtt_pub_sub import mqtt_client_connect
from Chamber_corepro.serial_data import Ser
import pymysql

if __name__ == "__main__":
    """
    通過設備的三元組獲得設備的mqtt地址以及username password
    平台設備上線 發佈設備topic上傳數據 
    """
    #設備鑒權
    Thermocouple = auth_corepro(
        ProductKey='6462819109098411118',
        DeviceName='Chamber0001',
        DeviceSecret='0ec3d603a3e1f1d5a25352cc97eece4a6809acfa9eb390ed88d8a980fb6976c946eb2885c0ae3fbc14c092a4879bda975c49d5a16a44f5feef24de5679f91ff5'
    )
    #Corepro MQTT broker
    yunmqttClient1=mqtt_client_connect(broker=Thermocouple.mqtthost,port=Thermocouple.mqttport,username=Thermocouple.username,password=Thermocouple.password,client_id=Thermocouple.username)
    # Corepro MQTT device Topic
    yunmqttClient1.mqttc.subscribe(topic="/"+Thermocouple.ProductKey+"/"+Thermocouple.DeviceName+"/property/post/reply",qos=1)

    while True:

        db = pymysql.connect('127.0.0.1', 'root', '123456', 'chamber')
        cursor = db.cursor()
        sql = """select * from chamber_info"""
        try:
            cursor.execute(sql)
            # 獲取所有記錄列表
            results = cursor.fetchall()
            for row in results:
                # ser = Ser("COM7")
                # ser.run()
                data = {"Cone_set_value": row[0], "Cone_temperature": row[1]}
                timestamp = str(round(time.time() * 1000))
                load = {}
                load["id"] = timestamp
                load["msg_ver"] = "null"
                # load["msg_ver"] = yunmqttClient1.num
                load["params"] = data
                payload = json.dumps(load)
                yunmqttClient1.mqttc.publish(
                    topic="/" + Thermocouple.ProductKey + "/" + Thermocouple.DeviceName + "/property/post",
                    payload=payload, qos=1)
                yunmqttClient1.num = yunmqttClient1.num + 1
                time.sleep(3)
                # 打印結果
                # print('Cone_set_value=%s,Cone_set_value=%s'%(Cone_set_value,Cone_temperature))
        except:
            print("Error:unable to fetch data")

        db.close()






