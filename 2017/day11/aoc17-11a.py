# AoC 2017 - Day 11a
# https://www.redblobgames.com/grids/hexagons

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.read().split(',')]

def calc_dist(indata):
    x, y = 0, 0
    dirs = {'nw':(-1, -1), 'n':(0, -2), 'ne':(1, -1),
            'sw':(-1, 1), 's':(0, 2), 'se':(1, 1)}
    for m in indata:
        x += dirs[m][0]
        y += dirs[m][1]
    return int(abs(x) + max(0, (abs(y) - abs(x))/2))

def main():
    assert calc_dist(['nw', 'nw', 'nw']) == 3
    assert calc_dist(['ne', 'ne', 'sw', 'sw']) == 0
    assert calc_dist(['ne', 'ne', 's', 's']) == 2
    assert calc_dist(['se', 'sw', 'se', 'sw', 'sw']) == 3
    d = load_data()
    print(calc_dist(d))

if __name__ == '__main__':
    main()
