# AoC 2016 -Day 2a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def parse_instrs(instr):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    moves = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
    code = []

    curr_y, curr_x = 1, 1

    for line in instr:
        for move in line:
            curr_y, curr_x = curr_y + moves[move][0], curr_x + moves[move][1]
            if curr_y < 0: curr_y = 0
            if curr_x < 0: curr_x = 0
            if curr_y > 2: curr_y = 2
            if curr_x > 2: curr_x = 2
        code.append(keypad[curr_y][curr_x])
    return ''.join([str(x) for x in code])

def main():
    assert parse_instrs(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '1985'
    data = load_data()
    print(parse_instrs(data))

if __name__ == '__main__':
    main()
