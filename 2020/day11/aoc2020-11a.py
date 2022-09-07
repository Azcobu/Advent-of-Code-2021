# AoC 2020 Day 11a

def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        d = infile.read()
    for linenum, line in enumerate(d.split('\n')):
        for colnum, char in enumerate(line):
            if char == 'L':
                grid[(colnum, linenum)] = 'L'
    return grid

def neighbours(grid, coords):
    found = 0
    for offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        n_x, n_y = coords[0] + offset[0], coords[1] + offset[1]
        if (n_x, n_y) in grid and grid[(n_x, n_y)] == '#':
            found += 1
    return found

def find_occupied(grid):
    prevstates = []
    
    while grid not in prevstates:
        prevstates.append(grid)
        newgrid = {}

        for k, v in grid.items():
            if v == 'L':
                newgrid[k] = '#' if not neighbours(grid, k) else 'L'
            elif v == '#':
                newgrid[k] = 'L' if neighbours(grid, k) >= 4 else '#'
        grid = newgrid
    
    return sum([1 for x in grid.values() if x == '#'])

def main():
    print(find_occupied(load_data()))

if __name__ == '__main__':
    main()
