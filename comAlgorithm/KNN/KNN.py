#!/usr/bin/python
# -*- coding: UTF-8 -*-

#文件里面含有两个函数，一个用于生成小数据库，一个实现KNN分类算法

#####################################################
##KNN  K Nearest Neighbors
# Input newInput: vector to compare to existing dataset(1xN)
#       dataset: size m data set of know vector(NxM)
#       labels: data set labels
#       k:      number of neighbors to use for comparison

#Output: the most popular class label
#######################################################
from numpy import *
import operator

#create a dataset which contains 4 samples with 2 classes
#使用的是numpy里面的array
def createDataSet():
    #create a matrix :each row as a sample
    group= array([[1.0,0.9],[1.0,1.0],[0.1,0.2],[0.0,0.1]])
    labels=['A','A','B','B'] #four samples and two classes
    return group,labels
#classify using kNN
def kNNClassify(newInput,dataSet, labels,k):
    #数组的一维长度--
    numSamples=dataSet.shape[0]#shape[0] stands for the number of row
    #numSamples为输入的数组的行？
    ##step 1:calculate Euclidean distance
    #tile(A,reps):Constract an array by repeating A reqs times
    #the following copy numSamples rows for dataSet

    #以下是计算待分类的点和训练集中的任一点的欧式距离
    #tile函数位于python模块 numpy.lib.shape_base中，功能是重复某个数组
    #例如tile(A,n),功能是将数组A重复n次，构成一个新的数组
    diff =tile(newInput,(numSamples,1))-dataSet#Subtract element-wise#
    print "输入的数组和dataSet的shape[0]为："
    print newInput,numSamples
    print "显示一下diff的值："
    print diff
    squaredDiff=diff**2 #squared for dataSet#取平方
    print "显示一下squaredDiff的值："
    print squaredDiff

    squaredDist=sum(squaredDiff,axis=1)#sum is performed by row#按行求和
    distance=squaredDist**0.5
    ##step2: sort the distance
    #argsort() returns the indices that  would sort an array in ascending  orfer
    #下面是一些统计工作
    sortedDistIndices=argsort(distance)

    classCount={}#define a dictionary (can be append element)
    for i in xrange(k):
        ##step 3: choose the min k distance
        voteLabel=labels[sortedDistIndices[i]]

        ##sted 4:count the times labels occur
        #when the key voteLabel is not in dictionary classCount, get()
        #will return 0
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    ##step 5: the max voted class will return
    maxCount=0
    for key,value in classCount.items():
        if value>maxCount:
            maxCount=value
            maxIndex=key
    return maxIndex


if __name__=='__main__':
    a=[0, 1, 2]
    b=tile(a,2)
    print '将a数组复制两遍'
    print b
    #假如输入一个元组（1,2）
    print '输入元组（1,2）：'
    b=tile(a, (1,2))
    print b
    #假如想变成二维数组
    print '输入元组（2，1）'
    b=tile(a, (2,1))
    print b
    #输入其他元组
    print '输入元组（3,1）'
    print tile(a, (3,1))
    #其它
    print '输入元组（3,2）'
    print tile(a, (3,2))