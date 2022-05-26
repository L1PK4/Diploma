import numpy as np
from tools.node_make import nodes
from tools.decartes import convert

def get_approx_phi(seg, deg=1):
    PHI, R = seg
    cR = np.polyfit(PHI, R, deg)
    pR = np.poly1d(cR)
    r = []
    res = []
    for i, t in enumerate(PHI):
        r.append(pR(t))
        res.append(np.abs(r[i] - R[i]))
    x, y = convert(PHI, r)
    return x, y, cR, res


def get_approx_lamb(seg, par='length', deg=1):
    X, Y = convert(*seg)
    lamb = nodes(X, Y, par=par)
    cX = np.polyfit(lamb, X, deg)
    pX = np.poly1d(cX)
    cY = np.polyfit(lamb, Y, deg)
    pY = np.poly1d(cY)
    x = []
    y = []
    res = []
    for i, t in enumerate(lamb):
        x.append(pX(t))
        y.append(pY(t))
        res.append(np.sqrt((x[i] - X[i]) ** 2 + (y[i] - Y[i]) ** 2))
    
    return x, y, cX, cY, res
