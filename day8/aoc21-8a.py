# Advent of Code 2021 8a

def load_data():
    fname = r'D:\Python\Code\aoc21\aoc-8-input.txt'
    with open(fname, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]
    return data

def count_uniques(data):
    total = 0
    segs = [x.partition(' | ')[2] for x in data]
    segs = [x.split() for x in segs]
    for s in segs:
        total += sum([1 for x in s if len(x) in [2, 3, 4, 7]])
    return total

def main():
    data = load_data()
    u = count_uniques(data)
    print(u)


if __name__ == '__main__':
    main()
