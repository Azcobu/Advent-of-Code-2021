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

def parse(instrs, currprog = 0):
    queues = {0: [], 1: []}
    regs = {k:{x:0 for x in list('acdefghijklmnopqrstuvwxyz')} for k in [0, 1]}
    regs[1]['p'] = 1
    currpos = [0, 0]
    blockflags = [False, False]
    p1sendval = 0

    while True:
        jump = 0
        op, *args = instrs[currpos[currprog]]
        if len(args) == 2:
            a, b = args[0], get_val(regs[currprog], args[1])
        else:
            a = args[0]
        if op == 'set':
            regs[currprog][a] = b
        elif op == 'add':
            regs[currprog][a] += b
        elif op == 'mul':
            regs[currprog][a] *= b
        elif op == 'mod':
            regs[currprog][a] %= b
        elif op == 'snd':
            queues[not currprog].append(b)
            if currprog == 1:
                p1sendval += 1
        elif op == 'rcv':
            if len(queues[currprog]) > 0:
                regs[currprog][a] = queues[currprog].pop(0)
                blockflags[not currprog] = False
            blockflags[currprog] = not(len(queues[currprog]) > 0)

            if blockflags[currprog] == True and blockflags[not currprog] == True:
                break

        elif op == 'jgz':
            if a in regs[currprog]:
                if regs[currprog][a] > 0:
                    jump = b
            elif int(a) > 0:
                    jump = b
            else:
                print(f'{a}')

        if not blockflags[currprog]:
            currpos[currprog] += jump if jump else 1
        else:
            currprog = int(not currprog)

    return p1sendval

def main():
    i = load_data()
    print(parse(i))

if __name__ == '__main__':
    main()
