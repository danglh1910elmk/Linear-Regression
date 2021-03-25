import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model

A = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]]).T # x
b = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T  # y
plt.plot(A, b, 'ro')

# create model
lr = linear_model.LinearRegression()
lr.fit(A, b) # train the model

# y = mx+n
m = lr.coef_ # coefficient
n = lr.intercept_ # intercept

x0 = np.array([[0,50]]).T
y0 = m*x0 + n
plt.plot(x0, y0)
plt.show()