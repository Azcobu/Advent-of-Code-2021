#AoC 24 Day 3a
import re

def load_data() -> str:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return infile.read()

def main():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    instr = load_data()
    total = sum([int(x) * int(y) for x, y in re.findall(pattern, instr)])
    print(total)

if __name__ == '__main__':
    main()
