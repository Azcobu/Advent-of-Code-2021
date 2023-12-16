# AoC 2023 Day 8a
from math import lcm

def load_data():
    nodes = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        data = infile.readlines()
    path = data[0].strip()
    for line in data[2:]:
        n, _, m = line.partition(' = ')
        nodes[n] = (m[1:4], m[6:9])
    return path, nodes

def main():
    curr = 'AAA'
    path, nodes = load_data()
    pathcounts = []

    a_nodes = {x for x in nodes if x[2] == 'A'}
    z_nodes = {x for x in nodes if x[2] == 'Z'}

    for curr in a_nodes:
        steps = 0
        while curr not in z_nodes:
            for p in path:
                curr = nodes[curr][0] if p == 'L' else nodes[curr][1]
                steps += 1
        pathcounts.append(steps)

    print(lcm(*pathcounts))

if __name__ == '__main__':
    main()
