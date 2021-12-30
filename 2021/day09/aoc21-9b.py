# Advent of Code 2021 - 9b
# 1075536

def explore_basin(y, x, data, found):
    if (y, x) not in found and data[y][x] != '9':
        found.append((y, x))
        for p in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
             if 0 <= p[0] < len(data) and 0 <= p[1] < len(data[0]):
                yield from explore_basin(p[0], p[1], data, found)
    yield found

def find_basins(data):
    basins = []

    for ypos, row in enumerate(data):
        for xpos, val in enumerate(row):
            neighbours = []
            poss = (ypos-1, xpos), (ypos+1, xpos), (ypos, xpos-1), (ypos, xpos+1)
            nears = [p for p in poss if 0 <= p[0] < len(data) and 0 <= p[1] < len(row)]
            for p in nears:
                neighbours.append(data[p[0]][p[1]])

            if val < min(neighbours):
                for x in explore_basin(ypos, xpos, data, []):
                    if x not in basins:
                        basins.append(x)

    sizes = sorted([len(x) for x in basins], reverse=True)[:3]
    print(sizes)
    return sizes[0] * sizes[1] * sizes[2]

def main():
    fname = 'aoc-9-input.txt'
    with open(fname, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    print(find_basins(data))

if __name__ == '__main__':
    main()
