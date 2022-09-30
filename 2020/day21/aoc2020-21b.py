# AoC 2020 Day 21b
from parse import parse

def load_data():
    ingreds, allergdict = set(), {}
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        ingred, allerg = parse('{} (contains {})', line)
        ingreds |= set(ingred.split())
        for a in allerg.split(','):
            if a.strip() not in allergdict:
                allergdict[a.strip()] = set(ingred.split())
            else:
                allergdict[a.strip()] &= set(ingred.split())
    return allergdict, ingreds

def gen_dangerlist(allergdict, ingredset):
    found = {}
    while len(found) < len(allergdict):
        for allerg, ingred in allergdict.items():
            if len(ingred) == 1:
                found[allerg] = list(ingred)[0]
                allergdict = {k:v - ingred for k, v in allergdict.items()}
    return ','.join([v for k, v in sorted(found.items())])

def main():
    print(gen_dangerlist(*load_data()))

if __name__ == '__main__':
    main()
