# AoC 2017 - Day 4a

def load_data():
    with open('input.txt', 'r') as infile:
        return [line.strip().split() for line in infile.readlines()]

def count_valid(indata):
    valid = 0
    for line in indata:
        anags = [''.join(sorted(w)) for w in line]
        if len(anags) == len(set(anags)):
            valid += 1
    return valid

def main():
    print(count_valid(load_data()))

if __name__ == '__main__':
    main()
