# AoC 2018 - Day 5a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def collapse(instr):
    letts = [x for x in set(instr) if x.islower()]
    pairs = [l + l.upper() for l in letts] + [l.upper() + l for l in letts]
    
    while True:
        changed = False
        for p in pairs:
            if p in instr:
                instr = instr.replace(p, '')
                changed = True
        if not changed:
            return len(instr)

def main():
    print(collapse(load_data()))

if __name__ == '__main__':
    main()
