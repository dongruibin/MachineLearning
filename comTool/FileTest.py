#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys


try:
    fsock=open("D:/scn/test.txt","r")
except IOError:
    print "The file don't exist,Please double check!"
    exit()
print 'The file mode is ',fsock.mode
print 'The file name is ',fsock.name
