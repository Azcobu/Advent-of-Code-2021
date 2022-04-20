# AoC 2017 - Day 16a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip().split(',')

def parse(instrs):
    progs = list('abcdefghijklmnop')
    for i in instrs:
        if i[0] == 's':
            step = -1 * int(i[1:])
            progs = progs[step:] + progs[:step]
        elif i[0] == 'x':
            pos1, pos2 = map(int, i[1:].split('/'))
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
        else: # p
            let1, let2 = i[1:].split('/')
            pos1, pos2 = progs.index(let1), progs.index(let2)
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
    return ''.join(progs)

def main():
    d = load_data()
    print(parse(d))

if __name__ == '__main__':
    main()
