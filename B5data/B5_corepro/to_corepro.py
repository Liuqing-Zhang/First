#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 16:55
# @Author  : userzhang

import auth_corepro
import requests
B5device=auth_corepro.auth_corepro()
params={
        "config":{
            "user_id":"7040310179"
        },
        "data":{
            'product_id': '6451261594457507856',
            'device_name': 'Cosmosdevice'
        }
}

r=requests.post(B5device.msglog_url,params=params)
data=r.text
print(data)

