# AoC 2016 - Day 1a

def load_data():
    with open('input.txt', 'r') as infile:
        indata = infile.read()
    return [x.strip() for x in indata.split(', ')]

def parse_instrs(instrs):
    x, y, facing = 0, 0, 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # n, e, s, w

    for i in instrs:
        turn, blocks = i[0], int(i[1:])
        facemod = 1 if turn == 'R' else -1
        facing += facemod
        if facing < 0: facing = 3
        if facing > 3: facing = 0
        x += dirs[facing][0] * blocks
        y += dirs[facing][1] * blocks
    return abs(x) + abs(y)

def main():
    test = load_data()
    print(parse_instrs(test))

if __name__ == '__main__':
    main()
