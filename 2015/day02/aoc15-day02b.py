#AoC 2015 - Day 2

def calc_ribbon(l, w, h):
    sides = sorted([l, w, h])
    return sides[0] * 2 + sides[1] * 2 + l * w * h

def load_data():
    outdata = []
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for x in data:
        y = [int(n) for n in x.split('x')]
        outdata.append(y)
    return outdata

def total(indata):
    return sum([calc_ribbon(p[0], p[1], p[2]) for p in indata])

def main():
    assert calc_ribbon(2, 3, 4) == 34
    assert calc_ribbon(1, 1, 10) == 14
    data = load_data()
    print(total(data))

if __name__ == '__main__':
    main()
