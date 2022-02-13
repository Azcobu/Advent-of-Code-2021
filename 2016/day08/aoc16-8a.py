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
        instrs.append((i_type, int(m.group(1)), int(m.group(2))))
    return instrs

def rotate(grid, instr):
    gridsize = 50, 6
    mode, pos, offset = instr
    rowcol = 1 if mode == 'x' else 0
    for node in grid:
        if node[rowcol] == pos:
            node[rowcol] += offset
            if node[rowcol] > gridsize[rowcol]:
                node[rowcol] = node[rowcol] % gridsize[rowcol]
    return grid

def parse_instrs(instrs):
    grid = []
    for i in instrs:
        if i[0] == 'r':
            for y in range(i[2]):
                for x in range(i[1]):
                    grid.append((x, y))
        else:
            grid = rotate(grid, i)
    return grid


def main():
    print(load_data())
    parse_instrs([('r', 3, 2), ('x', 1, 1)])


if __name__ == '__main__':
    main()
