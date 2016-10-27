#!/usr/bin/python
# -*- coding: UTF-8 -*-

#本文件的主要作用是熟练下函数的使用

#定义函数
#1.函数代码使用def关键字，后面接函数标识符和圆括号（）
#2.任何传入参数和自变量必须放在圆括号里面。
#3.函数第一行语句可以选择性的使用文档字符串，用于存放函数说明
#4.函数内容以冒号起始，必须缩进
#5.return 结束函数，选择性的返回一个值给调用方，不带的话，相当于None

#注意：按值传递参数和按引用传递参数
#所有参数（自变量）在Python里都是按引用传递，函数里面修改，调用这个函数，原始参数也被修改。
#可写函数说明

def change (mylist):
    "修改传入的参数"
    mylsit.append([1,2,3,4]);
    print "函数内取值：",mylist
    return