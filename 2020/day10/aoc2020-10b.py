# AoC 2020 Day 10b
from collections import defaultdict

def load_data():
    with open('input.txt', 'r') as infile:
        return sorted([int(x) for x in infile.read().splitlines()])

def find_paths(adaptors):
    paths = defaultdict(int, {0 : 1})

    for adapt in adaptors:
        paths[adapt] = paths[adapt - 1]  + paths[adapt - 2] + paths[adapt - 3]
    print(paths[adaptors[-1]])

def main():
    find_paths(load_data())

if __name__ == '__main__':
    main()
