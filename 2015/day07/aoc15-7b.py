# AoC 2015 - Day 7

wirevals = {}

def load_data():
    output = {}
    with open('input.txt', 'r') as infile:
        for line in infile:
            ops, res = line.split(' -> ')
            output[res.strip()] = ops.strip().split(' ')
    return output

def eval_wire(target):
    print(f'Evaluating {target}')
    if target.isnumeric():
        return int(target)

    if target not in wirevals:
        instr = eval_wire.instrs[target]

        if len(instr) == 1:
            if instr[0].isnumeric():
                return int(instr[0])
            else:
                wirevals[target] = eval_wire(instr[0])
        elif 'NOT' in instr:
            wirevals[target] = 65536 + ~eval_wire(instr[1])
        elif 'AND' in instr:
            wirevals[target] = eval_wire(instr[0]) & eval_wire(instr[2])
        elif 'LSHIFT' in instr:
            wirevals[target] = eval_wire(instr[0]) << int(instr[2])
        elif 'RSHIFT' in instr:
            wirevals[target] = eval_wire(instr[0]) >> int(instr[2])
        elif 'OR' in instr:
            wirevals[target] = eval_wire(instr[0]) | eval_wire(instr[2])

    return wirevals[target]

def main():
    eval_wire.instrs = load_data()
    eval_wire.instrs['b'] = ['46065']
    print(eval_wire('a'))

if __name__ == '__main__':
    main()
