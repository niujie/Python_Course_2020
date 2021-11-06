"""
calculate the average distance of two random points in a unit circle
"""

import numpy as np
import matplotlib.pyplot as plt


def draw(X=None, Y=None):
    theta = np.arange(0, 2*np.pi, 0.01)
    r = 1.0
    plt.plot(np.cos(theta)*r, np.sin(theta)*r)
    plt.axis('equal')
    plt.plot(X, Y, '.', markersize=1)
    plt.show()


def generate_random_points(N=100):
    theta = np.random.rand(N) * 2 * np.pi
    r = np.random.rand(N)
    # use square root for the correct distribution
    # otherwise the generated points tend to be gathered
    # in the center of the disc
    r = np.sqrt(r)
    return np.cos(theta)*r, np.sin(theta)*r


def generate_random_points_reject(N=100):
    X = []
    Y = []
    i = 0
    while i < N:
        x = np.random.rand() * 2 - 1
        y = np.random.rand() * 2 - 1
        if x*x + y*y <= 1.0:
            X.append(x)
            Y.append(y)
            i += 1
    return np.array(X), np.array(Y)


def cal_avg_dist(X, Y):
    N = len(X)
    dist = 0
    n = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist += np.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2)
            n += 1
    return dist / n


if __name__ == '__main__':
    X, Y = generate_random_points(1000)
    print("True avg dist: " + "{:.4f}".format(128/45/np.pi))
    print("N = " + str(len(X)) + ", calculated avg dist: " +
          "{:.4f}".format(cal_avg_dist(X, Y)))
    draw(X, Y)
