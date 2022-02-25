# AoC 2016 - Day 16a

def gen_data(limit, instr):
    while len(instr) < limit:
        bstr = ''.join(['1' if x == '0' else '0' for x in instr[::-1]])
        instr = f'{instr}0{bstr}'
    return instr

def calc_checksum(data, limit):
    data = data[:limit]
    checksum = ''.join(['1' if x == y else '0' for x, y in zip(data[::2], data[1::2])])
    return checksum if len(checksum) % 2 else calc_checksum(checksum, limit)

def main():
    basedata = gen_data(272, '10001110011110000')
    print(calc_checksum(basedata, 272))

if __name__ == '__main__':
    main()
