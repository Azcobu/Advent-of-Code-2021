# AoC 2016 - Day 8a
import re

def load_data():
    instrs = []
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for d in data:
        if d.startswith('rect'):
            m = re.search(r'rect (\d+)x(\d+)', d)
            i_type = 'r'
        else:
            m = re.search(r'(\d+) by (\d+)', d)
            i_type = 'x' if 'x' in d else 'y'
        instrs.append((i_type, int(m.group(1)), int(m.group(2))))
    return instrs

def rotate(mode, amount):
    pass

def parse_instrs(instrs):
    pass

def main():
    print(load_data())

if __name__ == '__main__':
    main()
