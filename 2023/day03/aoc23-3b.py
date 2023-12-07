# AoC 2023 Day 3a
import re
from collections import defaultdict

def load_data():
    nums = {}
    symbols = {}

    with open('input.txt', 'r', encoding='utf-8') as infile:
        grid = infile.readlines()
    for linenum, line in enumerate(grid):
        for match in re.finditer('\d+', line.strip()):
            coords = frozenset([(p, linenum) for p in range(match.start(), match.end())])
            nums[coords] = int(match.group())
        for match in re.finditer('[^0-9.]', line.strip()):
            coords = []
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    coords.append((match.start() + x_offset, linenum + y_offset))
            symbols[(match.start(), linenum)] = set(coords)
    return nums, symbols

def main():
    found = defaultdict(list)

    nums, symbols = load_data()
    for numcoords, num in nums.items():
        for sym, symcoords in symbols.items():
            if len(symcoords & numcoords) and num not in found[sym]:
                found[sym].append(num)

    print(sum([v[0] * v[1] for v in found.values() if len(v) == 2]))

if __name__ == '__main__':
    main()
