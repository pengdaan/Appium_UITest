# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 16:37
# @Author  : Leo_Peng
# @File    : 1213_2.py
# @Software: PyCharm
# number对象_分数（有理数对象）
from fractions import Fraction
x=Fraction(1,3)
y=Fraction(4,6)
print(x,y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
a=Fraction('.25')
b=Fraction(1,4)
c=Fraction('1.25')
d=Fraction(5,4)
GG=a+b
print('GG',GG)
print(Fraction('.25')+Fraction('1.25'))

print(Fraction(1,10)+Fraction(1,10)+Fraction(1,10)-Fraction(3,10))

print(1/3)
print(Fraction(1,3))
print((1/3)+(6/12))
print(Fraction(2,3)+ Fraction(6,12))
print(Fraction(1000,1234567890))
print()