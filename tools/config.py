#封装断言方法
import os


def assert_commen(self,response):
    # 断言响应状态码
    self.assertEqual(200, response.status_code)
    #断言登陆是否成功
    self.assertEqual(True,response.json()['success'])
    #断言返回数据的code
    self.assertEqual(10000,response.json()['code'])
    #断言返回数据
    self.assertEqual('操作成功！',response.json()['message'])

#封装读取文件的方法
def get_data(filename):
    result = []
    with open(BASE_PATH+'/data/'+filename,encoding='utf8') as f:
        #所有行读取文件
        data = f.readlines()
        #遍历data数据
        for info in data:
            x = info.strip().split(',')
            result.append(x)
        return result[1::]


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


