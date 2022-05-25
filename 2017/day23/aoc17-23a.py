#AoC 2017- Day 23a

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
    reg = {x:0 for x in list('abcdefgh')}
    currpos = 0
    mul_count = 0

    while currpos < len(instrs):
        jump = 0
        op, *args = instrs[currpos]
        a, b = args[0], get_val(reg, args[1])
        if op == 'set':
            reg[a] = b
        elif op == 'sub':
            reg[a] -= b
        elif op == 'mul':
            reg[a] *= b
            mul_count += 1
        elif op == 'jnz':
            if a in reg.keys():
                if reg[a] != 0:
                    jump = b
            else:
                if int(a) != 0:
                    jump = b

        currpos += jump if jump else 1
    return mul_count

def main():
    i = load_data()
    print(parse(i))

if __name__ == '__main__':
    main()
