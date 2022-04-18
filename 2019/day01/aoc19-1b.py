# AoC 2019 - Day 1a

def load_data():
    with open('input.txt', 'r') as infile:
        return [int(x) for x in infile.readlines()]

def calc_fuel(data):
    total = []
    for base in data:
        add = base // 3 - 2
        total.append(add)
        while True:
            add = add // 3 - 2
            if add > 0:
                total.append(add)
            else:
                break
    return sum(total)

def main():
    print(calc_fuel(load_data()))

if __name__ == '__main__':
    main()
