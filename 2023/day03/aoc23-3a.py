# AoC 2023 Day 3a
import re

def load_data():
    nums = {}
    symbols = set()

    with open('input.txt', 'r', encoding='utf-8') as infile:
        grid = infile.readlines()
    for linenum, line in enumerate(grid):
        for match in re.finditer('\d+', line.strip()):
            coords = tuple([(p, linenum) for p in range(match.start(), match.end())])
            nums[coords] = match.group()
        for match in re.finditer('[^0-9.]', line.strip()):
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    symbols.add((match.start() + x_offset, linenum + y_offset))
    return nums, symbols

def main():
    total = 0

    nums, symbols = load_data()
    for k, v in nums.items():
        for coord in k:
            if coord in symbols:
                total += int(v)
                break
    print(total)

if __name__ == '__main__':
    main()
