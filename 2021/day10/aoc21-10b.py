# Advent of Code 2021 - 10b

from statistics import median

def load_data(fname):
    with open(fname, 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def autocorrect(instr):
    scores = {'(':1, '[':2, '{':3, '<':4}

    pairings = ['()', '[]', '{}', '<>']
    while any(x in instr for x in pairings):
        for p in pairings:
            instr = instr.replace(p, '')

    for x in ') ] } >'.split():
        if x in instr:
            return # corrupted string

    score = 0
    for x in instr[::-1]:
        score = (score * 5) + scores[x]
    return score

def main():
    data = load_data('aoc-10-input.txt')
    scores = []

    #data = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '(((({<>}<{<{<>}{[]{[]{}',
    #        '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]']

    for line in data:
        score = autocorrect(line)
        if score:
            scores.append(score)
    print(median(scores))

if __name__ == '__main__':
    main()
