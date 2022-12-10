import logging
from logging.handlers import TimedRotatingFileHandler
import time

#封装断言方法
def assert_commen(self,response,result,code,msg):
    # 断言响应状态码
    self.assertEqual(200, response.status_code)
    #断言登陆是否成功
    self.assertEqual(result,response.json()['success'])
    #断言返回数据的code
    self.assertEqual(code,response.json()['code'])
    #断言返回数据
    self.assertEqual(msg,response.json()['message'])

#定义获取日志信息方法
def get_log_info():
    #创建日志器
    mylogger = logging.getLogger()
    #创建处理器
    shl = logging.StreamHandler()
    thl = TimedRotatingFileHandler('../log/{}.log'.format(time.strftime('%y%m%d%H%M%S')),
                                   when='h',interval=1,backupCount=0)
    #创建格式化器
    fmt = logging.Formatter()
    #处理器添加格式化器
    shl.setFormatter(fmt)
    thl.setFormatter(fmt)
    #日志器添加处理器
    mylogger.addHandler(shl)
    mylogger.addHandler(thl)
    #日志器设置日志级别
    mylogger.setLevel('DEBUG')