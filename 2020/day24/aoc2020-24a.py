# AoC 2020 - Day 24a
from collections import defaultdict

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().splitlines()

def parse(data):
    grid = defaultdict(bool)

    for line in data:
        q, r = 0, 0
        while line:
            if line[0] == 'e':
                q += 1
            elif line[0] == 'w':
                q -= 1
            elif line[:2] == 'se':
                r -= 1
            elif line[:2] == 'sw':
                q -= 1
                r -= 1
            elif line[:2] == 'ne':
                q += 1
                r += 1
            elif line[:2] == 'nw':
                r += 1
            line = line[1:] if line[0] in ['e', 'w'] else line[2:]
        grid[q, r] = not grid[q, r]

    return sum(1 for k, v in grid.items() if v)

def main():
    print(parse(load_data()))

if __name__ == '__main__':
    main()
