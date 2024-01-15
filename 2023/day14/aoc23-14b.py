# AoC 2023 Day 14b

def load_data():
    rocks = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, char in enumerate(row):
                if char in '#O':
                    rocks[(colnum, rownum)] = char
    return rocks

def rotate(grid):
    centre_x = max(x for x, y in grid.keys()) / 2
    centre_y = max(y for x, y in grid.keys()) / 2

    grid = {(k[0] - centre_x, k[1] - centre_y): v for k, v in grid.items()}
    grid = {(-k[1], k[0]): v for k, v in grid.items()}
    grid = {(int(k[0] + centre_x), int(k[1] + centre_y)): v for k, v in grid.items()}

    return grid

def tilt(grid):
    maxrow = max([x[1] for x in grid.keys()]) + 1
    maxcol = max([x[0] for x in grid.keys()]) + 1
    newrocks = {}

    for y in range(maxrow):
        for x in range(maxcol):
            if (x, y) in grid:
                rock = grid[(x, y)]

                if rock == '#':
                    newrocks[(x, y)] = '#'
                else:
                    nx, ny = x, y
                    while (nx, ny - 1) not in newrocks and (ny - 1) >= 0:
                        ny -= 1
                    newrocks[(nx, ny)] = 'O'
    return newrocks

def cycle(grid):
    for _ in range(4):
        grid = tilt(grid) 
        grid = rotate(grid) 
    return grid

def main():
    g = load_data()
    seen = [g]
    counter = 0
    target = 1000000000

    while counter < target:
        counter += 1
        g = cycle(g)
        if g in seen:
            looplen = counter - seen.index(g)
            counter += (target - counter) // looplen * looplen 
            seen = []
        else:
            seen.append(g)

    maxrow = max([x[1] for x in g.keys()]) + 1
    load = sum([maxrow - coords[1] for coords, rock in g.items() if rock == 'O'])
    print(load)

if __name__ == '__main__':
    main()
