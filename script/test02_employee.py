import unittest
import logging
import requests
from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.config import assert_commen, get_data


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_employee = ApiEmployee()
        #访问登陆接口，并返回token
        data = {"mobile":"13800000002","password":"123456"}
        r_login = requests.post(url=api.BASE_URL+'/api/sys/login',json=data,headers=api.headers)
        #返回token
        token = r_login.json()['data']
        #给api.headers重新赋值
        api.headers["Authorization"] = 'Bearer '+token

    @parameterized.expand(get_data('add_data.txt'))
    def test01_post(self,username,mobile,workNumber):
        #业务对象调用访问添加员工接口，并接收
        r_post = self.api_employee.post_employee(username=username,mobile=mobile,workNumber=workNumber)
        api.user_id = r_post.json()['data']['id']
        # logging.debug(r_post.json())
        print('测试数据为：',username,mobile,workNumber)
        print(r_post.json())
        #断言
        try:
            assert_commen(self,r_post)
        except Exception as e:
            raise e

    #创建查询接口的测试用例
    def test02_get(self):
        #业务对象调用访问查询接口
        r_get = self.api_employee.get_employee(api.user_id)
        # logging.debug(r_get.json())
        print(r_get.json())
        #断言
        try:
            assert_commen(self,r_get)
        except Exception as e:
            raise e

    #创建更新员工接口的测试用例
    def test03_put(self):
        #业务对象调用访问更新接口
        r_put = self.api_employee.put_employee(new_name='这是新名字',user_id=api.user_id)
        # logging.debug(r_put.json())
        print(r_put.json())
        #断言
        try:
            assert_commen(self,r_put)
        except Exception as e:
            raise e

    #创建删除员工接口的测试用例
    def test04_delete(self):
        #业务对象访问删除员工接口
        r_delete = self.api_employee.delete_employee(api.user_id)
        #删除后，再查看该员工
        r = self.api_employee.get_employee(api.user_id)
        # logging.debug(r.json())
        print(r.json())
        #断言
        try:
            assert_commen(self,r_delete)
        except Exception as e:
            raise e