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
            self.user = self.data['login']['user']
            self.psw = self.data['login']['pwd']
            self.wps.makeprotocol()
            try:
                self.wps.Avatar()
            except:
                self.wps.Table_my()
            self.wps.iplogin(self.user, self.psw)



    def tearDown(self):
         self.driver.quit()
    #     self.driver.close()



if __name__ == '__main__':
    unittest.main()

