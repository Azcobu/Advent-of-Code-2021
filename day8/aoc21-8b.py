# Advent of Code 2021 8b

segments =  {'0':'abcefg', '1':'cf', '2':'acdeg', '3':'acdfg', '4':'bcdf', '5':'abdfg',
             '6':'abdefg', '7':'acf', '8':'abcdefg', '9':'abcdfg'}
segments = {k:set(v) for k, v in segments.items()}

def decode_line(inline):
    mapping = {}
    line, outstr = inline.split(' | ')

    for seg, target in {'b':6, 'e':4, 'f':9}.items():
        for letter in list('abcdefg'):
            if line.count(letter) == target:
                mapping[seg] = letter

    for seg, strlen in {'c':2, 'a':3, 'd':4}.items():
        digit = [x for x in line.split() if len(x) == strlen][0]
        mapping[seg] = [x for x in digit if x not in mapping.values()][0]

    mapping['g'] = [x for x in list('abcdefg') if x not in mapping.values()][0]
    decode = {v:k for k, v in mapping.items()}
    decoded_str = ''.join([decode[x] if x in decode else x for x in outstr])

    num = ''
    for digit in decoded_str.split(' '):
        for k, v in segments.items():
            if set(digit) == set(v):
                num += k
    return int(num)

def main():
    fname = 'aoc-8-input.txt'
    with open(fname, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    print(sum([decode_line(x) for x in data]))

if __name__ == '__main__':
    main()
