# AoC 2015 - Day 16a

from parse import parse

def load_data():
    aunts = {}
    with open('input.txt', 'r') as infile:
        indata = [x.strip() for x in infile]
    for line in indata:
        parsestr = 'Sue {}: {}: {}, {}: {}, {}: {}'
        num, item1, item1val, item2, item2val, item3, item3val = parse(parsestr, line)
        aunts[int(num)] = {item1: int(item1val), item2:int(item2val), item3:int(item3val)}
    return aunts

def find_match(data, target):
    scores = {x:0 for x in range(1, 501)}
    for a, vals in data.items():
        for trait, traitval in target.items():
            if trait in vals and vals[trait] == traitval:
                scores[a] += 1
    return sorted(scores.items(), key=lambda x:x[1], reverse=True)[0][0]

def main():
    target = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
              'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    data = load_data()
    print(find_match(data, target))

if __name__ == '__main__':
    main()
