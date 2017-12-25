# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 14:32
# @Author  : Leo_Peng
# @File    : 1213_1.py
# @Software: PyCharm
import math
import decimal
print(math.pi,math.e)
#使用小数对象,decimal.Decimai()传入的为字符串
print(decimal.Decimal((decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3'))))
#全局设置精度,获取上下门对象，允许指定的精度（小数后4位）和舍入模式
decimal.getcontext().prec= 4
print(decimal.Decimal(decimal.Decimal('1')/decimal.Decimal('7')))

print(decimal.Decimal(decimal.Decimal('1999')+decimal.Decimal('1.33')))
print(decimal.Decimal(str(1999+1.33)))

