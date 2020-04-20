# 1.20 (c) on Applied Numerical Methods Using MATLAB
# p65
import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(14, 16, 100)

y1 = np.sqrt(2 * x**2 + 1) - 1
y2 = 2 * x**2 / (np.sqrt(2 * x**2 + 1) + 1)

fig = plt.figure()
ax = fig.add_subplot(211)
ax.loglog(x, y1, 'bo-', x, y2, 'rx-')
ax.legend(('y1', 'y2'))

ax = fig.add_subplot(212)
ax.semilogx(x, y1 - y2, 'rx-', label='y1 - y2')
ax.legend()

plt.show()
