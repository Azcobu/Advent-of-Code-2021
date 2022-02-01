# AoC 2016 - Day 1b

def load_data():
    with open('input.txt', 'r') as infile:
        indata = infile.read()
    return [x.strip() for x in indata.split(', ')]

def parse_instrs(instrs):
    x, y, facing = 0, 0, 0
    visited = [(x, y)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # n, e, s, w

    for i in instrs:
        turn, blocks = i[0], int(i[1:])
        facemod = 1 if turn == 'R' else -1
        facing += facemod
        if facing < 0: facing = 3
        if facing > 3: facing = 0
        for dist in range(1, blocks + 1):
            x += dirs[facing][0] * 1
            y += dirs[facing][1] * 1
            if (x, y) in visited:
                return abs(x) + abs(y)
            else:
                visited.append((x, y))

def main():
    assert parse_instrs(['R8', 'R4', 'R4', 'R8']) == 4
    print(parse_instrs(load_data()))

if __name__ == '__main__':
    main()
