import sys
sys.path.append("D:/programming/python/Diploma")


from tools.decartes import convert
from tools.divide import divide_by_der2 as divide
from tools.node_make import nodes

"ideal_data/ideal_data.csv"
with open("data/data.csv", "rt") as f:
    data = list(map(lambda x : list(map(float, x.strip('\n').split(', '))), f.readlines()))

div, _ = divide(data, thrashold=30)
print(div)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(*list(zip(*data)))
ax.plot(*list(zip(*div)), 'ro')
ax.set_rmax(5)
ax.grid(True)

plt.show()