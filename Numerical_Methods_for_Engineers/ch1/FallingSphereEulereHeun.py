# src-ch1/FallingSphereEulerHeun.py;ODEschemes.py @ git@lrhgit/tkt4140/src/src-ch1/ODEschemes.py;
from DragCoefficientGeneric import cd_sphere
from ODEschemes import euler, heun
from matplotlib.pyplot import *
import numpy as np

# change some default values to make plots more readable
LNWDT = 2
FNT = 11
rcParams['lines.linewidth'] = LNWDT
rcParams['font.size'] = FNT

g = 9.81      # Gravity m/s^2
d = 41.0e-3   # Diameter of the sphere
rho_f = 1.22  # Density of fluid [kg/m^3]
rho_s = 1275  # Density of sphere [kg/m^3]
nu = 1.5e-5   # Kinematical viscosity [m^2/s]
CD = 0.4      # Constant drag coefficient


def f(z, t):
    """2x2 system for sphere with constant drag."""
    zout = np.zeros_like(z)
    alpha = 3.0*rho_f/(4.0*rho_s*d)*CD
    zout[:] = [z[1], g - alpha*z[1]**2]
    return zout


def f2(z, t):
    """2x2 system for sphere with Re-dependent drag."""
    zout = np.zeros_like(z)
    v = abs(z[1])
    Re = v*d/nu
    CD = cd_sphere(Re)
    alpha = 3.0*rho_f/(4.0*rho_s*d)*CD
    zout[:] = [z[1], g - alpha*z[1]**2]
    return zout

# main program starts here


T = 10  # end of simulation
N = 20  # no of time steps
time = np.linspace(0, T, N+1)

z0 = np.zeros(2)
z0[0] = 2.0

# compute response with constant CD using Euler's method
ze = euler(f, z0, time)
# compute response with varying CD using Euler's method
ze2 = euler(f2, z0, time)

# compute response with constant CD using Heun's method
zh = heun(f, z0, time)
# compute response with varying CD using Heun's method
zh2 = heun(f2, z0, time)

k1 = np.sqrt(g*4*rho_s*d/(3*rho_f*CD))
k2 = np.sqrt(3*rho_f*g*CD/(4*rho_s*d))
# compute response with constant CD using analytical solution
v_a = k1*np.tanh(k2*time)

# plotting

legends = []
line_type = ['-', ':', '.', '-.', '--']

plot(time, v_a, line_type[0])
legends.append('Analytical (constant CD)')

plot(time, ze[:, 1], line_type[1])
legends.append('Euler (constant CD)')

plot(time, zh[:, 1], line_type[2])
legends.append('Heun (constant CD)')

plot(time, ze2[:, 1], line_type[3])
legends.append('Euler (varying CD)')

plot(time, zh2[:, 1], line_type[4])
legends.append('Heun (varying CD)')

legend(legends, loc='best', frameon=False)

xlabel('Time [s]')
ylabel('Velocity [m/s]')
grid()
show()
