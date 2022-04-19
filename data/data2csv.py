import pickle
import math

with open('data/data.pickle', 'rb') as f:
    data = pickle.load(f)

with open('data/data.csv', 'wt') as f:
    d1 = data[10]
    for i in zip(*d1):
        print(i[0] * 2 * math.pi / 360, ',', i[1], file=f)

