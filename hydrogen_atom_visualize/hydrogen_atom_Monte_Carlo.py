import warnings
from math import factorial
import numpy as np
from pyshtools.legendre import PLegendreA, PlmIndex
from tqdm import tqdm
import matplotlib.pyplot as plt

a0 = 0.52917721067  # Bohr radius, in Ångstrom


def rAbs(r):
    return np.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2)


def thetaVal(r):
    return np.arccos(r[2] / np.sqrt(np.sum(r ** 2)))


def fillVector(dx, dy, dz):
    r = np.random.rand(3)
    r[0] = dx * (r[0] - 0.5)
    r[1] = dy * (r[1] - 0.5)
    r[2] = dz * (r[2] - 0.5)
    return r


def radDF(n, l, r):
    """
    radial part
    :param n: radial quantum number
    :param l: azimuthal quantum number
    :param r: radius
    :return: result of the radial part
    """
    Z = 1  # atomic number, 1 for hydrogen atom
    r0 = 2.0 * Z / (n * a0) * r
    s = 0  # sum
    terms = np.zeros(6)

    for k in range(0, n - l):
        # from 0 to n-l-1
        terms[0] = (-1.0) ** (k + 1)
        terms[1] = factorial(n + l) ** 2.0
        terms[2] = factorial(n - l - 1 - k)
        terms[3] = factorial(2 * l + 1 + k)
        terms[4] = factorial(k)
        terms[5] = r0 ** k
        s += terms[0] * terms[1] / (terms[2] * terms[3] * terms[4]) * terms[5]

    terms[:] = 0.0
    terms[0] = (2.0 * Z / (n * a0)) ** 3.0
    terms[1] = factorial(n - l - 1)
    terms[2] = 2.0 * n
    terms[3] = factorial(n + l) ** 3.0

    normTermSquared = terms[0] * terms[1] / (terms[2] * terms[3])

    radialTerm = np.exp(-r0 / 2.0) * (r0 ** l)

    radDF = (s * radialTerm) ** 2.0
    radDF = radDF * normTermSquared
    return radDF


def angDF(l, m, theta):
    """
    angular part
    :param l: azimuthal quantum number
    :param m: magnetic quantum number
    :param theta: polar angle
    :return: result of the angular part
    """
    z = np.cos(theta)
    p = PLegendreA(l, z)
    arrayIndex = PlmIndex(l, m)

    normRoot = 1.0 * factorial(l - m) / factorial(l + m)
    normRoot = normRoot * (2.0 * l + 1.0) / (4.0 * np.pi)

    angDF = normRoot * p[arrayIndex] ** 2.0

    return angDF


def wave2max(coordRange, nlm, rDiv, thetaDiv):
    """
    upper limit of the wave function squared
    :param coordRange: box dimension
    :param nlm:        n, l, and m
    :param rDiv:       number of division in r
    :param thetaDiv:   number of division in theta
    :return: the upper limit of the waver function squared
    """

    rMax = np.sqrt(np.sum(coordRange ** 2))

    dr = rMax / (1.0 * rDiv)
    dTheta = np.pi / (1.0 * thetaDiv)
    maxValue = 0.0

    curr = np.zeros(2)
    for i in range(rDiv):
        r = i * dr
        for j in range(thetaDiv):
            theta = j * dTheta
            curr[0] = angDF(nlm[1], nlm[2], theta)
            curr[1] = radDF(nlm[0], nlm[1], r)
            calc = curr[0] * curr[1]

            if calc > maxValue:
                maxValue = calc

    return maxValue


if __name__ == '__main__':
    n, l, m = 6, 3, 1  # radial, azimuthal, and magnetic quantum numbers
    dx, dy, dz = 90.0, 0.0, 90.0  # box dimension
    dr, dTheta = 2.0, 0.04  # incremental spacing for r and theta
    icr = 1.05  # 5% increment
    points = 15000  # total number of points

    rDiv = int(rAbs(np.array([dx, dy, dz])) / dr) + 1  # number of divisions in r
    thetaDiv = int(2.0 * np.pi / dTheta) + 1  # number of divisions in theta
    maxVal = wave2max(np.array([dx, dy, dz]), np.array([n, l, m]), rDiv, thetaDiv)

    i = 0
    X = np.zeros(points)
    Y = np.zeros(points)
    Z = np.zeros(points)
    W = np.zeros(points)
    pBar = tqdm(total=points)
    while i < points:
        w = np.random.rand() * maxVal * icr
        rVector = fillVector(dx, dy, dz)
        r = rAbs(rVector)
        theta = thetaVal(rVector)
        psi2 = radDF(n, l, r) * angDF(l, m, theta)
        if w < psi2:
            X[i], Y[i], Z[i], W[i] = rVector[0], rVector[1], rVector[2], w
            i += 1
            pBar.update(1)

    plt.figure(figsize=(12, 8))
    plt.scatter(X, Z, s=0.1)
    plt.axis('square')
    plt.xlim((-dx/2, dx/2))
    plt.ylim((-dz/2, dz/2))
    plt.xlabel('x ($\AA$)')
    plt.ylabel('z ($\AA$)')
    plt.show()
