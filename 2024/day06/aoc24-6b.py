# AoC 24 - Day 6b

def load_data() -> dict:
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, symbol in enumerate(row):
                grid[(colnum, rownum)] = symbol
    return grid

def is_cyclic(grid: dict, start: tuple, changed: tuple = (-1, -1)) -> tuple:
    dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    visited = set()
    pos = start
    facing ='N'
    visited.add((pos, facing))

    newgrid = grid.copy()
    newgrid[changed] = '#'

    while True:
        next_pos = (pos[0] + dirs[facing][0], pos[1] + dirs[facing][1])
        if next_pos not in newgrid:
            return visited if changed == (-1, -1) else None
        if newgrid[next_pos] == '#':
            facing = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[facing]
        else:
            pos = next_pos
            if (pos, facing) in visited:
                return changed
            else:
                visited.add((pos, facing))
 
def main():
    grid = load_data()
    start = [k for k, v in grid.items() if v == '^'][0]
    base_path = [x[0] for x in (is_cyclic(grid, start))]
    found = set()

    for obs in base_path:
        if is_cyclic(grid, start, obs):
            found.add(obs)
    print(len(found))

if __name__ == '__main__':
    main()
    