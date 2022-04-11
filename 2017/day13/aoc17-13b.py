# AoC 2017 - Day 13b

def load_data():
    d = {}
    with open('input.txt', 'r') as infile:
        for l in infile.readlines():
            y = l.strip().split(': ')
            d[int(y[0])] = int(y[1])
    return d

def calc_safety(data, delay):
    for k, v in data.items():
        period = (v - 1) * 2
        if (k + delay) % period == 0 and (k + delay) % 2 == 0:
            return False
    return True

def calc_delay(data):
    x = 1
    while not calc_safety(data, x):
        x += 1
    return x

def main():
    assert calc_delay({0: 3, 1: 2, 4: 4, 6: 4}) == 10
    print(calc_delay(load_data()))


if __name__ == '__main__':
    main()