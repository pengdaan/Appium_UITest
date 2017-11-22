# -*- coding: utf-8 -*-
__author__ = 'JennyHui'
import unittest
import yaml
from PO import WpsPage
from public.CommonDriver import *
import os
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class Login(unittest.TestCase):
    def setUp(self):
        self.driver=CommonDriver()
        self.wps = WpsPage.Wps(self.driver)
        self.faile=open(path + '/Data/LoginData.ymal','r',encoding='utf-8')
        self.data = yaml.load(self.faile)
        self.faile.close()


    def test_QQLogin(self):
        u'''使用QQ账号登录'''
        self.wps.makeprotocol()
        try:
            self.wps.Avatar()
        except:
            self.wps.Table_my()
        self.wps.qqlogin('321321', '176')

    def test_ipLogin(self):
            u'''使用phone账号登录'''
            self.user = self.data['login_01']['user']
            self.psw = self.data['login_01']['pwd']
            self.status=self.data['login_01']['status']
            self.assert_expected=self.data['login_01']['assert']
            self.wps.makeprotocol()
            try:
                self.wps.Avatar()
            except:
                self.wps.Table_my()
            self.assert_return=self.wps.iplogin(self.user, self.psw,self.status)
            self.assertEqual(self.assert_expected, self.assert_return, msg='fail resons:%s !=%s' % (self.assert_expected, self.assert_return))


    def tearDown(self):
        pass
        # self.driver.quit()
        # self.driver.close()



if __name__ == '__main__':
    unittest.main()

