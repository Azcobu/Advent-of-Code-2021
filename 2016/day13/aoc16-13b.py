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
                if (n_x, n_y) not in navigate.found:
                    navigate.found.add((n_x, n_y))
                    yield from navigate(keynum, n_x, n_y, steps + 1)

def main():
    navigate.found = set((0, 0))
    list(navigate(1364, 0, 0, 0))
    print(len(navigate.found))

if __name__ == '__main__':
    main()
