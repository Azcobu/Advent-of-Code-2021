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
        for monk in [x.strip() for x in infile.read().split('\n\n')]:
            lines = [x.strip() for x in monk.split('\n')]
            tmp_num = int(re.findall(r'\d+', lines[0])[0])
            tmp_items = [int(x) for x in re.findall(r'\d+', lines[1])]
            tmp_op = lines[2][17:]
            tmp_test = int(re.findall(r'\d+', lines[3])[0])
            tmp_true = int(re.findall(r'\d+', lines[4])[0])
            tmp_false = int(re.findall(r'\d+', lines[5])[0])
            data.append(Monkey(tmp_num, tmp_items, tmp_op, tmp_test, tmp_true, tmp_false))
    return data

def count_inspections(data):
    inspects = {}
    maxrounds = 20
    worry = 0

    for roundnum in range(maxrounds):
        for monk in data:
            inspects[monk.num] = inspects.get(monk.num, 0) + len(monk.items)
            while monk.items:
                old = monk.items.pop(0)
                worry = eval(monk.op) // 3
                throwto = monk.testtrue if worry % monk.test == 0 else monk.testfalse
                data[throwto].items.append(worry)

    x, y = sorted(inspects.values())[-2:]
    return x * y

def main():
    print(count_inspections(load_data()))

if __name__ == '__main__':
    main()
