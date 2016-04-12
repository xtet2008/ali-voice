# -*- coding: utf-8 -*-
import top.api

url = "gw.api.taobao.com"
port = 80
appkey = "23343883"
secret = "3b78b41ce9219f79c26cea5f0204f5c9"

req=top.api.AlibabaAliqinFcSmsNumSendRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.extend="18618458391"
req.sms_type="normal"
req.sms_free_sign_name="大鱼测试"
req.sms_param="{\"code\":\"123456\",\"product\":\"验证码短信通知服务\"}"
req.rec_num="18618458391"
req.sms_template_code="SMS_7501215"
try:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)