# generate an N-dimensional random vector having the uniform distribution over [a, b]
import numpy as np
import matplotlib.pyplot as plt


def randu(N, a, b):
    if a == b:
        raise ValueError('a should no be equal to b!')
    elif a > b:
        a, b = b, a

    res = a + (b - a) * np.random.rand(N)
    plt.hist(res, bins=20)
    plt.show()
    return res


if __name__ == '__main__':
    randu(1000, -2, 2)
