# AoC 2015 Day 24a

from functools import reduce
import itertools

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.readlines()]

def itersrch(packs, divs):
    target = sum(packs) // divs
    for num in range(1, len(packs)):
        poss = [x for x in itertools.combinations(packs, num) if sum(x) == target]
        if poss != []: return sorted([reduce(lambda x, y: x*y, x) for x in poss])[0]

def main():
    packs = load_data()
    print(itersrch(packs, 4))

if __name__ == '__main__':
    main()
