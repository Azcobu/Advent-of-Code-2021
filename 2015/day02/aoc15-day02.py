#AoC 2015 - Day 2

def calc_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def load_data():
    outdata = []
    with open('input.txt', 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    for x in data:
        y = [int(n) for n in x.split('x')]
        outdata.append(y)
    return outdata

def total(indata):
    return sum([calc_area(p[0], p[1], p[2]) for p in indata])

def main():
    assert calc_area(2, 3, 4) == 58
    assert calc_area(1, 1, 10) == 43
    data = load_data()
    print(total(data))

if __name__ == '__main__':
    main()
