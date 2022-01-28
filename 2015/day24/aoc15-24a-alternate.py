# AoC 2015 Day 24a

from functools import reduce
import itertools

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.readlines()]

def rec_srch(packs, g1, g2, g3, found):
    if packs == []:
        if sum(g1) == sum(g2) == sum(g3):
            if rec_srch.maxlen > len(g1):
                rec_srch.maxlen = len(g1)
            if g1 not in found: found.append(g1)
            yield g1
    else:
        if len(g1) <= rec_srch.maxlen:
            if g1 not in found:
                currnum = packs[0]
                yield from rec_srch(packs[1:], g1 + [currnum], g2, g3, found)
                yield from rec_srch(packs[1:], g1, g2 + [currnum], g3, found)
                yield from rec_srch(packs[1:], g1, g2, g3 + [currnum], found)

def main():
    packs = load_data()
    rec_srch.maxlen = 10
    #packs = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    for x in rec_srch(packs, [], [], [], []):
        print(x)

if __name__ == '__main__':
    main()
