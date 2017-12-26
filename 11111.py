#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')



"app_crashed_reason":"android.app.ActivityThread.handleBindApplication(ActivityThread.java:4768)\nandroid.app.ActivityThread.access$1700(ActivityThread.java:153)\nandroid.app.ActivityThread$H.handleMessage(ActivityThread.java:1436)\nandroid.os.Handler.dispatchMessage(Handler.java:102)\nandroid.os.Looper.loop(Looper.java:154)\nandroid.app.ActivityThread.main(ActivityThread.java:5527)\njava.lang.reflect.Method.invoke(Native Method)\ncom.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739)\ncom.android.internal.os.ZygoteInit.main(ZygoteInit.java:629)\n",




android.app.ActivityThread.handleBindApplication(ActivityThread.java:4768) 
android.app.ActivityThread.access$1700(ActivityThread.java:153) 
android.app.ActivityThread$H.handleMessage(ActivityThread.java:1436) 
android.os.Handler.dispatchMessage(Handler.java:102) android.os.Looper.loop(Looper.java:154) 
android.app.ActivityThread.main(ActivityThread.java:5527) 
java.lang.reflect.Method.invoke(Native Method) 
com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739) 
com.android.internal.os.ZygoteInit.main(ZygoteInit.java:629)

app_crashed_reason":"java.lang.RuntimeException: Unable to create application cn.sensorsdata.demo.MyApplication: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.toString()' on a null object reference\n\tat 
android.app.ActivityThread.handleBindApplication(ActivityThread.java:4768)\n
\tat android.app.ActivityThread.access$1700(ActivityThread.java:153)\n
\tat android.app.ActivityThread$H.handleMessage(ActivityThread.java:1436)\n
\tat android.os.Handler.dispatchMessage(Handler.java:102)\n
\tat android.os.Looper.loop(Looper.java:154)\n\tat android.app.ActivityThread.main(ActivityThread.java:5527)\n
\tat java.lang.reflect.Method.invoke(Native Method)\n\tat com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739)\n
\tat com.android.internal.os.ZygoteInit.main(ZygoteInit.java:629)\n
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.toString()' on a null object reference\n\tat 
cn.sensorsdata.demo.MyApplication.initSensorsDataAPI(MyApplication.java:251)\n\
tat cn.sensorsdata.demo.MyApplication.onCreate(MyApplication.java:100)\n\tat android.app.Instrumentation.callApplicationOnCreate(Instrumentation.java:1014)\n\tat android.app.ActivityThread.handleBindApplication(ActivityThread.java:4765)\n\t... 8 more\njava.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.toString()' on a null object reference\n\tat cn.sensorsdata.demo.MyApplication.initSensorsDataAPI(MyApplication.java:251)\n\tat cn.sensorsdata.demo.MyApplication.onCreate(MyApplication.java:100)\n\tat android.app.Instrumentation.callApplicationOnCreate(Instrumentation.java:1014)\n\tat android.app.ActivityThread.handleBindApplication(ActivityThread.java:4765)\n\tat android.app.ActivityThread.access$1700(ActivityThread.java:153)\n\tat android.app.ActivityThread$H.handleMessage(ActivityThread.java:1436)\n\tat android.os.Handler.dispatchMessage(Handler.java:102)\n\tat android.os.Looper.loop(Looper.java:154)\n\tat android.app.ActivityThread.main(ActivityThread.java:5527)\n\tat java.lang.reflect.Method.invoke(Native Method)\n\tat com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739)\n\tat com.android.internal.os.ZygoteInit.main(ZygoteInit.java:629)\n",



java.lang.RuntimeException: Unable to create application cn.sensorsdata.demo.MyApplication: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.toString()' on a null object reference 
at android.app.ActivityThread.handleBindApplication(ActivityThread.java:4768) 
at android.app.ActivityThread.access$1700(ActivityThread.java:153) 
at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1436) 
at android.os.Handler.dispatchMessage(Handler.java:102) 
at android.os.Looper.loop(Looper.java:154) 
at android.app.ActivityThread.main(ActivityThread.java:5527) 
at java.lang.reflect.Method.invoke(Native Method) 
at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:739) 
at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:629) 
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.toString()' on a null object reference 
at cn.sensorsdata.demo.MyApplication.initSensorsDataAPI(My$

