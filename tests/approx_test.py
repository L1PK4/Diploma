import sys
sys.path.append("D:/programming/python/Diploma")


from tools.decartes import convert
from tools.divide import divide_by_der2 as divide
from tools.node_make import nodes

"ideal_data/ideal_data.csv"
with open("data/data.csv", "rt") as f:
    data = list(map(lambda x : list(map(float, x.strip('\n').split(', '))), f.readlines()))

"""
data = [
    [phi0, r0],
    [phi1, r1], 
    . . .
    [phin, rn]
]
"""
div, indexes = divide(data, thrashold=30)

segments = []
last_i = 0
print(div)

import matplotlib.pyplot as plt
from hilbert.method import get_approx

fig, ax = plt.subplots()
ax.plot(*convert(*list(zip(*div))), 'ro')
ax.grid(True)

for i in indexes:
    print(f'{last_i=}  {i=}\n')
    segments.append(data[last_i : i])
    last_i = i
    seg = segments[-1]
    print(f'{seg=}\n')
    X, Y = convert(*list(zip(*seg)))

    X, Y = get_approx(X, Y)
    ax.plot(X, Y)

plt.show()