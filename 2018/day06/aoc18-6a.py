# AoC 2018 - Day 6a

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
    min_x = min(c[0] for c in coords.values())
    max_x = max(c[0] for c in coords.values())
    min_y = min(c[1] for c in coords.values())
    max_y = max(c[1] for c in coords.values())

    for curr_y in range(min_y, max_y + 1):
        for curr_x in range(min_x, max_x+1):
            mindist = 99999
            for node_id, c in coords.items():
                coord_x, coord_y = c
                dist = abs(coord_x - curr_x) + abs(coord_y - curr_y)
                if dist < mindist:
                    mindist = dist
                    grid[(curr_x, curr_y)] = node_id
                elif dist == mindist:
                    grid[(curr_x, curr_y)] = '.'

    for coords, closest in grid.items():
        gridcount[closest] = gridcount.get(closest, 0) + 1

    return sorted(gridcount.items(), key=lambda x:x[1])[-1][1]

def main():
    print(calc_dists(load_data()))

if __name__ == '__main__':
    main()
