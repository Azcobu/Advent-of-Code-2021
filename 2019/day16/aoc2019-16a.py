# AoC 2019 Day 16a

def load_data():
    with open('input.txt') as infile:
        return infile.read().strip()

def gen_pattern(pos, reqlen):
    base = [0, 1, 0, -1]
    out = []

    for b in base:
        for p in range(pos + 1):
            out.append(b)
    while len(out) < reqlen + 1:
        out += out
    return out[1:]

def calc_fft(instr, phases):
    out = []
    patterns = {}

    for p in range(phases):
        out = []
        for pos, char in enumerate(instr):
            if pos not in patterns:
                patterns[pos] = gen_pattern(pos, len(instr))
            total = sum([int(x) * y for x, y in zip(instr, patterns[pos])])
            out.append(str(abs(total))[-1])
        instr = ''.join(out)

    return instr[:8]

def main():
    assert calc_fft('80871224585914546619083218645595', 100) == '24176176'
    assert calc_fft('19617804207202209144916044189917', 100) == '73745418'
    assert calc_fft('69317163492948606335995924319873', 100) == '52432133'
    print(calc_fft(load_data(), 100))

if __name__ == '__main__':
    main()
