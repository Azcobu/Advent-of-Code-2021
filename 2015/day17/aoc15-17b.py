# AoC 2015 - Day 17a
from itertools import combinations

def load_data():
    with open('input.txt', 'r') as infile:
        data = [int(line) for line in infile]
    return data

def find_combinations(data, target):
    found = []
    for num in range(len(data)+1):
        found += [x for x in combinations(data, num) if sum(x) == target]
    contnums = [len(x) for x in found]
    return contnums.count(min(contnums))

def main():
    target = 150
    data = load_data()
    print(find_combinations(data, target))

if __name__ == '__main__':
    main()
