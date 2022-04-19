import numpy as np

def divide_by_der2(data, thrashold = 1e-1):
    turns = []
    for i in range(1, len(data) - 1):
        d2 = (data[i - 1][1] - 2 * data[i][1] + data[i + 1][1]) / (data[i - 1][0] - data[i][0]) ** 2

        if np.abs(d2) > thrashold:
            print(d2)
            turns.append(data[i])
    return turns