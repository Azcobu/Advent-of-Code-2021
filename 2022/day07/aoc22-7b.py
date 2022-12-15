# AoC 2022 Day 7b
from collections import defaultdict

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read().splitlines()

def parse_data(data):
    dirsizes = defaultdict(int)
    currdir = []

    for line in data:
        if line.startswith('$'):
            if 'cd /' in line:
                currdir = []
            elif 'cd ..' in line:
                currdir.pop()
            elif 'cd ' in line:
                currdir.append(line[5:])
            elif line == '$ ls':
                pass
        elif line.startswith('dir '):
            pass
        else:
            filesize = int(line.split(' ')[0])
            for d in range(len(currdir)+1):
                dirsizes[tuple(currdir[:d])] += filesize

    delsize = dirsizes[()] - 40000000
    return min([v for k, v in dirsizes.items() if v >= delsize])

def main():
    print(parse_data(load_data()))

if __name__ == '__main__':
    main()
