#!/usr/bin/python
# -*- coding: UTF-8 -*-
#创建一个数据函数
from numpy import *
import operator

#创建一个方法，生成dataset
def createDataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    print group
    labels = ['A', 'A', 'B', 'B']
    return group, labels