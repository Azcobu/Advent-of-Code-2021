# Advent of Code 2021 - 11a

def load_data(fname):
    octs = {}
    with open(fname, 'r') as infile:
        for y, line in enumerate(infile.readlines()):
            line = line.strip()
            for x, val in enumerate(line):
                octs[(y, x)] = int(val)
    return octs

def find_neighbours(octs, y, x):
    valid = []
    n = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for ymod, xmod in n:
        if 0 <= y + ymod < 9 and 0 <= x + xmod < 9 :
            valid.append((y + ymod, x + xmod))
    return valid

def draw_grid(octs):
    print('*****************')
    for y in range(10):
        row = ''
        for x in range(10):
            row += str(octs[(y, x)])
        print(row)

def count_flashes(octs, steps):
    flashcount = 0

    for step in range(steps):
        draw_grid(octs)
        flashed_already = []
        octs = {k:v+1 for k, v in octs.items()}

        flashes = set({k:v for k, v in octs.items() if v > 9})
        while flashes:
            curr_flash = flashes.pop()
            if curr_flash not in flashed_already:
                octs[curr_flash] = 0
                flashcount += 1
                flashed_already.append(curr_flash)

                for n in find_neighbours(octs, *curr_flash):
                    octs[n] += 1
                    if octs[n] > 9:
                        flashes.add(n)
        for f in flashed_already:
            octs[f] = 0

    return flashcount

def inc_energy(octs):
    for y in octs:
        y = [x+1 for x in y]
    return octs

def main():
    octs = load_data('aoc-11-test.txt')
    steps = 100
    count = count_flashes(octs, steps)
    print(count)

if __name__ == '__main__':
    main()
