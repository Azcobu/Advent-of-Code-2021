# AoC 2016 - Day 23a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip().split() for x in infile.readlines()]

def modify_instr(ins):
    if len(ins) == 2:
        ins[0] = 'dec' if ins[0] == 'inc' else 'inc'
    elif len(ins) == 3:
        ins[0] = 'cpy' if ins[0] == 'jnz' else 'jnz'
    return ins

def parse(instrs):
    reg = {'a':7, 'b':0, 'c':0, 'd':0}
    curr_pos = 0

    while curr_pos < len(instrs):
        curr_instr = instrs[curr_pos]
        jump = 1

        if curr_instr[0] == 'cpy':
            x, y = curr_instr[1], curr_instr[2]
            if y.isnumeric():
                continue
            else:
                reg[y] = reg[x] if x in reg.keys() else int(x)
        elif curr_instr[0] == 'inc':
            reg[curr_instr[1]] += 1
        elif curr_instr[0] == 'dec':
            reg[curr_instr[1]] -= 1
        elif curr_instr[0] == 'tgl':
            tgl_jump = reg[curr_instr[1]]
            if curr_pos + tgl_jump < len(instrs):
                targ_instr = instrs[curr_pos + tgl_jump]
                instrs[curr_pos + tgl_jump] = modify_instr(targ_instr)
        else: # jnz
            x, y = curr_instr[1], curr_instr[2]
            y = reg[y] if y in reg.keys() else int(y)
            if x.isnumeric() or (x in reg.keys() and reg[x]):
                jump = int(y)
        curr_pos += jump

    return reg['a']

def main():
    print(parse(load_data()))

if __name__ == '__main__':
    main()
