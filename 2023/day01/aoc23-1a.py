# Advent of Code 2023 Day 1a

def load_data() -> list:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        return [x.strip() for x in infile.readlines()]

def main():
    digsum = 0
    data = load_data()

    for d in data:
        d = [char for char in d if char.isdigit()]
        digsum += int(d[0] + d[-1])

    print(digsum)

if __name__ == '__main__':
    main()
