# AoC 2020 Day 5a

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile.readlines()]

def bin_part(instr, start, end):
    pivot = (start + end) // 2 
    for c in instr:
        if c in ['F', 'L']:
            end = pivot
        else:
            start = pivot + 1
        pivot = (start + end) // 2 
    return start if c in ['F', 'L'] else end

def find_id(instr):
    return bin_part(instr[:7], 0, 127) * 8 + bin_part(instr[7:], 0, 7)

def find_high(data):
    return max([find_id(d) for d in data])

def main():
    #print(load_data())
    assert find_id('FBFBBFFRLR') == 357
    assert find_id('BFFFBBFRRR') == 567
    assert find_id('FFFBBBFRRR') == 119
    assert find_id('BBFFBBFRLL') == 820
    print(find_high(load_data()))

if __name__ == '__main__':
    main()