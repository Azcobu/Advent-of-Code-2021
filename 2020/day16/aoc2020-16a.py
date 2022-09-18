# AoC 2020 Day 16a
from parse import parse

def load_data():
    valid, tickets = [], []
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    for line in d:
        parsestr = '{}: {}-{} or {}-{}'
        if ' or ' in line:
            field, x1, x2, y1, y2 = parse(parsestr, line)
            valid += [(int(x1), int(x2)), (int(y1), int(y2))]
        elif ',' in line:
            tickets.append([int(x) for x in line.split(',')])
    return valid, tickets

def find_errors(valid, tickets):
    invalid = []
    for t in tickets[1:]:
        for num in t:
            for rule in valid:
                if rule[0] <= num <= rule[1]:
                    break
            else:
                invalid.append(num)
    return sum(invalid)

def main():
    print(find_errors(*load_data()))

if __name__ == '__main__':
    main()
