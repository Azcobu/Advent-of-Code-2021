# AoC 2019 - Day 1a

def calc():
    with open('input.txt', 'r') as infile:
        data = [int(x) for x in infile.readlines()]
    return sum(x // 3 - 2 for x in data)

def main():
    print(calc())

if __name__ == '__main__':
    main()
