import numpy as np

def divide_by_der2(data, thrashold = 3e1):
    turns = []
    indexes = []
    for i in range(1, len(data) - 1):
        d2 = (data[i - 1][1] - 2 * data[i][1] + data[i + 1][1]) / (data[i - 1][0] - data[i][0]) ** 2

        if np.abs(d2) > thrashold:
            if not turns or not i - indexes[-1] < 2:
                turns.append(data[i])
                indexes.append(i)
    turns.append(data[-1])
    indexes.append(len(data) - 1)
    return turns, indexes