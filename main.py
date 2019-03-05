#coding=utf8
import requests
import itchat
from alien_translator import AlienTranslator
import threading
threads=[]

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]


@itchat.msg_register(itchat.content.TEXT)
def mes_reply(): #定义回复函数，回复是，先输入想要回复的人，然后输入一个#，再输入回复消息即可回复。
    while(1):
        try:
            mes = input()
            s = mes.split("#")
            # print(s)
            #define the key
            translator = AlienTranslator("as k")
            #encrypt
            ans = translator.encrypt_to_code(s[1])
            # print(ans)
            #send message
            itchat.send(ans, mes_list[s[0]])
        except:
            print("error")
#
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    if len(get_key(mes_list,msg['FromUserName'])) > 0:
        translator1 = AlienTranslator("as k")
        # print(msg['User']['PYQuanPin'])
        data = msg[msg['Type']].strip("\n")
        # print(data)
        ans = translator1.decrypt_to_msg(data)
        if ans:
            print(get_key(mes_list,msg['FromUserName']),ans)
        else:
            print(get_key(mes_list,msg['FromUserName']),data)
    else:
        print(get_key(mes_list, msg['FromUserName']), msg[msg['Type']])


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
    mes_list[f["RemarkName"]] = f["UserName"]
code = friends[0]["PYQuanPin"]
print(code)
print(mes_list)
t = threading.Thread(target=mes_reply) #开启并行线程
t.setDaemon(True)
t.start()

itchat.run()