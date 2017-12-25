# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:50
# @Author  : Leo_Peng
# @File    : BasePage.py
# @Software: PyCharm
import os


class Base:
    app = os.path.abspath(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/App', 'moffice_10.6.2_1033.apk'))
    # 获取app的存放路径
    AppSetting = {
        'app': app,
        'appPackage': 'cn.wps.moffice_eng',
        'appAcitivity': 'cn.wps.moffice.documentmanager.PreStartActivity',
        'platformName': 'Android',
        'platformVersion': '4.4.2',
        'deviceName': u'夜神模拟器',
        'newCommandTimeout': 90,  # 设置收到下一条命令的超时时间,超时appium会自动关闭session ,默认60秒
        'unicodeKeyboard': True,  # 支持中文输入，会自动安装Unicode 输入法。默认值为 false
        'autoWebviewTimeout': 3000,  # 以毫秒为单位，等待Webview上下文激活的时间。默认值2000
        'resetKeyboard': True,  # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。
        'autoWebview': True  # 直接转换到 WebView 上下文。 默认值 false
    }













