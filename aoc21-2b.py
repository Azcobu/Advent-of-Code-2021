#Advent of Code 2021 - 2a
# 2039912

testdata = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

def load_data():
    with open(r'd:\python\code\aoc21\aoc-2-input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]
    return indata

def get_digit(instr):
    return int(instr.partition(' ')[2])

def calc_course(indata):
    hor_pos, depth, aim = 0, 0, 0

    for instr in indata:
        if instr.startswith('forward'):
            hor_pos += get_digit(instr)
            depth += get_digit(instr) * aim
        elif instr.startswith('up'):
            aim -= get_digit(instr)
        elif instr.startswith('down'):
            aim += get_digit(instr)
        else:
            print(f'Unknown command: {instr}')
    return hor_pos, depth

def main():
    h, d = calc_course(testdata)
    assert h * d == 900
    indata = load_data()
    h, d = calc_course(indata)
    print(h*d)

if __name__ == '__main__':
    main()
