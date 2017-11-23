# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:50
# @Author  : Leo_Peng
# @File    : BasePage.py
# @Software: PyCharm


import unittest
import yaml
from PO import WpsLoginPage
from public.CommonDriver import *
import os
from logger import logger
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Login(unittest.TestCase):

    def setUp(self):
        title=u'登录测试'
        self.log=logger.Logger(title)
        self.driver=CommonDriver()
        self.wps = WpsLoginPage.Wps(self.driver)
        self.faile=open(path + '/Data/LoginData.ymal','r',encoding='utf-8')
        self.data = yaml.load(self.faile)
        self.faile.close()

    def test_QQLogin(self):
        u'''使用QQ账号登录'''

        try:
            self.wps.makeprotocol(status=True)
            try:
                self.wps.Avatar()
            except:
                self.wps.Table_my()
            self.wps.qqlogin('321321', '176')

        except:
            self.driver.launch_app()


    def test_ipLogin(self):
            u'''使用phone账号登录'''
            try:
                user = self.data['login_01']['user']
                psw = self.data['login_01']['pwd']
                status=self.data['login_01']['status']
                assert_expected=self.data['login_01']['assert']
                self.wps.makeprotocol()
                try:
                    self.wps.Avatar()
                except:
                    self.wps.Table_my()
                self.assert_return=self.wps.iplogin(user, psw,status=status)
                self.log.info_log(('input data:username:%s,pwd:%s, test_nu:%s,assert:%s' % (user, psw, status, assert_expected)))
                self.assertEqual(assert_expected, self.assert_return, msg='fail resons:%s !=%s' % (assert_expected, self.assert_return))
            except Exception as e:
                self.log.error_log(u'失败原因:%s'%e)
                print('reg1 fail  reson is :%s'%e)

    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()

