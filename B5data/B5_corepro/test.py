#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 16:48
# @Author  : userzhang
import time
strcurtime=time.strptime('2018-9-30 11:32:23',"%Y-%m-%d %H:%M:%S")
ti=12
strcurtime=time.strftime("%Y-%m-%d %H:%M:%S",(2018, 9, 30, 12, 0, 0, 0, 0, 0))
print(type(strcurtime),strcurtime)
