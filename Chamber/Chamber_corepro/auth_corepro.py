#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 15:48
# @Author  : userzhang

import hashlib
import hmac
import time
import json
import requests


class auth_corepro(object):

    def __init__(self,ProductKey='6453387282597968558',DeviceName='B5device',DeviceSecret='b442f2b99ecfd290ebf28f42b31266187fd23aedd24393f509fd412097100f4e318f047d53d61af2e461c5e41ad6cee89e65b1063d7eead2bb9914637cbed414',auth_url='https://service-o8bikfta-1256676747.ap-guangzhou.apigateway.myqcloud.com/release/corepro_deviceauth/mqtt_auth?X-MicroService-Name=beacon-corepro-deviceauth&X-NameSpace-Code=default-code'):

        # ---------------- device 三元組 --------------------
        self.ProductKey = ProductKey
        self.DeviceName = DeviceName
        self.DeviceSecret = DeviceSecret

        # --------------------- 鑒權URL -----------------------
        self.auth_url = auth_url
        self.msglog_url = 'https://service-o8bikfta-1256676747.ap-guangzhou.apigateway.myqcloud.com/release/corepro/equipment/device/msglog/?X-MicroService-Name=beacon-corepro-equipment-new&X-NameSpace-Code=default-code'

        # ------sign timestamp username password mqtthost mqttport  -----
        self.sign=None
        self.timestamp=None
        self.username = None
        self.password = None
        self.mqtthost = None
        self.mqttport = None

        self.get_auth_sign()
        self.get_username_pwd()

    # ------------------ 获取sign 签名 -----------------------------------
    def get_auth_sign(self):
        DeviceSecret = bytearray.fromhex(self.DeviceSecret)
        self.timestamp = str(round((time.time() * 1000)))
        # print(self.timestamp)
        sign_content = ''.join(('clientId',self.ProductKey,'-',self.DeviceName,'deviceName', self.DeviceName, 'productKey', self.ProductKey, 'timestamp', self.timestamp))
        sign_content = bytes(sign_content, encoding='utf-8')
        sign_method = hashlib.sha256
        self.sign = hmac.new(DeviceSecret, sign_content, sign_method).hexdigest()
        # print(self.sign)

    # -------------------- post请求 获取Token -----------------------------
    def get_username_pwd(self):
        while True:
            try:
                params={  "productKey":self.ProductKey,
                          "deviceName":self.DeviceName,
                          "sign":self.sign,
                          "timestamp":self.timestamp,
                          "signmethod":"HmacSHA256",
                          "clientId":self.ProductKey+'-'+self.DeviceName
                        }

                r=requests.post(self.auth_url,data=params,timeout=60)
                data=r.text
                data=json.loads(data)
                # print(type(data))
                if not data["errmsg"]=="":
                    print(self.DeviceName," 鉴权失败！................     error1: device is forbidden")
                    time.sleep(3)

                elif data["errmsg"]=="":
                    self.mqtthost = data["payload"][0]["iotHost"]
                    self.mqttport = data["payload"][0]["iotPort"]
                    self.username=data["payload"][0]["iotId"]
                    self.password=data["payload"][0]["iotToken"]
                    print("mqtthost:",self.mqtthost+"  mqttport:",self.mqttport)
                    print("username:",self.username+"  password:",self.password)

                    # print(data)
                    print(self.DeviceName," 鉴权成功！................")
                    break
            except:
                print("requests.post error： Http Connect failed or Timeout please check you network")
                time.sleep(3)
                continue



#  # 实例
# B5device=auth_corepro(
#     ProductKey='6453668283668082833',
#     DeviceName='P115XK828',
#     DeviceSecret='188c8a493e14354ed0ae164db678ff55446f97a13abfd3430f2e6f98f8d3b6dfe7b48efae725977c15af5f1207efd7b462ab4d8a3e556e15c856cc940b0c2a6e'
# )
#
# print(B5device.username,B5device.password,B5device.mqtthost,B5device.mqttport)

# B5device=auth_corepro(
#     ProductKey='6453668283668082833',
#     DeviceName='6453668283668082833_P10XXK370',
#     DeviceSecret='ff99aaa845774651edeebcad72a7b6810b8fa0f237bece49001476ab20f09fe4f0b648747b924999a3f5c3ba2ee31880463cff2f376c7df55fff31b917a85acc'
# )
#
# print(B5device.username,B5device.password,B5device.mqtthost,B5device.mqttport)
