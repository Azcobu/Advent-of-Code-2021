# AoC 2023 Day 11a
from itertools import combinations

def load_data():
    grid = set()
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, line in enumerate(infile.readlines()):
            for colnum, char in enumerate(line):
                if char == '#':
                    grid.add((colnum, rownum))
    return grid

def main():
    grid = load_data()
    newgrid = set()
    rowgaps = set(range(max([x[1] for x in grid]))) - {x[1] for x in grid}
    colgaps = set(range(max([x[0] for x in grid]))) - {x[0] for x in grid}

    for s in grid:
        gaps_y = sum(999999 for r in rowgaps if r < s[1])
        gaps_x = sum(999999 for c in colgaps if c < s[0])
        newgrid.add((s[0] + gaps_x, s[1] + gaps_y))

    total = sum([abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(newgrid, 2)])
    print(total)

if __name__ == '__main__':
    main()
