# AoC 2023 Day 14b

def load_data():
    rocks = {}
    with open('example.txt', 'r', encoding='utf-8') as infile:
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

def draw(grid):
    maxrow = max([x[1] for x in grid.keys()]) + 1
    maxcol = max([x[0] for x in grid.keys()]) + 1

    for y in range(maxcol):
        for x in range(maxrow):
            if (x, y) in grid:
                print(grid[(x, y)], end='')
            else:
                print('.', end='')
        print()
    print()
    print()

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
    for x in range(3):
        grid = tilt(grid) 
        draw(grid)
        grid = rotate(grid) 
        draw(grid)
    return grid

def main():
    g = load_data()
    g = cycle(g)
    draw(g)

if __name__ == '__main__':
    main()
