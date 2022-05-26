import argparse as ap

parser = ap.ArgumentParser(description="Lidar data approximation")
parser.add_argument('--data_type', '-dt', choices=['ideal', 'real'], default='real', help='Choose type of input data')
parser.add_argument('--degree', '-d', type=int, default=1, help='Polynomial degree')
parser.add_argument('--full', '-f', action='store_true', help='Show full information')
parser.add_argument('--parameter', '-p', choices=['lambda', 'phi'], default='lambda',help='Parameter of approximation')

args = parser.parse_args()

def main(args):
    if args.data_type == 'ideal':
        path = "ideal_data/ideal_data.csv"
        import ideal_data.create
    elif args.data_type == 'real':
        path = "data/data.csv"
        import data.data2csv
    with open(path, "rt") as f:
        data = list(map(lambda x : list(map(float, x.strip('\n').split(', '))), f.readlines()))
    
    from tools.decartes import convert
    from tools.divide import divide_by_der2 as divide
    from tools.node_make import nodes
    if args.parameter == 'lambda':
        from approx.method import get_approx_lamb as approx
    elif args.parameter == 'phi':
        from approx.method import get_approx_phi as approx
    import numpy as np
    import matplotlib.pyplot as plt

    if args.full:
        import time
        start = time.time()
    
    div, indexes = divide(data)
    if args.full:
        end = time.time()
        print(f"Time for dividion: {end - start}")

    segments = []
    last_i = 0
    fig, ax = plt.subplots()
    ax.plot(*convert(*list(zip(*div))), 'ro')
    ax.plot(*convert(*list(zip(*data))), linestyle='dashed')
    ax.grid(True)
    n = 1
    RES = []
    for i in indexes:
        segments.append(data[last_i : i])
        last_i = i
        seg = segments[-1]
        # ax.plot(X, Y)
        if args.full:
            start = time.time()
        X, Y, *c, res = approx(list(zip(*seg)), deg=args.degree)
        if args.full:
            end = time.time()
            if args.parameter == 'lambda':
                print("-" * 30 + str(n) + "-" * 30 + f"\nTime for approximation: {end - start}\n\nmean res:{np.mean(res)}\n\nX coef:{c[0]}\n\nY coef:{c[1]}\n")
            if args.parameter == 'phi':
                print("-" * 30 + str(n) + "-" * 30 + f"\nTime for approximation: {end - start}\n\nmean res:{np.mean(res)}\n\ncoef:{c[0]}\n")
        RES.extend(res)
        n += 1

        ax.plot(X, Y)
    with open(f'res/{args.parameter}_d{args.degree}.txt', 'wt') as f:
        f.write(str(np.mean(RES)))
    plt.show()


if __name__ == '__main__':
    main(args)