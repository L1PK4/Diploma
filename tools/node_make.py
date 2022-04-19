import numpy as np

def nodes(X, Y):
    res = [0]
    for i in range(1, len(X)):
        res.append(res[-1] + np.sqrt((X[i - 1] - X[i]) ** 2 + (Y[i - 1] - Y[i]) ** 2))
    return np.array(res)