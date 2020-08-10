import unittest
import jsonpath

from ddt import ddt, data, unpack

from ddtdemo01.exceloperator import excelData
from ddtdemo01.operator_Common import operator_Common
from ddtdemo01.convertoperator import convertConvert,depend
@ddt
class MyTestCase(unittest.TestCase):

    @data(*excelData().getExcel())
    @unpack
    def test_get_commonapi(self, url, body, header, method, method_type, expect, resjsonpath,dependency):
        comon=operator_Common()
        body = "" if body is None else body
        header = "" if header is None else header
        #如果传入的body包含$字符，调用convertConvert类方法进行替换
        body = convertConvert().convertop(body) if body.find("$") >= 0 else body
        # 如果传入的header包含$字符，调用convertConvert类方法进行替换
        header = convertConvert().convertop(header) if header.find("$") >= 0 else header
        res=comon.request(method,url,method_type,body,header)

        #得到的json值存放到convertConvert类里的depend字典
        if len(dependency)>0 and dependency.find("/")<0:
            depend[dependency] = res.content
        #print(depend)
        resjson = res.json()
        #解析实际值
        actual = jsonpath.jsonpath(resjson, resjsonpath)
        #断言
        self.assertEqual(expect, actual[0])

