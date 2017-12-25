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
from PO.BasePage import *
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Login(unittest.TestCase):

    @classmethod
    def setUp(cls):
        title=u'登录测试'
        cls.log=logger.Logger(title)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.AppSetting)
        cls.drivers=CommonDriver(cls.driver)
        cls.wps = WpsLoginPage.Wps(cls.drivers)
        cls.faile=open(path + '/Data/LoginData.ymal','r',encoding='utf-8')
        cls.data = yaml.load(cls.faile)
        cls.faile.close()

    # def test_QQLogin(self):
    #     u'''使用QQ账号登录'''
    #     self.wps.makeprotocol(status=True)
    #     self.driver.saveScreenshot(name='Error')
    #     self.wps.Table_my()

        # try:
        #     try:
        #         self.wps.makeprotocol(status=True)
        #         try:
        #             self.wps.Avatar()
        #         except:
        #             self.wps.Table_my()
        #             self.wps.qqlogin('321321', '176')
        #     except:
        #         #self.driver.saveScreenshot(name='Error')
        #         self.driver.launch_app()
        #
        # except Exception as e:
        #     self.log.error_log(u'失败原因:%s' % e)
        #     print('reg1 fail  reson is :%s' % e)






    def test_ipLogin(self):
        u'''使用phone账号登录'''
        Title = self.data['login_01']['Title']
        user = self.data['login_01']['user']
        psw = self.data['login_01']['pwd']
        status = self.data['login_01']['status']
        assert_expected = self.data['login_01']['assert']
        self.wps.makeprotocol()
        self.wps.Table_my()
        self.assert_return=self.wps.iplogin(user, psw,status=status)
        self.log.info_log(('input data:username:%s,pwd:%s, test_nu:%s,assert:%s' % (user, psw, status, assert_expected)))
        self.assertTrue(False)
        #self.assertEqual(assert_expected, self.assert_return, msg='fail resons:%s !=%s' % (assert_expected, self.assert_return))
        #time.sleep(5)







    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()

