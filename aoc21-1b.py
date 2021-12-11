# Advent of Code 2021 - 1b
# 1589

testinput = [int(x) for x in '199 200 208 210 200 207 240 269 260 263'.split()]

def load_data():
    with open(r'd:\python\code\aoc21\aoc-1a-input.txt', 'r') as infile:
        indata = [int(x.strip()) for x in infile.readlines()]
    return indata

def count_increase(indata):
    inc_count = 0

    for pos, point in enumerate(indata[:-1]):
        if point < indata[pos+1]:
            inc_count += 1
    return inc_count

def preprocess(indata):
    return [indata[pos] + indata[pos+1] + indata[pos+2] for pos, x in enumerate(indata[:-2])]

def main():
    indata = load_data()
    indata = preprocess(indata)
    result = count_increase(indata)
    print(result)
    assert count_increase(testinput) == 7

if __name__ == '__main__':
    main()
