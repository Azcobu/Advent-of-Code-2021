# AoC 2017 - Day 9b

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read()

def calc_score(instr):
    score, total, garbage = 0, 0, False

    instr = instr.replace('!!', '')
    excs = [(pos, pos+1) for pos, char in enumerate(instr) if char == '!']
    excpos = [x for y in excs for x in y]
    newstr = ''.join([c for pos, c in enumerate(instr) if pos not in excpos])

    for char in newstr:
        if garbage:
            if char != '>':
                score += 1
        if char == '<':
            garbage = True
        elif char == '>':
            garbage = False

    return score

def main():
    print(calc_score('<{o"i!a,<{i<a>'))

if __name__ == '__main__':
    main()
