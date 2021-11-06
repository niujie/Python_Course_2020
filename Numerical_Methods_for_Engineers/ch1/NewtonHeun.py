# src-ch1/NewtonHeun.py
# Program Newton
# Computes the solution of Newton's 1st order equation (1671):
# dy/dx = 1-3*x + y + x^2 +x*y , y(0) = 0
# using Heun's method.

import matplotlib.pylab as plt
from scipy.special import erf
import numpy as np

xend = 2
dx = 0.1
steps = np.int(np.round(xend/dx, 0)) + 1
y, x = np.zeros((steps, 1), float), np.zeros((steps, 1), float)
y[0], x[0] = 0.0, 0.0

for n in range(0, steps-1):
    x[n+1] = (n+1)*dx
    xn = x[n]
    fn = 1 + xn*(xn-3) + y[n]*(1+xn)
    yp = y[n] + dx*fn
    xnp1 = x[n+1]
    fnp1 = 1 + xnp1*(xnp1-3) + yp*(1+xnp1)
    y[n+1] = y[n] + 0.5*dx*(fn+fnp1)

# Analytical solution
a = np.sqrt(2)/2
t1 = np.exp(x*(1 + x/2))
t2 = erf((1+x)*a)-erf(a)
ya = 3*np.sqrt(2*np.pi*np.exp(1))*t1*t2 + 4*(1-t1)-x

# plotting

# change some default values to make plots more readable
LNWDT = 2
FNT = 11
plt.rcParams['lines.linewidth'] = LNWDT
plt.rcParams['font.size'] = FNT

plt.plot(x, y, '-b.', x, ya, '-g.')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Solution to Newton\'s equation')
plt.legend(['Heun', 'Analytical'], loc='best', frameon=False)
plt.grid()
plt.show()
