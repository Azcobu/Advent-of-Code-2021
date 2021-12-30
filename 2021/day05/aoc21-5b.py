# Advent of Code 2021 - 5b

def load_data(fname):
    with open(fname, 'r') as infile:
        indata = [x.strip().split(' -> ') for x in infile.readlines()]
    return indata

def parse_lines(indata):
    all_coords = {}

    for coords in indata:
        start_x, start_y = [int(x) for x in coords[0].split(',')]
        end_x, end_y = [int(x) for x in coords[1].split(',')]

        if start_x == end_x:
            for k in range(min(start_y, end_y), max(start_y, end_y) + 1):
                all_coords[start_x, k] = all_coords.get((start_x, k), 0) + 1
        elif start_y == end_y:
            for k in range(min(start_x, end_x), max(start_x, end_x) + 1):
                all_coords[k, start_y] = all_coords.get((k, start_y), 0) + 1
        else:
            xdir = 1 if start_x < end_x else -1
            ydir = 1 if start_y < end_y else -1
            for prog, dx in enumerate(range(start_x, end_x + xdir, xdir)):
                dy = start_y + (prog * ydir)
                all_coords[dx, dy] = all_coords.get((dx, dy), 0) + 1
    return all_coords

def main():
    coords = load_data(r'D:\Python\Code\aoc21\aoc-5-input.txt')
    ventmap = parse_lines(coords)
    print(sum([1 for x in ventmap.values() if x > 1]))

if __name__ == '__main__':
    main()
