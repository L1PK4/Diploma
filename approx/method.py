import numpy as np
from tools.node_make import nodes

def get_approx(X, Y, delta=0.001):
    lamb = nodes(X, Y)
    z = np.polyfit(lamb, X, 3)
    pX = np.poly1d(z)
    z = np.polyfit(lamb, Y, 3)
    pY = np.poly1d(z)
    t = lamb[0]
    x = []
    y = []
    n = len(X)
    while t < lamb[-1]:
        x.append(pX(t))
        y.append(pY(t))
        t += delta
    return x, y
