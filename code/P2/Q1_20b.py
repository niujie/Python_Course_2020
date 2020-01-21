# 1.20 (b) on Applied Numerical Methods Using MATLAB
# p64
import numpy as np
import matplotlib.pyplot as plt

a = 1
c = 1
N = 100
b = np.logspace(7.4, 8.5, N)

x1 = 1 / (2*a) * (-b - np.sign(b) * np.sqrt(b**2 - 4*a*c))
x2 = 1 / (2*a) * (-b + np.sign(b) * np.sqrt(b**2 - 4*a*c))

x3 = c / a / x1

plt.semilogy(np.abs(x1), 'b-')
plt.semilogy(np.abs(x2), 'r-', linewidth=2)
plt.semilogy(np.abs(x3), 'k-', linewidth=2)
plt.legend(('x1', 'x2', 'x3'))
plt.show()
