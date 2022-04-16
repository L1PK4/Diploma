import pickle

with open('data/data.pickle', 'rb') as f:
    data = pickle.load(f)

with open('data/data.csv', 'wt') as f:
    print(data, file=f)

