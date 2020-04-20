import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 2  # define the function


def fp(x):
    return 2 * x  # define the derivative of the function


plt.ion()
_, ax = plt.subplots()


def square_root_2():
    x = 9  # initial point
    iter_ = 0
    while abs(x - np.sqrt(2)) > 1e-12:
        plt.cla()
        plot_basics()
        ax.set_title('iteration = {}, root = {}'.format(iter_, x))
        x = one_step(x)
        plt.pause(0.5)
        iter_ += 1

    plt.pause(0)


def plot_basics():
    # plot the axes
    x = np.arange(-10, 10, 0.1)
    ax.plot(x, f(x), 'b', linewidth=2)
    ax.plot(x, np.zeros(len(x)), 'k', linewidth=1)  # plot x axis
    # plot y axis
    y = np.arange(-20, 100, 0.1)
    ax.plot(np.zeros(len(y)), y, 'k', linewidth=1)

    # plot the square root of 2
    ax.plot(np.sqrt(2), 0, 'ro', markersize=12, linewidth=2)


def one_step(x0):
    # plot the initial guess and the slope
    slope = fp(x0)
    # intercept
    b = f(x0) - slope * x0
    ax.plot(x0, f(x0), 'ko', markersize=10, markerfacecolor='k')
    plt.pause(0.5)
    # new x point
    x1 = x0 - f(x0) / fp(x0)
    # plot the tangent line
    if x0 < x1:
        x = np.arange(x0 - 0.5, x1 + 0.5, 0.1)
    else:
        x = np.arange(x1 - 0.5, x0 + 0.5, 0.1)
    ax.plot(x, slope * x + b, 'r')
    plt.pause(0.5)
    y = np.arange(0, f(x1), 0.1)
    x = np.ones(len(y)) * x1
    ax.plot(x, y, 'm--')
    ax.plot(x1, f(x1), 'mo', markersize=8, markerfacecolor='m')
    return x1


if __name__ == '__main__':
    square_root_2()
