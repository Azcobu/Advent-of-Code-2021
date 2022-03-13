# AoC 2016 - Day 25a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip().split() for x in infile.readlines()]

def parse(instrs, init_a):
    reg = {'a':init_a, 'b':0, 'c':0, 'd':0}
    curr_pos = 0
    counter = 0
    output = []

    while curr_pos < len(instrs) and counter < 1000000:
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
        elif curr_instr[0] == 'out':
            outval = int(curr_instr[1]) if curr_instr[1].isnumeric() else reg[curr_instr[1]]
            if len(output) > 0:
                if outval == output[-1]: # pattern break
                    return False
            output.append(reg[curr_instr[1]])
        else: # jnz
            x, y = curr_instr[1], curr_instr[2]
            if x != 0 and x != '0':
                y = reg[y] if y in reg.keys() else int(y)
                if x.isnumeric() or (x in reg.keys() and reg[x] != 0):
                    jump = int(y)

        curr_pos += jump
        counter += 1

    return True

def main():
    for x in range(1000):
        print(f'Testing {x}')
        if parse(load_data(), x):
            print(x)
            break

if __name__ == '__main__':
    main()
