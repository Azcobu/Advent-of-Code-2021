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

def calc_sqr_totals(grid, x, y):
    maxsize = 15
    totals = {}
    runtotal = 0

    for size in range(1, maxsize+1):
        new_row = y + size - 1
        new_col = x + size - 1
        if new_row < 301 and new_col < 301:
            runtotal += sum([grid[(nx, new_row)] for nx in range(x, new_col + 1)])
            runtotal += sum([grid[(new_col, ny)] for ny in range(y, new_row + 1)])
            runtotal -= grid[(new_col, new_row)]
            totals[size] = runtotal
        else:
            break
    
    best = sorted(totals.items(), key=lambda x:x[1])[-1]
    return best
   
def find_ltp(grid):
    max_pwr = 0
    max_loc = None
    max_size = 0

    for x in range(1, 300):
        for y in range(1, 300):
            best_sqr_size, best_sqr_pwr = calc_sqr_totals(grid, x, y)
            if best_sqr_pwr > max_pwr:
                max_pwr = best_sqr_pwr
                max_loc = (x, y)
                max_size = best_sqr_size
    return max_loc, max_size

def main():
    print(find_ltp(gen_grid(1309)))

if __name__ == '__main__':
    main()
