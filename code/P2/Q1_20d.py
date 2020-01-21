# 1.20 (d) on Applied Numerical Methods Using MATLAB
# p65
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10**-9, 10**-7.4, 100)

y1 = np.sqrt(x + 4) - np.sqrt(x + 3)
y2 = 1 / (np.sqrt(x + 4) + np.sqrt(x + 3))

fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y1, 'bo-', x, y2, 'rx-')
ax.legend(('y1', 'y2'))

ax = fig.add_subplot(212)
ax.plot(x, y1 - y2, 'rx-', label='y1 - y2')
ax.legend()

plt.show()
