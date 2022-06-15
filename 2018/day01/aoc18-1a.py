# AoC 2018 Day 1a

def load_data():
    freqs = []
    with open(r'input.txt', 'r') as infile:
        d = [x.strip() for x in infile.readlines()]
        return [int(x) if '-' in x else int(x) for x in d]

def main():
    d = load_data()
    print(sum(d))

if __name__ == '__main__':
    main()
