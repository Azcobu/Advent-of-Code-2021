# Advent of Code 2023 Day 1b

def load_data() -> list:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return [x.strip() for x in infile.readlines()]

def main():
    digsum = 0
    data = load_data()
    digits = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x',\
              'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}

    for line in data:
        for k, v in digits.items():
            line = line.replace(k, v)

        line = [char for char in line if char.isdigit()]
        digsum += int(line[0] + line[-1])

    print(digsum)

if __name__ == '__main__':
    main()
