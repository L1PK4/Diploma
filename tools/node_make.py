from email.policy import default
import numpy as np

def nodes(X, Y, par='length'):
    res = [0]
    match par:
        case 'length':
            for i in range(1, len(X)):
                res.append(res[-1] + np.sqrt((X[i - 1] - X[i]) ** 2 + (Y[i - 1] - Y[i]) ** 2))
        case float(delta):
            for i in range(1, len(X)):
                res.append(i * delta)
        case _:
            return None
    return np.array(res)