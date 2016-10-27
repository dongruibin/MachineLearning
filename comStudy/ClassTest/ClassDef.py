#!/usr/bin/python
# -*- coding: UTF-8 -*-

#主要说明Python类的定义以及使用方法

#__private_attrs两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问
#	在类内部的方法中使用时self.__private_attrs
#类的方法
#	在类内部，使用def关键字可以为类定义一个方法,与一般函数定义不同，类方法必须包含
#	参数self，且为第一个参数
#私有的类方法
#	__private_attrs_method两个下划线开头，声明该方法为私有方法，不能在类地外部调用
#	使用时，在类的内部调用self.__private_methods
#类的专有方法
#	__init__构造函数，在生成对象时调用
#	__del__析构函数，释放对象时使用
#	__repr__打印，转换
#	__setitem__按照索引赋值
#	__getitem__按照索引获取值
#	__len__获得长度
#	__cmp__比较运算
#	__call__函数调用
#	__add__加运算
#	__sub__减运算
#	__mul__乘运算
#	__div__除运算
#	__mod__求余运算
#	__pow__称方

#类定义
class people:
	#定义基本属性
	name=''
	age=0
	#定义私有属性，私有属性在类外部无法直接进行访问
	__weight=0
	#定义构造方法
	def __init__(self,n,a,w):
		self.name=n
		self.age=a
		self.__weight=w
	def speak(self):
		print("%s is speaking:I am %d years old"%(self.name,self.age))

#实现单继承
#继承格式 class 类名(父类名):
class student(people):#继承People父类
	grade=''
	def __init__(self,n,a,w,g):
		#调用父类的构造函数
		people.__init__(self,n,a,w)
		self.grade=g
	#覆写父类的方法
	def speak(self):
		print("%s is speaking: I am %d years old,and I am in grade%d"%(self.name,self.age,self.grade))
#实现类的多重继承
#实现格式 class 类名(父类名1，父类名2，父类名3...父类名n)
class speaker():
	topic=''
	name=''
	def __init__(self,n,t):
		self.name=n
		self.topic=t
	def speak(self):
		print("I am %s,I am a speaker!My topic is %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
	a=''
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)
		
		
if __name__=='__main__':
	#测试第一个类
	p=people('tom',10,30)
	p.speak()
	#测试第二个类，即单继承的类的使用
	s=student('ken',20,60,3)
	s.speak()
	#测试多继承
	test=sample("Tim",25,80,4,"Python")
	test.speak()#方法名同，默认调用的是在括号中排前地父类的方法