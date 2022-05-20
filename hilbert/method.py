from scipy import interpolate
import numpy as np
from itertools import starmap
from numpy.linalg import solve as m_solve
from tools.node_make import nodes

# def make_matrix(x, y):
#     n = len(x)
#     g = np.array([[ sum(list(map(lambda xk : xk ** (i + j), x))) for i in range(n)] for j in range(n)])
#     d = np.array([sum(list(starmap(lambda xk, yk : yk * (xk ** i), zip(x,y) ))) for i in range(n)])
#     return g, d



# def solve(t, Y):
#     # G, d = make_matrix(t, Y)
#     # m = m_solve(G, d)
#     return m

def get_approx(X, Y, delta=0.001):
    lamb = nodes(X, Y)
    Xc = interpolate.interp1d(lamb, X)
    Yc = interpolate.interp1d(lamb, Y)
    t = 0
    x = []
    y = []
    n = len(X)
    while t < 2 * np.pi:
        x.append(Xc(t))
        y.append(Yc(t))
        t += delta
    return x, y
