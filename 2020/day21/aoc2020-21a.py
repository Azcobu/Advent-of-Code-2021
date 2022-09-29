# AoC 2020 Day 21a
from parse import parse
from collections import defaultdict

def load_data():
    ingreds, allergdict = [], defaultdict(list)
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        ingred, allerg = parse('{} (contains {})', line)
        ingreds += ingred.split()
        for a in allerg.split(','):
            allergdict[a.strip()].append(set(ingred.split()))
    return allergdict, ingreds

def count_non_allergens(allergdict, ingredlist):
    total, found = 0, set()
    for allerg, ingreds in allergdict.items():
        found |= set.intersection(*ingreds)
    return len([x for x in ingredlist if x not in found])

def main():
    print(count_non_allergens(*load_data()))

if __name__ == '__main__':
    main()
