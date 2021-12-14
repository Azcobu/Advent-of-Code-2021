#Advent of Code 2021 - 3b
# 2990784

test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010']

def load_data():
    with open(r'd:\python\code\aoc21\aoc-3-input.txt', 'r') as infile:
        indata = [x.strip() for x in infile.readlines()]
    return indata

def find_matching_values(inlist, pos, srchtype):
    zeroes = [x for x in inlist if x[pos] == '0']
    ones = [x for x in inlist if x[pos] == '1']
    if len(zeroes) > len(ones):
        return zeroes if srchtype == 'oxy' else ones
    else:
        return ones if srchtype == 'oxy' else zeroes

def calc_vals(indata):
    oxylist, co2list = indata[:], indata[:]
    for pos, x in enumerate(indata[0]):
        oxylist = find_matching_values(oxylist, pos, 'oxy')
        if len(oxylist) == 1: break
    for pos, x in enumerate(indata[0]):
        co2list = find_matching_values(co2list, pos, 'co2')
        if len(co2list) == 1: break
    return int(oxylist[0], 2), int(co2list[0], 2)

def main():
    oxy, co2 = calc_vals(test)
    assert oxy * co2 == 230
    indata = load_data()
    oxy, co2 = calc_vals(indata)
    print(oxy * co2)

if __name__ == '__main__':
    main()
