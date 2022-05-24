#AoC 2017 - Day 22a

def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        for rownum, row in enumerate(infile.read().splitlines()):
            for colnum, char in enumerate(row):
                if char == '#':
                    grid.add((colnum, rownum))
    return grid

def turn(curr_dir, turn_dir):
    turnmod = -1 if turn_dir == 'left' else 1
    idx = (curr_dir + turnmod) % 4
    return idx

def move(x, y, curr_dir):
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return (x + moves[curr_dir][0], y + moves[curr_dir][1])

def count_infections(grid):
    curr_dir, infs = 0, 0
    x = round(max([k[0] for k in grid])/2)
    y = round(max([k[1] for k in grid])/2)

    for burst in range(10000):
        turn_dir = 'right' if (x, y) in grid else 'left'
        curr_dir = turn(curr_dir, turn_dir)

        if (x, y) in grid:
            grid.remove((x, y))
        else:
            grid.add((x, y))
            infs += 1

        x, y = move(x, y, curr_dir)

    return infs

def main():
    print(count_infections(load_data()))

if __name__ == '__main__':
    main()
