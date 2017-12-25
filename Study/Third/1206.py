# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 11:50
# @Author  : Leo_Peng
# @File    : 1206.py
# @Software: PyCharm
list01=['SB',789,123,'join',60.2]
list02=[123,'leo']
list03=[1,2,3,4,5]
list04=[5,8,956,31,1]
print('获取列表长度',len(list01))
print('获取索引对应的值',list01[1])
list01.append('leo')
print('打印append后的列表',list01)
del list01[0]
print('打印删除后的列表',list01)
list01.insert(0,'gread')
print('打印插入元素后的字符串',list01)
list01.remove(list01[4])
print('打印移除的后的list',list01)
list02.pop(1)
print('打印减去后的list',list02)
print('统计出现次数',list01.count('SB'))
print('获取列表最大值',max(list03))
print('获取列表最小值',min(list03))
list04.sort()
print('对元素进行顺序排序',list04)
list04.reverse()
print('对元素进行反向排序',list04)
