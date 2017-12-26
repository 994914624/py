#!/usr/bin/env python
# -*- coding: utf-8 -*-

'  test '
__author__ = 'yang'

import logging
logging.basicConfig(level=logging.INFO)
import sys
import os  
import time
import subprocess

# #subprocess 方式
# order='adb logcat'
# pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
# for i in iter(pi.stdout.readline,'b'):
#     print i

# # 打开系统设置页面
# print('adb shell am start -n com.android.settings/.Settings')
# os.system('adb shell am start -n com.android.settings/.Settings')
# # adb logcat 抓日志
# print('adb logcat -v time')
# os.system('adb logcat -v time')
