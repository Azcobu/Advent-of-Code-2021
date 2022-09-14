# AoC 2020 Day 14b
from parse import parse
from itertools import product

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    return d

def permute_addr(addr):
    variants = []

    for var in product('01', repeat=addr.count('X')):
        new = addr[:]
        for pos, char in enumerate(var):
            new[new.index('X')] = char
        variants.append(int(''.join(new), 2))
    return variants

def calc_vals(data):
    mem = {}
    parsestr = 'mem[{}] = {}'

    for line in data:
        if 'mask = ' in line:
            mask = line[7:]
        else:
            addr, val = parse(parsestr, line)
            addr = f'{int(addr):036b}'
            newaddr = []
            for addrbit, maskbit in zip(addr, mask):
                if maskbit == '0':
                    newaddr.append(addrbit)
                elif maskbit == '1':
                    newaddr.append('1')
                else:
                    newaddr.append('X')
            for k in permute_addr(newaddr):
                mem[k] = int(val)

    return sum(mem.values())

def main():
    d = load_data()
    print(calc_vals(d))

if __name__ == '__main__':
    main()
