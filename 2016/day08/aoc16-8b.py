# AoC 2016 - Day 8b
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

def rotate(grid, instr):
    mode, pos, offset = instr
    rowcol = 0 if mode == 'x' else 1
    found = set(filter(lambda x: x[rowcol] == pos, grid))
    if mode == 'x':
        newnodes = set([(n[0], (n[1] + offset) % 6) for n in found])
    else:
        newnodes = set([((n[0] + offset) % 50, n[1]) for n in found])
    return (grid - found) | newnodes

def parse_instrs(instrs):
    grid = set()
    for i in instrs:
        if i[0] == 'r':
            grid |= {(x, y) for y in range(i[2]) for x in range(i[1])}
        else:
            grid = rotate(grid, i)
    return grid

def print_grid(grid):
    for x in range(6):
        for y in range(50):
            out = '#' if (y, x) in grid else '.'
            print(out, end='')
        print('')

def main():
    grid = parse_instrs(load_data())
    print_grid(grid)

if __name__ == '__main__':
    main()
