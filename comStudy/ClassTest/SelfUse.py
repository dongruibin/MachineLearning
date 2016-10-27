#!/usr/bin/python
# -*- coding: UTF-8 -*-

#明确self的使用
#首先self只有在类的方法中才会有，独立的函数或方法不必带有self的。
#self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
#self名称不是必须的，在python中self不是关键字，可以将self改为myname
#一样没有问题。

#self是指类实例对象本身(注意：不是类本身)
class Person:
	def __init__(self,name):#构造方法为__init__是两根"_"这样的下划线
		self.name=name
	def sayhello(self):
		print 'My name is :',self.name
		

#self是指向实例的，如果指向类，存在多个对象，就没有办法指了		
if __name__=='__main__':
	p=Person("dong")
	p1=Person('ding')
	print p