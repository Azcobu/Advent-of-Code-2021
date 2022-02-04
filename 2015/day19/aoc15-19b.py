# AoC 2015 - Day 19b

def load_data():
    repls, mole = {}, ''
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for line in data:
        if '=>' in line:
            instr, _, outstr = line.partition(' => ')
            if instr in repls:
                repls[instr].append(outstr)
            else:
                repls[instr] = [outstr]
        else:
            if line:
                mole = line
    return repls, mole

def count_repls(repls, instr):
    found = set()

    for target, replace in repls.items():
        for pos in range(len(instr)):
            if instr[pos: pos + len(target)] == target:
                for r in repls[target]:
                    found.add(instr[:pos] + instr[pos:].replace(target, r, 1))
    return len(found)

def main():
    repls = {'H':['HO', 'OH'], 'O':['HH']}
    print(count_repls(repls, 'HOH'))
    print(count_repls(repls, 'HOHOHO'))
    repls, mole = load_data()
    print(count_repls(repls, mole))

if __name__ == '__main__':
    main()
