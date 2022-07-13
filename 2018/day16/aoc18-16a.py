import re

def load_data():
    tests = []
    with open('input.txt', 'r') as infile:
        data = infile.read().split('\n\n\n\n')[0]
    data = data.split('\n\n')
    for test in data:
        nums = [int(x) for x in re.findall('-?\d+', test)]
        before = {k:v for k, v in zip(range(4), nums[:4])}
        after = {k:v for k, v in zip(range(4), nums[8:])}
        tests.append([before, nums[4:8], after])
    return tests

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

def check_tests(tests):
    count = 0

    for test in tests:
        opcount = 0
        before, inputs, after = test
        opcode, a, b, c = inputs
        for opname, op in ops.items():
            res = before.copy()
            res[c] = op(res, a, b)
            if res == after:
                opcount += 1
        if opcount >= 3:
            count += 1
    return count
        
def main():
    d = load_data()
    print(check_tests(d))

if __name__ == '__main__':
    main()
