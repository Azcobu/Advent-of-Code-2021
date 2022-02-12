# AoC 2016 - Day 7a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_abas(instr):
    aba_list = []
    for pos, letter in enumerate(instr[:-2]):
        if instr[pos] == instr[pos+2] and instr[pos] != instr[pos+1]:
            aba_list.append(instr[pos:pos+3])
    return aba_list or False

def verify_ip(instr):
    aba_list = []
    found = False
    instr = instr.replace('[', ']').split(']')
    outs, ins = instr[::2], instr[1::2]

    for x in outs:
        if res := find_abas(x):
            aba_list += res

    for a in aba_list:
        bab = a[1] + a[0] + a[1]
        if any([bab in x for x in ins]):
            found = True

    return found

def main():
    print(sum([1 for x in load_data() if verify_ip(x)]))

if __name__ == '__main__':
    main()
