import requests

from api import BASE_URL, headers


class ApiEmployee:
    #初始化员工接口
    def __init__(self):
        self.url_add_employee = BASE_URL+'/api/sys/user'
        self.url_employee = BASE_URL+'/api/sys/user/{}'

    #定义访问添加员工接口的方法
    def post_employee(self,username,mobile,workNumber):
        #准备添加员工接口的入参
        data ={"username":username,
              "mobile":mobile,
              "workNumber":workNumber}
        return requests.post(url=self.url_add_employee,json=data,headers=headers)

    #定义访问查询员工接口的方法
    def get_employee(self,user_id):
        return requests.get(url=self.url_employee.format(user_id),headers=headers)

    #定义访问更新员工接口的方法
    def put_employee(self,new_name,user_id):
        #准备更改员工信息的数据
        data = {"username":new_name}
        return requests.put(url=self.url_employee.format(user_id),json=data,headers=headers)

    #定义访问删除员工接口的方法
    def delete_employee(self,user_id):
        return requests.delete(url=self.url_employee.format(user_id),headers=headers)