# -*- coding: utf-8 -*-
# 日期：2020/8/1
# @Author   :梓梦扬
import json
import requests
import unittest
import json
import jsonpath


class MallShopping(unittest.TestCase):
    # 定义全局变量
    vardict = {}

    # 登录
    def test_1login(self):
        url = "http://39.98.138.157:5000/api/login"
        data = {"username": "admin", "password": "123456"}
        header = {"content-type": "application/json"}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        MallShopping.vardict["login"] = resjson
        httpstatus = jsonpath.jsonpath(MallShopping.vardict['login'], "$.httpstatus")[0]
        self.assertEqual(httpstatus, 200)
        # print(resjson)

    # 获取商品信息get请求
    def test_2getProductInfo(self):
        url = "http://39.98.138.157:5000/api/getproductinfo"
        data = {"productid": 2222}
        res = requests.get(url, params=data)
        resjson = res.json()
        MallShopping.vardict["ProductInfo"] = resjson
        # print(resjson)
        httpstatus = jsonpath.jsonpath(MallShopping.vardict['ProductInfo'], "$.httpstatus")[0]
        productname = jsonpath.jsonpath(MallShopping.vardict['ProductInfo'], "$.data[0].productname")[0]
        self.assertEqual(httpstatus, 200)
        self.assertEqual(productname, '海南小青芒2斤装')

    # 获取个人信息
    def test_3getuserinfo(self):
        url = "http://39.98.138.157:5000/api/getuserinfo"
        token = jsonpath.jsonpath(MallShopping.vardict['login'], "$.token")[0]
        header = {"token": token}
        res = requests.get(url, headers=header)
        resjson = res.json()
        MallShopping.vardict["userinfo"] = resjson
        # print(resjson)
        httpstatus = jsonpath.jsonpath(MallShopping.vardict['userinfo'], "$.httpstatus")[0]
        nikename = jsonpath.jsonpath(MallShopping.vardict['userinfo'], "$.data[0].nikename")[0]
        self.assertEqual(httpstatus, 200)
        self.assertEqual(nikename, '风清扬')

    # 加入购物车
    def test_4addcart(self):
        url = "http://39.98.138.157:5000/api/addcart"
        userid = jsonpath.jsonpath(MallShopping.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MallShopping.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MallShopping.vardict["ProductInfo"], "$.data[0].productid")[0]
        token = jsonpath.jsonpath(MallShopping.vardict['login'], "$.token")[0]
        data = {"userid": userid, "openid": openid, "productid": productid}
        header = {"token": token, "content-type": "application/json"}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        MallShopping.vardict["addcart"] = resjson
        # print(resjson)
        httpstatus = jsonpath.jsonpath(MallShopping.vardict['addcart'], "$.httpstatus")[0]
        openid = jsonpath.jsonpath(MallShopping.vardict["addcart"], "$.data[0].openid")[0]
        self.assertEqual(httpstatus, 200)
        self.assertEqual(openid, 'UEHUXUXU78272SDSassDD')

    # 创建订单post请求
    def test_5createOrder(self):
        url = "http://39.98.138.157:5000/api/createorder"
        cartid = jsonpath.jsonpath(MallShopping.vardict["addcart"], "$.data[0].cartid")[0]
        userid = jsonpath.jsonpath(MallShopping.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MallShopping.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MallShopping.vardict["ProductInfo"], "$.data[0].productid")[0]
        token = jsonpath.jsonpath(MallShopping.vardict['login'], "$.token")[0]
        data = {"cartid": cartid, "openid": openid, "productid": productid, "userid": userid}
        header = {"token": token, "content-type": "application/json"}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        print(type(res.content))
        print(type(res.json()))
        MallShopping.vardict["createOrder"] = resjson
        # print(res.json())
        httpstatus = jsonpath.jsonpath(MallShopping.vardict['createOrder'], "$.httpstatus")[0]
        self.assertEqual(httpstatus, 200)
        print(type(MallShopping.vardict))

if __name__ == '__main__':
    unittest.main()
