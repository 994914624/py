#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
from urllib import request, parse


req = request.Request('http://test2-zouyuhan.cloud.sensorsdata.cn:8006/sa?project=yangzhankun&token=386e4bed00b5701e')
#req = request.Request('http://analysis.aoyou.com:8106/sa?project=default')

raw_data='{"distinct_id": "test123456", "type": "track", "event": "$AppStart", "properties": {"product": "null", "product_price": 14}}'
raw_data2='{"type":"track","distinct_id":"308597799c71b44b95d1f6845","event": "AppClick","lib":{"lib":"Android","lib_version": "0.0.4-SNAPSHOT","app_version": "1.0"},"properties": {"element_type": "android.support.v7.widget.AppCompatTextView","screen_name_class": "主Activity","parent": "","parent_class": "","os": "Android","imeicode": "359906070806943","network_type": "WIFI","wifi": true,"screen_height": 1440,"referrer": "com.foolchen.lib.tracker.demo.MainActivity","device_id": "c71b44b95d1f6845","referrer_alias": "主Activity","element_content": "ButterKnife点击事件测试","carrier": "中国联通","os_version": "8.0.0","parent_alias": "","model": "Pixel XL","screen_width": 2560,"app_version": "1.0","lib": "Android","title": "主Activity","lib_version": "0.0.4-SNAPSHOT","screen_name": "主Activity","manufacturer": "google","channel": "baidu","project": "xcar"}}'

base64_data=base64.b64encode(str.encode(raw_data2))
data = parse.urlencode([('data',base64_data)])



with request.urlopen(req, data.encode('utf-8')) as f:
    print(data.encode('utf-8'))
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))



# curl -v \
#      --data 'data=eyJkaXN0aW5jdF9pZCI6IjE1ZmIzMmU2YzUwNWZiLTBjYzgxZWZiMDU1YjNhLTMxNjA3YzAwLTEwMjQwMDAtMTVmYjMyZTZjNTEyNTUiLCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS44LjE0In0sInByb3BlcnRpZXMiOnsiJHNjcmVlbl9oZWlnaHQiOjU2NywiJHNjcmVlbl93aWR0aCI6NDIzLCIkbGliIjoianMiLCIkbGliX3ZlcnNpb24iOiIxLjguMTQiLCJhIjoxLCJiIjoiWFhYIiwiJGxhdGVzdF9yZWZlcnJlciI6IuWPluWAvOW8guW4uCIsIiRsYXRlc3RfcmVmZXJyZXJfaG9zdCI6IuWPluWAvOW8guW4uCIsIiRsYXRlc3Rfc2VhcmNoX2tleXdvcmQiOiLlj5blgLzlvILluLgiLCIkbGF0ZXN0X3RyYWZmaWNfc291cmNlX3R5cGUiOiLlj5blgLzlvILluLgiLCIkaXNfZmlyc3RfZGF5IjpmYWxzZX0sInR5cGUiOiJ0cmFjayIsImV2ZW50IjoiVGVzdEFQSSIsIl9ub2NhY2hlIjoiMDY5MzI2OTc3NDEyODUyIn0%3D' \
#      http://test2-zouyuhan.cloud.sensorsdata.cn:8006/sa\?project\=yangzhankun\&token\=386e4bed00b5701e


# curl -v \
#      --data 'data_list=W3sidHlwZSI6InRyYWNrIiwiZGlzdGluY3RfaWQiOiIzMDg1OTc3OTljNzFiNDRiOTVkMWY2ODQ1IiwiZXZlbnQiOiAiQXBwQ2xpY2siLCJsaWIiOnsibGliIjoiQW5kcm9pZCIsImxpYl92ZXJzaW9uIjogIjAuMC40LVNOQVBTSE9UIiwiYXBwX3ZlcnNpb24iOiAiMS4wIn0sInByb3BlcnRpZXMiOiB7ImVsZW1lbnRfdHlwZSI6ICJhbmRyb2lkLnN1cHBvcnQudjcud2lkZ2V0LkFwcENvbXBhdFRleHRWaWV3Iiwic2NyZWVuX25hbWVfY2xhc3MiOiAi5Li7QWN0aXZpdHkiLCJwYXJlbnQiOiAiIiwicGFyZW50X2NsYXNzIjogIiIsIm9zIjogIkFuZHJvaWQiLCJpbWVpY29kZSI6ICIzNTk5MDYwNzA4MDY5NDMiLCJuZXR3b3JrX3R5cGUiOiAiV0lGSSIsIndpZmkiOiB0cnVlLCJzY3JlZW5faGVpZ2h0IjogMTQ0MCwicmVmZXJyZXIiOiAiY29tLmZvb2xjaGVuLmxpYi50cmFja2VyLmRlbW8uTWFpbkFjdGl2aXR5IiwiZGV2aWNlX2lkIjogImM3MWI0NGI5NWQxZjY4NDUiLCJyZWZlcnJlcl9hbGlhcyI6ICLkuLtBY3Rpdml0eSIsImVsZW1lbnRfY29udGVudCI6ICJCdXR0ZXJLbmlmZeeCueWHu%2BS6i%2BS7tua1i%2BivlSIsImNhcnJpZXIiOiAi5Lit5Zu96IGU6YCaIiwib3NfdmVyc2lvbiI6ICI4LjAuMCIsInBhcmVudF9hbGlhcyI6ICIiLCJtb2RlbCI6ICJQaXhlbCBYTCIsInNjcmVlbl93aWR0aCI6IDI1NjAsImFwcF92ZXJzaW9uIjogIjEuMCIsImxpYiI6ICJBbmRyb2lkIiwidGl0bGUiOiAi5Li7QWN0aXZpdHkiLCJsaWJfdmVyc2lvbiI6ICIwLjAuNC1TTkFQU0hPVCIsInNjcmVlbl9uYW1lIjogIuS4u0FjdGl2aXR5IiwibWFudWZhY3R1cmVyIjogImdvb2dsZSIsImNoYW5uZWwiOiAiYmFpZHUiLCJwcm9qZWN0IjogInhjYXIifX1d' \
#      http://test2-zouyuhan.cloud.sensorsdata.cn:8006/sa\?project\=yangzhankun\&token\=386e4bed00b5701e
