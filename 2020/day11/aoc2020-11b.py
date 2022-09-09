# AoC 2020 Day 11b

def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        d = infile.read()
    for linenum, line in enumerate(d.split('\n')):
        for colnum, char in enumerate(line):
            if char == 'L':
                grid[(colnum, linenum)] = 'L'
    return grid

def extend_line(grid, linedir, max_coords, pos):
    while True:
        pos = pos[0] + linedir[0], pos[1] + linedir[1]
        if 0 <= pos[0] <= max_coords[0] and 0 <= pos[1] <= max_coords[1]:
            if pos in grid:
                return 1 if grid[pos] == '#' else 0
        else:
            return 0

def visible_neighbours(grid, max_coords, pos):
    found = 0
    for linedir in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        found += extend_line(grid, linedir, max_coords, pos)
    return found

def find_occupied(grid):
    prevstates = []
    max_coords = (max([x[0] for x in grid.keys()]), max([y[1] for y in grid.keys()]))

    while grid not in prevstates:
        prevstates.append(grid)
        newgrid = {}

        for k, v in grid.items():
            if v == 'L':
                newgrid[k] = '#' if not visible_neighbours(grid, max_coords, k) else 'L'
            elif v == '#':
                newgrid[k] = 'L' if visible_neighbours(grid, max_coords, k) >= 5 else '#'
        grid = newgrid
    
    return sum([1 for x in grid.values() if x == '#'])

def main():
    print(find_occupied(load_data()))

if __name__ == '__main__':
    main()
