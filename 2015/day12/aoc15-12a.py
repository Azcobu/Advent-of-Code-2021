# AoC 15 Day 12a
import re

def load_data():
    with open('input.txt', 'r') as infile:
        return infile.read()

def main():
    data = load_data()
    print(sum(int(x) for x in re.findall('-?\d+', data)))

if __name__ == '__main__':
    main()
