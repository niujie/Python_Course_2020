# 1.20 (a) on Applied Numerical Methods Using MATLAB
# p64
import numpy as np

x = 9.8e201
y = 10.2e199


def z1(x_, y_):
    return np.sqrt(x_ ** 2 + y_ ** 2)


def z2(x_, y_):
    return y_ * np.sqrt((x_ / y_) ** 2 + 1)


try:
    print('z1({}, {}) = {}'.format(x, y, z1(x, y)))
except OverflowError:
    print('Too Large!')

print('z2({}, {}) = {}'.format(x, y, z2(x, y)))

x = 9.8e-201
y = 10.2e-199

print('z1({}, {}) = {}'.format(x, y, z1(x, y)))
print('z2({}, {}) = {}'.format(x, y, z2(x, y)))
