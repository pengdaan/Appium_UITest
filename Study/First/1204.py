# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:23
# @Author  : Leo_Peng
# @File    : 1204.py
# @Software: PyCharm
import random
Number=[1,2,3,4,5,6,7,8,9,10]
number=[11,12,13,14]
# 从随机数列中挑选一个元素
Choice=random.choice(Number)
print('从随机数列中挑选一个元素:',Choice)

# 从指定的范围内按指定基数递增的集合中获取一个随机数，基数缺省值为1
Ranrdange=random.randrange(Number[0],number[1])
print('从指定的范围内按指定基数递增的集合中获取一个随机数:',Ranrdange)
Ranrdanges=random.randrange(10000,99999)
print('生成4位数的随机数:',Ranrdanges)

# 随机生成一个实数，区间范围为0-1
a=random.random()
print('随机生成一个实数，区间范围为0-1:',a)

# 生成一个区间内的实数，返回一个浮点类型的值
b= random.uniform(10,20)
print('生成一个区间内的实数，返回一个浮点类型的值:',b)

# 根据某种子器生成一个随机数,同一种子生成器生成一样的随机数
a_1=random.choice([1,2,3])
random.seed(a_1)
print(('1号种子的生成的随机数为：%s')%(str(random.choice(Number))))
a_2=random.choice([1])
random.seed(a_2)
print(('2号种子的生成的随机数为：%s')%(str(random.choice(Number))))
if a_2==a_1:
    print('种子的号码一致：',a_1,a_2)
else:
    print('种子的号码不一致')

print(1<2)