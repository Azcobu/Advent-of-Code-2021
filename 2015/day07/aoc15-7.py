# AoC 2015 - Day 7

from collections import defaultdict

def load_data():
    output = []
    with open('input.txt', 'r') as infile:
        return [x.split() for x in infile]

def calc_signals(instrs):
    wires = defaultdict(int)
    for instr in instrs:
        if 'AND' in instr:
            wires[instr[-1]] = wires[instr[0]] & wires[instr[2]]
        elif 'LSHIFT' in instr:
            wires[instr[-1]] = wires[instr[0]] << int(instr[2])
        elif 'RSHIFT' in instr:
            wires[instr[-1]] = wires[instr[0]] >> int(instr[2])
        elif 'NOT' in instr:
            wires[instr[-1]] = 65536 + ~wires[instr[1]]
        elif 'OR' in instr:
            wires[instr[-1]] = wires[instr[0]] | wires[instr[2]]
        else:
            if instr[0].isnumeric():
                wires[instr[-1]] = int(instr[0])
            else:
                wires[instr[-1]] = wires[instr[0]]
    return wires['a']

def main():
    data = load_data()
    print(calc_signals(data))

if __name__ == '__main__':
    main()
