def load_data():
    rules = []
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            start, stop = line.strip().split('-')
            rules.append((int(start), int(stop)))
    return sorted(rules)

def find_lowest(n, rules):
    x = 1
    while True:
        for r in rules:
            if r[0] <= x <= r[1]:
                x = r[1] + 1
        return x

def main():
    print(find_lowest(4294967295, load_data()))

if __name__ == '__main__':
    main()
