import re

def load_data():
    tests, prog = [], []
    with open('input.txt', 'r') as infile:
        data, program = infile.read().split('\n\n\n\n')
    data = data.split('\n\n')
    for test in data:
        nums = [int(x) for x in re.findall('-?\d+', test)]
        before = {k:v for k, v in zip(range(4), nums[:4])}
        after = {k:v for k, v in zip(range(4), nums[8:])}
        tests.append([before, nums[4:8], after])
    for line in program.split('\n'):
        nums = [int(x) for x in re.findall('-?\d+', line)]
        if nums: prog.append(nums)
    return tests, prog

ops = {'addr': lambda regs, a, b: regs[a] + regs[b], 
       'addi': lambda regs, a, b: regs[a] + b,
       'mulr': lambda regs, a, b: regs[a] * regs[b], 
       'muli': lambda regs, a, b: regs[a] * b,
       'banr': lambda regs, a, b: regs[a] & regs[b], 
       'bani': lambda regs, a, b: regs[a] & b,
       'borr': lambda regs, a, b: regs[a] | regs[b], 
       'bori': lambda regs, a, b: regs[a] | b,
       'setr': lambda regs, a, b: regs[a], 
       'seti': lambda regs, a, b: a,
       'gtir': lambda regs, a, b: 1 if a > regs[b] else 0, 
       'gtri': lambda regs, a, b: 1 if regs[a] > b else 0,
       'gtrr': lambda regs, a, b: 1 if regs[a] > regs[b] else 0, 
       'eqir': lambda regs, a, b: 1 if a == regs[b] else 0,
       'eqri': lambda regs, a, b: 1 if regs[a] == b else 0, 
       'eqrr': lambda regs, a, b: 1 if regs[a] == regs[b] else 0
}

def gen_opcode_mappings(tests):
    opcodes = {k:list(ops.keys()) for k in range(16)}

    for test in tests:
        before, inputs, after = test
        opcode, a, b, c = inputs
        opslist = opcodes[opcode]

        for opname in opslist:
            res = before.copy()
            res[c] = ops[opname](res, a, b)
            if res != after:
                opcodes[opcode].remove(opname)

    single = [k for k, v in opcodes.items() if len(v) == 1][0]
    done = []
    while len(done) < 15:
        done.append(single)
        for k, v in opcodes.items():
            if opcodes[single][0] in v and single != k:
                v.remove(opcodes[single][0])
        single = [k for k, v in opcodes.items() if len(v) == 1 and k not in done][0]

    return opcodes

def run_program(opcodes, program):
    regs = {0:0, 1:0, 2:0, 3:0}

    for instr in program:
        opnum, a, b, c = instr
        opname = opcodes[opnum][0]
        regs[c] = ops[opname](regs, a, b)
    print(regs[0])

def main():
    data, program = load_data()
    opcodes = gen_opcode_mappings(data)
    run_program(opcodes, program)

if __name__ == '__main__':
    main()
