#!/usr/bin/python
# -*- coding: UTF-8 -*-

####测试for的使用
#for循环可以遍历任何序列的项目，如一个列表或者一个字符串
#for iterating_var in sequence:
#    statements(s)
for letter in 'Python':#
    print '当前字母：',letter

#第二列表
fruits=['banana','apple','mango']
for fruit in fruits:
    print '当前字母：',fruit

####通过序列索引迭代
for index in range(len(fruits)):
    print '当前水果：',fruits[index]

######循环使用else语句
for num in range(10,20):#迭代10到20之间的数字
    for i in range(2,num):#根据因子迭代
        if num%i==0:#确定第一个因子
            j=num/i#计算第二个因子
            print '%d等于 %d* %d'%(num,i,j)
            break#跳出当前循环
    else:#跳出当前循环
        print num,'是一个质数'