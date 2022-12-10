import requests

from api import BASE_URL, headers


#创建登陆接口类
class ApiLogin:
    #初始化登陆接口
    def __init__(self):
        self.url_login = BASE_URL+'/api/sys/login'

    #定义访问登录接口的方法
    def login(self,mobile,password):
        #准备登陆接口入参
        data = {"mobile":mobile,"password":password}
        return requests.post(url=self.url_login,json=data,headers=headers)