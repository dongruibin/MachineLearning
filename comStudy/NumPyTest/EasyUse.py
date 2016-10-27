#!/usr/bin/python
# -*- coding: UTF-8 -*-


#标准安装的Python中使用列表(list)保存一组值，可以用来当作数组使用，不过由于列表的元素可以是任何
#对象，因此列表中所保存的是兑现的指针。
#Python还有一个array模块，array对象和列表不同，它直接保存数值，和C语言的一维数组比较类似。但是没有
#多维，也没有各种运算函数，因此不适合做数值运算。

#NumPy提供了两种基本的对象：ndarray(N-dimensional array object)和ufunc(universal function object).
#ndarray(下文称为数组)是存储单一数据类型的多维数组，而ufunc则是能够对数组进行处理的函数。


#Numpy数组的维数称为秩(rank)，一维数组的秩为1，二维数组的秩为2，以此类推，在numpy中，每一个线性
#的数组称为一个轴(axes)，秩其实就是轴的数量。
#NumPy里面比较重要ndarray对象的属性：
#ndarry.ndim:数组维数（即数组的轴个数）
#ndarry.shape 数组的维数，为了表示数组在每个维度上大小的整数元组。
#	例如二维数组中，表示数组的“行数”和“列数”。ndarray.shape返回一个元组。
#ndarray.size 数组元素的总个数，等于shape属性中元素的乘积。
#函数库的导入
import numpy as np

#array函数的使用
a = np.array([1,2,3,4])
b = np.array((5,6,7,8))#注意格式与上面不一样
#创建多维函数
c=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

def printArray():
	#数组a的shape只有一个元素，因此它是一维数组，而数组
	#c的shape有两个元素，因此它是二维数组，其中第0轴的长度
	#为3(自己理解相当是3列)，第二轴长度为4(字节理解是每组列数)。
	#还可以通过修改数组的shape属性，在保持数组元素个数不变的情况下，
	#改变数组每个轴的长度，注：不是转置。
	#注：当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度，
	#使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape
	#保持不变。
	print a.shape
	print c.shape
	c.shape=4,3
	print c
	
	#数组元素的存取方法和Python的标准方法相同，可以使用脚标配
	#数组元素的存取
	print a[0]
	
	#使用范围作为下标获取数组的一个切片，包括a[1]不包括a[3]
	#省略下标，从0开始，后面如果还有参数，表示步长
	#步长为负值表示整个数组头尾颠倒
	print a[1:3]
	
	#注意通过下标范围产生的新数组，是原始数组的一个视图，它与原始数组
	#共享同一块数据空间
	h=a[1:3]
	

	#arange函数类似于Python的range函数，通过指定开始值，终值和步长来创建一维数组
	#注意不包含终值
	d=np.arange(0,1,0.1)
	print d



#测试文件处
if __name__=='__main__':
	print a
	print b
	print c
	#属性打印测试
	printArray()
