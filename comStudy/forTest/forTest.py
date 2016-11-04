#!/usr/bin/python
# -*- coding: UTF-8 -*-

####测试for的使用
#for循环可以遍历任何序列的项目，如一个列表或者一个字符串
#for iterating_var in sequence:
#    statements(s)
for letter in 'Python':#
    print '当前字母：',letter

#第二列表
#列表可以使用下标进行访问，具体可以见下面的使用
fruits=['banana','apple','mango']
for fruit in fruits:
    print '当前字母：',fruit

####通过序列索引迭代
#这里的fruits为一个列表，使用下标进行元素的访问。
#列表的使用--len---获取列表长度
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

print "演示列表的使用（主要是元素的截取）>>>>>>>"
####列表使用示例----使用下标进行访问,下标从0开始
print "fruits[0]:",fruits[0]
#注意[ss:xx],是包含ss下标这个元素，而不包含xx这个末尾元素
print "fruits[0:1]:",fruits[0:1]
print "fruits[0:2]：",fruits[0:2]
print "fruits[0:3]：",fruits[0:3]
#打印倒数过来的元素
print "fruits[-1]:",fruits[-1]#倒数第一个

#列表使用的函数
#cmp(list1,list2)#比较两个列表的元素
#len(list)#列表元素个数
#max(list)#返回列表元素最大值
#min(list)
#list(seq)#将元组转换为列表

#列表中包含的方法
#list.append(obj)#在列表末尾添加新的对象
#list.count(obj)#统计某个元素在列表中出现的次数
#list.extend(seq)#在列表末尾一次性追加另一个序列中的多个值（用新列表来扩展原来的列表）
#list.index(obj)#从列表中找出某个值第一个匹配项的索引位置
#list.insert(index,obj)#将对象插入列表
#list.pop(obj=list[-1])#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
#list.remove(obj)#移除列表中某个值得第一个匹配项
#list.reverse()#反向列表中元素
#list.sort([func])#对原列表进行排序

