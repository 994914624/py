#!/usr/bin/env python
# -*- coding: utf-8 -*-

'  DEBUG_AND_TRACK模式下 过滤log '
__author__ = 'yang'

try:
    #写处理后的日志到另一个文件
    write_file=open('/Users/yang/Desktop/logFilter.txt', 'w')
    write_file.write('过滤后的日志\n')
    # 处理日志
    file=open("/Users/yang/Desktop/log2.txt",'r')

    flush_tag=False
    error_tag=False
    track_num=0
    flush_num=0
    error_num=0

    events='"event":'
    track_key='SA.SensorsDataAPI'
    flush_key='SA.AnalyticsMessages'
    valid_key_begain='valid message'
    valid_key_end='Events flushed'
    invalid_key='invalid message'
    invalid_content='ret_content:'
    while True:
        line = file.readline()
        if len(line) == 0:
            break;
       # 前提条件
        if(line.__contains__(track_key)|line.__contains__(flush_key)):
            # 表明是 track 事件
            if(line.__contains__(events)&line.__contains__(track_key)):
                track_num=track_num+1
                print ('触发的事件%d：%s'%(track_num,line[line.find(events)+8:]))
                write_file.write('触发的事件%d：%s'%(track_num,line[line.find(events)+8:]))
                continue


            # 表明是 flush 事件 日志的开始
            if(line.__contains__(valid_key_begain)&line.__contains__(flush_key)&(line.__contains__(invalid_key)==False)):
                flush_tag=True
                continue
            if(flush_tag&line.__contains__(events)&line.__contains__(flush_key)):
                flush_num=flush_num+1
                print ('-----------------------------发送成功的事件%d：%s'%(flush_num,line[line.find(events)+8:]))
                write_file.write('-----------------------------发送成功的事件%d：%s'%(flush_num,line[line.find(events)+8:]))
                continue
            # 表明是 flush 事件 日志的结束
            if(line.__contains__(valid_key_end)&line.__contains__(flush_key)):
                flush_tag=False
                continue

            # invalid 无效事件
            if(line.__contains__(invalid_key)&line.__contains__(flush_key)):
                error_tag=True
                continue
            if(error_tag&line.__contains__(events)&line.__contains__(flush_key)):
                error_num=error_num+1
                print ('***************************************无效事件%d：%s'%(error_num,line[line.find(events)+8:]))
                write_file.write('***************************************无效事件%d：%s'%(error_num,line[line.find(events)+8:]))
                continue
            if(error_tag&line.__contains__(invalid_content)&line.__contains__(flush_key)):
                print('***************************************错误原因%s'%(line[line.find(invalid_content)+11:]))
                write_file.write('***************************************错误原因%s'%(line[line.find(invalid_content)+11:]))
                continue
            # 表明是 flush 事件 日志的结束
            if(line.__contains__(valid_key_end)&line.__contains__(flush_key)):
                error_tag=False
                continue


finally:
    if file:
        file.close()
    if write_file:
        write_file.close()





# # 读取日志文件(小文件)
# with open('/Users/yang/Desktop/log2.txt','r') as f:

#     flush_tag=False
#     error_tag=False
#     track_num=0
#     flush_num=0
#     error_num=0

#     events='"event":'
#     track_key='SA.SensorsDataAPI'
#     flush_key='SA.AnalyticsMessages'
#     valid_key_begain='valid message'
#     valid_key_end='Events flushed'
#     invalid_key='invalid message'
#     invalid_content='ret_content'
#     for line in f.readlines():
        

#         # 前提条件
#         if(line.__contains__(track_key)|line.__contains__(flush_key)):
#             # 表明是 track 事件 
#             if(line.__contains__(events)&line.__contains__(track_key)):
#                 track_num=track_num+1
#                 print ('触发的事件%d：%s'%(track_num,line[line.find(events)+8:]))
                
        
#             # 表明是 flush 事件 日志的开始 
#             if(line.__contains__(valid_key_begain)&line.__contains__(flush_key)&(line.__contains__(invalid_key)==False)):
#                 flush_tag=True
#             if(flush_tag&line.__contains__(events)&line.__contains__(flush_key)):
#                 flush_num=flush_num+1
#                 print ('-----------------------------发送成功的事件%d：%s'%(flush_num,line[line.find(events)+8:]))
#             # 表明是 flush 事件 日志的结束 
#             if(line.__contains__(valid_key_end)&line.__contains__(flush_key)):
#                 flush_tag=False

#             # invalid 无效事件
#             if(line.__contains__(invalid_key)&line.__contains__(flush_key)):
#                 error_tag=True
#             if(error_tag&line.__contains__(events)&line.__contains__(flush_key)):
#                 error_num=error_num+1
#                 print ('***************************************无效事件%d：%s'%(error_num,line[line.find(events)+8:]))
#             if(error_tag&line.__contains__(invalid_content)&line.__contains__(flush_key)):
#                 print('***************************************错误原因%s：'%(line[line.find(invalid_content)+11:]))
#             # 表明是 flush 事件 日志的结束 
#             if(line.__contains__(valid_key_end)&line.__contains__(flush_key)):
#                 error_tag=False
