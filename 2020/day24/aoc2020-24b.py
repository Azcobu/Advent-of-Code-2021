# AoC 2020 - Day 24a
from collections import defaultdict

def load_data():
    with open('example.txt', 'r') as infile:
        return infile.read().splitlines()

def parse(data):
    grid = defaultdict(bool) # black = true, white = false

    for line in data:
        q, r = 0, 0
        while line:
            if line[0] == 'e':
                q += 1
            elif line[0] == 'w':
                q -= 1
            elif line[:2] == 'se':
                r -= 1
            elif line[:2] == 'sw':
                q -= 1
                r -= 1
            elif line[:2] == 'ne':
                q += 1
                r += 1
            elif line[:2] == 'nw':
                r += 1
            line = line[1:] if line[0] in ['e', 'w'] else line[2:]
        grid[q, r] = not grid[q, r]

    return grid

def iterate_grid(grid, steps):
    for step in range(steps):
        print(sum(1 for x in grid.values() if x))
        newgrid = grid.copy()
        for coords, tile in newgrid.items():
            numblack = 0
            for diff_q, diff_r in [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]:
                new_q, new_r = coords[0] + diff_q, coords[1] + diff_r
                if grid[new_q, new_r] == True:
                    numblack += 1
            if tile: # black
                if numblack == 0 or numblack > 2:
                    newgrid[coords] = False
            else:
                if numblack == 2:
                    newgrid[coords] = True
        grid = newgrid

    return sum(1 for x in grid.values() if x)
            
def main():
    g = parse(load_data())
    print(iterate_grid(g, 2))

if __name__ == '__main__':
    main()
