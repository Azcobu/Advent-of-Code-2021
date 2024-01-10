# AoC 2023 Day 13b

def load_data():
    grids = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for grid in infile.read().split('\n\n'):
            grids.append(grid.split('\n'))
    return grids

def find_mirror(grid):
    for rownum in range(len(grid) - 1):
        offset, diffs = 0, 0
        while rownum - offset >= 0 and rownum + 1 + offset < len(grid) and diffs < 2:
            diffs += sum([1 for x, y in zip(grid[rownum - offset], grid[rownum + 1 + offset]) if x != y])
            offset += 1
        if diffs == 1:
            return rownum + 1

def mngr(g):
    if result := find_mirror(g):
        return result * 100
    else:
        rotated = [''.join(x) for x in list(zip(*g[::-1]))]
        return find_mirror(rotated)

def main():
    print(sum(mngr(g) for g in load_data()))

if __name__ == '__main__':
    main()
