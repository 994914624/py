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



print('qwewretrt'.__contains__('we')==False)

strlen=len('java.lang.RuntimeException: Unable to create application cn.sensorsdata.demo.MyApplication: java.lang.NullPointerException: Attempt to invoke virtual method \'java.lang.String java.lang.String.toString()\' on a null object reference at android.app.ActivityThread.handleBindApplication(ActivityThread.java:4768) at android.app.ActivityThread.access$1700(ActivityThread.java:153) at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1436) at android.os.Handler.dispatchMessage(Handler.java:102) at android.os.Looper.loop(Looper.java:154) at android.app.ActivityThread.main(ActivityThread.java:5527) at java.lang.reflect.Method.invoke(Native Method) at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739) at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:629) Caused by: java.lang.NullPointerException: Attempt to invoke virtual method \'java.lang.String java.lang.String.toString()\' on a null object reference at cn.sensorsdata.demo.MyApplication.initSensorsDataAPI(My$'.encode('utf-8'))
print ('字符串长度%s'%strlen)

#os.system("adb shell am broadcast -a com.umeng.auto.track --es param \"" + str(es) + "\"  --ei caseId " + bytes(ei))