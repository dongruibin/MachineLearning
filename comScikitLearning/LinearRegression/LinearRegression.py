#!/usr/bin/python
# -*- coding: UTF-8 -*-
#学习scikit-learn
#	This example use the only the first feature of the
#diabetes dataset,in order to illustrate(表明) a two-dimensional(维的) 
#plot of this regression technique.
print(__doc__)
#导入
import matplotlib.pyplot as plt
import numpy as np
#from sklearn import datasets,  linear_model#注意，的位置，前面没有空格，后面有空格
from sklearn import datasets, linear_model

#Load the diabetes dataset
diabetes=datasets.load_diabetes()

#use only one feature
diabetes_X=diabetes.data[:,np.newaxis,2]

#Split the data into training/testing sets
diabetes_X_train=diabetes_X[:-20]
diabetes_X_test=diabetes_X[-20:]

#Split the targets into training/testing sets
diabetes_y_train=diabetes.target[:-20]
diabetes_y_test=diabetes.target[-20:]

#Create linear regression object
regr=linear_model.LinearRegression()

#Train the model using the training sets
regr.fit(diabetes_X_train,diabetes_y_train)

#The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"% np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()