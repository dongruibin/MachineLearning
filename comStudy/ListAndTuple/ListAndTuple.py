#!/usr/bin/python
# -*- coding: UTF-8 -*-


#本模块主要使用list和tuple
#序列是python中最基本的数据结构，序列中的每个元素都分配一个
#数字，它的位置，从0开始
list1 = ['physics', 'chemistry', 1997, 2000]#不需要;
list2 = [1, 2, 3, 4, 5];

print "打印出list："
print list1
print list2
print "下标访问list1[0]:", list1[0]
#可以使用del语句del语句来删除列表的元素
del list1[0]
print "del list1[0]:", list1

#python列表函数&方法
#cmp(list1, list2)#比较两个列表元素
#len(list1)#列表元素个数
#max min(list)#放回列表最值
#list(seq)#将元组转换为列表



#python的元组与列表类似，不同之处在于元组的元素不能修改
#元组使用小括号，列表使用方括号
#元组创建很简单，只要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
#备注元组只要包含一个元素，需要在元素后面添加逗号。tup1=(50, );
#元组中的元素值不允许修改，但是我们可以对元组进行连接组合
str="元组中的元素值不允许修改，但是我们可以对元组进行连接组合"
print str
tup4=tup1+tup2
print "打印元组之中的元素："
print "tup2[2:5]:", tup2[2:5]

#tup1[0]=100;#该操作是非法的
#元组中的元素值是不允许删除的，但是可以使用del语句来删除整个元组。
#元组运算符
#与字符串一样，元组之间可以使用+和*进行运算，这就可以组合和复制。
print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "元组运算符：>>>>>>>"
print "计算元素个数：", len((1, 2, 3))
print "连接：", (1, 2, 3)+(4, 5, 6)
print "复制：", ("Hi", )*4
print "元素是否存在：",3 in (1, 2, 3)
print "迭代："
for x in (1, 2, 3):
	print x
L=('span', 'Span', 'SPAN')
print "读取第三个元素", L[2]
print "反向读取，读取倒数第二个元素：", L[-2]
print "截取元素：", L[1:]


