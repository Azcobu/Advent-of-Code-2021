# AoC 2017 - Day 2b
from itertools import combinations

def load_data():
    with open('input.txt', 'r') as infile:
        return [[int(x) for x in line.split()] for line in infile.readlines()]

def calc_checksum(indata):
    return sum([y//x for line in indata for x, y in combinations(sorted(line), 2) if y % x == 0])

def main():
    print(calc_checksum(load_data()))

if __name__ == '__main__':
    main()
