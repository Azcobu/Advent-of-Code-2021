# AoC 2017 - Day 13a

def load_data():
    d = {}
    with open('input.txt', 'r') as infile:
        for l in infile.readlines():
            y = l.strip().split(': ')
            d[int(y[0])] = int(y[1])
    return d

def calc_severity(d):
    sev = 0
    for k, v in d.items():
        period = (v - 1) * 2
        if k % period == 0 and k % 2 == 0:
            sev += k * v
    return sev

def main():
    assert calc_severity({0: 3, 1: 2, 4: 4, 6: 4}) == 24
    print(calc_severity(load_data()))


if __name__ == '__main__':
    main()