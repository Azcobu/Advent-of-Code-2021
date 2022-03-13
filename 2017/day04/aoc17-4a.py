# AoC 2017 - Day 4a

def load_data():
    with open('input.txt', 'r') as infile:
        return [line.strip().split() for line in infile.readlines()]

def count_valid(indata):
    return sum([1 for x in indata if len(x) == len(set(x))])

def main():
    print(count_valid(load_data()))

if __name__ == '__main__':
    main()
