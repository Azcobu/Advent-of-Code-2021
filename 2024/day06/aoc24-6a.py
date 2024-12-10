# AoC 24 - Day 6a

def load_data() -> dict:
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, symbol in enumerate(row):
                grid[(colnum, rownum)] = symbol
    return grid

def main():
    dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    visited = set()
    facing = 'N'
    grid = load_data()

    pos = [k for k, v in grid.items() if v == '^'][0]
    visited.add(pos)

    while True:
        next_pos = (pos[0] + dirs[facing][0], pos[1] + dirs[facing][1])
        if next_pos not in grid:
            break
        if grid[next_pos] == '#':
            facing = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[facing]
        else:
            pos = next_pos
            visited.add(pos)

    print(len(visited))

if __name__ == '__main__':
    main()
    