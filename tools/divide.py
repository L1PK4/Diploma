import numpy as np

# def d(a, b):
#     x1 = a[1] * np.cos(a[0])
#     y1 = a[1] * np.sin(a[0])
#     x2 = b[1] * np.cos(b[0])
#     y2 = b[1] * np.sin(b[0])
#     return np.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)

def divide_by_der2(data, thrashold = 1e-1):
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