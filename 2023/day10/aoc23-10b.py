# AoC 2023 Day 10b

def load_data():
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, line in enumerate(infile.readlines()):
            for colnum, char in enumerate(line.strip()):
                grid[(colnum, rownum)] = char
    return grid

def count_enclosed(grid, loop):
    enclosed = 0
    max_x = max(x[0] for x in grid.keys())
    max_y = max(x[1] for x in grid.keys())

    for y in range(max_y):
        for x in range(max_x):
            if (x, y) not in loop:
                maxsteps = min(x, y)
                linecoords = [(x - k, y - k) for k in range(maxsteps + 1)]
                intersects = sum([1 for x in linecoords if grid[x] in '|-FJ' and x in loop])
                if intersects % 2 == 1:
                    enclosed += 1
    print(enclosed)

def main():
    dirs = {'N': (0, -1) , 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    startdirs = {'N': '|F7', 'E': '-J7', 'S': '|JL', 'W': '-LF'}
    transitions = {('N', '7'): 'W', ('N', 'F'): 'E', ('S', 'L'): 'E', ('S', 'J'): 'W',\
                   ('E', 'J'): 'N', ('E', '7'): 'S', ('W', 'L'): 'N', ('W', 'F'): 'S'}
    grid = load_data()
    start = [k for k, v in grid.items() if v == 'S'][0]
    currpos = start
    currdir = 'N'
    loop = set()

    for k, v in dirs.items():
        cand = (start[0] + v[0], start[1] + v[1])
        if cand in grid and grid[cand] in startdirs[k]:
            currdir = k
            break

    while True:
        nextpos = dirs[currdir]
        currpos = (currpos[0] + nextpos[0], currpos[1] + nextpos[1])
        currchar = grid[currpos]
        loop.add(currpos)
        if currchar == 'S':
            break
        if currchar not in '|-':
            currdir = transitions[(currdir, currchar)]

    # set S pipe - ex2 = F, ex3 = F, ex4 = 7, input = J
    grid[start] = 'J'
    count_enclosed(grid, loop)

if __name__ == '__main__':
    main()
