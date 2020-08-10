# -*- coding: utf-8 -*-
# 日期： 2020/8/7
# @Author: 梓梦扬
import json
import jsonpath

#定义一个字典，存放接口返回的json
depend = {}
class convertConvert():
    #此方法用于将测试用例里两个$$中的内容替换成真实的值，并返回
    def convertop(self, body):
        #以$符号对传入内容dict切片
        listvar = body.split("$")
        # print(listvar)
        #循环取值
        num = 0
        for strchuck in listvar:
            if num % 2 == 1:
                #以.切割
                envar = strchuck[0:strchuck.find('.')]
                #取出环境变量值
                varvalue = depend[envar]
                # 取出jsonpath值
                varjsonpath = strchuck[strchuck.find('.')+1:]
                # 将json格式数据转换为字典
                varjsonresult = json.loads(varvalue)
                #jsonpath方式取出内容，并进行替换
                varchuck = jsonpath.jsonpath(varjsonresult, expr="$."+varjsonpath)
                listvar[num] = str(varchuck[0])
            num = num+1
        #将替换的内容，用空格链接起来，并返回
        listvar = "".join(listvar)
        return listvar

# if __name__ == '__main__':
#     convertConvert().convertop(body)


