# AoC 2017 - Day 11a
# https://www.redblobgames.com/grids/hexagons

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.read().split(',')]

def calc_dist(indata):
    maxdist = 0
    x, y = 0, 0
    dirs = {'nw':(-1, -1), 'n':(0, -2), 'ne':(1, -1),
            'sw':(-1, 1), 's':(0, 2), 'se':(1, 1)}
    for m in indata:
        x += dirs[m][0]
        y += dirs[m][1]
        maxdist = max(maxdist, int(abs(x) + max(0, (abs(y) - abs(x))/2)))
    return maxdist

def main():
    print(calc_dist(load_data()))

if __name__ == '__main__':
    main()
