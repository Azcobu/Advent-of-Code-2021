# AoC 2016 - Day 22b
import re

def load_data():
    nodes = {}
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines() if '/dev/grid/' in x]
    for line in indata:
        x, y, size, used, free, perc = [int(x) for x in re.findall(r'\d+', line)]
        nodes[(x, y)] = size, used, free
    return nodes

def count_wallnodes(nodes):
    return sum([1 for k, v in nodes.items() if v[1] > 80])

def min_wallnode_x(nodes):
    return min([k[0] for k, v in nodes.items() if v[1] > 80])

def calc_path(nodes): # formula from u/Senoy05
    return 30 * 5 + 26 + count_wallnodes(nodes) + (24 - min_wallnode_x(nodes)) + 1

def main():
    print(calc_path(load_data()))

if __name__ == '__main__':
    main()
