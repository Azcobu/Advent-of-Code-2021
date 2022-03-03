# AoC 2016 - Day 24a

def load_data():
    walls, nums = [], {}
    with open('input.txt', 'r') as infile:
        for ypos, y_c in enumerate(infile.readlines()):
            for xpos, x_c in enumerate(y_c):
                if x_c == '#':
                    walls.append((xpos, ypos))
                elif x_c.isnumeric():
                    nums[int(x_c)] = (xpos, ypos)
    return walls, nums

def find_dist(walls, x, y, t_x, t_y, path):
    if x == t_y and y == t_y:
        yield len(path)
    else:
        for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            n_x, n_y = x + diff[0], y + diff[1]
            if (n_x, n_y) not in walls:
                yield from find_dist(walls, n_x, n_y, t_x, t_y, path + )

def main():
    find_dist.visited = {(3, 5): 0} # goal 5, 173
    w, n = load_data()
    print(n)

if __name__ == '__main__':
    main()
