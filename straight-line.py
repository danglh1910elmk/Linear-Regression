import numpy as np 
import matplotlib.pyplot as plt

A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46] # x
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  # y

# change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T

# draw data
plt.plot(A,b,'ro')


A = np.hstack((A, np.ones( (len(A), 1) )))

# use formula
x = np.linalg.inv(A.T@A)@A.T@b

x0 = [0,50]
plt.plot(x0, x[0]*x0+x[1])
plt.show()