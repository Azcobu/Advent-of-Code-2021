# AoC 2020 Day 1b

def load_data():
    data = set()
    with open('input.txt', 'r') as infile:
        data = {int(x.strip()) for x in infile.readlines()}
    return data

def main():
    # x + y + z = 2020 so x + y = 2020 - z
    d = load_data()
    pairs = {x + y: (x, y) for x in d for y in d}
    for z in d:
        if 2020 - z in pairs:
            print(z * pairs[2020 - z][0] * pairs[2020 - z][1])
            return

if __name__ == '__main__':
    main()
