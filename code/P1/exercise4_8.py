# Exercise 4.8 Physical Modeling in MATLAB
import numpy as np
import matplotlib.pyplot as plt

n = 500
X = np.zeros(n)
r = 3.9

X[0] = 0.5
for i in range(n-1):
    X[i+1] = r * X[i] * (1 - X[i])

_ = plt.figure()
plt.plot(X)

_ = plt.figure()
for r in np.arange(2.4, 4.0, 0.1):
    for i in range(n-1):
        X[i+1] = r * X[i] * (1 - X[i])
    plt.plot(X)
    plt.title('r = {}'.format(r))

_ = plt.figure()
r = np.arange(2.4, 3.5, 0.001)
Y = np.zeros(len(r))
for j in range(len(r)):
    for i in range(n-1):
        X[i+1] = r[j] * X[i] * (1 - X[i])
    Y[j] = X[n-1]
plt.plot(r, Y)
plt.show()
