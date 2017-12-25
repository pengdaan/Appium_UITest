# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 11:48
# @Author  : Leo_Peng
# @File    : 1205.py
# @Software: PyCharm

a="ZJ"
print("双引号生成字符串",a)
b='SB'
print('单引号创建字符串',b)
c=a+b
print('字符串+号拼接',c)
a=a*3
print('字符串乘法',a)
print('字符串长度：',len(a))
line='1 2 3 4 5'
nu=line.split()
print('使用空格进行分割',nu)
lines='1,2,3,4,5'
nus=line.split(',')
print('使用逗号进行分割',nus)
d=''
e=d.join(nus)
print('使用空格将元素连起来，生成新的字符串：',e)
nus='12345'
f=','
f=f.join(nus)
print('使用,将元素连起来，生成新的字符串：',f)
print('小写转换大写','hello'.upper())
print('大写转小写','HELLO'.lower())
g='HEllo'
g.replace('HE','he')
print('替换',g.replace('HE','he'))

s = "  hello world   "
print('返回一个将s两端的多余空格除去的新字符串',s.strip())
print('返回一个将s开头的多余空格除去的新字符串',s.lstrip())
print('返回一个将s结尾的多余空格除去的新字符串',s.rstrip())

s = "some numbers:"
x = 1.34
y = 2
# 用百分号隔开，括号括起来
t = "%s %f, %d" % (s, x, y)
print('使用%格式化字符串',t)


# 字符串中花括号 {} 的部分会被format传入的参数替代，传入的值可以是字符串，也可以是数字或者别的对象。
g='{} {} {}'.format('a','b','c')
print(g)
# 可以用数字指定传入参数的相对位置
h='{2} {1} {0}'.format('a', 'b', 'c')
print(h)

# 还可以指定传入参数的名称：
i='{color} {n} {x}'.format(n=10, x=1.5, color='blue')
print(i)
# 混合用法
j='{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color='blue')
print(j)