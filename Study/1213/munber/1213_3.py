# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 18:01
# @Author  : Leo_Peng
# @File    : 1213_3.py
# @Software: PyCharm
#转换和混合类型
import fractions
print((2.5).as_integer_ratio())
a=0.5
a.as_integer_ratio()
print(a.as_integer_ratio())
f =2.5
z= fractions.Fraction(*f.as_integer_ratio())
print(z)
x=fractions.Fraction(1,3)
print(x+z)
print(float(x))
print(float(x+z))
print(fractions.Fraction.from_float(1.75))
print(fractions.Fraction(*(1.75).as_integer_ratio()))
print(4.0/3)
print((4.0/3).as_integer_ratio())
g=x + fractions.Fraction(*(4.0/3).as_integer_ratio())
print(g.limit_denominator(10))