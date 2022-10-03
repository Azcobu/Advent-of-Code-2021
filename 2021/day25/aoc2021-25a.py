# AoC 2021 - Day 25a

def load_data():
    grid = {}
    with open('example.txt', 'r') as infile:
        d = infile.read().splitlines()
    for linenum, line in enumerate(d):
        for colnum, char in enumerate(line):
            if char != '.':
                grid[(colnum, linenum)] = char
    return grid

def print_grid(grid, width, height):
    for y in range(height):
        k = ''.join([grid[(x, y)] if (x, y) in grid else '.' for x in range(width)])
        print(k)
    print('\n\n')

def find_halt(grid):
    gridwidth = max(x[0] for x in grid.keys()) + 1
    gridheight = max(x[1] for x in grid.keys()) + 1
    steps = 0

    while True:
        newgrid = grid.copy()

        for unittype in ['>', 'v']:
            for pos, unit in grid.items():
                if unit == unittype:
                    if unittype == '>':
                        movepos = ((pos[0] + 1) % gridwidth, pos[1])
                    else:
                        movepos = (pos[0], (pos[1] + 1) % gridheight)
                    if movepos not in grid:
                        newgrid[movepos] = unittype
                        del newgrid[pos]
        steps += 1
        print_grid(grid, gridheight, gridwidth)
        if grid != newgrid:
            grid = newgrid
            print(steps)
        else:
            return steps

def main():
    print(find_halt(load_data()))

if __name__ == '__main__':
    main()
