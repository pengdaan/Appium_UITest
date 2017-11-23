#coding=utf-8
import os
from appium import webdriver
app = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/App','20171109 17_22_27_com.andli.myproject_1.0.apk'))

# 1.获取app绝对路径
# 2.将多个路径组合后返回
capabilities = {
    'app': app,
    'appPackage': 'com.xmyy.smarthome',
    'appActivity': 'com.xmyy.smarthome.version2.SplashActivity',
    'platformName': 'Android',
    'platformVersion': '4.4.2',
    'deviceName': u'夜神模拟器',
    'newCommandTimeout': 90,  # 设置收到下一条命令的超时时间,超时appium会自动关闭session ,默认60秒
    'unicodeKeyboard': True,  # 支持中文输入，会自动安装Unicode 输入法。默认值为 false
    'autoWebviewTimeout': 3000,  # 以毫秒为单位，等待Webview上下文激活的时间。默认值2000
    'resetKeyboard': True,  # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。
    'autoWebview': True  # 直接转换到 WebView 上下文。 默认值 false
}
driver=webdriver.Remote('http://localhost:4723/wd/hub', capabilities)