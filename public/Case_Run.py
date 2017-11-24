# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 11:45
# @Author  : Leo_Peng
# @File    : Case_Run.py
# @Software: PyCharm
import unittest
from public.suite import Suite
from public import HTMLTestRunner
import os,time
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(path)
case_path =path+'/TestCase'
result =path+'/Result/'
def Creatsuite():
    #定义单元测试容器
    testunit = Suite()

    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print (testunit)
    return testunit

test_case = Creatsuite()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title=u'Appium测试报告', description=u'用例详情：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    os.mkdir(tdresult)
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title=u'Appium测试报告', description=u'用例详情：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
