#AoC 24 Day 3a
import re

def load_data() -> str:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return infile.read().replace('\n', '')

def main():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    dontdo = r"don't\(\)(.*?do\(\)|.*$)"

    instr = load_data()
    instr = re.sub(dontdo, "", instr)
    total = sum([int(x) * int(y) for x, y in re.findall(pattern, instr)])
    print(total)

if __name__ == '__main__':
    main()
