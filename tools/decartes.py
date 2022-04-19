
from math import cos, sin


def convert(PHI, RO):
    X = []
    Y = []
    for phi, ro in zip(PHI, RO):
        X.append(ro * cos(phi))
        Y.append(ro * sin(phi))
    return X, Y