# AoC 2016 -Day 2b

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def parse_instrs(instr):
    keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0],
              [0, 0, 'D', 0, 0]]
    moves = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
    code = []

    curr_y, curr_x = 2, 0

    for line in instr:
        for move in line:
            poss_y, poss_x = curr_y + moves[move][0], curr_x + moves[move][1]
            if poss_y < 0: poss_y = 0
            if poss_x < 0: poss_x = 0
            if poss_y > 4: poss_y = 4
            if poss_x > 4: poss_x = 4
            if keypad[poss_y][poss_x]:
                curr_y, curr_x = poss_y, poss_x
        code.append(keypad[curr_y][curr_x])
    return ''.join([str(x) for x in code])

def main():
    assert parse_instrs(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '5DB3'
    data = load_data()
    print(parse_instrs(data))

if __name__ == '__main__':
    main()
