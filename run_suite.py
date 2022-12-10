import unittest
from HTMLTestReportCN import HTMLTestRunner

from script.test02_employee import TestEmployee
from script.test01_login import TestLogin
from tools.config import BASE_PATH

#创建套件
suite = unittest.defaultTestLoader.discover('script/')
# suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestEmployee))
#创建运行器并创建测试报告
with open(BASE_PATH+'/report/report.html', 'wb') as f:
    runner = HTMLTestRunner(stream=f,title='iHRM人力资源管理系统测试报告')
    runner.run(suite)