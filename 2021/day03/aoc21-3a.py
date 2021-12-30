#Advent of Code 2021 - 3a

test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010']

def load_data():
    with open(r'd:\python\code\aoc21\aoc-3-input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]
    return indata

def calc_vals(indata):
    results = [0 for x in indata[0]]

    for item in indata:
        for pos, digit in enumerate(item):
            if digit == '1':
                results[pos] += 1

    gamma = ''.join(['1' if x > len(indata)/2 else '0' for x in results])
    epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])
    return int(gamma, 2), int(epsilon, 2)

def main():
    gam, eps = calc_vals(test)
    assert gam * eps == 198
    indata = load_data()
    gam, eps = calc_vals(indata)
    print(gam * eps)

if __name__ == '__main__':
    main()
