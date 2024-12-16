# AoC 24 - Day 6b

def load_data() -> dict:
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, symbol in enumerate(row):
                grid[(colnum, rownum)] = symbol
    return grid

def is_cyclic(grid: dict, start: tuple, facing: str,changed: tuple = (-1, -1)) -> bool:
    dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    pos = start
    visited = []
    visited.append((start, facing))

    newgrid = grid.copy()
    newgrid[changed] = '#'

    while True:
        next_pos = (pos[0] + dirs[facing][0], pos[1] + dirs[facing][1])
        if next_pos not in newgrid:
            return visited if changed == (-1, -1) else False
        if newgrid[next_pos] == '#':
            facing = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[facing]
        else:
            pos = next_pos
            if (pos, facing) in visited:
                print(f'Cycle found for {changed}')
                return True
            else:
                visited.append((pos, facing))
 
def main():
    loops = 0
    grid = load_data()
    start = [k for k, v in grid.items() if v == '^'][0]
    base_path = [x for x in (is_cyclic(grid, start, 'N'))]

    for pos, start in enumerate(base_path[:-1]):
        obs = base_path[pos + 1]
        print(f'{pos} of {len(base_path) - 1}: {start[0]} - {obs[0]}')
        if is_cyclic(grid, start[0], start[1], obs[0]):
            loops += 1
    print(loops)


if __name__ == '__main__':
    main()
    