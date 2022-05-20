DELTA = 0.04
from numpy import pi, sin, cos

with open("ideal_data/ideal_data.csv", 'wt') as f:
    theta = pi / 4
    while theta < 9 * pi / 4:
        if 3 * pi / 4 > theta > pi /4:
            print(f"{theta}, {1 / sin(theta)}", file=f)
        elif 5 * pi / 4 > theta > 3 * pi /4:
            print(f"{theta}, {1 / sin(theta - pi / 2)}", file=f)
        elif 7 * pi / 4 > theta > 5 * pi /4:
            print(f"{theta}, {1 / cos(theta + pi / 2)}", file=f)
        elif 9 * pi / 4 > theta > 7 * pi /4:
            print(f"{theta}, {1 / cos(theta)}", file=f)
        # print(f"{theta}, 3", file=f)
        theta += DELTA
        
