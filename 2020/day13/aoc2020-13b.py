# AoC 202 Day 13b

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    buses = {k:int(v) for k, v in enumerate(d[1].strip().split(',')) if v.isnumeric()}
    return buses

def find_next(buses):
    num = 0
    step = 1

    for offset, busnum in buses.items():
        while (num + offset) % busnum != 0:
            num += step
        step *= busnum
    return num

def main():
    buses = load_data()
    print(find_next(buses))

if __name__ == '__main__':
    main()