# AoC 2016 - Day 22a
import re

def load_data():
    nodes = {}
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines() if '/dev/grid/' in x]
    for line in indata:
        x, y, size, used, free, perc = [int(x) for x in re.findall(r'\d+', line)]
        nodes[(x, y)] = size, used, free
    return nodes

def find_pairs(nodes):
    found = []
    for k, v in nodes.items():
        size, used, free = v
        if used > 0:
            found.append(sum([1 for n_k, n_v in nodes.items() if k != n_k and used < n_v[2]]))
    return sum(found)

def main():
    print(find_pairs(load_data()))

if __name__ == '__main__':
    main()
