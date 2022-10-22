# AoC 2019 Day 12b
from parse import parse
from math import lcm
from itertools import permutations

def load_data():
    vals = []
    parsestr = '<x={}, y={}, z={}>'
    with open('input.txt', 'r') as infile:
        for line in infile.read().splitlines():
            x, y, z = map(int, parse(parsestr, line))
            vals.append([x, y, z, 0, 0, 0])
    return vals

def sim_moons(vals):
    periods = {}
    step, energy = 0, 0

    startstate = vals[:]

    while True:
        for moon1, moon2 in permutations(range(4), 2):
            for velpos in range(0, 3):
                if vals[moon1][velpos] > vals[moon2][velpos]:
                    vals[moon1][velpos + 3] -= 1
                elif vals[moon1][velpos] < vals[moon2][velpos]:
                    vals[moon1][velpos + 3] += 1

        for num in range(4):
            for velpos in range(3):
                vals[num][velpos] += vals[num][velpos + 3]

        step += 1

        for axis in range(3):
            if all([vals[moon][axis] == startstate[moon][axis] and vals[moon][axis + 3] == 0 for moon in range(4)]):
               periods[axis] = step

        if len(periods) == 3:
            break

    return lcm(*periods.values())

def main():
    print(sim_moons(load_data()))

if __name__ == '__main__':
    main()
