# AoC 2023 Day 15b
from collections import defaultdict

def load_data():
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return infile.read()

def hashstr(instr):
    val = 0
    for c in instr:
        val = ((val + ord(c)) * 17) % 256
    return val

def main():
    boxes = defaultdict(dict)

    instr = load_data().strip()
    for s in instr.split(','):
        label = s[:-1] if '-' in s else s[:s.index('=')]
        boxnum = hashstr(label)
        if '-'in s:
            if label in boxes[boxnum]:
                del boxes[boxnum][label]
        else:
            boxes[boxnum][label] = int(s[-1])

    power = 0
    for box, lenses in boxes.items():
        for slotnum, (label, foclen) in enumerate(lenses.items()):
            power += (box + 1) * (slotnum + 1) * foclen

    print(power)

if __name__ == '__main__':
    main()
