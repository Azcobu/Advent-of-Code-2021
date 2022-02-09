# AoC 2016 - Day 6a
from collections import Counter

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def find_msg(instrs):
    wordlen = len(instrs[0])
    cols = [[] for x in range(wordlen)]

    for word in instrs:
        for pos, letter in enumerate(word):
            cols[pos].append(letter)

    return ''.join([Counter(c).most_common(1)[0][0] for c in cols])

def main():
    print(find_msg(load_data()))

if __name__ == '__main__':
    main()
