# -*- coding: utf-8 -*-
'''
@File  : demo.py
@Date  : 2019/1/15/015 16:18
'''
from configparser import ConfigParser
import os
import json
import pytest_html


import requests
headers={"cookie":"_umdata=G1D9DFFBA554E65A731DFE539C75C23F93ACB10; Hm_lpvt_484788504bd0bc163a54b110d0dc003c=1547633889; Hm_lvt_484788504bd0bc163a54b110d0dc003c=1547632717,1547633889; DIS4=47cbc635e8c6402aa899522deb710a0f; lite_token=fe591551c125ba768d11c343a770baed; _uab_collina=154763271682458273515994; ln=1; lu=61984850; user_redirct_subtask_list=1",
         "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 version=2.0.2018101201 bid=com.he.ar",
         "Accept":"application/json"}
url="http://fp01.ops.gaoshou.me/s5/login.mobile"
url1="http://fp01.ops.gaoshou.me/s4/dashboard"
data={"phone":"17711794059"}
s=requests.get(url1,data="")
print(s.json())
# s=[{'id': 1, 'name': '测试', 'host': '/s5/login.mobile', 'except': {'data': 'd', 'code': '200'}, 'fact': '用例请求方法错误', 'ispass': 'fail', 'time': '2019/01/17 14:10:09', 'reason': '用例错误，无法执行，没有put请求方法'}, {'id': 2, 'name': '测试', 'host': '/s5/login.mobile', 'except': {'data': 'd', 'code': '200'}, 'fact':'<Response [400]' , 'ispass': 'fail', 'time': '2019/01/17 14:10:09', 'reason': '网络连接错误或其他错误，接口返回400'}, {'id': 3, 'name': '测试', 'host': '/s5/login.mobile', 'except': {'data': 'd', 'code': '200'}, 'fact': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n', 'ispass': 'pass', 'time': '2019/01/17 14:10:09'}, {'id': 4, 'name': '测试', 'host': '/s5/login.mobile', 'except': {'data': 'd', 'code': '200', 'payload': {'coin': '100'}}, 'fact': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n', 'ispass': 'pass', 'time': '2019/01/17 14:10:10'}]
# for i in s:
#     print(i)
from common.log import Log
class A(object):
    def __init__(self):
        self.log=Log()
        self.log.info("初始化成功")
a=A()

