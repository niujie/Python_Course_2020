# speed comparison of matrix multiplication between loop and numpy .dot
import numpy as np
import matplotlib.pyplot as plt
import time


def matrix_multiplication_row(A_, B_):
    # matrix multiplication row major
    if np.size(A_, 1) != np.size(B_, 0):
        raise ValueError('A can not be multiplied by B!')

    M = np.size(A_, 0)
    K, N = np.size(B_, 0), np.size(B_, 1)
    C_ = np.zeros((M, N))

    for m in range(M):
        for n in range(N):
            for k in range(K):
                C_[m][n] += A_[m][k] * B_[k][n]

    return C_


def matrix_multiplication_col(A_, B_):
    # matrix multiplication column major
    if np.size(A_, 1) != np.size(B_, 0):
        raise ValueError('A can not be multiplied by B!')

    M = np.size(A_, 0)
    K, N = np.size(B_, 0), np.size(B_, 1)
    C_ = np.zeros((M, N))

    for n in range(N):
        for m in range(M):
            for k in range(K):
                C_[m][n] += A_[m][k] * B_[k][n]

    return C_


def speed_test():
    N = 10  # number of matrices
    m = np.round(np.logspace(1, 2.5, N)).astype(np.int)  # matrix size
    ntimes = 3  # number of tests
    time_cost = np.zeros((N, ntimes))

    for i in range(N):
        A_ = np.random.rand(m[i], m[i])
        B_ = np.random.rand(m[i], m[i])

        start_time = time.time()
        for n in range(ntimes):
            matrix_multiplication_row(A_, B_)

        time_cost[i][0] = (time.time() - start_time) / ntimes

        start_time = time.time()
        for n in range(ntimes):
            matrix_multiplication_col(A_, B_)

        time_cost[i][1] = (time.time() - start_time) / ntimes

        start_time = time.time()
        for n in range(ntimes):
            A_.dot(B_)

        time_cost[i][2] = (time.time() - start_time) / ntimes

    plt.loglog(m, time_cost[:, 0], 'bo-', label='row major')
    plt.loglog(m, time_cost[:, 1], 'rx-', label='col major')
    plt.loglog(m, time_cost[:, 2], 'md-', label='.dot()')
    plt.loglog(m, time_cost[:, 0] / time_cost[:, 1], 'ks--', label='row / col')
    plt.loglog(m, time_cost[:, 0] / time_cost[:, 2], 'bo--', label='row / .dot()')
    plt.loglog(m, time_cost[:, 1] / time_cost[:, 2], 'rx--', label='col / .dot()')

    plt.title('Speed comparison of matrix multiplication')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    speed_test()
