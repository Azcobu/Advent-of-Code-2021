# Advent of Code 2021 - 10a

def load_data(fname):
    with open(fname, 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_corrupted(instr):
    pairings = ['()', '[]', '{}', '<>']
    while any(x in instr for x in pairings):
        for p in pairings:
            instr = instr.replace(p, '')

    for x in instr:
        if x in ') ] } >'.split():
            return x

def main():
    data = load_data('aoc-10-input.txt')
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137, None:0}
    syntax_score = 0

    #data = ['{([(<{}[<>[]}>{[]{[(<()>', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]',
    #        '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{']
    for line in data:
        syntax_score += scores[find_corrupted(line)]
    print(syntax_score)

if __name__ == '__main__':
    main()
