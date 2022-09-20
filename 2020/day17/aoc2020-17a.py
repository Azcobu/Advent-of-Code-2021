# AoC 2020 Day 17a

from itertools import product

def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for rownum, line in enumerate(d):
        for colnum, char in enumerate(line):
            if char == '#':
                grid.add((colnum, rownum, 0))
    return grid

def count_neighbours(grid, cube):
    count = 0
    for offset in product([-1, 0, 1], repeat=3):
        if offset != (0, 0, 0):
            if (cube[0] + offset[0], cube[1] + offset[1], cube[2] + offset[2]) in grid:
                count += 1
    return count

def count_active(grid, cycles):
    gridstart = 0
    gridsize = max(x[0] for x in grid)

    for tick in range(cycles):
        newgrid = set()

        for cube in product(range(gridstart - 1, gridsize + 2), repeat=3):
            if cube in grid and count_neighbours(grid, cube) in [2, 3]:
                newgrid.add(cube)
            if cube not in grid and count_neighbours(grid, cube) == 3:
                newgrid.add(cube)
        
        grid = newgrid
        gridstart -= 1
        gridsize += 1
    
    return len(grid)

def main():
    print(count_active(load_data(), 6))

if __name__ == '__main__':
    main()
