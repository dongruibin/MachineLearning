#!/usr/bin/python
# -*- coding: UTF-8 -*-


#爬taoMM
import urllib
import urllib2
import re
#test other package
from comTry.OpenWeb import openUrl


print 'It is ok'
class Spider:
    #页面初始化
    def __init__(self):
        self.url='www.baidu.com'
        self.dong='aa'
        self.__don='bb_cc'#私有变量创建
        print 'This is Spider class'
    def myPrint(self,km):
        print km
    def myFounction(self,a,b):
        a=a*a
        b=b*b
        return (a,b)
class NewSpider(Spider):
    def __init__(self):
        print'This is NewSpider class'
    def myPrint(self,km):
        print 'This new class'


#Spider spider--object of Spider
spider=Spider()
spider.myPrint('www.baodu.com')
print spider.url
print spider.dong
print spider._Spider__don#调用私有变量
#other package
#opurl=openUrl('www.baidu.com')
#opurl.openweb()
newSpider = NewSpider()
#newSpider.myPrint('dong')