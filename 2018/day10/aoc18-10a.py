# AoC 2018 - Day 10a
from parse import parse

def load_data():
    points, vels = [], []
    with open('input.txt', 'r') as infile:
        parsestr = 'position=<{}, {}> velocity=<{}, {}>\n'
        for line in infile:
            p_x, p_y, v_x, v_y = parse(parsestr, line)
            points.append([int(p_x), int(p_y)])
            vels.append((int(v_x), int(v_y)))
    return points, vels

def output(points, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        line = ['#' if [x, y] in points else '.' for x in range(min_x, max_x + 1)]
        print(''.join(line))

def find_text(points, vels):
    while True:
        for pos, p in enumerate(points):
            p[0] += vels[pos][0]
            p[1] += vels[pos][1]

        max_x, min_x = max([x[0] for x in points]), min([x[0] for x in points])
        max_y, min_y = max([x[1] for x in points]), min([x[1] for x in points])
        height = max_y - min_y
        if height <= 15:
            break
    output(points, min_x, max_x, min_y, max_y)

def main():
    p, v = load_data()
    find_text(p, v)

if __name__ == '__main__':
    main()
