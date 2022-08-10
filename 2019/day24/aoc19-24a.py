
def load_data():
    grid = set()
    with open('input.txt', 'r') as infile:
        for ynum, line in enumerate([x.strip() for x in infile.readlines()]):
            for xnum, char in enumerate(line):
                if char == '#':
                    grid.add((xnum, ynum))
    return grid

def calc_biodiv_rating(grid):
    total = 0
    for y in range(5):
        for x in range(5):
            if (x, y) in grid:
                total += 2 ** (x + y * 5)
    return total

def evolve(grid):
    gridstates = []

    while grid not in gridstates:
        gridstates.append(grid)
        nextgen = set()

        for y in range(5):
            for x in range(5):
                nearbugs = 0
                for d_x, d_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (x + d_x, y + d_y) in grid:
                        nearbugs += 1
                if (x, y) in grid:
                    if nearbugs == 1:
                        nextgen.add((x, y))
                else:
                    if nearbugs in [1, 2]:
                        nextgen.add((x, y))
        grid = nextgen

    return calc_biodiv_rating(grid)

def main():
    d = load_data()
    print(evolve(d))

if __name__ == '__main__':
    main()
