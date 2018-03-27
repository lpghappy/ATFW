
# import testsuites
# from testsuites.test_baidu_search import BaiduSearch
# from testsuites.test_get_page_title import GetPageTitle

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time

# # #用addTest()方法来加载我们测试用例到suite中
# suite = unittest.TestSuite()
# # suite.addTest(BaiduSearch('test_baidu_search1'))
# # suite.addTest(BaiduSearch('test_baidu_search2'))
# suite.addTest(GetPageTitle('test_get_title'))

# 利用makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))

# 利用discover（）方法去加载一个路径下所有的测试用例
suite = unittest.TestLoader().discover("testsuites")

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
#获取系统当前时间
now = time.strftime("%Y%m%d %H-%M-%S",time.localtime(time.time()))
#设置报告名称格式"测试报告"
HtmlFile = report_path + "【测试报告】" + now + ".html"
fp = open(HtmlFile, 'wb')

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"XXX项目测试报告", description=u"测试用例执行情况")
    # 执行用例
    runner.run(suite)
