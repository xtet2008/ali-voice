#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import top.api,sys,os,datetime

global g_arg1,g_arg2,g_arg3,g_err
g_arg1,g_arg2,g_arg3,g_err = '','','',''

url = "gw.api.taobao.com"
port = 80
appkey = "23345058"
secret = "049ac60eda7b6965dc75baa5bc71126b"
req=top.api.AlibabaAliqinFcTtsNumSinglecallRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))
def voice(phoneNo=g_arg1, content=g_arg2, note=g_arg3,err=g_err):
    log_file = '/tmp/text.txt'

    if err:
        strtofile(log_file,err)
        exit()

    if not phoneNo:
        strtofile(log_file,'unknow mobile phoneNo')
        exit()

    if not content:
        strtofile(log_file,'nothing to say')
        exit()

    req.extend="12345"
    req.tts_code = "TTS_7730017"
    req.tts_param="{\"product\":\"%s\", \"code\":\"本次通知完毕,对您的打扰表示抱歉,祝愉快\"}" % (g_arg2.replace('.huivo.net','').replace('huivo.net',''))
    str = req.tts_param + "\n\ndetail info:" + content
    req.called_show_num = "4008221620"
    req.called_num= phoneNo
    try:
        resp= req.getResponse()
        str += "\n\nret:%s" % resp
        print(resp)
    except Exception,e:
        str += "\n\nerr:"+e.message
        print(e)
    finally:
        strtofile(fname=log_file,content=str)


def filetostr(fname=""):
    if not fname or not os.path.exists(fname) : return ""
    with open(fname,"r") as f_handler:return f_handler.readline()


def strtofile(fname="", content=""):
    if not fname :return 0
    if not os.path.exists(fname):
        with open(fname,'w') as f_handler:
            f_handler.write(content)
    else:
        with open(fname,'w') as f_handler:
            #f_handler.truncate()
            f_handler.write(content)

if __name__=='__main__':
    try:
        g_arg1, g_arg2, g_arg3 = sys.argv[1],sys.argv[2],sys.argv[3]
    except Exception,e:
        g_err= e.message
    finally:
        pass


    class switch(object):
        def __init__(self, value):
            self.value = value
            self.fall = False

        def __iter__(self):
            yield self.match
            raise StopIteration

        def match(self, *args):
            if self.fall or not args:
                return True
            elif self.value in args:
                self.fall = True
                return True
            else:
                return False

    phone = ''
    for case in switch((datetime.datetime.now().weekday()) + 1):
        if case(1,3): # 周一,三
            phone = '13141163261' # 吴志新
            break
        if case(2,4): # 周二,四
            phone = '13439930315'  # 秋林
            break
        if case(5): # 周五
            phone = '18601907819'  # 宁思平
            break
        if case(6,7): # 周六,日
            phone = '18601086705'  # 恩东
            break
        if case():
            print "unknow weekday"
            break
    # voice(phoneNo=g_arg1, content=g_arg2, note=g_arg3)
    voice(phoneNo=phone, content=g_arg2, note=g_arg3)
    exit()

    '''
    phoneList = {
                    '13439930315':'秋林',
                    '18618458391':'张胜',
                    '13141163261':'吴志新',
                    '13693567420':'武举光',
                    '18601907819':'宁思平',
                    '18601086705':'王恩东'
                 }
    for phone in phoneList:
        voice(phone)
    '''