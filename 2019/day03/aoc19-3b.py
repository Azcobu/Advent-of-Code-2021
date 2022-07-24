def load_data():
    with open('input.txt') as infile:
        return [x.strip() for x in infile.readlines()]

def process_data(lines):
    wires = []
    for line in lines:
        newline = []
        line = line.strip()
        for straight in line.split(','):
            newline.append((straight[0], int(straight[1:])))
        wires.append(newline)
    return wires

def find_intersect(wires):
    grid = {}
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    x, y = 0, 0
    intersect = []

    for wirenum, wire in enumerate(wires):
        x, y = 0, 0
        step = 0
        for direct, length in wire:
            for j in range(length):
                step += 1
                x, y = x + dirs[direct][0], y + dirs[direct][1]
                if (x, y) in grid:
                    if grid[(x, y)][0] != wirenum:
                        intersect.append(grid[(x, y)][1] + step)
                else:
                    grid[(x, y)] = (wirenum, step)

    return min(intersect)

def main():
    assert find_intersect(process_data(['R8,U5,L5,D3', 'U7,R6,D4,L4'])) == 30
    test2 = process_data(['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'])
    assert(find_intersect(test2)) == 610
    test3 = process_data(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    assert(find_intersect(test3)) == 410
    aoc = process_data(load_data())
    print(find_intersect(aoc))

if __name__ == '__main__':
    main()
