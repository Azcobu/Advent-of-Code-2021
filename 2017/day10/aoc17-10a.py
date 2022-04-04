# AoC 2017 - Day 10a
from collections import deque

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.read().split(',')]

def knothash(listsize, lens):
    k = deque(range(listsize), listsize)
    currpos = 0
    for strlen in lens:
        k[currpos:currpos+strlen] = k[currpos:currpos+strlen][::-1]
        print(k)

def main():
    print(load_data())
    print(knothash(5, [3, 4, 1, 5]))

if __name__ == '__main__':
    main()
