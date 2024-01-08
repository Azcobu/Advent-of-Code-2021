# AoC 2023 Day 13a

def load_data():
    grids = []
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for grid in infile.read().split('\n\n'):
            grids.append(grid.split('\n'))
    return grids

def find_mirror(grid):
    for rownum, row in enumerate(grid[:-1]):
        if row == grid[rownum+1]:
            checksteps = min(rownum - 0, len(grid) - rownum - 2)
            for x in range(1, checksteps + 1):
                if grid[rownum - x] != grid[rownum + 1 + x]:
                    break
            else:
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
