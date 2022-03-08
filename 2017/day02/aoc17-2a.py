# AoC 2017 - Day 2a

def load_data():
    with open('input.txt', 'r') as infile:
        return [[int(x) for x in line.split()] for line in infile.readlines()]

def calc_checksum(indata):
    return sum([max(l) - min(l) for l in indata])

def main():
    print(calc_checksum(load_data()))

if __name__ == '__main__':
    main()
