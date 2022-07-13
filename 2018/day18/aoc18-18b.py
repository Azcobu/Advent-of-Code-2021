def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate([x.strip() for x in infile.readlines()]):
            for colnum, char in enumerate(row):
                grid[(colnum, rownum)] = char
    return grid

def sim_grid(grid, gridsize):
    saved = []
    skipped = False
    tick = 0
    neighs = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    
    while tick < 1000000000:
        nextgen = {}
        for y in range(gridsize):
            for x in range(gridsize):
                treecount, yardcount = 0, 0
                for mod_x, mod_y in neighs:
                    new_x, new_y = x + mod_x, y + mod_y
                    if 0 <= new_x < gridsize and 0 <= new_y < gridsize:
                        if grid[(new_x, new_y)] == '|':
                            treecount += 1
                        if grid[(new_x, new_y)] == '#':
                            yardcount += 1

                if grid[(x, y)] == '.':
                    nextgen[(x, y)] = '|' if treecount >= 3 else '.'
                elif grid[(x, y)] == '|':
                    nextgen[(x, y)] = '#' if yardcount >= 3 else '|'
                elif grid[(x, y)] == '#':
                    nextgen[(x, y)] = '#' if yardcount > 0 and treecount > 0 else '.'

        grid = nextgen

        if not skipped:
            if grid in saved:
                cyclelen = tick - saved.index(grid)
                jump = (1000000000 - tick) // cyclelen * cyclelen
                print(f'Cycle with length {cyclelen} found, jumping ahead by {jump} ticks.')
                tick += jump
                skipped = True
            else:
                saved.append(grid)
        tick += 1

    treecount = sum([1 for k, v in grid.items() if v == '|'])
    yardcount = sum([1 for k, v in grid.items() if v == '#'])
    return treecount * yardcount

def print_grid(grid, gridsize):
    for y in range(gridsize):
        print(''.join([grid[(x, y)] for x in range(gridsize)]))
    print()
        
def main():
    grid = load_data()
    print(sim_grid(grid, 50))

if __name__ == '__main__':
    main()
