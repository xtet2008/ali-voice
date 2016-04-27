#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import top.api, sys, os, datetime

global g_arg1, g_arg2, g_arg3, g_err
g_arg1, g_arg2, g_arg3, g_err = '', '', '', ''

url = "gw.api.taobao.com"
port = 80
appkey = "23345058"
secret = "049ac60eda7b6965dc75baa5bc71126b"
req = top.api.AlibabaAliqinFcTtsNumSinglecallRequest(url, port)
req.set_app_info(top.appinfo(appkey, secret))
def voice(phoneNo=g_arg1, content=g_arg2, note=g_arg3, err=g_err):
    log_file = '/tmp/text.txt'

    if err:
        strtofile(log_file, now() + ' ' + err, True)
        exit()

    if not phoneNo:
        strtofile(log_file, now() + ' ' + 'unknow mobile phoneNo', True)
        exit()

    if not content:
        strtofile(log_file, now() + ' ' + 'nothing to say', True)
        exit()
    else:
        content = content.replace('.huivo.net', '').replace('huivo.net', '')

    if int(datetime.datetime.now().strftime('%H')) >= 23 and int(datetime.datetime.now().strftime('%H')) <= 7:
        strtofile(log_file, now() + ' ' + 'error found in sleep times', True)
        exit()

    req.extend = "12345"
    req.tts_code = "TTS_7730017"
    req.tts_param = "{\"product\":\"%s\", \"code\":\"本次通知完毕,对您的打扰表示抱歉,祝愉快\"}" % (content)
    str = req.tts_param + "\n\tcontent:" + content
    str += '\n\tdetail:' + note
    req.called_show_num = "4008221620"
    req.called_num= phoneNo
    # req.called_num = '18618458391'
    # req.called_num = '13693567420'
    try:
        resp = req.getResponse()
        str += "\n\tret:%s" % resp
        print(resp)
        pass
    except Exception, e:
        if hasattr(e, 'errmsg'): str += "\n\terr:" + e.message.encode('utf-8')
        if hasattr(e, 'submsg'): str += "\n\tsubmsg:" + e.submsg.encode('utf-8')
        print(e)
    finally:
        strtofile(fname=log_file, content=now() + ' ' + str, append=True)


def file(fname=''):
    ret = False
    if fname:
        import os
        ret = os.path.exists(fname)
    return ret

def filetostr(fname=""):
    if not fname or not os.path.exists(fname): return ""
    with open(fname, "r") as f_handler: return f_handler.readline()

def strtofile(fname="", content="", append=False):
    if not fname: return 0
    if append:
        fexist = file(fname)
        with open(fname, 'a') as f_handler:
            if fexist:
                f_handler.write('\n' + content)
            else:
                f_handler.write(content)
    else:  # overwrite
        with open(fname, 'w') as f_handler:
            f_handler.write(content)


def now(format='%Y-%m-%d %H:%M:%S'):  # yyyy-mm-dd hh:mm:ss
    import datetime
    return datetime.datetime.now().strftime(format)


if __name__ == '__main__':
    try:
        g_arg1, g_arg2, g_arg3 = sys.argv[1], sys.argv[2], sys.argv[3]
    except Exception, e:
        g_err = e.message
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
        if case(1, 3):  # 周一,三
            phone = '13141163261'  # 吴志新
            break
        if case(2, 4):  # 周二,四
            phone = '13439930315'  # 秋林
            break
        if case(5):  # 周五
            phone = '18601907819'  # 宁思平
            break
        if case(6, 7):  # 周六,日
            phone = '18601086705'  # 恩东
            break
        if case():
            print "unknow weekday"
            break

    voice(phoneNo=phone, content=g_arg2, note=g_arg3)  # voice(phoneNo=g_arg1, content=g_arg2, note=g_arg3)
    exit()
