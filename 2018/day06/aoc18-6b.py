# AoC 2018 - Day 6b

def load_data():
    coords = {}
    designator = 0
    with open('input.txt', 'r') as infile:
        for l in infile.read().splitlines():
            x, y = l.split(', ')
            coords[str(designator)] = (int(x), int(y))
            designator += 1
    return coords

def calc_dists(coords):
    grid, gridcount = {}, {}
    inrange = 0
    min_x = min(c[0] for c in coords.values())
    max_x = max(c[0] for c in coords.values())
    min_y = min(c[1] for c in coords.values())
    max_y = max(c[1] for c in coords.values())

    for curr_y in range(min_y, max_y + 1):
        for curr_x in range(min_x, max_x+1):
            currdist = 0
            for node_id, c in coords.items():
                coord_x, coord_y = c
                currdist += abs(coord_x - curr_x) + abs(coord_y - curr_y)
            if currdist < 10000:
                inrange += 1

    return inrange

def main():
    print(calc_dists(load_data()))

if __name__ == '__main__':
    main()
