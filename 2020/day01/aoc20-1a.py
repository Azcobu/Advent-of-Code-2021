# AoC 2020 Day 1a

def load_data():
    data = set()
    with open('input.txt', 'r') as infile:
        data = {int(x.strip()) for x in infile.readlines()}
    return data

def main():
    d = load_data()
    for x in d:
        if 2020 - x in d:
            print(x * (2020 - x))
            break

if __name__ == '__main__':
    main()
