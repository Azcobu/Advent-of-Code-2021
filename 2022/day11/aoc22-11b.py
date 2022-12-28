# AoC 2022 Day 11a
import re
from dataclasses import dataclass

@dataclass
class Monkey:
    num: int
    items: list
    op: str
    test: int
    testtrue: int
    testfalse: int

def load_data():
    data = []
    with open('input.txt', 'r') as infile:
        for monk in infile.read().split('\n\n'):
            lines = [x.strip() for x in monk.split('\n')]
            num = int(re.findall(r'\d+', lines[0])[0])
            items = [int(x) for x in re.findall(r'\d+', lines[1])]
            op = lines[2][17:]
            test = int(re.findall(r'\d+', lines[3])[0])
            true = int(re.findall(r'\d+', lines[4])[0])
            false = int(re.findall(r'\d+', lines[5])[0])
            data.append(Monkey(num, items, op, test, true, false))
    return data

def count_inspections(data):
    inspects = {}
    maxrounds = 10000
    mod = 1

    for x in data:
        mod *= x.test

    for roundnum in range(maxrounds):
        for monk in data:
            inspects[monk.num] = inspects.get(monk.num, 0) + len(monk.items)
            while monk.items:
                old = monk.items.pop(0)
                worry = eval(monk.op) % mod
                throwto = monk.testtrue if worry % monk.test == 0 else monk.testfalse
                data[throwto].items.append(worry)

    x, y = sorted(inspects.values())[-2:]
    return x * y

def main():
    print(count_inspections(load_data()))

if __name__ == '__main__':
    main()
