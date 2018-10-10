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
b=b'{\r\n  "gwid": "70208430AC23",\r\n  "gwmode": "type_child_12e2edf65e5b11e8ab8d005056b6166b",\r\n  "m-mode": "90",\r\n  "devlist": [\r\n    {\r\n      "deviceid": "",\r\n      "varlist": [\r\n        {\r\n          "status": null,\r\n          "speed_f": "100",\r\n          "speed_s": "0",\r\n          "load": "0",\r\n          "current_time": "1:00",\r\n          "program_name": "O8363",\r\n          "program_num": "8363",\r\n          "alarm": "",\r\n          "alarm_msg": "\xc4\xe3\xba\xc3",\r\n          "offset": "",\r\n          "run": "3",\r\n          "aut": "1",\r\n          "cnc_ip": "10.153.20.83",\r\n          "device_ip": "10.148.88.220",\r\n          "cnc_mac": "",\r\n          "part_count": "324",\r\n          "spindle_temperature": "46",\r\n          "feedrate_override": "0%",\r\n          "rapid_override": "25%",\r\n          "des": "P10XXK370",\r\n          "readtime": "2018-10-08 08:44:39",\r\n          "varname": "ftg18tl_mixed",\r\n          "varid": "driver_0bf5c1ba5e5811e8a9af005056c00008"\r\n        }\r\n      ]\r\n    }\r\n  ]\r\n}'
# b=str(b,encoding="utf-8")


print(b)
S=str(b,encoding="GBK")
print(type(S),S)
