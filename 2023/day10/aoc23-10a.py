# AoC 2023 Day 10a

def load_data():
    grid = {}
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, line in enumerate(infile.readlines()):
            for colnum, char in enumerate(line.strip()):
                grid[(colnum, rownum)] = char
    return grid

def main():
    dirs = {'N': (0, -1) , 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    transitions = {('N', '7'): 'W', ('N', 'F'): 'E', ('S', 'L'): 'E', ('S', 'J'): 'W',\
                   ('E', 'J'): 'N', ('E', '7'): 'S', ('W', 'L'): 'N', ('W', 'F'): 'S'}

    grid = load_data()
    start = [k for k, v in grid.items() if v == 'S'][0]
    currpos = start
    currdir = 'N'
    steps = 0

    while True:
        nextpos = dirs[currdir]
        currpos = (currpos[0] + nextpos[0], currpos[1] + nextpos[1])
        currchar = grid[currpos]
        steps += 1
        if currchar == 'S':
            break
        if currchar not in '|-':
            currdir = transitions[(currdir, currchar)]
    print(steps//2)

if __name__ == '__main__':
    main()
