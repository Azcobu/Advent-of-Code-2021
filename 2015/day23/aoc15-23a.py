# AoC 2015 - Day 23

def load_instrs():
    with open('input.txt', 'r') as infile:
        return {pos:line for pos, line in enumerate(infile.read().splitlines())}

def parse_instrs(instrs):
    currpos = 0
    regs = {'a':0, 'b':0}

    while True:
        if currpos not in instrs.keys():
            break

        curr_instr = instrs[currpos]
        instr = curr_instr[:3]
        jump = 1

        if instr != 'jmp':
            curr_reg = curr_instr[4]
            if instr == 'hlf':
                regs[curr_reg] //= 2
            elif instr == 'tpl':
                regs[curr_reg] *= 3
            elif instr == 'inc':
                regs[curr_reg] += 1
            else: # jio or jie
                if (instr == 'jie' and not regs[curr_reg] % 2) or\
                   (instr == 'jio' and regs[curr_reg] == 1):
                    sign, jump = curr_instr[7], int(curr_instr[8:])
                    if sign == '-': jump *= -1
        else:
            sign, jump = curr_instr[4], int(curr_instr[5:])
            if sign == '-': jump *= -1
        currpos += jump
    return regs

def main():
    instrs = load_instrs()
    print(parse_instrs(instrs)['b'])

if __name__ == '__main__':
    main()
