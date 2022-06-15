# AoC 2018 Day 1b
from itertools import cycle

def load_data():
    freqs = []
    with open(r'input.txt', 'r') as infile:
        d = [x.strip() for x in infile.readlines()]
        return [int(x) if '-' in x else int(x) for x in d]

def track_freqs(d):
    freqs = set([0])
    curr_freq = 0

    for mod in cycle(d):
        curr_freq += mod
        if curr_freq in freqs:
            return curr_freq
        freqs.add(curr_freq)

def main():
    d = load_data()
    print(track_freqs(d))

if __name__ == '__main__':
    main()
