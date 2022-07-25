# AoC 2015 - Day 19b
import random

def load_data():
    repls, mole = [], ''
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for line in data:
        if '=>' in line:
            instr, _, outstr = line.partition(' => ')
            repls.append((instr, outstr))
        else:
            if line:
                mole = line
    return repls, mole

def gen_molecule(rules, mole):
    steps  = 0
    curr_mol = mole

    while len(curr_mol) > 1:
        start = curr_mol
        for instr, outstr in rules:
            if outstr in curr_mol:
                steps += curr_mol.count(outstr)
                curr_mol = curr_mol.replace(outstr, instr)
        if start == curr_mol:  
            random.shuffle(rules)
            curr_mol = mole
            steps = 0
    print(f'{steps} steps needed.')

def main():
    rules, mole = load_data()
    gen_molecule(rules, mole)

if __name__ == '__main__':
    main()
