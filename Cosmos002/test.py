#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 15:42
# @Author  : userzhang
import json


with open("CPUstationlog.txt", "r+") as target:
    lines = target.readlines()
    for line in lines:

        data = line.replace("\n", "").replace("_", "").replace("seq", "seqNum").replace("'", "\"")
        data=json.loads(data,encoding="utf-8")
        print(data["seqNum"])