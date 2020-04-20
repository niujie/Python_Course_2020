# Exercise 4.7 Physical Modeling in MATLAB
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

n = 10000
# pre-allocate arrays
x = np.zeros(n, dtype=float)
y = np.zeros(n, dtype=float)
z = np.zeros(n, dtype=float)

# initial values
x[0] = 1.0
y[0] = 2.0
z[0] = 3.0

# parameters
sigma = 10.0
b = 8.0 / 3.0
r = 28.0
dt = 0.01

for i in range(n-1):
    x[i+1] = x[i] + sigma * (y[i] - x[i]) * dt
    y[i+1] = y[i] + (x[i] * (r - z[i]) - y[i]) * dt
    z[i+1] = z[i] + (x[i] * y[i] - b * z[i]) * dt

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.plot(x, y, z, 'k.', markersize=0.5)
ax.plot(x, y, z)
plt.show()
