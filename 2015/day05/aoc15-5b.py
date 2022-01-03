# AoC 2015 - Day 5b
import re

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def nice2(instr):
    return re.search(r"(..).*\1", instr) != None and re.search(r"(.).\1", instr) != None

def main():
    assert nice2('qjhvhtzxzqqjkmpb') == True
    assert nice2('xxyxx') == True
    assert nice2('uurcxstgmygtbstg') == False
    assert nice2('ieodomkazucvgmuy') == False
    indata = load_data()
    print(sum([1 for x in indata if nice2(x)]))

if __name__ == '__main__':
    main()
