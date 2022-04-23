# AoC 2017 - Day 18a

def get_val(reg, s):
    try:
        return int(s)
    except ValueError:
        return reg[s]

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        d = infile.readlines()
    for i in d:
        instrs.append(i.strip().split(' '))
    return instrs

def parse(instrs):
    reg = {x:0 for x in list('acdefghijklmnopqrstuvwxyz')}
    currpos = 0
    lastfreq = 0

    while currpos < len(instrs):
        jump = 0
        op, *args = instrs[currpos]
        if len(args) == 2:
            a, b = args[0], get_val(reg, args[1])
        else:
            a = args[0]
        if op == 'set':
            reg[a] = b
        elif op == 'add':
            reg[a] += b
        elif op == 'mul':
            reg[a] *= b
        elif op == 'mod':
            reg[a] %= b
        elif op == 'snd':
            lastfreq = reg[a]
        elif op == 'rcv':
            if reg[a]:
                return lastfreq
        elif op == 'jgz':
            if reg[a]:
                jump = b

        currpos += jump if jump else 1

def main():
    i = load_data()
    print(parse(i))

if __name__ == '__main__':
    main()
