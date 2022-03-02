def load_data():
    rules = []
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            start, stop = line.strip().split('-')
            rules.append((int(start), int(stop)))
    return sorted(rules)

def find_next_open(rules, x):
    while True:
        for r in rules:
            if r[0] <= x <= r[1]:
                x = r[1] + 1
            if r[0] > x:
                break
        return x

def sum_valid(n, rules):
    found = 0
    x = 1
    while x < 2**32:
        start = find_next_open(rules, x)
        found += 1
        x = start + 1
    return found - 1

def main():
    print(sum_valid(4294967295, load_data()))

if __name__ == '__main__':
    main()
