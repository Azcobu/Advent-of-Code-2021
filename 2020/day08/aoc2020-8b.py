
def load_data():
    instrs = {}
    with open('input.txt', 'r') as infile:
        for linenum, line in enumerate(infile.read().splitlines()):
            instr, num = line.split(' ')
            instrs[linenum] = (instr, int(num))
    return instrs

def find_valid(instrs):
    visited = set()
    currline = 0
    acc = 0

    while True:
        if currline in visited:
            return False
        if currline not in instrs.keys():
            return acc
        instr, num = instrs[currline]
        nextline = 1
        if instr == 'acc':
            acc += num
        elif instr == 'jmp':
            nextline = num
        visited.add(currline)
        currline += nextline

def gen_variations(instrs):
    variants = []
    for k, v in instrs.items():
        if 'jmp' in v or 'nop' in v:
            repl = 'nop' if 'jmp' in v else 'jmp'
            newdict = dict(instrs)
            newdict[k] = (repl, v[1])
            variants.append(newdict)
    return variants
        
def main():
    for v in gen_variations(load_data()):
        if acc := find_valid(v):
            print(acc)
            break

if __name__ == '__main__':
    main()
