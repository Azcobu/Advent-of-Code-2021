# AoC 2016 - Day 12a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip().split() for x in infile.readlines()]

def parse(instrs):
    reg = {'a':0, 'b':0, 'c':0, 'd':0}
    curr_pos = 0

    while curr_pos < len(instrs):
        curr_instr = instrs[curr_pos]
        jump = 1

        if curr_instr[0] == 'cpy':
            x, y = curr_instr[1], curr_instr[2]
            reg[y] = reg[x] if x in reg.keys() else int(x)
        elif curr_instr[0] == 'inc':
            reg[curr_instr[1]] += 1
        elif curr_instr[0] == 'dec':
            reg[curr_instr[1]] -= 1
        else:
            x, y = curr_instr[1], curr_instr[2]
            if x.isnumeric() or (x in reg.keys() and reg[x]):
                jump = int(y)
        curr_pos += jump

    return reg['a']

def main():
    print(parse(load_data()))

if __name__ == '__main__':
    main()
