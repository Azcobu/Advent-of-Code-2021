# AoC 2016 - Day 13b

def is_open(keynum, x, y):
    k = x*x + 3*x + 2*x*y + y + y*y + keynum
    return bin(k).count('1') % 2 == 0

def navigate(keynum, curr_x, curr_y, steps):
    if steps == 50:
        yield
    else:
        for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            n_x, n_y = curr_x + diff[0],  curr_y + diff[1]
            if n_x >= 0 and n_y >= 0 and is_open(keynum, n_x, n_y):
                if (n_x, n_y) not in navigate.visited or navigate.visited[(n_x, n_y)] > steps:
                    navigate.visited[(n_x, n_y)] = steps
                    yield from navigate(keynum, n_x, n_y, steps + 1)

def main():
    navigate.visited = {(1, 1): 0}
    list(navigate(1364, 1, 1, 0))
    print(len(navigate.visited))

if __name__ == '__main__':
    main()
