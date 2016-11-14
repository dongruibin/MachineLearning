#!/usr/bin/python
# -*- coding: UTF-8 -*-

#本模块主要是明确numpy里面的sum模块使用
import numpy as np

L = range(5)#生成一个列表[0,1,2,3,4]

#一、首先看一下python上自带的sum。
#sum是内建函数，返回一个数字序列（非字符串）的和
#并加上参数‘start'的值（默认为0），如果序列为空，
#则返回参数start的值（如果start为赋值，则出错）
print sum(L)#求列表的和，参数start值为0
print sum(L, -5)

#二、numpy里面的sum的使用
#sum(a,axis=None,dtype=Nope, out=None, keepdims=False)
#可以使用help(sum)查看具体的param
#默认axis为None,表示将所有元素的值相加
#对于二维数组
#axis=1表示按行相加，axis=0表示按列相加
print np.sum(L)
print np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
print np.sum([[0, 1], [0, 5]])
print np.sum([[0, 1], [0, 5]], axis=0)#axis=0是按列求和
print np.sum([[0, 1], [0, 5]], axis=1)#axis=1是按行求和