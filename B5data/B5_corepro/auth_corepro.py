#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 15:48
# @Author  : userzhang
import hashlib
import hmac
import time
import requests
import json

class auth_corepro():

    def __init__(self,ProductKey='6453387282597968558',DeviceName='B5device',DeviceSecret='b442f2b99ecfd290ebf28f42b31266187fd23aedd24393f509fd412097100f4e318f047d53d61af2e461c5e41ad6cee89e65b1063d7eead2bb9914637cbed414'):

        ############ B5device 三元組 ###################
        self.ProductKey = ProductKey
        self.DeviceName = DeviceName
        self.DeviceSecret = DeviceSecret
        ##################################################


        ########################鑒權URL#################
        self.auth_url = 'https://service-o8bikfta-1256676747.ap-guangzhou.apigateway.myqcloud.com/release/corepro_deviceauth/mqtt_auth?X-MicroService-Name=beacon-corepro-deviceauth&X-NameSpace-Code=default-code'
        self.msglog_url = 'https://service-o8bikfta-1256676747.ap-guangzhou.apigateway.myqcloud.com/release/corepro/equipment/device/msglog/?X-MicroService-Name=beacon-corepro-equipment-new&X-NameSpace-Code=default-code'
        ###############################################



        ########## MQTT 服務器 topic ########################################
        self.mqttHost = '193.112.225.54'
        self.mqttPort = 1883
        self.pub_topic='/' + self.ProductKey + self.DeviceName + '/property/post'
        self.sub_topic='/' + self.ProductKey + self.DeviceName + '/property/post/reply'
        ##################################################

        self.get_auth_sign()
        self.get_username_pwd()

    def get_auth_sign(self):

        DeviceSecret = bytearray.fromhex(self.DeviceSecret)
        self.timestamp = str(round((time.time() * 1000)))
        sign_content = ''.join(('deviceName', self.DeviceName, 'productKey', self.ProductKey, 'timestamp', self.timestamp))
        sign_content = bytes(sign_content, encoding='utf-8')
        sign_method = hashlib.sha256
        self.sign = hmac.new(DeviceSecret, sign_content, sign_method).hexdigest()

    def get_username_pwd(self):

        params={  "productKey":self.ProductKey,
                  "deviceName":self.DeviceName,
                  "sign":self.sign,
                  "timestamp":self.timestamp,
                  "signmethod":"HmacSHA256"
                }

        r=requests.post(self.auth_url,data=params)
        data=r.text
        data=json.loads(data)
        self.username=data["payload"][0]["iotId"]
        self.password=data["payload"][0]["iotToken"]

# B5device=auth_corepro(
#     ProductKey='6453387282597968558',
#     DeviceName='B5device',
#     DeviceSecret='b442f2b99ecfd290ebf28f42b31266187fd23aedd24393f509fd412097100f4e318f047d53d61af2e461c5e41ad6cee89e65b1063d7eead2bb9914637cbed414'
# )
# print("B5device 鉴权成功！................")
