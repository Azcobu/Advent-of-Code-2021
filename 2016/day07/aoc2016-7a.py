# AoC 2016 - Day 7a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_abba(instr):
    for pos, letter in enumerate(instr[:-3]):
        if instr[pos] != instr[pos+1]:
            pair = instr[pos] + instr[pos+1]
            if instr[pos:pos+4] == pair + pair[::-1]:
                return True
    return False

def verify_ip(instr):
    found = False
    outside = True if instr[0] != '[' else False
    instr = instr.replace('[', ']').split(']')
    for s in instr:
        if find_abba(s):
            if not outside:
                return False
            else:
                found = True
        outside = not outside
    return found

def count_valid(indata):
    return sum([1 for x in indata if verify_ip(x)])

def main():
    print(count_valid(load_data()))

if __name__ == '__main__':
    main()
