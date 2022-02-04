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
    return rules, mole

def gen_molecule(rules, currstr, target, steps):
    if currstr == target:
        yield steps
    else:
        if len(currstr) <= len(target):
            for k, v in rules.items():
                for pos in range(len(currstr)):
                    if currstr[pos: pos + len(k)] == k:
                        for r in rules[k]:
                            currstr = currstr[:pos] + currstr[pos:].replace(k, r, 1)
                            yield from gen_molecule(rules, currstr, target, steps + 1)

def main():
    rules = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
    k = [x for x in gen_molecule(rules, 'e', 'HOH', 0)]
    print(k)


    #rules, mole = load_data()
    #print(count_repls(repls, mole))

if __name__ == '__main__':
    main()
