# AoC 202 Day 13a

def load_data():
    with open('input.txt', 'r') as infile:
        d = infile.read().splitlines()
    start = int(d[0])
    buses = [int(x) for x in d[1].strip().split(',') if x != 'x']
    return start, buses

def find_next(start, buses):
    orig_start = start
    while True:
        for b in buses:
            if start % b == 0:
                return (start - orig_start) * b
        start += 1

def main():
    start, buses = load_data()
    print(find_next(start, buses))

if __name__ == '__main__':
    main()