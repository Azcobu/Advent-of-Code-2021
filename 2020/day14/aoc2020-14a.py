# AoC 2020 Day 14b
from parse import parse

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    return d

def calc_vals(data):
    mem = {}
    parsestr = 'mem[{}] = {}'

    for line in data:
        if 'mask = ' in line:
            mask = line[7:]
        else:
            addr, val = parse(parsestr, line)
            val = f'{int(val):036b}'
            newval = ''.join([y if y != 'X' else x for x, y in zip(val, mask)])
            mem[addr] = int(newval, 2)
    return sum(mem.values())

def main():
    d = load_data()
    print(calc_vals(d))

if __name__ == '__main__':
    main()
