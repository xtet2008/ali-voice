# -*- coding: utf-8 -*-
import top.api

url = "gw.api.taobao.com"
#url = "www.baidu.com"
port = 80
appkey = "23343883"
secret = "3b78b41ce9219f79c26cea5f0204f5c9"

req=top.api.AlibabaAliqinFcTtsNumSinglecallRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.extend="12345"
req.tts_param="{\"product\":\"慧沃\", \"code\":\"8888168\"}"
req.called_num="18618458391"
req.called_show_num="4000"
req.tts_code="TTS_7501222"
try:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)