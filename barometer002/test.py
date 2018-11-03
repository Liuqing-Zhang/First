#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 15:42
# @Author  : userzhang
import serial

b=b"\x13\x1144\r"
a=str(b,encoding="utf-8")
num=str(b)[2:-3].split(r"\x")[2]

print(round(int(num,16)/100,2))

b="\x1143"
print(str(b))