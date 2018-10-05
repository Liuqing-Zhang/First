#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang


# # 获取最新的31条信息
# import auth_corepro
# import requests
# import json
# B5device=auth_corepro.auth_corepro()
# params={
#         "config":'{"user_id":"7040310179"}',
#         "data":"{'product_id': '6451261594457507856','device_name': 'Cosmosdevice'}"
# }
# print(B5device.msglog_url)
# r=requests.post(B5device.msglog_url,data=params)
#
# data=r.text
# print(len(json.loads(data)['payload']))
