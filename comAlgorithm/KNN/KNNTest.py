#!/usr/bin/python
# -*- coding: UTF-8 -*-

#同一个目录下直接导入文件

import KNN
from numpy import *
#K最近邻（K-Nearest Neighbor ,KNN)分类算法。它采用测量不同特征之间的距离进行分类
#思想：如果一个样本在特征空间中的K个最相似(即特征空间中最邻近)的样本中的大多数属于
#某个类别，则该样本也属于某一个类别
dataSet,labels=KNN.createDataSet()

testX=array([1.2,1.0])
k=3
outputLabel =KNN.kNNClassify(testX,dataSet,labels,3)
print "Your input is :",testX,"and classified to class:",outputLabel

testY=array([0.1,0.3])
outputLabel=KNN.kNNClassify(testY,dataSet,labels,3)
print "Your input is :",testY,"and classified to class:",outputLabel