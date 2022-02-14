# AoC 2016 - Day 8a
import re

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for d in data:
        if d.startswith('rect'):
            m = re.search(r'rect (\d+)x(\d+)', d)
            i_type = 'r'
        else:
            m = re.search(r'(\d+) by (\d+)', d)
            i_type = 'x' if 'x' in d else 'y'
        instrs.append([i_type, int(m.group(1)), int(m.group(2))])
    return instrs

def rotate_col(grid, instr):
    mode, pos, offset = instr

    found = set(filter(lambda x: x[0] == pos, grid))
    newnodes = set([(n[0], (n[1] + offset) % 6) for n in found])
    return (grid - found) | newnodes

def rotate_row():
    pass

def parse_instrs(instrs):
    grid = set()
    for i in instrs:
        if i[0] == 'r':
            for y in range(i[2]):
                for x in range(i[1]):
                    grid.add((x, y))
        elif i[0] == 'x':
            grid = rotate_col(grid, i)

    return grid

def print_grid(grid):
    for x in range(6):
        for y in range(50):
            out = '#' if (x, y) in grid else '.'
            print(out, end='')
        print('')

def main():
    #print(load_data())
    grid = parse_instrs([('r', 3, 2), ('x', 1, 1)])
    print_grid(grid)
    print(grid)

if __name__ == '__main__':
    main()
