#coding=utf8
import requests
import itchat
from alien_translator import AlienTranslator
import time
import csv
import datetime
# import pandas as pd
# import numpy as np
import threading
KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
threads=[]

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]

def get_response(msg): #通过改下面的代码，也可以自动回复
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def mes_reply(): #定义回复函数，回复是，先输入想要回复的人或群的前面的标识数字，然后输入一个空格，再输入回复消息即可回复。
    while(1):
        try:
            mes = []
            mes = input()
            # i = int(mes[0])  # 获取标识
            s = mes.split("#")
            print(s)
            translator = AlienTranslator(code)
            ans = translator.encrypt_to_code(s[1])
            itchat.send(ans, mes_list[s[0]])
        except:
            print("error")
#
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # print(msg)
    # if len(get_key(mes_list,msg['FromUserName'])) > 0 and msg['Type'] == 'Text':
    #     translator1 = AlienTranslator(msg['FromUserName'])
    #     ans = translator1.decrypt_to_msg(msg[msg['Type']])
    #     print(get_key(mes_list,msg['FromUserName']),ans)
    # else:
    #     print(get_key(mes_list, msg['FromUserName']), msg[msg['Type']])
    print(get_key(mes_list, msg['FromUserName']), msg[msg['Type']])
    # print(mes_list.index(msg['FromUserName']),msg['User']['NickName'].encode('utf-8'),msg['User']['RemarkName'].encode('utf-8'),msg['Content'].encode('utf-8'))


#
# @itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
# def text_reply(msg):
#     if (msg['User']['UserName'] not in mes_list) :
#         mes_list.append(msg['User']['UserName'])
#     # csv_writer.writerow(row)
#     print(mes_list.index(msg['User']['UserName']),msg['User']['NickName'].encode('utf-8'),msg['ActualNickName'].encode('utf-8'),msg['User']['RemarkName'].encode('utf-8'),msg['Content'].encode('utf-8'))

itchat.auto_login(hotReload=True)
mes_list={}
friends = itchat.get_friends(update=True)[0:]
for f in friends[1:]:
    print(f["NickName"])
    mes_list[f["RemarkName"]] = f["UserName"]
code = friends[0]["UserName"]
print(mes_list)
t = threading.Thread(target=mes_reply) #开启并行线程
t.setDaemon(True)
t.start()

itchat.run()