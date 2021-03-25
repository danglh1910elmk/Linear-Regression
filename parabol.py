import numpy as np 
import matplotlib.pyplot as plt

# random data
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]

# change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T

# draw data
plt.plot(A,b,'ro')

A = np.hstack((A**2, A, np.ones((len(A), 1))))


# use formula
x = np.linalg.inv(A.T@A)@A.T@b


x0 = np.linspace(0,30,1000)
y0 = x[0]*x0**2 + x[1]*x0 + x[2]
plt.plot(x0, y0)
plt.show()