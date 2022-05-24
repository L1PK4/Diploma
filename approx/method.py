from argparse import Namespace
import numpy as np
from tools.node_make import nodes


def get_approx(X, Y, par='length', deg=1):
    lamb = nodes(X, Y, par=par)
    cX = np.polyfit(lamb, X, deg)
    pX = np.poly1d(cX)
    cY = np.polyfit(lamb, Y, deg)
    pY = np.poly1d(cY)
    t = lamb[0]
    x = []
    y = []
    res = []
    for i, t in enumerate(lamb):
        x.append(pX(t))
        y.append(pY(t))
        res.append(np.sqrt((x[i] - X[i]) ** 2 + (y[i] - Y[i]) ** 2))
    
    return x, y, cX, cY, res
