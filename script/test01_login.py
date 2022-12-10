import unittest
import json
from parameterized import parameterized
import logging

from api import headers
from api.api_login import ApiLogin
from tools.config02 import assert_commen

def get_data():
    result = []
    with open('../data/login_data.json',encoding='utf8') as f:
        data = json.load(f)
        for value in data.values():
            result.append((value.values()))
        return result


#创建测试类
class TestLogin(unittest.TestCase):
    #类方法创建业务对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_login = ApiLogin()

    #创建测试用例
    @parameterized.expand(get_data())
    def test01_login(self,mobile,password,result,code,msg):
        #业务对象调用访问登陆接口的方法，并接收，以便后续使用
        r_login = self.api_login.login(mobile=mobile,password=password)
        # logging.info('测试数据为：',mobile,password,result,code,msg)
        print('测试数据为：',mobile,password,result,code,msg)
        #断言--调用公共方法断言
        try:
            assert_commen(self,response=r_login,code=code,result=result,msg=msg)
        except Exception as e:
            raise e