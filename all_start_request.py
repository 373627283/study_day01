# -*- coding: utf-8 -*-
# 日期：2020/7/29
# @Author   :梓梦扬

import hashlib
import time
import requests
import json
from pip._vendor.pyparsing import unicode

def get_sign(params):
    str_parm = ""
    for p in sorted(params):
        if p == "showapi_sign":
            continue
        else:
            # 每次排完序的加到串中
            str_parm = str_parm + p + params[p]
    str_parm = str_parm + "e3d0428dd0b1459495012aff834746ed"
    #print(str_parm)
    if isinstance(str_parm, str):
        # 如果是unicode先转utf-8
        parmStr = str_parm.encode("utf-8")
        m = hashlib.md5()
        m.update(parmStr)
        return m.hexdigest()


class requesClass():
    #圆通快递鉴权接口
    def yuantongtest(self):
        data = {"com": "yuantong",
                "nu": "YT4620020577123",
                "phone": "13566661111",
                "showapi_appid": "298130",
                "showapi_timestamp": str(time.strftime("%Y%m%d%H%M%S")),
                "showapi_sign": "85457a48434616f9d13ec224630b6730"}#随便填一个 后面算出sign替换
        sign = get_sign(data)
        data["showapi_sign"] = sign #将算好"showapi_sign"和值加到data里
        #data = json.dumps(data)
        #header = {"content-type":"application/json"}
        url = "https://route.showapi.com/64-19"
        #res = requests.post(url,headers=header,params=data)
        res = requests.get(url, params=data)
        print(res.json())
        print(unicode(res.content, 'unicode_escape'))
        print(res.url)
    def yuantongtest1(self):
        data = {"com": "yuantong",
                "nu": "YT4620020577123",
                "phone": "13566661111",
                "showapi_appid": "298130",
                "showapi_timestamp": str(time.strftime("%Y%m%d%H%M%S")),
                "showapi_sign": "85457a48434616f9d13ec224630b6730"}#随便填一个 后面算出sign替换
        sign = get_sign(data)
        data["showapi_sign"] = sign #将算好"showapi_sign"和值加到data里
        #data = json.dumps(data)
        header = {"Content-Type": "application/x-www-form-urlencoded"}

        url = "https://route.showapi.com/64-19"
        res = requests.post(url, headers=header, data=data)
        #res = requests.get(url, params=data)
        print(res.content.decode('UTF-8'))




    #获取商品信息get请求
    def getProductInfo(self):
        params = {"productid": 2222}
        url = "http://39.98.138.157:5000/api/getproductinfo"
        res = requests.get(url, params=params)
        print(res.json())
        print(unicode(res.content, 'unicode_escape'))
        print(res.url)


    #创建订单post请求
    def createOrder(self):
        data = {"cartid": 45233, "openid": "UEHUXUXU78272SDSassDD", "productid": 2222, "userid": 17890}
        data = json.dumps(data)
        header = {"token":"23657DGYUSGD126731638712GE18271H", "content-type":"application/json"}
        url = "http://39.98.138.157:5000/api/createorder"
        res = requests.post(url, headers=header, data=data)
        print(res.json())
        print(unicode(res.content, 'unicode_escape'))
        print(res.url)

if __name__ == "__main__":
    requesClass().yuantongtest1()
    # requesClass().createOrder()
    # requesClass().getProductInfo()