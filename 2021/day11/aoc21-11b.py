# Advent of Code 2021 - 11a

def load_data(fname):
    octs = {}
    with open(fname, 'r') as infile:
        for y, line in enumerate(infile.readlines()):
            line = line.strip()
            for x, val in enumerate(line):
                octs[(x, y)] = int(val)
    return octs

def find_neighbours(octs, x, y):
    valid = []
    n = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for ymod, xmod in n:
        if 0 <= y + ymod < 10 and 0 <= x + xmod < 10 :
            valid.append((x + xmod, y + ymod))
    return valid

def draw_grid(octs, step):
    print('*****************')
    print(f'Step {step}:')
    for y in range(10):
        row = ''
        for x in range(10):
            row += str(octs[(x, y)])
        print(row)

def count_flashes(octs, steps):
    flashcount = 0

    for step in range(steps):
        flashed_already = set()

        octs = {k:v+1 for k, v in octs.items()}
        flashes = set([k for k, v in octs.items() if v > 9])

        while flashes:
            curr_flash = flashes.pop()
            octs[curr_flash] = 0
            flashed_already.add(curr_flash)

            for n in find_neighbours(octs, *curr_flash):
                if n not in flashed_already:
                    octs[n] += 1
                    if octs[n] > 9:
                        flashes.add(n)

        flashcount += len(flashed_already)
        if len(flashed_already) == len(octs):
            print(f'Synchronised flash at step {step+1}')
        #draw_grid(octs, step)
    return flashcount

def main():
    octs = load_data('aoc-11-input.txt')
    steps = 600
    count = count_flashes(octs, steps)
    print(count)

if __name__ == '__main__':
    main()
