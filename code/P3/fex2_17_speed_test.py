# speed comparison of matrix inversion using inv and solve
import numpy as np
import time
import matplotlib.pyplot as plt


def fex2_17(x_, omega_):
    # Iteration formula Eq. (2.35) for Example 2.17 on Numerical Methods in
    # Engineering with MATLAB. 2nd Edition

    n_ = len(x_)
    x_[0] = omega_ * (x_[1] - x_[n_ - 1]) / 2.0 + (1.0 - omega_) * x_[0]
    for i_ in range(1, n_ - 1):
        x_[i_] = omega_ * (x_[i_ - 1] + x_[i_ + 1]) / 2.0 + (1.0 - omega_) * x_[i_]

    x_[n_ - 1] = omega_ * (1 - x_[0] + x_[n_ - 2]) / 2.0 + (1.0 - omega_) * x_[n_ - 1]

    return x_


def gaussSeidel(func, x_, *args):
    """Solves Ax = b by Gauss-Seidel method with relaxation.
    USAGE: [x, numIter, omega] = gaussSeidel(func, x, maxIter, epsilon)
    INPUT:
    func    = handle of function that returns improved x using
              the iterative formulas
    x       = starting solution vector
    maxIter = allowable number of iterations (default is 500)
    epsilon = error tolerance (default is 1.0e-9)
    OUTPUT:
    x       = solution vector
    numIter = number of iterations carried out
    omega   = computed relaxation factor"""

    if len(args) < 2:
        epsilon = 1.0e-9
    if len(args) < 1:
        maxIter = 5000
    k = 10
    p = 1
    omega_ = 1
    for numIter_ in range(maxIter):
        xOld = x_.copy()
        x_ = func(x_, omega_)
        dx = np.sqrt(np.dot(x_ - xOld, x_ - xOld))
        if dx < epsilon:
            return x_, numIter_, omega_
        if numIter_ == k:
            dx1 = dx
        if numIter_ == k + p:
            omega_ = 2.0 / (1.0 + np.sqrt(1.0 - (dx / dx1) ** (1.0 / p)))

    print('Too many iterations')
    return x_, maxIter, omega_


# speed comparison between Gauss Seidel method and MATLAB intrinsic \ operator
# to solve Example 2.17 on Numerical Methods in Engineering with MATLAB. 2nd Edition

N = 20
m = np.round(np.logspace(1, 2, N)).astype(np.int)
time_cost = np.zeros((N, 2))

ntimes = 5
for i in range(len(m)):
    A = np.eye(m[i])
    b = np.zeros(m[i])
    b[-1] = 1
    A = A * 2
    for n in range(1, m[i]):
        A[n, n - 1] = -1   # A = A + diag(eye(n-1)*-1, -1);
        A[n-1, n] = -1     # A = A + diag(eye(n-1)*-1, 1);

    A[0, -1] = 1
    A[-1, 0] = 1

    start = time.time()
    for n in range(ntimes):
        np.linalg.solve(A, b)

    time_cost[i, 0] = (time.time() - start) / ntimes

    start = time.time()
    for n in range(ntimes):
        gaussSeidel(fex2_17, np.zeros(m[i]))

    time_cost[i, 1] = (time.time() - start) / ntimes

plt.loglog(m, time_cost[:, 0], 'bo-', m, time_cost[:, 1], 'rx-')
plt.title('Speed comparison of matrix ...')
plt.legend(('linalg.solve', 'Gauss Seidel'))
plt.show()
