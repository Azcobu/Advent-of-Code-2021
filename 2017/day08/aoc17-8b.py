# AoC 2017 - Day 8a
from collections import defaultdict

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip().split() for x in infile]

def parse(instrs):
    maxvals = []
    reg = defaultdict(lambda: 0)
    for i in instrs:
        targ, op, amt, _, cond_reg, cond_op, cond_amt = i
        if eval(f'{reg[cond_reg]} {cond_op} {cond_amt}'):
            reg[targ] += int(amt) if op == 'inc' else (-1 * int(amt))
        maxvals.append(sorted(reg.items(), key=lambda x:x[1], reverse=True)[0][1])
    return max(maxvals)

def main():
    print(parse(load_data()))

if __name__ == '__main__':
    main()
