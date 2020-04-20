# 1.20 (e) on Applied Numerical Methods Using MATLAB
# p65
import numpy as np

try:
    print(300.0 ** 125.0 / np.prod(range(1, 126), dtype=np.float64) * np.exp(-300))
except OverflowError:
    print('int too large to convert to float!!!')

try:
    print((300.0 / np.exp(1.0)) ** 125.0 * np.exp(-175.0) / np.prod(range(1, 126), dtype=np.float64))
except OverflowError:
    print('int too large to convert to float!!!')


def p(k):
    # 1.20 (e) on Applied Numerical Methods Using MATLAB
    # p66
    lambda_ = 300

    if 1 == k:
        return lambda_ * np.exp(-lambda_)
    else:
        return p(k - 1) * lambda_ / k


print(p(125))
