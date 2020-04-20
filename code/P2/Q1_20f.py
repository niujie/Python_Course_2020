import numpy as np


def S(K):
    # 1.20 (f) on Applied Numerical Methods Using MATLAB
    # p65

    lambda_ = 100
    out = np.exp(-lambda_)
    for k in range(1, K + 1):
        out = out + p(k, lambda_)

    return out


def p(k, lambda_):
    # 1.20 (e) on Applied Numerical Methods Using MATLAB
    # p66

    if 1 == k:
        return lambda_ * np.exp(-lambda_)
    else:
        return p(k - 1, lambda_) * lambda_ / k


print(S(100))
