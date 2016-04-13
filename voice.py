# -*- coding: utf-8 -*-
import top.api

url = "gw.api.taobao.com"
#url = "www.baidu.com"
port = 80
appkey = "23345058"
secret = "049ac60eda7b6965dc75baa5bc71126b"

req=top.api.AlibabaAliqinFcTtsNumSinglecallRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

def voice(phoneNo):
    req.extend="12345"
    req.tts_param="{\"product\":\"慧沃服务器故障语音通知\", \"code\":\"慧沃中国abcd-1234，本次通知完毕,对您的打扰表示抱歉,祝愉快\"}"
    req.called_num= phoneNo #"13439930315"
    req.called_show_num="4008221620"
    req.tts_code="TTS_7730017"
    try:
        resp= req.getResponse()
        print(resp)
    except Exception,e:
        print(e)

if __name__=='__main__':
    phoneList = {
                    '13439930315':'秋林',
                    '18618458391':'张胜',
                    '13141163261':'吴志清',
                    '13693567420':'武举光',
                    '18601907819':'宁思平',
                    '18601086705':'王恩东'
                 }
    for phone in phoneList:
        voice(phone)