# AoC 2018 - Day 3n
from collections import defaultdict
from parse import parse

def load_data(): #9 @ 445,84: 22x24
    with open('input.txt', 'r') as infile:
        claims = {}
        indata = [x.strip() for x in infile]
        for line in indata:
            parsestr = '#{} @ {},{}: {}x{}'
            id, left, top, width, height = parse(parsestr, line)
            claims[int(id)] = [int(left), int(top), int(width), int(height)]
    return claims

def find_non_overlap(data):
    claims = set(data.keys())
    fabric = defaultdict(list)

    for k, v in data.items():
        left, top, width, height = v
        for x in range(left, left + width):
            for y in range(top, top + height):
                fabric[(x, y)].append(k)
    
    for k, v in fabric.items():
        if len(v) > 1:
            for claim in v:
                claims.discard(claim)

    return claims

def main():
    d = load_data()
    print(find_non_overlap(d))

if __name__ == '__main__':
    main()
