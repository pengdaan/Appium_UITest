# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 13:35
# @Author  : Leo_Peng
# @File    : test_1.py
# @Software: PyCharm
import pytest
# content of sample.py
def test_main():
   assert 1 + 2 == 3

if __name__ == '__main__':
   pytest.main("-q test_main.py")