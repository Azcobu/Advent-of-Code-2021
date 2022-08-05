# AoC 2018 Day 22a

def calc_erosion(x, y, cave, depth, target):
    if x == y == 0 or (x, y) == target:
        geo_index = 0
    elif x == 0:
        geo_index = y * 48271
    elif y == 0:
        geo_index = x * 16807
    else:
        geo_index = cave[(x-1, y)] * cave[(x, y-1)]
    return (geo_index + depth) % 20183

def calc_risk(depth, target):
    cave = {}
    for y in range(target[1] + 1):
        for x in range(target[0] + 1):
            cave[(x, y)] = calc_erosion(x, y, cave, depth, target)

    return sum([x % 3 for x in cave.values()])

def main():
    assert calc_risk(510, (10,10)) == 114
    print(calc_risk(11394,(7, 701)))

if __name__ == '__main__':
    main()
