# AoC 2019 Day 12a
from parse import parse

def load_data():
    vals = []
    parsestr = '<x={}, y={}, z={}>'
    with open('input.txt', 'r') as infile:
        for line in infile.read().splitlines():
            x, y, z = map(int, parse(parsestr, line))
            vals.append([x, y, z, 0, 0, 0])
    print(vals)
    return vals

def sim_moons(vals, steps):
    energy = 0

    for step in range(steps):
        for num in range(len(vals)):
            for velpos in range(0, 3):
                for n in range(len(vals)):
                    if n != num:
                        if vals[n][velpos] > vals[num][velpos]:
                            vals[num][velpos + 3] += 1
                        elif vals[n][velpos] < vals[num][velpos]:
                            vals[num][velpos + 3] -= 1

        for num in range(len(vals)):
            for velpos in range(0, 3):
                vals[num][velpos] += vals[num][velpos+3]

    for x in range(len(vals)):
        energy += sum([abs(vals[x][v]) for v in range(3)]) * sum([abs(vals[x][v]) for v in range(3, 6)])
    return energy

def main():
    print(sim_moons(load_data(), 1000))

if __name__ == '__main__':
    main()
