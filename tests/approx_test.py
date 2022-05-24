import sys
sys.path.append("D:/programming/python/Diploma")


from tools.decartes import convert
from tools.divide import divide_by_der2 as divide
from tools.node_make import nodes
import numpy as np

import time

# Принцип максимума Лагранджа
# Оптимальная параметризация -параметризация натуральным пар-ом
# ВВ: помимо классичских опт задач (сост ур-я движ мех сист принц мин действ лагр) могут быть ещё и не класс постановки, св с этой задачей
# закл: в рез-те пров числ эксп доказано что наил пар-ей для этой задачи явл натур пар-ция контура которая механически соотв движ мат точки по этому контуру
# без действия акт сил и силы трения. При этом Лагранжиан совп с кин. энергией а ур-е движение сост по принц макс лагр интегрируются и в рез-те пол-ся движ с пост по модулю скорости

"ideal_data/data.csv"
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
start = time.time()
div, indexes = divide(data)
end = time.time()
print(f"Time for dividion: {end - start}")

segments = []
last_i = 0

import matplotlib.pyplot as plt
from approx.method import get_approx

fig, ax = plt.subplots()
ax.plot(*convert(*list(zip(*div))), 'ro')
ax.grid(True)

n = 1
for i in indexes:
    # print(f'{last_i=}  {i=}\n')
    segments.append(data[last_i : i])
    last_i = i
    seg = segments[-1]
    # print(f'{seg=}\n')
    X, Y = convert(*list(zip(*seg)))
    ax.plot(X, Y)
    start = time.time()
    X, Y, *c, res = get_approx(X, Y)
    end = time.time()
    print("-" * 30 + str(n) + "-" * 30 + f"\nTime for approximation: {end - start}\n\nmean res:{np.mean(res)}\n\ncoef:{c}\n")
    n += 1

    ax.plot(X, Y, linestyle='dashed')

plt.show()