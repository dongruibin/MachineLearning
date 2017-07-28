#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import webbrowser module
import webbrowser as wb

url='www.baidu.com'
wb.open(url,0,True)

#wb.close()

class openUrl:
    def __init__(self,url):
        self.myurl=url
    def openweb(self):
        wb.open(self.myurl,0,True)
    def closeweb(self):
        #wb.close()
        print 'need close'


