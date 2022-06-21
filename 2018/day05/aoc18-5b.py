# AoC 2018 - Day 5a

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().strip()

def collapse(instr):
    letts = [x for x in set(instr) if x.islower()]
    pairs = [l + l.upper() for l in letts] + [l.upper() + l for l in letts]
    results = {x:0 for x in letts}

    for letter in letts:
        currstr = instr.replace(letter, '')
        currstr = currstr.replace(letter.upper(), '')
    
        while True:
            changed = False
            for p in pairs:
                if p in currstr:
                    currstr = currstr.replace(p, '')
                    changed = True
            if not changed:
                results[letter] = len(currstr)
                break

    print(sorted(results.items(), key=lambda x:x[1])[0])

def main():
    print(collapse(load_data()))

if __name__ == '__main__':
    main()
