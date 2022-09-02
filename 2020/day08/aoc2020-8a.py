
def load_data():
    instrs = {}
    with open('input.txt', 'r') as infile:
        for linenum, line in enumerate(infile.read().splitlines()):
            instr, num = line.split(' ')
            instrs[linenum] = (instr, int(num))
    return instrs

def find_loop(instrs):
    visited = set()
    currline = 0
    acc = 0

    while currline not in visited:
        instr, num = instrs[currline]
        nextline = 1
        if instr == 'acc':
            acc += num
        elif instr == 'jmp':
            nextline = num
        visited.add(currline)
        currline += nextline
    return acc

def main():
    print(find_loop(load_data()))

if __name__ == '__main__':
    main()
