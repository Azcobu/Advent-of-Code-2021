#AoC 2018 - Day 11a

def gen_grid(serial):
    grid = {}

    for y in range(1, 301):
        for x in range(1, 301):
            rack = x + 10
            power = (rack * y + serial) * rack
            if power < 100:
                power = 0
            else:
                power = int(str(power)[-3])
            power -= 5
            grid[(x, y)] = power
    return grid

def find_ltp(grid):
    max_pwr = 0
    max_loc = None

    for y in range(1, 298):
        for x in range(1, 298):
            sqr_pwr = 0
            for yscan in range(y, y+3):
                for xscan in range(x, x+3):
                    sqr_pwr += grid[(xscan, yscan)]
            if max_pwr < sqr_pwr:
                max_pwr = sqr_pwr
                max_loc = (x, y)
    return max_loc

def main():
    print(find_ltp(gen_grid(1309)))

if __name__ == '__main__':
    main()
