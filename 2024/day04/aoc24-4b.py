# AoC 24 - Day 4a
from collections import defaultdict

def load_data() -> dict:
    letters = defaultdict(lambda:'.')
    with open('input.txt', 'r', encoding='utf-8') as infile:
        for rownum, row in enumerate(infile.readlines()):
            for colnum, letter in enumerate(row):
                letters[(colnum, rownum)] = letter
    return letters

def main():
    found = 0
    dirs = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    letters = load_data()
    for pos, letter in list(letters.items()):
        if letter == 'A':
            ns = [letters[(d[0] + pos[0], d[1] + pos[1])] for d in dirs]
            if ''.join(ns) in ['MSMS', 'MMSS', 'SMSM', 'SSMM']:
                found += 1
    print(found)

if __name__ == '__main__':
    main()
