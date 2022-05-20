# AoC 2017 - Day 19

def load_data():
    grid = {}
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, col in enumerate(row):
                if col not in (' ', '\n'):
                    grid[(colnum, rownum)] = col
    return grid

def navigate(grid, x, y, curr_dir, mode='look_ahead'):
    dirs = ['u', 'r', 'd', 'l']
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    idx = dirs.index(curr_dir)

    if mode == 'look_ahead':
        nextpos = (x + moves[idx][0], y + moves[idx][1])
        if nextpos in grid:
            return nextpos
    else:
        opts = (idx - 1), (idx + 1) % 4
        for opt in opts:
            new_x, new_y = x + moves[opt][0], y + moves[opt][1]
            if (new_x, new_y) in grid:
                return new_x, new_y, dirs[opt]

def follow(grid):
    letters = []
    curr_dir = 'd'

    x, y = [c for c in grid.keys() if c[1] == 0][0]
    while True:
        if grid[(x, y)].isalpha():
            letters.append(grid[(x, y)])

        ahead = navigate(grid, x, y, curr_dir)
        if ahead:
            x, y = ahead
        else:
            turn = navigate(grid, x, y, curr_dir, 'turn')
            if turn:
                x, y, curr_dir = turn
            else:
                break
    return ''.join(letters)

def main():
    g = load_data()
    print(follow(g))

if __name__ == '__main__':
    main()
