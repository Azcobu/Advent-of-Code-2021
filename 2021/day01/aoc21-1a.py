# Advent of Code 2021 - 1a
# 1548

testinput = '199 200 208 210 200 207 240 269 260 263'.split()

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

def main():
    indata = load_data()
    assert count_increase(testinput) == 7
    result = count_increase(indata)
    print(result)

if __name__ == '__main__':
    main()
