# speed comparison of matrix multiplication between loop and numpy .dot
import numpy as np
import time


def speed_test():
    N = 5  # number of matrices
    m = np.round(np.logspace(2, 4, N))  # matrix size
    ntimes = 3  # number of tests
    time_cost = np.zeros(N, ntimes)

    for i in range(N):
        A = np.random.rand(m[i])
        B = np.random.rand(m[i])

        start_time = time.time()
        for n in range(ntimes):
            matrix_multiplication_row(A, B)

        time_cost[i][0] = (time.time() - start_time) / ntimes

        start_time = time.time()
        for n in range(ntimes):
            matrix_multiplication_col(A, B)

        time_cost[i][1] = (time.time() - start_time) / ntimes

        start_time = time.time()
        for n in range(ntimes):
            A.dot(B)

        time_cost[i][2] = (time.time() - start_time) / ntimes
