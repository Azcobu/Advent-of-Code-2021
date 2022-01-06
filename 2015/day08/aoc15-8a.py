# AoC 2015 - Day 8

def load_data():
    with open('input.txt', 'r') as infile:
        return [x.strip() for x in infile]

def calc_strlens(data):
    return sum([len(x) - len(eval(x)) for x in data])

def main():
    data = load_data()
    print(calc_strlens(data))

if __name__ == '__main__':
    main()
