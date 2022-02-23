# AoC 2016 - Day 13a

def is_open(keynum, x, y):
    k = x*x + 3*x + 2*x*y + y + y*y + keynum
    return bin(k).count('1') % 2 == 0

def navigate(keynum, curr_x, curr_y, targ_x, targ_y, visited):
    if curr_x == targ_x and curr_y == targ_y:
        if len(visited) < navigate.minlen:
            navigate.minlen = len(visited)
            yield len(visited)
    else:
        if len(visited) < navigate.minlen:
            for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                n_x, n_y = curr_x + diff[0],  curr_y + diff[1]
                if n_x >= 0 and n_y >= 0 and (n_x, n_y) not in visited \
                and is_open(keynum, n_x, n_y):
                    yield from navigate(keynum, n_x, n_y, targ_x, targ_y, visited + [(n_x, n_y)])

def main():
    navigate.minlen = 999
    print(min([k for k in navigate(1364, 1, 1, 31, 39, [])]))

if __name__ == '__main__':
    main()
