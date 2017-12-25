# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 15:47
# @Author  : Leo_Peng
# @File    : 1222_2.py
# @Software: PyCharm
s1='spa"m'
s2="sp'am"
s3='''...spam...''',"""...spam..."""
s4="s\tp\na\om"
s5=r"c:\a\b\test.py"

s6='A"s',"ASAA's" #使用逗号，转换成元组
print('s6',s6)
s7="Meaning "" of " "life" #字符串拼接
print('s7',s7)
s8='kinght\'s',"kinght\'s" #使用转义字符
print('s8',s8)
s9='king\t''6666'
print(s9)
s10='a\0b\0c'
print(s10,len(s10))
s11='\001\002\x03'
print(s11)

