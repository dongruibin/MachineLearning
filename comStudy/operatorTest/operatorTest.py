#!/usr/bin/python
# -*- coding: UTF-8 -*-
#本模块主要是讲解operator模块使用
import operator
a=[1,2,3,4]
b=[5,6,7,8]
c = map(operator.mul,a,b)
print c
print operator.add(13,3)