#!/usr/bin/python
# -*- coding: UTF-8 -*-
####本模块主要作用是学习了解os模块
import os
#os.name()#判断现在正在使用的平台，windows返回‘nt’；Linux返回‘posix’
#os.getcwd()#得到当前工作的目录
#os.listdir()#指定所有目录下所有的文件和目录名。

#os.mkdir()#创建目录
#os.path.isfile()#判断指定的对象是否为文件，是返回True
#os.path.isdir()#判断指定的对象是否为目录。

#os.path.split()#返回路径的目录和文件名。

#os.getcwd()#获得当前工作的目录
#os.system()#执行shell命令>>
var=123
os.environ['var']=str(var)#此处[]内得是“字符串”
os.system('echo $var')

#os.chdir()#改变目录到指定目录
#os.path.getsize()#获得文件的大小，如果为目录，返回0
#os.path.abspath()#获得绝对路径
#os.path.join(path,name)#连接目录和文件名

#os.path.basename(path)#返回文件名
#os.path.dirname(path)#返回文件路径
#

import sys
if __name__=="__main__":
	#测试一些必要选项
	print os.name
	print os.getcwd()#获取当前的路径

	print os.path.realpath(sys.argv[0])
	print os.path.split(os.path.realpath(sys.argv[0]))
	print os.path.split(os.path.realpath(sys.argv[0]))[0]
